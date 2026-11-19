"""Join manually assigned search batches with their actual requests and judgments."""
import csv,json
from pathlib import Path
D=Path(__file__).resolve().parents[1]
claims=json.loads((D/'root_records/claims.json').read_text())
refs={r['key']:r for r in json.loads((D/'root_records/refs.json').read_text())}
with (D/'root_records/literature_search.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','search_batches','queries_or_navigation','opened_locators','assessment'])
    for c in claims:
        requests=[]
        for batch in c['search_ids']:
            p=D/'evidence'/('web_root_'+batch.removeprefix('root')+'.json')
            obj=json.loads(p.read_text())
            req=obj.get('request',{})
            queries=[x['q'] for e in ('system1_search_query','system2_search_query') for x in req.get(e,[])]
            if queries:requests.extend(queries)
            else:requests.append(batch+': primary open/find/click; full request retained in retrieval metadata')
        loc=[]
        for k in c['refs']:
            if k in refs:loc.append(k+': '+refs[k]['locator']+'; '+refs[k]['url']+'; '+refs[k]['verification_scope'])
            else:loc.append(k+': collaborator verification; see consolidated bibliography and corresponding search ledger')
        w.writerow([c['id'],'2026-11-19','; '.join(c['search_ids']),' || '.join(dict.fromkeys(requests)),' || '.join(loc),c['fate']])
print(json.dumps({'claim_search_rows':len(claims),'all_have_assigned_search_batches':all(c['search_ids'] for c in claims)},indent=2))
