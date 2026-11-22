"""Record build20 and the 21 pages actually inspected by root after rendering."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, time

R = Path(__file__).resolve().parents[1]
started = time.perf_counter()
render = json.loads((R / 'code/root_render_build20_output.json').read_text())
log = (R / 'logs/RESEARCH_SA22_paper.log').read_text()
pdf = R / 'RESEARCH_SA22_paper.pdf'
pages = [1, 4, 19, 20, 30, 35, 55, 60, 65, 66, 71, 76, 77, 79, 80, 81, 90, 106, 107, 116, 123]
assert render['rendered_pages'] == pages
assert all(x['exit_code'] == 0 for x in render['results'])
assert hashlib.sha256(pdf.read_bytes()).hexdigest() == render['pdf_sha256']
over = [float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt', log)]
undefined = len(re.findall(r'Warning:.*(?:Citation|Reference).*undefined|There were undefined references', log))
missing = len(re.findall('Missing character:', log))
assert not over and not undefined and not missing
out = dict(
    checkpoint=6, build_log='logs/build_20.out', final_tex_log='logs/RESEARCH_SA22_paper.log',
    pages=123, pdf_bytes=pdf.stat().st_size, sha256=render['pdf_sha256'],
    historical_overfull_above_2pt_before=[26.38113, 5.72717],
    overfull_boxes_after=len(over), undefined_references_or_citations=undefined, missing_characters=missing,
    rendered_pages=pages, visually_inspected_pages=pages,
    visual_result=('All 21 pages actually displayed and inspected by root after the earlier truncated tool response. '
                   'They include the new regularity proof, original Gabber comparison, Raynaud flatness proof and Picard application, '
                   'literal group-system clarification, and bibliography. No visible clipping, overlap, or unreadable table/formula layout. '
                   'The sample spans the paper and includes earlier overflow sections.'),
    build_timing_record='code/root_timed_build_20_output.json',
    render_timing_records=['code/root_render_build20_output.json'],
    verification_time_utc=datetime.now(timezone.utc).isoformat(),
    preceding_failures_preserved_in='logs/typesetting_checkpoint_05.json',
    seconds=time.perf_counter()-started)
for target in ['logs/typesetting_checkpoint_06.json', 'code/root_checkpoint06_qa_record_output.json']:
    (R / target).write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
