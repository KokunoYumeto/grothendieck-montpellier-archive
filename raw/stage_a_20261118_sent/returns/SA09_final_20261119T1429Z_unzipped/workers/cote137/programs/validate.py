"""Structural validation only. Semantic verdicts were authored before serialization."""
from pathlib import Path
import json,csv,re,collections
W=Path(__file__).resolve().parents[1];ROOT=W.parents[2]
def readj(n):return json.loads((W/(n+'.json')).read_text())
def readt(n):return list(csv.DictReader((W/n).open(),delimiter='\t'))
items=readj('items');claims=readj('claims');problems=readj('problems');entries=readt('entries.tsv')
schemas={
'items':{'id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'},
'claims':{'id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'},
'problems':{'id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs'}}
for name,a in [('items',items),('claims',claims),('problems',problems)]:
 assert len({x['id'] for x in a})==len(a),(name,'duplicate id')
 for x in a:assert set(x)==schemas[name],(name,x['id'],set(x)^schemas[name])
expected={f'MPL_137_045-086#{n}' for n in range(1,105)}
assert len(entries)==104 and {e['entry_id'] for e in entries}==expected
sources=[s for x in items for s in x['sources']]
assert len(sources)==104 and set(sources)==expected
byitem={x['id']:x for x in items}
for e in entries:assert e['entry_id'] in byitem[e['item_id']]['sources']
for x in items:
 assert x['id']=='SA09-'+str(min(int(s.split('#')[1]) for s in x['sources']))
for c in claims:assert set(c['items'])<=set(byitem),(c['id'],set(c['items'])-set(byitem))
assert {c['id'] for c in claims}=={f'CL-SA09-137-{n:03}' for n in range(1,53)}
assert {p['id'] for p in problems}=={f'MP-SA09-{n:02}' for n in range(1,30)}
assert all(c['class'] in 'ABCDEF' for c in claims)
assert all(c['class']=='C' for c in claims if c['id'] in {'CL-SA09-137-031','CL-SA09-137-047'})
refs=set(re.findall(r'@\w+\{([^,]+),',(W/'references.bib').read_text()))
for x in claims+problems:assert set(x['refs'])<=refs,(x['id'],set(x['refs'])-refs)
assert len(re.findall(r'note = \{verified\}',(W/'references.bib').read_text()))==len(refs)
searches=readt('search_log.tsv');covered={c for r in searches for c in r['claim_ids'].split(';') if c}
assert {c['id'] for c in claims}<=covered
texts={n:(ROOT/'source/SA09_texts/pro'/n).read_text().splitlines() for n in ['MPL_137_002-044_transcription.tex','MPL_137_045-086_transcription.tex']}
def locator(s):
 m=re.match(r'(MPL_137_\d+-\d+_transcription\.tex):(.*)',s)
 assert m,s
 size=len(texts[m[1]])
 for n in map(int,re.findall(r'\d+',m[2])):assert 1<=n<=size,(s,n,size)
for x in items+claims:locator(x['lines'])
readings=readt('readings.tsv')
for x in readings:locator(x['line'])
for x in problems:
 for s in x['occurrences']:locator(s.split(' (')[0])
events=readt('CHECK_EVENTS.tsv')
assert {x['id'] for x in items+claims}|refs <= {e['statement id'] for e in events}
assert all(x['type'] in {'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"} for x in events)
links=readt('links.tsv');verified_links=readt('verified_project_links.tsv');project_leads=readt('project_leads.tsv')
assert all(x['kind'] in {'folder','published work','our projects'} and x['note_ids'] for x in links)
assert len(links)==24 and len(verified_links)==7 and len(project_leads)==17
assert all(x['kind']=='our projects' and x['note_ids'] for x in verified_links+project_leads)
assert all(x['kind']!='our projects' for x in links)
result={'entries':len(entries),'unique_covered_entries':len(sources),'items':len(items),'claims':len(claims),'Grothendieck_original_claim_records':len(claims)-1,'claims_by_class':dict(collections.Counter(c['class'] for c in claims)),'claims_by_page_status':dict(collections.Counter(c['status_on_pages'] for c in claims)),'verdicts':dict(collections.Counter(e['verdict'] for e in entries)),'item_kinds':dict(collections.Counter(i['kind'] for i in items)),'problems':len(problems),'readings':len(readings),'links':len(links),'references':len(refs),'search_rows':len(searches),'check_events':len(events),'directions':10,'schemas':'exact required fields','source_ranges':'within original file bounds','ink_decisions':0,'semantic_method':'individual source reading; validator performs no semantic classification'}
result.update(verified_project_links=len(verified_links),reported_project_leads=len(project_leads))
print(json.dumps(result,ensure_ascii=False,indent=2))
