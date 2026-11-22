"""Compile C.3be; retain exact commands, elapsed times, and all pass output."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import time

BASE = Path(__file__).resolve().parents[1]
RESEARCH = BASE.parents[1]
OUT = BASE / "output"
NAME = "C3_surface_reduction_Fpbar_check"
env = dict(os.environ)
env["TEXMFHOME"] = str(RESEARCH.parent / "texmf")
tex = ["lualatex", "-fmt=" + str(RESEARCH / "lualatex.fmt"),
       "-interaction=nonstopmode", "-halt-on-error", NAME + ".tex"]
commands = [tex, ["bibtex", NAME], tex, tex, tex]
report = {"started_utc": datetime.now(timezone.utc).isoformat(), "passes": []}
started = time.perf_counter()
logs = []
for command in commands:
    t = time.perf_counter()
    result = subprocess.run(command, cwd=OUT, env=env, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    report["passes"].append({"command": command,
                            "runtime_seconds": time.perf_counter()-t,
                            "returncode": result.returncode})
    logs.append(result.stdout)
    if result.returncode:
        break
report["runtime_seconds"] = time.perf_counter()-started
pdf = OUT / (NAME + ".pdf")
if pdf.exists():
    report["pdf_bytes"] = pdf.stat().st_size
log = (OUT / (NAME + ".log")).read_text(errors="replace")
report["warnings"] = [line for line in log.splitlines()
                      if re.search(r"Warning|Overfull|Underfull|^!", line)]
report["output_line"] = next((line for line in log.splitlines()
                             if line.startswith("Output written on")), None)
(OUT / "C3_surface_reduction_Fpbar_build.out").write_text("\n".join(logs))
(OUT / "C3_surface_reduction_Fpbar_build.json").write_text(
    json.dumps(report, indent=2)+"\n")
print(json.dumps(report, indent=2))
