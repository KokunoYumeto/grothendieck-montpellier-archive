"""Take an exclusive, byte-verified snapshot without storing the attached scans."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import datetime,sys,time
root=Path('out');ident=sys.argv[1]
if len(sys.argv)>2:
 due=datetime.datetime.fromisoformat(sys.argv[2]).timestamp()
 while time.time()<due:time.sleep(min(30,due-time.time()))
checkpoint=ident!='out'
if checkpoint:
 assembly=b''.join(p.read_bytes() for p in sorted((root/'pages').glob('*.tex')))
 (root/'K58-03_transcription.tex').write_bytes(assembly)
 with (root/'progress.log').open('a') as f:
  print(ident, datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),file=f)
target=Path('/mnt/data')/f'K58-03_{ident}.zip'
files=[p for p in sorted(root.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not(checkpoint and p.name=='PREAMBLE.tex')]
with ZipFile(target,'x',compression=ZIP_DEFLATED,compresslevel=8) as z:
 for p in files:z.write(p,p.as_posix())
with ZipFile(target) as z:
 assert not z.testzip()
 assert len(z.namelist())==len(files)
 if not checkpoint:
  for p in files:assert z.read(p.as_posix())==p.read_bytes()
print(target, len(files), target.stat().st_size)
