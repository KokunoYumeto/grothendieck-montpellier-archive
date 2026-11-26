"""Meaningful completeness and referential-integrity checks for SA29 part2.

No manuscript verdict is inferred here. Source immutability is compared directly
with the already supplied archive without extracting it a second time.
"""
import csv,hashlib,importlib.metadata,json,re,sys,zipfile
from pathlib import Path
from collections import Counter,defaultdict
from datetime import datetime,timezone
W=Path(__file__).resolve().parents[1];BASE=W.parent
errors=[];warnings=[];checks={}
def check(label,condition,detail=None):
    checks[label]={'passed':bool(condition)}
    if detail is not None:checks[label]['detail']=detail
    if not condition:errors.append(label)
def readj(p):return json.loads(p.read_text())
def readt(p):
    with p.open(newline='')as f:return list(csv.DictReader(f,delimiter='\t'))
def writej(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')

schema={
'SA29_items.json':['id','sources','kind','cote','scans','lines','his_words','statement','reconstruction','check','check_reason'],
'SA29_claims.json':['id','items','cote','scans','lines','his_statement','statement','status_on_pages','computation','class','fate','fate_date','present_status','refs','confidence'],
'SA29_problems.json':['id','title','occurrences','as_he_states','plausible_today','state_of_art','why_open','worth','refs']}
data={}
for f,fields in schema.items():
    data[f]=readj(W/f)
    missing=[(x.get('id'),[k for k in fields if k not in x]) for x in data[f] if any(k not in x for k in fields)]
    check('required fields '+f,not missing,missing)
    check('unique IDs '+f,len(data[f])==len({x['id']for x in data[f]}))
    check('nonempty substantive fields '+f,all(str(x[k]).strip() for x in data[f]for k in fields if k not in ['scans','lines','his_words','his_statement','refs']))
items=data['SA29_items.json'];claims=data['SA29_claims.json'];problems=data['SA29_problems.json']
I={x['id']:x for x in items};C={x['id']:x for x in claims};P={x['id']:x for x in problems}
aliases=readj(W/'audit/id_aliases.json');all_alias={k:v for group in aliases.values() for k,v in group.items()}
editorial=readj(W/'audit/editorial_checks.json');refined=readj(W/'audit/refined_statements.json')
other={x['id']:x for x in editorial+refined}
check('auxiliary statement IDs are unique',len(other)==len(editorial)+len(refined))
entries=readt(W/'SA29_entries.tsv');index=readt(BASE/'sources/SA29_notes/NOTES_INDEX.tsv')
indexids=[x.get('entry_id',x.get('id'))for x in index]
check('380 entry verdicts',len(entries)==380==len({x['entry_id']for x in entries}))
check('entry IDs match source index',{x['entry_id']for x in entries}==set(indexids))
check('each source belongs to one consolidated item',Counter(s for x in items for s in x['sources'])==Counter(indexids))
check('entry targets resolve',all(x['item_id'] in I for x in entries))
check('entry and item provenance agree',all(x['entry_id'] in I[x['item_id']]['sources']for x in entries))
check('allowed verdicts',all(x['verdict']in{'kept','merged','corrected','withdrawn','rests on a misreading'}for x in entries))
check('allowed claim classes',all(x['class']in'ABCDEF'for x in claims))
check('claim item targets resolve',all(i in I for x in claims for i in x['items']))
check('allowed item checks',all(x['check']in{'agrees','overstates','understates','misreads','not on the page'}for x in items))
check('all claims dated in November2026',all('2026' in str(x['present_status']) for x in claims))
check('every problem has occurrences and a literature state',all(x['occurrences'] and x['state_of_art'] and x['refs']for x in problems))

bib=(W/'SA29_references.bib').read_text()
bibkeys=re.findall(r'^@\w+\{([^,]+),',bib,re.M);B=set(bibkeys)
check('unique bibliography keys',len(B)==len(bibkeys))
check('all cited claim/problem keys exist',all(k in B for x in claims+problems for k in x['refs']))
blocks=re.split(r'(?=^@\w+\{)',bib,flags=re.M)
check('bibliography verification tags',all(re.search(r'note\s*=\s*\{(?:un)?verified\}',b)for b in blocks if b.strip()))
verified_bibkeys={re.search(r'^@\w+\{([^,]+),',b).group(1)for b in blocks if b.strip() and re.search(r'note\s*=\s*\{verified\}',b)}
check('each problem cites an opened source',all(set(x['refs'])&verified_bibkeys for x in problems))
refchecks=readj(W/'audit/reference_checks.json');checkedkeys={x['key']for x in refchecks}
check('all bibliography keys have verification records',B<=checkedkeys,sorted(B-checkedkeys))

search=readt(W/'audit/search_log.tsv');searched=set()
for row in search:
    for sid in re.findall(r'C-SA29-\d+',row['claim_ids']):searched.add(all_alias.get(sid,sid))
check('every retained claim has a search ledger record',set(C)<=searched,sorted(set(C)-searched))
check('search records preserve actual query and result',all(x['query'].strip() and x['result'].strip()for x in search))

events=readt(W/'CHECK_EVENTS.tsv');valid_ids=set(I)|set(C)|set(P)|set(other)|B|set(all_alias)
unknown_event_ids=sorted({x['statement_id']for x in events}-valid_ids)
check('check-event statement IDs resolve',not unknown_event_ids,unknown_event_ids)
canonical_events={all_alias.get(x['statement_id'],x['statement_id'])for x in events}
check('every item has an actual check event',set(I)<=canonical_events,sorted(set(I)-canonical_events))
check('every retained claim has an actual check event',set(C)<=canonical_events,sorted(set(C)-canonical_events))
check('every used reference has an event',B<=canonical_events,sorted(B-canonical_events))
allowed_types={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found'}
badtypes=sorted({x['type']for x in events if x['type'] not in allowed_types and not x['type'].startswith('refuted')})
check('event types are actual allowed categories',not badtypes,badtypes)
unresolved_refutations=[]
for e in events:
    if e['type'].startswith('refuted'):
        ids=re.findall(r'C-SA29-\d+(?:-R\d*)?',e['type']+' '+e['outcome'])
        targets=[q for q in ids if q!=e['statement_id']]
        if not targets or not any(q in valid_ids for q in targets):unresolved_refutations.append(e)
check('refutations name a resolvable refined statement',not unresolved_refutations,[x['statement_id']for x in unresolved_refutations])

links=readt(W/'SA29_links.tsv');readings=readt(W/'SA29_readings.tsv')
check('allowed link kinds',all(x['kind']in{'folder','published work','our projects'}for x in links))
check('links retain evidence and endpoints',all(x['from'] and x['to'] and x['evidence']for x in links))
check('project leads are separately tabulated',readt(W/'SA29_project_links.tsv')==[x for x in links if x['kind']=='our projects'])
check('reading alarms retain alternatives and evidence',all(x['reading'] and x['alternative'] and x['evidence']for x in readings))
note_ids=[]
for x in links:note_ids.extend(re.findall(r'MPL_[A-Za-z0-9_+\-]+#\d+',x['note_ids']))
check('link note IDs exist',set(note_ids)<=set(indexids),sorted(set(note_ids)-set(indexids)))

direction=(W/'SA29_directions.md').read_text();sections=re.split(r'^## \d+\. ',direction,flags=re.M)[1:]
check('ranked directions have provenance and first steps',len(sections)==12 and all('**Sources:**'in s and 'C-SA29-'in s and 'MP-SA29-'in s and '**First concrete step.**'in s for s in sections))
explicit_ids=set(re.findall(r'(?<![A-Za-z0-9_-])(?:C-SA29-|MP-SA29-|SA29-)\d+(?:-R\d*)?',direction))
check('explicit direction IDs resolve',explicit_ids<=valid_ids,sorted(explicit_ids-valid_ids))
body=(W/'SA29_dossier.md').read_text()
unresolved_text_ids=[]
for name,contents in [('dossier',body),('directions',direction)]:
    for m in re.finditer(r'(?<![A-Za-z0-9_-])((?:C-|MP-)?SA29-)(\d+)(?:[–-](\d+))?',contents):
        prefix,a,b=m.groups()
        for n in range(int(a),int(b or a)+1):
            if not({prefix+str(n),prefix+str(n).zfill(2)}&valid_ids):unresolved_text_ids.append((name,m.group(),n))
check('overview and direction IDs including ranges resolve',not unresolved_text_ids,unresolved_text_ids)
check('dossier has final counts',not'{{COUNTS}}'in body and '## 7. Counts'in body)
check('no unfilled editorial placeholders',not re.search(r'\b(?:TODO|TBD|FIXME|PLACEHOLDER)\b',body+'\n'+direction))

# Verify the actual supplied bytes without a second extraction.
archive=BASE/'upload/SA29_Autour_de_La_Longue_Marche_travers_la_th_part2.zip'
source_records=[]
with zipfile.ZipFile(archive)as z:
    names=z.namelist()
    for p in sorted((BASE/'sources').rglob('*')):
        if not p.is_file():continue
        rel=p.relative_to(BASE/'sources').as_posix()
        matches=[n for n in names if n==rel or n.endswith('/'+rel)]
        if len(matches)!=1:source_records.append(dict(path=rel,error='archive member not unique',matches=matches));continue
        current=hashlib.sha256(p.read_bytes()).hexdigest();original=hashlib.sha256(z.read(matches[0])).hexdigest()
        source_records.append(dict(path=rel,archive_member=matches[0],sha256=current,original_sha256=original,unchanged=current==original))
check('all supplied source files unchanged',bool(source_records) and all(x.get('unchanged',False)for x in source_records),len(source_records))
writej(W/'audit/input_integrity.json',source_records)

# A requested-range audit is evidence of reading coverage, not an automated
# substitute for the saved individual textual judgments.
ledger=readj(W/'audit/source_read_ledger.json');coverage=[]
for p in sorted((BASE/'sources/SA29_texts/pro').glob('*_transcription.tex')):
    lines=p.read_text().splitlines();covered=set()
    for x in ledger:
        if x['path'].endswith(p.name):covered.update(range(max(1,x['start']),min(len(lines),x['end'])+1))
    uncovered=[i for i in range(1,len(lines)+1)if i not in covered]
    coverage.append(dict(file=p.name,total_lines=len(lines),requested_lines=len(covered),uncovered=uncovered))
check('transcription source-reading range coverage',all(not x['uncovered']for x in coverage),[{k:v for k,v in x.items()if k!='uncovered'}for x in coverage])
writej(W/'audit/source_read_coverage.json',coverage)

versions={'python':sys.version,'checked_utc':datetime.now(timezone.utc).isoformat()}
for name in ['sympy','requests','pypdf']:
    try:versions[name]=importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:versions[name]='not installed under this distribution name'
writej(W/'audit/runtime_versions.json',versions)
out={'checked_utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'errors':errors,'warnings':warnings,
     'counts':{'entries':len(entries),'items':len(items),'claims':len(claims),'problems':len(problems),'readings':len(readings),'links':len(links),'references':len(B),'events':len(events),'directions':len(sections)}}
writej(W/'audit/validation_output.json',out)
print(json.dumps({'errors':errors,'warnings':warnings,'counts':out['counts'],'checks':len(checks)},indent=2))
if errors:sys.exit(1)
