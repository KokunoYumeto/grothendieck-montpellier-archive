"""Record completed direct image inspections of the delivered fifth-checkpoint PDF."""
from pathlib import Path
import datetime, hashlib, json, re, time

root = Path(__file__).resolve().parents[1]
start = time.perf_counter()
target = root/'logs/root_checkpoint05_visual_complete.json'
if target.exists():
    raise SystemExit('Fifth-checkpoint visual record already exists.')
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
record_path = root/'logs/root_pdf_review_checkpoint05_final.json'
record = json.loads(record_path.read_text())
pdf_hash = hashlib.sha256((root/'RESEARCH_SA23_paper.pdf').read_bytes()).hexdigest()
assert pdf_hash == record['pdf_sha256'] == 'f4c32598c77805631fcecf7fce909411c53583f2bffd7f0c14fa58d5fc5edab7'
root_pages = [45,46,47,49,68,79,80,81,82,84]
algebra_pages = [1,20,40,60,90]
assert sorted(root_pages+algebra_pages) == record['pages_rendered']
assert (root/'notes/algebra_checkpoint05_visual_QA.md').exists()
build = json.loads((root/'logs/build_diagnostics.json').read_text())
assert len(build['commands']) == 4
assert all(command['returncode'] == 0 for command in build['commands'])
assert build['warnings'] == [] and build['overfull_count'] == 0
bib = (root/'RESEARCH_SA23_references.bib').read_text()
starts = list(re.finditer(r'(?m)^@\w+\s*\{\s*([^,\s]+)\s*,', bib))
missing = []
for i, match in enumerate(starts):
    body = bib[match.start():starts[i+1].start() if i+1<len(starts) else len(bib)]
    if 'opened' not in body.casefold():
        missing.append(match.group(1))
assert len(starts) == 96 and not missing
record.update({'visual_inspection': 'All fifteen rendered page images displayed one at a time and inspected directly: ten by root, five by the algebra agent.',
               'inspection_completed_utc':stamp,
               'root_pages_inspected':root_pages,
               'algebra_pages_inspected':algebra_pages,
               'inspection_findings':'No clipping, overlapping text, missing symbols or page-margin overflow observed. Page81 contains the short final scope paragraph before the bibliography page break.',
               'algebra_evidence':'notes/algebra_checkpoint05_visual_QA.md;logs/algebra_checkpoint05_visual_QA.json'})
record_path.write_text(json.dumps(record,indent=2)+'\n')
with (root/'verification/visual_QA.md').open('a') as handle:
    handle.write(f'''

### Fifth checkpoint: final 96-entry bibliography build

The delivered paper has **90 pages**, SHA256 **{pdf_hash}**. Inspection
completed {stamp}. We directly displayed fifteen page images individually:
root inspected pages 45, 46, 47, 49, 68, 79, 80, 81, 82 and 84; the algebra
agent inspected pages 1, 20, 40, 60 and 90. Its independent image-review
record is `notes/algebra_checkpoint05_visual_QA.md`. No clipping, overlaps,
missing symbols or margin overflow was observed. Page 81 carries the short
final scope paragraph before the bibliography break.

All four compilation commands returned zero. Warnings: 0. Overfull boxes:
0. Boxes above 2pt: 0. Maximum overflow: 0pt. Before/after counts remain
0/0, and no overflow pages required additional inspection. Build time:
{build['seconds']:.9f} seconds. Render time: {record['elapsed_seconds']:.9f}
seconds. All 96 bibliography entries explicitly identify their access
status, with qualifications where only metadata or a later source was read.

The earlier preparation renders were not certified as viewed. An initial
final-tag render occurred before the last build finished; it was replaced
by the post-build render at 03:50:25 UTC before any inspection certification.
Only the final PDF hash above is covered by this record.
''')
output = {'created_utc':stamp,'pdf_pages':90,'pdf_sha256':pdf_hash,
          'root_pages_inspected':root_pages,'algebra_pages_inspected':algebra_pages,
          'bibliography_entries':len(starts),'missing_access_flags':missing,
          'overfull_before':0,'overfull_after':0,
          'elapsed_seconds':time.perf_counter()-start}
target.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
