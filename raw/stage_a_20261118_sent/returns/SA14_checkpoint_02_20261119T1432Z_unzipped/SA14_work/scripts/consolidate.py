#!/usr/bin/env python3
"""Join already-read, manually adjudicated registers using explicit semantic decisions.

No verdict is inferred from headings, keywords, or mathematical cues here.
Every merge below was selected after reading both item statements and source contexts.
Original part records remain available as an audit trail.
"""
from pathlib import Path
import csv,json,re,collections
W=Path(__file__).resolve().parents[1]
PARTS=['picard_early','picard_lefschetz','lfunctions','root']
def J(p):return json.loads(p.read_text())
def T(p):return list(csv.DictReader(p.open(),delimiter='\t')) if p.exists() else []
def uniq(xs):
    out=[];seen=set()
    for x in xs:
        k=json.dumps(x,ensure_ascii=False,sort_keys=True)
        if k not in seen:out.append(x);seen.add(k)
    return out
def flat(x):return x if isinstance(x,list) else [x]

# Duplicate contextual comparisons and exact repeated mathematical questions.
item_aliases={
 'SA14-201':'SA14-1','SA14-335':'SA14-1','SA14-202':'SA14-2',
 'SA14-204':'SA14-4','SA14-205':'SA14-5','SA14-206':'SA14-6',
 'SA14-207':'SA14-7','SA14-208':'SA14-8','SA14-209':'SA14-9','SA14-210':'SA14-10',
 'SA14-231':'SA14-16','SA14-232':'SA14-16','SA14-233':'SA14-16',
 'SA14-235':'SA14-16','SA14-337':'SA14-16','SA14-445':'SA14-16',
 'SA14-69':'SA14-626'
}
claim_aliases={
 'C-SA14-096':'C-SA14-626','C-SA14-204':'C-SA14-626',
 'C-SA14-211':'C-SA14-608','C-SA14-327':'C-SA14-642',
 'C-SA14-328':'C-SA14-642','C-SA14-330':'C-SA14-634'
}
problem_aliases={
 'MP-SA14-038':'MP-SA14-626','MP-SA14-203':'MP-SA14-626',
 'MP-SA14-261':'MP-SA14-642'
}
aliases={**item_aliases,**claim_aliases,**problem_aliases}

items={x['id']:x for part in PARTS for x in J(W/'parts'/part/'items.json')}
claims={x['id']:x for part in PARTS for x in J(W/'parts'/part/'claims.json')}
problems={x['id']:x for part in PARTS for x in J(W/'parts'/part/'problems.json')}

def add_item_claim(i,c):
    i.setdefault('source_variants',[]).append({'claim':c['id'],'cote':c['cote'],'scans':c['scans'],'lines':c['lines'],'his_words':c['his_statement'],'statement':c['statement']})
    i['claims']=uniq(i.get('claims',[])+[c['id']])
    i['sources']=uniq(i['sources']+['transcript:'+x['file'].removeprefix('sources/') for x in c['lines'] if isinstance(x,dict)])
    i['cote']=uniq(flat(i['cote'])+flat(c['cote']));i['cote']=i['cote'][0] if len(i['cote'])==1 else i['cote']
    i['scans']=uniq(flat(i['scans'])+flat(c['scans']))
    i['lines']=uniq(flat(i['lines'])+flat(c['lines']))
    i['his_words']+='\nAdditional source occurrence ('+c['id']+'): '+c['his_statement']
    i['statement']+='\nAdditional checked formulation ('+c['id']+'): '+c['statement']
    i['reconstruction']+=' Additional Codex occurrence read independently; hypotheses and conventions are detailed in '+c['id']+'.'
for cid,iid in J(W/'parts/root/item_joins.json').items():add_item_claim(items[iid],claims[cid])

for old,new in item_aliases.items():
    a,b=items[old],items[new]
    b.setdefault('source_variants',[]).append(a)
    b['sources']=uniq(b['sources']+a['sources'])
    b['scans']=uniq(flat(b['scans'])+flat(a['scans']))
    b['lines']=uniq(flat(b['lines'])+flat(a['lines']))
    cs=uniq(flat(b['cote'])+flat(a['cote']));b['cote']=cs[0] if len(cs)==1 else cs
    b['his_words']+='\nSource occurrence formerly '+old+': '+a['his_words']
    b['statement']+='\nCompared occurrence formerly '+old+': '+a['statement']
    b['reconstruction']+='\n'+old+': '+a['reconstruction']
    b['check_reason']+='\n'+old+' ['+a['check']+']: '+a['check_reason']
    b['claims']=uniq(b.get('claims',[])+a.get('claims',[]))
    del items[old]

for old,new in claim_aliases.items():
    a,b=claims[old],claims[new]
    b.setdefault('source_variants',[]).append(a)
    b['items']=uniq(b['items']+a['items']);b['scans']=uniq(flat(b['scans'])+flat(a['scans']))
    b['lines']=uniq(flat(b['lines'])+flat(a['lines']))
    cs=uniq(flat(b['cote'])+flat(a['cote']));b['cote']=cs[0] if len(cs)==1 else cs
    b['his_statement']+='\nRelated source occurrence formerly '+old+': '+a['his_statement']
    b['fate']+='\nScope at '+old+': '+a['fate']
    b['computation']+='\nAdditional source check '+old+': '+str(a['computation'])
    b['refs']=uniq(b['refs']+a['refs'])
    b['searches']=uniq(b.get('searches',[])+a.get('searches',[])+flat(a.get('search_log',[])))
    del claims[old]

for old,new in problem_aliases.items():
    a,b=problems[old],problems[new]
    b.setdefault('source_variants',[]).append(a)
    b['occurrences']=uniq(flat(b['occurrences'])+flat(a['occurrences']))
    for field in ['as_he_states','plausible_today','state_of_art','why_open','worth']:
        b[field]+='\nOccurrence formerly '+old+': '+str(a[field])
    b['refs']=uniq(b['refs']+a['refs'])
    b['claims']=uniq(b.get('claims',[])+a.get('claims',[])+a.get('claim_ids',[]))
    del problems[old]

# Preserve source_versions verbatim. Rewrite only outward pointers in final records.
idpat=re.compile(r'(?<![A-Za-z0-9-])(?:MP-SA14-\d+|C-SA14-\d+|SA14-\d+)(?![0-9])')
compactpat=re.compile(r'(?<![A-Za-z0-9-])(MP-SA14-|C-SA14-|SA14-)(\d+(?:[–-]\d+)?(?:,\s*\d+(?:[–-]\d+)?)*)')
def expand_aliased_compact(m):
    prefix,body=m.groups()
    if not any(ch in body for ch in ',–-'):return m.group()
    nums=[]
    for segment in body.split(','):
        limits=re.split('[–-]',segment.strip())
        if len(limits)==1:nums.append(int(limits[0]))
        else:
            start,stop=map(int,limits)
            if stop<start or stop-start>1000:raise ValueError(('invalid ID range',m.group()))
            nums.extend(range(start,stop+1))
    ids=[prefix+(str(n) if prefix=='SA14-' else f'{n:03d}') for n in nums]
    # Expand before rewriting: otherwise201–202 would become1–202.
    if not any(s in aliases for s in ids):return m.group()
    return ', '.join(uniq([aliases.get(s,s) for s in ids]))
def rewrite(v,key=''):
    if key in ('source_variants','original_statement_id','original_item_id'):return v
    if isinstance(v,str):
        v=compactpat.sub(expand_aliased_compact,v)
        return idpat.sub(lambda m:aliases.get(m.group(),m.group()),v)
    if isinstance(v,list):return [rewrite(x) for x in v]
    if isinstance(v,dict):return {k:rewrite(x,k) for k,x in v.items()}
    return v
items={k:rewrite(v) for k,v in items.items()};claims={k:rewrite(v) for k,v in claims.items()};problems={k:rewrite(v) for k,v in problems.items()}
for c in claims.values():
    detail=c['status_on_pages']
    # Normalize an already-authored status label, preserving every qualifier.
    if detail.startswith('proved there'):normal='proved there'
    elif detail.startswith('proof sketched'):normal='proof sketched'
    elif detail.startswith('stated'):normal='stated without proof'
    elif detail.startswith('open on the pages'):normal='open on the pages'
    elif detail.startswith('corrected by himself later'):normal='corrected by himself later'
    elif detail.startswith('false'):normal='false as stated'
    else:raise ValueError(('unrecognized human status',detail))
    if normal!=detail:c['page_status_detail']=detail
    c['status_on_pages']=normal

# Literal authorship/fate audit, based on the actual opened endpoint, not on
# inclusion in a seminar associated with Grothendieck. Attribution is retained.
authorship_corrections={
 'C-SA14-413':('B','The checked established treatment is Stacks0BQM; no exact Grothendieck-authored publication endpoint was established in this search.'),
 'C-SA14-414':('B','The exact checked determinant/duality endpoint is Deligne1973, with Illusie’s historical discussion; this is not an own-author publication of Grothendieck.'),
 'C-SA14-417':('B','The checked boundary/localization treatment is in the Stacks Project and Wildeshaus; no exact own-author publication was established.'),
 'C-SA14-428':('B','The exact checked published endpoint is Deligne1973 §§10.5–10.7, under Deligne’s authorship.'),
 'C-SA14-444':('B','Raynaud286 and Laumon are the exact checked publication endpoints. Attribution of the formula to Grothendieck is retained; authorship of those publications is distinct.'),
 'C-SA14-447':('B','The established triangulated-category formalism is checked in the Stacks Project; no exact Grothendieck-authored publication endpoint was established.'),
 'C-SA14-210':('C','The sheaf-level splitting has an independent proof in P22, but the search located the published framework rather than this exact displayed decomposition. This classification marks a publication-identification gap, not an assertion that the proved splitting remains mathematically open.')
}
for cid,(cls,why) in authorship_corrections.items():
    c=claims[cid];c['class_before_authorship_audit']=c['class'];c['class']=cls
    if cid=='C-SA14-210':
        c['fate']='FGA supplies the Picard-descent framework, and rigidification proves the exact sheaf-level splitting as checked in P22. The exact displayed formula was not identified as a theorem in an opened own-author publication. '+why
    else:c['fate']+=' Publication-authorship audit: '+why
    c['present_status']='As of 2026-11-19: '+c['fate']

entries=[]
for part in PARTS:
    for row in T(W/'parts'/part/'entries.tsv'):
        old=row['item_id']
        if old in item_aliases:
            row['item_id']=item_aliases[old]
            if row['verdict']=='kept':row['verdict']='merged'
            row['reason']+=' Cross-package consolidation: '+old+' merged into '+row['item_id']+' after comparing both source contexts; source-specific mathematical qualification retained.'
        entries.append(row)
readings=uniq([rewrite(x) for part in PARTS for x in T(W/'parts'/part/'readings.tsv')])
links=uniq([rewrite(x) for part in PARTS for x in T(W/'parts'/part/'links.tsv')])
projects=[]
for part in PARTS:
    for fn in ('project_leads.tsv','quarantined_context_leads.tsv','project_links.tsv'):
        for x in T(W/'parts'/part/fn):projects.append(dict(part=part,source_table=fn,record=x))
# Existing our-project rows are leads, never counted as verified endpoints.
checked_links=[]
for l in links:
    if l['kind']=='our projects':
        l['evidence']='QUARANTINED LEAD — external endpoint unavailable; no mathematical link verified. '+l['evidence']
    checked_links.append(l)
entry_items={x['entry_id']:x['item_id'] for x in entries}
for src in projects:
    x=src['record'];ids=x.get('note_ids','')
    if src['part']=='picard_early':
        l={k:x.get(k,'') for k in ['from','to','what','evidence','note_ids']}
        l['evidence']='QUARANTINED LEAD — external endpoint unavailable. '+l['evidence']+' Original run names: '+x.get('run_names','')
    else:
        localids=uniq([entry_items[n.strip()] for n in ids.split(';') if n.strip() in entry_items])
        l={'from':'; '.join(i+' '+str(items[i]['lines']) for i in localids),'to':x.get('run_or_endpoint',''),'what':x.get('relation_claimed_by_earlier_run',''),'evidence':'QUARANTINED LEAD — external endpoint unavailable. '+x.get('checked_end','')+' '+x.get('limit',''),'note_ids':ids}
    l['kind']='our projects';checked_links.append(rewrite(l))

events=[]
for part in PARTS:
    for e in T(W/'parts'/part/'CHECK_EVENTS.tsv'):
        old=e['statement_id'];e=rewrite(e)
        if old in aliases:e['outcome']='Original record '+old+'; canonical '+e['statement_id']+'. '+e['outcome']
        events.append(e)
for cid,(cls,why) in authorship_corrections.items():
    events.append({'statement_id':cid,'date':'2026-11-19','who':'GPT-6 Astra Pro; effort not exposed; SA14-20261119; root with independent part-owner audit','type':'used and rechecked in this run','outcome':'Bibliographic classification check, not a new mathematical proof. Class revised to '+cls+'. '+why})

def dump(name,rows):
    rows=sorted(rows,key=lambda x:int(x['id'].rsplit('-',1)[1]))
    (W/name).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
dump('SA14_items.json',list(items.values()));dump('SA14_claims.json',list(claims.values()));dump('SA14_problems.json',list(problems.values()))
def tab(name,rows,fields):
    with (W/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
tab('SA14_entries.tsv',entries,['entry_id','item_id','verdict','reason'])
tab('SA14_readings.tsv',readings,['cote','scan','line','reading','alternative','evidence','weight','confidence'])
tab('SA14_links.tsv',checked_links,['kind','from','to','what','evidence','note_ids'])
tab('CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'])
(W/'research/consolidation_aliases.json').write_text(json.dumps({'items':item_aliases,'claims':claim_aliases,'problems':problem_aliases,'method':'Explicit decisions after manual reading of both source contexts; original parts retained.'},indent=2)+'\n')
(W/'research/quarantined_project_leads.json').write_text(json.dumps(projects,ensure_ascii=False,indent=2)+'\n')
(W/'SA14_references.bib').write_text('\n\n'.join((W/'parts'/p/'references.bib').read_text() for p in PARTS)+'\n')
counts={'entries':len(entries),'items':len(items),'claims':len(claims),'problems':len(problems),'readings':len(readings),'links':len(checked_links),'check_events':len(events),'verdicts':dict(collections.Counter(x['verdict'] for x in entries)),'item_kinds':dict(collections.Counter(x['kind'] for x in items.values())),'claim_classes':dict(collections.Counter(x['class'] for x in claims.values())),'claim_statuses':dict(collections.Counter(x['status_on_pages'] for x in claims.values())),'links_by_kind':dict(collections.Counter(x['kind'] for x in checked_links)),'quarantined_project_source_records':len(projects)}
(W/'research/final_counts.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n');print(json.dumps(counts,indent=2))
