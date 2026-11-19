"""Rerun the four delivered mathematical certificates as an integration gate."""
from pathlib import Path
import subprocess, sys, time, json
ROOT=Path(__file__).resolve().parents[1]
scripts=['a1_checks.py','a2_a4_checks.py','a3_b4_verify.py','B1_B2_B3_certificate.py']
records=[]
for script in scripts:
 start=time.perf_counter()
 proc=subprocess.run([sys.executable,str(ROOT/'code'/script)],cwd=ROOT.parent,capture_output=True,text=True)
 log=ROOT/'logs'/('final_'+script.removesuffix('.py')+'.txt')
 log.write_text(proc.stdout+proc.stderr)
 rec={'script':'code/'+script,'exit_code':proc.returncode,'wall_seconds':round(time.perf_counter()-start,6),'captured_output':str(log.relative_to(ROOT))}
 records.append(rec);print(json.dumps(rec),flush=True)
 if proc.returncode: raise SystemExit(proc.returncode)
(ROOT/'logs'/'final_certificate_runs.json').write_text(json.dumps(records,indent=2))
