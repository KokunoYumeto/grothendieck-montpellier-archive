"""Create the13:40UTC immutable checkpoint, never early; no formal review."""
from pathlib import Path
from datetime import datetime, timezone
import time, subprocess
root=Path(__file__).resolve().parents[1]
due=datetime(2026,11,20,13,40,tzinfo=timezone.utc)
remaining=(due-datetime.now(timezone.utc)).total_seconds()
assert remaining<=60,'Do not block more than60seconds for this schedule.'
if remaining>0:time.sleep(remaining)
for name,args in [
    ('assemble_checkpoint18',['python3','code/assemble.py']),
    ('inventory_checkpoint18',['python3','code/program_inventory.py']),
    ('checkpoint18_create',['python3','code/checkpoint.py','18'])]:
    subprocess.run(['python3','code/run_logged.py',name]+args,cwd=root,check=True)
