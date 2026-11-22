"""Record checkpoint08 only after explicit inspection of every rendered contact sheet."""
from pathlib import Path
import datetime, hashlib, json, sys
import fitz

root=Path(__file__).resolve().parents[1]
pdf=root/'RESEARCH_SA14_SA19_paper.pdf'
render=json.loads((root/'code/render_qa_08_output.json').read_text())
build=json.loads((root/'code/paper_build_diagnostics.json').read_text())
digest=hashlib.sha256(pdf.read_bytes()).hexdigest()
assert digest==render['pdf_sha256']==sys.argv[1]
assert build['commands'][-1]['returncode']==0
assert build['overfull_gt_2pt']==build['missing_characters']==build['undefined_citations']==build['undefined_references']==0
pages=len(fitz.open(pdf))
qa=dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    pdf_sha256=digest,page_count=pages,pages_visually_inspected=render['pages_rendered'],
    inspection_method='Every numerically ordered contact sheet explicitly viewed in batches of no more than two. Coverage includes the newly integrated Part A and Part F proofs, I7b, representative earlier results, register and bibliography.',
    overfull_total_after=build['overfull_total'],overfull_gt_2pt_after=build['overfull_gt_2pt'],
    maximum_overfull_pt_after=max(build['overfull_sizes_pt'],default=0),
    missing_characters=build['missing_characters'],undefined_citations=build['undefined_citations'],
    undefined_references=build['undefined_references'],
    assessment='Readable formulas and scope qualifications; no clipped content or unresolved references. Unrestricted open parent questions remain marked INCOMPLETE.')
(root/'code/visual_qa_08.json').write_text(json.dumps(qa,indent=2)+'\n')
with (root/'RESEARCH_SA14_SA19_report.md').open('a') as out:
    out.write(f'\n## Checkpoint08 visual verification\n\nThe {pages}-page paper passed explicit visual inspection on {len(render["pages_rendered"])} selected pages, including every newly integrated proof section. No overfull box exceeds2pt, and there are no missing characters, undefined citations or undefined references. The PDF hash and exact inspection record are in code/visual_qa_08.json.\n')
with (root/'PROGRESS_LEDGER.md').open('a') as out:
    out.write('\n### Checkpoint08 production check — '+qa['time_utc']+'\n\nThe rendered new proofs and representative prior sections were explicitly inspected. Packaging and visual QA are not counted as research movement. The formal review is recorded separately.\n')
print(json.dumps(qa,indent=2))
