"""Create checkpoint30 only at the fixed22:40UTC slot; no formal review is due then."""
from pathlib import Path
from datetime import datetime,timezone
import time,subprocess,json,hashlib
root=Path(__file__).resolve().parents[1]
from estimate_archive_size import estimate
due=datetime(2026,11,20,22,40,tzinfo=timezone.utc)
now=datetime.now(timezone.utc)
remaining=(due-now).total_seconds()
assert -2<=remaining<=60, 'Start this scheduled wrapper in the final minute before22:40UTC.'
qa=json.loads((root/'qa/pdf_verified_checkpoint30.json').read_text())
assert hashlib.sha256((root/'build/RESEARCH_SA12_paper.pdf').read_bytes()).hexdigest()==qa['sha256']
assert not (root.parent/'RESEARCH_SA12_checkpoint_30.zip').exists()
size=estimate(root)
assert size['conservative_bound_bytes']<500_000_000, size
(root/'code/output/checkpoint30_immediate_size_bound.json').write_text(json.dumps(size,indent=2)+'\n')
remaining=(due-datetime.now(timezone.utc)).total_seconds()
assert remaining>=-2, 'Preflight exceeded the scheduled checkpoint window.'
if remaining>0:time.sleep(remaining)
freeze=json.loads((root/'code/output/checkpoint30_source_freeze.json').read_text())
assert freeze['build']==qa['build']
for rel,digest in freeze['files'].items():
 assert hashlib.sha256((root/rel).read_bytes()).hexdigest()==digest, rel
for name,args in [
 ('assemble_checkpoint30',['python3','code/assemble.py']),
 ('inventory_checkpoint30',['python3','code/program_inventory.py']),
 ('checkpoint30_create',['python3','code/checkpoint.py','30'])
]:
 subprocess.run(['python3','code/run_logged.py',name]+args,cwd=root,check=True)
