#!/usr/bin/env python3
"""Package the reviewed CX_GRH deliverables and authored research record."""
from pathlib import Path
import csv
import hashlib
import io
import json
import zipfile

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / 'work'
DELIVERABLES = ROOT / 'deliverables'
OUTPUT = ROOT / 'CX_GRH_final.zip'

required = {'CX_GRH.tex', 'CX_GRH.pdf', 'QUESTIONS.tsv', 'LEDGER.md',
            'CHECK_EVENTS.tsv', 'IMPLICATIONS.md', 'README.md'}
files = {}
for path in sorted(DELIVERABLES.iterdir()):
    if path.is_file() and path.name != 'MANIFEST.sha256':
        files[path.name] = path.read_bytes()

for path in sorted(WORK.iterdir()):
    if path.is_file() and path.suffix in {'.md', '.tex', '.tsv', '.py', '.json'}:
        if path.name == 'SOURCE_FILES.tsv':
            continue
        files['work/' + path.name] = path.read_bytes()

files['research/PROMPT.md'] = (ROOT / 'upload/PROMPT(20261120-225916).md').read_bytes()
files['research/SOURCE_FILES.tsv'] = (WORK / 'SOURCE_FILES.tsv').read_bytes()
for path in sorted((WORK / 'final_qa').glob('*.png')):
    files['research/visual_QA/' + path.name] = path.read_bytes()
for name in ['compile-7.log', 'compile-8.log']:
    files['research/typesetting/' + name] = (WORK / 'texbuild' / name).read_bytes()

assert required <= files.keys(), required - files.keys()
assert not any(name.lower().endswith('.zip') for name in files)
assert all(not name.startswith('/') and '..' not in Path(name).parts for name in files)

manifest = ''.join(f'{hashlib.sha256(data).hexdigest()}  {name}\n'
                   for name, data in sorted(files.items()))
files['MANIFEST.sha256'] = manifest.encode('utf-8')

with zipfile.ZipFile(OUTPUT, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for name, data in sorted(files.items()):
        archive.writestr(name, data)

with zipfile.ZipFile(OUTPUT) as archive:
    assert archive.testzip() is None
    assert len(archive.namelist()) == len(set(archive.namelist()))
    assert set(archive.namelist()) == set(files)
    for name, data in files.items():
        assert archive.read(name) == data, name
    for row in csv.DictReader(io.StringIO(archive.read('PROOF_FILES_SHA256.tsv').decode()), delimiter='\t'):
        assert hashlib.sha256(archive.read(row['file'])).hexdigest() == row['sha256'], row['file']
    questions = list(csv.DictReader(io.StringIO(archive.read('QUESTIONS.tsv').decode()), delimiter='\t'))
    checks = list(csv.DictReader(io.StringIO(archive.read('CHECK_EVENTS.tsv').decode()), delimiter='\t'))
    assert len(questions) == 39
    assert len(checks) == 197
    assert archive.read('CX_GRH.pdf').startswith(b'%PDF-')

print(json.dumps({
    'path': str(OUTPUT), 'bytes': OUTPUT.stat().st_size,
    'sha256': hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
    'files': len(files), 'questions': len(questions), 'check_events': len(checks),
    'required_files_present': True, 'crc_and_content_validation': 'passed',
    'proof_file_hashes': 'passed', 'nested_checkpoint_archives': 0
}, indent=2))
