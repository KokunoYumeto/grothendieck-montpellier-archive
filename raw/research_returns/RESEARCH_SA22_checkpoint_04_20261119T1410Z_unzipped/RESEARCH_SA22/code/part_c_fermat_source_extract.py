#!/usr/bin/env python3
"""Extract and render the exact original pages used in the Fermat proof."""
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
pdf = root / 'sources/shioda_katsura1979.pdf'
outdir = root / 'sources/shioda_katsura1979_pages'
outdir.mkdir(exist_ok=True)
start = time.perf_counter()
began = datetime.now(timezone.utc).isoformat()
commands = [
    ['pdftotext', '-layout', str(pdf), str(root/'sources/shioda_katsura1979.txt')],
]
for page in (2, 3, 7):
    commands.append(['pdftoppm', '-f', str(page), '-l', str(page), '-singlefile', '-r', '130', '-png', str(pdf), str(outdir/f'printed-{page+96}')])
events = []
for cmd in commands:
    t = time.perf_counter()
    p = subprocess.run(cmd, capture_output=True, text=True, check=False)
    events.append({'command': cmd, 'exit_code': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr, 'runtime_seconds': time.perf_counter()-t})
    if p.returncode:
        break
out = {'started_utc': began, 'runtime_seconds': time.perf_counter()-start, 'results': events}
Path(__file__).with_name('part_c_fermat_source_extract_output.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
