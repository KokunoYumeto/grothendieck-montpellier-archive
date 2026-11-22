"""Create checkpoint29 only at the fixed21:55UTC slot; no formal review is due then."""
from pathlib import Path
from datetime import datetime,timezone
import time,subprocess,json,hashlib
root=Path(__file__).resolve().parents[1]
due=datetime(2026,11,20,21,55,tzinfo=timezone.utc)
now=datetime.now(timezone.utc)
remaining=(due-now).total_seconds()
assert -2<=remaining<=60, 'Start this scheduled wrapper in the final minute before21:55UTC.'
qa=json.loads((root/'qa/pdf_verified_checkpoint29.json').read_text())
assert hashlib.sha256((root/'build/RESEARCH_SA12_paper.pdf').read_bytes()).hexdigest()==qa['sha256']
assert not (root.parent/'RESEARCH_SA12_checkpoint_29.zip').exists()
if remaining>0:time.sleep(remaining)
for name,args in [
 ('assemble_checkpoint29',['python3','code/assemble.py']),
 ('inventory_checkpoint29',['python3','code/program_inventory.py']),
 ('checkpoint29_create',['python3','code/checkpoint.py','29'])
]:
 subprocess.run(['python3','code/run_logged.py',name]+args,cwd=root,check=True)
