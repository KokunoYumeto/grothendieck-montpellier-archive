"""Create the15:55UTC immutable checkpoint, never early; no formal review."""
from pathlib import Path
from datetime import datetime,timezone
import time,subprocess
root=Path(__file__).resolve().parents[1]
due=datetime(2026,11,20,15,55,tzinfo=timezone.utc)
remaining=(due-datetime.now(timezone.utc)).total_seconds()
assert remaining<=60
if remaining>0:time.sleep(remaining)
for name,args in [
 ('assemble_checkpoint21',['python3','code/assemble.py']),
 ('inventory_checkpoint21',['python3','code/program_inventory.py']),
 ('checkpoint21_create',['python3','code/checkpoint.py','21'])]:
 subprocess.run(['python3','code/run_logged.py',name]+args,cwd=root,check=True)
