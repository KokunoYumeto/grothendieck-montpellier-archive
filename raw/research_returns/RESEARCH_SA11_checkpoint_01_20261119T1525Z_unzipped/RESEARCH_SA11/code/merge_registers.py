#!/usr/bin/env python3
"""Normalize all result and check-event registers without losing branch originals."""
from pathlib import Path
import csv
root=Path(__file__).resolve().parent.parent
fields=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
rows=[]
for name in ['audit/extension_results.csv','notes/counts_results.csv','notes/polygons_results.csv']:
 with (root/name).open() as f:
  for r in csv.DictReader(f):
   r={k:r.get(k,'') for k in fields}
   s=r['status'];r['status']='Refuted' if s.startswith('Refuted') else 'Known' if s.startswith('Known') else 'Proved under stated hypotheses' if s.startswith('Proved under') else 'Proved'
   r['where_proved']='RESEARCH_SA11_paper.tex, Statement '+r['id']+'; '+r['where_proved']
   rows.append(r)
for id,statement,dep,pages,status,notes in [
 ('T1','Repeated-vertex gen-gen gaps contain a specialization or an exceptional corridor','P7 P8; SZ1993 Corollary4.5','154/035-039 154/093','Proved','Finite acyclic program and exposed fan proof; multiple vertices allowed'),
 ('T2','Every all-ordinary corner circuit is a four-cycle with four distinct relative positions','T1; independent resolutions','154/039-045 154/151 154/154','Proved','Tracks the prescribed reflected endpoints; no bound on the number of specializations'),
 ('T3','X_2 is a compact connected nonorientable surface with embedded closed cells and s2=F(1), s1=2Fprime(1)+2b, s0=Fprime(1)+b','T1 T2 E1 E2; SA10-A4.3','154/005 154/007 154/035-045 154/064 154/120','Proved','Explicit flag circuits, Mobius bands, links and no-zigzag embeddings'),
 ('T4','L4 literal tether/chord identification is false; proper chords with a marked point correspond to pairs of interior-to-boundary tethers','Endpoint-type invariance; exact finite certificate','156-4/032 156-4/045 154/035','Refuted','Typed-arc counterexample, not a model of unspecified 1986 axioms; both readings of the doubtful negation covered')]:
 rows.append(dict(zip(fields,[id,statement,status,'RESEARCH_SA11_paper.tex, Statement '+id,dep,pages,notes])))
assert len(rows)==25 and len({r['id'] for r in rows})==25
with (root/'RESEARCH_SA11_results.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
base=root/'audit/root_initial_CHECK_EVENTS.tsv'
if not base.exists():base.write_bytes((root/'CHECK_EVENTS.tsv').read_bytes())
events=[]
for name in ['audit/root_initial_CHECK_EVENTS.tsv','audit/extension_CHECK_EVENTS.tsv','notes/counts_CHECK_EVENTS.tsv','notes/polygons_CHECK_EVENTS.tsv','audit/root_final_CHECK_EVENTS.tsv']:
 p=root/name
 if not p.exists():continue
 with p.open() as f:
  for r in csv.DictReader(f,delimiter='\t'):
   events.append([r.get('statement_id',r.get('id','')),r.get('date',r.get('date_utc','')),r['who'],r.get('type',r.get('how','')),r.get('outcome',r.get('result',''))+(' Locator: '+r['where'] if r.get('where') else '')])
with (root/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(events)
print(f'{len(rows)} statements; {len(events)} check events')
