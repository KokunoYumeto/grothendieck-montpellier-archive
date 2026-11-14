"""Write a new, non-overwriting checkpoint of all edition work, excluding supplied scans."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import json,sys,datetime
sys.path.insert(0,str(Path(__file__).parent))
import audit_record
ROOT=Path(__file__).resolve().parents[1]
out=ROOT.parent/'checkpoints';out.mkdir(exist_ok=True)
numbers=[int(p.stem.rsplit('_',1)[1]) for p in out.glob('EGA_V_READERS_checkpoint_*.zip')]
n=max(numbers,default=0)+1
p=out/f'EGA_V_READERS_checkpoint_{n:02}.zip'
audit_record.aggregate()
with ZipFile(p,'x',compression=ZIP_DEFLATED) as z:
 for f in sorted(ROOT.rglob('*')):
  if not f.is_file() or '__pycache__' in f.parts:continue
  if f.suffix.lower() in {'.jpg','.jpeg','.png'}:continue
  if f.name.startswith('EGA_V_READERS_checkpoint_'):continue
  z.write(f,Path('edition')/f.relative_to(ROOT))
print(json.dumps(dict(path=str(p),name=p.name,bytes=p.stat().st_size,pages_checked=len(list((ROOT/'checked_pages').glob('*.tex'))))))
