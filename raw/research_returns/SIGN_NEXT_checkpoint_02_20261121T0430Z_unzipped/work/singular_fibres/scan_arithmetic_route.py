#!/usr/bin/env python3
"""Read-only exact-source search for the arithmetic specialization routes.

No Lean code is changed or compiled.  Regex matches are research locators,
not formal certificates or claims about unmentioned declarations.
"""
from pathlib import Path
import argparse
import hashlib
import json
import re
import tarfile

ROOT = Path('/workspace/scratch/3c0a202771c9')
OUT = ROOT/'SIGN_NEXT/work/singular_fibres/arithmetic_review'
parser = argparse.ArgumentParser()
parser.add_argument('name')
parser.add_argument('regex')
args = parser.parse_args()
terms = re.compile(args.regex, re.MULTILINE)


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
members = files = 0
with tarfile.open(fileobj=Parts(), mode='r|gz') as tf:
    for member in tf:
        members += 1
        if not member.isfile() or not member.name.endswith('.lean'):
            continue
        files += 1
        data = tf.extractfile(member).read()
        text = data.decode('utf-8')
        if not terms.search(text):
            continue
        rel = member.name.removeprefix('lean/src/')
        destination = OUT/'source_cache'/rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        hits = [{'line':i, 'text':line}
                for i,line in enumerate(text.splitlines(),1) if terms.search(line)]
        records.append({'path':rel, 'bytes':len(data),
                        'sha256':hashlib.sha256(data).hexdigest(),'hits':hits})
        print(f'{rel}: {len(hits)} matches', flush=True)

report = {'members_scanned':members,'lean_files_scanned':files,
          'terms_regex':terms.pattern,'selected_files':len(records),
          'records':records,'scope':'read-only text search; no Lean compilation'}
(OUT/f'{args.name}_manifest.json').write_text(json.dumps(report,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='records'}),flush=True)
