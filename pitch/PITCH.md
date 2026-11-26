# PITCH Gruppo 10 · PIRadar · 3 MINUTI, slide per slide
Presentazione: https://eliseyrotar.github.io/piradar-basf-hackathon/ (frecce per cambiare slide, F per lo schermo intero)
Versione corta: circa 420 parole, 3:00-3:10. Le frasi rimaste sono IDENTICHE a prima: avete solo tolto dei pezzi.
La demo live NON si fa nel pitch: tenete aperta la chat di Copilot e mostratela se nelle domande chiedono "funziona davvero?".

---

## SLIDE 1 · Copertina · 🎤 AHMED (8 s)
"Buongiorno, siamo il Gruppo 10. Questo è **PIRadar**: un radar di mercato per i produttori di pannelli sandwich in poliuretano, costruito con due agenti su Copilot."

## SLIDE 2 · Team · 🎤 AHMED (12 s)
"**Federico Roncalli** ha fatto la ricerca. **Elisey Rotar** ha costruito l'Agente 1. **Io, Ahmed**, l'Agente 2. **Andrea Moretti** ha curato il pitch e questa presentazione."

## SLIDE 3 · Problema · 🎤 AHMED (30 s)
"Immaginate di produrre pannelli isolanti.
**Primo:** a settembre la costruzione di edifici in Europa è scesa del 4%: lo dice Eurostat.
**Secondo:** il benzene, da cui nasce l'MDI che serve per la schiuma, costa quasi il doppio di un anno fa.
**Terzo:** a Hormuz il traffico di petrolio è sceso del 40%.
La nostra decisione è per il **responsabile commerciale di BASF Italia**: quali clienti e quali prodotti privilegiare nei prossimi 12 mesi. Andrea?"

## SLIDE 4 · Archivio · 🎤 ANDREA (30 s)
"Il nostro punto di partenza è un **archivio di 40 evidenze pubbliche**: Eurostat, Commissione europea, World Bank, BASF stessa.
**35 su 40 le abbiamo controllate aprendo il link**, e ogni riga dice se è **fatto, inferenza o limite**.
La verifica serve davvero: l'agente aveva dimenticato che il prezzo medio dell'MDI scende. L'abbiamo trovato e corretto prima che arrivasse al consiglio.
Elisey?"

## SLIDE 5 · Due agenti · 🎤 ELISEY (30 s)
"**Agente 1, Research Curator:** cerca le fonti e le classifica. Non dà mai consigli.
Poi **una persona verifica**, i dati entrano nell'**archivio**, e l'**Agente 2, Advisor**, usa solo dati controllati e cita sempre l'ID della fonte.
Agent Builder non permette agli agenti di parlarsi, quindi l'abbiamo fatto noi: **nella stessa chat chiamiamo @Agente 1 e poi @Agente 2**, che usa subito i dati appena trovati."

## SLIDE 6 · Prove · 🎤 ELISEY (25 s)
"Le quattro prove misuravano come gestisce i dati deboli, mancanti o in conflitto.
**Prova B:** un '+30% nel 2027' senza fonte. L'ha rifiutato.
**Prova C:** dazio e fine della guerra. Li ha tenuti separati, senza dare per scontato che con la pace il gas costi meno.
**Prova D:** su Lattonedil e Isopan non c'erano dati, e non li ha inventati. Federico?"

## SLIDE 7 · Raccomandazione · 🎤 FEDERICO (25 s)
"Il nostro consiglio si chiama **PIR Priority Portfolio**, rivisto ogni trimestre.
**Per BASF:** proteggere capacità per i pannellisti che servono **catena del freddo e data center**, dove BASF ha già Elastopir.
**Per il pannellista:** un pilota piccolo e reversibile su una linea, con criteri scritti per andare avanti o fermarsi."

## SLIDE 8 · Futuro · 🎤 FEDERICO (15 s)
"Con un piccolo investimento: Copilot Studio per collegare gli agenti da soli, un radar settimanale, e lo stesso modello per altri mercati BASF."

## SLIDE 9 · Chiusura · 🎤 FEDERICO (8 s)
"Il nostro prototipo non indovina il futuro: **trasforma dati verificati in decisioni che una persona può controllare**. Grazie."

---

## SE SIETE IN RITARDO (tagli d'emergenza)
- Slide 3: saltate il "Terzo" (Hormuz).
- Slide 6: dite solo la prova B.
- Slide 8: una frase sola, "Con un piccolo investimento diventa automatico e replicabile."

## DOMANDE PROBABILI (max 20 secondi)
| Domanda | Chi | Risposta |
|---|---|---|
| Funziona davvero? | Elisey | Mostra la chat di Copilot già pronta: Agente 1, poi Agente 2, poi l'Agente 1 che rifiuta di consigliare. |
| Come sapete che una fonte è affidabile? | Andrea | Scala A/B/C e ogni URL aperto a mano: 35 su 40 verificati. |
| Fatto o scenario? | Federico | Ogni frase ha l'etichetta FATTO con ID, IPOTESI o SCENARIO. La fine della guerra è sempre ipotetica. |
| Cosa succede se manca un dato? | Elisey | Lo dichiara, abbassa la confidenza e scrive cosa cercare all'Agente 1. |
| Gli agenti leggono l'Excel? | Elisey | L'archivio è caricato come skill in entrambi gli agenti, perché Agent Builder non accettava file. Con Copilot Studio diventerebbe un collegamento diretto. |
| Perché catena del freddo e data center? | Ahmed | L'edilizia cala, ma questi segmenti chiedono fuoco e isolamento, dove BASF ha già prodotti. |
| E la privacy? | Federico | Solo fonti pubbliche, nessun dato personale, la decisione finale è di una persona. |
