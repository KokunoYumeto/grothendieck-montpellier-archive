"""Create a complete research ZIP; checkpoint time gating is deliberate."""
from pathlib import Path
import argparse, hashlib, json, zipfile
from datetime import datetime, timezone, timedelta
root=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('kind',choices=['checkpoint','final']);ap.add_argument('--number',type=int);args=ap.parse_args()
now=datetime.now(timezone.utc)
if args.kind=='checkpoint':
 if not args.number or args.number<1: raise SystemExit('Checkpoint number required')
 due=datetime(2026,11,20,23,0,tzinfo=timezone.utc)+timedelta(minutes=45*args.number)
 if now<due: raise SystemExit(f'Not due: {due.isoformat()}')
 name=f'GCT_NSRH_checkpoint_{args.number:02d}.zip'
else: name='GCT_NSRH_final.zip'
out=root.parent/name
if out.exists(): raise SystemExit(f'Refusing overwrite: {out}')
exclude_dirs={'tex_check','source_build','__pycache__','qa','rendered'}
allowed={'.tex','.pdf','.md','.tsv','.json','.py','.txt','.log'}
files=[]
for p in sorted(root.rglob('*')):
 if not p.is_file() or p.suffix not in allowed: continue
 rel=p.relative_to(root)
 if any(part in exclude_dirs or part.startswith('.') for part in rel.parts): continue
 if rel.parts[0]=='primary_sources' and p.suffix not in {'.py','.md','.tsv','.json'}: continue
 if p.name=='missfont.log': continue
 files.append(p)
# Snapshot each member once so an agent's later report update cannot make
# its packaged bytes differ from the recorded member hash.
payloads=[(str(p.relative_to(root)),p.read_bytes()) for p in files]
manifest={'package':name,'created_utc':now.isoformat(),'status':'WORK IN PROGRESS; active research' if args.kind=='checkpoint' else 'See README and QUESTIONS.tsv','files':[{'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()} for rel,data in payloads]}
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for rel,data in payloads:z.writestr(rel,data)
 z.writestr('PACKAGE_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(out) as z:
 bad=z.testzip()
 if bad:raise SystemExit(f'Corrupt member {bad}')
 required={'GCT_NSRH.tex','QUESTIONS.tsv','LEDGER.md','CHECK_EVENTS.tsv','IMPLICATIONS.md'}
 assert required<=set(z.namelist())
 assert not any(n.endswith('.zip') for n in z.namelist())
print(json.dumps({'path':str(out),'bytes':out.stat().st_size,'members':len(files)+1,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'created_utc':now.isoformat()}))
