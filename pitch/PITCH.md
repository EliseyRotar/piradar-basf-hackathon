# PITCH Gruppo 10 - 4 minuti (circa 520 parole)
Regola: si parla, non si legge. Si impara a memoria solo la prima frase della propria parte. Tutti in piedi, sguardo alla giuria, sorriso all'inizio.

---

## 1. AHMED - Apertura (0:00-0:50)
"Immaginate di produrre pannelli isolanti. A settembre la costruzione di edifici in Europa è scesa del 4% [Eurostat]. Il benzene, da cui nasce l'MDI, costa quasi il doppio di un anno fa. E a Hormuz il traffico di petrolio è sceso del 40%.
Domanda: come fa BASF ad aiutare questi clienti a vedere il cambiamento **prima** che arrivi?
Noi siamo il Gruppo 10. La nostra risposta è una decisione chiara per il **responsabile commerciale BASF Italia**: quali clienti e quali prodotti privilegiare nei prossimi 12 mesi, con un piano a scenari che si aggiorna ogni trimestre.
Per decidere servono dati veri. Andrea, ci racconti da dove partiamo?"

## 2. ANDREA - Le evidenze (0:50-1:45)
"Abbiamo costruito un archivio condiviso di **40 evidenze pubbliche**: Eurostat, Commissione europea, World Bank, UN Comtrade, BASF stessa, Argus.
Ogni riga ha fonte, URL, data e una qualità: **fatto, inferenza o limite**.
La parte di cui siamo più orgogliosi è la **verifica umana**: 35 righe su 40 le abbiamo controllate aprendo il link. E funziona: in un caso l'agente aveva riportato solo che il prezzo dell'MDI per i pannelli PIR saliva, dimenticando che il prezzo medio scendeva. L'abbiamo trovato e corretto.
I dati deboli non li abbiamo nascosti: tre stime di mercato che non concordano e un prezzo che non esiste in fonti gratuite restano nell'archivio, segnati come LIMITE e MANCANTE.
Elisey, mostra come gli agenti usano questi dati."

## 3. ELISEY - Il prototipo (1:45-2:50)
"Due agenti su Microsoft 365 Copilot, con **ruoli separati**.
L'**Agente 1, Research Curator**, cerca fonti e prepara le righe: non dà mai consigli. Se glieli chiedi, risponde 'è compito dell'Agente 2'.
L'**Agente 2, Advisor**, non cerca sul web: lavora solo su evidenze verificate e cita sempre l'ID della fonte.
La cosa più interessante: Agent Builder non permette agli agenti di parlarsi. Noi abbiamo trovato il modo di farlo: **nella stessa chat chiamiamo @Agente 1 e poi @Agente 2**, e l'Advisor usa subito i dati appena trovati. Se mancano dati, l'Advisor scrive una richiesta all'Agente 1: il ciclo si chiude.
E sa dire di no. Nella prova B gli hanno dato un '+30% di domanda nel 2027' senza fonte: l'ha rifiutato, ha spiegato che le stime vere dicono 2-5% l'anno e non l'ha aggiunto all'archivio.
Federico, cosa consiglia?"

## 4. FEDERICO - Raccomandazione, futuro, chiusura (2:50-4:00)
"Il consiglio per BASF: un **'PIR Priority Portfolio' trimestrale**. Proteggere capacità per i pannellisti che servono **catena del freddo e data center**, dove contano fuoco e isolamento e dove BASF ha già Elastopir, con opzione Biomass Balance per chi deve dichiarare il carbonio dal 2028. Prezzi con revisione trimestrale, non fissi per un anno.
Per il cliente: un **pilota piccolo e reversibile** su una linea, con criteri chiari per proseguire o fermarsi.
Fatti e scenari sempre separati: oggi la guerra in Ucraina non è finita, quindi resta un'ipotesi.
E ora in inglese, perché è qui che il prototipo può crescere."

**PARTE IN INGLESE (slide "With a small investment", circa 35 secondi, parlare lenti):**
"With a small investment, BASF gets three things.
**One:** Copilot Studio. The Advisor calls the Curator automatically. The architecture is already tested.
**Two:** a weekly radar. It updates the sources and sends an alert when a trigger fires.
**Three:** it is replicable. For any other BASF market, you change the archive, not the agents.
Our prototype does not guess the future. **It turns verified data into decisions that a person can check.** Thank you!"

Pronuncia: *Copilot* = "copàilot", *archive* = "àrcaiv", *replicable* = "rèplicabol", *verified* = "vèrifaid".

---

## DOMANDE PROBABILI (risposte in massimo 20 secondi)
| Domanda | Chi | Risposta |
|---|---|---|
| Come sapete che una fonte è affidabile? | Andrea | Scala A/B/C: ufficiali, analisti, report a pagamento. Ogni URL aperto a mano: 35 su 40 verificati. |
| Questo è un fatto o uno scenario? | Federico | Ogni frase ha l'etichetta: FATTO con ID, IPOTESI, SCENARIO. La fine della guerra è sempre IPOTETICA. |
| Cosa succede se manca un dato? | Elisey | Lo dichiara, abbassa la confidenza e scrive cosa cercare all'Agente 1 (prova D: niente dati su Lattonedil e Isopan, non ha inventato nulla). |
| Perché non è automatico? | Elisey | Agent Builder non collega agenti e non avevamo licenza Studio. Abbiamo usato la @menzione, e la verifica umana tra i due agenti è voluta. |
| Perché catena del freddo e data center? | Ahmed | Edilizia in calo [Eurostat -4%], ma questi segmenti chiedono fuoco e isolamento, dove BASF ha già prodotti, e il PMDI per PIR tiene il prezzo [Argus]. |
| E la privacy? | Federico | Solo fonti pubbliche, nessun dato personale, la decisione finale è di una persona. |
Se non sapete: "È un limite che il prototipo dichiara, e lo vediamo come prossimo passo."

## PROVE (prima delle 16:25)
- 2 prove complete ad alta voce con timer: obiettivo 3:45.
- Passaggi di parola già scritti nel copione: non saltateli.
- Mani ferme davanti, niente telefono in mano mentre si parla.
