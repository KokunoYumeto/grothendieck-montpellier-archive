"""Record the current build21 review and explicit reuse of identical images."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, time

R = Path(__file__).resolve().parents[1]
started = time.perf_counter()
render = json.loads((R/'code/root_render_build21_output.json').read_text())
old = json.loads((R/'code/root_checkpoint06_qa_record_output.json').read_text())
(R/'logs/typesetting_build20.json').write_text(json.dumps(old,indent=2)+'\n')
comparison = json.loads((R/'code/root_build20_21_image_comparison.json').read_text())
identical = [x['page'] for x in comparison if x['status']=='identical']
direct = [1,20,35,55,68,69,71,79,90,106,123]
assert set(identical) <= set(old['visually_inspected_pages'])
assert set(render['rendered_pages']) == set(identical)|set(direct)
assert all(x['exit_code']==0 for x in render['results'])
pdf = R/'RESEARCH_SA22_paper.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==render['pdf_sha256']
log = (R/'logs/RESEARCH_SA22_paper.log').read_text()
over = [float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
undefined = len(re.findall(r'Warning:.*(?:Citation|Reference).*undefined|There were undefined references',log))
missing = len(re.findall('Missing character:',log))
assert not over and not undefined and not missing
out = dict(checkpoint=6,build=21,build_log='logs/build_21.out',
    final_tex_log='logs/RESEARCH_SA22_paper.log',pages=123,pdf_bytes=pdf.stat().st_size,
    sha256=render['pdf_sha256'],historical_overfull_above_2pt_before=[26.38113,5.72717],
    overfull_boxes_after=0,undefined_references_or_citations=0,missing_characters=0,
    rendered_pages=render['rendered_pages'],visually_inspected_pages=direct,
    byte_identical_to_previously_inspected_build20_pages=identical,
    pages_with_direct_or_identical_image_review=sorted(set(direct)|set(identical)),
    visual_result='Eleven current-build pages were actually displayed and inspected by root, including the changed B1b pages 68,69,71 and a sample across the full paper. All twenty pixel-identical build20 counterparts had been displayed and inspected earlier. No visible clipping, overlap or unreadable formulas/tables; this records 23 distinct rendered pages reviewed by the two explicitly distinguished routes.',
    build_timing_record='code/root_timed_build_21_output.json',
    render_timing_records=['code/root_render_build21_output.json'],
    image_comparison='code/root_build20_21_image_comparison.json',
    verification_time_utc=datetime.now(timezone.utc).isoformat(),
    preceding_failures_preserved_in='logs/typesetting_checkpoint_05.json',
    seconds=time.perf_counter()-started)
for target in ['logs/typesetting_checkpoint_06.json','code/root_checkpoint06_qa21_record_output.json']:
    (R/target).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
