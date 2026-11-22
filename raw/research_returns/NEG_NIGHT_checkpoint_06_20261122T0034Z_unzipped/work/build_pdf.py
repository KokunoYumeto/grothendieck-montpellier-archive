"""Build the paper with the installed TeX files and a task-local format.

The system's TeX filename databases are absent. Explicit recursive search
paths avoid treating those absent databases as an absent TeX installation.
This script creates no checkpoint and makes no proof-verification claim.
"""
import argparse
import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / 'work/texbuild'
BUILD.mkdir(exist_ok=True)
OUT = ROOT / 'deliverables'
env = os.environ.copy()
env['TEXINPUTS'] = '.:/usr/share/texlive/texmf-dist/tex//:/usr/share/texmf/tex//:'
env['TFMFONTS'] = '/usr/share/texlive/texmf-dist/fonts/tfm//:/usr/share/texmf/fonts/tfm//:'
env['VFFONTS'] = '/usr/share/texlive/texmf-dist/fonts/vf//:/usr/share/texmf/fonts/vf//:'
env['T1FONTS'] = '/usr/share/texlive/texmf-dist/fonts/type1//:/usr/share/texmf/fonts/type1//:'
env['ENCFONTS'] = '/usr/share/texlive/texmf-dist/fonts/enc//:/usr/share/texmf/fonts/enc//:'
env['TEXPSHEADERS'] = '/usr/share/texlive/texmf-dist/fonts/enc//:/usr/share/texmf/fonts/enc//:'
env['TEXFONTMAPS'] = str(BUILD) + ':/usr/share/texlive/texmf-dist/fonts/map//:/usr/share/texmf/fonts/map//:'
env['TEXFORMATS'] = str(BUILD) + ':'

maps = [
    '/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/cm.map',
    '/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/cmextra.map',
    '/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/latxfont.map',
    '/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/euler.map',
    '/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/symbols.map',
    '/usr/share/texmf/fonts/map/dvips/lm/lm.map',
]
(BUILD / 'pdftex.map').write_text('\n'.join(Path(p).read_text() for p in maps if Path(p).is_file()))

parser = argparse.ArgumentParser()
parser.add_argument('--passes', type=int, default=1)
args = parser.parse_args()

if not (BUILD / 'pdflatex.fmt').exists():
    result = subprocess.run([
        'pdftex', '-ini', '-etex', '-interaction=nonstopmode', '-halt-on-error',
        '-jobname=pdflatex', '-progname=pdflatex', 'pdflatex.ini'
    ], cwd=BUILD, env=env, text=True, capture_output=True)
    (BUILD / 'format_build.log').write_text(result.stdout + result.stderr)
    if result.returncode:
        print((result.stdout + result.stderr)[-5000:])
        raise SystemExit(result.returncode)

for i in range(args.passes):
    result = subprocess.run([
        'pdftex', '-fmt=pdflatex', '-progname=pdflatex',
        '-interaction=nonstopmode', '-halt-on-error',
        'NEG_NIGHT.tex'
    ], cwd=OUT, env=env, text=True, capture_output=True)
    log = result.stdout + result.stderr
    (BUILD / f'paper_pass_{i+1}.log').write_text(log)
    print(json.dumps({'pass':i+1,'returncode':result.returncode,'log':str(BUILD/f'paper_pass_{i+1}.log')}))
    print(log[-5500:])
    if result.returncode:
        raise SystemExit(result.returncode)
