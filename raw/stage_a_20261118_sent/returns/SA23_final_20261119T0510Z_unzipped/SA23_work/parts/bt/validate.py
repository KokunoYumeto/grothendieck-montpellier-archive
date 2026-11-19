#!/usr/bin/env python3
import json,csv,collections
from pathlib import Path
P=Path(__file__).parent
items=json.loads((P/'items.json').read_text()); claims=json.loads((P/'claims.json').read_text()); problems=json.loads((P/'problems.json').read_text()); refs=json.loads((P/'reference_checks.json').read_text())
def rows(name):
    with (P/name).open() as f:return list(csv.DictReader(f,delimiter='\t'))
entries=rows('entries.tsv');reads=rows('readings.tsv');links=rows('links.tsv');events=rows('check_events.tsv');queries=[json.loads(s) for s in (P/'search_log.jsonl').read_text().splitlines()]
ii={a['id'] for a in items};ci={a['id'] for a in claims};rr={a['key'] for a in refs}
assert len(entries)==99 and len({e['entry_id'] for e in entries})==99
assert all(e['item_id'] in ii for e in entries)
assert set(s for a in items for s in a['sources'])==set(e['entry_id'] for e in entries)
assert all(set(c['items'])<=ii for c in claims)
assert all(set(c['refs'])<=rr for c in claims)
assert all(set(p['refs'])<=rr for p in problems)
assert ci<={s for q in queries for s in q['claim_ids']}
assert ci<={a['statement_id'] for a in events}
assert all(a['id'] in {e['statement_id'] for e in events} for a in items)
assert all(a['key'] in {e['statement_id'] for e in events} for a in refs)
assert len(ci)==len(claims) and len(ii)==len(items)
directions=json.loads((P/'directions.json').read_text());pi={p['id'] for p in problems}
assert all(c.get('status_category') and c.get('record_origin') for c in claims)
for d in directions:
    assert set(d['items'])<=ii and set(d['claims'])<=ci and set(d['problems'])<=pi
    assert d['items'] and d['claims'] and d['problems']
    assert all(1<=d[k]<=5 for k in ['interest','feasible_progress_in_one_run'])
report=dict(scope='Core99 indexed entries and overlapping Codex161-5; no claim to161-3,161-4 or API24 coverage in this part',date='2026-11-19',entries=len(entries),items=len(items),claims=len(claims),problems=len(problems),reading_flags=len(reads),links=len(links),project_leads=sum(a['kind']=='our projects' for a in links),bibliography=len(refs),search_records=len(queries),events=len(events),claims_by_class=dict(collections.Counter(c['class'] for c in claims)),verdicts=dict(collections.Counter(e['verdict'] for e in entries)),claim_confidence=dict(collections.Counter(c['confidence'] for c in claims)),computational_blocks=len(json.loads((P/'compute_checks.output.json').read_text())),checks='All entry/item/ref/claim/search/event identifiers resolve; all89claims have searched fates. Source read coverage is separately documented; a structural check is not a proof of mathematical completeness.')
report['directions']=len(directions)
report['claims_by_origin']=dict(collections.Counter(c['record_origin'] for c in claims))
report['claims_by_status']=dict(collections.Counter(c['status_category'] for c in claims))
import runpy
report['problem_origin_validation']=runpy.run_path(str(P.parents[1]/'integration/validate_problem_origins.py'))['validate']('bt')
report['editorial_tasks']=report['problem_origin_validation']['editorial_tasks']
report['editorial_directions']=report['problem_origin_validation']['editorial_directions']
(P/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2))
