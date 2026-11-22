"""Record the actual completed build and the root's explicit page inspections."""
from pathlib import Path
import datetime,hashlib,json,re,time
ROOT=Path(__file__).resolve().parents[1]
started=time.perf_counter()
log=(ROOT/'logs/RESEARCH_SA22_paper.log').read_text()
render=json.loads((ROOT/'code/root_render_checkpoint05_output.json').read_text())
extra=json.loads((ROOT/'code/root_render_checkpoint05_extra_output.json').read_text())
pages=sorted(r['page'] for r in render['renders']+extra['renders'])
assert all(r['exit_code']==0 for r in render['renders']+extra['renders'])
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
undefined=len(re.findall(r'Warning:.*(?:Citation|Reference).*undefined|There were undefined references',log))
missing=len(re.findall('Missing character:',log))
assert not over and not undefined and not missing
pdf=ROOT/'RESEARCH_SA22_paper.pdf'
out=dict(checkpoint=5,build_log='logs/build_18.out',final_tex_log='logs/RESEARCH_SA22_paper.log',
         pages=render['pdf_pages'],pdf_bytes=pdf.stat().st_size,sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
         historical_overfull_above_2pt_before=[26.38113,5.72717],
         overfull_boxes_after=len(over),undefined_references_or_citations=undefined,missing_characters=missing,
         rendered_pages=pages,visually_inspected_pages=pages,
         visual_result='All20 selected pages actually opened as rendered images by root, including the new Lehto, Birman and Alling comparison passages/table. No observed overflow, clipping, collisions or unreadable formula/table layout. The sample spans the document and includes prior overflow sections.',
         build_timing_record='code/root_timed_build_18_output.json',
         render_timing_records=['code/root_render_checkpoint05_output.json','code/root_render_checkpoint05_extra_output.json'],
         verification_time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
         preceding_failures={'15':'Wrapper argument repeated code/; failed before TeX, exit127,0.002974177s.',
                             '16':'Raw underscores in new Alling/Birman bibliography provenance paths caused a TeX error; paths corrected using path macro and actual included code/ location.',
                             '17':'Raw underscore in Lehto note path caused a TeX error; fixed it and the raw publisher access-status token. Logs and actual timings retained.'},
         seconds=time.perf_counter()-started)
(ROOT/'logs/typesetting_checkpoint_05.json').write_text(json.dumps(out,indent=2)+'\n')
(ROOT/'code/root_checkpoint05_qa_record_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
