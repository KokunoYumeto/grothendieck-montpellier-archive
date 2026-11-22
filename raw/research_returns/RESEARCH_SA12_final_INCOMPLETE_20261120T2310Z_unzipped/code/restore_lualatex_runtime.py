"""Install only missing LuaLaTeX runtime assets in a task-local support tree."""
from pathlib import Path
import hashlib, io, json, os, shutil, subprocess, time, urllib.request, zipfile

root=Path(__file__).resolve().parents[1]
support=root.parent/'sa12_tex_support'
support.mkdir(exist_ok=True)
started=time.perf_counter()
items=[]
receipt=root/'code/output/restore_lualatex_runtime.json'
cached={x['name']:x for x in json.loads(receipt.read_text())['dependencies']} if receipt.exists() else {}
for name,url in [
 ('luaotfload','https://mirror.apps.cam.ac.uk/pub/tex-archive/macros/luatex/generic/luaotfload.zip'),
 ('luatexbase','https://mirror.apps.cam.ac.uk/pub/tex-archive/macros/luatex/generic/luatexbase.zip'),
 ('lualibs','https://mirror.apps.cam.ac.uk/pub/tex-archive/macros/luatex/generic/lualibs.zip'),
 ('lua-uni-algos','https://mirror.apps.cam.ac.uk/pub/tex-archive/macros/luatex/generic/lua-uni-algos.zip')]:
    if name in cached:
        items.append(cached[name]);continue
    request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
    with urllib.request.urlopen(request,timeout=45) as response:
        data=response.read(); final=response.geturl()
    target=support/'texmf/tex/luatex'/name
    target.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        saved=[]
        for info in archive.infolist():
            if info.is_dir():continue
            path=Path(info.filename)
            if '..' in path.parts:raise ValueError('Unexpected dependency path')
            if path.suffix not in {'.lua','.sty','.tex','.otf','.gz','.dtx','.ins','.txt'}:continue
            dest=target/path.name;dest.write_bytes(archive.read(info));saved.append(path.name)
    items.append({'name':name,'url':url,'resolved_url':final,'download_bytes':len(data),
                  'sha256':hashlib.sha256(data).hexdigest(),'files':saved})
texenv=os.environ.copy()
texenv['TEXMF']='{'+str(support/'texmf')+',/usr/share/texlive/texmf-dist,/usr/share/texmf}'
for name, source, generated in [('lualibs','lualibs.dtx','lualibs.lua'),('luatexbase','luatexbase.ins','luatexbase.sty')]:
    directory=support/'texmf/tex/luatex'/name
    if not (directory/generated).exists():
        p=subprocess.run(['luatex','-ini','-interaction=nonstopmode','\\input plain \\input '+source],cwd=directory,env=texenv,capture_output=True,text=True)
        (root/f'code/output/{name}_docstrip.log').write_text(p.stdout+p.stderr)
        p.check_returncode()
if not (support/'lualatex.fmt').exists():
    p=subprocess.run(['luahbtex','-ini','-jobname=lualatex','-progname=lualatex','lualatex.ini'],cwd=support,env=texenv,capture_output=True,text=True)
    (root/'code/output/lualatex_format_initialization.log').write_text(p.stdout+p.stderr)
    p.check_returncode()
maps=list(Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts').glob('*.map'))
maps.append(Path('/usr/share/texmf/fonts/map/dvips/lm/lm.map'))
maptarget=support/'texmf/fonts/map/pdftex/sa12/pdftex.map'
maptarget.parent.mkdir(parents=True,exist_ok=True)
maptarget.write_text('\n'.join(p.read_text() for p in maps))
record={'support':str(support),'dependencies':items,'seconds':time.perf_counter()-started,
        'font_map_sources':[str(p) for p in maps],
        'note':'Runtime dependencies are outside the research archive; no supplied input archive is extracted.'}
(root/'code/output/restore_lualatex_runtime.json').write_text(json.dumps(record,indent=2)+'\n')
if (support/'lualatex.log').exists():shutil.copy2(support/'lualatex.log',root/'code/output/lualatex_format_initialization.log')
print(json.dumps({'support':str(support),'dependencies':[x['name'] for x in items],'seconds':record['seconds']}))
