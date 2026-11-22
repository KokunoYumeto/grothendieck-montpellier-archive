"""Compile the auxiliary relative Milnor proof; retain actual run details."""
from datetime import datetime, timezone
import json, os, re, subprocess, time
from pathlib import Path

base = Path(__file__).resolve().parents[1]
research = base.parents[1]
out = base / "output"
name = "K2_relative_Milnor_check"
env = dict(os.environ)
env["TEXMFHOME"] = str(research.parent / "texmf")
tex = ["lualatex", "-fmt=" + str(research / "lualatex.fmt"),
       "-interaction=nonstopmode", "-halt-on-error", name + ".tex"]
commands = [tex, ["bibtex", name], tex, tex, tex]
report = {"started_utc": datetime.now(timezone.utc).isoformat(), "passes": []}
start = time.perf_counter()
logs = []
for cmd in commands:
    t = time.perf_counter()
    r = subprocess.run(cmd, cwd=out, env=env, text=True,
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    report["passes"].append({"command": cmd, "runtime_seconds": time.perf_counter()-t,
                            "returncode": r.returncode})
    logs.append(r.stdout)
    if r.returncode:
        break
report["runtime_seconds"] = time.perf_counter()-start
report["finished_utc"] = datetime.now(timezone.utc).isoformat()
pdf = out / (name + ".pdf")
if pdf.exists():
    report["pdf_bytes"] = pdf.stat().st_size
logpath = out / (name + ".log")
log = logpath.read_text(errors="replace") if logpath.exists() else ""
report["warnings"] = [x for x in log.splitlines() if re.search(r"Warning|Overfull|Underfull|^!", x)]
report["output_line"] = next((x for x in log.splitlines() if x.startswith("Output written on")), None)
(out / "K2_relative_Milnor_build.out").write_text("\n".join(logs))
(out / "K2_relative_Milnor_build.json").write_text(json.dumps(report, indent=2)+"\n")
print(json.dumps(report, indent=2))
