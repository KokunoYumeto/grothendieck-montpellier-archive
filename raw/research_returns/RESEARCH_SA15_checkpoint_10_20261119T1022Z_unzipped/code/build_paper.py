"""Reproducible LuaLaTeX/BibTeX build and overflow inventory.

Runtime path repairs are confined to this process. On a complete TeX Live
installation the extra local TEXMF roots are harmless and unnecessary.
"""
import os, pathlib, subprocess, json, re, time
root=pathlib.Path(__file__).resolve().parents[1]
local=root.parent/'.tex-runtime'
env=os.environ.copy()
env['TEXMF']='{'+','.join(map(str,[local,local/'texmf-dist',root,pathlib.Path('/usr/share/texmf'),pathlib.Path('/usr/share/texlive/texmf-dist')]))+'}'
env['TEXFORMATS']=str(root)+':'+env.get('TEXFORMATS','')
out=root/'outputs';out.mkdir(exist_ok=True)
log=[]; start=time.monotonic()
def run(args):
    result=subprocess.run(args,cwd=root,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    log.append('$ '+' '.join(args)+'\n'+result.stdout)
    if result.returncode:
        (out/'build_console.txt').write_text('\n'.join(log))
        print(result.stdout[-6000:]);raise SystemExit(result.returncode)
if not (root/'lualatex.fmt').exists():
    run(['luahbtex','--ini','--interaction=nonstopmode','--halt-on-error','--jobname=lualatex','lualatex.ini'])
command=['lualatex','-interaction=nonstopmode','-halt-on-error','RESEARCH_SA15_paper.tex']
(root/'RESEARCH_SA15_paper.bbl').unlink(missing_ok=True)
run(command)
run(['bibtex','RESEARCH_SA15_paper'])
run(command);run(command)
(out/'build_console.txt').write_text('\n'.join(log))
final=(root/'RESEARCH_SA15_paper.log').read_text(errors='replace')
boxes=[{'kind':m.group(1),'points':float(m.group(2)),'context':final[m.start():m.start()+320]} for m in re.finditer(r'Overfull \\([hv])box \(([-\d.]+)pt too (?:wide|high)\)',final)]
summary={'seconds':round(time.monotonic()-start,3),'overfull_boxes':boxes,
         'over_2pt':sum(b['points']>2 for b in boxes),'pdf_bytes':(root/'RESEARCH_SA15_paper.pdf').stat().st_size,
         'undefined_references':'There were undefined references' in final,
         'undefined_citations':'There were undefined citations' in final}
(out/'build_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
