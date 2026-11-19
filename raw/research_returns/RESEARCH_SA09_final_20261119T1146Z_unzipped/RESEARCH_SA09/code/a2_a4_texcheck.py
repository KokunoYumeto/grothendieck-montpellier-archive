#!/usr/bin/env python3
"""Compile a temporary harness for the A2/A4 fragment; not a deliverable PDF."""
from pathlib import Path
import subprocess
import re
import json
import time
from tex_runtime import environment

root=Path(__file__).resolve().parents[1]
qa=root/'qa'
qa.mkdir(exist_ok=True)
tex=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=27mm]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage{fontspec}
\usepackage[hidelinks]{hyperref}
\setlength{\emergencystretch}{2em}
\begin{document}
\input{sections/A2_A4.tex}
\bibliographystyle{plain}
\bibliography{notes/A2_A4_references}
\end{document}
'''
(qa/'a2_a4_check.tex').write_text(tex)
start=time.perf_counter()
cmd=['lualatex','-interaction=nonstopmode','-halt-on-error','-output-directory=qa','qa/a2_a4_check.tex']
proc=subprocess.run(cmd,cwd=root,env=environment(),text=True,capture_output=True)
(root/'logs/a2_a4_texcheck.stdout.txt').write_text(proc.stdout+proc.stderr)
log_path=qa/'a2_a4_check.log'
log=log_path.read_text(errors='replace') if log_path.exists() else proc.stdout+proc.stderr
over=[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',log)]
result={'command':cmd,'exit_code':proc.returncode,'runtime_seconds':time.perf_counter()-start,
        'overfull_hbox_count':len(over),'over_2pt_count':sum(x>2 for x in over),'widths_pt':over,
        'log_created':log_path.exists(),
        'scope':'Temporary fragment syntax/layout harness; zero overflow counts are not a success when exit_code is nonzero. Root verifies the final integrated PDF.'}
print(json.dumps(result,indent=2))
if proc.returncode:
    print('\n'.join(log.splitlines()[-30:]))
