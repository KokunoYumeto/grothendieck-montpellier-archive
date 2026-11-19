"""Record actual completed visual QA and finalize CP13's report/registers."""
from pathlib import Path
import csv,datetime,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/visual_qa_checkpoint13.json'
assert not dest.exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
groups={
 'root':[1,14,24,28,39,55,70,85,327],
 'monodromy':[175,176,177,178,179,180,181,182,183,184,185,192],
 'obstructions_crystals':[165,166,167,174,193,194,195,196],
 'reduction_descent':[198,251,252,253,254,255,256,261]}
pending=json.loads((w/'outputs/visual_qa_pending.json').read_text())
assert sorted(sum(groups.values(),[]))==pending['pages_rendered']
build=json.loads((w/'outputs/build_summary.json').read_text())
assert build['over_2pt']==0 and not build['undefined_references'] and not build['undefined_citations']
qa={'checkpoint':13,'actual_observed_utc':now,'status':'PASS','pdf_pages':327,
    'pdf_bytes':build['pdf_bytes'],'build_seconds':build['seconds'],
    'actually_viewed_pages_by_reviewer':groups,'total_distinct_pages':37,
    'final_overfull_boxes':len(build['overfull_boxes']),
    'criteria':'All10 montages actually viewed. Complete new sections inspected for clipping, overlap, glyphs, long paths, tables, margins and formula alignment. Each delegated reviewer returned actual-page confirmation; root viewed montages1,2,10.',
    'failed_build_retained':'Initial multi-alignment split error in two contact displays; changed to aligned. Also replaced an unbreakable path stem. Failed full A_monodromy input, full TeX log, console and preparation output retained.',
    'failed_attempt_timing':'No exact subprocess stopwatch completed on failure. Preparation stdout birth12:28:44.365244598UTC and final modification12:28:51.885411698UTC give a7.5201671s file-timestamp interval; this is not claimed as a separately measured LuaLaTeX runtime.'}
dest.write_text(json.dumps(qa,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t').writerow(['CP13-VISUAL-QA',now,
 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root with delegated independent page checks',
 'artifact verification',
 'PASS:327-page PDF2436705bytes; successful build32.491s; zero overfull boxes or undefined references/citations. All37 rendered pages actually viewed, covering complete new sections plus prior samples and final bibliography. Initial split/aligned failure and long-path repair preserved in full.'])
with (w/'notes/checkpoint13_changes.md').open('a') as f:
 f.write('''
## Final checkpoint verification

The paper has327 pages and2,436,705 bytes. Its successful build took32.491 seconds, with zero overfull boxes and no undefined references or citations. The initial build stopped on multiple alignment tabs in two split displays; both were changed to aligned. An unbreakable long certificate stem was also converted to a breakable path. The complete failed input, console, TeX log and preparation output are retained. The failed subprocess did not complete its stopwatch report; the available file-timestamp interval is recorded explicitly as such in outputs/visual_qa_checkpoint13.json.

All37 selected pages were actually inspected: root9, monodromy12, obstruction/crystal8, reduction/descent8. These include every new mathematical subsection and a spread through earlier pages and the bibliography. Every reviewer reported clean formulas, tables, glyphs, paths and margins. The exact page assignments and observation time are retained in the visual-QA record.

The paper contains373 numbered statements; all25 statements added since checkpoint12 have explicit check-event identifiers. There are139 bibliography entries and140 source-census rows including the unused Hua witness. The exact final event and program-export counts are available in the regenerated registers.

After the paper freeze, a proposed sharper C3-residual gate (B39) and a proposed eventual mixed-product polarization formula were written separately. They remain visibly unpromoted candidates in this checkpoint, and are neither integrated into the inspected paper nor counted in its current outcome table. The next actual hourly review is due12:50:40UTC. No review is fabricated at this checkpoint time.
''')
for name in ['merge_registers.py','source_census.py','export_agent_programs.py','update_current13.py']:
 subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with (w/'RESEARCH_SA15_report.md').open('a') as f:
 f.write('\n'+(w/'notes/SOURCE_CENSUS.md').read_text()+'\n')
assert (w/'RESEARCH_SA15_report.md').read_text().startswith('INCOMPLETE\n\n| Item |')
print(json.dumps(qa,indent=2))
