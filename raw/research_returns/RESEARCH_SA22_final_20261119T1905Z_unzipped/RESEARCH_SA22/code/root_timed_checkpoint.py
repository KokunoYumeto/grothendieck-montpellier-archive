"""Create a checkpoint only after45minutes from the last successful save, with measured output."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import json,subprocess,sys,time
R=Path(__file__).resolve().parents[1];n=int(sys.argv[1]);start=time.perf_counter()
now=datetime.now(timezone.utc)
records=json.loads((R/'notes/checkpoint_saved_records.json').read_text())['checkpoints']
last=max(records,key=lambda x:x['saved_utc'])
due=datetime.fromisoformat(last['saved_utc'])+timedelta(minutes=45)
assert now>=due, f'Checkpoint not due until {due.isoformat()}'
target=R/'code'/f'root_timed_checkpoint_{n:02d}_output.json';assert not target.exists()
p=subprocess.run([sys.executable,str(R/'code/make_checkpoint.py'),str(n)],cwd=R,text=True,capture_output=True)
out=dict(checkpoint=n,started_utc=now.isoformat(),due_utc=due.isoformat(),previous=last['name'],
 exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr,seconds=time.perf_counter()-start)
if p.returncode==0:out['archive']=json.loads(p.stdout)
target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));sys.exit(p.returncode)
