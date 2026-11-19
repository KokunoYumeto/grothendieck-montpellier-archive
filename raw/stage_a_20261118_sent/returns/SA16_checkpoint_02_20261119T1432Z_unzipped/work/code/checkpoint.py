#!/usr/bin/env python3
"""Create the requested complete, non-overwriting 45-minute checkpoint ZIP."""
from pathlib import Path
import zipfile,datetime,json,re,hashlib,sys
root=Path(__file__).resolve().parents[2];now=datetime.datetime.now(datetime.timezone.utc)
log=root/'work/progress.log'
text=log.read_text();first=re.search(r'2026-11-19T13:02:36\.687537\+00:00',text)
start=datetime.datetime.fromisoformat('2026-11-19T13:02:36.687537+00:00')
out=root/'checkpoints';out.mkdir(exist_ok=True)
existing=sorted(out.glob('SA16_checkpoint_[0-9][0-9].zip'))
n=len(existing)+1;due=start+datetime.timedelta(minutes=45*n)
if now<due:
 print(json.dumps({'created':False,'next_due_utc':due.isoformat(),'now':now.isoformat()}));sys.exit(0)
target=out/f'SA16_checkpoint_{n:02}.zip'
if target.exists():raise RuntimeError('Never overwrite a checkpoint')
with log.open('a') as f:f.write(f'{now.isoformat()}\tcheckpoint {n:02} scheduled interval reached; writing current complete work bundle\n')
paths=sorted(p for p in (root/'work').rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix.lower()!='.pdf')
deliver=root/'deliverables'
if deliver.exists():paths+=sorted(p for p in deliver.rglob('*') if p.is_file())
with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in paths:z.write(p,str(p.relative_to(root)))
 z.writestr('CHECKPOINT_MANIFEST.txt',f'Checkpoint {n:02}\nUTC {now.isoformat()}\nWork start {start.isoformat()}\nEarlier checkpoint names: '+', '.join(p.name for p in existing)+'\nSources are not included; restore the original attachment once into sources/.\nAll current part records, programs, outputs and progress logs are in work/.\n')
record={'number':n,'path':str(target),'created_utc':now.isoformat(),'scheduled_due_utc':due.isoformat(),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'bytes':target.stat().st_size,'files':len(paths)}
(out/f'SA16_checkpoint_{n:02}_manifest.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
