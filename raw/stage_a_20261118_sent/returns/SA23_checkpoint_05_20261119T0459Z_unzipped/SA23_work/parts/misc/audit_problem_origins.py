"""Manual origin-cue correction: assertions stay claims, checks become ED tasks."""
import copy,csv,json,pathlib
P=pathlib.Path(__file__).resolve().parent
ps=json.loads((P/'problems.json').read_text())
olded=json.loads((P/'editorial_tasks.json').read_text()) if (P/'editorial_tasks.json').exists() else []
for e in olded:
    if e.get('original_id') and not any(p['id']==e['original_id'] for p in ps):
        p=copy.deepcopy(e);p['id']=p['original_id'];ps.append(p)
ps.sort(key=lambda p:p['id'])
reasons={
 2:'The Pro text at382–386 states its own finite-projectivity/representability qualification. It does not ask for a theorem; our base-change counterexample and commentary are editorial verification.',
 8:'K161-6-01:123 says that the last vector need not be checked and changes to a rotation proof. It does not leave that verification open; our explicit distance computation is an editorial check.',
 17:'K161-6-02:294–298 states three arithmetic assertions a), b), c) without a proof. No question, deferred proof request, or explicit conjectural marker appears; the missing-hypothesis investigation is editorial.',
 27:'K161-6-01:214–222 asserts an equivalence of data and the fifth-power circle-bundle identification. The uncertain final soit/ellipsis is not enough to establish an authorial question; collation and verification belong to the editorial register.',
}
ed=[];redirect={};keep=[];audit=[]
for p in ps:
    n=int(p['id'].rsplit('-',1)[1])
    if n in reasons:
        e=copy.deepcopy(p);e['original_id']=p['id'];e['id']=p['id'].replace('MP-','ED-',1)
        e.update(origin='present-run editorial task',record_type='editorial task',source_cue=reasons[n],cue_or_reason=reasons[n])
        for o in e['occurrences']:o['drafting_status']='source assertion or proof; no authorial question at this endpoint'
        if n==27:e['occurrences'][0]['lines']='214–222'
        e.setdefault('editorial_formulation',e['as_he_states'])
        e['as_he_states']=e['source_cue']
        ed.append(e);redirect[p['id']]=e['id'];audit.append(dict(original_id=p['id'],destination=e['id'],decision='editorial task',reason=reasons[n]))
    else:
        p.update(origin='authorial question, doubt, deferred step, or unfinished calculation',record_type='authorial problem')
        keep.append(p);audit.append(dict(original_id=p['id'],destination=p['id'],decision='retained authorial problem',reason=p['as_he_states']))
for name,data in [('problems.json',keep),('editorial_tasks.json',ed),('problem_editorial_redirects.json',redirect),('problem_origin_audit.json',audit)]:
    (P/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
ds=json.loads((P/'directions.json').read_text())
for d in ds:
    moved=[x for x in d['problems'] if x in redirect]
    if moved:d['editorial_tasks']=list(dict.fromkeys(d.get('editorial_tasks',[])+[redirect[x] for x in moved]))
    d['problems']=[x for x in d['problems'] if x not in redirect]
    assert d['problems'],d['id']
(P/'directions.json').write_text(json.dumps(ds,ensure_ascii=False,indent=2)+'\n')
for filename in ['directions.md','section.md']:
    text=(P/filename).read_text()
    for old,new in redirect.items():text=text.replace(old,new)
    (P/filename).write_text(text)
counts=json.loads((P/'counts.json').read_text());counts.update(problems=len(keep),editorial_tasks=len(ed));(P/'counts.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
coverage=(P/'coverage.md').read_text()
if '## Authorial-origin audit' not in coverage:
    coverage+='\n## Authorial-origin audit\n\nThe final literal-source audit separates four editorial verification tasks from the authorial problem index: former MP-SA23-misc-02,08,17,27 become ED-SA23-misc-02,08,17,27. All underlying claims, proofs, searches, and reading alarms remain. The source respectively supplies a qualification, a deliberately dispensable check, three unproved assertions, and a bundle-identification margin; none is an explicit author question. There are now **23 authorial problems and four editorial tasks**. The earlier count of 27 is the historical pre-audit register, not the final problem total. The remaining source cues include actual questions, deferred proofs, canceled doubts, and unfinished displayed calculations. `problem_origin_audit.json` records each decision; `problem_editorial_redirects.json` records stable redirects.\n'
(P/'coverage.md').write_text(coverage)
print(json.dumps({'authorial_problems':len(keep),'editorial_tasks':len(ed),'redirects':redirect}))
