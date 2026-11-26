<p align="center"><img src="pitch/logo_piradar.svg" width="120" alt="Logo PIRadar"></p>

# PIRadar

**Il radar di mercato per i pannelli sandwich PU/PIR.** È il prototipo del Gruppo 10 (ITIS Marconi di Dalmine) per l'Hackathon BASF "MarketStrategist" del 26 novembre 2026: due agenti su Microsoft 365 Copilot che trasformano fonti pubbliche verificate in una decisione per BASF e per i produttori di pannelli.

**▶ Presentazione online:** https://eliseyrotar.github.io/piradar-basf-hackathon/ (frecce per cambiare slide, F per lo schermo intero)

> **La sfida:** come può un fornitore di soluzioni chimiche come BASF aiutare i produttori di pannelli sandwich continui in poliuretano ad anticipare un cambiamento di mercato?

## La decisione
| | |
|---|---|
| **Destinatario** | Il responsabile commerciale BASF Italia che segue i produttori di pannelli sandwich continui in PU/PIR |
| **Bisogno** | I pannellisti vedono tardi dove si sposta la domanda (edilizia in calo, logistica, data center, EPBD, ricostruzione) e come cambiano i costi di MDI, polioli e acciaio |
| **Decisione** | Quali segmenti di clienti e quali prodotti privilegiare nei prossimi 12-24 mesi, e come proteggere la fornitura, con un piano a scenari e trigger rivisti ogni trimestre |
| **Raccomandazione** | Un *PIR Priority Portfolio* trimestrale: capacità protetta per catena del freddo e data center (Elastopir, opzione Biomass Balance) e un pilota piccolo e reversibile con il pannellista |

## Architettura
```
AGENTE 1  Research & Data Curator   ricerca web ON, non dà consigli
    │  righe nuove DA_VERIFICARE + BLOCCO_HANDOFF
    ▼
VERIFICA UMANA                      si apre ogni URL, si corregge, STATO=VERIFICATO
    ▼
ARCHIVIO CONDIVISO                  40 evidenze, pubblicato come skill "archivio-g10" in entrambi gli agenti
    ▼
AGENTE 2  Advisor                   ricerca web OFF, cita ogni ID, separa fatti / inferenze / scenari
    └── se mancano dati: RICHIESTA ALL'AGENTE 1 (ciclo di ritorno)
```
- **Passaggio diretto tra agenti senza Copilot Studio.** In una nuova chat di Microsoft 365 Copilot si chiama `@G10 Agente 1`, poi, nella stessa chat, `@G10 Agente 2`. L'Advisor usa subito il BLOCCO_HANDOFF appena prodotto. Il test è documentato in [archivio/Gruppo10_Rotar_LogVerifica.txt](archivio/Gruppo10_Rotar_LogVerifica.txt).
- **L'archivio come skill.** Agent Builder accettava come conoscenza solo link web, quindi l'archivio è impacchettato come skill (`SKILL.md` + `references/archivio.md` e `archivio.csv`), caricata in entrambi gli agenti.

## L'archivio delle evidenze
[archivio/Gruppo10_Rotar_Archivio.xlsx](archivio/Gruppo10_Rotar_Archivio.xlsx) (anche in CSV): **40 evidenze**, 35 VERIFICATO, 4 DA_VERIFICARE, 1 MANCANTE.
Campi: ID, DATA_RACCOLTA, FONTE, URL, DATA_FONTE, PERIODO_DATI, TEMA, EVIDENZA, NUMERO_CHIAVE, QUALITA (fatto / inferenza / limite), AFFIDABILITA (A/B/C), LIMITI, NOTA_INFERENZA, STATO.
Le fonti principali sono Eurostat, Commissione UE (EPBD, F-gas), World Bank (RDNA5), UN Comtrade (API pubblica), EIA, BASF, Argus Media e Lloyd's List.
I dati deboli sono lasciati apposta (stime di mercato in conflitto, prezzi MDI effettivi non disponibili gratis), per mostrare come il prototipo gestisce l'incertezza.

## Le 4 prove minime
Gli output dell'Agente 2 sono in [consegna_onedrive/](consegna_onedrive). Ogni prova è stata eseguita in una conversazione nuova, con il prompt non modificato.
| Prova | Esito |
|---|---|
| A | Una sola azione concreta per i prossimi 6-12 mesi (pilota PIR), con ID, URL, KPI e confidenza |
| B | "+30% nel 2027" senza fonte: classificato non verificato, non usato, non aggiunto all'archivio |
| C | Dazio e fine della guerra analizzati separatamente, senza effetti automatici su sanzioni, prezzi o rotte |
| D | Nessun dato su Lattonedil e Isopan: dichiarato, niente inventato, proposto un test reversibile con criteri per proseguire o fermarsi |

## Struttura della repo
| Cartella | Contenuto |
|---|---|
| `consegna_onedrive/` | I file consegnati: export JSON dei 2 agenti, istruzioni complete, prove A-D |
| `agenti/` | Istruzioni dei due agenti (da incollare in Agent Builder) e la skill `skill_archivio_g10.zip` |
| `archivio/` | Archivio delle evidenze (xlsx, csv) e log della verifica umana |
| `pitch/` | Copione del pitch di 4 minuti e logo |
| `docs/` | Guida operativa usata durante la giornata e bozza dell'archivio di Andrea |
| `strumenti/` | `crea_skill_archivio.py`: rigenera la skill dal CSV |

## Come riprodurlo
1. In Microsoft 365 Copilot > Agents > New agent > Configure: crea `G10 Agente 1 Research Curator` con le istruzioni di `agenti/agente1_research_curator_istruzioni.txt`, la ricerca web ON e la skill `agenti/skill_archivio_g10.zip`.
2. Crea `G10 Agente 2 Advisor` con `agenti/agente2_advisor_istruzioni.txt`, la ricerca web OFF e la stessa skill.
3. Per aggiornare l'archivio: aggiungi le righe verificate al CSV, lancia `python3 strumenti/crea_skill_archivio.py` e ricarica lo zip in entrambi gli agenti.
4. **Replicabile:** per un altro mercato BASF basta cambiare l'archivio e la decisione nelle istruzioni, gli agenti restano gli stessi.

## Uso responsabile
Solo fonti pubbliche, nessun dato personale. Fatti, inferenze e scenari sono sempre etichettati, e la decisione finale spetta a una persona. È un dimostratore educativo, non un sistema per decisioni aziendali reali.

## Team
Gruppo 10: Federico Roncalli (ricerca delle fonti), Elisey Rotar (Agente 1 Research Curator), Ahmed Ounifi (Agente 2 Advisor), Andrea Moretti (pitch e presentazione).
