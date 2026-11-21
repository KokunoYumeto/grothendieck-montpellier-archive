from pathlib import Path
import zipfile,sys,hashlib,json,datetime
base=Path(__file__).resolve().parent.parent
name=sys.argv[1]; target=base/name
if target.exists(): raise SystemExit('Refusing to overwrite existing package: '+name)
files=[]
for p in (base/'deliverable').iterdir():
 if p.suffix in {'.tex','.pdf','.md','.tsv','.json'}:files.append((p,p.name))
for p in sorted((base/'work').rglob('*')):
 # Preserve every source, proof fragment, experiment, rendered check and
 # reproduction helper. Only disposable Python bytecode is excluded.
 if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc':
  if p.suffix == '.zip' and p.name.startswith('ALPOGE_GCT_checkpoint_'):
   continue
  files.append((p,'work/'+str(p.relative_to(base/'work'))))
for p in (base/'sources').rglob('*'):
 if p.is_file():files.append((p,'supplied_sources/'+str(p.relative_to(base/'sources'))))
files.append((base/'upload/PROMPT(20261120-230053).md','TASK_PROMPT.md'))
manifest=[]
with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p,arc in files:
  data=p.read_bytes();z.writestr(arc,data)
  manifest.append({'path':arc,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
 z.writestr('PACKAGE_MANIFEST.json',json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':manifest},indent=2))
with zipfile.ZipFile(target) as z:
 bad=z.testzip()
 if bad:raise SystemExit('Zip integrity failure: '+bad)
print(json.dumps({'path':str(target),'bytes':target.stat().st_size,'entries':len(manifest)+1,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}))
