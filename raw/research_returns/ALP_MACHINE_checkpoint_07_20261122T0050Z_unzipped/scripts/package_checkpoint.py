#!/usr/bin/env python3
"""Create a new, complete checkpoint at its due time; never overwrite one."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import argparse, hashlib, json, zipfile

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('number',type=int)
args=parser.parse_args()
state=json.loads((root/'research/run_state.json').read_text())
now=datetime.now(timezone.utc)
due=datetime.fromisoformat(state['next_checkpoint_due_utc'].replace('Z','+00:00'))
if now<due:
    raise SystemExit('Checkpoint not yet due; no package created.')
if args.number!=state['checkpoint_count']+1:
    raise SystemExit('Checkpoint number is not the next unused count.')
dest=root.parent/'outputs'/f'ALP_MACHINE_checkpoint_{args.number:02d}.zip'
if dest.exists(): raise SystemExit('Refusing to overwrite an earlier checkpoint.')
manifest={'run':'ALP_MACHINE','checkpoint_number':args.number,'created_utc':now.isoformat(),
          'scope':'All current deliverables and work documentation; original supplied attachments remain separate inputs.',
          'files':[]}
contents=[]
captured_state=dict(state)
captured_state.update(checkpoint_count=args.number,
 last_checkpoint_created_utc=now.isoformat(),
 next_checkpoint_due_utc=(due+timedelta(minutes=45)).isoformat())
for path in sorted(root.rglob('*')):
    if not path.is_file():continue
    rel=path.relative_to(root)
    if '__pycache__' in rel.parts or path.suffix in {'.pyc','.zip'}:continue
    if str(rel)=='PACKAGE_MANIFEST.json':continue
    data=((json.dumps(captured_state,indent=2)+'\n').encode()
          if str(rel)=='research/run_state.json' else path.read_bytes())
    contents.append((str(rel),data))
    manifest['files'].append({'path':str(rel),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
manifest_data=(json.dumps(manifest,indent=2)+'\n').encode()
(root/'PACKAGE_MANIFEST.json').write_bytes(manifest_data)
dest.parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for rel,data in contents:z.writestr('ALP_MACHINE/'+rel,data)
    z.writestr('ALP_MACHINE/PACKAGE_MANIFEST.json',manifest_data)
with zipfile.ZipFile(dest) as z:
    assert z.testzip() is None
    assert not any(n.lower().endswith('.zip') for n in z.namelist())
result={'path':str(dest),'created_utc':now.isoformat(),'bytes':dest.stat().st_size,
        'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'entries':len(contents)+1}
print(json.dumps(result,indent=2))
