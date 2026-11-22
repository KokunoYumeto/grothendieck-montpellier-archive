"""Retained standalone typesetting check for the auxiliary integral Chow lemma."""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import json
import os
import subprocess

base = Path(__file__).resolve().parents[1]
research = base.parents[1]
output = base / "output"
name = "exceptional_cubic_lattice_check"
wrapper = r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=27mm]{geometry}
\usepackage{amsmath,amsthm,amssymb,mathtools,natbib,longtable,booktabs,hyperref}
\begin{document}
\input{agents/cycles/exceptional_cubic_lattice_draft.tex}
\bibliographystyle{plainnat}
\bibliography{agents/cycles/references,agents/real_weil/C3bi_references}
\end{document}
"""
(output / (name + ".tex")).write_text(wrapper)
env = os.environ.copy()
env["TEXMFHOME"] = str(research.parent / "texmf")
latex = ["lualatex", "-interaction=nonstopmode", "-halt-on-error",
         "-output-directory=agents/cycles/output", "agents/cycles/output/" + name + ".tex"]
started = datetime.now(timezone.utc).isoformat()
tic = perf_counter()
stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
runs = []
for index, command in enumerate([latex, ["bibtex", "agents/cycles/output/" + name], latex, latex], 1):
    result = subprocess.run(command, cwd=research, env=env, capture_output=True, text=True)
    path = output / (stamp + f"_exceptional_cubic_pass{index}.out")
    path.write_text(result.stdout + result.stderr)
    runs.append({"command": command, "returncode": result.returncode, "output": str(path)})
    if result.returncode:
        break
log = (output / (name + ".log")).read_text(errors="replace")
report = {"started_at_utc": started, "finished_at_utc": datetime.now(timezone.utc).isoformat(),
          "runtime_seconds": perf_counter() - tic, "runs": runs,
          "diagnostics": [line for line in log.splitlines()
                          if "Overfull" in line or "undefined" in line or line.startswith("!")]}
(output / "compile_exceptional_cubic_lattice.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
