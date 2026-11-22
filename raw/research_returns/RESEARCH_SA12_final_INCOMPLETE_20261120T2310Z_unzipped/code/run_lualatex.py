"""Run a logged LuaLaTeX pass with this workspace's existing support tree."""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
support = root.parent / 'sa12_tex_support'
assert len(sys.argv) == 2, 'Supply a new immutable build-pass log name.'
name = sys.argv[1]
assert not (root / f'code/output/{name}.run.json').exists()
env = os.environ.copy()
env['TEXMF'] = '{' + str(support / 'texmf') + ',/usr/share/texlive/texmf-dist,/usr/share/texmf}'
fmt = support / 'lualatex.fmt'
assert fmt.is_file()
config = {'recorded_utc': datetime.now(timezone.utc).isoformat(),
          'TEXMF': env['TEXMF'], 'format': str(fmt), 'build': name}
(root / f'code/output/{name}.runtime.json').write_text(json.dumps(config, indent=2) + '\n')
result = subprocess.run([
    'python3', 'code/run_logged.py', name, 'lualatex', '-fmt=' + str(fmt),
    '-interaction=nonstopmode', '-halt-on-error', '-output-directory=build',
    'RESEARCH_SA12_paper.tex'
], cwd=root, env=env)
raise SystemExit(result.returncode)
