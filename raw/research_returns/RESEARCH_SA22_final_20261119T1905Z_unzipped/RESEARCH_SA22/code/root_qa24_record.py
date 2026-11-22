"""Run only after every recorded build24 page has actually been viewed."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter()
target=R/'code/root_qa24_record_output.json';assert not target.exists()
render=json.loads((R/'code/root_render_current_24_output.json').read_text())
seen=[1,3,15,16,17,18,64,65,66,67,68,80,99,117,134]
assert render['rendered_pages']==seen
assert all(x['exit_code']==0 for x in render['results'])
pdf=R/'RESEARCH_SA22_paper.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==render['pdf_sha256']
log=(R/'logs/RESEARCH_SA22_paper.log').read_text()
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
undef=len(re.findall(r'Warning:.*(?:Citation|Reference).*undefined|There were undefined references',log))
missing=log.count('Missing character:')
assert not over and not undef and not missing
pages=int(re.search(r'Pages:\s+(\d+)',render['pdfinfo'])[1]);assert pages==134
out=dict(checkpoint=7,build=24,pages=pages,pdf_bytes=pdf.stat().st_size,sha256=render['pdf_sha256'],
 build_log='logs/build_24.out',final_tex_log='logs/RESEARCH_SA22_paper.log',
 historical_overfull_above_2pt_before=[26.38113,5.72717],overfull_boxes_after=0,
 preceding_build23_issue='One new Stacks citation was undefined because the aggregate bibliography predated the new source fragment. Regenerated the aggregate and reran BibTeX plus both LuaLaTeX passes; no source or mathematical change was needed.',
 undefined_references_or_citations=0,missing_characters=0,rendered_pages=seen,visually_inspected_pages=seen,
 visual_result='Root actually displayed and inspected all15 pages, including all pages15-18 of the new cap-jet/plumbing/descent argument and pages64-68 of the mixed-characteristic, Frobenius, wild-cover and node-character supplement, plus a sample over the paper. No visible clipping, overlap or unreadable formulas.',
 build_timing_record='code/root_timed_build_24_output.json',render_timing_record='code/root_render_current_24_output.json',
 verification_time_utc=datetime.now(timezone.utc).isoformat(),seconds=time.perf_counter()-start)
for name in ['logs/typesetting_checkpoint_07.json','logs/typesetting_build24.json','logs/typesetting_current.json','code/root_qa24_record_output.json']:
 (R/name).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
