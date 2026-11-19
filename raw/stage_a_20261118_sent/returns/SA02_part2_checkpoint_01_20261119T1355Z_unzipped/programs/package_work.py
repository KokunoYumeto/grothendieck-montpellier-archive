"""Package the current dossier and reproducible work; never overwrite a checkpoint.
External publications are cited and logged, not redistributed as full-text copies.
The uploaded source archive remains a separate prerequisite supplied by the user.
"""
import argparse,datetime,hashlib,json,zipfile
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('name');a=p.parse_args()
W=Path(__file__).resolve().parents[1];dest=W.parent/a.name
if dest.exists():raise SystemExit('Refusing to overwrite '+str(dest))
def excluded(path):
 r=path.relative_to(W).as_posix();n=path.name
 if path.suffix.lower() in {'.zip','.pdf','.ps','.dvi','.gz','.png','.jpg','.jpeg','.tif','.pyc'}:return 'external reference binary or derived image / cache / archive'
 if '__pycache__' in path.parts:return 'Python cache'
 if n.endswith('.txt') and (path.with_suffix('.pdf').exists() or any(s in n for s in ['RS_public','StandardConjs','Voight_quat','Voight_ch','Loos1997','EGAII','EGAIV','SGA1','BichselKnus','Roby1963'])):return 'full external reference text'
 if path.suffix=='.json' and (n.startswith('c84a_') or n=='web_search_records.json' or ('evidence' in path.parts and n.startswith(('open_','search_','Pirashvili_publication')))):return 'raw external retrieval excerpts; concise authored search ledger retained'
 return None
allfiles=sorted(x for x in W.rglob('*') if x.is_file())
omit=[{'path':str(x.relative_to(W)),'reason':excluded(x)} for x in allfiles if excluded(x)]
meta={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'archive_name':a.name,'source_attachment':'SA02_Gomtrie_et_topologie_combinatoire_part2.zip',
 'source_attachment_included':False,'previous_checkpoints_included':False,
 'excluded_external_reference_cache':omit,
 'scope':'All authored deliverables, programs, computational outputs and concise evidence logs currently written. External full-text publications are not redistributed.'}
(W/'outputs/packaging_current.json').write_text(json.dumps(meta,indent=2)+'\n')
files=sorted(x for x in W.rglob('*') if x.is_file() and not excluded(x) and x.name!='ARCHIVE_MANIFEST.json')
manifest=dict(meta,files=[{'path':str(x.relative_to(W)),'bytes':x.stat().st_size,'sha256':hashlib.sha256(x.read_bytes()).hexdigest()} for x in files])
(W/'ARCHIVE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=8) as z:
 for x in files+[W/'ARCHIVE_MANIFEST.json']:z.write(x,str(x.relative_to(W)))
with zipfile.ZipFile(dest) as z:
 bad=z.testzip()
 if bad:raise SystemExit('Bad ZIP member: '+bad)
print(json.dumps({'archive':str(dest),'members':len(files)+1,'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
