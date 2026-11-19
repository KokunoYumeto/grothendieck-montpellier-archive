"""Save a research search result passed on stdin; no interpretation."""
from pathlib import Path
import sys,datetime
root=Path(__file__).resolve().parents[1]
name=sys.argv[1]
text=sys.stdin.read()
(root/'evidence'/name).write_text(text)
print(f'Saved {name}: {len(text)} characters')
