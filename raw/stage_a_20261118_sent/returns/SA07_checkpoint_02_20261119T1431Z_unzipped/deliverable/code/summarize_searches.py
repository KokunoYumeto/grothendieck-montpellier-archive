"""Inventory actual web requests; never infer that a search proved a claim."""
import csv, json, re
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'deliverable'/'evidence'
rows=[]
for owner, folder in [('root',ROOT/'deliverable'/'evidence'),('p15',ROOT/'agents'/'p15'/'evidence'),('p16',ROOT/'agents'/'p16'/'evidence'),('p18',ROOT/'agents'/'p18'/'evidence')]:
    for p in sorted(folder.glob('web*.json')):
        if not re.match(r'web_?(?:root_)?\d+',p.name): continue
        if any(x in p.name for x in ('response','metadata','ledger')): continue
        d=json.loads(p.read_text())
        req=d.get('request',d.get('query',d.get('params',d)))
        if not isinstance(req,dict): continue
        for engine in ('system1_search_query','system2_search_query'):
            for q in req.get(engine,[]) or []:
                rows.append({'owner':owner,'batch':p.stem,'operation':engine,'query_or_ref':q['q'],'detail':json.dumps({k:v for k,v in q.items() if k!='q'},ensure_ascii=False)})
        for op in ('open','find','click','screenshot'):
            for q in req.get(op,[]) or []:
                rows.append({'owner':owner,'batch':p.stem,'operation':op,'query_or_ref':q.get('ref_id',''),'detail':json.dumps({k:v for k,v in q.items() if k!='ref_id'},ensure_ascii=False)})
with (OUT/'web_request_inventory.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['owner','batch','operation','query_or_ref','detail'],delimiter='\t');w.writeheader();w.writerows(rows)
terms=['zbmath','arxiv','mathoverflow','numdam','EGA','SGA']
report={'requests':len(rows),'by_owner':dict(Counter(x['owner'] for x in rows)),
 'by_operation':dict(Counter(x['operation'] for x in rows)),
 'named_channels_in_queries_or_urls':{s:sum(s.lower() in x['query_or_ref'].lower() for x in rows) for s in terms},
 'scope':'Counts measure actual queries/navigation, not successful verification or completeness of any database. Per-claim judgment remains in literature_search.tsv.'}
print(json.dumps(report,ensure_ascii=False,indent=2))
