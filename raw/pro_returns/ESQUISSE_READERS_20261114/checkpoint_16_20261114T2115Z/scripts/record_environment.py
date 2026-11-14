#!/usr/bin/env python3
"""Record public runtime versions, without installation paths or host identifiers."""
import argparse,importlib.metadata,json,pathlib,platform,subprocess

def record(root):
    packages={}
    for name in ['PyMuPDF','Pillow','numpy','matplotlib']:
        try:packages[name]=importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError:packages[name]=None
    process=subprocess.run(['lualatex','--version'],capture_output=True,text=True)
    data={'python':platform.python_version(),'operating_system':platform.system(),'lualatex_version':process.stdout.splitlines()[0] if process.stdout else 'unavailable','python_packages':packages,'roles':{'PyMuPDF':'PDF measurements, links and rendering','Pillow':'rendered-page contact sheets and source detail handling','numpy':'optional source-glyph tracing','matplotlib':'optional source-glyph contour extraction'},'standalone_compilation':'A working standard TeX Live with LuaLaTeX compiles each delivered source directly; Python is needed only to regenerate or audit the edition.'}
    (root/'records/BUILD_ENVIRONMENT.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    return data

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);a=p.parse_args();print(json.dumps(record(a.root),indent=2))
