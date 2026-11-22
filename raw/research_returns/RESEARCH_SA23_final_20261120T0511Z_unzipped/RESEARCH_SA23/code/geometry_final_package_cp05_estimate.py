"""Refresh a noncreating package estimate including checkpoint05."""
from pathlib import Path
import subprocess,time,json,hashlib
from datetime import datetime,timezone
b=Path(__file__).resolve().parents[1]
argv=['python',str(b/'code/geometry_final_package.py'),'--estimate','--estimate-report',str(b/'notes/geometry_final_package_estimate_cp05.json'),'--plan-report',str(b/'notes/geometry_final_package_plan_cp05.json')]
before=sorted(str(p) for p in b.parent.glob('*.zip'))
t=time.perf_counter();r=subprocess.run(argv,capture_output=True,text=True);elapsed=time.perf_counter()-t
after=sorted(str(p) for p in b.parent.glob('*.zip'))
(b/'logs/geometry_final_package_cp05_estimate_stdout.txt').write_text(r.stdout)
(b/'logs/geometry_final_package_cp05_estimate_stderr.txt').write_text(r.stderr)
meta={'utc':datetime.now(timezone.utc).isoformat(),'argv':argv,'exit_code':r.returncode,'elapsed_seconds':elapsed,'zip_paths_before':before,'zip_paths_after':after,'zip_path_set_unchanged':before==after,'archive_creation_mode_used':False,'mathematical_movement':False}
(b/'logs/geometry_final_package_cp05_estimate.json').write_text(json.dumps(meta,indent=2)+'\n')
print(r.stdout)
print(r.stderr)
print(json.dumps(meta,indent=2))
raise SystemExit(r.returncode)
