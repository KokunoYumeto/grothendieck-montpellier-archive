from pathlib import Path
from datetime import datetime,timezone
import time,subprocess
root=Path(__file__).resolve().parents[2]
due=datetime(2026,11,21,4,0,tzinfo=timezone.utc)
while True:
 delay=(due-datetime.now(timezone.utc)).total_seconds()
 if delay<=0:break
 time.sleep(min(delay,10))
subprocess.run(['python3',str(root/'work/root/create_scheduled_checkpoint.py'),'5'],cwd=root,check=True)
