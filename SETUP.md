# Setup — in 4 Schritten online

Geschätzte Zeit beim ersten Mal: ca. 20 Minuten. Danach nie wieder.

Du brauchst nichts zu installieren. Alle Schritte sind Klicks im Browser.

---

## Schritt 1 — GitHub-Repo anlegen und Dateien hochladen

1. Auf <https://github.com> einloggen (oder kostenlos registrieren).
2. Oben rechts auf das **+**-Icon → **New repository** klicken.
3. Eintragen:
   - **Repository name:** `briefing` (oder beliebig)
   - **Privacy:** **Private** anklicken
   - Haken bei „Add a README" **nicht** setzen (wir laden eines hoch)
4. **Create repository** klicken.

Jetzt die Dateien hochladen:

5. Auf der nächsten Seite siehst du den Hinweis „uploading an existing file" — klicken.
6. Im Finder den Ordner `briefing-agent` öffnen, **alle Inhalte markieren** (Cmd+A) und ins Browserfenster ziehen. Wichtig: nicht den Ordner selbst, sondern die **Dateien darin**.
7. Unten **Commit changes** klicken.

GitHub zeigt jetzt deine Datei-Liste. Der Workflow ist live — er läuft beim nächsten Cron-Termin von allein, oder du startest ihn jetzt manuell (siehe Schritt 4 unten).

---

## Schritt 2 — Resend für E-Mail einrichten

Resend verschickt deine Briefings als Mail. Free Tier: 100 Mails/Tag. Mehr als genug.

1. Auf <https://resend.com> registrieren (geht mit GitHub-Login in 30 Sekunden).
2. Im Dashboard links: **API Keys** → **Create API Key**.
3. Name vergeben („briefing"), **Permission: Sending access**, **Create**.
4. Den Key kopieren (beginnt mit `re_…`). **Wichtig:** der wird nur einmal angezeigt.

Den Key in GitHub als Secret hinterlegen:

5. In deinem GitHub-Repo: oben **Settings** → links **Secrets and variables** → **Actions**.
6. **New repository secret** klicken.
7. **Name:** `RESEND_API_KEY` — **Secret:** den `re_…`-Key einfügen — **Add secret**.

Hinweis: Resend nutzt im Free-Tier die Test-Absenderadresse `onboarding@resend.dev`, die ausschließlich an die E-Mail des Resend-Accounts liefert. Da du dich als `raffelino666@googlemail.com` registrierst und in der `themen.yml` denselben Empfänger eingetragen hast, geht das ohne Domain-Verifikation. Wenn du später eine eigene Absender-Domain möchtest, kannst du das in Resend nachholen.

---

## Schritt 3 — Cloudflare Pages mit Access für die Webansicht

Die Webansicht soll erreichbar sein, aber nur für dich — deshalb mit Login-Schutz (Cloudflare Access). Free Tier reicht für bis zu 50 Nutzer.

### 3a. Cloudflare-Account erstellen

1. <https://dash.cloudflare.com/sign-up> — kostenlos registrieren, E-Mail bestätigen.

### 3b. Pages-Projekt aus dem GitHub-Repo bauen

2. Im Cloudflare-Dashboard links: **Workers & Pages** → **Create** → Tab **Pages** → **Connect to Git**.
3. **GitHub** auswählen, App autorisieren — bei **Repository access** auf **Only select repositories** das `briefing`-Repo zulassen.
4. Repo auswählen → **Begin setup**.
5. Build-Einstellungen:
   - **Project name:** `briefing` (frei wählbar; ergibt deine URL)
   - **Production branch:** `main`
   - **Framework preset:** *None*
   - **Build command:** **leer lassen**
   - **Build output directory:** `web`
6. **Save and Deploy**.

Nach ~30 Sekunden ist die Seite unter `https://<projektname>.pages.dev` erreichbar — aber noch öffentlich. Das fixen wir jetzt.

### 3c. Cloudflare Access aktivieren (Login-Schutz)

7. Im Cloudflare-Dashboard links **Zero Trust** wählen (öffnet das Zero-Trust-Dashboard in neuem Tab). Beim ersten Mal: Team-Domain wählen (z.B. `raffel`), Free-Plan auswählen.
8. Im Zero-Trust-Dashboard: **Access** → **Applications** → **Add an application** → **Self-hosted**.
9. Eintragen:
   - **Application name:** `briefing`
   - **Subdomain:** dein Pages-Projektname (z.B. `briefing`)
   - **Domain:** `pages.dev`
   - **Path:** leer
10. **Next**.
11. **Policy name:** `nur ich` — **Action:** *Allow* — **Configure rules:** unter „Include" wählen: **Emails** → `raffelino666@googlemail.com`.
12. **Next** → **Add application**.

Beim nächsten Aufruf von `https://<projektname>.pages.dev` musst du dich per E-Mail-Code anmelden. Niemand sonst kommt rein.

---

## Schritt 4 — Erster Test-Lauf

1. Ins GitHub-Repo gehen → Tab **Actions** → links **Briefing** → rechts **Run workflow** → **Run workflow** (Modus `taeglich` ist Default).
2. ~1 Minute warten. Grüner Haken = erfolgreich.
3. E-Mail-Postfach checken — dein erstes Briefing sollte angekommen sein.
4. `https://<projektname>.pages.dev` öffnen — nach Login siehst du dasselbe Briefing als Webansicht.

Cloudflare Pages baut bei jedem zukünftigen Commit (also: bei jedem neuen Briefing) automatisch neu. Du musst nichts mehr tun.

---

## Tägliche Nutzung danach

| Was du willst | Was du tust |
|---|---|
| Briefing lesen | Mail öffnen, oder die Pages-URL aufrufen. |
| Themen ändern | `themen.yml` im Repo öffnen, Bleistift-Icon, tippen, **Commit changes**. |
| Quelle ergänzen | Genau wie oben — neue Zeile unter `quellen:` einfügen. |
| Takt verschieben | `.github/workflows/briefing.yml` öffnen, die `cron`-Zeile editieren. Cron-Hilfe: <https://crontab.guru> |
| Pause machen | Im Repo: **Actions** → **Briefing** → rechts **`...`** → **Disable workflow**. Wieder anwerfen genauso. |
| Manuell ein Briefing erzwingen | **Actions** → **Briefing** → **Run workflow**. |

---

## Lokal laufen (optional, falls du mal offline testen willst)

```bash
cd briefing-agent
python3 -m venv .venv && source .venv/bin/activate
pip install -r agent/requirements.txt

# Trockenlauf ohne LLM und ohne Mail (zum Schauen, was rauskommt):
DRY_RUN=1 python agent/briefing.py taeglich

# Echter Lauf (braucht GitHub Personal Access Token mit models:read und Resend-Key):
export GITHUB_TOKEN=ghp_…
export RESEND_API_KEY=re_…
python agent/briefing.py taeglich

# Webansicht ansehen:
cd web && python3 -m http.server 8000
# dann http://localhost:8000 im Browser
```

---

## Wenn was hakt

| Symptom | Wahrscheinlich | Fix |
|---|---|---|
| Workflow läuft, aber keine Mail | `RESEND_API_KEY`-Secret fehlt oder Tippfehler | Schritt 2 prüfen, exakt der Name `RESEND_API_KEY` |
| Mail kommt nicht in Inbox | Spam-Ordner | Absender `onboarding@resend.dev` whitelisten |
| Keine Treffer / leeres Briefing | Themen-Keywords passen nicht zur Tagesnews | `themen.yml` — mehr Keywords pro Thema, oder weiter gefasst |
| Cloudflare-Build-Fehler | Output-Dir falsch | In Pages-Settings: **Build output directory** = `web` |
| LLM-Antwort fehlt im Briefing | Rate Limit GitHub Models | Workflow später nochmal anwerfen, oder Themen reduzieren |
| GitHub Models 401 | `permissions: models: read` fehlt im Workflow | Workflow-Datei prüfen — bei dir bereits korrekt drin |
