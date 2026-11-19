"""Reproduce the initial attachment inspection and safe source extraction.

Usage: python SA05/programs/bootstrap.py
The supplied uploads must already be present; no source bytes are in SA05.zip.
"""
from pathlib import Path
from zipfile import ZipFile
import collections, csv, difflib, json

root = Path(__file__).resolve().parents[2]
out = root / 'SA05' / 'programs' / 'outputs'
out.mkdir(parents=True, exist_ok=True)
report = []
for p in sorted((root / 'upload').glob('*.zip')):
    with ZipFile(p) as z:
        report.append({'archive': p.name, 'members': [
            {'name': i.filename, 'bytes': i.file_size} for i in z.infolist()]})
for label in ('notes', 'texts'):
    target = root / 'sources' / label
    with ZipFile(root / 'upload' / f'SA05_{label}.zip') as z:
        for member in z.infolist():
            if not (target / member.filename).resolve().is_relative_to(target.resolve()):
                raise ValueError(member.filename)
        z.extractall(target)
with ZipFile(root / 'upload' / 'SA05_PROMPT.zip') as z:
    old = z.read('PROMPT.md').decode('utf-8').splitlines()
new = (root / 'upload' / 'PROMPT(4).md').read_text().splitlines()
rows = list(csv.DictReader((root / 'sources/notes/NOTES_INDEX.tsv').open(), delimiter='\t'))
report.append({'entries': len(rows), 'by_package': dict(collections.Counter(r['package'] for r in rows))})
report.append({'prompt_diff': '\n'.join(difflib.unified_diff(old, new, fromfile='zip_prompt', tofile='attached_prompt'))})
result = json.dumps(report, ensure_ascii=False, indent=2)
(out / 'bootstrap.json').write_text(result + '\n')
print(result)
