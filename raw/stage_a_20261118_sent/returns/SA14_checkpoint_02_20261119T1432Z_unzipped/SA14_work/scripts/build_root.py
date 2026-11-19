#!/usr/bin/env python3
"""Serialize manually authored Codex-source research. This script does not classify notes.

Every claim and judgment is entered explicitly below or in root_records.py after
reading the transcriptions. Source utilities only attach exact physical locators.
"""
from pathlib import Path
import json, re, csv, runpy

ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/'SA14_work'
OUT=WORK/'parts'/'root'
OUT.mkdir(parents=True,exist_ok=True)
SOURCE={p.stem.replace('_transcription',''):p for p in (ROOT/'sources/SA14_texts/codex').glob('*.tex')}
CLAIMS=[]
PROBLEMS=[]
READINGS=[]
LINKS=[]

def source_lines(alias):
    return SOURCE[alias].read_text().splitlines()

def quote(alias,first,last=None):
    lines=source_lines(alias)
    return '\n'.join(lines[first-1:(last or first)])

def locus(alias,scans):
    ls=source_lines(alias); anchors=[]
    for i,line in enumerate(ls,1):
        m=re.search(r'\\scanpage\{(\d+)\}',line)
        if m: anchors.append((int(m.group(1)),i))
    result=[]
    for j,(scan,start) in enumerate(anchors):
        if scan in scans:
            stop=anchors[j+1][1]-1 if j+1<len(anchors) else len(ls)
            result.append({'file':str(SOURCE[alias].relative_to(ROOT)), 'scan':scan,'first':start,'last':stop})
    assert {x['scan'] for x in result}==set(scans),(alias,scans,result)
    return result

def claim(n,locs,q,statement,status,cls,fate,refs,searches,computation='No numerical computation is asserted; mathematical qualification is stated in the claim.',confidence='high',fate_date='First circulation not independently dated; publication dates in the cited bibliography.',status_reason='',present=None,items=None,ref_locators=None):
    assert cls in 'ABCDEF'
    loci=[x for alias,scans in locs for x in locus(alias,scans)]
    cotes=sorted({int(re.search(r'57|58|59',a).group()) for a,s in locs})
    CLAIMS.append({'id':f'C-SA14-{n:03d}','items':items or [],'cote':cotes[0] if len(cotes)==1 else cotes,'scans':sorted(set(x['scan'] for x in loci)), 'lines':loci, 'his_statement':q,'statement':statement,'status_on_pages':status,'page_status_reason':status_reason,'computation':computation,'class':cls,'fate':fate,'fate_date':fate_date,'present_status':'As of 2026-11-19: '+(present or fate),'refs':refs,'ref_locators':ref_locators or {},'confidence':confidence,'searches':[f'research/web_root_{s:03d}.json' for s in searches]})

def problem(n,title,claim_ids,as_he_states,plausible,state,why,worth,refs,extra_loci=None):
    found=[c for c in CLAIMS if c['id'] in claim_ids]
    assert len(found)==len(claim_ids),(n,claim_ids)
    occ=[x for c in found for x in c['lines']]
    if extra_loci: occ += [x for a,s in extra_loci for x in locus(a,s)]
    PROBLEMS.append({'id':f'MP-SA14-{n:03d}','title':title,'occurrences':occ,'as_he_states':as_he_states,'plausible_today':plausible,'state_of_art':state,'why_open':why,'worth':worth,'refs':refs,'claims':claim_ids})

def reading(alias,scan,line,reading,alternative,evidence,weight='high',confidence='medium'):
    c=int(re.search(r'57|58|59',alias).group())
    READINGS.append({'cote':c,'scan':scan,'line':f'{SOURCE[alias].name}:{line}','reading':reading,'alternative':alternative,'evidence':evidence,'weight':weight,'confidence':confidence})

def link(kind,fr,to,what,evidence,note_ids=''):
    LINKS.append({'kind':kind,'from':fr,'to':to,'what':what,'evidence':evidence,'note_ids':note_ids})

runpy.run_path(str(WORK/'scripts/root_records.py'),init_globals=globals())
runpy.run_path(str(WORK/'scripts/root_aux.py'),init_globals=globals())
for name,records in [('claims',CLAIMS),('problems',PROBLEMS)]:
    (OUT/(name+'.json')).write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
for name,rows,fields in [('readings',READINGS,['cote','scan','line','reading','alternative','evidence','weight','confidence']),('links',LINKS,['kind','from','to','what','evidence','note_ids'])]:
    with (OUT/(name+'.tsv')).open('w',newline='') as f:
        w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'manually_authored_claims':len(CLAIMS),'problems':len(PROBLEMS),'readings':len(READINGS),'links':len(LINKS)},indent=2))
