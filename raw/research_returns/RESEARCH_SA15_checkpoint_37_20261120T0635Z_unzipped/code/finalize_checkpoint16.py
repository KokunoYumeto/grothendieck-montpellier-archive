"""Finalize CP16 only after all assigned pages have actually been inspected."""
from pathlib import Path
import csv,datetime,json,subprocess,sys,io,zipfile,re
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/visual_qa_checkpoint16.json';assert not dest.exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
reviewers=json.loads((w/'notes/qa16_actual_reviewers.json').read_text())
groups=reviewers['actually_viewed_pages_by_reviewer']
assert reviewers['all_explicitly_confirmed'] is True
pending=json.loads((w/'outputs/visual_qa_pending.json').read_text())
assert sorted(sum(groups.values(),[]))==pending['pages_rendered']
build=json.loads((w/'outputs/build_summary.json').read_text())
initial=json.loads((w/'outputs/checkpoint16_initial_build_summary.json').read_text())
failure=json.loads((w/'outputs/failed_checkpoint16_build/build_failure.json').read_text())
assert build['over_2pt']==0 and not build['undefined_references'] and not build['undefined_citations']
assert 'Missing character:' not in (w/'RESEARCH_SA15_paper.log').read_text()
identity=json.loads((w/'outputs/statement_identity_checkpoint16.json').read_text())
for name in ['merge_registers.py','source_census.py','export_agent_programs.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_15.zip') as z:
    old={r['id'] for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
current=list(csv.DictReader((w/'RESEARCH_SA15_results.csv').open()))
events=list(csv.DictReader((w/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
checked={r['statement_id'] for r in events}
new={r['id'] for r in current}-old
assert new<=checked,sorted(new-checked)
assert not any('pending' in r['where_proved'] for r in current)
coverage={'status':'PASS','actual_utc':now,'current_statements':len(current),
          'check_events':len(events),'new_identifiers':len(new),
          'all_new_identifiers_have_explicit_event':True}
(w/'outputs/statement_coverage_checkpoint16.json').write_text(json.dumps(coverage,indent=2)+'\n')
qa={'checkpoint':16,'actual_observed_utc':now,'status':'PASS',
    'pdf_pages':pending['pages_in_pdf'],'pdf_bytes':build['pdf_bytes'],
    'final_build_seconds':build['seconds'],'first_successful_build_seconds':initial['seconds'],
    'first_failed_build_seconds':failure['seconds'],
    'actually_viewed_pages_by_reviewer':groups,'total_distinct_pages':len(pending['pages_rendered']),
    'initial_successful_overfull_boxes':len(initial['overfull_boxes']),
    'final_overfull_boxes':len(build['overfull_boxes']),
    'max_overfull_points':max((b['points'] for b in build['overfull_boxes']),default=0),
    'over_2pt_before':initial['over_2pt'],'over_2pt_after':0,
    'build_attempts':3,'criteria':reviewers['criteria'],
    'undefined_references':False,'undefined_citations':False,'missing_glyphs':False}
dest.write_text(json.dumps(qa,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    csv.writer(f,delimiter='\t').writerow(['CP16-VISUAL-QA',now,
      'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root with delegated independent page checks',
      'artifact verification',
      f"PASS: {qa['pdf_pages']}-page PDF, {qa['pdf_bytes']}bytes; all{qa['total_distinct_pages']} selected pages actually viewed. Final build{build['seconds']}s, zero boxes above2pt, no undefined references/citations or missing glyphs. Failed alignment build and both subsequent overflow examples retained, then repaired without mathematical change."])
with (w/'notes/checkpoint16_changes.md').open('a') as f:
    f.write(f'''\n## Final checkpoint verification\n\nThe complete paper contains{qa['pdf_pages']} pages and{qa['pdf_bytes']} bytes. All{qa['total_distinct_pages']} selected pages were actually viewed by the root and three independent reviewers. The selection covers every new subsection, earlier samples, the repaired overflow locations and the final bibliography. The two original overflow pages were also actually viewed by the root and are retained as the specifically discussed problem images.\n\nThere were three build attempts. The first stopped on an extra alignment tab in the two-pencil display after{failure['seconds']} seconds; its full merged source, source fragment, log, console and actual runtime are retained. The first successful build took{initial['seconds']} seconds and had two boxes above2pt (55.7315pt and24.32054pt), plus one0.41342pt line. Separating the residue matrix from its three entry definitions and shortening the B44 runtime lead-in repaired both large overflows without changing the mathematics. The final successful build took{build['seconds']} seconds and has{len(build['overfull_boxes'])} overfull boxes, maximum{qa['max_overfull_points']}pt, zero above2pt, and no undefined references, citations or missing glyphs. The before/after counts above2pt are2 and0.\n\nThere are{len(current)} numbered statements, a net addition of{len(current)-len(old)} since checkpoint15. The{len(new)} new identifiers include three existing scope remarks whose content-derived labels changed when the newly proved even-degree consequence replaced the earlier open gate. Root read all three complete old/current pairs; the explicit injective map is in outputs/statement_identity_checkpoint16.json. The first inventory identified three new scope remarks without explicit identifier events; their full passages were then actually checked and all three events recorded. Final coverage confirms every new identifier has an explicit event and every statement has its final number.\n\nThe current bibliography has146 entries and the source census147 rows, including the unused Hua witness. The final merged registers and program-export inventory supply their exact counts. Further generic nonordinary-ppav, fixed-modulus mixed-product, positive-index first-image and next-prime inertia investigations are separate post-checkpoint candidates, excluded from the inspected paper and proved outcome table.\n\nThe actual review10 is recorded at or after14:50:40UTC; the archive is created only after that review and the scheduled checkpoint time. The next checkpoint is due15:35:40UTC and next hourly review15:50:40UTC.\n\n### Existing scope remarks updated by proved results\n\n| Earlier identifier | Current identifier | Reason |\n|---|---|---|\n''')
    for pair in identity['remark_identity_map']:
        f.write(f"| {pair['old_id']} | {pair['current_id']} | {pair['reason']} |\n")
for name in ['merge_registers.py','source_census.py','export_agent_programs.py','update_current16.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with (w/'RESEARCH_SA15_report.md').open('a') as f:
    f.write('\n'+(w/'notes/SOURCE_CENSUS.md').read_text()+'\n')
assert (w/'RESEARCH_SA15_report.md').read_text().startswith('INCOMPLETE\n\n| Item |')
print(json.dumps(qa,indent=2))
