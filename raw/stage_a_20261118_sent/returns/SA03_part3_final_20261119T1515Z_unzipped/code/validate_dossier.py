"""Mechanical integrity checks after the human source and mathematical reviews."""
from pathlib import Path
import csv,json,re,collections
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'deliverable';SRC=ROOT/'source'
def js(n):return json.loads((OUT/n).read_text())
def tv(path):
    with path.open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
errors=[];warnings=[]
def check(condition,message):
    if not condition:errors.append(message)
items=js('SA03_items.json');claims=js('SA03_claims.json');problems=js('SA03_problems.json')
entries=tv(OUT/'SA03_entries.tsv');index=tv(SRC/'SA03_notes/NOTES_INDEX.tsv')
ids={x['id'] for x in items};cids={x['id'] for x in claims};pids={x['id'] for x in problems}
entry_ids=[x['entry_id'] for x in entries];index_ids=[x['entry_id'] for x in index]
check(len(entries)==321,'Expected 321 verdict rows')
check(collections.Counter(entry_ids)==collections.Counter(index_ids),'Verdict IDs differ from NOTES_INDEX')
check(len(set(entry_ids))==len(entry_ids),'Duplicate verdict ID')
check(len(ids)==len(items) and len(cids)==len(claims) and len(pids)==len(problems),'Duplicate object ID')
valid_verdicts={'kept','merged','corrected','withdrawn','rests on a misreading'}
valid_checks={'agrees','overstates','understates','misreads','not on the page'}
valid_kinds={'conjecture','unproved claim','unpursued implication','idea of the earlier run','reading question','self-flagged step','withdrawn in the same text','title, date or page count','other'}
expected={
 'item':set('id sources kind cote scans lines his_words statement reconstruction check check_reason'.split()),
 'claim':set('id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split()),
 'problem':set('id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split())}
bib=(OUT/'SA03_references.bib').read_text()
bibkeys=re.findall(r'@\w+\s*\{\s*([^,\s]+)\s*,',bib)
check(len(bibkeys)==len(set(bibkeys)),'Duplicate BibTeX key')
refs=set(bibkeys)
for match in re.finditer(r'@\w+\s*\{\s*([^,\s]+)\s*,',bib):
    start=match.start();end=bib.find('\n@',match.end());end=len(bib) if end<0 else end
    body=bib[start:end]
    check(bool(re.search(r'\bnote\s*=\s*\{(?:verified|unverified)\}',body,re.I)),f'Reference lacks exact verification note: {match.group(1)}')
for row in entries:
    check(row['item_id'] in ids,f'Entry missing item: {row["entry_id"]}')
    check(row['verdict'] in valid_verdicts,f'Unknown verdict: {row["entry_id"]}: {row["verdict"]}')
    check(bool(row['reason']),f'Empty verdict reason: {row["entry_id"]}')
item_by_id={x['id']:x for x in items}
indexed_source_uses=collections.Counter(s for x in items for s in x['sources'] if s in set(index_ids))
check(indexed_source_uses==collections.Counter(index_ids),'Indexed note sources are not attached to exactly one canonical item each')
for row in entries:
    if row['item_id'] in ids:check(row['entry_id'] in item_by_id[row['item_id']]['sources'],f'Entry not in item sources: {row["entry_id"]}')
lengths={}
scan_rows=tv(OUT/'SCAN_LOCATORS.tsv')
def validate_locs(rid,locations):
    touched=set()
    for loc in locations:
        check(isinstance(loc,dict) and {'file','start','end'}<=loc.keys(),f'{rid}: unparsed locator {loc}')
        if isinstance(loc,dict) and 'file' in loc:
            path=SRC/loc['file'];check(path.exists(),f'{rid}: missing source {loc["file"]}')
            if path.exists():
                if str(path) not in lengths:lengths[str(path)]=len(path.read_text().splitlines())
                check(1<=loc['start']<=loc['end']<=lengths[str(path)],f'{rid}: out-of-bounds locator {loc}')
            for scan in scan_rows:
                if scan['file']==loc['file'] and int(scan['line_start'])<=loc['end'] and int(scan['line_end'])>=loc['start']:
                    touched.add((int(scan['cote']),int(scan['scan'])))
    return touched
for family,records in [('item',items),('claim',claims),('problem',problems)]:
    for row in records:
        rid=row['id'];check(set(row)==expected[family],f'{rid}: schema keys differ')
        if family=='item':
            check(row['check'] in valid_checks,f'{rid}: unknown textual check')
            check(row['kind'] in valid_kinds,f'{rid}: unknown item kind')
        if family=='claim':
            check(row['class'] in set('ABCDEF'),f'{rid}: unknown class')
            check(row['confidence'] in {'high','medium','low'},f'{rid}: unknown confidence')
            for i in row['items']:check(i in ids,f'{rid}: missing item {i}')
            for field in ['statement','status_on_pages','computation','fate','fate_date','present_status']:
                check(bool(row[field]),f'{rid}: empty {field}')
        for key in row.get('refs',[]):check(key in refs,f'{rid}: missing reference {key}')
        touched=validate_locs(rid,row.get('lines',[]))
        if row.get('lines'):
            for scan in row.get('scans',[]):
                if (row['cote'],scan) not in touched:warnings.append(f'{rid}: named scan {row["cote"]}/{scan} has no overlap with the supplied line ranges')
        for occurrence in row.get('occurrences',[]):
            if occurrence.get('item'):check(occurrence['item'] in ids,f'{rid}: missing occurrence item {occurrence["item"]}')
            if occurrence.get('claim'):check(occurrence['claim'] in cids,f'{rid}: missing occurrence claim {occurrence["claim"]}')
            validate_locs(rid+' occurrence',occurrence.get('lines',[]))
events=tv(OUT/'CHECK_EVENTS.tsv');event_ids={x['statement_id'] for x in events}
for rid in ids|cids|refs:check(rid in event_ids,f'Missing check event: {rid}')
allowed_events={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found'}
for row in events:
    check(row['type'] in allowed_events or row['type'].startswith('refuted'),f'Unknown check-event type {row["type"]}')
    check(bool(row['who']) and 'GPT-6' in row['who'],f'Missing model identity in event {row["statement_id"]}')
for x in tv(OUT/'SA03_links.tsv'):
    check(x['kind'] in {'folder','published work','our projects'},'Unknown confirmed-link kind')
    check(x['kind']!='our projects','Unverified project lead entered confirmed-link table')
for name in ['SA03_dossier.md','SA03_directions.md','REFERENCE_POLICY.md','README.md']:
    check((OUT/name).exists(),f'Missing final document {name}')
alias_rows=tv(OUT/'ID_ALIASES.tsv')
aliases={x['retired_id']:x['canonical_id'] for x in alias_rows}
def canonical(rid):
    seen=set()
    while rid in aliases:
        check(rid not in seen,'Cyclic alias '+rid)
        if rid in seen:break
        seen.add(rid);rid=aliases[rid]
    return rid
all_ids=ids|cids|pids
for row in alias_rows:check(canonical(row['canonical_id']) in all_ids,'Alias has no canonical target '+row['retired_id'])
for name in ['SA03_dossier.md','SA03_directions.md']:
    document=(OUT/name).read_text()
    check(not re.search(r'<!--\s*(?:FINAL_CENSUS|ADDITIONAL_DIRECTIONS)',document),f'{name}: unfinished placeholder')
    for rid in re.findall(r'(?<![A-Za-z0-9-])(?:MP-SA03-\d+|CL-SA03-\d+|SA03-\d+)(?!\d)',document):
        check(canonical(rid) in all_ids,f'{name}: missing record {rid}')
    for key in re.findall(r'(?<![A-Za-z0-9_])(?:A2?|B2?|C2?|D)_[A-Za-z0-9_]+',document):
        check(key in refs,f'{name}: missing bibliography key {key}')
directions=re.split(r'^## (\d+)\. ',(OUT/'SA03_directions.md').read_text(),flags=re.M)
numbers=[]
for i in range(1,len(directions),2):
    numbers.append(int(directions[i]));body=directions[i+1]
    for pattern,label in [(r'(?<![A-Za-z0-9-])SA03-\d+','item'),(r'CL-SA03-\d+','claim'),(r'MP-SA03-\d+','problem')]:
        check(bool(re.search(pattern,body)),f'Direction {directions[i]} lacks {label} anchor')
check(numbers==list(range(1,len(numbers)+1)),'Direction ranks are not consecutive and unique')
status=js('outputs/consolidation_status.json')
check(not status['missing_part_files'],'Part files not yet complete: '+str(status['missing_part_files']))
check(not status['unparsed_locators'],'Unparsed locators remain')
if (OUT/'CLAIM_SEARCH_COVERAGE.tsv').exists():
    search=tv(OUT/'CLAIM_SEARCH_COVERAGE.tsv');search_ids={x['claim_id'] for x in search}
    for rid in cids:check(rid in search_ids,f'Missing search coverage {rid}')
    searched_ids={x['claim_id'] for x in search if x['search_log_present']=='True'}
    for rid in cids:check(rid in searched_ids,f'Missing actual search log {rid}')
else:errors.append('Missing claim search coverage table')
if (OUT/'STATUS_GROUPS.tsv').exists():
    groups=tv(OUT/'STATUS_GROUPS.tsv')
    check({x['claim_id'] for x in groups}==cids,'Status census does not cover exactly the canonical claims')
    check(not any(x['status_group']=='REVIEW REQUIRED' for x in groups),'Status census has unreviewed classifications')
for part in ['a','b','c','d','a2','b2','c2']:
    for name in ['items.json','claims.json','problems.json','readings.tsv','links.tsv','references.bib','CHECK_EVENTS.tsv','search_log.tsv','narrative.md','directions.md']:
        check((OUT/'parts'/part/name).exists(),f'Missing completed part artifact: {part}/{name}')
report=dict(errors=errors,warnings=warnings,counts=dict(entries=len(entries),items=len(items),claims=len(claims),problems=len(problems),references=len(refs),check_events=len(events)),
    check_scope='Schema, canonical IDs and aliases, source byte bounds and scan alignment, exact-once indexed-entry coverage, reference keys, event presence, actual search-log presence, authored census groups, direction anchors and completed-part artifact presence. This validator does not prove any mathematics or certify that a page was read.')
(OUT/'outputs/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
