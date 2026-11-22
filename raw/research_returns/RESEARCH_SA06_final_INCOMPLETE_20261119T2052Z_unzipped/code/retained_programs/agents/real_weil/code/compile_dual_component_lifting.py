#!/usr/bin/env python3
"""Timed four-pass standalone assembly of C.3bs."""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import json, os, subprocess

started=perf_counter()
started_utc=datetime.now(timezone.utc).isoformat()
base=Path(__file__).resolve().parents[1]
research=base.parents[1]
out=base/'output'
name='dual_component_lifting_check'
source='C3_component_lifting_no_top_dual_cohomology.tex'
if not (base/source).exists():
    source='C3_component_lifting_no_top_dual_cohomology_draft.tex'
tex=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=27mm]{geometry}
\usepackage{amsmath,amsthm,amssymb,mathtools,natbib,longtable,booktabs,hyperref}
\hypersetup{hypertexnames=false}
\setlength{\emergencystretch}{2em}
\begin{document}
\input{agents/real_weil/SOURCE_FILE}
\bibliographystyle{plainnat}
\bibliography{agents/real_weil/C3br_references,agents/real_weil/C3bj_references,agents/real_weil/SEMIPURITY_references,agents/real_weil/references,agents/frobenius/C3_SNC_Fpbar_references,sources/root_references}
\end{document}
'''.replace('SOURCE_FILE',source)
(out/f'{name}.tex').write_text(tex)
latex=['lualatex','-interaction=nonstopmode','-halt-on-error','-output-directory=agents/real_weil/output',f'agents/real_weil/output/{name}.tex']
env=os.environ.copy()
env['TEXMFHOME']=str(research.parent/'texmf')
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
runs=[]
for index,command in enumerate([latex,['bibtex',f'agents/real_weil/output/{name}'],latex,latex],1):
    t=perf_counter()
    r=subprocess.run(command,cwd=research,env=env,capture_output=True,text=True)
    path=out/f'{stamp}_{name}_{index}.txt'
    path.write_text(r.stdout+r.stderr)
    runs.append({'command':command,'returncode':r.returncode,'runtime_seconds':perf_counter()-t,'output':str(path)})
    if r.returncode: break
logpath=out/f'{name}.log'
log=logpath.read_text(errors='replace') if logpath.exists() else ''
pdfpath=out/f'{name}.pdf'
record={'started_utc':started_utc,'completed_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':perf_counter()-started,'source':source,'runs':runs,
        'pdf_bytes':pdfpath.stat().st_size if pdfpath.exists() else None,
        'diagnostics':[line for line in log.splitlines() if 'Overfull' in line or 'undefined' in line or line.startswith('!')]}
(out/f'{stamp}_compile_dual_component_lifting.json').write_text(json.dumps(record,indent=2)+'\n')
(out/'compile_dual_component_lifting.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
if any(r['returncode'] for r in runs):raise SystemExit(1)
