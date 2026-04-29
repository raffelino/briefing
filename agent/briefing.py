#!/usr/bin/env python3
"""
Briefing-Agent — single-file.

Laeuft entweder online (GitHub Actions) oder lokal:

    python agent/briefing.py taeglich
    python agent/briefing.py woechentlich

Liest themen.yml, zieht alle Quellen, filtert Artikel nach Themen-Keywords,
laesst pro Thema mit GitHub Models eine kurze Zusammenfassung schreiben,
schreibt Markdown + JSON nach web/data/briefings/, aktualisiert den Index
und schickt das Ganze als Mail ueber Resend.

Erforderliche Umgebungsvariablen:
    GITHUB_TOKEN     — fuer GitHub Models (Actions liefert das automatisch).
                       Bei Fehlen: Skript laeuft im Mock-Modus ohne LLM.
    RESEND_API_KEY   — fuer den Mailversand. Bei Fehlen: keine Mail (Briefing
                       wird trotzdem erzeugt und ist ueber die Webansicht
                       verfuegbar).
    DRY_RUN=1        — Trockenlauf ohne LLM-Calls und ohne Mail (zum Testen).
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any

import feedparser
import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "themen.yml"
WEB_DATA = ROOT / "web" / "data"
BRIEFINGS_DIR = WEB_DATA / "briefings"
INDEX_FILE = WEB_DATA / "index.json"

GITHUB_MODELS_ENDPOINT = "https://models.github.ai/inference/chat/completions"
GITHUB_MODELS_MODEL = "openai/gpt-4o-mini"
RESEND_ENDPOINT = "https://api.resend.com/emails"
RESEND_FROM = "Briefing Agent <onboarding@resend.dev>"

USER_AGENT = "briefing-agent/1.0 (+https://github.com)"


# ---------------------------------------------------------------------------
# Konfig & Feeds
# ---------------------------------------------------------------------------

def load_config() -> dict[str, Any]:
    return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fetch_feeds(urls: list[str]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for url in urls:
        try:
            d = feedparser.parse(url, request_headers={"User-Agent": USER_AGENT})
            source = (d.feed.get("title") or url).strip()
            for e in d.entries[:40]:
                items.append({
                    "title": (e.get("title") or "").strip(),
                    "link": e.get("link") or "",
                    "summary": strip_html(e.get("summary") or e.get("description") or "")[:1200],
                    "published": e.get("published") or e.get("updated") or "",
                    "source": source,
                })
        except Exception as exc:  # noqa: BLE001
            print(f"[warn] feed-fehler {url}: {exc}", file=sys.stderr)
    print(f"[info] {len(items)} Roh-Items von {len(urls)} Feeds.", file=sys.stderr)
    return items


# ---------------------------------------------------------------------------
# Filterung
# ---------------------------------------------------------------------------

def parse_dt(s: str) -> dt.datetime | None:
    if not s:
        return None
    try:
        d = parsedate_to_datetime(s)
        if d.tzinfo is None:
            d = d.replace(tzinfo=dt.timezone.utc)
        return d
    except Exception:  # noqa: BLE001
        return None


def filter_items(
    items: list[dict[str, Any]],
    themen: list[dict[str, Any]],
    mode: str,
) -> dict[str, dict[str, Any]]:
    cutoff_hours = 30 if mode == "taeglich" else 24 * 7 + 6
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=cutoff_hours)

    by_topic: dict[str, dict[str, Any]] = {}
    seen_links: set[str] = set()

    # Sortieren: neueste zuerst (so dass die "wichtigsten N" oben stehen).
    items.sort(key=lambda it: parse_dt(it.get("published", "")) or dt.datetime.min.replace(tzinfo=dt.timezone.utc), reverse=True)

    for it in items:
        published = parse_dt(it.get("published", ""))
        if published and published < cutoff:
            continue

        link = it.get("link", "")
        if not link or link in seen_links:
            continue

        haystack = (it.get("title", "") + " " + it.get("summary", "")).lower()

        for t in themen:
            if any(kw.lower() in haystack for kw in t.get("keywords", [])):
                seen_links.add(link)
                bucket = by_topic.setdefault(t["id"], {
                    "id": t["id"],
                    "name": t["name"],
                    "items": [],
                })
                bucket["items"].append(it)
                break

    total = sum(len(b["items"]) for b in by_topic.values())
    print(f"[info] {total} Treffer in {len(by_topic)} Themen.", file=sys.stderr)
    return by_topic


# ---------------------------------------------------------------------------
# LLM
# ---------------------------------------------------------------------------

def llm_summarise(topic_name: str, items: list[dict[str, Any]], mode: str) -> dict[str, Any]:
    """Eine LLM-Anfrage pro Thema. Gibt {summary, highlights} zurueck."""
    token = os.environ.get("GITHUB_TOKEN")
    if not token or os.environ.get("DRY_RUN") == "1":
        return _mock_summary(topic_name, items, mode)

    if mode == "taeglich":
        instructions = (
            "Schreibe eine knappe Zusammenfassung dieses Themas in 2-3 Saetzen "
            "(max 60 Worte) und 3 prazise Highlight-Stichpunkte mit konkreten "
            "Fakten. Keine Floskeln, keine Werbung."
        )
    else:
        instructions = (
            "Schreibe einen Wochen-Recap zu diesem Thema in 4-6 Saetzen "
            "(max 120 Worte), in dem du die roten Faden und Trends "
            "herausarbeitest, plus 4-5 Highlight-Stichpunkte mit konkreten "
            "Fakten. Sachlich, kein Marketing."
        )

    item_blob = "\n\n".join(
        f"- TITEL: {it['title']}\n  QUELLE: {it['source']}\n  TEASER: {it['summary'][:600]}"
        for it in items[:10]
    )

    user_prompt = (
        f"Thema: {topic_name}\n\n"
        f"News-Items von heute:\n{item_blob}\n\n"
        f"{instructions}\n\n"
        "Antworte ausschliesslich als JSON in dieser Form:\n"
        '{"summary": "...", "highlights": ["...", "...", "..."]}'
    )

    body = {
        "model": GITHUB_MODELS_MODEL,
        "messages": [
            {"role": "system", "content": "Du bist ein praeziser deutschsprachiger News-Redakteur."},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0.3,
        "response_format": {"type": "json_object"},
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    for attempt in range(3):
        try:
            r = requests.post(GITHUB_MODELS_ENDPOINT, json=body, headers=headers, timeout=60)
            if r.status_code == 429:
                time.sleep(5 * (attempt + 1))
                continue
            r.raise_for_status()
            content = r.json()["choices"][0]["message"]["content"]
            data = json.loads(content)
            return {
                "summary": data.get("summary", "").strip(),
                "highlights": [h.strip() for h in data.get("highlights", []) if h.strip()],
            }
        except Exception as exc:  # noqa: BLE001
            print(f"[warn] LLM-Fehler ({attempt+1}/3) {topic_name}: {exc}", file=sys.stderr)
            time.sleep(2)
    return _mock_summary(topic_name, items, mode)


def _mock_summary(topic_name: str, items: list[dict[str, Any]], mode: str) -> dict[str, Any]:
    """Fallback ohne LLM — listet nur die ersten Titel."""
    return {
        "summary": f"({len(items)} Beitraege zu {topic_name} im Zeitraum — keine LLM-Zusammenfassung verfuegbar.)",
        "highlights": [it["title"] for it in items[:3]],
    }


# ---------------------------------------------------------------------------
# Render: Markdown + JSON
# ---------------------------------------------------------------------------

def render_markdown(briefing: dict[str, Any]) -> str:
    title = "Tagesbriefing" if briefing["mode"] == "taeglich" else "Wochen-Recap"
    md = [f"# {title} — {briefing['date']}", ""]
    if not briefing["topics"]:
        md.append("_Heute keine Treffer in deinen Themen._")
        return "\n".join(md)

    for t in briefing["topics"]:
        md.append(f"## {t['name']}")
        md.append("")
        if t.get("summary"):
            md.append(t["summary"])
            md.append("")
        for h in t.get("highlights", []):
            md.append(f"- {h}")
        if t.get("highlights"):
            md.append("")
        md.append("**Artikel:**")
        for it in t["items"]:
            md.append(f"- [{it['title']}]({it['link']}) — _{it['source']}_")
        md.append("")
    return "\n".join(md)


def markdown_to_html(md: str) -> str:
    """Mini-Renderer, damit wir keine zusaetzliche Lib brauchen."""
    out = []
    for line in md.splitlines():
        if line.startswith("# "):
            out.append(f"<h1>{line[2:].strip()}</h1>")
        elif line.startswith("## "):
            out.append(f"<h2>{line[3:].strip()}</h2>")
        elif line.startswith("- "):
            content = line[2:].strip()
            content = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', content)
            content = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", content)
            content = re.sub(r"_([^_]+)_", r"<em>\1</em>", content)
            out.append(f"<li>{content}</li>")
        elif not line.strip():
            out.append("")
        else:
            content = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', line)
            content = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", content)
            out.append(f"<p>{content}</p>")
    # <li> in <ul> einwickeln (simpel, fuer mehrere aufeinanderfolgende):
    html = "\n".join(out)
    html = re.sub(r"(<li>[\s\S]*?</li>)(\s*<li>[\s\S]*?</li>)+", lambda m: f"<ul>{m.group(0)}</ul>", html)
    html = re.sub(r"(<li>[\s\S]*?</li>)(?!\s*<li)", r"<ul>\1</ul>", html)
    return html


# ---------------------------------------------------------------------------
# Mail
# ---------------------------------------------------------------------------

def send_mail(cfg: dict[str, Any], date: str, mode: str, md: str) -> None:
    api_key = os.environ.get("RESEND_API_KEY")
    if not api_key or os.environ.get("DRY_RUN") == "1":
        print("[info] kein RESEND_API_KEY (oder DRY_RUN) — Mailversand uebersprungen.", file=sys.stderr)
        return

    week = dt.date.fromisoformat(date).isocalendar().week
    template = cfg["email"][f"betreff_{mode}"]
    subject = template.format(date=date, week=f"{week:02d}")
    recipient = cfg["email"]["empfaenger"]

    html_body = (
        "<div style=\"font-family:-apple-system,Segoe UI,sans-serif;max-width:680px;\">"
        + markdown_to_html(md)
        + "</div>"
    )

    payload = {
        "from": RESEND_FROM,
        "to": [recipient],
        "subject": subject,
        "html": html_body,
        "text": md,
    }

    r = requests.post(
        RESEND_ENDPOINT,
        json=payload,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        timeout=30,
    )
    if r.status_code >= 400:
        print(f"[error] Resend antwortete {r.status_code}: {r.text}", file=sys.stderr)
    else:
        print(f"[info] Mail versendet an {recipient}.", file=sys.stderr)


# ---------------------------------------------------------------------------
# Index
# ---------------------------------------------------------------------------

def update_index() -> None:
    files = sorted(BRIEFINGS_DIR.glob("*.json"), reverse=True)
    idx = []
    for f in files:
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
            idx.append({
                "date": d.get("date", ""),
                "mode": d.get("mode", ""),
                "file": f.name,
                "topic_count": len(d.get("topics", [])),
            })
        except Exception:  # noqa: BLE001
            continue
    INDEX_FILE.write_text(json.dumps(idx, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(mode: str) -> None:
    if mode not in ("taeglich", "woechentlich"):
        raise SystemExit(f"Modus '{mode}' unbekannt — taeglich oder woechentlich erwartet.")

    cfg = load_config()

    items = fetch_feeds(cfg["quellen"])
    by_topic = filter_items(items, cfg["themen"], mode)

    limit_key = "artikel_pro_thema_taeglich" if mode == "taeglich" else "artikel_pro_thema_woechentlich"
    limit = int(cfg.get("limits", {}).get(limit_key, 5))

    # Themen in Konfig-Reihenfolge ausgeben (nicht alphabetisch).
    ordered_topics = []
    for t in cfg["themen"]:
        bucket = by_topic.get(t["id"])
        if not bucket:
            continue
        bucket["items"] = bucket["items"][:limit]
        result = llm_summarise(t["name"], bucket["items"], mode)
        bucket.update(result)
        ordered_topics.append(bucket)

    today = dt.date.today().isoformat()
    briefing = {"date": today, "mode": mode, "topics": ordered_topics}

    BRIEFINGS_DIR.mkdir(parents=True, exist_ok=True)
    json_file = BRIEFINGS_DIR / f"{today}-{mode}.json"
    md_file = BRIEFINGS_DIR / f"{today}-{mode}.md"
    json_file.write_text(json.dumps(briefing, ensure_ascii=False, indent=2), encoding="utf-8")
    md = render_markdown(briefing)
    md_file.write_text(md, encoding="utf-8")
    update_index()

    send_mail(cfg, today, mode, md)
    print(f"[ok] Briefing geschrieben: {json_file.relative_to(ROOT)}", file=sys.stderr)


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "taeglich"
    main(arg)
