"""Create a new, immutable, scheduled checkpoint; never include older ZIPs."""
from pathlib import Path
import datetime,zipfile,sys,hashlib
root=Path(__file__).resolve().parents[1]
num=int(sys.argv[1])
start=datetime.datetime.fromisoformat('2026-11-19T02:54:34+00:00')
due=start+datetime.timedelta(minutes=45*num)
now=datetime.datetime.now(datetime.timezone.utc)
if now<due:raise SystemExit(f'Not due until {due.isoformat()}')
dest=root.parent/f'OBJ_H035_checkpoint_{num:02}.zip'
if dest.exists():raise SystemExit('Refusing to overwrite existing checkpoint')
with (root/'progress.log').open('a') as f:f.write(f'checkpoint {num:02} created {now.isoformat()}\n')
files=sorted(p for p in root.rglob('*') if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts)
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in files:z.write(p,Path('OBJ_H035')/p.relative_to(root))
print(f'{dest.name}\t{len(files)} files\t{dest.stat().st_size} bytes\tsha256={hashlib.sha256(dest.read_bytes()).hexdigest()}')
