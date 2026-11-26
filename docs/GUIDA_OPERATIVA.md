# GUIDA OPERATIVA FINALE - Gruppo 10 (Rotar, Moretti, Ounifi, Roncalli)
Versione delle 12:30. Piattaforma: Microsoft 365 Copilot, Agent Builder (Copilot Studio non disponibile: "User license not found").

---------------------------------------------------------------------
## 0. COSA C'È NELLA CARTELLA `consegna/`
| File | A cosa serve | Si consegna? |
|---|---|---|
| `agente1_istruzioni.txt` | Istruzioni da incollare nell'Agente 1 | no (sono dentro il file Istruzioni) |
| `agente2_istruzioni.txt` | Istruzioni da incollare nell'Agente 2 | no (idem) |
| `Gruppo10_Rotar_Istruzioni.txt` | Problema, decisione, architettura + istruzioni complete dei 2 agenti | **SÌ** |
| `Gruppo10_Rotar_Archivio.xlsx` / `.csv` | Archivio condiviso: 40 evidenze (35 VERIFICATO, 4 DA_VERIFICARE, 1 MANCANTE) | **SÌ** |
| `skill_archivio_g10.zip` | L'archivio impacchettato come skill da caricare in entrambi gli agenti | **SÌ** |
| `Gruppo10_Rotar_LogVerifica.txt` | Due cicli reali di passaggio dati e verifica umana (E33-E37 incollate, E38-E40 con @menzione) | **SÌ** |
| `Gruppo10_Rotar_ProvaA..D.txt` | Da creare alle 15:15 | **SÌ** |

---------------------------------------------------------------------
## 1. LA DECISIONE (stesse parole in chat, al checkpoint e nel pitch)
- **Destinatario:** responsabile commerciale BASF Italia che segue i produttori di pannelli sandwich continui in PU/PIR.
- **Bisogno:** i pannellisti vedono tardi dove si sposta la domanda (edilizia in calo, logistica, data center, EPBD, ricostruzione) e come cambiano i costi di MDI, polioli e acciaio, e reagiscono in ritardo con margini sotto pressione.
- **Decisione prioritaria:** quali segmenti di clienti (logistica, catena del freddo, data center, edifici pubblici EPBD, ricostruzione) e quali prodotti (PIR resistente al fuoco, basso lambda, minore impronta, Biomass Balance) privilegiare nei prossimi 12-24 mesi, e come proteggere la fornitura, con un piano a scenari e trigger rivisti ogni trimestre.

## 2. ARCHITETTURA
```
AGENTE 1 Research & Data Curator (ricerca web ON)
   | righe nuove DA_VERIFICARE + BLOCCO_HANDOFF
   v
VERIFICA UMANA (si apre ogni URL, si corregge, STATO=VERIFICATO)
   v
ARCHIVIO CONDIVISO (Excel/CSV su OneDrive -> skill archivio-g10 in entrambi gli agenti)
   v
AGENTE 2 Advisor (ricerca web OFF) -> raccomandazione + RICHIESTA ALL'AGENTE 1 se mancano dati
   ^__________________________ ciclo di ritorno ________________________|
```

---------------------------------------------------------------------
## 3. AGENTE 1: NON va rifatto, va solo modificato (5 min, Elisey)
Copilot > Agents > `G10 Agente 1 Research Curator` > ⋯ > **Edit** > Configure. Controlla campo per campo:
| Campo | Valore |
|---|---|
| Nome | `G10 Agente 1 Research Curator` |
| Descrizione | `Raccoglie evidenze pubbliche datate (Eurostat, UN Comtrade, EUR-Lex) sul mercato dei pannelli sandwich PU e le prepara per l'archivio condiviso. Non dà consigli.` |
| Instructions | Seleziona tutto, cancella, incolla TUTTO `agente1_istruzioni.txt` (versione nuova: sezione "PASSAGGIO DATI", prossimo ID E41) |
| Skills | Rimuovi `archivio-g10` vecchia > Add > Upload > `skill_archivio_g10.zip` |
| Knowledge | Nessun link (oppure il test del punto 5.3) |
| Ricerca web | **ON** |
| Modello | **Think deeper** |
| Suggested prompts | `Hormuz e materie prime` / `Cerca evidenze recenti su Hormuz e sui costi di MDI e polioli in Europa e prepara le righe per l'archivio` |
| | `Eurostat costruzioni` / `Trova l'ultimo comunicato Eurostat sulla produzione nelle costruzioni e prepara la riga per l'archivio` |
| | `Domanda per segmenti` / `Cerca dati recenti su logistica, catena del freddo e data center in Italia e prepara le righe per l'archivio` |
Premi **Update**.

**Test (1 min):** `Qual è l'ultimo ID nell'archivio e quante righe sono DA_VERIFICARE?` Risposta attesa: E40, con 4 righe DA_VERIFICARE (E08, E24, E27, E32). Se dice un ID più basso, la skill non è stata aggiornata.

---------------------------------------------------------------------
## 4. AGENTE 2: crearlo (10 min, Elisey)
Copilot > Agents > **New agent** > ignora la chat > **Configure**.
| Campo | Valore |
|---|---|
| Nome | `G10 Agente 2 Advisor` |
| Descrizione | `Legge l'archivio condiviso, collega le evidenze a rischi e opportunità e propone una next action motivata, separando fatti e scenari.` |
| Instructions | Incolla TUTTO `agente2_istruzioni.txt` |
| Skills | Add > Upload > `skill_archivio_g10.zip` |
| Knowledge | **Nessun link** |
| Ricerca web | **OFF** (solo l'Agente 1 porta fonti: i due ruoli restano separati) |
| Modello | **Think deeper** |
| Suggested prompts | `Scenario base` / `Domani tutto come oggi: quali clienti e prodotti deve privilegiare BASF con i pannellisti nei prossimi 12 mesi?` |
| | `Fine guerra Ucraina` / `Ipotizziamo la fine della guerra in Ucraina: come cambiano le priorità di clienti, prodotti e fornitura?` |
| | `Dati in conflitto` / `Quanto vale il mercato europeo dei pannelli sandwich? Le fonti concordano?` |
Premi **Create**. Poi per **entrambi** gli agenti: ⋯ > **Share** > aggiungi Andrea, Ahmed e Federico.

**Test (3 min):** nella chat dell'Agente 2 incolla il BLOCCO_HANDOFF dell'Agente 1 (righe E33-E37), poi:
`Domani tutto come oggi con Hormuz ancora parzialmente bloccato: quali clienti e prodotti deve privilegiare BASF con i pannellisti nei prossimi 12 mesi?`
Controlla: 11 sezioni (da 0 a 10), ID citati, "SCENARIO BASE", una sola azione prioritaria con KPI e trigger, sezione 9 RICHIESTA ALL'AGENTE 1. **Manda la risposta a Claude.**

---------------------------------------------------------------------
## 5. PASSAGGIO DIRETTO CON @MENZIONE (TESTATO: FUNZIONA)
È il flusso principale per la demo e per le prove.
1. Copilot > **New chat** (la chat normale, NON dentro un agente). In alto scegli **Think deeper**.
2. Scrivi solo `@` e **scegli `G10 Agente 1 Research Curator` dalla lista** (scritto a mano non funziona). Poi scrivi la richiesta, ad esempio `Cerca evidenze su Hormuz e prepara il BLOCCO_HANDOFF`.
3. Quando ha risposto, nella **stessa chat** scrivi `@`, **scegli `G10 Agente 2 Advisor` dalla lista**, poi `Usa il BLOCCO_HANDOFF qui sopra e rispondi: <domanda>`.
4. Controlla l'intestazione della risposta: deve esserci "G10 Agente 2 Advisor", e devono comparire gli ID nuovi dell'Agente 1.
Se un giorno non funzionasse: copia il BLOCCO_HANDOFF e incollalo nella chat dell'Agente 2 (metodo di riserva).

## 6. COME SI AGGIORNA L'ARCHIVIO (quando l'Agente 1 trova righe nuove)
1. **Verifica (Ahmed o Federico):** per ogni riga nuova apri l'URL e cerca il numero nella pagina.
   - Coincide: metti STATO=VERIFICATO.
   - Errato o incompleto: correggi la riga e annotalo nel log.
   - Pagina illeggibile: lascia DA_VERIFICARE.
2. **Salva:** incolla le righe in fondo a `consegna/Gruppo10_Rotar_Archivio.csv`, separatore punto e virgola.
3. **Rigenera (Elisey, dal PC Linux):**
   `python3 /home/eli6/Documents/BASF/strumenti/crea_skill_archivio.py`
   Poi ricarica `skill_archivio_g10.zip` in **entrambi** gli agenti (Edit > Skills).
4. **Log:** aggiungi due righe a `Gruppo10_Rotar_LogVerifica.txt` (cosa hai verificato e cosa hai corretto).
Oppure mandate le righe a Claude: le verifica in automatico e rigenera tutto.

---------------------------------------------------------------------
## 7. DRY RUN DELLE PROVE (14:15-15:00, Andrea + Elisey)
Ogni domanda va fatta con il flusso @menzione del §5 (prima Agente 1, poi Agente 2 nella stessa chat):
1. `Domani tutto come oggi: cosa deve fare BASF con i pannellisti nei prossimi 12 mesi?` (previsione certa / scenario base)
2. `Ipotizziamo che la guerra in Ucraina finisca a gennaio 2027: cosa cambia?` (ipotetico: deve dire che oggi non c'è un cessate il fuoco [E20, E21])
3. `Hormuz torna pienamente navigabile: cosa cambia per BASF e per i pannellisti?` (ipotetico: deve dire che oggi Hormuz è ancora critico [E11, E33])
4. `Un biopolimero rinnovabile sostituisce parte dei polioli: cosa può fare BASF?` (bio: deve dire che le fonti E18-E19 sono vecchie e il rischio HFO/PFAS [E30, E32])
5. `Quanto vale il mercato europeo dei pannelli?` (conflitto E08-E10)
Mandate a Claude gli output delle domande 1 e 2. Claude corregge le istruzioni; reincollatele in tutti e due gli agenti.

---------------------------------------------------------------------
## 8. PROVE UFFICIALI (15:15-16:00)
1. Alle 15:15 aprite la cartella OneDrive del Gruppo 10 e leggete le 4 prove.
2. **Coppia 1** (Elisey + Andrea): prove A e B. **Coppia 2** (Ahmed + Federico): prove C e D. Massimo 10 minuti per prova. Il timekeeper Ahmed chiama i tempi.
3. Per ogni prova:
   1. **New chat** con Think deeper > `@` > scegli **G10 Agente 1** > incolla il testo della prova + `Raccogli le evidenze per questa richiesta e prepara il BLOCCO_HANDOFF`.
   2. **Verifica veloce:** apri gli URL delle righe nuove (2-3 min) e annota cosa confermi o correggi. Se non c'è tempo, lasciale DA_VERIFICARE e scrivilo.
   3. Stessa chat > `@` > scegli **G10 Agente 2** > `Usa il BLOCCO_HANDOFF qui sopra. Verifica umana: <righe confermate o corrette>. Rispondi alla prova: <testo della prova>`.
   4. **Salva in Blocco note / Word** come `Gruppo10_Rotar_ProvaA.txt` (B, C, D):
```
PROVA A - Gruppo 10 - Capogruppo Elisey Rotar
TESTO DELLA PROVA: (incolla)
===== OUTPUT AGENTE 1 (Research & Data Curator) =====
(incolla)
===== VERIFICA UMANA =====
Righe verificate: E.. E..  Corrette: ...  Lasciate DA_VERIFICARE: ...
===== OUTPUT AGENTE 2 (Advisor) =====
(incolla)
```
4. **Alle 15:45** mandate i 4 txt a Claude. Se un output è debole, si rifà la prova (c'è tempo fino alle 16:00).
5. Per copiare le risposte usate l'icona 📋 sotto ogni risposta, non la selezione con il mouse: le tabelle restano intatte.

---------------------------------------------------------------------
## 9. CONSEGNA (16:00-16:15) - cartella OneDrive "Gruppo 10"
- [ ] `Gruppo10_Rotar_Istruzioni.txt`
- [ ] `Gruppo10_Rotar_ProvaA.txt`, `..._ProvaB.txt`, `..._ProvaC.txt`, `..._ProvaD.txt`
- [ ] `Gruppo10_Rotar_Archivio.xlsx` e `.csv` (con le righe aggiunte durante le prove)
- [ ] `skill_archivio_g10.zip`
- [ ] `Gruppo10_Rotar_LogVerifica.txt`
- [ ] Prototipo: chiedete al prof. Magni come "copiare l'agente" nella cartella. Se non si può esportare, create `Gruppo10_Rotar_Prototipo.txt` con nomi, impostazioni, link di condivisione dei 2 agenti e 2 screenshot della schermata Configure.
Prima di chiudere, uno che non ha preparato i file controlla nomi e contenuto (Federico).

---------------------------------------------------------------------
## 10. PITCH (3 minuti) - bozza, la completa Claude dopo le prove
| Tempo | Chi | Cosa |
|---|---|---|
| 0:00-0:40 | Ahmed | Gancio + problema + decisione + destinatario |
| 0:40-1:20 | Andrea | Archivio: 37 evidenze, fatto/inferenza/limite, l'omissione trovata dalla verifica |
| 1:20-2:10 | Elisey | Demo live in una sola chat: @Agente 1 > verifica > @Agente 2, con un caso di dato mancante |
| 2:10-3:00 | Federico | Raccomandazione, scenario base contro ipotetico, limiti, frase finale |
Piano B demo: screenshot di una prova già riuscita sul telefono.

---------------------------------------------------------------------
## 11. ORARI E RUOLI
| Ora | Elisey (builder) | Andrea (test) | Ahmed (timekeeper, fonti) | Federico (product lead) |
|---|---|---|---|---|
| 12:30-12:45 | Reincolla le istruzioni nell'Agente 2 + skill nuova in entrambi | Prova del flusso @menzione (§5) | Verifica a campione E07, E12, E16 | Prepara il CP2 |
| 12:45-13:30 | Pranzo | Pranzo | Pranzo | Pranzo |
| 13:30-14:15 | Dry run domande 1-2 (§7) | Dry run domande 3-5 (§7) | Scrive il copione del pitch | Scrive il copione del pitch |
| 14:15-15:00 | Dry run (§7) | Dry run (§7) | Prova del pitch ×2 | Prova del pitch ×2 |
| 15:00-15:15 | CP2: mostra il flusso | | | |
| 15:15-16:00 | Prove A, B | Prove A, B | Prove C, D + tempi | Prove C, D |
| 16:00-16:15 | Carica i file | | | Controlla la consegna |
| 16:25 | Demo | Archivio | Apertura | Chiusura |

## 12. REGOLE D'ORO
- Mai presentare uno scenario come previsione: oggi non c'è un cessate il fuoco in Ucraina e Hormuz è ancora critico.
- Ogni numero detto a voce deve avere il suo ID (E07, E34...).
- Niente dati personali e niente consigli di investimento: l'analisi del titolo BASF in Borsa non si usa.
- Il pitch parla di un dimostratore educativo: la decisione finale la prende una persona.
