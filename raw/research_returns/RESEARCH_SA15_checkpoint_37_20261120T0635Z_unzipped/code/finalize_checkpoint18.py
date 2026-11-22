"""Finalize CP18 only after actual individual visual reviews and clean log checks."""
from pathlib import Path
import csv,datetime,json,subprocess,sys,io,zipfile,re
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/visual_qa_checkpoint18.json';assert not dest.exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
reviewers=json.loads((w/'notes/qa18_actual_reviewers.json').read_text())
groups=reviewers['actually_viewed_pages_by_reviewer']
assert reviewers['all_explicitly_confirmed'] is True
pending=json.loads((w/'outputs/visual_qa18_pending.json').read_text())
assert sorted(sum(groups.values(),[]))==pending['pages_rendered']
build=json.loads((w/'outputs/build_summary.json').read_text())
initial=json.loads((w/'outputs/checkpoint18_initial_build_summary.json').read_text())
failed=json.loads((w/'outputs/failed_checkpoint18_build/outputs__build_failure.json').read_text())
assert build['over_2pt']==0 and not build['undefined_references'] and not build['undefined_citations']
assert 'Missing character:' not in (w/'RESEARCH_SA15_paper.log').read_text()
paths=json.loads((w/'outputs/checkpoint18_program_path_verification.json').read_text())
assert paths['status']=='PASS'
for name in ['merge_registers.py','source_census.py','export_agent_programs.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_17.zip') as z:
    old={r['id'] for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
current=list(csv.DictReader((w/'RESEARCH_SA15_results.csv').open()))
events=list(csv.DictReader((w/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
checked={r['statement_id'] for r in events};current_ids={r['id'] for r in current}
new=current_ids-old
assert old<=current_ids,'A previously delivered statement identifier disappeared.'
assert new<=checked,sorted(new-checked)
assert not any('pending' in r['where_proved'] for r in current)
coverage={'status':'PASS','actual_utc':now,'current_statements':len(current),
          'check_events':len(events),'new_identifiers':len(new),
          'removed_identifiers':0,'all_new_identifiers_have_explicit_event':True}
(w/'outputs/statement_coverage_checkpoint18.json').write_text(json.dumps(coverage,indent=2)+'\n')
qa={'checkpoint':18,'actual_observed_utc':now,'status':'PASS',
    'pdf_pages':pending['pages_in_pdf'],'pdf_bytes':build['pdf_bytes'],
    'final_build_seconds':build['seconds'],'first_successful_build_seconds':initial['seconds'],
    'failed_first_build_seconds':failed['seconds'],
    'actually_viewed_pages_by_reviewer':groups,'total_distinct_pages':len(pending['pages_rendered']),
    'first_successful_overfull_boxes':len(initial['overfull_boxes']),
    'final_overfull_boxes':len(build['overfull_boxes']),
    'max_overfull_points':max((b['points'] for b in build['overfull_boxes']),default=0),
    'over_2pt_before':initial['over_2pt'],'over_2pt_after':0,
    'build_attempts':3,'criteria':reviewers['criteria'],
    'root_actually_viewed_original_overflow_pages':[243,245],
    'undefined_references':False,'undefined_citations':False,'missing_glyphs':False}
dest.write_text(json.dumps(qa,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    csv.writer(f,delimiter='\t').writerow(['CP18-VISUAL-QA',now,
      'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root with delegated independent page checks',
      'artifact verification',
      f"PASS: {qa['pdf_pages']}-page PDF, {qa['pdf_bytes']} bytes; all {qa['total_distinct_pages']} selected pages actually viewed individually. Successful build {build['seconds']}s, zero boxes above2pt, no undefined references/citations or missing glyphs. The failed first build and missing B-RD51.2 delimiter were retained and repaired; no mathematical change."])
bib_count=len(re.findall(r'^@', (w/'RESEARCH_SA15_references.bib').read_text(),re.M))
census_count=len(list(csv.DictReader((w/'notes/SOURCE_CENSUS.tsv').open(),delimiter='\t')))
export_count=len(json.loads((w/'outputs/exported_programs.json').read_text()))
with (w/'notes/checkpoint18_changes.md').open('a') as f:
    f.write(f'''\n### Final checkpoint verification\n\nThe complete paper has {qa['pdf_pages']} pages and {qa['pdf_bytes']} bytes. All {qa['total_distinct_pages']} selected pages were actually viewed individually by the root and three independent reviewers. The selection covers all five new subsections, a spread of earlier pages, and the final bibliography.\n\nThe first build failed after {failed['seconds']} seconds because the second B51 display lacked its closing delimiter. Its source, full console, log and failure metadata are retained in outputs/failed_checkpoint18_build. The missing delimiter after B-RD51.2 was inserted without altering the mathematics. The earlier repaired delimiter was after B-RD51.1; these were two distinct omissions. The first successful build took {initial['seconds']} seconds and had two boxes above2pt, a40.82396pt long bold status and a7.21278pt exact-sequence display. Root actually viewed their original pages243 and245, retained in outputs/checkpoint18_overflow_evidence. The audit explanation was moved into ordinary prose and the display split into two lines, without mathematical change. The final build took {build['seconds']} seconds and contains {len(build['overfull_boxes'])} overfull box, maximum {qa['max_overfull_points']}pt, zero above2pt, and no undefined references, citations or missing glyphs. The before/after counts above2pt on successful builds are {initial['over_2pt']} and0. The initial failed build produced no publishable PDF and has no successful-build overflow count.\n\nThere are {len(current)} numbered statements, {len(new)} new identifiers since checkpoint17, and no removed delivered identifier. Every new statement has an explicit check event and its final statement number. There are {bib_count} bibliography records, {census_count} source census rows and {export_count} exported agent program/output files. All {paths['referenced_program_paths']} literal printed program paths resolve. Four older texttt references missed by the earlier path-only audit received exact byte-identical aliases; the initial failed path check and repair mapping are retained, and no mathematical program was rerun for this repair. The trace-radical candidate passed the complete root and monodromy audits and was promoted before the successful build. Its earlier candidate version remains as explicit provenance.\n\nThe higher-degree mixed strip argument and B52 potential-CM refinement remain separate candidates outside the proved outcome table. No candidate is silently counted as an established theorem. Actual review11 remains the last scheduled review, at15:51:59.733641UTC, with no-movement streak zero. The archive is created only at or after16:20:40UTC. Next checkpoint:17:05:40UTC. Next actual review:16:50:40UTC.\n''')
for name in ['merge_registers.py','source_census.py','export_agent_programs.py','update_current18.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with (w/'RESEARCH_SA15_report.md').open('a') as f:
    f.write('\n'+(w/'notes/SOURCE_CENSUS.md').read_text()+'\n')
with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n## '+now+': checkpoint18 current-gate snapshot\n\nThis is a current-state checkpoint snapshot, not an early hourly review. Actual review11 remains the last scheduled review; review12 is due16:50:40UTC. Its no-movement streak remains zero.\n\n'+(w/'notes/current_outcome_table.md').read_text()+'\n')
assert (w/'RESEARCH_SA15_report.md').read_text().startswith('INCOMPLETE\n\n| Item |')
print(json.dumps(qa,indent=2))
