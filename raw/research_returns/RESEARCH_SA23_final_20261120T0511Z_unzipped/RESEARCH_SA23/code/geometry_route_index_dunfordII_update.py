from pathlib import Path
import csv,json,datetime,hashlib,time
root=Path(__file__).resolve().parents[1];p=root/'notes/manuscript_date_attempts.tsv';start=time.monotonic();before=p.read_bytes();rows=list(csv.DictReader(before.decode().splitlines(),delimiter='\t'))
r=dict(route='Dunford–Schwartz Part II original historical pages (access limited)',evidence='New exact-title, academic/author-repository and historical-note searches recorded for original English Part II (1963); returned records and citations do not contain the requested original pages.',failed_step='No relevant original page read. New Wiley opening returned 403 and was stopped; prior Google snippet and challenged DjVu routes were not retried. No book-content absence claim follows.',next_step='An independently public original historical note or acknowledgment could be checked for a dated supplied-proof or enclosure identification.',record='notes/algebra_dunfordII_public_repository_search.md')
assert not any(x['route']==r['route'] for x in rows);assert (root/r['record']).exists();rows.append(r)
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['route','evidence','failed_step','next_step','record'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
log={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':len(rows),'added':r['route'],'before_sha256':hashlib.sha256(before).hexdigest(),'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'formal_movement':False,'elapsed_seconds':time.monotonic()-start}
(root/'logs/geometry_route_index_dunfordII_update.json').write_text(json.dumps(log,indent=2)+'\n');print(json.dumps(log))
