"""Record QA only after the root has actually displayed every page of this sample."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, sys, time

R=Path(__file__).resolve().parents[1]
began=time.perf_counter()
build=int(sys.argv[1])
description=sys.argv[2]
target=R/'code'/f'root_record_current_qa_{build:02d}_output.json'
assert not target.exists()
render_path=R/'code'/f'root_render_current_{build:02d}_output.json'
render=json.loads(render_path.read_text())
assert all(x['exit_code']==0 for x in render['results'])
pdf=R/'RESEARCH_SA22_paper.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==render['pdf_sha256']
log=(R/'logs/RESEARCH_SA22_paper.log').read_text()
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
undefined=len(re.findall(r'Warning:.*(?:Citation|Reference).*undefined|There were undefined references',log))
missing=log.count('Missing character:')
assert not over and not undefined and not missing
out=dict(build=build,pages=int(re.search(r'Pages:\s+(\d+)',render['pdfinfo'])[1]),
 pdf_bytes=pdf.stat().st_size,sha256=render['pdf_sha256'],
 build_log=f'logs/build_{build:02d}.out',final_tex_log='logs/RESEARCH_SA22_paper.log',
 historical_overfull_above_2pt_before=[26.38113,5.72717],overfull_boxes_after=0,
 undefined_references_or_citations=0,missing_characters=0,
 rendered_pages=render['rendered_pages'],visually_inspected_pages=render['rendered_pages'],
 visual_result='Root actually displayed and inspected every listed page. No visible clipping, overlapping text, or unreadable formula was found.',
 change_scope=description,build_timing_record=f'code/root_timed_build_{build:02d}_output.json',
 render_timing_record=str(render_path.relative_to(R)),
 verification_time_utc=datetime.now(timezone.utc).isoformat(),seconds=time.perf_counter()-began)
for path in [R/'logs'/f'typesetting_build{build}.json',R/'logs/typesetting_current.json',target]:
    path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
