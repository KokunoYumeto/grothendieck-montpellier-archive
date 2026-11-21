"""Capture complete current work at the user's 45-minute boundaries only."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import hashlib,json,sys,zipfile

root=Path(__file__).resolve().parents[2]
index=int(sys.argv[1])
start=datetime(2026,11,21,0,15,tzinfo=timezone.utc)
due=start+timedelta(minutes=45*index)
now=datetime.now(timezone.utc)
if now<due:raise SystemExit(f'Refusing early checkpoint; due {due.isoformat()}')
if now>due+timedelta(minutes=3):raise SystemExit('Boundary missed; review schedule before writing')
out=root/f'AN_GRH_checkpoint_{index:02d}.zip'
if out.exists():raise SystemExit('Refusing to overwrite an earlier checkpoint')
skip_prefixes=('work/library_helpers/','work/library_upload_helpers/',
               'work/root/archive149_probe/')
files=[]
for base in ('final','work','source'):
    for p in (root/base).rglob('*'):
        if not p.is_file():continue
        rel=p.relative_to(root).as_posix()
        if rel.startswith(skip_prefixes):continue
        if '__pycache__' in p.parts or p.suffix in {'.zip','.pyc'}:continue
        if p.name.startswith('checkpoint_') and p.suffix=='.json':continue
        files.append(p)
for rel in ('AN_GRH_SESSION_STATE.md','upload/PROMPT(20261121-001542).md'):
    files.append(root/rel)
with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(set(files)):z.write(p,p.relative_to(root))
with zipfile.ZipFile(out) as z:
    assert not any(n.endswith('.zip') for n in z.namelist())
    assert z.testzip() is None
meta=dict(filename=out.name,snapshot_at_utc=now.isoformat(),files=len(set(files)),
          bytes=out.stat().st_size,sha256=hashlib.sha256(out.read_bytes()).hexdigest())
(root/f'work/root/checkpoint_{index:02d}_local.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
