#!/usr/bin/env python3
"""Print numbered source text and preserve an exact reading/output audit trail.

Usage: read_sources.py RELATIVE_SOURCE [START [END]]
The numbers are one-based physical UTF-8 source lines, not manuscript lines.
"""
from pathlib import Path
from datetime import datetime, timezone
import sys

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'sources'
args = sys.argv[1:]
path = (SOURCE / args[0]).resolve()
assert path.is_relative_to(SOURCE.resolve())
lines = path.read_text().splitlines()
start = int(args[1]) if len(args) > 1 else 1
end = min(int(args[2]), len(lines)) if len(args) > 2 else len(lines)
stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
out = '\n'.join([f'FILE {path.relative_to(SOURCE)} | lines {start}–{end} / {len(lines)}'] +
                [f'{i:5}: {lines[i-1]}' for i in range(start,end+1)]) + '\n'
dest = ROOT / 'work/outputs' / f'read_{stamp}_{path.stem}_{start}-{end}.txt'
dest.write_text(out)
with (ROOT/'work/progress.log').open('a') as f:
    f.write(f'{stamp}\tSOURCE_READ\t{path.relative_to(SOURCE)}:{start}-{end}; output={dest.relative_to(ROOT/"work")}\n')
print(out)
