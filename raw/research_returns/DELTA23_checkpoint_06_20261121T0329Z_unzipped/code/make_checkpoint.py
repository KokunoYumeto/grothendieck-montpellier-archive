"""Create one complete, immutable checkpoint ZIP at its scheduled time."""
from pathlib import Path
import argparse, datetime, hashlib, json, subprocess, sys, zipfile

p=argparse.ArgumentParser()
p.add_argument('number',type=int)
p.add_argument('scheduled_utc')
a=p.parse_args()
root=Path(__file__).resolve().parents[2]
now=datetime.datetime.now(datetime.timezone.utc)
due=datetime.datetime.fromisoformat(a.scheduled_utc.replace('Z','+00:00'))
if now < due:
    raise SystemExit('Checkpoint is not due; no ZIP was created.')
name=f'DELTA23_checkpoint_{a.number:02}.zip'
target=root/name
if target.exists():
    raise SystemExit('Refusing to overwrite an earlier checkpoint.')
work=root/'work'; package=work/'package'
meta={'name':name,'scheduled_utc':due.isoformat(),'snapshot_utc':now.isoformat(),
      'scope':'Complete current deliverables and recovery documentation, relative to the supplied source archive.',
      'prior_checkpoint_archives_included':False}
(work/'records'/f'checkpoint_{a.number:02}_snapshot.json').write_text(json.dumps(meta,indent=2)+'\n')
subprocess.run([sys.executable,str(work/'code/sync_package.py')],check=True)
paths=sorted(x for x in package.rglob('*') if x.is_file())
if any(x.suffix.lower()=='.zip' for x in paths):
    raise SystemExit('Refusing nested ZIP archive.')
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for path in paths:z.write(path,path.relative_to(package))
with zipfile.ZipFile(target) as z:
    if z.testzip() is not None:raise RuntimeError('ZIP validation failed.')
    manifest=json.loads(z.read('PACKAGE_MANIFEST.json'))
    for item in manifest:
        if hashlib.sha256(z.read(item['path'])).hexdigest()!=item['sha256']:
            raise RuntimeError('Manifest validation failed: '+item['path'])
print(json.dumps({'name':name,'path':str(target),'snapshot_utc':now.isoformat(),
                 'bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
                 'files':len(paths)}))
