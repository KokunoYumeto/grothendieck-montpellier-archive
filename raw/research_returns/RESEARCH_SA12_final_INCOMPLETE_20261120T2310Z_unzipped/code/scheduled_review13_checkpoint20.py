"""Review then checkpoint at15:10UTC, never early and with no long blocking wait."""
from pathlib import Path
from datetime import datetime,timezone
import time,subprocess
root=Path(__file__).resolve().parents[1];due=datetime(2026,11,20,15,10,tzinfo=timezone.utc)
remaining=(due-datetime.now(timezone.utc)).total_seconds();assert remaining<=60
if remaining>0:time.sleep(remaining)
for name,args in [('formal_review13',['python3','code/formal_review13.py']),('assemble_checkpoint20',['python3','code/assemble.py']),('inventory_checkpoint20',['python3','code/program_inventory.py']),('checkpoint20_create',['python3','code/checkpoint.py','20'])]:
 subprocess.run(['python3','code/run_logged.py',name]+args,cwd=root,check=True)
