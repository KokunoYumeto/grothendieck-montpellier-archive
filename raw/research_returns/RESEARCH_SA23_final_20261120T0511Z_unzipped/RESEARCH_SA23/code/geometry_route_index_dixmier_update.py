from pathlib import Path
import csv,json,hashlib,datetime,time
root=Path(__file__).resolve().parents[1];p=root/'notes/manuscript_date_attempts.tsv';start=time.monotonic(); before=p.read_bytes();rows=list(csv.DictReader(before.decode().splitlines(),delimiter='\t'))
route='Dixmier 1957 first edition and historical notes (original unopened)'
if any(r['route']==route for r in rows): raise RuntimeError('already added')
rows.append(dict(route=route,evidence='CiNii first-edition metadata, distinct Open Library 1957/1969 records, Google Books 1969 metadata, Gabay revised-edition description and contents, and Cooper 1958 review metadata opened.',failed_step='No original 1957 book page, review text or preview image was read. Later revised editions cannot certify wording in the first edition; no target manuscript-date witness obtained.',next_step='An independently public original 1957 preface, acknowledgments or historical note could be inspected for a dated unpublished-proof identification.',record='notes/algebra_dixmier1957_source_search.md'))
for r in rows:
 if r['route']=='Bourbaki congress minutes 803 and804':
  r['route']='Bourbaki congress minutes 803 and 804'
  r['evidence']='Original covers and all 16/6 typed main pages directly read. Original headings date 24 June–7 July 1956 and 7–14 October 1956; R230/part Ib circulation and further part Ic assignments are explicit.'
  r['failed_step']='No target proof, Weyl/genus-zero discussion or manuscript enclosure identified in the main minutes. Twenty/sixteen appendix pages unread; some record 804 right-edge text is clipped in the source.'
 if r['route']=='Bourbaki congress minutes 802 and805':
  r['route']='Bourbaki congress minutes 802 and 805'
  r['evidence']='Each original modern cover and complete six-page main fascicle visually read. Original headings date 11–17 March 1956 and 17–24 March 1957; both list R230.'
  r['failed_step']='No target trace/genus-zero draft or enclosure identified. This is identifier-level circulation evidence, not line-for-line identification of the surviving IECL text. Remaining 29/21 appendix pages unread.'
 if r['route']=='Two original 1954 Comptes rendus notes':
  r['evidence']='Both originals, CR 239 pp. 577–579 and 607–609, read fully, with all six original pages visually inspected; printed session and publication dates recorded.'
 if r['route']=='Villavicencio–Mendoza 1954 contribution (original pending)':
  r['evidence']='Finnish institutional catalogue and CSG21 metadata opened; original Korányi volume review, Acta scient. math. 17 (1956), p. 265, visually read.'
  r['failed_step']='Grothendieck pp. 173–177 and full volume remain unopened. UNESCO and linked review routes returned 403 and were stopped; the read review lists contributors but no target proof.'
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['route','evidence','failed_step','next_step','record'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
for r in rows:
 for q in r['record'].split('; '):
  assert (root/q).is_file(),q
log={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':len(rows),'added_route':route,'format_only_changes':'spacing in four recently added rows','before_sha256':hashlib.sha256(before).hexdigest(),'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'all_record_paths_exist':True,'elapsed_seconds':time.monotonic()-start,'formal_movement':False}
(root/'logs/geometry_route_index_dixmier_update.json').write_text(json.dumps(log,indent=2)+'\n');print(json.dumps(log))
