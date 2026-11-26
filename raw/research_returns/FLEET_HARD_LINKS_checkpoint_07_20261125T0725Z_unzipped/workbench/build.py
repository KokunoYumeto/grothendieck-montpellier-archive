#!/usr/bin/env python3
"""Build each standalone paper from a clean temporary copy.
Run from any directory: python build.py [A B C]
Requires Python 3 and pdfLaTeX (TeX Live, standard packages).
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
records = []
for letter in (sys.argv[1:] or ['A', 'B', 'C']):
    source = ROOT / 'papers' / letter
    with tempfile.TemporaryDirectory(prefix='fleet-paper-' + letter + '-') as td:
        build = Path(td)
        for p in source.rglob('*'):
            if p.is_file() and p.suffix in {'.tex', '.bib', '.sty', '.cls', '.png', '.pdf', '.eps'} and p.name != 'main.pdf':
                dest = build / p.relative_to(source)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(p, dest)
        for run in range(3):
            proc = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'main.tex'],
                                  cwd=build, capture_output=True, text=True)
            if proc.returncode:
                print(proc.stdout[-12000:])
                raise SystemExit(proc.returncode)
        log = (build/'main.log').read_text(errors='replace')
        over = [float(x) for x in re.findall(r'Overfull \\hbox \(([0-9.]+)pt too wide\)', log)]
        unresolved = bool(re.search(r'(undefined references|undefined citations|Citation .+ undefined|Reference .+ undefined)', log))
        for name in ['main.pdf']:
            shutil.copy2(build/name, source/name)
        (ROOT/'checks'/('build_'+letter+'.log')).write_text(log)
        record = {'paper':letter,'engine':'pdfLaTeX','clean_copy':True,'passes':3,
                  'overfull_boxes_pt':over,'unresolved_references':unresolved,
                  'pdf_sha256':hashlib.sha256((source/'main.pdf').read_bytes()).hexdigest()}
        records.append(record)
        print(json.dumps(record))
(ROOT/'checks'/'build_latest.json').write_text(json.dumps(records,indent=2)+'\n')
