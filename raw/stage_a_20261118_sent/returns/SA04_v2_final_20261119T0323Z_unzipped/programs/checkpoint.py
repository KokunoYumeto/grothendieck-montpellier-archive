"""Create only a due 45-minute checkpoint, including all current work products.
External copyrighted source copies and original user attachments are excluded.
"""
import datetime,hashlib,json,zipfile,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];WORK=ROOT/'SA04_work'
start=datetime.datetime(2026,11,19,1,13,45,tzinfo=datetime.timezone.utc)
n=int(sys.argv[1]);now=datetime.datetime.now(datetime.timezone.utc)
due=start+datetime.timedelta(minutes=45*n)
if now<due:raise SystemExit('Checkpoint is not due: '+due.isoformat())
out=ROOT/f'SA04_checkpoint_{n:02d}.zip'
if out.exists():raise SystemExit('Never overwrite an existing checkpoint')
with (WORK/'progress.log').open('a') as f:f.write(now.isoformat()+'\tCHECKPOINT\t'+out.name+'; due '+due.isoformat()+'\n')
excluded=[];files=[]
for p in sorted(WORK.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(WORK)
    if rel.parts[0]=='evidence' or p.name=='search_capture.json' or p.suffix in ['.pdf','.dvi','.jpg','.png'] or '__pycache__' in rel.parts:
        excluded.append(str(rel));continue
    files.append(p)
manifest={'created_utc':now.isoformat(),'scheduled_utc':due.isoformat(),'checkpoint':out.name,
          'earlier_checkpoints':[f'SA04_checkpoint_{i:02d}.zip' for i in range(1,n)],
          'source_inputs':'Original attached ZIPs and standalone instructions are not duplicated.',
          'excluded_external_raw_sources':excluded,
          'files':[{'path':str(p.relative_to(WORK)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:z.write(p,str(p.relative_to(WORK)))
    z.writestr('CHECKPOINT_MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
record={'file':str(out),'bytes':out.stat().st_size,'files':len(files),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'created_utc':now.isoformat()}
(WORK/'outputs'/f'checkpoint_{n:02d}.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
