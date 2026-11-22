from pathlib import Path
import csv,json,datetime,hashlib,time
root=Path(__file__).resolve().parents[1];p=root/'notes/manuscript_date_attempts.tsv';start=time.monotonic();before=p.read_bytes();rows=list(csv.DictReader(before.decode().splitlines(),delimiter='\t'))
new=[dict(route='Cartier 211 proof-addition reference / Amemiya–Shiga 1957',evidence='All fourteen Cartier facsimile text pages 85–98 visually read; February 1961 header distinguished from collected edition. Its explicit reference [1] followed to Amemiya–Shiga: full text searched, only pages 161, 166 and 178 visually read.',failed_step='Cartier trace uses are finite rank, and neither inspected source identifies a dated Hilbert trace/genus-zero manuscript. Grothendieck’s 1961 proof addition and Amemiya–Shiga receipt date their own texts, not cote 1.',next_step='A specific contemporary unpublished-proof acknowledgment or dated enclosure matching the manuscript would be needed.',record='notes/algebra_cartier211_source_audit.md'),dict(route='Montpellier cote 162-6 unassigned original pages',evidence='Actual advertised public scan opened; all six physical pages individually displayed and read: modern cover plus five originals concerning gamma/L-factors, Weil-group data and idele/torus diagrams.',failed_step='No matching trace/genus-zero duplicate, legible date, enclosure identifier or target-leaf reference observed. Mathematical subject is not used to infer a year or original dossier.',next_step='A dated duplicate or explicit archival cross-reference identifying the actual proof remains necessary.',record='notes/root_montpellier162_6_date_audit.md')]
for r in new:
 assert not any(x['route']==r['route'] for x in rows)
 assert (root/r['record']).exists()
 rows.append(r)
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['route','evidence','failed_step','next_step','record'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
log={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':len(rows),'added':[x['route'] for x in new],'before_sha256':hashlib.sha256(before).hexdigest(),'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'formal_movement':False,'elapsed_seconds':time.monotonic()-start}
(root/'logs/geometry_route_index_cartier_unassigned_update.json').write_text(json.dumps(log,indent=2)+'\n');print(json.dumps(log))
