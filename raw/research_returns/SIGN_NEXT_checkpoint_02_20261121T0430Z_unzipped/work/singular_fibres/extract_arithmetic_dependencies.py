#!/usr/bin/env python3
"""Copy exact Lean archive members for source review; do not modify or compile Lean."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import tarfile

ROOT = Path('/workspace/scratch/3c0a202771c9')
OUT = ROOT/'SIGN_NEXT/work/singular_fibres/arithmetic_review'
p = argparse.ArgumentParser()
p.add_argument('name')
p.add_argument('path_regex')
a = p.parse_args()
pattern = re.compile(a.path_regex)

class Parts:
    def __init__(self):
        self.i = 1
        self.f = (ROOT/'lean_parts/part01').open('rb')
    def read(self, n=-1):
        chunks = []
        remaining = n
        while self.i <= 14 and (remaining > 0 or n < 0):
            chunk = self.f.read(remaining)
            if chunk:
                chunks.append(chunk)
                if n >= 0:
                    remaining -= len(chunk)
            else:
                self.f.close()
                self.i += 1
                if self.i <= 14:
                    self.f = (ROOT/f'lean_parts/part{self.i:02d}').open('rb')
        return b''.join(chunks)

records = []
with tarfile.open(fileobj=Parts(), mode='r|gz') as tf:
    for member in tf:
        rel = member.name.removeprefix('lean/src/')
        if not member.isfile() or not rel.endswith('.lean') or not pattern.search(rel):
            continue
        data = tf.extractfile(member).read()
        destination = OUT/'source_cache'/rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        records.append({'path':rel, 'bytes':len(data),
                        'sha256':hashlib.sha256(data).hexdigest()})
report = {'path_regex':pattern.pattern, 'selected_files':len(records),
          'bytes':sum(r['bytes'] for r in records), 'records':records,
          'scope':'exact archive copies for source inspection; no Lean build'}
(OUT/f'{a.name}_manifest.json').write_text(json.dumps(report,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='records'}),flush=True)
