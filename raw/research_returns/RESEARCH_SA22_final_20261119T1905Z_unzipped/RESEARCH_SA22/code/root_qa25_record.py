"""Record build25 QA after actual root inspection of all fifteen rendered pages."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, time

R = Path(__file__).resolve().parents[1]
start = time.perf_counter()
target = R/'code/root_qa25_record_output.json'
assert not target.exists()
render = json.loads((R/'code/root_render_current_25_output.json').read_text())
seen = [1,3,16,18,30,45,64,68,69,70,82,101,114,129,136]
assert render['rendered_pages'] == seen
assert all(x['exit_code'] == 0 for x in render['results'])
pdf = R/'RESEARCH_SA22_paper.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest() == render['pdf_sha256']
log = (R/'logs/RESEARCH_SA22_paper.log').read_text()
over = [float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
undef = len(re.findall(r'Warning:.*(?:Citation|Reference).*undefined|There were undefined references',log))
missing = log.count('Missing character:')
assert not over and not undef and not missing
pages = int(re.search(r'Pages:\s+(\d+)',render['pdfinfo'])[1])
assert pages == 136
out = dict(build=25,pages=pages,pdf_bytes=pdf.stat().st_size,sha256=render['pdf_sha256'],
 build_log='logs/build_25.out',final_tex_log='logs/RESEARCH_SA22_paper.log',
 historical_overfull_above_2pt_before=[26.38113,5.72717],overfull_boxes_after=0,
 undefined_references_or_citations=0,missing_characters=0,
 rendered_pages=seen,visually_inspected_pages=seen,
 visual_result='Root actually displayed and inspected all15 pages, including every page68-70 of the added intrinsic tame category and a sample spread over Parts A/B/C and the bibliography. No visible clipping, overlapping text, or unreadable formula was found.',
 change_scope='Added Proposition6.20 and its complete proof; cleaned two bibliography source-note locators. All theorem labels and references resolved.',
 build_timing_record='code/root_timed_build_25_output.json',
 render_timing_record='code/root_render_current_25_output.json',
 verification_time_utc=datetime.now(timezone.utc).isoformat(),
 seconds=time.perf_counter()-start)
for name in ['logs/typesetting_build25.json','logs/typesetting_current.json','code/root_qa25_record_output.json']:
    (R/name).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
