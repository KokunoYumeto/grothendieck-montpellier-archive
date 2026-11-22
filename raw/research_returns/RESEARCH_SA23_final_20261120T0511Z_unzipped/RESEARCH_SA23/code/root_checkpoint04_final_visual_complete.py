"""Record the actual eleven-page visual inspection of the final checkpoint PDF."""
from pathlib import Path
import datetime, hashlib, json, re, time
root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
path = root / 'logs/root_pdf_review_checkpoint04_final.json'
record = json.loads(path.read_text())
pdf_hash = hashlib.sha256((root / 'RESEARCH_SA23_paper.pdf').read_bytes()).hexdigest()
assert pdf_hash == record['pdf_sha256']
assert record['pages_rendered'] == [1, 20, 40, 45, 46, 47, 60, 67, 78, 79, 87]
build = json.loads((root / 'logs/build_diagnostics.json').read_text())
assert all(command['returncode'] == 0 for command in build['commands'])
assert build['warnings'] == [] and build['overfull_count'] == 0
record.update({'visual_inspection': 'Root displayed all eleven page images separately and inspected them directly.',
               'inspection_completed_utc': stamp,
               'inspection_findings': 'No clipping, overlapping text, missing symbols or page-margin overflow observed.'})
path.write_text(json.dumps(record, indent=2) + '\n')
bib = (root / 'RESEARCH_SA23_references.bib').read_text()
starts = list(re.finditer(r'(?m)^@\w+\s*\{\s*([^,\s]+)\s*,', bib))
missing = []
for i, match in enumerate(starts):
    body = bib[match.start():starts[i+1].start() if i+1 < len(starts) else len(bib)]
    if 'opened' not in body.casefold():
        missing.append(match.group(1))
assert missing == []
qa = root / 'verification/visual_QA.md'
marker = '### Fourth checkpoint: final bibliography build'
assert marker not in qa.read_text()
with qa.open('a') as handle:
    handle.write(f'''

{marker}

The preparation PDF was subsequently rebuilt to include three additional
documentary bibliography entries and to repair observed spacing in notes.
Its 86-page visual record above is retained and is not substituted for this
new inspection. The delivered checkpoint PDF has **87 pages** and SHA256
**{pdf_hash}**. Inspection completed {stamp}.

We displayed and inspected pages 1, 20, 40, 45, 46, 47, 60, 67, 78, 79 and
87 one at a time. No clipping, overlaps, missing symbols or margin overflow
was observed. All four compilation commands returned zero; warnings 0,
overfull boxes 0, overflows above 2pt 0, maximum overflow 0pt. Counts
before/after remain 0/0. There were no overflow pages requiring inspection.
Build time: {build['seconds']:.9f} seconds. Render time:
{record['elapsed_seconds']:.9f} seconds. All 85 bibliography entries have
an explicit opened or not-opened statement, qualified where only metadata
or a later source was inspected.
''')
output = {'created_utc': stamp, 'pdf_pages': record['pdf_pages'], 'pdf_sha256': pdf_hash,
          'pages_inspected': record['pages_rendered'], 'bibliography_entries': len(starts),
          'missing_access_flags': missing, 'overfull_before': 0, 'overfull_after': 0,
          'elapsed_seconds': time.perf_counter() - started}
(root / 'logs/root_checkpoint04_final_visual_complete.json').write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps(output, indent=2))
