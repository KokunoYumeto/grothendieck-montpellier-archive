"""Create an immutable complete checkpoint, excluding input archives and old ZIPs."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import csv, json, hashlib, datetime
root=Path(__file__).resolve().parents[1]
dest=root.parent
existing=list(dest.glob('PS_READERS_checkpoint_*.zip'))
number=max([int(p.stem.rsplit('_',1)[1]) for p in existing]+[0])+1
name=f'PS_READERS_checkpoint_{number:02d}.zip'
pages=list((root/'checked_pages').glob('*.tex'))
status={'checkpoint':name,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checked_page_files':len(pages),'page_keys':[p.stem for p in sorted(pages)],'status':'in progress; consult page and PDF ledgers for verified scope'}
(root/'records/CHECKPOINT_STATE.json').write_text(json.dumps(status,indent=2)+'\n')
files=[p for p in root.rglob('*') if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts]
with ZipFile(dest/name,'x',ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(files):z.write(p,p.relative_to(root))
print(json.dumps({'checkpoint':name,'files':len(files),'bytes':(dest/name).stat().st_size,'checked_pages':len(pages),'sha256':hashlib.sha256((dest/name).read_bytes()).hexdigest()}))
