#!/usr/bin/env python3
"""Create a current combined view without pretending unfinished source coverage is complete."""
import json,csv,re,datetime
from pathlib import Path
W=Path(__file__).resolve().parents[1];owners=sorted(p for p in(W/'parts').iterdir()if p.is_dir())
report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'owners':{},'warnings':[]}
for name in ['items','claims','problems']:
    out=[]
    for owner in owners:
        f=owner/(name+'.json')
        if f.exists():
            x=json.loads(f.read_text());assert isinstance(x,list),str(f);out+=x;report['owners'].setdefault(owner.name,{})[name]=len(x)
    ids=[x['id']for x in out];assert len(ids)==len(set(ids)),name+' duplicate IDs'
    (W/('SA23_'+name+'.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    report[name]=len(out)
for name,fields in [('entries',['entry_id','item_id','verdict','reason']),('readings',['cote','scan','line','reading','alternative','evidence','weight','confidence']),('links',['kind','from','to','what','evidence','note_ids'])]:
    rows=[]
    for owner in owners:
        f=owner/(name+'.tsv')
        if f.exists()and f.stat().st_size:
            with f.open()as h:
                reader=csv.DictReader(h,delimiter='\t');assert reader.fieldnames==fields,(str(f),reader.fieldnames);rows+=list(reader)
    if name=='entries':
        ids=[x['entry_id']for x in rows];assert len(ids)==len(set(ids));assert len(rows)==326,len(rows)
    with(W/('SA23_'+name+'.tsv')).open('w')as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
    report[name]=len(rows)
fields=['statement_id','date','who','type','outcome'];events=[];seen=set()
for owner in owners:
    for f in sorted(owner.glob('*check_events.tsv')):
        with f.open()as h:
            rd=csv.DictReader(h,delimiter='\t')
            if rd.fieldnames!=fields:report['warnings'].append('Check event schema awaiting integration: '+str(f));continue
            for row in rd:
                key=tuple(row.get(k,'')for k in fields)
                if key not in seen:seen.add(key);events.append(row)
with(W/'CHECK_EVENTS.tsv').open('w')as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
report['check_events']=len(events)
bib='\n'.join('% Owner: '+p.name+'\n'+(p/'references.bib').read_text()for p in owners if(p/'references.bib').exists())
(W/'SA23_references.bib').write_text(bib)
sections=['# SA23 dossier — current working assembly\n\nThis assembly records the sections written so far. The final completeness audit has not yet run; source coverage is reported in each owner’s coverage file. The immutable checkpoint contains the full work tree and programs so the remaining source readings can continue.\n']
sections.extend((p/'section.md').read_text()for p in owners if(p/'section.md').exists())
(W/'SA23_dossier.md').write_text('\n\n'.join(sections))
dirs=['# SA23 research directions — current assembly\n\nFinal cross-topic ranking follows the complete source audit.\n']
dirs.extend((p/'directions.md').read_text()for p in owners if(p/'directions.md').exists())
(W/'SA23_directions.md').write_text('\n\n'.join(dirs))
trace=[]
for owner in owners:
    for f in sorted(owner.glob('search_*.json')):
        if not re.fullmatch(r'search_\d+\.json',f.name):continue
        raw=json.loads(f.read_text());res=raw.get('result',raw);requests=raw.get('args',raw.get('queries'))
        metadata=[]
        for block in res.get('content',[]):
            text=block.get('text','')
            for chunk in text.split('--------------------------------------------------------------------------------'):
                m=re.search(r'^\s*(.*?)\s*\((https?://[^\n]+)\)\s*\n【([^】]+)】',chunk,re.M)
                if m:metadata.append({'title':m.group(1),'url':m.group(2),'retrieval_ref':m.group(3),'failed':'Failed to fetch'in chunk})
        trace.append({'owner':owner.name,'batch':f.name,'requests':requests,'result_metadata':metadata,'note':'No third-party article text is included. Owner search_log.jsonl supplies exact claim mappings and interpretations.'})
with(W/'outputs'/'search_metadata.jsonl').open('w')as f:
    for x in trace:f.write(json.dumps(x,ensure_ascii=False)+'\n')
(W/'outputs'/'current_assembly.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
