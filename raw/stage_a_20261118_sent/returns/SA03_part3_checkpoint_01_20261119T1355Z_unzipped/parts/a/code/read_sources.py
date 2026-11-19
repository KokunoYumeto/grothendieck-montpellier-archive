"""Read source ranges with stable original-file line numbers; no classification."""
import sys
from pathlib import Path
p=Path(sys.argv[1]); start=int(sys.argv[2]); end=int(sys.argv[3])
for n,line in enumerate(p.read_text().splitlines(),1):
 if start<=n<=end: print(f'{n:04d}: {line}')
