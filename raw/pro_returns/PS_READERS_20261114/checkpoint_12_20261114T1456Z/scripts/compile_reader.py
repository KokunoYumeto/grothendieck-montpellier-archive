"""Compile a relative project TeX file; keep only sanitized logs in the project."""
from pathlib import Path
import argparse,os,re,subprocess,json,shutil
P=Path(__file__).resolve().parents[1]
W=P.parent
p=argparse.ArgumentParser();p.add_argument('file');p.add_argument('--passes',type=int,default=1);a=p.parse_args()
src=P/a.file
if not src.exists():raise SystemExit('Reader source does not exist')
env=os.environ.copy()
def texvar(name):
    return subprocess.run(['kpsewhich','-var-value='+name],stdout=subprocess.PIPE,text=True).stdout.strip()
texdist=texvar('TEXMFDIST');texmain=texvar('TEXMFMAIN')
default_tree=subprocess.run(['kpsewhich','-expand-var=$TEXMF'],stdout=subprocess.PIPE,text=True).stdout.strip()
extra=W/'.tex_extra/usr/share/texlive/texmf-dist'
if extra.exists():
    env['TEXMF']='{'+str(extra)+','+default_tree+'}'
    env['TEXMFVAR']=str(W/'.tex_runtime/cache');env['TEXMFCACHE']=env['TEXMFVAR'];env['TEXFORMATS']=str(W/'.tex_runtime')+'//:'
maps=W/'.tex_runtime/maps'
if maps.exists():env['TEXFONTMAPS']=str(maps)+'//:'
tmp=W/'.tex_runtime/build'/src.stem;tmp.mkdir(parents=True,exist_ok=True)
shutil.copyfile(src,tmp/src.name)
combined=[]
for run in range(a.passes):
    r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',src.name],cwd=tmp,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    combined.append(r.stdout)
    if r.returncode:break
raw='\n'.join(combined)
def clean(s):
    s=re.sub(r'<(/[^>]+)>',lambda m:'<FONT:'+Path(m[1].replace('\n','')).name+'>',s,flags=re.S)
    for path,replacement in [(str(P),'PROJECT'),(str(W),'WORKSPACE'),(texdist,'TEXMFDIST'),(texmain,'TEXMF'),(str(Path.home()),'AGENT')]:
        if path:s=re.sub(r'\s*'.join(re.escape(c) for c in path),replacement,s)
    s=re.sub(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}', '[address omitted]',s,flags=re.I)
    return s
logdir=P/'logs';prefix=src.stem+'_'+src.parent.name
runid=len(list(logdir.glob(prefix+'_run*.stdout')))+1
stem=prefix+f'_run{runid:03d}'
(logdir/(stem+'.stdout')).write_text(clean(raw))
if (tmp/(src.stem+'.log')).exists():(logdir/(stem+'.log')).write_text(clean((tmp/(src.stem+'.log')).read_text(errors='replace')))
if r.returncode==0 and (tmp/(src.stem+'.pdf')).exists():shutil.copyfile(tmp/(src.stem+'.pdf'),src.with_suffix('.pdf'))
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([\d.]+)pt',raw)]
print(json.dumps({'source':a.file,'exit':r.returncode,'overfull_count':len(over),'widest_pt':max(over,default=0),'missing_character_lines':len(re.findall('Missing character:',raw))}))
print(clean(raw[-2600:]))
