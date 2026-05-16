# Wochen-Recap — 2026-05-16

## Data & AI / Data Science

In dieser Woche standen bei Data & AI insbesondere Herausforderungen und Entwicklungen im Bereich der Datenverarbeitung im Fokus. Pinterest hat erfolgreich CPU-Störungen in seiner Kubernetes-basierten Plattform PinCompute behoben, die die Leistung von Machine-Learning-Jobs beeinträchtigten. Gleichzeitig betonte Fivetrans CPO die Notwendigkeit offener Datenarchitekturen, um der steigenden Komplexität durch AI-Agenten gerecht zu werden. Diese Themen verdeutlichen die Wichtigkeit von Systemverständnis und Flexibilität in der Datenverarbeitung.

- Pinterest löste CPU-Störungen durch Deaktivierung eines ungenutzten Amazon ECS-Agenten.
- Die Stabilisierung der Leistung auf PinCompute verbesserte die Effizienz von Machine-Learning-Jobs.
- Fivetran warnt, dass geschlossene Datenstacks in der Ära von AI-Agenten nicht überlebensfähig sind.
- AI-Agenten können die Anzahl der Abfragen in einem Data Warehouse erheblich steigern.
- Das Verständnis von Systemstandards ist entscheidend für effektives Troubleshooting.

**Artikel:**
- [Pinterest Engineers Eliminate CPU Zombies to Resolve Production Bottlenecks](https://www.infoq.com/news/2026/05/pinterest-cpu-zombies-bottleneck/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global) — _InfoQ_
- [Fivetran’s CPO: Closed data stacks won’t survive the agent era](https://thenewstack.io/agentic-analytics-cost-squeeze/) — _The New Stack_

## Cloud-Architektur & Plattformen

In dieser Woche dominierten Entwicklungen in der Cloud-Architektur und Plattformen, wobei Unternehmen wie Google und Microsoft bedeutende Neuerungen präsentierten. Google stellte die Cloud Fraud Defense vor, die über die Bot-Erkennung hinausgeht, während Microsoft mit Aspire 13.3 wichtige Updates für die Bereitstellung in Azure und Kubernetes einführte. Zudem wurde die Bedeutung von Softwareanforderungen und deren Bugs durch AWS hervorgehoben, während Kubernetes mit Version 1.36 Sicherheits- und AI-Workload-Verbesserungen umsetzte.

- Google Cloud Fraud Defense als Nachfolger von reCAPTCHA zur Bekämpfung von Online-Betrug vorgestellt.
- Microsofts Aspire 13.3 führt neue Befehle für die Bereitstellung in Azure und Kubernetes ein.
- AWS identifiziert Bugs in 60% der Softwareanforderungen und setzt auf einen 50 Jahre alten Logik-Engine zur Behebung.
- Kubernetes v1.36 veröffentlicht mit 70 Verbesserungen, darunter Sicherheits- und AI-Workload-Unterstützung.

**Artikel:**
- [Google Introduces Cloud Fraud Defense as Successor to reCAPTCHA](https://www.infoq.com/news/2026/05/cloud-fraud-defense-recaptcha/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global) — _InfoQ_
- [Microsoft Releases Aspire 13.3 with Major Deployment and Frontend Updates](https://www.infoq.com/news/2026/05/aspire-13-3-release/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global) — _InfoQ_
- [Why Block handed Goose to the Linux Foundation](https://thenewstack.io/block-goose-agentic-foundation/) — _The New Stack_
- [AWS found bugs in 60% of software requirements. Its fix isn’t more AI — it’s a 50-year-old logic engine.](https://thenewstack.io/kiro-requirements-analysis-automated-reasoning/) — _The New Stack_
- [GTA 6 kurz vor dem Start? Warum die Börse schon einmal feiert](https://t3n.de/news/gta-6-start-boerse-feiern-1742633/?utm_source=rss&utm_medium=newsFeed&utm_campaign=newsFeed) — _t3n.de - News_
- [Benchmarking AI Agents on Kubernetes](https://www.infoq.com/news/2026/05/ai-agents-kubernetes-rag/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global) — _InfoQ_
- [Anthropic Traces Six Weeks of Claude Code Quality Complaints to Three Overlapping Product Changes](https://www.infoq.com/news/2026/05/anthropic-claude-code-postmortem/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global) — _InfoQ_
- [Kubernetes v1.36 Released: Security Defaults Tighten as AI Workload Support Matures](https://www.infoq.com/news/2026/05/kubernetes-1-36-released/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global) — _InfoQ_

## Software-Architektur & Java

In der vergangenen Woche standen Entwicklungen in der Software-Architektur und Java im Fokus. Besonders hervorzuheben ist die zunehmende Bedeutung von API-Design und -Entwicklung, wie ein Workshop von heise zeigt. Zudem wurde die Portierung des Bun-Servers von JavaScript/TypeScript nach Rust thematisiert, was auf einen Trend zur Effizienzsteigerung hinweist. Schließlich wird die Foreign Function & Memory API als moderne Alternative zum veralteten JNI in Java vorgestellt, um den Zugriff auf C-Libraries zu erleichtern.

- Workshop zu API-Design und -Entwicklung mit Fokus auf HTTP, REST und OpenAPI.
- Bun-Server wird von JavaScript/TypeScript nach Rust portiert, um die Codebasis zu optimieren.
- Foreign Function & Memory API bietet vereinfachten Zugang zu C-Libraries in Java.
- Veraltetes JNI wird durch moderne Ansätze ersetzt, um die Interoperabilität zu verbessern.

**Artikel:**
- [heise-Angebot: iX-Workshop: API-Design und -Entwicklung mit HTTP, REST und OpenAPI](https://www.heise.de/news/iX-Workshop-API-Design-und-Entwicklung-mit-HTTP-REST-und-OpenAPI-11142307.html?wt_mc=rss.red.ho.ho.atom.beitrag.beitrag) — _heise online News_
- [KI-Portierung: Claude schreibt Bun-Codebasis in Rust neu](https://www.heise.de/news/KI-Portierung-Claude-schreibt-Bun-Codebasis-in-Rust-neu-9787350.html) — _heise developer News_
- [C-Libraries in Java nutzen 2: Funktionen mit veränderlichen Parametern](https://www.heise.de/hintergrund/C-Libraries-in-Java-nutzen-2-Funktionen-mit-veraenderlichen-Parametern-11291161.html) — _heise developer News_

## IT-Sicherheit & Security by Design

In dieser Woche standen IT-Sicherheit und die Implementierung von Security by Design im Fokus. OpenAI stellte seine neue Cybersecurity-Initiative Daybreak vor, die auf GPT-5.5 basiert und eine tiered access framework sowie Codex Security umfasst. Zudem bietet heise einen Workshop an, der Unternehmen bei der strategischen Reaktion auf Ransomware-Angriffe unterstützt. Diese Entwicklungen verdeutlichen die wachsende Bedeutung von proaktiven Sicherheitsmaßnahmen und strategischer Kommunikation im Umgang mit Cyber-Bedrohungen.

- OpenAI lanciert Daybreak, eine Cybersecurity-Initiative mit GPT-5.5.
- Daybreak umfasst ein tiered access framework und Codex Security.
- Anthropic's Glasswing zeigt ähnliche Benchmarks und Partner wie OpenAI.
- heise bietet einen Workshop zur strategischen Reaktion auf Ransomware-Angriffe an.
- Fokus auf proaktive Sicherheitsmaßnahmen und strategische Kommunikation.

**Artikel:**
- [OpenAI’s Daybreak and Anthropic’s Glasswing have nearly identical benchmarks — and 3 of the same partners](https://thenewstack.io/openai-daybreak-anthropic-glasswing/) — _The New Stack_
- [heise-Angebot: iX-Workshop: Nach dem Ransomware-Angriff – sicher entscheiden und kommunizieren](https://www.heise.de/news/iX-Workshop-Nach-dem-Ransomware-Angriff-sicher-entscheiden-und-kommunizieren-11280571.html?wt_mc=rss.red.ho.ho.atom.beitrag.beitrag) — _heise online News_

## Agile Methoden & UX/UI

In dieser Woche standen agile Methoden und UX/UI im Kontext der Digitalisierung und der damit verbundenen Herausforderungen im Fokus. Die Diskussion über den Digitalzwang und das Recht auf ein analoges Leben zeigt, dass die Balance zwischen digitalen und analogen Erfahrungen zunehmend wichtig wird. Gleichzeitig wird die Notwendigkeit praxistauglicher Digitalisierung in verschiedenen Bereichen, wie der Medizin, betont, um die Nutzererfahrung zu verbessern und Bürokratie abzubauen.

- 64.000 Menschen fordern das Recht auf analoges Leben im Grundgesetz.
- Ärztetag unterstützt Digitalisierung, wenn sie Ärzte entlastet und Patienten schützt.
- Wissenschaftlicher Dienst des EP warnt vor Anonymitätsverlust durch VPN-Regulierungen.
- Fedora Hummingbird Linux bringt eine neue containerbasierte Distribution auf den Markt.

**Artikel:**
- [Neuer Job als Head of Online Marketing &amp;amp; Growth gesucht? Schau dir unsere Top Jobs an](https://t3n.de/news/unsere-jobs-der-woche-1175973/?utm_source=rss&utm_medium=newsFeed&utm_campaign=newsFeed) — _t3n.de - News_
- [Petition gegen Digitalzwang: 64.000 Menschen wollen das Grundgesetz ändern](https://netzpolitik.org/2026/petition-gegen-digitalzwang-64-000-menschen-wollen-das-grundgesetz-aendern/) — _netzpolitik.org_
- [Wissenschaftlicher Dienst des EP: Wer Kinder ausschließen will, muss Anonymität verbieten](https://netzpolitik.org/2026/wissenschaftlicher-dienst-des-ep-wer-kinder-ausschliessen-will-muss-anonymitaet-verbieten/) — _netzpolitik.org_
- [Privilegienausweitung in Linux: Lokale Nutzer können fremde Dateien lesen](https://www.heise.de/news/Privilegienausweitung-in-Linux-Lokale-Nutzer-koennen-fremde-Dateien-lesen-11295751.html?wt_mc=rss.red.ho.ho.atom.beitrag.beitrag) — _heise online News_
- [Fedora Hummingbird Linux: Neue Container-basierte Distribution](https://www.heise.de/news/Fedora-Hummingbird-Linux-Neue-Container-basierte-Distribution-11295489.html?wt_mc=rss.red.ho.ho.atom.beitrag.beitrag) — _heise online News_
- [„Fragnesia“: Nächste Rechteausweitungslücke im Linux-Kernel](https://www.heise.de/news/Fragnesia-Microsoft-warnt-vor-weiterer-Rechteausweitungsluecke-in-Linux-11294817.html?wt_mc=rss.red.ho.ho.atom.beitrag.beitrag) — _heise online News_
- [heise-Angebot: c’t-Webinar: Keine Angst vor Linux – so klappt der Wechsel](https://www.heise.de/news/c-t-Webinar-Keine-Angst-vor-Linux-so-klappt-der-Wechsel-11285784.html?wt_mc=rss.red.ho.ho.atom.beitrag.beitrag) — _heise online News_
- [Ärztetag fordert praxistaugliche Digitalisierung & Änderungen der Notfallreform](https://www.heise.de/news/Aerztetag-fordert-praxistaugliche-Digitalisierung-Aenderungen-der-Notfallreform-11294681.html?wt_mc=rss.red.ho.ho.atom.beitrag.beitrag) — _heise online News_

## Generative KI & LLMs

In dieser Woche standen generative KI und LLMs im Fokus, insbesondere die Herausforderungen in Bezug auf Privatsphäre und Unternehmensnutzung. Viele Unternehmen setzen KI-Agenten ein, ohne deren Überwachung zu gewährleisten, was zu technischen Altlasten führt. Zudem zeigen neue Entwicklungen bei Anthropic und Cloudflare, wie KI-Tools zunehmend in die Softwareentwicklung integriert werden. Gleichzeitig gibt es kritische Stimmen zur Integration von KI in bestehende Systeme, wie im Fall von Microsoft und Apple.

- Über 50% der KI-Agenten in Unternehmen werden nicht überwacht.
- Sprachmodelle wie ChatGPT stellen eine Herausforderung für die Privatsphäre dar.
- Anthropic führt Routines für automatisierte Codierung ein.
- Microsoft zieht Claude Code nach kurzer Zeit zurück.
- Cloudflare präsentiert Workflows V2 mit 50.000 gleichzeitigen Instanzen.

**Artikel:**
- [Agent Sprawl: Warum Unternehmen gerade KI-Altlasten produzieren – ohne es zu merken](https://t3n.de/news/agent-sprawl-ki-altlasten-unternehmen-1741167/?utm_source=rss&utm_medium=newsFeed&utm_campaign=newsFeed) — _t3n.de - News_
- [KI gegen die Privatsphäre: Wenn Sprachmodelle zu viel wissen – und wie sie es verraten](https://t3n.de/news/ki-gegen-die-privatsphaere-wenn-sprachmodelle-zu-viel-wissen-und-wie-sie-es-verraten-1742662/?utm_source=rss&utm_medium=newsFeed&utm_campaign=newsFeed) — _t3n.de - News_
- [Anthropic’s $1.5B copyright settlement is getting messy as judge delays approval](https://arstechnica.com/tech-policy/2026/05/authors-fight-for-higher-payouts-from-anthropics-1-5b-copyright-settlement/) — _Ars Technica - All content_
- [OpenAI feels “burned” by Apple’s crappy ChatGPT integration, insiders say](https://arstechnica.com/tech-policy/2026/05/openai-feels-burned-by-apples-crappy-chatgpt-integration-insiders-say/) — _Ars Technica - All content_
- [Anthropic Introduces Routines for Claude Code Automation](https://www.infoq.com/news/2026/05/anthropic-routines-claude/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global) — _InfoQ_
- [Nur wenige Monate nach Einführung: Warum Microsoft seinen Entwicklern Claude Code wieder wegnimmt](https://t3n.de/news/microsoft-nimmt-entwicklern-claude-code-nach-monaten-wieder-weg-1742686/?utm_source=rss&utm_medium=newsFeed&utm_campaign=newsFeed) — _t3n.de - News_
- [Cloudflare Introduces Workflows V2 with Deterministic Execution and 50K Concurrent Workflows](https://www.infoq.com/news/2026/05/cloudflare-workflows-v2-release/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global) — _InfoQ_
- [Ein Viertel durchsucht heimlich das Smartphone des Partners: Welche Gründe stecken dahinter?](https://t3n.de/news/ein-viertel-durchsucht-heimlich-das-smartphones-partners-welche-gruende-stecken-dahinter-1742665/?utm_source=rss&utm_medium=newsFeed&utm_campaign=newsFeed) — _t3n.de - News_

## EU-Tech-Regulierung

In dieser Woche standen technische Herausforderungen und Fortschritte im Fokus der Tech-Branche. Discord veröffentlichte eine Analyse zu einem massiven Ausfall seiner Sprachdienste, der durch eine unentdeckte zirkuläre Abhängigkeit in der Infrastruktur verursacht wurde. Gleichzeitig verzeichnete das Unternehmen Temporal einen Anstieg auf 3.000 zahlende Kunden für seine ausfallsichere Workflow-Engine, was auf ein wachsendes Interesse an stabilen und zuverlässigen Softwarelösungen hinweist. Diese Entwicklungen spiegeln die Notwendigkeit wider, technische Systeme robuster zu gestalten, um Ausfälle zu vermeiden.

- Discord erlitt am 25. März 2026 einen massiven Sprachdienstausfall.
- Der Ausfall wurde durch eine zirkuläre Abhängigkeit in der Infrastruktur ausgelöst.
- Temporal hat nun 3.000 zahlende Kunden für seine Workflow-Engine.
- Die Nachfrage nach stabilen Softwarelösungen wächst in der Branche.

**Artikel:**
- [Discord Reveals How a Hidden Circular Dependency Triggered Its March Voice Outage](https://www.infoq.com/news/2026/05/discord-circular-dependency/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global) — _InfoQ_
- [Temporal hits 3,000 paying customers with its crash-proof workflow engine](https://thenewstack.io/temporal-durable-execution-ai-workflows/) — _The New Stack_

## Platform Engineering / IDPs

In der aktuellen Woche hat SolidJS die Beta-Version 2.0 veröffentlicht, die wesentliche Verbesserungen in der Handhabung von asynchronen Prozessen und Reaktivität bietet. Besonders hervorzuheben ist die Einführung von Async als erstklassiges Feature, das die direkte Nutzung von Promises innerhalb des Frameworks ermöglicht. Diese Änderungen zielen darauf ab, die Entwicklererfahrung zu optimieren und gleichzeitig die feingranulare Reaktivität ohne ein virtuelles DOM beizubehalten. Die Aktualisierung bringt auch neue Primitiven für Mutationen und verändert die Zustandsverwaltung, was zu signifikanten Breaking Changes führt.

- Einführung von Async als erstklassiges Feature in SolidJS 2.0 Beta.
- Direkte Nutzung von Promises innerhalb des Frameworks möglich.
- Neue Primitiven für Mutationen implementiert.
- Veränderte Zustandsverwaltung mit signifikanten Breaking Changes.
- Ziel: Verbesserung der Entwicklererfahrung bei gleichzeitiger Beibehaltung feingranularer Reaktivität.

**Artikel:**
- [SolidJS 2.0 Beta: First-Class Async, Reworked Suspense and Deterministic Batching](https://www.infoq.com/news/2026/05/solidjs-2-async/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global) — _InfoQ_

## Open Source & Software Supply Chain

In der vergangenen Woche wurde die Bedeutung von KI und deren Einfluss auf verschiedene Bereiche deutlich. Während Universitäten wie Princeton Maßnahmen gegen KI-Betrug ergreifen, warnen Forscher von Microsoft vor den Risiken der KI-Nutzung bei der Bearbeitung großer Dokumente. Zudem zeigt sich, dass Remote Work durch fehlende Prozesse behindert wird, was die Notwendigkeit effektiver Tools unterstreicht. Die Entwicklungen im Bereich der digitalen Kommunikation und Datenschutz, wie die Einführung eines Inkognitomodus für Meta AI in WhatsApp, verdeutlichen den Trend zu mehr Privatsphäre im digitalen Raum.

- Princeton bricht Tradition gegen KI-Betrug.
- Microsoft warnt vor Datenverfälschung durch KI bei großen Dokumenten.
- Remote Work leidet unter fehlenden Prozessen.
- Meta führt Inkognitomodus für private Chats mit KI in WhatsApp ein.
- Konsolenpreise steigen bei Sony und Nintendo.

**Artikel:**
- [In Princeton durften Studierende 133 Jahre lang ohne Aufsicht Prüfungen schreiben: KI ändert das jetzt](https://t3n.de/news/princeton-studierende-133-jahre-ohne-aufsicht-pruefungen-ki-aendert-das-1742651/?utm_source=rss&utm_medium=newsFeed&utm_campaign=newsFeed) — _t3n.de - News_
- [KW 20: Die Woche, in der die Anonymität im Netz noch mehr ins Wanken geriet](https://netzpolitik.org/2026/kw-20-die-woche-in-der-die-anonymitaet-im-netz-noch-mehr-ins-wanken-geriet/) — _netzpolitik.org_
- [Remote Work klappt bei euch nicht? Dann liegt es nicht am Homeoffice](https://t3n.de/news/remote-work-homeoffice-prozesse-1738204/?utm_source=rss&utm_medium=newsFeed&utm_campaign=newsFeed) — _t3n.de - News_
- [Vom 4. Stock Richtung Karriereende: Deshalb wollte niemand mit Steve Jobs in den Aufzug steigen](https://t3n.de/news/steve-jobs-aufzug-apple-mitarbeiter-kuendigung-1742220/?utm_source=rss&utm_medium=newsFeed&utm_campaign=newsFeed) — _t3n.de - News_
- [Honda shows off new hybrids for America as it absorbs $9 billion EV loss](https://arstechnica.com/cars/2026/05/honda-shows-off-new-hybrids-for-america-as-it-absorbs-9-billion-ev-loss/) — _Ars Technica - All content_
- [Playstation 5 und Nintendo Switch 2: Hersteller erhöhen die Preise – hier gibt es die Konsolen noch günstig](https://t3n.de/news/playstation-5-nintendo-switch-guenstig-kaufen-1742739/?utm_source=rss&utm_medium=newsFeed&utm_campaign=newsFeed) — _t3n.de - News_
- [Inkognitomodus für Meta AI: Wie du  in Whatsapp bald private Chats mit der KI führst](https://t3n.de/news/inkognitomodus-whatsapp-meta-ai-1742741/?utm_source=rss&utm_medium=newsFeed&utm_campaign=newsFeed) — _t3n.de - News_
- [Bis zu 25 Prozent verfälscht: Microsoft-Forscher warnen davor, große Dokumente von KI bearbeiten zu lassen](https://t3n.de/news/bis-zu-25-prozent-verfaelscht-microsoft-forscher-warnen-davor-grosse-dokumente-von-ki-bearbeiten-zu-lassen-1742608/?utm_source=rss&utm_medium=newsFeed&utm_campaign=newsFeed) — _t3n.de - News_
