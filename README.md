# Briefing-Agent

Ein persönlicher News-Briefing-Agent. Sammelt regelmäßig RSS-Feeds, filtert nach deinen Themen, lässt eine kurze Zusammenfassung schreiben und schickt dir das Ergebnis als Mail. Eine kleine, login-geschützte Webansicht zeigt das aktuelle und alle vergangenen Briefings.

## Wie es funktioniert

```
GitHub Actions (Cron werktags 7:00, samstags 9:00)
        │
        ▼
   briefing.py
   ├─ zieht alle Feeds aus themen.yml
   ├─ filtert Artikel nach deinen Themen-Keywords
   ├─ ruft GitHub Models pro Thema an für Zusammenfassung + Highlights
   ├─ schreibt JSON + Markdown nach web/data/briefings/
   ├─ commitet zurück ins Repo
   └─ schickt Mail über Resend
        │
        ▼
   Cloudflare Pages baut automatisch
        │
        ▼
   https://<projekt>.pages.dev   (geschützt durch Cloudflare Access)
```

## Was du anfasst

Im Alltag nur eine Datei: **`themen.yml`**. Dort stehen Themen, Keywords, Quellen und der Empfänger der Mail. Direkt im GitHub-Browser editierbar.

## Setup

Siehe **[SETUP.md](./SETUP.md)** — Schritt-für-Schritt-Anleitung, ca. 20 Min beim ersten Mal.

## Stack

- **GitHub Actions** — Scheduler, kostenlos in privaten Repos (~2000 Action-Minuten/Monat).
- **GitHub Models** — LLM (gpt-4o-mini), kostenlos via `permissions: models: read`.
- **Python 3.12** + `feedparser` + `requests` + `PyYAML` — kein Framework, ~270 Zeilen.
- **Resend** — E-Mail-Versand, Free Tier 100 Mails/Tag.
- **Cloudflare Pages** + **Cloudflare Access** — Hosting der Webansicht mit Login-Schutz, Free Tier.
- **Single-File HTML** — Webansicht ohne Build-Step, Vanilla JavaScript.

Keine Datenbank, kein Server, keine Container, keine Subscription außer GitHub-Account.

## Dateien

```
briefing-agent/
├─ themen.yml                        ← Konfig (deine Steuerzentrale)
├─ README.md
├─ SETUP.md                          ← Schritt-für-Schritt-Anleitung
├─ .github/workflows/briefing.yml    ← Cron-Schedule und Workflow
├─ agent/
│  ├─ briefing.py                    ← der gesamte Agent
│  └─ requirements.txt
└─ web/
   ├─ index.html                     ← Webansicht (single-file)
   └─ data/
      ├─ index.json
      └─ briefings/                  ← die einzelnen Briefings landen hier
```

## Lokaler Trockenlauf

```bash
DRY_RUN=1 python agent/briefing.py taeglich
```

Schreibt ein Briefing-Skelett, ohne LLM-Call und ohne Mail — gut zum Testen, ob die Feeds erreichbar sind und Treffer entstehen.
