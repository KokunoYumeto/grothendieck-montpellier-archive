"""Finalize CP22 only after actual final-image inspections and log checks."""
from pathlib import Path
import csv,datetime,json,subprocess,sys,io,zipfile,re,hashlib
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
dest=w/'outputs/visual_qa_checkpoint22.json';assert not dest.exists()
paths_by_owner={
 'root':['notes/qa22_root_actual_review.json'],
 'monodromy':['agents/monodromy/outputs/monodromy_CP22_visual_QA.json'],
 'reduction_descent':['agents/reduction_descent/outputs/CP22_visual_QA.json'],
 'obstructions_crystals':['agents/obstructions_crystals/CP22_visual_QA.json']}
records={owner:[json.loads((w/p).read_text()) for p in rels] for owner,rels in paths_by_owner.items()}
groups={}
for owner,entries in records.items():
    pages=[]
    for r in entries:
        assert 'PASS' in r.get('status',r.get('result',''))
        pages.extend(x['page'] if isinstance(x,dict) else x for x in r.get('pages',r.get('actual_images_viewed',[])))
    groups[owner]=sorted(pages)
pending=json.loads((w/'outputs/visual_qa22_pending.json').read_text())
pdfhash=hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
assert pdfhash==pending['pdf_sha256']
assert sorted(sum(groups.values(),[]))==pending['pages_rendered']
build=json.loads((w/'outputs/build_summary.json').read_text())
assert build['over_2pt']==0 and not build['undefined_references'] and not build['undefined_citations']
assert 'Missing character:' not in (w/'RESEARCH_SA15_paper.log').read_text()
paths=json.loads((w/'outputs/checkpoint22_program_path_verification.json').read_text());assert paths['status']=='PASS'
for name in ['merge_registers.py','source_census.py','export_agent_programs.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_21.zip') as z:
    old={r['id'] for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
current=list(csv.DictReader((w/'RESEARCH_SA15_results.csv').open()));ids={r['id'] for r in current};new=ids-old
events=list(csv.DictReader((w/'CHECK_EVENTS.tsv').open(),delimiter='\t'));checked={r['statement_id'] for r in events}
assert old<=ids and new<=checked,(old-ids,new-checked)
assert not any('pending' in r['where_proved'] for r in current)
coverage={'status':'PASS','actual_utc':now,'current_statements':len(current),'check_events_before_layout_event':len(events),'new_identifiers':len(new),'removed_identifiers':0,'all_new_identifiers_have_explicit_event':True,'new_ids':sorted(new)}
(w/'outputs/statement_coverage_checkpoint22.json').write_text(json.dumps(coverage,indent=2)+'\n')
attempts=[json.loads(p.read_text()) for p in sorted((w/'outputs').glob('checkpoint22_integration_attempt*.json'))]
first=json.loads((w/'outputs/checkpoint22_build_attempt01/build_summary.json').read_text())
qa={'checkpoint':22,'actual_observed_utc':now,'status':'PASS','pdf_pages':pending['pages_in_pdf'],'pdf_bytes':build['pdf_bytes'],'pdf_sha256':pdfhash,'final_build_seconds':build['seconds'],'actual_build_attempts':len(attempts),'failed_builds':sum(r['build_exit_code']!=0 for r in attempts),'over_2pt_before':first['over_2pt'],'over_2pt_after':0,'maximum_before_points':max((b['points'] for b in first['overfull_boxes']),default=0),'max_overfull_points':max((b['points'] for b in build['overfull_boxes']),default=0),'actually_viewed_pages_by_reviewer':groups,'total_distinct_pages':len(pending['pages_rendered']),'all_selected_images_have_actual_inspection':True,'image_hashes':{str(n):hashlib.sha256((w/f'outputs/qa22/page_{n:03d}.png').read_bytes()).hexdigest() for n in pending['pages_rendered']},'undefined_references':False,'undefined_citations':False,'missing_glyphs':False,'criteria':'Every selected final page PNG was actually opened and visually inspected. All nine new subsections, the sole residual overflow page, a spread across earlier material, and bibliography pages are covered. This is actual layout QA, not a mathematical computation.'}
dest.write_text(json.dumps(qa,indent=2)+'\n')
(w/'notes/qa22_actual_reviewers.json').write_text(json.dumps({'all_explicitly_confirmed':True,'records':records,'pages_by_reviewer':groups},indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    csv.writer(f,delimiter='\t').writerow(['CP22-VISUAL-QA',now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root and three independent reviewers','artifact verification',f"PASS: all {qa['total_distinct_pages']} selected final images actually viewed; {qa['pdf_pages']}-page PDF. {len(attempts)} actual builds, {qa['failed_builds']} failed compilations. Initial and final boxes above2pt: {first['over_2pt']} and0. Final maximum overflow {qa['max_overfull_points']}pt. No undefined references/citations or missing glyphs."])
bib=len(re.findall(r'^@',(w/'RESEARCH_SA15_references.bib').read_text(),re.M));census=len(list(csv.DictReader((w/'notes/SOURCE_CENSUS.tsv').open(),delimiter='\t')));exports=len(json.loads((w/'outputs/exported_programs.json').read_text()))
with (w/'notes/checkpoint22_changes.md').open('a') as f:
    f.write(f'''\n### Final checkpoint verification\n\nThe frozen paper has {qa['pdf_pages']} pages and {qa['pdf_bytes']} bytes, with {len(current)} numbered statements, {len(new)} new identifiers since checkpoint21 and no removed identifier. Every new identifier has an explicit check event and a final statement number. The paper bibliography has {bib} entries; the source census has {census} rows. The export currently contains {exports} agent program/output files. All {paths['referenced_program_paths']} literal printed program paths resolve. Any later candidate computation before archiving is also exported, without silently promoting its statement.\n\nThere were {qa['actual_build_attempts']} actual builds and {qa['failed_builds']} failed compilations. The first build had {first['over_2pt']} boxes above2pt and the final build has zero; the final maximum is {qa['max_overfull_points']}pt. The final build took {build['seconds']} seconds. All {qa['total_distinct_pages']} selected final images were actually opened and visually reviewed, covering all nine newly included subsections, the residual overflow page, earlier material and the bibliography. No clipping, overlap, missing glyph or citation/tag defect was observed. The complete actual build inputs and logs are retained.\n\nCheckpoint22 is archived only at or after19:20:40UTC. Actual hourly review14 was recorded18:53:07.274754UTC, with movement and zero no-movement streak. The later B60/B61 closure and all-odd natural-block theorem will be assessed at the next actual review, due19:50:40UTC. The next checkpoint is due20:05:40UTC. No early review or early archive is represented as completed.\n''')
for name in ['merge_registers.py','source_census.py','update_current22.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with (w/'RESEARCH_SA15_report.md').open('a') as f:f.write('\n'+(w/'notes/SOURCE_CENSUS.md').read_text()+'\n')
with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n## '+now+': checkpoint22 current-gate snapshot\n\nThis is a current-state snapshot, not an hourly review. Actualreview14 and its movement assessment remain unchanged. B60/B61 now close the p>=5 minimal-ramification height-two interval at1; all fixed nonordinary odd degrees also contain an actual GL8 block. General A.3/A.4, higher-dimensional B.3 and the other B.4 ramification/height cases remain open. The next actual review is due19:50:40UTC.\n\n'+(w/'notes/current_outcome_table.md').read_text()+'\n')
assert (w/'RESEARCH_SA15_report.md').read_text().startswith('INCOMPLETE\n\n| Item |')
print(json.dumps({k:v for k,v in qa.items() if k!='image_hashes'},indent=2))
