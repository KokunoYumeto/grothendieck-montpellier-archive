"""Compile the new C.1n fragment; preserve command output and diagnostics."""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import subprocess
import time

ROOT=Path(__file__).resolve().parents[1]
RESEARCH=ROOT.parents[1]
OUT=ROOT/"output"
commands=[
    ["lualatex","-interaction=nonstopmode","-halt-on-error","-output-directory=agents/cycles/output","agents/cycles/output/C1_endpoint_check.tex"],
    ["bibtex","agents/cycles/output/C1_endpoint_check"],
    ["lualatex","-interaction=nonstopmode","-halt-on-error","-output-directory=agents/cycles/output","agents/cycles/output/C1_endpoint_check.tex"],
    ["lualatex","-interaction=nonstopmode","-halt-on-error","-output-directory=agents/cycles/output","agents/cycles/output/C1_endpoint_check.tex"],
]
start=time.perf_counter()
stamp=datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
environment=os.environ.copy()
environment["TEXMFHOME"]=str(RESEARCH.parent/"texmf")
records=[]
for i,cmd in enumerate(commands,1):
    run=subprocess.run(cmd,cwd=RESEARCH,env=environment,capture_output=True,text=True)
    path=OUT/f"{stamp}_C1_endpoint_compile_{i}.txt"
    path.write_text(run.stdout+run.stderr)
    records.append({"command":cmd,"exit":run.returncode,"output":str(path)})
    if run.returncode:
        break
log=(OUT/"C1_endpoint_check.log").read_text(errors="replace") if (OUT/"C1_endpoint_check.log").exists() else ""
diagnostics=[line for line in log.splitlines() if "Overfull" in line or "undefined" in line or line.startswith("!")]
result={"utc":datetime.now(timezone.utc).isoformat(),"seconds":time.perf_counter()-start,"commands":records,"diagnostics":diagnostics}
(OUT/"compile_endpoint_image.json").write_text(json.dumps(result,indent=2)+"\n")
(OUT/f"{stamp}_compile_endpoint_image.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
