"""Finalize only after actual final-image QA and source/register consistency checks."""
from pathlib import Path
import csv,datetime,json,subprocess,sys,io,zipfile,re
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/visual_qa_checkpoint19.json';assert not dest.exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
reviewers=json.loads((w/'notes/qa19_final_actual_reviewers.json').read_text())
assert reviewers['all_explicitly_confirmed'] is True
pending=json.loads((w/'outputs/visual_qa19_final_pending.json').read_text())
groups=reviewers['actually_viewed_pages_by_reviewer']
assert sorted(sum(groups.values(),[]))==pending['pages_rendered']
identical=json.loads((w/'outputs/checkpoint19_identical_QA_pages.json').read_text())
assert identical['status']=='PASS'
build=json.loads((w/'outputs/build_summary.json').read_text())
initial=json.loads((w/'outputs/checkpoint19_initial_build_summary.json').read_text())
assert build['over_2pt']==0 and not build['undefined_references'] and not build['undefined_citations']
assert 'Missing character:' not in (w/'RESEARCH_SA15_paper.log').read_text()
paths=json.loads((w/'outputs/checkpoint19_program_path_verification.json').read_text());assert paths['status']=='PASS'
for name in ['merge_registers.py','source_census.py','export_agent_programs.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_18.zip') as z:
    old={r['id'] for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
current=list(csv.DictReader((w/'RESEARCH_SA15_results.csv').open()))
events=list(csv.DictReader((w/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
checked={r['statement_id'] for r in events};ids={r['id'] for r in current};new=ids-old
assert old<=ids and new<=checked,(old-ids,new-checked)
assert not any('pending' in r['where_proved'] for r in current)
coverage={'status':'PASS','actual_utc':now,'current_statements':len(current),'check_events':len(events),
          'new_identifiers':len(new),'removed_identifiers':0,'all_new_identifiers_have_explicit_event':True}
(w/'outputs/statement_coverage_checkpoint19.json').write_text(json.dumps(coverage,indent=2)+'\n')
qa={'checkpoint':19,'actual_observed_utc':now,'status':'PASS','pdf_pages':pending['pages_in_pdf'],
    'pdf_bytes':build['pdf_bytes'],'final_build_seconds':build['seconds'],
    'initial_build_seconds':initial['seconds'],'build_attempts':2,'failed_builds':0,
    'actually_viewed_pages_by_reviewer':groups,'total_distinct_pages':len(pending['pages_rendered']),
    'unchanged_previously_viewed_images_verified_identical':13,
    'final_overfull_boxes':len(build['overfull_boxes']),
    'max_overfull_points':max((b['points'] for b in build['overfull_boxes']),default=0),
    'over_2pt_before':initial['over_2pt'],'over_2pt_after':0,
    'undefined_references':False,'undefined_citations':False,'missing_glyphs':False,'criteria':reviewers['criteria']}
dest.write_text(json.dumps(qa,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    csv.writer(f,delimiter='\t').writerow(['CP19-VISUAL-QA',now,
      'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root and three independent reviewers','artifact verification',
      f"PASS: {qa['pdf_pages']}-page PDF, {qa['pdf_bytes']} bytes. All {qa['total_distinct_pages']} selected images actually viewed:21 final images freshly opened and13 earlier viewed images verified byte-identical. Two successful builds retained, no failed build; zero boxes above2pt and no undefined reference/citation or missing glyph. No mathematical computation inferred from layout checks."])
bib=len(re.findall(r'^@',(w/'RESEARCH_SA15_references.bib').read_text(),re.M))
census=len(list(csv.DictReader((w/'notes/SOURCE_CENSUS.tsv').open(),delimiter='\t')))
exports=len(json.loads((w/'outputs/exported_programs.json').read_text()))
with (w/'notes/checkpoint19_changes.md').open('a') as f:
    f.write(f'''\n### Final checkpoint verification\n\nThe final paper has{qa['pdf_pages']}pages and{qa['pdf_bytes']}bytes, with{len(current)}numbered statements,{len(new)}new identifiers since checkpoint18 and no removed delivered identifier. Every new identifier has its explicit check event and final statement number. There are{bib}bibliography entries,{census}source-census rows and{exports}exported agent program/output files. All{paths['referenced_program_paths']}literal printed program paths resolve.\n\nBoth actual builds succeeded. The first, before the late degree-three/B54 promotions, took{initial['seconds']}seconds and produced445pages. The final build took{build['seconds']}seconds. Both have zero boxes above2pt; the sole final overfull box is{qa['max_overfull_points']}pt. Neither final references nor citations are undefined, and no glyph is missing. Full input snapshots, logs and summaries of both builds are retained. The initial26-page actual visual review is retained separately. The final selection covers all six new subsections and a spread of earlier material:21final images were freshly opened, and13already viewed images were verified byte-identical to the final rendered images. All34final selected images are covered by actual inspection.\n\nActual review12 remains16:52:24.659633UTC and its no-movement streak is zero; the post-review promotions will be assessed in review13, due17:50:40UTC. This archive is created only at or after17:05:40UTC. Next checkpoint:17:50:40UTC.\n''')
for name in ['merge_registers.py','source_census.py','export_agent_programs.py','update_current19.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with (w/'RESEARCH_SA15_report.md').open('a') as f:f.write('\n'+(w/'notes/SOURCE_CENSUS.md').read_text()+'\n')
with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n## '+now+': checkpoint19 current-gate snapshot\n\nThis is a current-state checkpoint snapshot, not an early hourly review. Actual review12 remains unchanged, including its B53 snapshot-guard omission. The B53 scope-only status was corrected at16:52:45.447033UTC; the mathematical assertions were promoted before review12 and its explicit movement assessment already counted them. The current table reconciles that omission. Degree3 and B54 were promoted after review12 and belong to the next assessment interval. The no-movement streak remains zero.\n\n'+(w/'notes/current_outcome_table.md').read_text()+'\n')
assert (w/'RESEARCH_SA15_report.md').read_text().startswith('INCOMPLETE\n\n| Item |')
print(json.dumps(qa,indent=2))
