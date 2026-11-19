#!/usr/bin/env python3
"""Workspace-local TeX environment, avoiding absent system ls-R databases.

Use: python code/tex_runtime.py --build-format
     python code/tex_runtime.py lualatex -interaction=nonstopmode ...
No system files or user home directories are changed.
"""
from pathlib import Path
import os
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
RUNTIME=ROOT/'tex-runtime'

def environment():
    for name in ['var','config','cache','home','formats','texmf']:
        (RUNTIME/name).mkdir(parents=True,exist_ok=True)
    env=os.environ.copy()
    # The system TeX tree is present, but its absent ls-R database is
    # preceded by !! in the system configuration.  Removing database-only
    # lookup restores read-only filesystem search of those installed trees.
    env.update({
      'TEXMF':'{'+str(RUNTIME/'texmf')+',/etc/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}',
      'TEXMFVAR':str(RUNTIME/'var'),
      'TEXMFCONFIG':str(RUNTIME/'config'),
      'TEXMFCACHE':str(RUNTIME/'cache'),
      'TEXMFHOME':str(RUNTIME/'home'),
      'TEXFORMATS':str(RUNTIME/'formats')+'//:',
      'TEXMFOUTPUT':str(ROOT),
    })
    return env

def main():
    args=sys.argv[1:]
    env=environment()
    if args==['--build-format']:
        ini=subprocess.check_output(['kpsewhich','-progname=lualatex','lualatex.ini'],env=env,text=True).strip()
        args=['luahbtex','--ini','--interaction=nonstopmode','--halt-on-error',
              '--jobname=lualatex','--progname=lualatex',ini]
        return subprocess.call(args,cwd=RUNTIME/'formats',env=env)
    if not args:
        raise SystemExit('Pass a TeX command or --build-format')
    return subprocess.call(args,env=env)

if __name__=='__main__':
    raise SystemExit(main())
