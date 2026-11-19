#!/usr/bin/env python3
"""Read numbered source lines and preserve the exact displayed output for audit.

This is a retrieval helper only: it does not generate any editorial verdict.
"""
import sys
from pathlib import Path
from datetime import datetime, timezone

root = Path('/workspace/scratch/a5176e5b5d45')
out = root / 'SA06_work/parts/cote14_early'
p = root / 'source' / sys.argv[1]
start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
lines = p.read_text().splitlines()
end = int(sys.argv[3]) if len(sys.argv) > 3 else len(lines)
text = '\n'.join(f'{i}: {line}' for i, line in enumerate(lines, 1) if start <= i <= end)
audit = out / 'audit'
audit.mkdir(exist_ok=True)
(audit / f'{p.stem}_{start:04}_{end:04}.txt').write_text(text + '\n')
with (out / 'progress.log').open('a') as f:
    f.write(f'{datetime.now(timezone.utc).isoformat()}\tREAD\t{p.relative_to(root)}:{start}-{end}\n')
print(text)
