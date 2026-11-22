"""Build the two audited, unregistered SNC nonzero-period research lemmas NP.1--9."""
from datetime import datetime, timezone
import hashlib, json, os, re, subprocess, time
from pathlib import Path

base=Path(__file__).resolve().parents[1]
research=base.parents[1]
out=base/'output'
name='C3_SNC_nonzero_period_combined_check'
sources=[base/'C3_SNC_nonzero_period_model_RESEARCH.tex',base/'C3_SNC_period_Picard_span_RESEARCH.tex']
keys=set()
for source in sources:
    for match in re.finditer(r'\\cite\w*(?:\[[^\]]*\])*\s*\{([^}]+)\}',source.read_text()):
        keys.update(k.strip() for k in match.group(1).split(','))
entries={}; origins={}
for path in sorted(research.rglob('*.bib')):
    if 'output' in path.parts or path.name.startswith('RESEARCH_'): continue
    data=path.read_text(errors='replace')
    starts=list(re.finditer(r'(?m)^@\w+\{([^,]+),',data))
    for j,match in enumerate(starts):
        key=match.group(1).strip()
        if key in keys and key not in entries:
            end=starts[j+1].start() if j+1<len(starts) else len(data)
            entries[key]=data[match.start():end].strip()
            origins[key]=str(path.relative_to(research))
assert keys==set(entries),(keys-set(entries))
(out/(name+'_refs.bib')).write_text('\n\n'.join(entries[k] for k in sorted(keys))+'\n')
wrapper=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=27mm]{geometry}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\usepackage{amsmath,amssymb,amsthm,mathtools,natbib,hyperref}
\setlength{\emergencystretch}{1.5em}
\begin{document}
\input{../C3_SNC_nonzero_period_model_RESEARCH.tex}
\input{../C3_SNC_period_Picard_span_RESEARCH.tex}
\bibliographystyle{plainnat}
\bibliography{C3_SNC_nonzero_period_combined_check_refs}
\end{document}
'''
(out/(name+'.tex')).write_text(wrapper)
env=dict(os.environ);env['TEXMFHOME']=str(research.parent/'texmf')
tex=['lualatex','-fmt='+str(research/'lualatex.fmt'),'-interaction=nonstopmode','-halt-on-error',name+'.tex']
commands=[tex,['bibtex',name],tex,tex,tex]
record={'started_utc':datetime.now(timezone.utc).isoformat(),
        'sources_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        'bibliography_origins':origins,'passes':[]}
tick=time.perf_counter(); logs=[]
for command in commands:
    start=time.perf_counter()
    result=subprocess.run(command,cwd=out,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    logs.append(result.stdout)
    record['passes'].append({'command':command,'returncode':result.returncode,'runtime_seconds':time.perf_counter()-start})
    if result.returncode: break
record['runtime_seconds']=time.perf_counter()-tick
record['finished_utc']=datetime.now(timezone.utc).isoformat()
pdf=out/(name+'.pdf')
if pdf.exists():record['pdf_bytes']=pdf.stat().st_size
log=(out/(name+'.log')).read_text(errors='replace')
record['warnings']=[line for line in log.splitlines() if re.search(r'Warning|Overfull|Underfull|^!',line)]
record['output_line']=next((line for line in log.splitlines() if line.startswith('Output written on')),None)
(out/'SNC_nonzero_period_combined_build.out').write_text('\n'.join(logs))
(out/'SNC_nonzero_period_combined_build.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
