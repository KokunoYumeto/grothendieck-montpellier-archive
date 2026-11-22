"""Record the completed visual and build checks for timed checkpoint07."""
from pathlib import Path
import datetime,hashlib,json
root=Path(__file__).resolve().parents[1]
pdf=root/'RESEARCH_SA14_SA19_paper.pdf'
render=json.loads((root/'code/render_qa_07_output.json').read_text())
build=json.loads((root/'code/paper_build_diagnostics.json').read_text())
digest=hashlib.sha256(pdf.read_bytes()).hexdigest()
assert digest==render['pdf_sha256']=='52067cb188f96ba583a87662c474ec4c83b9fdeb8a1ffed817010f824005637d'
assert build['commands'][-1]['returncode']==0
assert build['overfull_gt_2pt']==build['missing_characters']==build['undefined_citations']==build['undefined_references']==0
qa=dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),pdf_sha256=digest,page_count=159,
 pages_visually_inspected=render['pages_rendered'],
 inspection_method='All seven numerically ordered contact sheets explicitly viewed in small batches. Twenty-five pages include A2Y, E4 pinching, complete F12/F13 proofs and remaining scope, representative earlier parts, register and bibliography.',
 overfull_total_after=build['overfull_total'],overfull_gt_2pt_after=build['overfull_gt_2pt'],maximum_overfull_pt_after=max(build['overfull_sizes_pt']),
 missing_characters=build['missing_characters'],undefined_citations=build['undefined_citations'],undefined_references=build['undefined_references'],
 assessment='Readable formulas, explicit scope and remaining gates, no clipping or unresolved references. The report and paper remain explicitly INCOMPLETE.')
(root/'code/visual_qa_07.json').write_text(json.dumps(qa,indent=2)+'\n')
with (root/'RESEARCH_SA14_SA19_report.md').open('a') as out:
 out.write('\n## Checkpoint07 visual verification\n\nThe 159-page paper passed explicit visual inspection on 25 selected pages across all seven contact sheets. The final build has no missing characters, undefined citations or undefined references, and no overfull box above 2 pt. The exact PDF hash, inspected pages and diagnostics are in code/visual_qa_07.json. This timed checkpoint retains every unresolved research gate.\n')
with (root/'PROGRESS_LEDGER.md').open('a') as out:
 out.write('\n### Checkpoint07 production check — '+qa['time_utc']+'\n\nThe 159-page paper passed explicit visual inspection on 25 selected pages. F13 was proved and audited after formal review03; it is recorded for the next comparison, not retroactively added to review03. Packaging and this inspection are not substantive movement.\n')
print(json.dumps(qa,indent=2))
