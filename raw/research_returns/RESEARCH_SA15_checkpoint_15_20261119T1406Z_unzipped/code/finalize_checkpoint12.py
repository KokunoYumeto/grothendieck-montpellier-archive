"""Finalize CP12 only after the specified pages have actually been viewed."""
from pathlib import Path
import csv,datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
qa_path=w/'outputs/visual_qa_checkpoint12.json'
assert not qa_path.exists(), 'Do not duplicate final checkpoint verification'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
root=[1,14,24,28,39,55,70,85]
mono=[162,163,164,165,166,167,168,169,170,171,172,175]
rd=[176,177,178,181,230,231,232,233,234,238,254,255]
oc=list(range(256,270))+[305]
pending=json.loads((w/'outputs/visual_qa_pending.json').read_text())
assert sorted(root+mono+rd+oc)==pending['pages_rendered']
build=json.loads((w/'outputs/build_summary.json').read_text())
assert build['over_2pt']==0 and not build['undefined_references'] and not build['undefined_citations']
qa=dict(checkpoint=12,observed_utc=now,result='PASS',pdf_pages=305,
 root_actually_viewed_pages=root,monodromy_actually_viewed_pages=mono,
 reduction_descent_actually_viewed_pages=rd,obstruction_crystal_actually_viewed_pages=oc,
 total_distinct_pages=len(set(root+mono+rd+oc)),
 criteria='All12 montages actually viewed separately by assigned agents. No clipping, overlap, broken glyphs or formula/margin failures. Root1–2, monodromy3–5, reduction/descent6–8, obstruction/crystals9–12. The repaired display on page266 was explicitly inspected.',
 initial_overfull_count=1,initial_largest_overflow_points=123.4066,final_overfull_count=len(build['overfull_boxes']))
qa_path.write_text(json.dumps(qa,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t').writerow(['CP12-VISUAL-QA',now,
  'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root with delegated independent page checks',
  'artifact verification',
  'PASS:305-page PDF2289105bytes; final build31.906s; zero overfull boxes and undefined references/citations. All47 rendered pages actually viewed. Initial123.4066pt wide coherent-category display was split and explicitly reinspected on page266. Initial and final build logs retained.'])
note='''
## Final checkpoint verification

The final paper has305 pages and2,289,105 bytes. The reproducible final build passed in31.906 seconds with zero overfull boxes and no unresolved references or citations. The initial build had one123.4066pt overflow in the coherent-category equivalence display. That display was split into two compact arrays, rebuilt, and explicitly inspected on page266. Both build records are retained.

All47 selected pages were actually inspected:8 by the root,12 by monodromy,12 by reduction/descent and15 by obstruction/crystals. The sample covers the complete new sections and a spread through the existing text; the precise page lists and actual observation time are in outputs/visual_qa_checkpoint12.json. No clipping, overlap, broken glyphs or margin failures remained.

The final register contains348 numbered statements, and the source census has140 rows including the explicitly unused Hua witness. The remaining source scans are unavailable as before. Only complete, independently audited mathematics is promoted in the paper.

During the paper freeze, the two additional tangent-triple certificates also passed independent full global reruns:76.3690687260023 and74.86146398200071 seconds for144 collision ideals each, plus source smoothness3.7411868540002615 and3.3895406299998285 seconds and an independent local-series check0.007957189001899678 seconds. Their candidate witness proof and complete outputs are retained separately. A further ordinary arbitrary-embedding proof and a bounded probe of rectangular types(12,3),(24,3),(48,3),(96,3) are also retained as unintegrated work. The latter probe took0.6945195179941948 seconds and is explicitly not an all-valuation theorem. None of this post-freeze work is silently promoted into the already inspected PDF.
'''
with (w/'notes/checkpoint12_changes.md').open('a') as f:f.write(note)
for program in ['merge_registers.py','source_census.py','export_agent_programs.py','update_current12.py']:
 subprocess.run([sys.executable,str(w/'code'/program)],check=True,cwd=w)
with (w/'RESEARCH_SA15_report.md').open('a') as f:
 f.write('\n'+(w/'notes/SOURCE_CENSUS.md').read_text()+'\n')
assert (w/'RESEARCH_SA15_report.md').read_text().startswith('INCOMPLETE\n\n| Item |')
print(json.dumps(qa,indent=2))
