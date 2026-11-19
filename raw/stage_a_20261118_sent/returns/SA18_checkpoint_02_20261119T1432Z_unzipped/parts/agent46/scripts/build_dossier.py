#!/usr/bin/env python3
"""Serialize manually reviewed source records. No keyword-generated verdicts.

The semantic data in records.py are written by the reviewer after reading each
entry and passage. This program supplies deterministic ids, extracts quotations
at supplied exact line numbers, validates links, and writes the requested formats.
"""
from pathlib import Path
import csv,json,runpy,datetime
ROOT=Path('/workspace/scratch/c38eb4e8f07f')
OUT=ROOT/'SA18_work/parts/agent46'
SRC=ROOT/'sources'
P='SA18_texts/pro/MPL_46_002-048_transcription.tex'
C='SA18_texts/codex/C46-01_transcription.tex'
K1='SA18_texts/codex/K46-01_transcription.tex'
K2='SA18_texts/codex/K46-02_transcription.tex'
K3='SA18_texts/codex/K46-03_transcription.tex'
J1='SA18_texts/codex/J53-01_transcription.tex'
J2='SA18_texts/codex/J53-02_transcription.tex'
J3='SA18_texts/codex/J53-03_transcription.tex'
J4='SA18_texts/codex/J53-04_transcription.tex'
J5='SA18_texts/codex/J53-05_transcription.tex'
items=[];entries=[];claims=[];problems=[];readings=[];links=[];events=[]
ik={};ck={};pk={}
WHO='GPT-6 Astra Pro / inherited effort / agent46'
DATE='2026-11-19'
def loc(file,start,end=None):
    end=start if end is None else end
    text=(SRC/file).read_text().splitlines()
    assert 1<=start<=end<=len(text),(file,start,end,len(text))
    return {'file':file,'absolute_file':str(SRC/file),'start':start,'end':end,'numbering':'absolute 1-based transcription lines'}
def quote(file,start,end=None):
    end=start if end is None else end
    s='\n'.join((SRC/file).read_text().splitlines()[start-1:end])
    return s if len(s)<=480 else s[:360]+' […] '+s[-90:]
def event(id,type,outcome):
    events.append({'statement_id':id,'date':DATE,'who':WHO,'type':type,'outcome':outcome})
def I(key,ns,kind,cote,scans,places,q,statement,reconstruction,check,reason,verdicts=None):
    id=f'SA18-{46001+len(items):05d}'
    ik[key]=id
    sources=[f'MPL_46_002-048#{n}' for n in ns]
    x=dict(id=id,sources=sources,kind=kind,cote=cote,scans=scans,lines=places,his_words=q,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason,local_key=key)
    items.append(x)
    for j,n in enumerate(ns):
        verdict=(verdicts or {}).get(n,'kept' if j==0 else 'merged')
        entries.append(dict(entry_id=f'MPL_46_002-048#{n}',item_id=id,verdict=verdict,reason=reason))
    event(id,'used and rechecked in this run','Read the indexed entry (where present) and the cited transcription passage; '+reason)
    return id
def Cc(key,itemkeys,cote,scans,places,q,statement,status,computation,cls,fate,date,refs,confidence='high',searches=None):
    id=f'CL-SA18-{46001+len(claims):05d}'
    ck[key]=id
    x=dict(id=id,items=[ik[k] for k in itemkeys],cote=cote,scans=scans,lines=places,his_statement=q,statement=statement,status_on_pages=status,computation=computation,**{'class':cls},fate=fate,fate_date=date,present_status='As of 19 November 2026: '+fate,refs=refs,confidence=confidence,local_key=key,literature_search_ids=searches or [])
    claims.append(x)
    event(id,'used and rechecked in this run','Read the full cited passage, its cancellations and immediate proof; '+status)
    return id
def Pr(key,title,occ,as_he,plausible,state,why,worth,refs):
    id=f'MP-SA18-{46001+len(problems):05d}'
    pk[key]=id
    problems.append(dict(id=id,title=title,occurrences=occ,as_he_states=as_he,plausible_today=plausible,state_of_art=state,why_open=why,worth=worth,refs=refs,local_key=key))
    event(id,'used and rechecked in this run','Compared the authorial question with the cited opened source and kept the exact scope in the problem record.')
    return id
def R(cote,scan,file,line,reading,alternative,evidence,weight='high',confidence='high'):
    readings.append(dict(cote=cote,scan=scan,line=f'{SRC/file}:{line} (absolute 1-based)',reading=reading,alternative=alternative,evidence=evidence,weight=weight,confidence=confidence+' mathematical alarm; ink unresolved'))
def L(kind,a,b,what,evidence,ns=[]):
    links.append(dict(kind=kind,**{'from':a,'to':b},what=what,evidence=evidence,note_ids=';'.join(f'MPL_46_002-048#{n}' for n in ns)))
ns=globals()
for fname in ['records_items.py','records_claims.py','records_problems.py','records_readings_links.py','review_refinements.py','literature_mapping.py','check_events_extra.py']:
    p=OUT/'data'/fname
    if p.exists(): exec(compile(p.read_text(),str(p),'exec'),ns)
def tsv(name,rows,fields):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n',extrasaction='ignore');w.writeheader();w.writerows(rows)
for name,rows in [('items.json',items),('claims.json',claims),('problems.json',problems)]:
    (OUT/name).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
tsv('entries.tsv',sorted(entries,key=lambda x:int(x['entry_id'].split('#')[-1])),['entry_id','item_id','verdict','reason'])
tsv('readings.tsv',readings,['cote','scan','line','reading','alternative','evidence','weight','confidence'])
tsv('links.tsv',links,['kind','from','to','what','evidence','note_ids'])
tsv('CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'])
(OUT/'data'/'id_map.json').write_text(json.dumps(dict(items=ik,claims=ck,problems=pk),indent=2))
print(json.dumps(dict(entries=len(entries),items=len(items),claims=len(claims),problems=len(problems),readings=len(readings),links=len(links),events=len(events)),indent=2))
