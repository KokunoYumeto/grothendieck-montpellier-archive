"""Fresh four-pass wrappers for the reconstructed al/am/ao/ap proofs."""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import subprocess
import sys
import time

base=Path(__file__).resolve().parents[1];research=base.parents[1];out=base/'output'
out.mkdir(exist_ok=True)
items=[('C3al_check','principal_gysin_kernel','agents/cycles/principal_gysin_references'),
       ('C3am_check','critical_injectivity',''),
       ('C3ao_check','absolute_picard_kernel','agents/cycles/absolute_picard_references,sources/root_references,agents/real_weil/references'),
       ('C3ap_check','local_injectivity_classification','')]
env=os.environ.copy();env['TEXMFHOME']=str(research.parent/'texmf')
start=time.perf_counter();records=[]
selected=set(sys.argv[1:])
previous=out/'compile_recovered_injectivity.json'
if selected and previous.exists():
    records=[row for row in json.loads(previous.read_text())['wrappers'] if row['name'] not in selected]
for name,fragment,bib in items:
    if selected and name not in selected:continue
    wrapper='\\documentclass[11pt]{article}\n\\usepackage[a4paper,margin=27mm]{geometry}\n'
    wrapper+='\\usepackage{amsmath,amsthm,amssymb,mathtools,natbib,longtable,booktabs,hyperref}\n\\begin{document}\n'
    wrapper+='\\input{agents/cycles/'+fragment+'.tex}\n'
    if bib:wrapper+='\\bibliographystyle{plainnat}\n\\bibliography{'+bib+'}\n'
    wrapper+='\\end{document}\n';(out/(name+'.tex')).write_text(wrapper)
    latex=['lualatex','-interaction=nonstopmode','-halt-on-error','-output-directory=agents/cycles/output','agents/cycles/output/'+name+'.tex']
    commands=[latex]+([['bibtex','agents/cycles/output/'+name]] if bib else [])+[latex,latex]
    started=time.perf_counter();stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');runs=[]
    for j,cmd in enumerate(commands,1):
        p=subprocess.run(cmd,cwd=research,env=env,capture_output=True,text=True)
        logpath=out/f'{stamp}_{name}_recovery_{j}.txt';logpath.write_text(p.stdout+p.stderr)
        runs.append({'command':cmd,'returncode':p.returncode,'output':str(logpath)})
        if p.returncode:break
    logfile=out/(name+'.log');log=logfile.read_text(errors='replace') if logfile.exists() else ''
    diagnostics=[x for x in log.splitlines() if 'Overfull' in x or 'undefined' in x or x.startswith('!')]
    rec={'name':name,'utc':datetime.now(timezone.utc).isoformat(),
         'recovery_rerun':True,'runtime_seconds':time.perf_counter()-started,
         'runs':runs,'diagnostics':diagnostics}
    (out/('compile_'+fragment+'.json')).write_text(json.dumps(rec,indent=2)+'\n');records.append(rec)
records.sort(key=lambda row:row['name'])
record={'utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,
        'recovery_rerun':True,'this_invocation':sorted(selected) if selected else 'all four wrappers',
        'wrappers':records}
(out/'compile_recovered_injectivity.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
