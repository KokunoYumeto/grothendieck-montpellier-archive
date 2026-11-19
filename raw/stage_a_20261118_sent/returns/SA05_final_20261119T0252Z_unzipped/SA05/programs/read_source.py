"""Expose source lines/scans/entries and retain an auditable reading log.

Usage: python SA05/programs/read_source.py PATH START END [OWNER]
Line numbering is physical, starting at one. This merely exposes text; the
reviewer's judgment is recorded separately and is never generated here.
"""
from pathlib import Path
from datetime import datetime, timezone
import sys, hashlib, csv

base = Path(__file__).resolve().parents[2]
path = Path(sys.argv[1]); path = path if path.is_absolute() else base / path
start, end = int(sys.argv[2]), int(sys.argv[3])
owner = sys.argv[4] if len(sys.argv)>4 else 'root'
lines = path.read_text().splitlines()
end = min(end, len(lines))
text = '\n'.join(f'{i+1:05d}: {lines[i]}' for i in range(start-1, end))
out = base / 'SA05/work' / owner / 'readouts'
out.mkdir(parents=True, exist_ok=True)
dest = out / f'{path.stem}__{start:05d}-{end:05d}.txt'
dest.write_text(text+'\n')
log = base / 'SA05/work' / owner / 'reading_log.tsv'
new = not log.exists()
with log.open('a') as f:
    w=csv.writer(f,delimiter='\t')
    if new: w.writerow(['date','file','start','end','sha256','output','status'])
    w.writerow([datetime.now(timezone.utc).isoformat(),str(path.relative_to(base)),start,end,hashlib.sha256(path.read_bytes()).hexdigest(),str(dest.relative_to(base/'SA05')),'exposed for close reading; not an automated verdict'])
print(text)
