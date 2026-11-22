"""Finalize only after all selected final PDF pages were actually inspected."""
from pathlib import Path
import csv,datetime,json,subprocess,sys,io,zipfile,re
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/visual_qa_checkpoint17.json';assert not dest.exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
reviewers=json.loads((w/'notes/qa17_actual_reviewers.json').read_text())
groups=reviewers['actually_viewed_pages_by_reviewer']
assert reviewers['all_explicitly_confirmed'] is True
pending=json.loads((w/'outputs/visual_qa_pending.json').read_text())
assert sorted(sum(groups.values(),[]))==pending['pages_rendered']
build=json.loads((w/'outputs/build_summary.json').read_text())
initial=json.loads((w/'outputs/checkpoint17_initial_build_summary.json').read_text())
assert build['over_2pt']==0 and not build['undefined_references'] and not build['undefined_citations']
assert 'Missing character:' not in (w/'RESEARCH_SA15_paper.log').read_text()
paths=json.loads((w/'outputs/checkpoint17_program_path_verification.json').read_text())
assert paths['status']=='PASS'
for name in ['merge_registers.py','source_census.py','export_agent_programs.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_16.zip') as z:
    old={r['id'] for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
current=list(csv.DictReader((w/'RESEARCH_SA15_results.csv').open()))
events=list(csv.DictReader((w/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
checked={r['statement_id'] for r in events};current_ids={r['id'] for r in current}
new=current_ids-old
assert old<=current_ids,'No previously delivered statement identifier may disappear silently.'
assert new<=checked,sorted(new-checked)
assert not any('pending' in r['where_proved'] for r in current)
coverage={'status':'PASS','actual_utc':now,'current_statements':len(current),
          'check_events':len(events),'new_identifiers':len(new),
          'removed_identifiers':0,'all_new_identifiers_have_explicit_event':True}
(w/'outputs/statement_coverage_checkpoint17.json').write_text(json.dumps(coverage,indent=2)+'\n')
qa={'checkpoint':17,'actual_observed_utc':now,'status':'PASS',
    'pdf_pages':pending['pages_in_pdf'],'pdf_bytes':build['pdf_bytes'],
    'final_build_seconds':build['seconds'],'initial_build_seconds':initial['seconds'],
    'actually_viewed_pages_by_reviewer':groups,'total_distinct_pages':len(pending['pages_rendered']),
    'initial_overfull_boxes':len(initial['overfull_boxes']),
    'final_overfull_boxes':len(build['overfull_boxes']),
    'max_overfull_points':max((b['points'] for b in build['overfull_boxes']),default=0),
    'over_2pt_before':initial['over_2pt'],'over_2pt_after':0,
    'build_attempts':2,'criteria':reviewers['criteria'],
    'undefined_references':False,'undefined_citations':False,'missing_glyphs':False,
    'root_actually_viewed_original_overflow_page':342}
dest.write_text(json.dumps(qa,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    csv.writer(f,delimiter='\t').writerow(['CP17-VISUAL-QA',now,
      'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root with delegated independent page checks',
      'artifact verification',
      f"PASS: {qa['pdf_pages']}-page PDF, {qa['pdf_bytes']}bytes; all{qa['total_distinct_pages']} selected pages actually viewed. Final build{build['seconds']}s, zero boxes above2pt, no undefined references/citations or missing glyphs. The actual initial7.63602pt coefficient display on page342 was viewed and retained, then split without mathematical change. All41 literal code paths now resolve through exact unambiguous aliases where necessary."])
bib_count=len(re.findall(r'^@', (w/'RESEARCH_SA15_references.bib').read_text(),re.M))
census_count=len(list(csv.DictReader((w/'notes/SOURCE_CENSUS.tsv').open(),delimiter='\t')))
export_count=len(json.loads((w/'outputs/exported_programs.json').read_text()))
with (w/'notes/checkpoint17_changes.md').open('a') as f:
    f.write(f'''\n### Final checkpoint verification\n\nThe final complete paper has{qa['pdf_pages']} pages and{qa['pdf_bytes']} bytes. All{qa['total_distinct_pages']} selected pages were actually viewed individually by the root and the three independent reviewers. The selection covers every new subsection, earlier samples, the repaired display and the final bibliography. Root also actually viewed the original page342 overflow, retained as outputs/checkpoint17_overflow_evidence/page_342.png because this report discusses the problem.\n\nThe initial successful build took{initial['seconds']} seconds and had one box above2pt, the7.63602pt B49 coefficient display, plus the existing0.41342pt line. Splitting the display into two gathered lines repaired it without changing the formula. The final build took{build['seconds']} seconds and has{len(build['overfull_boxes'])} overfull box, maximum{qa['max_overfull_points']}pt, zero above2pt, and no undefined references, citations or missing glyphs. Before/after counts above2pt are1 and0. Both actual build summaries and consoles, the original B49 source before the layout repair, and the repair record are retained.\n\nThere are{len(current)} numbered statements, exactly{len(new)} new identifiers since checkpoint16, with no removed delivered identifier. Every new statement has an explicit check event and its final statement number. The provisional automatically named B49 scope remark was assigned stable label rem:B-RD49-scope and its literal code path corrected before delivery; its complete scope, counts and actual runtimes were checked. No claim or passage was silently discarded.\n\nThere are{bib_count} bibliography records and{census_count} source census rows. The merged register includes the monodromy agent's separate post-CP16 event file as well as all ordinary registers and root events. The export inventory contains{export_count} literal agent program/output copies. All{paths['referenced_program_paths']} code paths printed in the paper now resolve: {len(paths['literal_aliases_added'])} missing legacy references received byte-identical, unambiguous aliases, with no program rerun or mathematical edit. Their mapping is retained in outputs/checkpoint17_program_path_verification.json.\n\nThe new B50 tame boundary candidate and higher-degree mixed-product and positive-index determinant investigations remain separately labelled research, outside the inspected paper and proved outcome table. The archive is created only at or after15:35:40UTC. Next checkpoint:16:20:40UTC. Next actual hourly review:15:50:40UTC.\n''')
for name in ['merge_registers.py','source_census.py','export_agent_programs.py','update_current17.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with (w/'RESEARCH_SA15_report.md').open('a') as f:
    f.write('\n'+(w/'notes/SOURCE_CENSUS.md').read_text()+'\n')
with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n## '+now+': checkpoint17 current-gate snapshot\n\nThis is a current-state checkpoint snapshot, not an early hourly review. Actual review10 remains the last scheduled review; review11 is due15:50:40UTC. Its no-movement streak is unchanged.\n\n'+(w/'notes/current_outcome_table.md').read_text()+'\n')
assert (w/'RESEARCH_SA15_report.md').read_text().startswith('INCOMPLETE\n\n| Item |')
print(json.dumps(qa,indent=2))
