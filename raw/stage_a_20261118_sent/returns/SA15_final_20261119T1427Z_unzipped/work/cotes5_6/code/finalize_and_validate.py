"""Rebuild the hand-authored records and audit coverage/cross-references.

This validates serialization, not mathematical truth. Mathematical checks were
performed separately and are scoped in check_events.tsv and the proof appendix.
"""
from pathlib import Path
from collections import Counter
import csv,json,re,subprocess,sys
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
log=[]
for filename in ['build_dossier.py','build_references.py','build_search_families.py','build_claims.py','build_problems.py','build_readings.py','build_root_links.py','build_links.py','build_check_events.py']:
    completed=subprocess.run([sys.executable,str(ROOT/'code'/filename)],capture_output=True,text=True)
    log.append({'program':'code/'+filename,'exit_code':completed.returncode,'stdout':completed.stdout,'stderr':completed.stderr})
    if completed.returncode:
        (ROOT/'outputs/final_build.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
        raise RuntimeError(filename+' failed: '+completed.stderr)

def J(name):return json.loads((ROOT/name).read_text())
def T(name):return list(csv.DictReader((ROOT/name).open(),delimiter='\t'))
items=J('items.json'); claims=J('claims.json');problems=J('problems.json')
refs=J('reference_evidence.json');families=J('search_families.json')
entries=T('supplementary_entries.tsv');readings=T('readings.tsv');events=T('check_events.tsv')
ids={i['id'] for i in items};cids={c['id'] for c in claims};pids={p['id'] for p in problems}
rids={r['key'] for r in refs};fids={f['id'] for f in families}
assert len(ids)==len(items) and len(cids)==len(claims) and len(pids)==len(problems)
assert len(entries)==444
sourceids={f'MPL_5+6_001-037##{n}' for n in range(1,445)}
assert {e['entry_id'] for e in entries}==sourceids
assert Counter(s for i in items for s in i['sources'])==Counter(sourceids)
assert all(e['item_id'] in ids and e['reason'] for e in entries)

required={
 'items':{'id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'},
 'claims':{'id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence','hypotheses','literature_search_history'},
 'problems':{'id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs'}}
for label,records in [('items',items),('claims',claims),('problems',problems)]:
    for row in records:assert required[label]<=set(row),(label,row['id'])
for c in claims:
    assert set(c['items'])<=ids
    assert set(c['refs'])<=rids,(c['id'],set(c['refs'])-rids)
    assert c['literature_search_history']['family_id'] in fids
    assert c['class'] in 'ABCDEF'
    assert c['hypotheses'] and c['literature_search_history']['exact_match_assessment']
for p in problems:
    assert set(p['items'])<=ids and set(p['claims'])<=cids and set(p['refs'])<=rids
for r in refs:
    assert r['note']=='verified' and r['url'].startswith('https://') and r['exact_locator'] and r['verification_scope']

known=ids|cids|rids
assert {e['statement_id'] for e in events}==known
for e in events:
    if e['type']=='refuted, with the refined statement’s id':
        matches=re.findall(r'refined statement (P56-C\d+)',e['outcome'])
        assert len(matches)==1 and matches[0] in cids,e
assert all(r['item_id'] in ids for r in readings)
assert all('unchanged' in r['status'] for r in readings)

page_inventory=J('outputs/page_inventory.json')
page_set={(int(p['cote']),int(p['scan'])) for p in page_inventory}
read_log=T('source_read_log.tsv')
read_set={(int(r['cote']),int(r['scan'])) for r in read_log if r['source'].endswith('_transcription.tex') and r['cote'] and r['scan']}
assert page_set<=read_set,(page_set-read_set)
assert len(page_set)==89
for i in items:
    assert all((s['cote'],s['scan']) in page_set for s in i['scans'])
for filename in ['links.tsv','root_crosslinks.tsv','project_leads.tsv']:
    rows=T(filename)
    fields=next(csv.reader((ROOT/filename).open(),delimiter='\t'))
    assert fields==['kind','from','to','what','evidence','note_ids'],(filename,fields)
    for row in rows:
        assert row['kind'] in ['folder','published work','our projects']
        assert set(row['note_ids'].split(';'))<=sourceids,(filename,row)
        assert row['from'] and row['to'] and row['evidence']

claimby={c['id']:c for c in claims}
assert claimby['P56-C058']['class']=='B' and claimby['P56-C059']['class']=='B'
assert 'without a smoothness hypothesis' in claimby['P56-C102']['statement']
assert 'induced' in claimby['P56-C041']['statement']
assert 1000<=len((ROOT/'narrative.md').read_text().split())<=1500
for path in [ROOT/'narrative.md',ROOT/'directions.md',ROOT/'reviews/independent_proofs.md']:
    for ident in re.findall(r'P56-[ICP]\d{3}',path.read_text()):
        assert ident in ids|cids|pids,(path,ident)

summary={
 'completed_utc':datetime.now(timezone.utc).isoformat(),
 'source_scan_blocks':len(page_set),'substantive_supplemental_entries':len(entries),
 'items':len(items),'claims':len(claims),'problems':len(problems),'reading_alarms':len(readings),
 'links':len(T('links.tsv')),'root_crosslinks':len(T('root_crosslinks.tsv')),'project_leads':len(T('project_leads.tsv')),
 'directions':10,'references':len(refs),'search_families':len(families),'check_events':len(events),
 'items_by_kind':dict(Counter(i['kind'] for i in items)),
 'entry_verdict_counts':dict(Counter(e['verdict'] for e in entries)),
 'claims_by_class':dict(Counter(c['class'] for c in claims)),
 'claims_by_status':dict(Counter(c['status_on_pages'] for c in claims)),
 'check_event_types':dict(Counter(e['type'] for e in events)),
 'validation':'All coverage, field, ID, source-locator, refutation-target, provenance and table-schema checks passed. This is a serialization audit, not an additional mathematical proof.'}
(ROOT/'outputs/final_build.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
(ROOT/'outputs/validation_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
