"""Run and time the exact Part D finite checks, preserving stdout/stderr."""
from pathlib import Path
import subprocess,time,json,sys
P=Path(__file__).resolve().parent
t=time.monotonic()
r=subprocess.run([sys.executable,str(P/'check_part_d.py')],capture_output=True,text=True)
(P/'checks_output.txt').write_text(r.stdout)
(P/'checks_stderr.txt').write_text(r.stderr)
out={'command':[sys.executable,str(P/'check_part_d.py')],'exit_code':r.returncode,'seconds':round(time.monotonic()-t,6),'scope':'Exact finite examples only; no general theorem formalization','stdout':'checks_output.txt','stderr':'checks_stderr.txt'}
(P/'run_checks_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
raise SystemExit(r.returncode)
