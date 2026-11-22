"""Run an explicit command, preserving arguments, stdout, stderr and timing."""
import sys, subprocess, json, time
from pathlib import Path
from datetime import datetime, timezone
root=Path(__file__).resolve().parents[1]
name=sys.argv[1]
args=sys.argv[2:]
if not args: raise SystemExit('Usage: run_logged.py NAME COMMAND [ARG ...]')
start=time.perf_counter()
p=subprocess.run(args,capture_output=True,text=True)
elapsed=time.perf_counter()-start
out=root/'code/output'/name
out.parent.mkdir(parents=True,exist_ok=True)
out.with_suffix('.stdout.txt').write_text(p.stdout)
out.with_suffix('.stderr.txt').write_text(p.stderr)
out.with_suffix('.run.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'args':args,'cwd':str(Path.cwd()),'seconds':elapsed,'returncode':p.returncode},indent=2)+'\n')
print(p.stdout,end='')
print(p.stderr,end='',file=sys.stderr)
print(json.dumps({'log':str(out),'seconds':round(elapsed,4),'returncode':p.returncode}))
raise SystemExit(p.returncode)
