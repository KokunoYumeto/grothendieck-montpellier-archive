#!/usr/bin/env python3
"""Fresh four-pass verification of a recovered final top-quotient fragment."""
from pathlib import Path
from datetime import datetime,timezone
from time import perf_counter
import json,os,subprocess,sys
started=perf_counter();base=Path(__file__).resolve().parents[1];research=base.parents[1]
out=base/'output';out.mkdir(exist_ok=True)
key=sys.argv[1]
source={'an':'C3_top_p_tangent.tex','aq':'C3_top_all_positive_characteristics.tex',
        'as':'C3_top_all_dimensions.tex',
        'at':'C3_positive_characteristic_cy_boundary.tex',
        'av':'C3_positive_characteristic_low_range.tex',
        'aw':'C3_positive_characteristic_low_injectivity.tex',
        'ay':'C3_positive_characteristic_critical_injectivity.tex',
        'ba':'C3_positive_characteristic_all_quotients.tex',
        'bb':'C3_positive_characteristic_divisor_addendum.tex',
        'bf':'C3_integral_picard_kernel.tex'}[key]
name='C3'+key+'_check'
tex=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=27mm]{geometry}
\usepackage{amsmath,amsthm,amssymb,mathtools,natbib,longtable,booktabs,hyperref}
\setlength{\emergencystretch}{2em}
\begin{document}
\input{agents/real_weil/SOURCE}
\bibliographystyle{plainnat}
\bibliography{agents/real_weil/C3an_references,agents/real_weil/C3at_references,agents/real_weil/C3aw_references,agents/real_weil/C3ay_references,agents/real_weil/C3ba_references,agents/real_weil/C3bb_references,agents/real_weil/C3bf_references,agents/frobenius/K2_square_zero_references,agents/real_weil/references,sources/root_references,agents/frobenius/C4_prym_references,agents/cycles/absolute_picard_references,agents/cycles/principal_gysin_references}
\end{document}
'''.replace('SOURCE',source)
(out/f'{name}.tex').write_text(tex)
latex=['lualatex','-interaction=nonstopmode','-halt-on-error','-output-directory=agents/real_weil/output',f'agents/real_weil/output/{name}.tex']
commands=[latex,['bibtex',f'agents/real_weil/output/{name}'],latex,latex]
env=os.environ.copy();env['TEXMFHOME']=str(research.parent/'texmf')
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');runs=[]
for i,command in enumerate(commands,1):
    t0=perf_counter();r=subprocess.run(command,cwd=research,env=env,capture_output=True,text=True)
    path=out/f'{stamp}_C3{key}_recovery_compile_{i}.txt';path.write_text(r.stdout+r.stderr)
    runs.append({'command':command,'returncode':r.returncode,'runtime_seconds':perf_counter()-t0,'output':str(path)})
    if r.returncode:break
log=(out/f'{name}.log').read_text(errors='replace')
record={'utc':datetime.now(timezone.utc).isoformat(),'recovery_rerun':key in ('an','aq'),'runtime_seconds':perf_counter()-started,'runs':runs,
        'diagnostics':[s for s in log.splitlines() if 'Overfull' in s or 'undefined' in s or s.startswith('!')]}
(out/f'compile_C3{key}_recovery.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
if any(r['returncode'] for r in runs):raise SystemExit(1)
