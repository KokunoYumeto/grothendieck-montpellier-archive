from pathlib import Path
import csv,hashlib
a=Path('crops');b=Path('work/regenerated')
one=sorted(p.name for p in a.glob('*.png'));two=sorted(p.name for p in b.glob('*.png'))
assert one==two and len(one)==415,(len(one),len(two))
for name in one:
 p=a/name;q=b/name
 assert p.stat().st_size==q.stat().st_size and hashlib.sha256(p.read_bytes()).digest()==hashlib.sha256(q.read_bytes()).digest(),name
print(f'All {len(one)} inspection PNGs recreated byte-for-byte from the original supplied scans and the two tables.')
