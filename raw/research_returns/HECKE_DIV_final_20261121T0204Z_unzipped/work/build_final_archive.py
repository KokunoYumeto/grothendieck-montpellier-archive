"""Package already checked deliverables. This is not a mathematical proof checker."""
from pathlib import Path
import csv
import hashlib
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'deliverables'
COMPILED = ROOT / 'package'
OUT = ROOT / 'final_payload'
OUT.mkdir(exist_ok=True)
assert not any(OUT.iterdir()), 'Use an empty staging directory; no existing payload is overwritten.'

top = ['README.md', 'QUESTIONS.tsv', 'LEDGER.md', 'CHECK_EVENTS.tsv',
       'IMPLICATIONS.md', 'TRANSCRIPTION_NOTES.tsv', 'SOURCE_MANIFEST.tsv']
for name in top:
    shutil.copy2(D/name, OUT/name)
for name in ['HECKE_DIV.tex', 'HECKE_DIV.pdf']:
    shutil.copy2(COMPILED/name, OUT/name)
shutil.copytree(ROOT/'source', OUT/'source')
(OUT/'source_tex').mkdir()
for p in sorted(D.glob('*.tex')):
    shutil.copy2(p, OUT/'source_tex'/p.name)
shutil.copy2(ROOT/'upload'/'PROMPT(20261121-004949).md', OUT/'TASK_PROMPT.md')

excluded_parts = {'__pycache__', 'texformats', 'library_helpers_20261121'}
excluded_names = {'checkpoint01_xattrs.json', 'final_xattrs.json',
                  'grothendieck_cote16_ranges.pdf', 'EGA_III2.pdf'}
for p in sorted((ROOT/'work').rglob('*')):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT/'work')
    if any(x in excluded_parts for x in rel.parts) or p.name in excluded_names:
        continue
    if p.suffix in {'.pyc', '.fmt'} or 'checkpoint' in p.name.lower() or p.name.endswith('_xattrs.json'):
        continue
    dest = OUT/'work'/rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(p, dest)

tex = (OUT/'HECKE_DIV.tex').read_text()
assert '\\input{' not in tex and '\\include{' not in tex
assert tex.count('\\begin{proof}') == tex.count('\\end{proof}')
assert '\\end{document}' in tex
assert all(ord(ch) >= 32 or ch in '\n\r\t' for ch in tex)
with (OUT/'SOURCE_MANIFEST.tsv').open() as f:
    originals = list(csv.DictReader(f, delimiter='\t'))
assert len(originals) == 12
for row in originals:
    p = OUT/row['source_path']
    assert p.stat().st_size == int(row['bytes'])
    assert hashlib.sha256(p.read_bytes()).hexdigest() == row['sha256']
with (OUT/'QUESTIONS.tsv').open() as f:
    questions = list(csv.DictReader(f, delimiter='\t'))
assert len({row['id'] for row in questions}) == len(questions)
with (OUT/'CHECK_EVENTS.tsv').open() as f:
    events = list(csv.DictReader(f, delimiter='\t'))
assert all(row['statement_id'] and row['date'] and row['who'] and row['outcome'] for row in events)

files = sorted(p for p in OUT.rglob('*') if p.is_file())
manifest = ''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(OUT).as_posix()+'\n' for p in files)
(OUT/'MANIFEST.sha256').write_text(manifest)
archive = ROOT/'HECKE_DIV_final.zip'
assert not archive.exists(), 'The final archive already exists; do not overwrite a delivered archive.'
with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for p in sorted(p for p in OUT.rglob('*') if p.is_file()):
        z.write(p, p.relative_to(OUT).as_posix())
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    names = z.namelist()
    assert not any(n.lower().endswith('.zip') or 'checkpoint' in Path(n).name.lower() for n in names)
    for line in z.read('MANIFEST.sha256').decode().splitlines():
        checksum, name = line.split('  ', 1)
        assert hashlib.sha256(z.read(name)).hexdigest() == checksum
    for name in ['HECKE_DIV.tex', 'HECKE_DIV.pdf', *top]:
        assert name in names
report = {'file': str(archive), 'bytes': archive.stat().st_size,
          'sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
          'files': len(names), 'questions': len(questions), 'check_events': len(events),
          'proof_environments': tex.count('\\begin{proof}'),
          'crc_and_all_manifest_hashes': 'passed', 'nested_archives': 0}
print(json.dumps(report, indent=2))
