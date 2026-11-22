#!/usr/bin/env python3
"""Verify an immutable archive against its manifest and required deliverables."""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import time
import zipfile

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('archive', type=Path)
parser.add_argument('label')
args = parser.parse_args()
started = time.perf_counter()
required = {'RESEARCH_SA06_paper.tex', 'RESEARCH_SA06_paper.pdf',
            'RESEARCH_SA06_results.csv', 'RESEARCH_SA06_references.bib',
            'RESEARCH_SA06_report.md', 'CHECK_EVENTS.tsv', 'PROGRESS_LEDGER.md',
            'research_apalike.bst', 'FILE_LIST.tsv', 'code/PROGRAM_INDEX.md'}
with zipfile.ZipFile(args.archive) as archive:
    names = set(archive.namelist())
    manifest = list(csv.DictReader(io.StringIO(archive.read('FILE_LIST.tsv').decode()), delimiter='\t'))
    errors = []
    for row in manifest:
        data = archive.read(row['path'])
        if len(data) != int(row['bytes']) or hashlib.sha256(data).hexdigest() != row['sha256']:
            errors.append(row['path'])
    listed = {r['path'] for r in manifest} | {'FILE_LIST.tsv'}
    missing = sorted(required-names)
    assert not errors, errors
    assert not missing, missing
    assert names == listed, sorted(names.symmetric_difference(listed))
    assert args.archive.stat().st_size < 500_000_000
    outputs = sorted(n for n in names if n.endswith('.out') and '/output/' in n)
    c3be = [n for n in outputs if 'surface_reduction_Fpbar' in n]
    assert c3be, 'The retained C.3be compiler stdout is absent'
result = {'utc': datetime.now(timezone.utc).isoformat(), 'archive': str(args.archive),
          'status': 'pass', 'archive_files': len(names), 'manifest_rows': len(manifest),
          'size_bytes': args.archive.stat().st_size,
          'sha256': hashlib.sha256(args.archive.read_bytes()).hexdigest(),
          'missing_required_files': missing, 'hash_or_length_failures': errors,
          'owner_output_stdout_files': len(outputs), 'retained_C3be_stdout': c3be,
          'runtime_seconds': time.perf_counter()-started}
(root/'logs'/f'{args.label}_archive_verification.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
