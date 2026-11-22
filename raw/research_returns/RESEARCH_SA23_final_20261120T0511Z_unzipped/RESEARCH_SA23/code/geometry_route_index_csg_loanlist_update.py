from pathlib import Path
import csv,json,datetime,hashlib,time
root=Path(__file__).resolve().parents[1];p=root/'notes/manuscript_date_attempts.tsv';start=time.monotonic();before=p.read_bytes();rows=list(csv.DictReader(before.decode().splitlines(),delimiter='\t'))
for r in rows:
 if r['route']=='Montpellier inventory and methodology':
  r['evidence']='Official catalogue distinguishes undated notes from a 1953 letter; original dossiers substantially retained. All 178 public descriptions now read for duplicates; no second explicitly indexed operator-trace dossier identified. Public catalogue is a subset, not the complete internal instrument.'
  r['failed_step']='No recipient or target-leaf identification. Cote 2 is Riemann–Roch; subject-name matches elsewhere concern other mathematics. The fuller internal instrument/name index remains unopened.'
  r['next_step']='An item-level identification of the 1953 letter, dated duplicate or explicit archival cross-reference is needed; catalogue year and dossier adjacency do not date the leaves.'
  r['record']='notes/algebra_history_dating.md; notes/category_montpellier_duplicates_date_audit.md'
new=[dict(route='CSG unpublished-work and transcription finding aids',evidence='Both actual finding-aid pages opened; full returned texts extracted and keyword-searched, with early scientific/correspondence entries and archive-scope paragraphs read.',failed_step='The unpublished list is selective. No newly linked original was inspected and no target proof/date reference found in the returned text; known early correspondence leads repeat the separate Dixmier route.',next_step='A specific public dated duplicate, enclosure or authorial reference identifying the target argument is needed.',record='notes/root_csg_date_audit.md'),dict(route='Montpellier cote 162-1 papers-lent list',evidence='Followed the actual public catalogue link; all ten PDF pages visually inspected: modern cover, original folder and eight manuscript loan-list pages. Functional-analysis references occur on physical pages 3, 8 and 9.',failed_step='Legible entries give no target trace-proof/date/enclosure identification. Some crossed-out words remain undeciphered; generic tensor-product references are not assigned to an unseen manuscript.',next_step='A legible dated loan or enclosure reference must identify the particular proof; publication years or the catalogue lower-date estimate cannot substitute.',record='notes/category_montpellier_duplicates_date_audit.md')]
for r in new:
 assert not any(x['route']==r['route'] for x in rows)
 assert (root/r['record']).exists()
 rows.append(r)
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['route','evidence','failed_step','next_step','record'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
log={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':len(rows),'added':[x['route'] for x in new],'updated_existing':'Montpellier inventory and methodology','before_sha256':hashlib.sha256(before).hexdigest(),'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'formal_movement':False,'elapsed_seconds':time.monotonic()-start}
(root/'logs/geometry_route_index_csg_loanlist_update.json').write_text(json.dumps(log,indent=2)+'\n');print(json.dumps(log))
