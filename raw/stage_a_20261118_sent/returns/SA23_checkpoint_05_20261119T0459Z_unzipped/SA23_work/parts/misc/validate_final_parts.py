"""Integrity validation of the manually completed misc and Groupes records.

This checks serialization and provenance, not mathematical truth or novelty.
"""
import csv, datetime, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
report = {'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'scope': 'Structural and quotation integrity only; the source and mathematical assessments are manual.',
          'parts': {}}
expected = {'misc': (53,74,23,4,7,53), 'groupes': (27,115,61,13,11,0)}
for part, nums in expected.items():
    p = ROOT/'SA23_work/parts'/part
    def js(name): return json.loads((p/(name+'.json')).read_text())
    def ts(name):
        with (p/(name+'.tsv')).open() as f: return list(csv.DictReader(f,delimiter='\t'))
    items,claims,problems,eds,dirs = [js(n) for n in ['items','claims','problems','editorial_tasks','directions']]
    entries,events,readings,links = [ts(n) for n in ['entries','check_events','readings','links']]
    actual=tuple(map(len,[items,claims,problems,eds,dirs,entries])); assert actual==nums,(part,actual)
    ids=[{x['id'] for x in xs} for xs in [items,claims,problems,eds,dirs]]
    assert len(set.union(*ids)) == sum(map(len,[items,claims,problems,eds,dirs]))
    iid,cid,pid,eid,did=ids
    refs=set(re.findall(r'@\w+\{([^,]+),',(p/'references.bib').read_text()))
    searches=[json.loads(s) for s in (p/'search_log.jsonl').read_text().splitlines()]
    search_key='claim_ids' if part=='misc' else 'claims'
    searched={x for s in searches for x in s.get(search_key,[])}
    assert cid<=searched, (part,cid-searched)
    checked={e['statement_id'] for e in events}
    assert cid<=checked,(part,cid-checked)
    for c in claims:
        assert c['items'] and set(c['items'])<=iid,(c['id'],c['items'])
        assert set(c['refs'])<=refs,(c['id'],c['refs'])
        assert c['record_origin'] in ['source assertion','source question','source fragment, not an identifiable assertion'],(c['id'],c['record_origin'])
        assert c['reconstruction_boundary']
        assert c['computation']['proof_or_check']
        assert c['his_statement'] and c.get('source_paraphrase')
    for q in js('quotation_audit'):
        lines=(ROOT/q['source_file']).read_text().splitlines()
        selected='\n'.join('\n'.join(lines[a-1:b]) for a,b in q['selected_lines'])
        assert all(fragment in selected for fragment in q['literal_fragments']),q['id']
        assert q['id'] in cid
    assert len(js('quotation_audit'))==len(claims)
    redirects=js('problem_editorial_redirects')
    assert len(redirects)==(4 if part=='misc' else 11)
    assert not (set(redirects)&pid)
    assert set(redirects.values())<=eid
    for e in eds:
        assert e['origin']=='present-run editorial task'
        if 'original_id' in e:
            assert e['original_id'] not in pid and redirects[e['original_id']]==e['id']
        else:
            assert e['source_problem_id'] in pid and e['component_scope']
    for d in dirs:
        assert set(d['items'])<=iid and d['items'],d['id']
        assert set(d['claims'])<=cid and d['claims'],d['id']
        assert set(d['problems'])<=pid and d['problems'],d['id']
        assert set(d.get('editorial_tasks',[]))<=eid,d['id']
        assert 1<=d['interest']<=5 and 1<=d['feasible_progress_in_one_run']<=5
        assert d['first_step'] and d['known'] and d['residual']
    for problem in problems:
        assert problem['record_type']=='authorial problem'
        assert problem['occurrences'] and problem['as_he_states'] and problem['worth']
        assert set(problem['refs'])<=refs,(problem['id'],problem['refs'])
    for e in entries: assert e['item_id'] in iid
    count=js('counts')
    for key,value in [('claims',len(claims)),('problems',len(problems)),('editorial_tasks',len(eds)),
                      ('directions',len(dirs)),('readings',len(readings)),('links',len(links)),
                      ('references',len(refs)),('search_events',len(searches)),('check_events',len(events))]:
        assert count[key]==value,(part,key,count[key],value)
    if part=='groupes':
        assert all(c['status_category'] in ['proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages'] for c in claims)
        assert all(not c['missing_lines'] for c in js('read_coverage'))
        assert len(js('computations/check_groupes.output'))==19
        assert len(re.findall(r'^## C-SA23-groupes-',(p/'computations/proof_certificates.md').read_text(),re.M))==115
        assert count['transcription_physical_lines']==5006
    else:
        assert 'ALL ASSERTIONS PASSED' in (p/'computations/check_misc_output.txt').read_text()
    report['parts'][part]=dict(items=len(items),claims=len(claims),authorial_problems=len(problems),editorial_tasks=len(eds),
                              whole_redirects=len(redirects),partial_editorial_splits=sum('source_problem_id' in e for e in eds),
                              directions=len(dirs),literal_claim_quotations=len(claims),references=len(refs),
                              mapped_search_records=len(searches),check_events=len(events),passed=True)

report['all_assertions_passed']=True
out=Path(__file__).resolve().parent/'final_validation.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
