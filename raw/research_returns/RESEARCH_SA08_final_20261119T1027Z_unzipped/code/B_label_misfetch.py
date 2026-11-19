"""Preserve and correctly label a PDF reached by a mistaken article number."""
from pathlib import Path
import json

base = Path(__file__).resolve().parents[1]
old = 'B_cenkl_porter1984_cubical'
new = 'B_butler_erbe1984_misfetch'
for suffix in ('.pdf', '.txt'):
    source = base / 'sources' / (old + suffix)
    target = base / 'sources' / (new + suffix)
    if source.exists():
        source.rename(target)
receipt = base / 'logs' / (old + '_fetch.json')
record = json.loads(receipt.read_text())
record['corrected_file'] = str(base / 'sources' / (new + '.pdf'))
record['verification'] = ('First page proves this is Butler and Erbe, '
    'Comparison theorems for second-order operator-valued linear differential '
    'equations, Pacific J. Math.112(1984),21-34. It is not the Cenkl-Porter '
    'article at pp35-48 and is not used for SA08.')
receipt.write_text(json.dumps(record, indent=2))
print(record['verification'])
