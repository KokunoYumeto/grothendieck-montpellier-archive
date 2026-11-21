#!/usr/bin/env python3
"""Create and verify the complete research ZIP; never embeds another ZIP."""
from pathlib import Path
import csv, hashlib, io, sys, zipfile

r = Path(__file__).resolve().parent
base = r.parent
target = Path(sys.argv[1]) if len(sys.argv) > 1 else base / 'HODGE_SIGN_final.zip'
members = {}
for p in sorted(r.rglob('*')):
    rel = p.relative_to(r)
    if not p.is_file() or 'tex_build' in rel.parts or '__pycache__' in rel.parts:
        continue
    if p.suffix in {'.zip', '.aux', '.toc', '.out', '.fmt', '.pyc'}:
        continue
    if p.name in {'FILES.tsv', 'HODGE_SIGN.log', 'missfont.log', 'arithmetic_section_check.tex'}:
        continue
    members[rel.as_posix()] = p.read_bytes()
for origin, prefix in [('sources', 'sources'), ('lean_evidence', 'evidence/lean_source'),
                       ('lean_sign_search', 'evidence/lean_search_matches')]:
    folder = base / origin
    if not folder.exists():
        continue
    for p in sorted(folder.rglob('*')):
        if p.is_file() and p.suffix != '.zip':
            members[prefix + '/' + p.relative_to(folder).as_posix()] = p.read_bytes()
prompt = base / 'upload/PROMPT(20261121-001424).md'
if prompt.exists():
    members['sources/PROMPT.md'] = prompt.read_bytes()
required = {'HODGE_SIGN.tex', 'HODGE_SIGN.pdf', 'QUESTIONS.tsv', 'LEDGER.md',
            'CHECK_EVENTS.tsv', 'IMPLICATIONS.md', 'TRANSCRIPTION_NOTES.tsv'}
assert required <= set(members), required - set(members)
assert all(not n.startswith('/') and '..' not in Path(n).parts for n in members)
buf = io.StringIO()
w = csv.writer(buf, delimiter='\t', lineterminator='\n')
w.writerow(['path', 'bytes', 'sha256'])
for name, data in sorted(members.items()):
    w.writerow([name, len(data), hashlib.sha256(data).hexdigest()])
members['FILES.tsv'] = buf.getvalue().encode()
target.parent.mkdir(parents=True, exist_ok=True)
with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for name, data in sorted(members.items()):
        z.writestr(name, data)
with zipfile.ZipFile(target) as z:
    assert z.testzip() is None
    rows = csv.DictReader(io.StringIO(z.read('FILES.tsv').decode()), delimiter='\t')
    for row in rows:
        data = z.read(row['path'])
        assert len(data) == int(row['bytes'])
        assert hashlib.sha256(data).hexdigest() == row['sha256']
    assert len(z.namelist()) == len(set(z.namelist()))
    assert not any(n.endswith('.zip') for n in z.namelist())
print(f'{target}: {len(members)} members, {target.stat().st_size} bytes; CRC, manifest hashes, paths and required deliverables passed.')
