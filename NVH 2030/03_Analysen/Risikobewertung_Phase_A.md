# Risikobewertung & Kundenauswirkungsanalyse — Phase A

**Projekt:** NVH 2030 — Layoutumbau Vorschlag 4
**Standort:** Werk Gundernhausen
**Stand:** 27.02.2026
**Dokument-Nr.:** NVH2030-RISK-001

---

## 1. Bewertungsmethodik

### Eintrittswahrscheinlichkeit (W)

| Stufe | Bezeichnung | Beschreibung |
|-------|-------------|--------------|
| 1 | Sehr gering | Tritt voraussichtlich nicht ein (< 5%) |
| 2 | Gering | Unwahrscheinlich, aber moglich (5-20%) |
| 3 | Mittel | Kann eintreten (20-50%) |
| 4 | Hoch | Tritt wahrscheinlich ein (50-80%) |
| 5 | Sehr hoch | Fast sicher (> 80%) |

### Auswirkung (A)

| Stufe | Bezeichnung | Kosten | Zeitplan | Kunden |
|-------|-------------|--------|----------|--------|
| 1 | Minimal | < 10k EUR | < 1 Woche | Keine Auswirkung |
| 2 | Gering | 10-30k EUR | 1-2 Wochen | Interne Kommunikation |
| 3 | Mittel | 30-80k EUR | 2-4 Wochen | Kundeninformation |
| 4 | Hoch | 80-150k EUR | 1-3 Monate | Lieferverzogerung |
| 5 | Kritisch | > 150k EUR | > 3 Monate | Kundenverlust |

### Risikoprioritatsklasse (RPZ = W x A)

| RPZ | Klasse | Handlung |
|-----|--------|----------|
| 1-4 | Niedrig (grun) | Akzeptieren, beobachten |
| 5-9 | Mittel (gelb) | Massnahmen planen, uberwachen |
| 10-15 | Hoch (orange) | Sofortige Massnahmen erforderlich |
| 16-25 | Kritisch (rot) | Eskalation, Projektanpassung |

---

## 2. Risiko-Register

### 2.1 Produktionsrisiken

| ID | Risiko | W | A | RPZ | Massnahme |
|----|--------|---|---|-----|-----------|
| P1 | Stillstandszeit uberschreitet 2 Wochen Sommerpause | 2 | 4 | 8 | Detailplanung vorab, kritische Arbeiten priorisieren, Wochenendschichten einplanen |
| P2 | Unerwartete Infrastrukturprobleme beim Anschluss (Elektrik, Druckluft, Wasser) | 3 | 3 | 9 | Bestandsaufnahme Q2 2026 durchfuhren, Reservekapazitat Elektriker vorsehen |
| P3 | Maschine lasst sich nicht am neuen Standort in Betrieb nehmen | 2 | 4 | 8 | Testlauf je Maschine sofort nach Umstellung, Herstellersupport auf Abruf |
| P4 | Qualitatseinbusse nach Umstellung (Parameterdrift, Formtragertemperatur) | 3 | 3 | 9 | Erstmusterprufung nach Umstellung, Qualitatsprotokoll fur erste 2 Wochen |
| P5 | Schaumlinie C fallt wahrend Umbau aus (sehr alt) | 3 | 4 | 12 | F-Linie als Backup/Entlastung, Ersatzteile vorhalten, Wartung vor Umbau |

### 2.2 Kundenrisiken

| ID | Risiko | W | A | RPZ | Massnahme |
|----|--------|---|---|-----|-----------|
| K1 | Kunden erhalten wahrend Sommerpause keine Lieferungen | 4 | 3 | 12 | Vorproduktion (Sicherheitsbestand), Kundenabstimmung Mai/Juni 2026 |
| K2 | Qualitatsreklamation nach Wiederanlauf (neue Maschinenposition) | 3 | 3 | 9 | Erstmusterprufung, SPC-Uberwachung erste 4 Wochen, Kundeninfo vorab |
| K3 | Kunde fordert Audit wegen Standortveranderung | 2 | 2 | 4 | Proaktive Information, Audit-Bereitschaft sicherstellen |
| K4 | Lieferverzogerung durch verlangerten Anlauf nach Umbau | 2 | 4 | 8 | Pufferbestand aufbauen (4-6 Wochen vor Umbau), Anlaufkurve planen |

### 2.3 Technische Risiken

| ID | Risiko | W | A | RPZ | Massnahme |
|----|--------|---|---|-----|-----------|
| T1 | Elektrik/Druckluft in Halle 2 reicht nicht fur alle konsolidierten Anlagen | 2 | 3 | 6 | Lastberechnung Q2 2026, ggf. Verteilung anpassen oder erweitern |
| T2 | CO2-Leitung zu kurz fur neue Aufstellpositionen | 2 | 2 | 4 | Leitungsplanung im Detail, CO2-Tank-Position beachten |
| T3 | Formtragerheizung uberfordert bei gleichzeitigem Betrieb C + F | 2 | 3 | 6 | Heizleistung berechnen, ggf. Heizstation erweitern |
| T4 | Bodentragfahigkeit fur schwere Maschinen unbekannt | 1 | 3 | 3 | Baustatik prufen vor Aufstellung |

### 2.4 Personalrisiken

| ID | Risiko | W | A | RPZ | Massnahme |
|----|--------|---|---|-----|-----------|
| M1 | Schlusselpersonal nicht verfugbar wahrend Sommerpause | 3 | 3 | 9 | Urlaubsplanung abstimmen, Kernteam fruhzeitig festlegen |
| M2 | Widerstand der Belegschaft gegen Veranderung | 2 | 2 | 4 | Fruhzeitige Information, Einbindung Betriebsrat, Vorteile kommunizieren |
| M3 | Einarbeitungszeit an neuen Arbeitsplatzen langer als geplant | 3 | 2 | 6 | Schulungsplan, Begehung vor Umbau, Arbeitsplatzgestaltung mit MA abstimmen |

### 2.5 Finanzielle Risiken

| ID | Risiko | W | A | RPZ | Massnahme |
|----|--------|---|---|-----|-----------|
| F1 | Kosten uberschreiten Budget (> 460k EUR) | 2 | 3 | 6 | Pauschale Risikorucklage 15% einplanen (~40-70k EUR) |
| F2 | Unvorhergesehene Asbestsanierung bei alten Leitungen | 1 | 4 | 4 | Voruntersuchung Gefahrstoffe, Altlastenprufung |
| F3 | Abbaukosten Maschinen hoher als geschatzt | 2 | 2 | 4 | Mind. 2 Angebote einholen, Fixpreis vereinbaren |

### 2.6 Terminrisiken

| ID | Risiko | W | A | RPZ | Massnahme |
|----|--------|---|---|-----|-----------|
| Z1 | Lieferzeit fur Infrastrukturkomponenten > 8 Wochen | 3 | 3 | 9 | Fruhzeitig bestellen (Q2 2026), Langzeitlieferanten identifizieren |
| Z2 | Sommerpause 2026 wird nicht genehmigt oder verkurzt | 2 | 4 | 8 | Fruhzeitige Abstimmung mit Werksleitung + Kunden |
| Z3 | Parallele Projekte konkurrieren um Ressourcen | 2 | 2 | 4 | Ressourcenplanung mit anderen Abteilungen abstimmen |

---

## 3. Risikomatrix (Ubersicht)

```
AUSWIRKUNG
         1       2       3       4       5
    ┌───────┬───────┬───────┬───────┬───────┐
  5 │       │       │       │       │       │
    ├───────┼───────┼───────┼───────┼───────┤
W 4 │       │       │ K1    │       │       │
    ├───────┼───────┼───────┼───────┼───────┤
  3 │       │ M3    │P2,P4  │ P5    │       │
    │       │       │K2,M1  │       │       │
    │       │       │Z1     │       │       │
    ├───────┼───────┼───────┼───────┼───────┤
  2 │       │M2,F3  │T1,T3  │P1,P3  │       │
    │       │Z3     │F1     │K4,Z2  │       │
    ├───────┼───────┼───────┼───────┼───────┤
  1 │       │       │ T4    │ F2    │       │
    └───────┴───────┴───────┴───────┴───────┘
         grun    grun   gelb   orange   rot
```

### Top-5-Risiken (RPZ >= 9)

| Rang | ID | Risiko | RPZ | Verantwortlich |
|------|----|--------|-----|----------------|
| 1 | P5 | C-Linie Ausfall wahrend Umbau | 12 | Technik / Instandhaltung |
| 2 | K1 | Keine Lieferung wahrend Sommerpause | 12 | Vertrieb / Logistik |
| 3 | P2 | Unerwartete Infrastrukturprobleme | 9 | Technik |
| 4 | P4 | Qualitatseinbusse nach Umstellung | 9 | Qualitat |
| 5 | M1 | Schlusselpersonal nicht verfugbar | 9 | Werkleitung / HR |

---

## 4. Kundenauswirkungsanalyse

### 4.1 Betroffene Phase

**Kritischer Zeitraum:** Sommerpause 2026 (ca. KW 29-30)
**Max. Stillstand:** 2 Wochen
**Vor-/Nachlauf:** Je 1-2 Wochen reduzierte Kapazitat fur An-/Abfahren

### 4.2 Massnahmen zur Liefersicherung

| Phase | Zeitraum | Massnahme | Verantwortlich |
|-------|----------|-----------|----------------|
| Vorbereitung | Mai-Juni 2026 | Kundenkommunikation: Geplanter Umbau ankundigen, Lieferplan abstimmen | Vertrieb |
| Vorproduktion | Juni-Juli 2026 | Sicherheitsbestand aufbauen (4-6 Wochen Kundenbedarfe vorproduzieren) | Produktion + Logistik |
| Lagerung | Juni-Juli 2026 | Lagerflache fur Vorproduktion sichern (ggf. extern) | Logistik |
| Stillstand | KW 29-30 | Kritische Umbauten durchfuhren, Notfall-Erreichbarkeit Vertrieb | Technik + Vertrieb |
| Wiederanlauf | KW 31-32 | Erstmusterprufung, SPC-Monitoring, erhohte QS-Prasenz | Qualitat |
| Nachbereitung | KW 33-34 | Restbestand abbauen, Normalbetrieb bestatigen, Kunden-Feedback einholen | Vertrieb |

### 4.3 Kommunikationsplan Kunden

| Wann | Was | Wer | An wen |
|------|-----|-----|--------|
| April 2026 | Vorinformation: Geplanter Umbau in KW 29-30, keine Qualitatsanderung | Vertrieb / Key Account | Alle Bestandskunden |
| Mai 2026 | Detailabstimmung: Vorproduktionsmenge, Liefertermine, Sonderbedarfe | Vertrieb + Logistik | Hauptkunden einzeln |
| Juni 2026 | Bestatigung Lieferplan, Sicherheitsbestand Info | Vertrieb | Alle Bestandskunden |
| KW 30 | Statusupdate: Umbau im Plan | Vertrieb | Hauptkunden |
| KW 32 | Bestatigung Wiederanlauf, Auslieferung ab Lager | Vertrieb | Alle Bestandskunden |
| KW 34 | Abschlussmeldung: Umbau abgeschlossen, Qualitat bestatigt | Vertrieb + Qualitat | Alle Bestandskunden |

### 4.4 Vorproduktionsberechnung

| Parameter | Wert | Hinweis |
|-----------|------|---------|
| Jahresvolumen | 500-1.000 t | Basis fur Berechnung |
| Wochenvolumen (Durchschnitt) | ~10-20 t | 500-1000t / 50 Wochen |
| Stillstand | 2 Wochen | KW 29-30 |
| Reduzierte Kapazitat | +2 Wochen | An-/Abfahren |
| Benotigte Vorproduktion | ~40-80 t | 4 Wochen Bedarf |
| Vorlaufzeit Vorproduktion | 4-6 Wochen vor Stillstand | Start spatestens KW 23 |
| Zusatzliche Lagerflache | ~100-200 m2 | Fur Fertigteile (Paletten) |

### 4.5 AUDI Q1 STW LHD — Sondersituation

Die AUDI Q1 STW LHD Maschine wird im Rahmen des Projekts entfernt (Auslauf Kundenauftrag). Hier ist sicherzustellen:

| Aktion | Zeitpunkt | Status |
|--------|-----------|--------|
| Bestatigung Auslaufdatum mit AUDI | Vor Stillstand | Offen |
| Letzte Lieferung sicherstellen | Vor Maschinenabbau | Offen |
| Restteile-Vereinbarung (Nachlieferung, Werkzeugverbleib) | Vor Stillstand | Offen |
| Maschine freigeben fur Abbau | Nach letzter Lieferung | Offen |

---

## 5. Notfallszenarien

### Szenario A: Stillstand dauert langer als 2 Wochen

**Trigger:** Infrastrukturproblem, Maschinenausfall, Genehmigungsverzug
**Massnahmen:**
- Pufferbestand reicht fur 4 Wochen Lieferung
- Parallelen Betrieb einer Linie aufrechterhalten (nur partieller Umbau je Phase)
- Nachtschichten / Wochenendarbeit nach Wiederanlauf

### Szenario B: Qualitatsreklamation nach Umstellung

**Trigger:** Parameterdrift, Temperaturabweichung, Masskontrolle
**Massnahmen:**
- Sofortige Sperrung und 100%-Prufung betroffener Charge
- Ruckverfolgung uber Chargen-Nr.
- Kundeninfo innerhalb 24h
- Nacharbeit oder Ersatzlieferung aus Pufferbestand

### Szenario C: C-Linie fallt wahrend Umbau komplett aus

**Trigger:** Altersbedingte Ausfalle (C-Linie sehr alt)
**Massnahmen:**
- F-Linie (ex Halle 3) ubernimmt Kapazitat
- Beide Linien je 6 Mischkopfe — volle Redundanz
- Ersatzteilbestand fur C-Linie vor Umbau prufen und aufstocken

---

## 6. Risikobewertung — Fazit

**Gesamtrisiko Phase A: BEHERRSCHBAR (Mittel)**

- Kein Risiko im kritischen Bereich (RPZ >= 16)
- 5 Risiken im Bereich "Hoch" (RPZ 9-12) — alle mit klaren Massnahmen
- Grosstes Einzelrisiko: C-Linie Ausfall + Kundenversorgung wahrend Sommerpause
- **Mitigation:** Vorproduktion (4-6 Wochen), F-Linie als Backup, fruhzeitige Kundenkommunikation

**Empfehlung:**
1. Infrastruktur-Bestandsaufnahme Halle 2 bis April 2026 (Risiken T1, T3 eliminieren)
2. Kundenkommunikation starten ab April 2026 (Risiko K1 minimieren)
3. Vorproduktion ab KW 23 (Juni 2026) — 40-80 t Sicherheitsbestand
4. Risikorucklage 15% im Budget vorsehen (~40-70k EUR)
5. Schaumlinie C: Wartung + Ersatzteilprufung vor Umbau (Risiko P5)
