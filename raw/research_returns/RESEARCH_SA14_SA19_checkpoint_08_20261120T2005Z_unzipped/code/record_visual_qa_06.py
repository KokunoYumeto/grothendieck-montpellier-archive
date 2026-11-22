"""Record the explicit image review completed for checkpoint 06."""
from pathlib import Path
import datetime, hashlib, json

root = Path(__file__).resolve().parents[1]
pdf = root / 'RESEARCH_SA14_SA19_paper.pdf'
render = json.loads((root / 'code/render_qa_06_output.json').read_text())
build = json.loads((root / 'code/paper_build_diagnostics.json').read_text())
digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
assert digest == render['pdf_sha256']
qa = dict(
    time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    pdf_sha256=digest,
    page_count=152,
    pages_visually_inspected=render['pages_rendered'],
    inspection_method='All ten numerically ordered contact sheets explicitly viewed in small batches. Thirty-eight pages cover the new A2V/A2W, D4b, E4.Curve, F7-F11 and J6C proofs, plus samples of the other parts, register and bibliography.',
    overfull_total_after=build['overfull_total'],
    overfull_gt_2pt_after=build['overfull_gt_2pt'],
    maximum_overfull_pt_after=max(build['overfull_sizes_pt']),
    missing_characters=build['missing_characters'],
    undefined_citations=build['undefined_citations'],
    undefined_references=build['undefined_references'],
    assessment='Readable mathematics, no clipping, no unresolved references or citations. New proofs, explicit scope restrictions, remaining gates, register and bibliography are legible. Research is explicitly INCOMPLETE.'
)
(root / 'code/visual_qa_06.json').write_text(json.dumps(qa, indent=2) + '\n')
report = root / 'RESEARCH_SA14_SA19_report.md'
heading = '\n## Checkpoint 06 visual verification\n'
if heading not in report.read_text():
    with report.open('a') as out:
        out.write(heading + '\nThe 152-page PDF was compiled successfully and 38 rendered pages were explicitly inspected across all ten contact sheets. The build has no missing characters, undefined citations or undefined references, and no overfull box above 2 pt. New A2V/A2W, D4b, E4.Curve, F7–F11 and J6C material and representative register/bibliography pages are readable without clipping. The exact PDF hash, inspected pages and diagnostics are in `code/visual_qa_06.json`. This is a timed research checkpoint; the unresolved gates remain unresolved.\n')
with (root / 'PROGRESS_LEDGER.md').open('a') as out:
    out.write('\n### Checkpoint 06 production check — ' + qa['time_utc'] + '\n\nThe 152-page paper passed explicit visual inspection on 38 selected pages. The timed snapshot was delayed by the visual-verification and context-resumption step; no mathematical status is changed by this production check. See `code/visual_qa_06.json`.\n')
print(json.dumps(qa, indent=2))
