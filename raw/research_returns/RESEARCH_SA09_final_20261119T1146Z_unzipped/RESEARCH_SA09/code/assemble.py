"""Assemble independent statement/source/event fragments without changing them."""
from pathlib import Path
import csv, json, re, datetime
ROOT=Path(__file__).resolve().parents[1]
fragments=['A1','A2_A4','A3_B4','B']
rows=[]
events=[]
bibs=[]
for part in fragments:
 with (ROOT/'notes'/f'{part}_results.csv').open(newline='') as f:
  rows.extend(csv.DictReader(f))
 with (ROOT/'notes'/f'{part}_CHECK_EVENTS.tsv').open(newline='') as f:
  reader=csv.reader(f,delimiter='\t');header=next(reader)
  for row in reader:
   if len(row)==len(header):
    d=dict(zip(header,row))
    # Agent fragments use equivalent header names; normalize explicitly.
    events.append([d.get('statement_id',d.get('id','')),d.get('date',''),d.get('who',''),d.get('type',''),d.get('outcome','')])
   else: raise ValueError((part,'bad event row',row))
 bibs.append((ROOT/'notes'/f'{part}_references.bib').read_text())
extra=ROOT/'notes'/'extra_requested_references.bib'
if extra.exists(): bibs.append(extra.read_text())
for extra_events in [ROOT/'notes'/'requested_sources_CHECK_EVENTS.tsv',ROOT/'notes'/'root_CHECK_EVENTS.tsv']:
 if extra_events.exists():
  with extra_events.open(newline='') as f:
   for d in csv.DictReader(f,delimiter='\t'):
    outcome=d.get('outcome','')
    if d.get('manuscript_pages'): outcome+=' Manuscript: '+d['manuscript_pages']+'.'
    events.append([d.get('statement_id',d.get('id','')),d.get('date',''),d.get('who',''),d.get('type',''),outcome])
ids=[r['id'] for r in rows]
assert len(set(ids))==len(ids),ids
def key(r):
 m=re.fullmatch(r'([AB])(\d+)\.(\d+)',r['id'])
 return (m[1],int(m[2]),int(m[3]))
rows.sort(key=key)
with (ROOT/'RESEARCH_SA09_results.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['id','statement','status','where_proved','depends_on','manuscript_pages','notes'])
 w.writeheader();w.writerows(rows)
with (ROOT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 assert all(len(row)==5 for row in events)
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(events)
bib='\n\n'.join(bibs)
keys=re.findall(r'@\w+\s*\{\s*([^,]+)',bib)
assert len(set(keys))==len(keys),keys
(ROOT/'RESEARCH_SA09_references.bib').write_text(bib)
all_tex='\n'.join((ROOT/'sections'/name).read_text() for name in ['A1.tex','A2.tex','A3.tex','A4.tex','B1_B2_B3.tex','B4.tex'])
statement_ids=re.findall(r'\\paragraph\{([AB]\d+\.\d+)\s*\(',all_tex)
assert set(statement_ids)==set(ids),(set(statement_ids)-set(ids),set(ids)-set(statement_ids))
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'numbered_statements':len(rows),'check_events':len(events),'bibliography_entries':len(keys),'all_numbered_statements_have_registry_rows':True}
(ROOT/'logs'/'assembly.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result))
