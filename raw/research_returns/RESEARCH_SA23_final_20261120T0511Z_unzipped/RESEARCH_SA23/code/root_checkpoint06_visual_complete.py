"""Bind the completed seventeen-page inspection to the sixth-checkpoint PDF."""
from pathlib import Path
import datetime, hashlib, json, re, time
root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
target=root/'logs/root_checkpoint06_visual_complete.json'
if target.exists():
    raise SystemExit('Checkpoint06 visual certification already exists.')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
path=root/'logs/root_pdf_review_checkpoint06.json'
record=json.loads(path.read_text())
sha=hashlib.sha256((root/'RESEARCH_SA23_paper.pdf').read_bytes()).hexdigest()
assert sha==record['pdf_sha256']=='2a01da209cd326f1749883b29a1e00e8f0b5eb404f1cb17405b11881d5a7b906'
root_pages=[45,46,47,48,49,50,68,79,80,81,82,85]
category_pages=[1,20,40,60,91]
assert record['pdf_pages']==91
assert sorted(root_pages+category_pages)==record['pages_rendered']
peer=json.loads((root/'logs/category_checkpoint06_visual_QA_finish.json').read_text())
assert peer['pdf_sha256']==sha and peer['actual_pages_inspected']==category_pages
assert (root/'notes/category_checkpoint06_visual_QA.md').exists()
build=json.loads((root/'logs/build_diagnostics.json').read_text())
assert len(build['commands'])==4 and all(c['returncode']==0 for c in build['commands'])
assert build['warnings']==[] and build['overfull_count']==0
bib=(root/'RESEARCH_SA23_references.bib').read_text()
starts=list(re.finditer(r'(?m)^@\w+\s*\{\s*([^,\s]+)\s*,',bib))
missing=[]
for i,match in enumerate(starts):
    body=bib[match.start():starts[i+1].start() if i+1<len(starts) else len(bib)]
    if 'opened' not in body.casefold(): missing.append(match.group(1))
assert len(starts)==103 and not missing
record.update({'visual_inspection':'All seventeen rendered images individually displayed and directly inspected: twelve by root, five by the category agent.',
               'inspection_completed_utc':stamp,'root_pages_inspected':root_pages,
               'category_pages_inspected':category_pages,
               'inspection_findings':'No clipping, overlap, missing glyph, illegible formula or margin defect observed. The short scope discussion on page81 is followed by the normal bibliography page break.',
               'category_evidence':'notes/category_checkpoint06_visual_QA.md;logs/category_checkpoint06_visual_QA_finish.json'})
path.write_text(json.dumps(record,indent=2)+'\n')
with (root/'verification/visual_QA.md').open('a') as handle:
    handle.write(f'''

### Sixth checkpoint: 1951 notice and later documentary checks

The paper has **91 pages**, SHA256 **{sha}**. Actual inspection completed
{stamp}. Root individually displayed and inspected pages
45, 46, 47, 48, 49, 50, 68, 79, 80, 81, 82 and 85. The category agent
individually displayed and inspected pages 1, 20, 40, 60 and 91, with the
PDF, render-manifest and image hashes checked before and after its review.
Its exact record is `notes/category_checkpoint06_visual_QA.md`.

No clipping, overlap, missing glyph, illegible formula or margin defect
was observed. Page 81 carries the final scope discussion before the
bibliography page break. The changed historical comparison explicitly
includes the original 1951 announcement without identifying it as a proof
or assigning its date to the Montpellier sheets.

All four build commands returned zero. Warnings: 0. Overfull boxes: 0.
Boxes exceeding 2pt: 0. Maximum overflow: 0pt. Before/after counts are
0/0, so no overflow page required additional inspection. Build time:
{build['seconds']:.9f} seconds; rendering time:
{record['elapsed_seconds']:.9f} seconds. All 103 bibliography entries
state their actual access status. This record applies only to the PDF
hash above and does not inherit an inspection from an earlier build.
''')
output={'created_utc':stamp,'pdf_pages':91,'pdf_sha256':sha,
        'root_pages_inspected':root_pages,'category_pages_inspected':category_pages,
        'bibliography_entries':103,'missing_access_flags':missing,
        'overfull_before':0,'overfull_after':0,
        'elapsed_seconds':time.perf_counter()-started}
target.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
