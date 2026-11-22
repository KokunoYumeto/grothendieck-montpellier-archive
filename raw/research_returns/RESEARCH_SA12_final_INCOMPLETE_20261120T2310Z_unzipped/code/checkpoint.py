"""Create a scheduled, immutable research checkpoint; never embeds inputs or prior ZIPs."""
import sys,zipfile,json,hashlib,time,shutil
from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
number=int(sys.argv[1]); start=time.perf_counter()
out=root.parent/f'RESEARCH_SA12_checkpoint_{number:02d}.zip'
if out.exists():raise SystemExit('Refusing to overwrite existing checkpoint')
if not (root/'qa/pdf_verified.json').exists():raise SystemExit('PDF verification record required')
qa=json.loads((root/'qa/pdf_verified.json').read_text())
actual_hash=hashlib.sha256((root/'build/RESEARCH_SA12_paper.pdf').read_bytes()).hexdigest()
if number>1 and qa.get('sha256')!=actual_hash:raise SystemExit('Current PDF hash does not match completed verification')
shutil.copy2(root/'build/RESEARCH_SA12_paper.pdf',root/'RESEARCH_SA12_paper.pdf')
manifest=[]
created_utc=datetime.now(timezone.utc).isoformat()
paths=[p for p in sorted(root.rglob('*'))
       if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts
       and p.name!='CHECKPOINT_MANIFEST.json']
with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in paths:
        # Hash precisely the bytes written, so ongoing separate research cannot
        # create a mismatch between an earlier hash pass and a later ZIP read.
        data=p.read_bytes()
        rel=str(p.relative_to(root))
        manifest.append({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
        z.writestr(str(Path(root.name)/rel),data)
    record={'checkpoint':number,'utc':created_utc,'prior_checkpoints':[f'RESEARCH_SA12_checkpoint_{i:02d}.zip' for i in range(1,number) if i not in (10,11,12,28)],'missed_scheduled_slots':[i for i in (10,11,12,28) if i<number],'files':manifest,'note':'Current deliverables and all work documentation. Inputs supplied by user excluded. Earlier checkpoints not embedded. Each member is hashed from the exact bytes written in this archive.'}
    manifest_bytes=(json.dumps(record,indent=2)+'\n').encode()
    (root/'CHECKPOINT_MANIFEST.json').write_bytes(manifest_bytes)
    z.writestr(str(Path(root.name)/'CHECKPOINT_MANIFEST.json'),manifest_bytes)
assert out.stat().st_size<500_000_000
print(json.dumps({'archive':str(out),'bytes':out.stat().st_size,'files':len(manifest)+1,'seconds':time.perf_counter()-start}))

