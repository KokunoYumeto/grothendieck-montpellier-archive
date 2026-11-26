"""Validate delivery structure and referential integrity, not mathematical truth."""
import csv,json,re,sys,hashlib
from collections import Counter
from pathlib import Path
R=Path(__file__).resolve().parents[1]
SRC=R.parent/'source'
errors=[]
def require(ok,msg):
    if not ok:errors.append(msg)
def read_tsv(path):
    with path.open() as f:return list(csv.DictReader(f,delimiter='\t'))
expected=read_tsv(SRC/'SA27_notes/NOTES_INDEX.tsv')
entries=read_tsv(R/'SA27_entries.tsv')
items=json.loads((R/'SA27_items.json').read_text())
claims=json.loads((R/'SA27_claims.json').read_text())
problems=json.loads((R/'SA27_problems.json').read_text())
refinements=json.loads((R/'research/modern_refinements.json').read_text())
context_questions=json.loads((R/'research/context_questions.json').read_text())
modern_questions=json.loads((R/'research/modern_questions.json').read_text())
events=read_tsv(R/'CHECK_EVENTS.tsv')
links=read_tsv(R/'SA27_links.tsv')
readings=read_tsv(R/'SA27_readings.tsv')
schemas={
 'items':('id sources kind cote scans lines his_words statement reconstruction check check_reason').split(),
 'claims':('id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence').split(),
 'problems':('id title occurrences as_he_states plausible_today state_of_art why_open worth refs').split()}
for name,data in [('items',items),('claims',claims+refinements),('problems',problems+context_questions+modern_questions)]:
    ids=[v['id'] for v in data]
    require(len(ids)==len(set(ids)),f'duplicate {name} ids')
    for v in data:require(set(schemas[name])<=set(v),f'{v["id"]}: missing required fields')
eids=[e['entry_id'] for e in entries]
require(Counter(eids)==Counter(e['entry_id'] for e in expected),'entries do not cover the exact source index once')
iids={i['id'] for i in items};cids={c['id'] for c in claims+refinements};pids={p['id'] for p in problems+context_questions+modern_questions}
source_mapping={s:i['id'] for i in items for s in i['sources']}
require(len(source_mapping)==sum(len(i['sources']) for i in items),'an entry belongs to more than one item')
require(set(source_mapping)==set(eids),'item sources do not equal verdict-entry set')
verdicts={'kept','merged','corrected','withdrawn','rests on a misreading'}
checks={'agrees','overstates','understates','misreads','not on the page'}
for e in entries:
    require(e['item_id'] in iids,f'{e["entry_id"]}: missing item')
    require(source_mapping.get(e['entry_id'])==e['item_id'],f'{e["entry_id"]}: inconsistent item mapping')
    require(e['verdict'] in verdicts,f'{e["entry_id"]}: invalid verdict {e["verdict"]}')
    require(bool(e['reason'].strip()),f'{e["entry_id"]}: empty reason')
for i in items:
    require(bool(re.fullmatch(r'SA27-\d+',i['id'])),f'{i["id"]}: invalid item id')
    require(i['check'] in checks,f'{i["id"]}: invalid text-check label')
search_rows=[];search_locations={}
for path in [R/'research/root_search_log.tsv']+sorted((R/'work').glob('*/*search_log.tsv')):
    for row in read_tsv(path):
        sid=row['search_id'];relative=str(path.relative_to(R))
        require(sid not in search_locations or search_locations[sid]==relative,f'search namespace collision: {sid}')
        search_locations[sid]=relative;search_rows.append(row)
search_ids={q['search_id'] for q in search_rows}
search_members={}
for row in search_rows:
    search_members.setdefault(row['search_id'],set()).update(
        re.findall(r'SA27-C\d+',row.get('claim_ids',row.get('claim_id',''))))
for c in claims+refinements:
    require(set(c['items'])<=iids,f'{c["id"]}: missing item reference')
    require(c['class'] in 'ABCDEF' and len(c['class'])==1,f'{c["id"]}: invalid literature class')
    require(bool(c['fate']),f'{c["id"]}: no literature fate')
    require(bool(c['present_status']),f'{c["id"]}: no present status')
    require(bool(c.get('search_ids')),f'{c["id"]}: no mapped literature search record')
    require(set(c.get('search_ids',[]))<=search_ids,f'{c["id"]}: search id not present in an actual ledger')
    for sid in c.get('search_ids',[]):
        if search_members.get(sid):
            require(c['id'] in search_members[sid],f'{c["id"]}: ledger {sid} names other claims only')
for c in claims:require('modern' not in c.get('origin','').lower(),f'{c["id"]}: modern refinement counted as authorial')
page_statuses={'proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages'}
for c in claims:require(c.get('page_status_group') in page_statuses,f'{c["id"]}: missing or invalid manually assigned page-status group')
for p in problems+context_questions+modern_questions:
    require(bool(re.fullmatch(r'MP-SA27-\d+',p['id'])),f'{p["id"]}: invalid problem id')
    require(bool(p['state_of_art']),f'{p["id"]}: no state of art')
    for occurrence in p['occurrences']:
        if isinstance(occurrence,dict) and 'item' in occurrence:
            require(occurrence['item'] in iids,f'{p["id"]}: missing occurrence item {occurrence["item"]}')
for l in links:
    require(l['kind'] in {'folder','published work','our projects'},'invalid link kind')
    for sid in re.findall(r'MPL_(?:108\+112\+113\+114\+115|116\+117|118)#\d+',l['note_ids']):
        require(sid in source_mapping,f'link cites missing source entry {sid}')
bib=(R/'SA27_references.bib').read_text()
bibkeys=re.findall(r'@\w+\{([^,]+),',bib)
require(len(bibkeys)==len(set(bibkeys)),'duplicate bibliography keys')
used=set()
for v in claims+refinements+problems+context_questions+modern_questions:
    for ref in v['refs']:
        key=ref['key'] if isinstance(ref,dict) else ref
        used.add(key);require(key in bibkeys,f'{v["id"]}: missing bib key {key}')
event_ids={e['statement_id'] for e in events}
for k in iids|cids|used|set(bibkeys):require(k in event_ids,f'{k}: no check event')
for event in events:
    require(bool(event['who'].strip()),'event actor missing')
    typ=event['type']
    require(typ in {'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found'} or typ.startswith('refuted'),f'invalid check-event type {typ}')
for match in re.finditer(r'(?ms)^@\w+\{([^,]+),(.*?)(?=^@|\Z)',bib):
    require(bool(re.search(r'\bnote\s*=\s*\{(?:verified|unverified)\}',match.group(2))),f'{match.group(1)}: reference note must mark verified/unverified')
for path in ['SA27_dossier.md','SA27_directions.md','progress.log']:
    require((R/path).is_file(),f'missing {path}')
page_map=json.loads((R/'work/page_map.json').read_text())
expected_pages={(str(q['cote']),int(q['scan'])) for q in page_map}
page_reads=[]
for path in (R/'work').glob('*/page_read_log.tsv'):
    page_reads.extend(read_tsv(path))
read_pages=[(str(q['cote']),int(q['scan'])) for q in page_reads]
require(len(read_pages)==len(set(read_pages)),'duplicate page-read records')
require(set(read_pages)==expected_pages,'page-read logs do not cover exactly the supplied scan blocks')
inventory=json.loads((R/'work/source_inventory.json').read_text())
for meta in inventory:
    p=R.parent/meta['path']
    require(hashlib.sha256(p.read_bytes()).hexdigest()==meta['sha256'],f'source changed: {meta["path"]}')
summary={'entries':len(entries),'items':len(items),'claims':len(claims),'problems':len(problems),
 'modern_refinements':len(refinements),'historical_editorial_questions':len(context_questions),
 'modern_audit_questions':len(modern_questions),
 'readings':len(readings),'links':len(links),'references':len(bibkeys),'check_events':len(events),
 'reference_verification_marks':dict(Counter(re.findall(r'\bnote\s*=\s*\{(verified|unverified)\}',bib))),
 'scan_blocks':len(expected_pages),'page_read_records':len(read_pages),
 'verdicts':dict(Counter(e['verdict'] for e in entries)),
 'item_kinds':dict(Counter(i['kind'] for i in items)),
 'claim_classes':dict(Counter(c['class'] for c in claims)),
 'claim_statuses':dict(Counter(c['status_on_pages'] for c in claims)),
 'claim_status_groups':dict(Counter(c.get('page_status_group','missing') for c in claims)),
 'link_kinds':dict(Counter(l['kind'] for l in links)),
 'search_records':len(search_ids),'search_ledger_rows':len(search_rows),
 'errors':errors,'validation_scope':'Structural integrity, exact source-index coverage, and source immutability. Not a substitute for recorded close readings, proof checks, or literature matching.'}
print(json.dumps(summary,ensure_ascii=False,indent=2))
sys.exit(bool(errors))
