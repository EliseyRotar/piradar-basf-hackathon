# PITCH Gruppo 10 · PIRadar · 4 minuti, slide per slide
Presentazione: https://eliseyrotar.github.io/piradar-basf-hackathon/ (frecce per cambiare slide, F per lo schermo intero)
Regole: si parla guardando la giuria, non lo schermo. Chi parla cambia anche slide, oppure lo fa Elisey al cenno. Si impara a memoria solo la prima frase. Totale circa 520 parole, cioè 3:40.

---

## SLIDE 1 · Copertina "PIRadar" · 🎤 AHMED (10 secondi)
"Buongiorno, siamo il Gruppo 10. Questo è **PIRadar**: un radar di mercato per i produttori di pannelli sandwich in poliuretano, costruito con due agenti su Copilot."
➡ *passa alla slide del team*

## SLIDE TEAM · "Quattro persone, quattro ruoli" · 🎤 AHMED (20 secondi)
"Vi presento il team.
**Federico Roncalli** ha fatto la ricerca: ha trovato e selezionato le fonti.
**Elisey Rotar** ha costruito l'Agente 1, quello che cerca e cura i dati.
**Io, Ahmed Ounifi**, ho costruito l'Agente 2, quello che dà il consiglio.
**Andrea Moretti** ha curato il pitch e questa presentazione."
➡ *passa alla slide del problema*

## SLIDE 2 (problema) · "I pannellisti vedono il cambiamento quando è già arrivato" · 🎤 AHMED (40 secondi)
"Immaginate di produrre pannelli isolanti. Guardate questi tre numeri veri.
**Primo:** a settembre la costruzione di edifici in Europa è scesa del 4%: lo dice Eurostat.
**Secondo:** il benzene, da cui nasce l'MDI che serve per la schiuma, costa quasi il doppio di un anno fa.
**Terzo:** a Hormuz il traffico di petrolio è sceso del 40%.
Il problema è che il pannellista se ne accorge quando è tardi. Per questo la nostra decisione, nel riquadro blu, è per il **responsabile commerciale di BASF Italia**: quali clienti e quali prodotti privilegiare nei prossimi 12 mesi, con un piano che si aggiorna ogni trimestre.
Per decidere servono dati veri. Andrea?"

## SLIDE 3 · "40 evidenze pubbliche, 35 aperte e ricontrollate a mano" · 🎤 ANDREA (50 secondi)
"Il nostro punto di partenza è un **archivio di 40 evidenze pubbliche**: Eurostat, Commissione europea, World Bank, UN Comtrade, BASF stessa.
Come vedete nel primo riquadro, **35 su 40 le abbiamo controllate aprendo il link**.
Ogni riga ha un'etichetta: **fatto, inferenza o limite**, più fonte, URL e data.
E i dati deboli non li nascondiamo: 5 righe sono deboli apposta, ad esempio tre stime di mercato che non concordano.
Guardate il riquadro in basso: la verifica serve davvero. L'agente aveva scritto che il prezzo dell'MDI per i pannelli sale, ma aveva dimenticato che il prezzo medio scende. L'abbiamo trovato e corretto prima che arrivasse al consiglio.
Elisey, come usano i dati gli agenti?"

## SLIDE 4 · "Due agenti, un archivio, una persona che verifica" · 🎤 ELISEY (45 secondi)
"Lo schema si legge da sinistra a destra.
**Agente 1, Research Curator:** cerca le fonti e le classifica. Non dà mai consigli: se glielo chiedi, risponde che è compito dell'Agente 2.
Poi **una persona verifica**, i dati entrano nell'**archivio**, e l'**Agente 2, Advisor**, che non cerca sul web, usa solo dati controllati e cita sempre l'ID della fonte.
La cosa più importante è nel riquadro blu: Agent Builder non permette agli agenti di parlarsi, quindi l'abbiamo fatto noi. **Nella stessa chat chiamiamo @Agente 1 e poi @Agente 2**, che usa subito i dati appena trovati. E se mancano dati, l'Advisor scrive la richiesta all'Agente 1."
➡ *passa alla slide 5*

## SLIDE 5 · "Non è caduto nelle trappole" · 🎤 ELISEY (35 secondi)
"Le quattro prove avevano delle trappole.
**Prova B:** gli hanno detto 'la domanda crescerà del 30% nel 2027', senza fonte. L'ha rifiutato: le stime vere dicono 2-5% all'anno.
**Prova C:** dazio e fine della guerra. Li ha tenuti separati, e non ha dato per scontato che con la pace il gas costi meno, perché le sanzioni restano.
**Prova D:** due clienti veri, Lattonedil e Isopan. Non c'erano dati e non li ha inventati.
Federico, quindi cosa consigliamo?"

## SLIDE 6 · "PIR Priority Portfolio" (slide arancione) · 🎤 FEDERICO (40 secondi)
"Il nostro consiglio si chiama **PIR Priority Portfolio**, rivisto ogni trimestre.
**Per BASF**, nel riquadro a sinistra: proteggere capacità per i pannellisti che servono **catena del freddo e data center**, dove contano fuoco e isolamento. BASF ha già il prodotto, Elastopir, anche nella versione Biomass Balance per chi dal 2028 deve dichiarare il carbonio. E prezzi rivisti ogni tre mesi, non fissi per un anno.
**Per il pannellista**, a destra: un pilota piccolo e reversibile su una linea, con criteri scritti per andare avanti o fermarsi.
E come c'è scritto sotto: fatti e scenari sempre separati."
➡ *passa alla slide 7*

## SLIDE 7 · "Cosa diventa domani" · 🎤 FEDERICO (25 secondi)
"Con un piccolo investimento, tre passi.
**Uno:** con Copilot Studio gli agenti si collegano da soli.
**Due:** un radar settimanale che avvisa quando arriva un nuovo dato, ad esempio da Eurostat.
**Tre:** è replicabile: per un altro mercato BASF si cambia l'archivio, non gli agenti."
➡ *passa alla slide 8*

## SLIDE 8 · Chiusura · 🎤 FEDERICO (10 secondi)
"Il nostro prototipo non indovina il futuro: **trasforma dati verificati in decisioni che una persona può controllare**. Grazie."
*(Pausa, sorriso, tutti pronti alle domande.)*

---

## DOMANDE PROBABILI (risposte in massimo 20 secondi)
| Domanda | Chi | Risposta |
|---|---|---|
| Come sapete che una fonte è affidabile? | Andrea | Scala A/B/C: ufficiali, analisti, report a pagamento. Ogni URL aperto a mano: 35 su 40 verificati. |
| Questo è un fatto o uno scenario? | Federico | Ogni frase ha l'etichetta FATTO con ID, IPOTESI o SCENARIO. La fine della guerra è sempre ipotetica. |
| Cosa succede se manca un dato? | Elisey | Lo dichiara, abbassa la confidenza e scrive cosa cercare all'Agente 1, come nella prova D. |
| Perché non è automatico? | Elisey | Agent Builder non collega gli agenti e non avevamo la licenza Studio. Abbiamo usato la @menzione. E la verifica umana in mezzo è voluta. |
| Perché catena del freddo e data center? | Ahmed | L'edilizia è in calo, ma questi segmenti chiedono fuoco e isolamento, dove BASF ha già prodotti, e il prezzo dell'MDI per il PIR tiene. |
| E la privacy? | Federico | Solo fonti pubbliche, nessun dato personale, la decisione finale è di una persona. |
Se non sapete: "È un limite che il prototipo dichiara, ed è il prossimo passo."
