"""Build the paper with LuaLaTeX and record exact layout diagnostics.

The container has TeX source trees but lacks system ls-R/format databases.
Use a private, searchable TEXMF tree and a locally generated format; no
system configuration or package files are modified.
"""
from pathlib import Path
import subprocess,os,json,re,time,datetime
root=Path(__file__).resolve().parents[1]
private=root/'tmp'/'tex_runtime';private.mkdir(parents=True,exist_ok=True)
env=os.environ.copy()
env['TEXMF']='{'+str(private/'texmf')+',/usr/share/texmf,/usr/share/texlive/texmf-dist}'
env['TEXMFVAR']=str(private/'var');env['TEXMFCONFIG']=str(private/'config')
env['TEXMFCACHE']='./tmp/tex_runtime/cache';env['TEXMFHOME']=str(private/'home')
env['TEXFORMATS']=str(private)+':'
for folder in ['texmf','var','config','cache','home']:(private/folder).mkdir(exist_ok=True)
fontmap=private/'texmf/fonts/map/pdftex/private/pdftex.map'
fontmap.parent.mkdir(parents=True,exist_ok=True)
mapdir=Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts')
fontmap.write_text('\n'.join((mapdir/name).read_text() for name in ['cm.map','cmextra.map','euler.map','latxfont.map','symbols.map']))
commands=[];start=time.monotonic()
if not (private/'lualatex.fmt').exists():
    command=['luahbtex','--ini','--jobname=lualatex','--progname=lualatex','lualatex.ini']
    result=subprocess.run(command,cwd=private,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (root/'code'/'tex_format_build.log').write_text(result.stdout)
    commands.append({'command':command,'returncode':result.returncode})
    if result.returncode:
        print(result.stdout[-7000:]);raise SystemExit(result.returncode)
command=['latexmk','-g','-lualatex','-interaction=nonstopmode','-halt-on-error','RESEARCH_SA14_SA19_paper.tex']
result=subprocess.run(command,cwd=root,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(root/'code'/'paper_build_output.log').write_text(result.stdout)
commands.append({'command':command,'returncode':result.returncode})
log=root/'RESEARCH_SA14_SA19_paper.log'
text=log.read_text(errors='replace') if log.exists() else ''
overfull=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt too (?:wide|high)\)',text)]
report={'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'seconds':round(time.monotonic()-start,3),
        'commands':commands,'overfull_total':len(overfull),'overfull_gt_2pt':sum(x>2 for x in overfull),
        'overfull_sizes_pt':overfull,'missing_characters':len(re.findall('Missing character:',text)),
        'undefined_citations':len(re.findall(r'Citation .* undefined',text)),
        'undefined_references':len(re.findall(r'Reference .* undefined',text))}
(root/'code'/'paper_build_diagnostics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
if result.returncode:print(result.stdout[-7000:])
raise SystemExit(result.returncode)
