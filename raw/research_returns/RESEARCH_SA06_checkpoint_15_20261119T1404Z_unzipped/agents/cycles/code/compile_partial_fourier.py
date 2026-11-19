from pathlib import Path
from datetime import datetime, timezone
import json
import os
import subprocess
import time

base = Path(__file__).resolve().parents[1]
research = base.parents[1]
output = base / "output"
name = "partial_fourier_check"
wrapper = r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=27mm]{geometry}
\usepackage{amsmath,amsthm,amssymb,mathtools,natbib,longtable,booktabs,hyperref}
\begin{document}
\input{agents/cycles/partial_fourier_correspondence.tex}
\bibliographystyle{plainnat}
\bibliography{agents/cycles/partial_fourier_references,agents/cycles/references,agents/frobenius/C4_lagrangian_divisor_obstruction_references}
\end{document}
"""
(output / (name + ".tex")).write_text(wrapper)
environment = os.environ.copy()
environment["TEXMFHOME"] = str(research.parent / "texmf")
latex = ["lualatex", "-interaction=nonstopmode", "-halt-on-error",
         "-output-directory=agents/cycles/output",
         "agents/cycles/output/" + name + ".tex"]
started = time.perf_counter()
stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
runs = []
for index, command in enumerate([latex, ["bibtex", "agents/cycles/output/" + name], latex, latex], 1):
    process = subprocess.run(command, cwd=research, env=environment,
                             capture_output=True, text=True)
    path = output / (stamp + f"_partial_fourier_pass{index}.out")
    path.write_text(process.stdout + process.stderr)
    runs.append({"command": command, "returncode": process.returncode, "output": str(path)})
    if process.returncode:
        break
log = (output / (name + ".log")).read_text(errors="replace")
report = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "runtime_seconds": time.perf_counter() - started,
    "runs": runs,
    "diagnostics": [line for line in log.splitlines()
                    if "Overfull" in line or "undefined" in line or line.startswith("!")],
}
encoded = json.dumps(report, indent=2)
(output / "compile_partial_fourier.json").write_text(encoded + "\n")
print(encoded)
