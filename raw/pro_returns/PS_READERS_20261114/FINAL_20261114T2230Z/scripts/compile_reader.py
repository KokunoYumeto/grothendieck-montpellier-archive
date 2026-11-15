"""Compile a relative project TeX file; keep only sanitized logs in the project."""
from pathlib import Path
import argparse,os,re,subprocess,json,shutil,collections,hashlib
P=Path(__file__).resolve().parents[1]
W=P.parent
p=argparse.ArgumentParser();p.add_argument('file');p.add_argument('--passes',type=int,default=1);a=p.parse_args()
src=P/a.file
if not src.exists():raise SystemExit('Reader source does not exist')
env=os.environ.copy()
def texvar(name):
    return subprocess.run(['kpsewhich','-var-value='+name],stdout=subprocess.PIPE,text=True).stdout.strip()
texdist=texvar('TEXMFDIST');texmain=texvar('TEXMFMAIN')
default_tree=subprocess.run(['kpsewhich','-expand-var=$TEXMF'],stdout=subprocess.PIPE,text=True).stdout.strip().replace('!!','')
extra=W/'.tex_extra/usr/share/texlive/texmf-dist'
if extra.exists():
    env['TEXMF']='{'+str(extra)+','+default_tree+'}'
    env['TEXMFVAR']=str(W/'.tex_runtime/cache');env['TEXMFCACHE']=env['TEXMFVAR'];env['TEXFORMATS']=str(W/'.tex_runtime')+'//:'
maps=W/'.tex_runtime/maps'
if maps.exists():env['TEXFONTMAPS']=str(maps)+'//:'
tmp=W/'.tex_runtime/build'/'_'.join(src.relative_to(P).parts[:-1])/src.stem;tmp.mkdir(parents=True,exist_ok=True)
source_bytes=src.read_bytes();source_sha=hashlib.sha256(source_bytes).hexdigest()
(tmp/src.name).write_bytes(source_bytes)
combined=[]
for run in range(a.passes):
    r=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',src.name],cwd=tmp,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    combined.append(r.stdout)
    if r.returncode:break
raw='\n'.join(combined)
def clean(s):
    s=re.sub(r'<\s*(/[^>]+)>',lambda m:'<FONT:'+Path(m[1].replace('\n','')).name+'>',s,flags=re.S)
    for path,replacement in [(str(P),'PROJECT'),(str(W),'WORKSPACE'),(texdist,'TEXMFDIST'),(texmain,'TEXMF'),(str(Path.home()),'AGENT')]:
        if path:s=re.sub(r'\s*'.join(re.escape(c) for c in path),replacement,s)
    s=re.sub(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}', '[address omitted]',s,flags=re.I)
    return s
logdir=P/'logs';prefix=src.stem+'_'+src.parent.name
runid=len(list(logdir.glob(prefix+'_run*.stdout')))+1
stem=prefix+f'_run{runid:03d}'
(logdir/(stem+'.stdout')).write_text(clean(raw))
texlog=(tmp/(src.stem+'.log')).read_text(errors='replace') if (tmp/(src.stem+'.log')).exists() else raw
if (tmp/(src.stem+'.log')).exists():(logdir/(stem+'.log')).write_text(clean(texlog))
if r.returncode==0 and (tmp/(src.stem+'.pdf')).exists():shutil.copyfile(tmp/(src.stem+'.pdf'),src.with_suffix('.pdf'))
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([\d.]+)pt',texlog)]
result={'source':a.file,'source_sha256':source_sha,'source_changed_during_build':hashlib.sha256(src.read_bytes()).hexdigest()!=source_sha,'log':'logs/'+stem+'.log','exit':r.returncode,'overfull_count':len(over),'widest_pt':max(over,default=0),'missing_character_lines':len(re.findall('Missing character:',texlog)),'underfull_box_count':len(re.findall(r'Underfull \\[hv]box',texlog)),'latex_warning_count':len(re.findall(r'(?:LaTeX|Package [^\n]+) Warning:',texlog))}
marks=re.findall(r'PS-LINK-SHIP\|(scanpage|unsure|illegible)\|([^|\s]+)\|(\d+)\|(outer|nested)',texlog)
result['shipped_logical_link_marks']=dict(collections.Counter(m[0] for m in marks));result['nested_marks_sharing_an_outer_link']=sum(m[3]=='nested' for m in marks)
if r.returncode==0:
    import fitz
    result['pdf_sha256']=hashlib.sha256(src.with_suffix('.pdf').read_bytes()).hexdigest()
    pdf=fitz.open(src.with_suffix('.pdf'));links=[l for page in pdf for l in page.get_links() if l.get('uri')]
    uris=[l['uri'] for l in links if 'grothendieck.umontpellier.fr/web/viewer.html?' in l['uri']]
    result.update(pdf_pages=len(pdf),pdf_uri_annotations=len(links),archive_link_annotations=len(uris),distinct_archive_pages=len(set(uris)))
    manifest_path=src.parent/'BUILD_MANIFEST.json' if src.parent.name!='readers' else P/'records/BUILD_MANIFEST.json'
    if manifest_path.exists() and marks:
        mf=json.loads(manifest_path.read_text());mode='diplomatic' if src.stem.endswith('diplomatic') else 'reading' if src.stem.endswith('reading') else 'corrected_apparatus'
        expected={(m['key'],n):v for m in mf for n,v in m['expected_link_marks'][mode].items()}
        observed=collections.Counter((m[1],m[0]) for m in marks)
        result['link_mark_count_mismatches']=[{'key':k,'kind':n,'expected':v,'observed':observed[(k,n)]} for (k,n),v in expected.items() if observed[(k,n)]!=v]
        result['unexpected_link_mark_keys']=sorted({k for k,n in observed if (k,n) not in expected})
(logdir/(stem+'.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
print(clean(raw[-2600:]))
