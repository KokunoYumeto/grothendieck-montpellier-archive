"""Run the12:10 review and checkpoint in order, never early."""
from pathlib import Path
from datetime import datetime,timezone
import time,subprocess
root=Path(__file__).resolve().parents[1]
due=datetime(2026,11,20,12,10,tzinfo=timezone.utc)
remaining=(due-datetime.now(timezone.utc)).total_seconds()
assert remaining<=60,'Do not block more than60seconds for this schedule.'
if remaining>0:time.sleep(remaining)
for name,args in [
 ('formal_review10',['python3','code/formal_review10.py']),
 ('assemble_review10',['python3','code/assemble.py']),
 ('inventory_checkpoint16',['python3','code/program_inventory.py']),
 ('checkpoint16_create',['python3','code/checkpoint.py','16'])
]:
 subprocess.run(['python3','code/run_logged.py',name]+args,cwd=root,check=True)
