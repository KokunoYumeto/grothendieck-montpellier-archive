#!/usr/bin/env python3
"""Prepare missing LuaLaTeX support in a private tree, without system writes.

Ordinary TeX Live users do not need this helper. Runtime-only downloads are
excluded from the edition archives; the edition sources use standard packages.
"""
import argparse, concurrent.futures, json, os, pathlib, subprocess, tarfile, urllib.request
PACKAGES = ['luatex','luaotfload','luatexbase','lualibs','lua-alt-getopt','lua-uni-algos','luacode','hyph-utf8','hyphen-english','hyphen-french','babel-french','ulem','soul']
MIRROR = 'https://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2024/tlnet-final/archive/'
def prepare(root):
    root=pathlib.Path(root).resolve(); tree=root/'texmf'; tree.mkdir(parents=True,exist_ok=True)
    pkgdir=root/'packages-2024';pkgdir.mkdir(exist_ok=True)
    def fetch(name):
        archive=pkgdir/(name+'.tar.xz')
        if not archive.exists():
            with urllib.request.urlopen(MIRROR+archive.name,timeout=120) as r: archive.write_bytes(r.read())
        with tarfile.open(archive) as tf:
            for m in tf.getmembers():
                if m.name.startswith('texmf-dist/'):
                    m.name=m.name[len('texmf-dist/'):]
                if m.name.startswith(('tex/','fonts/','scripts/','web2c/')) and (tree/m.name).resolve().is_relative_to(tree):
                    tf.extract(m,tree,filter='data')
        return {'package':name,'bytes':archive.stat().st_size}
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for r in pool.map(fetch,PACKAGES): results.append(r); print(json.dumps(r),flush=True)
    config=tree/'tex/generic/config';config.mkdir(parents=True,exist_ok=True)
    (config/'language.dat').write_text('english hyphen.tex\n=usenglish\n=american\nfrench loadhyph-fr.tex\n=francais\n')
    (config/'language.dat.lua').write_text('return { english = { loader = "hyphen.tex", lefthyphenmin = 2, righthyphenmin = 3, synonyms = {"usenglish", "american"}, patterns = "hyph-en-us.pat.txt", hyphenation = "hyph-en-us.hyp.txt" }, french = { loader = "loadhyph-fr.tex", lefthyphenmin = 2, righthyphenmin = 3, synonyms = {"francais"}, patterns = "hyph-fr.pat.txt", hyphenation = "" } }\n')
    (config/'language.def').write_text('\\addlanguage{english}{hyphen.tex}{}{2}{3}\n\\addlanguage{french}{loadhyph-fr.tex}{}{2}{3}\n')
    # A small map assembled from installed maps is enough for the AMS and CM math fonts.
    maps=tree/'fonts/map/pdftex/updmap';maps.mkdir(parents=True,exist_ok=True)
    mapsrc=[]
    for d in [pathlib.Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts'),pathlib.Path('/usr/share/texmf/fonts/map/dvips/lm')]:
        mapsrc.extend(d.glob('*.map'))
    maplines={}
    for p in mapsrc:
        for line in p.read_text().splitlines():
            if line.strip() and not line.lstrip().startswith('%'):
                maplines.setdefault(line.split()[0],line)
    (maps/'pdftex.map').write_text('\n'.join(maplines.values())+'\n')
    env=tex_env(root)
    fmtdir=root/'var/web2c/luahbtex';fmtdir.mkdir(parents=True,exist_ok=True)
    if not (fmtdir/'lualatex.fmt').exists():
        r=subprocess.run(['luahbtex','--ini','--interaction=nonstopmode','--halt-on-error','--jobname=lualatex','lualatex.ini'],cwd=fmtdir,env=env,capture_output=True,text=True)
        (root/'format-build.txt').write_text(r.stdout+r.stderr)
        if r.returncode: raise RuntimeError('LuaLaTeX format generation failed; inspect runtime format-build.txt')
    (root/'bootstrap_result.json').write_text(json.dumps(results,indent=2)+'\n')
    return env

def tex_env(root):
    root=pathlib.Path(root).resolve();env=os.environ.copy()
    for d in ['cache','config','var']: (root/d).mkdir(parents=True,exist_ok=True)
    env['TEXMF']='{'+str(root/'texmf')+',/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}'
    env['openout_any']='a'
    env['TEXMFVAR']=str(root/'var');env['TEXMFCACHE']=str(root/'cache');env['TEXMFCONFIG']=str(root/'config')
    env['TEXFORMATS']=str(root/'var/web2c/luahbtex')+':';env['OSFONTDIR']='/usr/share/fonts//'
    return env

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('runtime');a=p.parse_args();prepare(a.runtime)
