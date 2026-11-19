"""Structural and coverage checks for the completed manually authored audit.

This validates serialization and evidence links, not the truth of mathematics.
"""
from pathlib import Path
from collections import Counter
import csv,json,re,sys
WORK=Path(__file__).resolve().parents[1];OUT=WORK/'parts/a'
ROOT=WORK.parent
def rows(name):return list(csv.DictReader((OUT/name).open(),delimiter='\t'))
entries=rows('entries.tsv');items=json.loads((OUT/'items.json').read_text())
claims=json.loads((OUT/'claims.json').read_text());problems=json.loads((OUT/'problems.json').read_text())
readings=rows('readings.tsv');links=rows('links.tsv');events=rows('CHECK_EVENTS.tsv');searches=rows('search_log.tsv')
schemas={
 'items':{'id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'},
 'claims':{'id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'},
 'problems':{'id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs'}
}
for name,data in [('items',items),('claims',claims),('problems',problems)]:
 assert len({x['id'] for x in data})==len(data),name
 assert all(set(x)==schemas[name] for x in data),name
 assert all(x['id'].startswith({'items':'SA04-','claims':'C-SA04-','problems':'MP-SA04-'}[name]) for x in data),name
expected={f'MPL_93_047-091#{n}' for n in range(1,161)}
actual=[e['entry_id'] for e in entries]
assert len(actual)==160 and set(actual)==expected
sourceindex=list(csv.DictReader((ROOT/'source/SA04_notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
assert expected.issubset({e['entry_id'] for e in sourceindex})
itemids={i['id'] for i in items};claimids={c['id'] for c in claims}
assert all(e['item_id'] in itemids for e in entries)
assert set(x for i in items for x in i['sources'])==expected
assert len([x for i in items for x in i['sources']])==160
for e in entries:
 assert e['entry_id'] in next(i['sources'] for i in items if i['id']==e['item_id'])
 assert e['reason'].strip()
assert all(i in itemids for c in claims for i in c['items'])
refs={r['key'] for r in rows('reference_checks.tsv')}
bib=(OUT/'references.bib').read_text()
assert refs==set(re.findall(r'@\w+\{([^,]+),',bib))
assert bib.count('note = {verified}')+bib.count('note = {unverified}')==len(refs)
assert all(r in refs for c in claims+problems for r in c['refs'])
assert all(c['class'] in 'ABCDEF' for c in claims)
assert all(c['status_on_pages'] in {'proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages'} for c in claims)
assert all(i['kind'] in {'conjecture','unproved claim','unpursued implication','idea of the earlier run','reading question','self-flagged step','withdrawn in the same text','title, date or page count','other'} for i in items)
assert all(c['fate'].strip() and c['fate_date'].strip() for c in claims)
assert all(c['id'] in {r['claim_ids'] for r in searches if r['search_id'].startswith('A-FATE-')} for c in claims)
assert itemids|claimids|refs <= {e['statement_id'] for e in events}
allowed={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
assert all(e['type'] in allowed for e in events)
for c in claims:
 for key in ['program','output','proof']:
  if key in c['computation']:assert (WORK/c['computation'][key]).is_file(),(c['id'],key)
assert len(readings)==30 and all(set(r)=={'cote','scan','line','reading','alternative','evidence','weight','confidence'} for r in readings)
assert len(links)==17 and all(set(r)=={'kind','from','to','what','evidence','note_ids'} for r in links)
assert all(r['kind'] in {'folder','published work','our projects'} for r in links)
assert len(re.findall(r'^## \d+\.',(OUT/'directions.md').read_text(),flags=re.M))==9
assert 'All asserted exact checks passed' in (WORK/'outputs/a_computations.txt').read_text()
assert not json.loads((OUT/'locator_audit.json').read_text())['issues'], 'A structured source locator is blank or out of bounds'
summary=dict(assigned_entries=160,reviewed_entries=len(entries),items=len(items),claims=len(claims),problems=len(problems),readings=len(readings),links=len(links),project_leads=sum(r['kind']=='our projects' for r in links),references=len(refs),directions=9,check_events=len(events),search_rows=len(searches),verdict_counts=dict(Counter(e['verdict'] for e in entries)),claim_classes=dict(Counter(c['class'] for c in claims)),claim_page_statuses=dict(Counter(c['status_on_pages'] for c in claims)),event_types=dict(Counter(e['type'] for e in events)),validation='All structural, exact index coverage and identifier/evidence-path checks passed. This is not an independent mathematical proof of the registered claims.')
(OUT/'validation.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
utc=sys.argv[1] if len(sys.argv)>1 else 'UTC timestamp not supplied'
with (OUT/'progress.log').open('a') as f:
 f.write(utc+'\tStages1–6 and evidence ledgers durable; structural validation completed. Counts:160 entries,110 items,80 claims,24 problems,30 readings,17 links,42 references,9 directions. The start/reading chronology is documented by the UTC-stamped read_source outputs; this completion record does not invent intermediate stage times.\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
