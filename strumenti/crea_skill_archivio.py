# Rigenera la skill "archivio-g10" (SKILL.md + references) dal CSV dell'archivio e crea lo zip da caricare in Copilot.
import csv, os, shutil, zipfile, datetime
base=os.path.dirname(os.path.abspath(__file__)); root=os.path.join(base,'..')
src=os.path.join(root,'archivio','Gruppo10_Rotar_Archivio.csv'); out=os.path.join(base,'skill_archivio_g10')
shutil.rmtree(out,ignore_errors=True); os.makedirs(os.path.join(out,'references'))
rows=list(csv.DictReader(open(src,encoding='utf-8'),delimiter=';'))
oggi=datetime.date.today().isoformat()
stati={}
for r in rows: stati[r['STATO']]=stati.get(r['STATO'],0)+1
skill=f"""---
name: archivio-g10
description: Archivio condiviso del Gruppo 10 (hackathon BASF) con le evidenze pubbliche su pannelli sandwich PU/PIR, edilizia, normativa, materie prime, logistica, Ucraina e bio. Usala sempre per leggere le evidenze per ID (E01, E02...) con fonte, data, qualità e stato, prima di cercare o di consigliare.
---

# Archivio condiviso Gruppo 10

Questo è l'archivio condiviso tra AGENTE 1 (Research & Data Curator) e AGENTE 2 (Advisor). Versione del {oggi}: {len(rows)} evidenze ({', '.join(f'{v} {k}' for k,v in stati.items())}).

## Dove sono i dati
- `references/archivio.md`: una scheda per evidenza, facile da leggere.
- `references/archivio.csv`: stessi dati, separatore punto e virgola.

## Campi
ID, DATA_RACCOLTA, FONTE, URL, DATA_FONTE, PERIODO_DATI, TEMA, EVIDENZA, NUMERO_CHIAVE, QUALITA, AFFIDABILITA, LIMITI, NOTA_INFERENZA, STATO.

## Regole di lettura
1. Cita sempre l'ID tra parentesi quadre, es. [E07].
2. QUALITA: FATTO = verificabile alla fonte; INFERENZA = stima o interpretazione; LIMITE = dato debole, vecchio, in conflitto o mancante.
3. AFFIDABILITA: A ufficiale o primaria; B associazioni, analisti, media specializzati; C report a pagamento o stampa generica.
4. STATO: VERIFICATO = URL aperto e numero ricontrollato; DA_VERIFICARE = non ancora controllato; MANCANTE = dato cercato e non trovato.
5. NOTA_INFERENZA è una deduzione del team (inizia con IPOTESI): non presentarla mai come fatto della fonte.
6. Se l'utente allega in chat righe più recenti (BLOCCO_HANDOFF o file), quelle si aggiungono a questo archivio: in caso di stesso ID vale la versione più recente.
7. Non inventare righe, numeri o URL che non sono qui o nel materiale allegato.
"""
open(os.path.join(out,'SKILL.md'),'w',encoding='utf-8').write(skill)
shutil.copy(src,os.path.join(out,'references','archivio.csv'))
md=[f"# Archivio evidenze Gruppo 10 (versione {oggi})\n"]
for r in rows:
    md.append(f"## {r['ID']} | {r['TEMA']} | {r['QUALITA']} | affidabilità {r['AFFIDABILITA'] or '-'} | {r['STATO']}\n")
    for k in ['FONTE','URL','DATA_FONTE','PERIODO_DATI','EVIDENZA','NUMERO_CHIAVE','LIMITI','NOTA_INFERENZA','DATA_RACCOLTA']:
        if r[k]: md.append(f"- **{k}**: {r[k]}")
    md.append("")
open(os.path.join(out,'references','archivio.md'),'w',encoding='utf-8').write('\n'.join(md))
z=os.path.join(root,'agenti','skill_archivio_g10.zip')
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as f:
    for root,_,files in os.walk(out):
        for fn in files:
            p=os.path.join(root,fn); f.write(p,os.path.relpath(p,out))
print('creato',z,len(rows),'righe')
