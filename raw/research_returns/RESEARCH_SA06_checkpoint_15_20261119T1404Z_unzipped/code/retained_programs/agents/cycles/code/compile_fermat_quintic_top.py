from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,time
b=Path(__file__).resolve().parents[1];r=b.parents[1];o=b/'output'
w=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=27mm]{geometry}
\usepackage{amsmath,amsthm,amssymb,mathtools,natbib,longtable,booktabs,hyperref}
\begin{document}
\input{agents/cycles/fermat_quintic_top.tex}
\bibliographystyle{plainnat}
\bibliography{agents/cycles/fermat_quintic_references,agents/cycles/absolute_picard_references,agents/real_weil/references,sources/root_references}
\end{document}
'''
(o/'C3au_check.tex').write_text(w)
env=os.environ.copy();env['TEXMFHOME']=str(r.parent/'texmf')
latex=['lualatex','-interaction=nonstopmode','-halt-on-error','-output-directory=agents/cycles/output','agents/cycles/output/C3au_check.tex']
start=time.perf_counter();stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');runs=[]
for i,cmd in enumerate([latex,['bibtex','agents/cycles/output/C3au_check'],latex,latex],1):
 p=subprocess.run(cmd,cwd=r,env=env,capture_output=True,text=True);target=o/(stamp+f'_C3au_pass{i}.out');target.write_text(p.stdout+p.stderr);runs.append({'command':cmd,'returncode':p.returncode,'output':str(target)})
 if p.returncode:break
log=(o/'C3au_check.log').read_text(errors='replace')
report={'utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'runs':runs,'diagnostics':[x for x in log.splitlines() if 'Overfull' in x or 'undefined' in x or x.startswith('!')]}
s=json.dumps(report,indent=2);(o/'compile_fermat_quintic_top.json').write_text(s+'\n');print(s)
