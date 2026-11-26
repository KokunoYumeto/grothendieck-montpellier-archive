"""Serialize the reviewed part dossiers; this script makes no source verdicts.

All mathematical judgments are authored in parts/* and in the explicit merge
and link-review tables. The script normalizes locators, applies approved aliases,
and checks referential integrity. It never alters a supplied transcription.
"""
from pathlib import Path
import csv, json, re, collections, hashlib, zipfile

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'deliverable'
SOURCE = ROOT / 'source'
PART_NAMES = ['a', 'b', 'c', 'd', 'a2', 'b2', 'c2']
ITEM_FIELDS = 'id sources kind cote scans lines his_words statement reconstruction check check_reason'.split()
CLAIM_FIELDS = 'id items cote scans lines his_statement statement status_on_pages computation class fate fate_date present_status refs confidence'.split()
PROBLEM_FIELDS = 'id title occurrences as_he_states plausible_today state_of_art why_open worth refs'.split()
LINK_FIELDS = ['kind','from','to','what','evidence','note_ids']
unparsed = []

def read_json(path, default=None):
    return json.loads(path.read_text()) if path.exists() else default

def read_tsv(path):
    if not path.exists(): return []
    with path.open(newline='') as f: return list(csv.DictReader(f, delimiter='\t'))

def write_json(name, value):
    (OUT/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

def write_tsv(name, fields, rows):
    with (OUT/name).open('w', newline='') as f:
        w=csv.DictWriter(f, fieldnames=fields, delimiter='\t', extrasaction='ignore')
        w.writeheader();w.writerows(rows)

def unique(values):
    seen=set();answer=[]
    for value in values:
        key=json.dumps(value, sort_keys=True, ensure_ascii=False)
        if key not in seen:seen.add(key);answer.append(value)
    return answer

def clean_path(path):
    path=str(path)
    if '/source/' in path:path=path.split('/source/',1)[1]
    return path.removeprefix('source/')

def line_ranges(value, owner=''):
    if value is None:return []
    if isinstance(value,dict):
        if {'file','start','end'}<=value.keys():
            return [dict(file=clean_path(value['file']),start=int(value['start']),end=int(value['end']))]
        unparsed.append(dict(owner=owner,locator=value));return [value]
    if isinstance(value,list):return unique([y for x in value for y in line_ranges(x,owner)])
    result=[];current=None
    for segment in re.split(r';\s*',str(value)):
        m=re.search(r'((?:source/)?SA03_(?:texts|notes)/[^\s:]+\.(?:tex|md))\s*:\s*(.*)',segment)
        if m:current=clean_path(m.group(1));tail=m.group(2)
        elif current and re.fullmatch(r'[L\d\s,–—-]+',segment):tail=segment
        else:
            unparsed.append(dict(owner=owner,locator=segment));result.append(dict(locator=segment));continue
        found=False
        for r in re.finditer(r'L?(\d+)\s*(?:[-–—]\s*L?(\d+))?',tail):
            result.append(dict(file=current,start=int(r.group(1)),end=int(r.group(2) or r.group(1))));found=True
        if not found:unparsed.append(dict(owner=owner,locator=segment));result.append(dict(locator=segment))
    return unique(result)

def numeric_id(value):return int(re.search(r'(\d+)$',value).group(1))

def joins(first, second):
    if first==second or not second:return first
    if not first:return second
    return first+'\n\nAdditional occurrence: '+second

parts={name:OUT/'parts'/name for name in PART_NAMES}
items={};claims={};problems={};entries=[];events=[];readings=[];ownership=[]
missing=[]
for name,folder in parts.items():
    for filename,target in [('items.json',items),('claims.json',claims),('problems.json',problems)]:
        data=read_json(folder/filename)
        if data is None:missing.append(str((folder/filename).relative_to(OUT)));continue
        for record in data:
            assert record['id'] not in target,record['id']
            if 'cote' in record:record['cote']=int(record['cote'])
            if 'lines' in record:record['lines']=line_ranges(record['lines'],record['id'])
            if 'scans' in record:record['scans']=sorted(set(map(int,record['scans'])))
            target[record['id']]=record
            ownership.append(dict(record_id=record['id'],part=name,source_file='parts/'+name+'/'+filename))
    entries+=read_tsv(folder/'entries.tsv')
    events+=read_tsv(folder/'CHECK_EVENTS.tsv')
    readings+=read_tsv(folder/'readings.tsv')

aliases={};merge_log=[]
for update in read_json(OUT/'PROBLEM_AUGMENTS.json',[]):
    record=problems[update['id']]
    for key in ['occurrences','refs']:record[key]=unique(record[key]+update.get(key,[]))
    record.update(update.get('overrides',{}))
for family,target,filename,union_fields,prose_fields in [
    ('item',items,'ITEM_MERGES.json',['sources','scans','lines'],['his_words','statement','reconstruction','check_reason']),
    ('claim',claims,'CLAIM_MERGES.json',['items','scans','lines','refs'],['his_statement','statement','computation','fate','fate_date','present_status']),
    ('problem',problems,'PROBLEM_MERGES.json',['occurrences','refs'],['as_he_states','plausible_today','state_of_art','why_open','worth'])]:
    for rule in read_json(OUT/filename,[]):
        old,new=rule['from'],rule['to']
        assert old in target and new in target,(family,old,new)
        assert old not in aliases
        a,b=target[new],target[old]
        for key in union_fields:a[key]=unique(a.get(key,[])+b.get(key,[]))
        for key in prose_fields:a[key]=joins(a.get(key,''),b.get(key,''))
        for key,value in rule.get('overrides',{}).items():a[key]=value
        if family=='item':
            assert {'kind','check'}<=rule.get('overrides',{}).keys(), 'Each item merge needs a reviewed kind/check'
            a['check_reason']+='\n\nConsolidation: '+rule['reason']
        aliases[old]=new;del target[old]
        merge_log.append(dict(kind=family,retired_id=old,canonical_id=new,reason=rule['reason']))

def canonical(x):
    seen=set()
    while x in aliases:
        assert x not in seen;seen.add(x);x=aliases[x]
    return x

id_pattern=re.compile(r'(?<![A-Za-z0-9-])(?:MP-SA03-\d+|CL-SA03-\d+|SA03-\d+)(?!\d)')
def rewrite(value):
    if isinstance(value,str):return id_pattern.sub(lambda m:canonical(m.group()),value)
    if isinstance(value,list):return [rewrite(x) for x in value]
    if isinstance(value,dict):return {k:rewrite(v) for k,v in value.items()}
    return value

scan_rows=read_tsv(OUT/'SCAN_LOCATORS.tsv')
def occurrence_record(value, owner):
    record=dict(value) if isinstance(value,dict) else {'source_locator':value,'lines':value}
    record['lines']=line_ranges(record.get('lines',[]),owner)
    touched=[]
    for loc in record['lines']:
        if 'file' not in loc:continue
        for scan in scan_rows:
            if loc['file']==scan['file'] and int(scan['line_start'])<=loc['end'] and int(scan['line_end'])>=loc['start']:
                touched.append((int(scan['cote']),int(scan['scan'])))
    if 'cote' in record:record['cote']=int(record['cote'])
    elif touched:record['cote']=touched[0][0]
    elif record.get('item') in items:record['cote']=items[record['item']]['cote']
    record['scans']=sorted(set(map(int,record.get('scans',[]))) if 'scans' in record else {n for _,n in touched})
    return record

for row in entries:
    old=row['item_id'];row['item_id']=canonical(old)
    if old!=row['item_id']:
        row['reason']+=' Cross-package consolidation: '+old+' is represented by '+row['item_id']+'.'
        if row['verdict']=='kept':row['verdict']='merged'
    if row['verdict'].startswith('merged'):row['verdict']='merged'
for row in events:
    old=row['statement_id'];row['statement_id']=canonical(old)
    if old!=row['statement_id']:row['outcome']='Original audit record '+old+'; canonical record '+row['statement_id']+'. '+row['outcome']

for family,target,fields,filename in [
    ('item',items,ITEM_FIELDS,'SA03_items.json'),
    ('claim',claims,CLAIM_FIELDS,'SA03_claims.json'),
    ('problem',problems,PROBLEM_FIELDS,'SA03_problems.json')]:
    result=[]
    for x in sorted(target.values(),key=lambda z:numeric_id(z['id'])):
        x=rewrite(x)
        if family=='problem':x['occurrences']=[occurrence_record(y,x['id']) for y in x['occurrences']]
        for key in ['sources','items','refs','scans','lines','occurrences']:
            if key in x and isinstance(x[key],list):x[key]=unique(x[key])
        result.append({k:x[k] for k in fields})
    write_json(filename,result)
write_tsv('SA03_entries.tsv',['entry_id','item_id','verdict','reason'],entries)
write_tsv('SA03_readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],unique(readings))
write_tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
write_tsv('ID_ALIASES.tsv',['kind','retired_id','canonical_id','reason'],merge_log)
write_tsv('RECORD_ORIGINS.tsv',['record_id','part','source_file'],ownership)

# Only explicitly reviewed two-endpoint links enter the main link table.
link_reviews=read_json(OUT/'LINK_REVIEW.json',{})
links=[];leads=[];projects=[]
for name,folder in parts.items():
    for i,row in enumerate(read_tsv(folder/'links.tsv'),1):
        decision=link_reviews.get(name+':'+str(i),{})
        original=dict(row)
        if row['kind']=='our projects':projects.append(row);continue
        if decision.get('disposition')=='lead':leads.append(row);continue
        if decision.get('keep_original_as_lead'):leads.append(original)
        row.update(decision.get('overrides',{}));links.append(row)
    for filename in ['link_leads.tsv','project_leads.tsv','projects.tsv']:
        for row in read_tsv(folder/filename):
            (projects if row.get('kind')=='our projects' else leads).append(row)
write_tsv('SA03_links.tsv',LINK_FIELDS,unique(rewrite(links)))
write_tsv('SA03_link_leads.tsv',LINK_FIELDS,unique(rewrite(leads)))
write_tsv('SA03_project_leads.tsv',LINK_FIELDS,unique(rewrite(projects)))

# Prefixes preserve which inspector verified each bibliographical record.
bib=['% SA03 part 3. See REFERENCE_POLICY.md for verification scopes.\n']
for name,folder in parts.items():
    p=folder/'references.bib'
    if p.exists():bib+=['\n% Source part '+name+'\n',p.read_text()]
(OUT/'SA03_references.bib').write_text(''.join(bib))
write_json('outputs/consolidation_status.json',dict(parts=PART_NAMES,missing_part_files=missing,unparsed_locators=unparsed,
    counts=dict(entries=len(entries),items=len(items),claims=len(claims),problems=len(problems),readings=len(unique(readings)),
    confirmed_links=len(unique(links)),link_leads=len(unique(leads)),project_leads=len(unique(projects)),events=len(events)),
    verdicts=dict(collections.Counter(x['verdict'] for x in entries)),classes=dict(collections.Counter(x['class'] for x in claims.values()))))
print(json.dumps(read_json(OUT/'outputs/consolidation_status.json'),ensure_ascii=False,indent=2))
