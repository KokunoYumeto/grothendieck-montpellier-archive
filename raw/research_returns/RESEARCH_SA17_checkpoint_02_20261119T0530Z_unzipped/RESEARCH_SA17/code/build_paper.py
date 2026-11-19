"""Rebuild the paper with LuaLaTeX, bibliography, and explicit log checks.

Normally uses the installed lualatex. This session used a recovered format and
TEXMF tree; optional --format and --texmf preserve that invocation exactly.
Visual inspection remains separate and is never implied by this script.
"""
from pathlib import Path
import argparse, hashlib, json, os, re, subprocess, time
from datetime import datetime, timezone

p = argparse.ArgumentParser()
p.add_argument('--format')
p.add_argument('--texmf')
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
env = os.environ.copy()
if a.texmf:
    env['TEXMFHOME'] = str(Path(a.texmf).resolve())
    env['TEXFONTMAPS'] = str(Path(a.texmf).resolve()) + '//:'
cmd = ['lualatex']
if a.format:
    cmd += ['--fmt=' + str(Path(a.format).resolve())]
cmd += ['-interaction=nonstopmode', '-halt-on-error', 'RESEARCH_SA17_paper.tex']
stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
start = time.perf_counter()
steps = []
for index, command in enumerate([cmd, ['bibtex', 'RESEARCH_SA17_paper'], cmd, cmd]):
    log = root / 'logs' / f'build_{stamp}_{index}.txt'
    with log.open('w') as out:
        r = subprocess.run(command, cwd=root, env=env, stdout=out,
                           stderr=subprocess.STDOUT)
    steps.append({'command': command, 'returncode': r.returncode,
                  'log': str(log.relative_to(root))})
    if r.returncode:
        raise SystemExit(f'Build failed; see {log}')
text = (root / 'RESEARCH_SA17_paper.log').read_text()
overflows = [float(x) for x in re.findall(r'Overfull \\[hv]box \(([\d.]+)pt', text)]
warnings = [s for s in text.splitlines() if 'undefined' in s.lower()
            or 'Missing character:' in s]
pdf = root / 'RESEARCH_SA17_paper.pdf'
result = {'timestamp': stamp, 'seconds': time.perf_counter()-start,
          'steps': steps, 'overfull_pt': overflows,
          'overfull_above_2pt': sum(x > 2 for x in overflows),
          'warnings': warnings, 'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
          'visual_qa': 'not performed by this script'}
(root / 'logs' / f'build_{stamp}.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result))
if any(x > 2 for x in overflows) or warnings:
    raise SystemExit('Build-log QA did not pass.')
