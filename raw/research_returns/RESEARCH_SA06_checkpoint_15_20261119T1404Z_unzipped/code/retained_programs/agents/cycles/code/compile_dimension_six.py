"""Retain the complete four-pass standalone C.3ag typesetting check."""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import subprocess
import time

root = Path(__file__).resolve().parents[1]
research = root.parents[1]
out = root/"output"
name = "C3ag_check"
latex = ["lualatex", "-interaction=nonstopmode", "-halt-on-error",
         "-output-directory=agents/cycles/output", f"agents/cycles/output/{name}.tex"]
commands = [latex, ["bibtex", f"agents/cycles/output/{name}"], latex, latex]
environment = os.environ.copy()
environment["TEXMFHOME"] = str(research.parent/"texmf")
started = time.perf_counter()
stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
runs = []
for index, command in enumerate(commands, 1):
    result = subprocess.run(command, cwd=research, env=environment,
                            capture_output=True, text=True)
    path = out/f"{stamp}_C3ag_compile_{index}.txt"
    path.write_text(result.stdout+result.stderr)
    runs.append({"command": command, "returncode": result.returncode,
                 "output": str(path)})
    if result.returncode:
        break
log = (out/f"{name}.log").read_text(errors="replace")
diagnostics = [line for line in log.splitlines()
               if "Overfull" in line or "undefined" in line or line.startswith("!")]
record = {"utc": datetime.now(timezone.utc).isoformat(),
          "runtime_seconds": time.perf_counter()-started,
          "runs": runs, "diagnostics": diagnostics}
(out/"compile_dimension_six.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
