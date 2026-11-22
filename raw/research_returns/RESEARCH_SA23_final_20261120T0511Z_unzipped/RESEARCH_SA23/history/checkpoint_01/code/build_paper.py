"""Build the current paper and record an honest typesetting diagnostic."""
from pathlib import Path
import subprocess, time, re, json, os
root=Path(__file__).resolve().parents[1]
start=time.perf_counter()
environment=os.environ.copy()
environment['TEXMF']='{/usr/share/texlive/texmf-dist,/usr/share/texmf}'
environment['TEXFORMATS']=str(root.parent/'.library_work')+':'
commands=[["lualatex","-interaction=nonstopmode","-halt-on-error","RESEARCH_SA23_paper.tex"],
          ["bibtex","RESEARCH_SA23_paper"],
          ["lualatex","-interaction=nonstopmode","-halt-on-error","RESEARCH_SA23_paper.tex"],
          ["lualatex","-interaction=nonstopmode","-halt-on-error","RESEARCH_SA23_paper.tex"]]
records=[]
for i,cmd in enumerate(commands,1):
    result=subprocess.run(cmd,cwd=root,capture_output=True,text=True,env=environment)
    (root/'logs'/f'build_{i:02d}.txt').write_text(result.stdout+'\n'+result.stderr)
    records.append({'command':cmd,'returncode':result.returncode})
    if result.returncode and cmd[0]=='lualatex': break
log_path=root/'RESEARCH_SA23_paper.log'
log=log_path.read_text(errors='replace') if log_path.exists() else ''
overflows=[float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)',log)]
warnings=[x for x in log.splitlines() if 'Warning' in x or 'Overfull' in x or x.startswith('!')]
report={'commands':records,'overfull_count':len(overflows),'overfull_gt_2pt':sum(x>2 for x in overflows),
        'max_overfull_pt':max(overflows,default=0),'warnings':warnings,'seconds':time.perf_counter()-start}
(root/'logs'/'build_diagnostics.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
