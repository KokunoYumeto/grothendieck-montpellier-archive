#!/usr/bin/env python3
"""Package the research record after its actual stopping review.

This utility does not assess mathematical progress. It refuses to run before
the separately recorded two-consecutive-no-movement stopping rule is met.
Current deliverables and working evidence are included; earlier saved versions
are identified by checkpoint and hash rather than copied into the archive.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import csv
import hashlib
import io
import json
import zipfile

OUT = Path(__file__).resolve().parent.parent
ROOT = OUT.parent.parent
STATE = json.loads((OUT / 'PROGRESS_REVIEW_STATE.json').read_text())
assert STATE.get('stop_rule_reached') is True, 'No actual stopping review is recorded'
assert STATE['consecutive_no_movement'] >= 2
ARCHIVE = ROOT / 'output' / 'RESEARCH_SA07_final.zip'
assert not ARCHIVE.exists(), 'Refusing to replace an existing final archive'

saved_ids = {
    1: 'libfile_fdbc4d4414cc8191b3c1e19714843c7a',
    2: 'libfile_7e71f48896248191931f7a99b7a2bae0',
    3: 'libfile_07530431eb90819190f1f7527f952bc4',
    4: 'libfile_917b46fca9b4819194af1237abf598ce',
    5: 'libfile_0653aab5238c81919dd18aaa06fc2cb3',
    6: 'libfile_c4fe625fd3908191baa3b36e85b45ef4',
    7: 'libfile_ef967b5c40588191b397c25da17551d4',
    8: 'libfile_0f6608efcd4c8191b242c98a1dbc3f42',
    9: 'libfile_847d43d7c2d88191b673bdb9633a9623',
    10: 'libfile_21aeafa6d4e4819195d639a8032340b9',
    11: 'libfile_013862cd33d08191b7646a510dea8546',
}
catalog = []
history = {}
for number, library_id in saved_ids.items():
    checkpoint = ROOT / 'output' / f'RESEARCH_SA07_checkpoint_{number:02d}.zip'
    assert checkpoint.exists(), checkpoint
    catalog.append({
        'archive': checkpoint.name,
        'bytes': checkpoint.stat().st_size,
        'sha256': hashlib.sha256(checkpoint.read_bytes()).hexdigest(),
        'library_file_id': library_id,
        'download': f'https://chatgpt.com/library?file_id={library_id}&account_id=personal',
        'save_observed_successful': True,
    })
    with zipfile.ZipFile(checkpoint) as z:
        for member in z.infolist():
            if member.is_dir() or member.filename.endswith('/FILE_MANIFEST.tsv'):
                continue
            relative = member.filename.removeprefix('RESEARCH_SA07/')
            data = z.read(member)
            key = (relative, hashlib.sha256(data).hexdigest())
            history[key] = (len(data), checkpoint.name)
(OUT / 'CHECKPOINT_CATALOG.json').write_text(json.dumps(catalog, indent=2) + '\n')

assertions = list(csv.DictReader((OUT / 'audit_claims.csv').open()))
counts = Counter(row['status'] for row in assertions)
numbered = list(csv.DictReader((OUT / 'RESEARCH_SA07_results.csv').open()))
computations = list(csv.DictReader((OUT / 'COMPUTATION_RECORD.tsv').open(), delimiter='\t'))
assert all(row['exit_code'] == '0' for row in computations)
for row in computations:
    for path, field in [(OUT / 'code' / row['script'], 'script_sha256'),
                        (OUT / row['output'], 'output_sha256')]:
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row[field], path

readme = [
    '# RESEARCH_SA07 final research package', '',
    'AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed.', '',
    '**The requested programme remains incomplete.** This is the final record under the user\'s actual stopping rule.', '',
    f'The stopping review was recorded at {STATE["actual_utc"]}; it is review {STATE["review_number"]:02d}, with {STATE["consecutive_no_movement"]} consecutive reviews without qualifying movement.', '',
    '## Start here', '',
    '- RESEARCH_SA07_report.md: outcome table, proof scope, computations, corrections, source attempts and visual checks.',
    '- RESEARCH_SA07_paper.pdf: the mathematical record, with its complete LuaLaTeX source and sections.',
    '- RESEARCH_SA07_results.csv: every numbered statement, its dependencies and current proof location.',
    '- audit_claims.csv: every requested canonical assertion and its retained obligation.',
    '- PROGRESS_LEDGER.md: all actual progress reviews, main gates and checkpoint receipts.',
    '- CHECK_EVENTS.tsv and LITERATURE_RECORD.tsv: individual checks and exact source/access records.',
    '- COMPUTATION_RECORD.tsv and code/: reproducible computations, inputs, arithmetic, output and hashes.',
    '- work/: additional audited reductions, exploratory calculations and source-route notes; their stated limitations apply.', '',
    '## Counts', '',
    f'{len(numbered)} numbered statements; {len(assertions)} canonical assertion rows; {len(computations)} registered mathematical programs with passing recorded runs and verified hashes.', '',
    '| Canonical state | Count |', '|---|---:|',
]
readme += [f'| {state} | {count} |' for state, count in sorted(counts.items())]
readme += ['', '## Remaining main gates', '', '| Question | Retained obligation |', '|---|---|']
readme += [f'| {key} | {value.replace(chr(10), " ").replace("|", "/")} |'
           for key, value in STATE['main_gates'].items()]
readme += [
    '', '## Reproduction and version inventory', '',
    'Run python3 code/build_paper.py with LuaLaTeX, latexmk and the packages named in the source. '
    'Run python3 code/record_computations.py to rerun every registered program, or supply the exact script names to rerun a selection. '
    'The environment record names the Python and numerical-library versions.', '',
    'FILE_MANIFEST.tsv hashes every included file. Earlier saved versions are listed with the checkpoint that retains them. '
    'CHECKPOINT_CATALOG.json gives the successful checkpoint identifiers and download links. Earlier ZIP archives are not embedded.', '',
    'Supplied attachments, retrieved original sources, rendered inspection images, interpreter caches and TeX runtime dependencies are excluded. '
    'Their source identities, access attempts and the specific visual checks are recorded in the report. Mathematical obligations have not been dropped.', '',
]
(OUT / 'RESEARCH_SA07_README.md').write_text('\n'.join(readme))

allowed = {'.tex', '.pdf', '.csv', '.bib', '.md', '.tsv', '.py', '.out', '.txt', '.json'}
entries = {}
for path in OUT.rglob('*'):
    if path.is_file() and path.suffix in allowed and path.name != 'FILE_MANIFEST.tsv':
        entries[str(path.relative_to(OUT))] = path
for path in (ROOT / 'work').glob('*'):
    if path.is_file() and path.suffix in allowed - {'.pdf'}:
        entries['work/' + path.name] = path
for folder in (ROOT / 'work').glob('code_*'):
    for path in folder.rglob('*'):
        if path.is_file() and path.suffix in allowed:
            entries['work/' + str(path.relative_to(ROOT / 'work'))] = path
for folder_name in ['elliptic_tex_next']:
    for path in (ROOT / 'work' / folder_name).rglob('*'):
        if path.is_file() and path.suffix in allowed:
            entries['work/' + str(path.relative_to(ROOT / 'work'))] = path

snapshots = {name: path.read_bytes() for name, path in sorted(entries.items())}
records = []
current_keys = set()
for name, data in snapshots.items():
    digest = hashlib.sha256(data).hexdigest()
    current_keys.add((name, digest))
    records.append([name, len(data), digest, 'included_current', ARCHIVE.name])
for (name, digest), (size, checkpoint) in sorted(history.items()):
    if (name, digest) not in current_keys:
        records.append([name, size, digest, 'earlier_saved_version', checkpoint])
buf = io.StringIO()
writer = csv.writer(buf, delimiter='\t', lineterminator='\n')
writer.writerow(['file', 'bytes', 'sha256', 'state', 'held_in'])
writer.writerows(records)
(OUT / 'FILE_MANIFEST.tsv').write_text(buf.getvalue())
with zipfile.ZipFile(ARCHIVE, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for name, data in snapshots.items():
        z.writestr('RESEARCH_SA07/' + name, data)
    z.writestr('RESEARCH_SA07/FILE_MANIFEST.tsv', buf.getvalue())
assert ARCHIVE.stat().st_size < 500 * 1024 * 1024, 'Split before saving: archive exceeds500 MiB'
with zipfile.ZipFile(ARCHIVE) as z:
    assert z.testzip() is None, 'ZIP CRC verification failed'
print(json.dumps({
    'archive': str(ARCHIVE), 'files': len(snapshots) + 1,
    'historical_versions_indexed': len(records) - len(snapshots),
    'bytes': ARCHIVE.stat().st_size,
    'sha256': hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'stopping_review': STATE['review_number'],
}))
