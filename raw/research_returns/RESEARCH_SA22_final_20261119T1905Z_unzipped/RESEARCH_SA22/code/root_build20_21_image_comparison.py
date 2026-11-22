"""Exact body executed inline for build20/build21 rendered-image comparison.

Preserved afterwards under this filename; it was not separately rerun. The
shell tool reported 0.000037206 seconds, not a Python perf_counter measurement.
"""
import hashlib,json
from pathlib import Path
r=Path('qa');out=[]
for b in sorted(r.glob('paper_build21_*.png')):
 a=r/b.name.replace('build21','build20')
 status='new' if not a.exists() else 'identical' if hashlib.sha256(a.read_bytes()).digest()==hashlib.sha256(b.read_bytes()).digest() else 'changed'
 out.append({'page':int(b.stem[-3:]),'status':status})
print(json.dumps(out,indent=2))
Path('code/root_build20_21_image_comparison.json').write_text(json.dumps(out,indent=2)+'\n')
