"""Finalize CP27 only after actual final-image inspections and log checks."""
from pathlib import Path
import csv,datetime,json,subprocess,sys,io,zipfile,re,hashlib
w=Path(__file__).resolve().parents[1]
now_dt=datetime.datetime.now(datetime.timezone.utc)
now=now_dt.isoformat()
review=json.loads((w/'notes/progress_review_18.json').read_text())
assert review['review']==18
review_actual=datetime.datetime.fromisoformat(review['actual_utc'].replace('Z','+00:00'))
review_due=datetime.datetime.fromisoformat('2026-11-19T22:50:40+00:00')
assert review_due<=review_actual<=now_dt, (review_due,review_actual,now_dt)
dest=w/'outputs/visual_qa_checkpoint27.json';assert not dest.exists()
paths_by_owner={
 'root':['notes/qa27_root_actual_review.json'],
 'monodromy':['agents/monodromy/outputs/monodromy_CP27_visual_QA.json'],
 'reduction_descent':['agents/reduction_descent/outputs/CP27_visual_QA.json'],
 'obstructions_crystals':['agents/obstructions_crystals/CP27_visual_QA.json']}
records={owner:[json.loads((w/p).read_text()) for p in rels] for owner,rels in paths_by_owner.items()}
groups={}
for owner,entries in records.items():
    pages=[]
    for r in entries:
        assert 'PASS' in r.get('status',r.get('result',''))
        keys=['pages','actual_images_viewed','pages_actually_viewed','actually_viewed_pages','actual_individually_viewed_pages']
        key=next(k for k in keys if k in r)
        pages.extend(x['page'] if isinstance(x,dict) else x for x in r[key])
    groups[owner]=sorted(pages)
pending=json.loads((w/'outputs/visual_qa27_pending.json').read_text())
pdfhash=hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
assert pdfhash==pending['pdf_sha256']
assert all(r['pdf_sha256']==pdfhash for entries in records.values() for r in entries)
assert sorted(sum(groups.values(),[]))==pending['pages_rendered']
build=json.loads((w/'outputs/build_summary.json').read_text())
assert build['over_2pt']==0 and not build['undefined_references'] and not build['undefined_citations']
assert 'Missing character:' not in (w/'RESEARCH_SA15_paper.log').read_text()
paths=json.loads((w/'outputs/checkpoint27_program_path_verification.json').read_text());assert paths['status']=='PASS'
for name in ['merge_registers.py','source_census.py','export_agent_programs.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with zipfile.ZipFile(w.parent/'RESEARCH_SA15_checkpoint_26.zip') as z:
    old={r['id'] for r in csv.DictReader(io.StringIO(z.read('RESEARCH_SA15_results.csv').decode()))}
current=list(csv.DictReader((w/'RESEARCH_SA15_results.csv').open()));ids={r['id'] for r in current};new=ids-old
events=list(csv.DictReader((w/'CHECK_EVENTS.tsv').open(),delimiter='\t'));checked={r['statement_id'] for r in events}
assert old<=ids and new<=checked,(old-ids,new-checked)
assert not any('pending' in r['where_proved'] for r in current)
coverage={'status':'PASS','actual_utc':now,'current_statements':len(current),'check_events_before_layout_event':len(events),'new_identifiers':len(new),'removed_identifiers':0,'all_new_identifiers_have_explicit_event':True,'new_ids':sorted(new)}
(w/'outputs/statement_coverage_checkpoint27.json').write_text(json.dumps(coverage,indent=2)+'\n')
attempts=[json.loads(p.read_text()) for p in sorted((w/'outputs').glob('checkpoint27_integration_attempt*.json'))]
# Failed attempts may contain a stale summary copied from the previous build.
# Parse each preserved actual log instead; never treat stale summary as that attempt.
actual_boxes=[]
for attempt in attempts:
    log=w/attempt['actual_build_snapshot']/'RESEARCH_SA15_paper.log'
    text=log.read_text(errors='replace')
    boxes=[{'points':float(m.group(1)),'context':text[m.start():m.start()+500]} for m in re.finditer(r'Overfull \\[hv]box \(([-\d.]+)pt',text)]
    actual_boxes.append({'attempt':attempt['attempt'],'build_exit_code':attempt['build_exit_code'],'log':str(log.relative_to(w)),'overfull_boxes':boxes,'over_2pt':sum(b['points']>2 for b in boxes)})
first_success=next(a for a in actual_boxes if a['build_exit_code']==0)
first={'attempt':first_success['attempt'],'over_2pt':first_success['over_2pt'],'overfull_boxes':first_success['overfull_boxes']}
maximum_all_attempts=max((b['points'] for a in actual_boxes for b in a['overfull_boxes']),default=0)
(w/'outputs/checkpoint27_all_actual_overflows.json').write_text(json.dumps(actual_boxes,indent=2)+'\n')
qa={'checkpoint':27,'actual_observed_utc':now,'status':'PASS','pdf_pages':pending['pages_in_pdf'],'pdf_bytes':build['pdf_bytes'],'pdf_sha256':pdfhash,'final_build_seconds':build['seconds'],'actual_build_attempts':len(attempts),'actual_log_overflows':actual_boxes,'maximum_overflow_across_all_attempts':maximum_all_attempts,'failed_builds':sum(r['build_exit_code']!=0 for r in attempts),'first_successful_attempt':first['attempt'],'over_2pt_before':first['over_2pt'],'over_2pt_after':0,'maximum_before_points':max((b['points'] for b in first['overfull_boxes']),default=0),'max_overfull_points':max((b['points'] for b in build['overfull_boxes']),default=0),'actually_viewed_pages_by_reviewer':groups,'total_distinct_pages':len(pending['pages_rendered']),'all_selected_images_have_actual_inspection':True,'image_hashes':{str(n):hashlib.sha256((w/f'outputs/qa27/page_{n:03d}.png').read_bytes()).hexdigest() for n in pending['pages_rendered']},'undefined_references':False,'undefined_citations':False,'missing_glyphs':False,'criteria':'Every selected final page PNG was actually opened and visually inspected. Every newly included subsection, the actual repaired-overflow locations, a spread across earlier material and bibliography pages are covered. This is actual layout QA, not a mathematical computation.'}
qa['required_actual_review']={'review':18,'actual_utc':review_actual.isoformat(),'source':'notes/progress_review_18.json'}
dest.write_text(json.dumps(qa,indent=2)+'\n')
(w/'notes/qa27_actual_reviewers.json').write_text(json.dumps({'all_explicitly_confirmed':True,'records':records,'pages_by_reviewer':groups},indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    csv.writer(f,delimiter='\t').writerow(['CP27-VISUAL-QA',now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root and three independent reviewers','artifact verification',f"PASS: all {qa['total_distinct_pages']} selected final images actually viewed; {qa['pdf_pages']}-page PDF. {len(attempts)} actual builds, {qa['failed_builds']} failed compilations. Maximum across every actual attempt, including failed compilations: {maximum_all_attempts}pt. First successful and final build boxes above2pt: {first['over_2pt']} and0. Final maximum overflow {qa['max_overfull_points']}pt. No undefined references/citations or missing glyphs."])
bib=len(re.findall(r'^@',(w/'RESEARCH_SA15_references.bib').read_text(),re.M));census=len(list(csv.DictReader((w/'notes/SOURCE_CENSUS.tsv').open(),delimiter='\t')));exports=len(json.loads((w/'outputs/exported_programs.json').read_text()))
with (w/'notes/checkpoint27_changes.md').open('a') as f:
    f.write(f'''\n### Final checkpoint verification\n\nThe frozen paper has {qa['pdf_pages']} pages and {qa['pdf_bytes']} bytes, with {len(current)} numbered statements, {len(new)} new identifiers since checkpoint26 and no removed identifier. Every new identifier has an explicit check event and a final statement number. The paper bibliography has {bib} entries; the source census has {census} rows. The export currently contains {exports} agent program/output files. All {paths['referenced_program_paths']} literal printed program paths resolve. Any later candidate computation before archiving is also exported, without silently promoting its statement.\n\nThere were {qa['actual_build_attempts']} actual builds and {qa['failed_builds']} failed compilations. The actual logs of every attempt, including any failed compilations, are parsed separately from stale summaries. The maximum across all actual attempts was {maximum_all_attempts}pt. The first successful build (attempt{first['attempt']}) had {first['over_2pt']} boxes above2pt and the final build has zero; the final maximum is {qa['max_overfull_points']}pt. The final build took {build['seconds']} seconds. All {qa['total_distinct_pages']} selected final images were actually opened and visually reviewed, covering all newly included subsections, the residual overflow page, earlier material and the bibliography. No clipping, overlap, missing glyph or citation/tag defect was observed. The complete actual build inputs and logs are retained.\n\nCheckpoint27 is archived only at or after23:05:40UTC. Actual review18 was recorded at {review_actual.isoformat()}, read directly from notes/progress_review_18.json; its recorded no-movement streak is {review['no_movement_streak']}. The next actual review19 is due23:50:40UTC and checkpoint28 is due23:50:40UTC. No review or archive is represented as completed before its actual execution.\n''')
for name in ['merge_registers.py','source_census.py','update_current27.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
with (w/'RESEARCH_SA15_report.md').open('a') as f:f.write('\n'+(w/'notes/SOURCE_CENSUS.md').read_text()+'\n')
with (w/'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n## '+now+': checkpoint27 current-gate snapshot\n\n'
            'This is a current-state snapshot, not an hourly review. The audited additions '
            'are explicitly enumerated in notes/checkpoint27_changes.md and in the retained '
            'checkpoint27 integration records. Candidate work is not promoted by this snapshot. '
            'The complete current outcome table below records both proved advances and '
            'remaining gates. Actual review18 was recorded at '+review_actual.isoformat()+
            '; the next actual review19 and checkpoint28 are due23:50:40UTC. '
            'This snapshot does not replace an actual review.\n\n'+
            (w/'notes/current_outcome_table.md').read_text()+'\n')
assert (w/'RESEARCH_SA15_report.md').read_text().startswith('INCOMPLETE\n\n| Item |')
print(json.dumps({k:v for k,v in qa.items() if k!='image_hashes'},indent=2))
