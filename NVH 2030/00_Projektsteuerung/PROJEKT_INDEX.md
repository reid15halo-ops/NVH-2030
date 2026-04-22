# NVH 2030 — Projektübersicht & Dateiindex

**Projekt:** Layoutoptimierung Werk Gundernhausen
**Ziel:** Halle 3 freimachen, Konsolidierung in Halle 2, neue Technologien integrieren
**Stand:** 26.02.2026

> **ENTSCHEIDUNG: Vorschlag 4 ausgewählt** (26.02.2026)
> Drei-Zonen-Konzept mit expliziter CO2- und Trennmittel-Planung.
> Budget Phase A (Layoutumbau): 262.000 - 460.000 EUR
> Projektdauer: ~22 Monate (Q2 2026 → Q1 2028)

---

## Projektstruktur

```
NVH 2030/
│
├── 00_Projektsteuerung/                 ← Projektübersicht & Steuerung
│   ├── PROJEKT_INDEX.html               ← Einstiegspunkt (diese Datei)
│   ├── PROJEKT_INDEX.md
│   └── NVH_2030_Intent_Questionnaire.md ← Ausgefüllter Fragebogen
│
├── 01_Quelldokumente/                   ← Quelldokumente & Referenzen
│   ├── Document_Summaries_Reference.md  ← Zusammenfassungen aller Dokumente
│   ├── EN_Flex_2024_Q1_WT_Global_Purchasing_Meeting.pdf
│   ├── 20240924_BIOPOL4MOTIVE.pdf
│   ├── 20242001_Foam EN_Bloom Foam Project.pdf
│   ├── Developements and posibilities in using release agents at flexible foam.pdf
│   ├── PUSH HR for Genk Trial 2 summary for EN.pdf
│   ├── BGEU_EN_Flex_13052025.pptx
│   └── Biopol4motive_Autoneum_CONFIDENTIAL.pptx
│
├── 02_Layouts/                          ← Layout-Bilder & Pläne
│   ├── Vorschlag 2 24-02-2026.png
│   ├── Vorschlag 3 24-02-2026.png
│   ├── Vorschlag 4 24-02-2026.jpg       ← AUSGEWÄHLT
│   ├── Current Layout Hall 2 and Hall 3.png
│   ├── Halle2_Layoutplan_V4.html        ← Schematischer Layoutplan (SVG)
│   ├── Layout_Spezifikation_V4.html     ← CAD-Briefing
│   └── Layout_Spezifikation_V4.md
│
├── 03_Analysen/                         ← Technische Analysen & Bewertungen
│   ├── Evaluation_Matrix.html           ← Interaktive Bewertungsmatrix
│   ├── Technische_Prozessbewertung.html
│   ├── Kostenschaetzung_Vergleich.html  ← Kostenschätzung & ROI
│   ├── Layoutentscheidung_Vorschlag4.html ← V4-Zonenanalyse & Entscheidung
│   ├── Risikobewertung_Phase_A.html     ← Risikobewertung & Kundenauswirkung
│   └── (+ zugehörige .md Dateien)
│
├── 04_Praesentationen/                  ← Präsentationen & Argumentation
│   ├── NVH2030_Management_Summary.pptx  ← Management Summary (10 Folien)
│   ├── Stakeholder_Praesentation_DE.html
│   ├── Argumentationspapier_Vorschlag4.html ← Business Case & 12 Argumente
│   ├── Phase_B_Zukunftsoptionen.html    ← Zukunftsoptionen Halle 3
│   └── (+ zugehörige .md Dateien)
│
├── 05_Planung/                          ← Zeitplanung & Umsetzung
│   └── Implementation_Gantt.html        ← Interaktiver Gantt-Chart
│
└── _Tools/                              ← Build-Skripte & Templates (intern)
    ├── generate_pptx.py
    ├── 200624_ATN_Template_16to9.potx
    └── _template_converted.pptx
```

---

## Deliverables — Nutzungsanleitung

### 1. Interaktive Bewertungsmatrix
**Datei:** `Evaluation_Matrix.html`
**Öffnen:** Doppelklick → öffnet im Browser
**Funktionen:**
- Bewertungen (1-5) je Kriterium editierbar
- Gewichtete Gesamtbewertung berechnet sich automatisch
- Radar-Chart aktualisiert sich live
- Ranking-Übersicht oben
- Kommentare je Zelle editierbar
- Export/Import als JSON
- Druckansicht verfügbar

### 2. Interaktiver Gantt-Chart
**Datei:** `Implementation_Gantt.html`
**Öffnen:** Doppelklick → öffnet im Browser
**Funktionen:**
- 22 Aufgaben in 5 Phasen (Q2 2026 → Q1 2028)
- 5 Meilensteine
- Kritischer Pfad rot markiert
- Abhängigkeiten als Pfeile
- Zoom (+/-) und Scroll
- Klick auf Aufgabe → Detailpanel
- Phasen ein-/ausklappbar
- Druckansicht verfügbar

### 3. Technische Prozessbewertung
**Datei:** `Technische_Prozessbewertung.md`
- Detaillierte technische Analyse je Vorschlag
- Infrastrukturbedarf (CO2-RA, Bio-Polyol, PUSH HR)
- Platzbedarf-Tabellen
- Vergleichsübersicht & Empfehlung

### 4. Kostenschätzung
**Datei:** `Kostenschaetzung_Vergleich.md`
- Grobe Richtwerte (Industriebenchmarks + Projektdaten)
- Maschinenabbau: 101-167k €
- CO2-RA-Infrastruktur: 235-370k €
- Gesamt je Vorschlag: 544-942k €
- Amortisationsrechnung
- Fazit: Kostenunterschied zwischen Vorschlägen < 4%

### 5. Stakeholder-Präsentation
**Datei:** `Stakeholder_Praesentation_DE.md`
- 16 Folien-Struktur auf Deutsch
- Bereit zum Übertragen in PowerPoint
- Alle Kerndaten und Empfehlungen enthalten

---

### 6. Layoutentscheidung Vorschlag 4
**Datei:** `Layoutentscheidung_Vorschlag4.md`
- Formale Entscheidungsdokumentation
- Detaillierte Zonenanalyse (Zone 1-3 + Nebenbereiche)
- Materialfluss-Diagramm (linearer Top-Down-Flow)
- Infrastrukturbedarf je Zone (CO2-RA, Bio-Polyol, PUSH HR)
- Nächste Schritte & offene Fragen

---

## Quelldokumente — Zusammenfassungen
**Datei:** `Information/Document_Summaries_Reference.md`
- 7 Dokumente vollständig zusammengefasst
- Cross-Document-Analyse für Layout-Bezug
- Infrastruktur-Anforderungstabelle
- 5 offene Schlüsselfragen identifiziert
