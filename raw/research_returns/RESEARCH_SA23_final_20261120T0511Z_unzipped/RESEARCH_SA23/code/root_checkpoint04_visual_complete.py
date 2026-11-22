"""Record the actual page-image inspection; no inspection is inferred from rendering."""
from pathlib import Path
import datetime, hashlib, json, time

root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
review = json.loads((root / 'logs/root_pdf_review_checkpoint04.json').read_text())
pdf_hash = hashlib.sha256((root / 'RESEARCH_SA23_paper.pdf').read_bytes()).hexdigest()
assert pdf_hash == review['pdf_sha256']
pages = [1, 20, 40, 45, 46, 47, 60, 67, 78, 79, 86]
assert review['pages_rendered'] == pages
build = json.loads((root / 'logs/build_diagnostics.json').read_text())
assert all(command['returncode'] == 0 for command in build['commands'])
assert build['overfull_count'] == 0 and build['overfull_gt_2pt'] == 0
assert build['warnings'] == []
review.update({
    'visual_inspection': 'Completed by root: each of the eleven images was displayed separately and actually inspected.',
    'inspection_completed_utc': stamp,
    'inspection_findings': 'No clipping, overlapping text, missing symbols or page-margin overflow observed in the inspected pages.',
})
(root / 'logs/root_pdf_review_checkpoint04.json').write_text(json.dumps(review, indent=2) + '\n')
qa = root / 'verification/visual_QA.md'
marker = '## Fourth scheduled checkpoint'
if marker not in qa.read_text():
    with qa.open('a') as handle:
        handle.write(f'''

{marker}

Inspection completed {stamp}. We directly displayed and inspected pages
1, 20, 40, 45, 46, 47, 60, 67, 78, 79 and 86 of the 86-page PDF. The
sample includes the new 1956 reconstruction, the expanded stack descent
argument, the remaining documentary gate and the final bibliography.
No clipping, overlaps, missing symbols or margin overflow was observed.
PDF SHA256: {pdf_hash}.

The first preparation attempt stopped on an unescaped underscore in a
bibliography note, before producing a usable new PDF. The exact failed
logs are retained. We changed the plain-text metadata to k(n)=1 and ran
LuaLaTeX/BibTeX/LuaLaTeX/LuaLaTeX again; all four commands returned zero.
The successful build has zero warnings and zero overfull boxes, including
zero above 2pt, with maximum overflow 0pt. Overfull counts before/after
were 0/0. There were no overflow pages requiring a further separate sample.
The successful build took {build['seconds']:.9f} seconds; rendering took
{review['elapsed_seconds']:.9f} seconds. The earlier truncated image batch
was not counted as visual inspection: all eleven pages were subsequently
displayed one at a time and read.
''')
record = {'created_utc': stamp, 'pdf_sha256': pdf_hash, 'pages_inspected': pages,
          'before_overfull_count': 0, 'after_overfull_count': 0,
          'elapsed_seconds': time.perf_counter() - started}
(root / 'logs/root_checkpoint04_visual_complete.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
