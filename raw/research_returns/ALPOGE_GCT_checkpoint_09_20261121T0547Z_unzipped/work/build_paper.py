"""Assemble and compile the standalone paper using this session's TeX format."""
from pathlib import Path
import os
import json
import subprocess

base = Path(__file__).resolve().parent.parent
subprocess.run(['python3', str(base/'work/assemble_paper.py')], check=True, cwd=base)
env = os.environ.copy()
environment_file = base/'work/tex_environment.json'
if environment_file.is_file():
    env.update(json.loads(environment_file.read_text()))
format_dir = base/'work/tex_runtime'
if (format_dir/'pdflatex.fmt').is_file():
    env['TEXFORMATS'] = str(format_dir) + ':' + env.get('TEXFORMATS', '')
for i in range(1, 4):
    with (base/f'work/compile_latest_{i}.log').open('w') as log:
        result = subprocess.run(
            ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
             '-output-directory=deliverable', 'deliverable/ALPOGE_GCT.tex'],
            cwd=base, env=env, stdout=log, stderr=subprocess.STDOUT)
    print(f'TeX pass {i}: exit {result.returncode}', flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
