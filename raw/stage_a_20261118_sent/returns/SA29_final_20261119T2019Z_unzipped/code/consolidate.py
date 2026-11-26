"""Apply explicit, source-read consolidation decisions and build final registers.

This program performs bookkeeping only. All textual judgments are authored in
the package records and merge_decisions.py. It neither reads headings to assign
verdicts nor infers mathematics from keyword matches.
"""
import copy,csv,importlib.util,json,re
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
W=Path(__file__).resolve().parents[1]
REVIEWS=['review_A','review_B','review_C','review_R']
REF_ALIASES={'Serre1977':'SerreTrees1977','JonesOperations':'JonesOperations1985','Grothendieck1984Esquisse':'GrothendieckEsquisse1984'}
spec=importlib.util.spec_from_file_location('decisions',W/'code/merge_decisions.py')
D=importlib.util.module_from_spec(spec);spec.loader.exec_module(D)

def readjson(p):return json.loads(p.read_text())
def readtsv(p):
    with p.open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def writejson(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def writetsv(p,rows,fields):
    with p.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
def seq(x):return x if isinstance(x,list) else [x]
def unique(xs):
    seen=set();out=[]
    for x in xs:
        s=json.dumps(x,sort_keys=True,ensure_ascii=False)
        if s not in seen:out.append(x);seen.add(s)
    return out
def idkey(x):return int(x['id'].rsplit('-',1)[1])

required=['items.json','entries.tsv','claims.json','problems.json','readings.tsv','links.tsv','references.bib','reference_checks.json','search_log.tsv','CHECK_EVENTS.tsv']
missing=[str(W/r/f) for r in REVIEWS for f in required if not(W/r/f).exists()]
if missing:raise RuntimeError('Review registers still required: '+json.dumps(missing))

items={};claims={};origin={};entries=[];problems=[];readings=[];links=[];events=[];searches=[];reference_checks=[]
refinements=[];editorial=[]
for r in REVIEWS:
    p=W/r
    for f,target in [('items.json',items),('claims.json',claims)]:
        for x in readjson(p/f):
            assert x['id'] not in target,(r,x['id']);target[x['id']]=x;origin[x['id']]=r
    entries.extend(readtsv(p/'entries.tsv'))
    problems.extend(readjson(p/'problems.json'))
    readings.extend(readtsv(p/'readings.tsv'))
    links.extend(readtsv(p/'links.tsv'))
    events.extend(readtsv(p/'CHECK_EVENTS.tsv'))
    searches.extend(dict(row,review=r) for row in readtsv(p/'search_log.tsv'))
    for x in readjson(p/'reference_checks.json'):reference_checks.append(dict(x,review=r))
    for f,target in [('refined_statements.json',refinements),('editorial_checks.json',editorial)]:
        if(p/f).exists():
            for x in readjson(p/f):target.append(dict(x,review=r))

for x in list(claims.values())+problems+editorial+refinements:
    if 'refs'in x:x['refs']=unique(REF_ALIASES.get(k,k)for k in x['refs'])
for x in reference_checks:
    if x['key']in REF_ALIASES:x['original_key']=x['key'];x['key']=REF_ALIASES[x['key']]
for x in events:
    if x['statement_id']in REF_ALIASES:
        x['outcome']+=' Original bibliography key: '+x['statement_id']+'.'
        x['statement_id']=REF_ALIASES[x['statement_id']]
for x in links:
    for field in ['from','to','what','evidence']:
        for old,new in REF_ALIASES.items():x[field]=re.sub(r'(?<!\w)'+re.escape(old)+r'(?!\w)',new,x[field])
original_items=copy.deepcopy(items);original_claims=copy.deepcopy(claims)
for key in ['C-SA29-240','C-SA29-246']:
    refinements.append(dict(original_claims[key],attribution='Later manuscript normalization/correction, retained here as a separately addressable refined statement and consolidated into the original claim.'))
item_aliases={x:x for x in items};claim_aliases={x:x for x in claims}
problem_aliases={x['id']:x['id'] for x in problems}

def locations(x):
    c=unique(str(y) for y in seq(x.get('cote',[])))
    scans=[]
    for s in seq(x.get('scans',[])):
        if isinstance(s,str) and '/' in s:scans.append(s)
        elif len(c)==1:scans.append(c[0]+'/'+str(s))
        else:scans.append('cotes'+','.join(c)+'/scan'+str(s))
    ls=[]
    packages=unique(s.split('#')[0] for s in x.get('sources',[]))
    if not packages:
        for it in x.get('items',[]):
            packages.extend(s.split('#')[0] for s in original_items.get(it,{}).get('sources',[]))
        packages=unique(packages)
    for line in seq(x.get('lines',[])):
        if isinstance(line,str):
            line=re.sub(r'(?<!\w)(062-121|122-167):',r'MPL_144_\1_transcription.tex:',line)
            if 'transcription.tex' not in line and len(packages)==1:line=packages[0]+'_transcription.tex: '+line
        ls.append(line)
    return c,scans,ls

def merged_location(xs):
    locs=[locations(x) for x in xs]
    c=unique(y for z in locs for y in z[0])
    return dict(cote=c[0] if len(c)==1 else c,scans=unique(y for z in locs for y in z[1]),lines=unique(y for z in locs for y in z[2]))

merge_log=[]
for decision in D.ITEM_MERGES:
    key=decision['canonical'];members=decision['members'];xs=[items[m] for m in members]
    z=copy.deepcopy(items[key]);z.update(merged_location(xs));z['sources']=unique(s for x in xs for s in x['sources'])
    z['his_words']=' / '.join(x['his_words']+' ['+x['id']+']' for x in xs)
    for f in ['kind','statement','reconstruction','check','check_reason']:z[f]=decision[f]
    for m in members:item_aliases[m]=key;items.pop(m)
    items[key]=z;merge_log.append(dict(decision,record_type='item'))

for row in entries:
    old=row['item_id'];new=item_aliases[old]
    if old!=new:
        if row['verdict'] in ['kept','merged']:row['verdict']='merged'
        row['reason']+=' Cross-package consolidation: '+old+' → '+new+'; see audit/merge_decisions.json.'
    row['item_id']=new

def localfiles(text,r):
    if not isinstance(text,str):return text
    for name in ['computations.py','computations_output.json','proofs.md','proof_notes.md','calculation_notes.md','geometric_checks.py','geometric_checks_output.json']:
        text=re.sub(r'(?<![\w/])'+re.escape(name),r+'/'+name,text)
    return text

for x in claims.values():x['computation']=localfiles(x['computation'],origin[x['id']])
for decision in D.CLAIM_MERGES:
    key=decision['canonical'];members=decision['members'];xs=[claims[m] for m in members]
    z=copy.deepcopy(claims[key]);z.update(merged_location(xs));z['items']=unique(i for x in xs for i in x['items'])
    z['his_statement']=' / '.join(str(x['his_statement'])+' ['+x['id']+']' for x in xs)
    z['computation']='\n'.join('['+x['id']+'] '+str(x['computation']) for x in xs)
    z['refs']=unique(k for x in xs for k in x['refs'])
    z['fate']='\n'.join('['+x['id']+'] '+str(x['fate']) for x in xs)
    z['fate_date']={x['id']:x['fate_date'] for x in xs}
    z['present_status']=decision.get('present_status','As of2026-11-19: the combined statement is established under the explicit hypotheses and convention dictionary. '+str(z['present_status']))
    for f in ['statement','status_on_pages']:z[f]=decision[f]
    assert len(set(x['class'] for x in xs))==1,(key,'class mismatch')
    for m in members:claim_aliases[m]=key;claims.pop(m)
    claims[key]=z;merge_log.append(dict(decision,record_type='claim'))

extra=W/'audit/final_editorial_claim_decisions.json'
extra_decisions=readjson(extra) if extra.exists() else {'editorial':[],'refinements':[]}
editorial_ids=set(D.EDITORIAL_CLAIMS)|set(extra_decisions.get('editorial',[]))
refinement_ids=set(extra_decisions.get('refinements',[]))
for key in sorted(editorial_ids|refinement_ids,key=lambda v:int(v.rsplit('-',1)[1])):
    if key in claims:
        x=claims.pop(key)
        x['attribution']='Earlier-run or current editorial deduction/refinement; not counted as a distinct assertion of the manuscript.'
        (refinements if key in refinement_ids else editorial).append(x)

for x in claims.values():x['items']=unique(item_aliases[i] for i in x['items'])

problem_map={x['id']:x for x in problems}
for decision in D.PROBLEM_MERGES:
    key=decision['canonical'];members=decision['members'];xs=[problem_map[m] for m in members]
    z=copy.deepcopy(problem_map[key]);z['occurrences']=unique(o for x in xs for o in x['occurrences'])
    z['refs']=unique(k for x in xs for k in x['refs'])
    for f in ['title','as_he_states','plausible_today','state_of_art','why_open','worth']:z[f]=decision[f]
    for m in members:problem_aliases[m]=key;problem_map.pop(m)
    problem_map[key]=z;merge_log.append(dict(decision,record_type='problem'))
problems=list(problem_map.values())

# Preserve aliases in saved historical events; an additional column is not added
# to the requested event schema. Canonical resolution is explicit in the outcome.
for e in events:
    sid=e['statement_id'];canon=item_aliases.get(sid,claim_aliases.get(sid,problem_aliases.get(sid,sid)))
    if canon!=sid:e['outcome']+=' Canonical consolidated statement: '+canon+'.'

for d in merge_log:
    events.append(dict(statement_id=d['canonical'],date='2026-11-19',who='GPT-6 Astra Pro; effort not independently observable; SA29 part2 consolidation',type='used and rechecked in this run',outcome='Cross-package source comparison, not an independent proof of all cited results: '+d['reason']+' Original records retained under their review folders.'))

for name in ['consolidation_links.tsv']:
    if(W/'audit'/name).exists():links.extend(readtsv(W/'audit'/name))

# Review-level links sometimes cite the reviewed item rather than its stable
# source-entry IDs. Expand that already established provenance mechanically.
link_note_normalizations=[]
for row in links:
    raw=row['note_ids'];source_ids=re.findall(r'MPL_[A-Za-z0-9_+\-]+#\d+',raw)
    for m in re.finditer(r'(?<![A-Za-z0-9_-])SA29-(\d+(?:[–-]\d+)?(?:\s*,\s*\d+(?:[–-]\d+)?)*)',raw):
        for part in m.group(1).split(','):
            bounds=re.split('[–-]',part.strip());nums=range(int(bounds[0]),int(bounds[-1])+1)
            for n in nums:
                source_ids.extend(original_items.get('SA29-'+str(n),{}).get('sources',[]))
    if raw=='MPL_144_001-061 notes bibliography':source_ids.append('MPL_144_001-061#173')
    if raw=='MPL_144_001-061 notes prologue':
        row['note_ids']='Unindexed prologue: MPL_144_001-061_notes.md, line 9; no NOTES_INDEX entry'
        row['evidence']='The supplied notes prologue, line 9, names this contextual file. The external endpoint is absent from the part2 packet and was not independently verified. This is a retained availability lead, not a two-endpoint mathematical comparison.'
        link_note_normalizations.append(dict(original=raw,stable_entry_ids=None,unindexed_source=row['note_ids'],source=row['from'],target=row['to']))
        continue
    if source_ids:
        row['note_ids']=';'.join(unique(source_ids))
        if row['note_ids']!=raw:link_note_normalizations.append(dict(original=raw,stable_entry_ids=row['note_ids'],source=row['from'],target=row['to']))
    else:raise ValueError('Link lacks stable source provenance: '+str(row))

# Exact repeated rows are collapsed; no mathematical reading is selected here.
readings=unique(readings);links=unique(links);events=unique(events)
item_rows=sorted(items.values(),key=idkey);claim_rows=sorted(claims.values(),key=idkey)
problem_rows=sorted(problems,key=idkey)

index=readtsv(W.parent/'sources/SA29_notes/NOTES_INDEX.tsv')
indexids=[x.get('entry_id',x.get('id')) for x in index]
assert len(entries)==380 and len({x['entry_id'] for x in entries})==380
assert set(indexids)=={x['entry_id'] for x in entries},(list(index[0]),'index mismatch')
order={k:i for i,k in enumerate(indexids)};entries.sort(key=lambda x:order[x['entry_id']])
assert Counter(s for x in item_rows for s in x['sources'])==Counter(indexids)
assert all(e['item_id'] in items for e in entries)

# All retained sources of an earlier merged record remain visible through the
# alias map, including IDs that appear in independently authored proof notes.
writejson(W/'SA29_items.json',item_rows);writejson(W/'SA29_claims.json',claim_rows);writejson(W/'SA29_problems.json',problem_rows)
writetsv(W/'SA29_entries.tsv',entries,['entry_id','item_id','verdict','reason'])
writetsv(W/'SA29_readings.tsv',readings,['cote','scan','line','reading','alternative','evidence','weight','confidence'])
writetsv(W/'SA29_links.tsv',links,['kind','from','to','what','evidence','note_ids'])
writetsv(W/'SA29_project_links.tsv',[x for x in links if x['kind']=='our projects'],['kind','from','to','what','evidence','note_ids'])
writetsv(W/'CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'])

writejson(W/'audit/merge_decisions.json',merge_log)
writejson(W/'audit/link_note_id_normalization.json',link_note_normalizations)
writejson(W/'audit/id_aliases.json',dict(items=item_aliases,claims=claim_aliases,problems=problem_aliases))
writejson(W/'audit/editorial_checks.json',unique(editorial))
writejson(W/'audit/refined_statements.json',unique(refinements))
writejson(W/'audit/reference_checks.json',reference_checks)
writetsv(W/'audit/search_log.tsv',searches,['claim_ids','source','query','opened_url','result','exact_match','review'])

# Bibliography: keep distinct historical keys until an explicit alias is chosen.
# Duplicate keys are one work; the richest current verified entry is used and
# all URL-level verification receipts remain in reference_checks.json.
bibs={};bib_choices=[]
for r in REVIEWS:
    text=(W/r/'references.bib').read_text()
    matches=list(re.finditer(r'^@\w+\{([^,]+),',text,re.M))
    for i,m in enumerate(matches):
        original_key=m.group(1);key=REF_ALIASES.get(original_key,original_key);body=text[m.start():matches[i+1].start() if i+1<len(matches) else len(text)].strip()
        if key!=original_key:body=body.replace('{'+original_key+',','{'+key+',',1)
        assert re.search(r'note\s*=\s*\{(?:un)?verified\}',body),key
        score=sum(bool(re.search(r'\b'+f+r'\s*=',body)) for f in ['doi','journal','volume','number','pages','publisher','isbn'])
        if key not in bibs or score>bibs[key][0]:bibs[key]=(score,body,r)
bibs['Belyi1979']=(10,'@article{Belyi1979,\n  author = {Belyi, Gennadii V.},\n  title = {On Galois extensions of a maximal cyclotomic field},\n  journal = {Mathematics of the USSR-Izvestiya},\n  volume = {14},\n  number = {2},\n  pages = {247--256},\n  year = {1980},\n  doi = {10.1070/IM1980v014n02ABEH001096},\n  url = {https://www.mathnet.ru/php/archive.phtml?jrnid=im&option_lang=eng&paperid=1682&wshow=paper},\n  annote = {English translation 1980; Russian original in Izvestiya Akademii Nauk SSSR, Seriya Matematicheskaya 43(2)(1979),267--276. Received 2 August 1978 is a receipt date, not an established first-circulation date. The key retains the original-publication year.},\n  note = {verified}\n}', 'root verified MathNet metadata')
bibs['JonesOperations1985']=(10,'@misc{JonesOperations1985,\n  author = {Jones, Gareth A.},\n  title = {Operations on Maps and Hypermaps},\n  year = {1985},\n  howpublished = {Seminaire Lotharingien de Combinatoire, session 13, scanned proceedings contribution},\n  pages = {45--56},\n  url = {https://www.mat.univie.ac.at/~slc/s/sc13jones.pdf},\n  annote = {The year records the seminar session in September 1985. Exact proceedings publication year and modern article code were not independently established. Primary definitions and converse construction read in sections 2 and 5.},\n  note = {verified}\n}', 'root preserves verified seminar date separately from unestablished proceedings publication year')
for key in sorted(bibs):bib_choices.append(dict(key=key,selected_review=bibs[key][2]))
(W/'SA29_references.bib').write_text('\n\n'.join(bibs[k][1] for k in sorted(bibs))+'\n')
writejson(W/'audit/bibliography_selection.json',bib_choices)
writejson(W/'audit/bibliography_editorial_decisions.json',{'aliases':REF_ALIASES,'Belyi1979':'Normalized the selected English-journal entry to its1980 translation year and retained the1979 Russian original separately. Do not mix an English volume/pages/DOI with the original year without explanation.','verification':'All original URL-level inspection records retained; aliases identify the same works/edition, not merely similarly titled sources.'})
referenced={k for x in claim_rows+problem_rows for k in x['refs']}
assert referenced<=set(bibs),('missing bibliography keys',sorted(referenced-set(bibs)))

searched=set()
for row in searches:
    for key in re.findall(r'C-SA29-\d+',row['claim_ids']):searched.add(claim_aliases.get(key,key))
assert set(claims)<=searched,('claims without searched fate',sorted(set(claims)-searched))

metrics=dict(entries=len(entries),raw_items=len(original_items),items=len(items),item_merge_groups=len(D.ITEM_MERGES),
 raw_claims=len(original_claims),claims=len(claims),claim_merge_groups=len(D.CLAIM_MERGES),
 verdicts=dict(Counter(x['verdict'] for x in entries)),item_kinds=dict(Counter(x['kind'] for x in item_rows)),
 claims_by_class=dict(sorted(Counter(x['class'] for x in claim_rows).items())),
 claims_by_literal_status=dict(sorted(Counter(x['status_on_pages'] for x in claim_rows).items())),
 problems=len(problem_rows),readings=len(readings),links=len(links),links_by_kind=dict(Counter(x['kind'] for x in links)),
 references=len(bibs),reference_keys_unverified=[k for k,(_,b,_) in bibs.items() if 'note = {unverified}' in b],
 check_events=len(events),search_rows=len(searches),searched_claims=len(set(claims)&searched),
 editorial_checks=len(editorial),refined_statements=len(refinements),generated_utc=datetime.now(timezone.utc).isoformat())
writejson(W/'audit/consolidation_metrics.json',metrics)
print(json.dumps(metrics,ensure_ascii=False,indent=2))
