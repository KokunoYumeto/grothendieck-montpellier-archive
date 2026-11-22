"""Wait at most sixty seconds, then invoke the time-guarded immutable archive."""
from pathlib import Path
import datetime,time,subprocess,sys
w=Path(__file__).resolve().parents[1]
due=datetime.datetime.fromisoformat('2026-11-20T06:35:40+00:00')
remaining=(due-datetime.datetime.now(datetime.timezone.utc)).total_seconds()
assert remaining<=60, 'Invoke only within one minute of the due time'
if remaining>0:time.sleep(remaining)
subprocess.run([sys.executable,str(w/'code/archive_checkpoint37.py')],cwd=w,check=True)
