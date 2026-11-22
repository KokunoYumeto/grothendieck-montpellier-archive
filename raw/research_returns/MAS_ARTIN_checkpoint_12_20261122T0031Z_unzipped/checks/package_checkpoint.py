"""Package a complete research snapshot without copyrighted draft copies or old archives."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, sys, zipfile
ROOT=Path(__file__).resolve().parents[1]
num=int(sys.argv[1])
output=ROOT.parent/f'MAS_ARTIN_checkpoint_{num:02d}.zip'
assert not output.exists(),f'Refusing to overwrite {output}'
files=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts: continue
    if 'private_sources' in p.relative_to(ROOT).parts: continue
    if p.suffix.lower() in {'.zip','.pyc','.aux','.out','.toc','.log'}: continue
    if p.name=='CHECKPOINT_MANIFEST.tsv': continue
    name=p.name.lower()
    assert not ('masullo' in name and p.suffix.lower() in {'.pdf','.png','.jpg','.txt'}),f'Private source accidentally present: {p}'
    files.append(p)
rows=[]
contents=[]
for p in files:
    data=p.read_bytes();rel=p.relative_to(ROOT).as_posix()
    rows.append([rel,len(data),hashlib.sha256(data).hexdigest()]);contents.append((rel,data))
manifest=ROOT/'CHECKPOINT_MANIFEST.tsv'
with manifest.open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['path','bytes','sha256']);w.writerows(rows)
with zipfile.ZipFile(output,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for rel,data in contents:z.writestr('MAS_ARTIN_work/'+rel,data)
    z.write(manifest,'MAS_ARTIN_work/CHECKPOINT_MANIFEST.tsv')
with zipfile.ZipFile(output) as z:
    assert z.testzip() is None
    assert not any(n.lower().endswith('.zip') for n in z.namelist())
report={'checkpoint':num,'created_utc':datetime.now(timezone.utc).isoformat(),'path':str(output),'files':len(contents)+1,'bytes':output.stat().st_size,'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'archive_integrity':'PASS','earlier_archives_nested':False,'copyrighted_Masullo_source_included':False}
print(json.dumps(report,indent=2))
