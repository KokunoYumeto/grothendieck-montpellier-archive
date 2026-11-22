"""Finalize frozen CP21 after actual image inspections and final-log checks."""
from pathlib import Path
import csv,datetime,json,subprocess,sys,io,zipfile,re,hashlib
w=Path(__file__).resolve().parents[1];now=datetime.datetime.now(datetime.timezone.utc).isoformat()
dest=w/'outputs/visual_qa_checkpoint21.json';assert not dest.exists()
records={
'root':[json.loads((w/'notes/qa21_root_actual_review.json').read_text()),json.loads((w/'notes/qa21_root_additional_review.json').read_text())],
'monodromy':[json.loads((w/'agents/monodromy/outputs/monodromy_CP21_visual_QA.json').read_text())],
'reduction_descent':[json.loads((w/'agents/reduction_descent/outputs/CP21_visual_QA.json').read_text())],
'obstructions_crystals':[json.loads((w/'agents/obstructions_crystals/CP21_visual_QA.json').read_text())]}
groups={}
for owner,entries in records.items():
    pages=[]
    for r in entries:
        assert 'PASS' in r['status']
        pages.extend(x['page'] if isinstance(x,dict) else x for x in r['pages'])
    groups[owner]=sorted(pages)
pending=json.loads((w/'outputs/visual_qa21_pending.json').read_text())
assert sorted(sum(groups.values(),[]))==pending['pages_rendered']
build=json.loads((w/'outputs/build_summary.json').read_text())
assert build['over_2pt']==0 and not build['undefined_references'] and not build['undefined_citations']
assert 'Missing character:' not in (w/'RESEARCH_SA15_paper.log').read_text()
paths=json.loads((w/'outputs/checkpoint21_program_path_verification.json').read_text());assert paths['status']=='PASS'
for name in ['merge_registers.py','source_census.py','export_agent_programs.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_20.zip') as z:
    old={r['id'] for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
current=list(csv.DictReader((w/'RESEARCH_SA15_results.csv').open()));ids={r['id'] for r in current};new=ids-old
events=list(csv.DictReader((w/'CHECK_EVENTS.tsv').open(),delimiter='\t'));checked={r['statement_id'] for r in events}
assert old<=ids and new<=checked,(old-ids,new-checked)
assert not any('pending' in r['where_proved'] for r in current)
coverage={'status':'PASS','actual_utc':now,'current_statements':len(current),'check_events_before_layout_event':len(events),'new_identifiers':len(new),'removed_identifiers':0,'all_new_identifiers_have_explicit_event':True,'new_ids':sorted(new)}
(w/'outputs/statement_coverage_checkpoint21.json').write_text(json.dumps(coverage,indent=2)+'\n')
attempts=[json.loads(p.read_text()) for p in sorted((w/'outputs').glob('checkpoint21_integration_attempt*.json'))]
first=json.loads((w/'outputs/checkpoint21_build_attempt01/build_summary.json').read_text())
qa={'checkpoint':21,'actual_observed_utc':now,'status':'PASS','pdf_pages':pending['pages_in_pdf'],'pdf_bytes':build['pdf_bytes'],'pdf_sha256':hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest(),'final_build_seconds':build['seconds'],'actual_build_attempts':len(attempts),'failed_builds':sum(r['build_exit_code']!=0 for r in attempts),'over_2pt_before':first['over_2pt'],'over_2pt_after':0,'maximum_before_points':max(b['points'] for b in first['overfull_boxes']),'max_overfull_points':max((b['points'] for b in build['overfull_boxes']),default=0),'actually_viewed_pages_by_reviewer':groups,'total_distinct_pages':len(pending['pages_rendered']),'all_selected_images_have_actual_inspection':True,'image_hashes':{str(n):hashlib.sha256((w/f'outputs/qa21/page_{n:03d}.png').read_bytes()).hexdigest() for n in pending['pages_rendered']},'undefined_references':False,'undefined_citations':False,'missing_glyphs':False,'criteria':'Every selected final page PNG was actually opened and visually inspected. All six new subsections, both pages carrying a prior or final overflow, and a spread across earlier material and bibliography are covered. No clipping, overlap, illegible mathematics, equation-tag collision or missing glyph observed. This is actual layout QA, not a mathematical audit or computation.'}
dest.write_text(json.dumps(qa,indent=2)+'\n')
(w/'notes/qa21_actual_reviewers.json').write_text(json.dumps({'all_explicitly_confirmed':True,'records':records,'pages_by_reviewer':groups},indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    csv.writer(f,delimiter='\t').writerow(['CP21-VISUAL-QA',now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root and three independent reviewers','artifact verification',f"PASS: all{qa['total_distinct_pages']}selected final images actually viewed;{qa['pdf_pages']}-page PDF. Two actual builds, no failed compilation. Initial3.4239ptB56.1overflow corrected by splitting its display; zero final boxes above2pt, sole0.41342ptbox actually viewed. No undefined references/citations or missing glyphs."])
bib=len(re.findall(r'^@',(w/'RESEARCH_SA15_references.bib').read_text(),re.M));census=len(list(csv.DictReader((w/'notes/SOURCE_CENSUS.tsv').open(),delimiter='\t')));exports=len(json.loads((w/'outputs/exported_programs.json').read_text()))
with (w/'notes/checkpoint21_changes.md').open('a') as f:
    f.write(f'''\n### Final checkpoint verification\n\nThe frozen paper has{qa['pdf_pages']}pages and{qa['pdf_bytes']}bytes, with{len(current)}numbered statements,{len(new)}new identifiers since checkpoint20 and no removed identifier. Every new identifier has an explicit check event and a final statement number. The paper bibliography has{bib}entries; the source census has{census}rows including late actually read candidate sources. The export currently contains{exports}agent program/output files; any later executed candidate files before archiving are also exported. All{paths['referenced_program_paths']}literal printed program paths resolve.\n\nThere were{qa['actual_build_attempts']}actual builds and{qa['failed_builds']}failed compilations. The first build had one box above2pt, a3.4239pt B56.1display onp405. Splitting its valuation line repaired it. The final build took{build['seconds']}seconds and has zero boxes above2pt; its sole smaller box is0.41342pt onp173. All{qa['total_distinct_pages']}selected final images were actually opened and visually reviewed, includingp405,p173,all six new subsections,and a spread over the earlier paper and bibliography. No clipping, overlap, missing glyph or citation/tag defect was observed. Both complete build inputs and logs are retained.\n\nCheckpoint21 is archived only at or after18:35:40UTC. The most recent actual hourly review remains review13 at17:50:58.396506UTC,with movement and zero no-movement streak. The next actual review is due18:50:40UTC; the next checkpoint is due19:20:40UTC. No early review or early archive is represented as completed.\n''')
for name in ['merge_registers.py','source_census.py','update_current21.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with (w/'RESEARCH_SA15_report.md').open('a') as f:f.write('\n'+(w/'notes/SOURCE_CENSUS.md').read_text()+'\n')
with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n## '+now+': checkpoint21 current-gate snapshot\n\nThis is a current-state snapshot, not an hourly review. Actualreview13 and its movement assessment remain unchanged. The new rank-six Lang gate, nilpotent-line variation gate and full-p⁴ wild-image gate will be assessed at actualreview14, due18:50:40UTC. B58/B59 and polar normal-form candidates are outside this frozen paper.\n\n'+(w/'notes/current_outcome_table.md').read_text()+'\n')
assert (w/'RESEARCH_SA15_report.md').read_text().startswith('INCOMPLETE\n\n| Item |')
print(json.dumps({k:v for k,v in qa.items() if k!='image_hashes'},indent=2))
