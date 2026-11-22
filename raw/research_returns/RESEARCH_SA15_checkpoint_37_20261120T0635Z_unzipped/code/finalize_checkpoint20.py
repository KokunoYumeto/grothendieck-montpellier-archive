"""Finalize CP20 only after actual image QA and source/register checks."""
from pathlib import Path
import csv,datetime,json,subprocess,sys,io,zipfile,re
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/visual_qa_checkpoint20.json';assert not dest.exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
reviewers=json.loads((w/'notes/qa20_actual_reviewers.json').read_text())
assert reviewers['all_explicitly_confirmed'] is True
pending=json.loads((w/'outputs/visual_qa20_final_pending.json').read_text())
groups=reviewers['actually_viewed_pages_by_reviewer']
assert sorted(sum(groups.values(),[]))==pending['pages_rendered']
comparison=json.loads((w/'outputs/checkpoint20_QA_image_comparison.json').read_text())
assert sorted(sum(reviewers['fresh_final_images'].values(),[]))==sorted(x['page'] for x in comparison['changed'])
assert sorted(sum(reviewers['previously_viewed_images_verified_byte_identical'].values(),[]))==sorted(x['page'] for x in comparison['same'])
build=json.loads((w/'outputs/build_summary.json').read_text())
assert build['over_2pt']==0 and not build['undefined_references'] and not build['undefined_citations']
assert 'Missing character:' not in (w/'RESEARCH_SA15_paper.log').read_text()
paths=json.loads((w/'outputs/checkpoint20_program_path_verification.json').read_text());assert paths['status']=='PASS'
for name in ['merge_registers.py','source_census.py','export_agent_programs.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_19.zip') as z:
    old={r['id'] for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
current=list(csv.DictReader((w/'RESEARCH_SA15_results.csv').open()))
events=list(csv.DictReader((w/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
checked={r['statement_id'] for r in events};ids={r['id'] for r in current};new=ids-old
assert old<=ids and new<=checked,(old-ids,new-checked)
assert not any('pending' in r['where_proved'] for r in current)
coverage={'status':'PASS','actual_utc':now,'current_statements':len(current),'check_events':len(events),
          'new_identifiers':len(new),'removed_identifiers':0,'all_new_identifiers_have_explicit_event':True}
(w/'outputs/statement_coverage_checkpoint20.json').write_text(json.dumps(coverage,indent=2)+'\n')
attempts=sorted((w/'outputs').glob('checkpoint20_integration_attempt*.json'))
attemptdata=[json.loads(p.read_text()) for p in attempts]
qa={'checkpoint':20,'actual_observed_utc':now,'status':'PASS','pdf_pages':pending['pages_in_pdf'],
    'pdf_bytes':build['pdf_bytes'],'final_build_seconds':build['seconds'],
    'actual_build_attempts':len(attemptdata),'failed_builds':sum(r['build_exit_code']!=0 for r in attemptdata),
    'preflight_failures_before_build':1,
    'actually_viewed_pages_by_reviewer':groups,'total_distinct_pages':len(pending['pages_rendered']),
    'fresh_final_images':reviewers['fresh_final_images'],
    'previously_viewed_images_verified_byte_identical':reviewers['previously_viewed_images_verified_byte_identical'],
    'all_selected_images_have_actual_inspection':True,
    'final_overfull_boxes':len(build['overfull_boxes']),
    'max_overfull_points':max((b['points'] for b in build['overfull_boxes']),default=0),
    'over_2pt_after':0,'undefined_references':False,'undefined_citations':False,'missing_glyphs':False,
    'criteria':reviewers['criteria']}
dest.write_text(json.dumps(qa,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    csv.writer(f,delimiter='\t').writerow(['CP20-VISUAL-QA',now,
      'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root and three independent reviewers','artifact verification',
      f"PASS: {qa['pdf_pages']}-page PDF, {qa['pdf_bytes']} bytes. All {qa['total_distinct_pages']} selected images have actual inspection: the corrected final bibliography page was freshly opened, and26other actually inspected images are byte-identical to the final rendering. Actual build attempts{qa['actual_build_attempts']}, failed builds{qa['failed_builds']}; one separate preflight missing-canonical-file failure occurred before integration or compilation and is retained. Zero boxes above2pt and no undefined reference/citation or missing glyph. No mathematical computation inferred from layout checks."])
bib=len(re.findall(r'^@',(w/'RESEARCH_SA15_references.bib').read_text(),re.M))
census=len(list(csv.DictReader((w/'notes/SOURCE_CENSUS.tsv').open(),delimiter='\t')))
exports=len(json.loads((w/'outputs/exported_programs.json').read_text()))
with (w/'notes/checkpoint20_changes.md').open('a') as f:
    f.write(f'''\n### Final checkpoint verification\n\nThe paper has {qa['pdf_pages']} pages and {qa['pdf_bytes']} bytes, with {len(current)} numbered statements, {len(new)} new identifiers since checkpoint19 and no removed delivered identifier. Every new identifier has an explicit check event and a final statement number. There are {bib} bibliography entries, {census} source-census rows and {exports} exported agent program/output files. All {paths['referenced_program_paths']} literal printed program paths resolve.\n\nThe final build took {build['seconds']} seconds. There were {qa['actual_build_attempts']} actual build attempts and {qa['failed_builds']} failed builds. One earlier preflight failed because the already-audited theta canonical file had not yet been created; it ran no integration or mathematical computation and its exact failure is retained separately. Complete build inputs, logs and summaries are preserved. There are zero overfull boxes above 2pt; the maximum is {qa['max_overfull_points']}pt. References, citations and glyphs pass their checks. All {qa['total_distinct_pages']} selected final page images are covered by actual visual inspection: the corrected final bibliography image was freshly opened, and26other actually inspected images were verified byte-identical to the final render. All four new subsections and a spread of earlier material are covered. The initial bibliography-note spacing defect and its repair are recorded; no fresh reinspection of unchanged pages is claimed.\n\nThe archive is created only at or after 17:50:40 UTC, after actual hourly review13. The next checkpoint is due 18:35:40 UTC and the next review 18:50:40 UTC. The archive contains the actual review13 ledger entry; no preparatory assessment is represented as an already-performed review.\n''')
for name in ['merge_registers.py','source_census.py','export_agent_programs.py','update_current20.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with (w/'RESEARCH_SA15_report.md').open('a') as f:f.write('\n'+(w/'notes/SOURCE_CENSUS.md').read_text()+'\n')
with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n## '+now+': checkpoint20 current-gate snapshot\n\nThis is a current-state snapshot, not an early hourly review. Actual review12 is unchanged; the three promoted strict reductions will be assessed in actual review13 at or after17:50:40UTC. The theta geometry refinement and finite pencil diagnostics are not separately counted as movement.\n\n'+(w/'notes/current_outcome_table.md').read_text()+'\n')
assert (w/'RESEARCH_SA15_report.md').read_text().startswith('INCOMPLETE\n\n| Item |')
print(json.dumps(qa,indent=2))
