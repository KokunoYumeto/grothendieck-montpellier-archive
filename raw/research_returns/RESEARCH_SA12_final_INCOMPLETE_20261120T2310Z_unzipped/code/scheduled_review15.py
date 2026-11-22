"""Run review15 at17:10UTC with a bounded scheduling wait; creates no archive."""
from datetime import datetime,timezone
from pathlib import Path
import time,subprocess
root=Path(__file__).resolve().parents[1]
due=datetime(2026,11,20,17,10,tzinfo=timezone.utc)
remaining=(due-datetime.now(timezone.utc)).total_seconds()
assert remaining<=60
if remaining>0:time.sleep(remaining)
for label,args in [('formal_review15',['python3','code/formal_review15.py']),('assemble_review15',['python3','code/assemble.py']),('inventory_review15',['python3','code/program_inventory.py'])]:
 subprocess.run(['python3','code/run_logged.py',label]+args,cwd=root,check=True)
