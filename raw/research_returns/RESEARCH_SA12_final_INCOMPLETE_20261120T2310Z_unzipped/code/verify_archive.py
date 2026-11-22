"""Verify an already created immutable checkpoint; never changes the ZIP."""
from pathlib import Path
from datetime import datetime,timezone
import sys,zipfile,hashlib,json,time
root=Path(__file__).resolve().parents[1];number=int(sys.argv[1]);t=time.perf_counter()
path=root.parent/f'RESEARCH_SA12_checkpoint_{number:02d}.zip'
assert path.stat().st_size<500_000_000
with zipfile.ZipFile(path) as z:
 assert z.testzip() is None
 names=z.namelist();assert not any(n.endswith('.zip') for n in names)
 manifest=json.loads(z.read('RESEARCH_SA12/CHECKPOINT_MANIFEST.json'))
 qa=json.loads(z.read('RESEARCH_SA12/qa/pdf_verified.json'))
 pdf_digest=hashlib.sha256(z.read('RESEARCH_SA12/RESEARCH_SA12_paper.pdf')).hexdigest()
 assert pdf_digest==qa['sha256']
 assert hashlib.sha256(z.read('RESEARCH_SA12/build/RESEARCH_SA12_paper.pdf')).hexdigest()==pdf_digest
record={'utc':datetime.now(timezone.utc).isoformat(),'archive':str(path),'bytes':path.stat().st_size,'members':len(names),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'full_crc':'PASS','pdf_sha256':pdf_digest,'pdf_pages':qa['pages'],'manifest_utc':manifest['utc'],'seconds':time.perf_counter()-t}
(root/f'code/output/checkpoint{number:02d}_hash.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
