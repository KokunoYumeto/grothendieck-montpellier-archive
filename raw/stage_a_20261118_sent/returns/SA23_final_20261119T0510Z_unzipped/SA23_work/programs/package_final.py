#!/usr/bin/env python3
"""Package the completed dossier after validation, without copying source caches."""
import json,hashlib,zipfile,re,datetime
from pathlib import Path
W=Path(__file__).resolve().parents[1];dest=W.parent/'SA23.zip'
validation=json.loads((W/'outputs/final_validation.json').read_text())
assert validation['passed']and not validation['errors'],'Final validation must pass.'
assert not dest.exists(),'Final artifact is created once after the completed review.'
required=['SA23_dossier.md','SA23_entries.tsv','SA23_items.json','SA23_claims.json','SA23_problems.json','SA23_readings.tsv','SA23_links.tsv','SA23_directions.md','SA23_references.bib','CHECK_EVENTS.tsv','progress.log']
for name in required:assert(W/name).is_file(),name
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
report={'created_utc':now,'artifact':'SA23.zip','validation':'outputs/final_validation.json','validation_passed':True,'required_deliverables':required,'scope':'Full completed dossier and authored work documentation. Original attachments and extracted inputs, external full publications, raw search caches, earlier archives and Python bytecode are excluded.','top_level':'SA23_work/'}
(W/'outputs/final_package_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
members=[]
for p in sorted(W.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(W)
 if 'external'in rel.parts or'__pycache__'in rel.parts or p.suffix.lower()=='.zip':continue
 if re.fullmatch(r'search_\d+\.json',p.name):continue
 if rel.as_posix()in ['FINAL_MANIFEST.json','outputs/final_archive_delivery.json']:continue
 data=p.read_bytes();members.append({'path':'SA23_work/'+str(rel),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
manifest={'created_utc':now,'artifact':'SA23.zip','status':'completed','files':members,'required_deliverables':required,'source_inventory':'SA23_work/SA23_source_coverage.tsv','validation':'SA23_work/outputs/final_validation.json','note':'This manifest lists every content file except the manifest itself. Original attachments remain separate user-supplied inputs. No earlier checkpoint archive is nested.'}
(W/'FINAL_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED,compresslevel=6)as z:
 for row in members:z.write(W/row['path'].removeprefix('SA23_work/'),row['path'])
 z.write(W/'FINAL_MANIFEST.json','SA23_work/FINAL_MANIFEST.json')
with zipfile.ZipFile(dest)as z:
 assert z.testzip()is None,'ZIP CRC verification failed.'
 for row in members:
  assert hashlib.sha256(z.read(row['path'])).hexdigest()==row['sha256'],row['path']
 assert not any(n.lower().endswith('.zip')for n in z.namelist()),'Nested archive.'
delivery={'path':str(dest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'members':len(members)+1,'created_utc':now,'manifest_hashes_verified':True}
(W/'outputs/final_archive_delivery.json').write_text(json.dumps(delivery,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(delivery,ensure_ascii=False))
