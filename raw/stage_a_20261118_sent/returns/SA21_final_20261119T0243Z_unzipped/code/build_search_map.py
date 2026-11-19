"""Consolidate already executed, manually assigned literature searches.

This script assigns no mathematical verdict or literature fate. It joins the
readers' explicit claim-to-query records and fails if any claim lacks one.
"""
from pathlib import Path
import csv,json,re,collections
R=Path(__file__).resolve().parents[1]
def read_tsv(p):
    with p.open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
claims=json.loads((R/'SA21_claims.json').read_text())
rows=[];missing=[];query_catalog=[]
for c in claims:
    part=Path(c['audit_part'])
    records=[]
    log=R/part/'search_log.tsv'
    if log.exists():
        for q in read_tsv(log):
            ids=re.findall(r'C-SA21-[\w-]+',q.get('claim_ids',q.get('claims','')))
            if c['id'] in ids:records.append(q)
    if part.name=='root':
        evidence=c.get('search_evidence',[])
        for path in evidence:
            p=R/path
            assert p.exists(),path
            o=json.loads(p.read_text())
            request=o.get('request',o.get('query',o.get('queries',{})))
            records.append({'search_id':p.stem,'queries_or_locators':json.dumps(request,ensure_ascii=False),'result':c['fate'],'raw_output':path})
    if not records:
        missing.append(c['id']);continue
    ids=[];queries=[];evidence=[]
    for q in records:
        sid=q.get('search_id',q.get('id',''))
        full_id=part.name+':'+sid
        ids.append(full_id)
        query=q.get('queries_or_locators',q.get('queries_and_opens',q.get('query',q.get('queries',''))))
        queries.append(query)
        raw=q.get('raw_output',q.get('output',''))
        if raw:evidence.append(raw)
        query_catalog.append({'id':full_id,'part':str(part),'query_or_locator':query,'result_and_limit':q.get('result_and_limit',q.get('result',q.get('results',q.get('limits','')))),'raw_output':raw})
    rows.append({'claim_id':c['id'],'part':str(part),'search_ids':';'.join(dict.fromkeys(ids)),
        'search_log':str(log.relative_to(R)) if log.exists() else 'parts/root/search_families.json',
        'queries_and_locators':' | '.join(dict.fromkeys(queries)),
        'opened_references':';'.join(c['refs']),
        'scope_and_limit':c['fate'],'search_cutoff':'2026-11-19'})
with (R/'SA21_search_map.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['claim_id','part','search_ids','search_log','queries_and_locators','opened_references','scope_and_limit','search_cutoff'],delimiter='\t');w.writeheader();w.writerows(rows)
unique=[];seen=set()
for q in query_catalog:
    k=(q['id'],q['query_or_locator'])
    if k not in seen:seen.add(k);unique.append(q)
(R/'audit/executed_search_catalog.json').write_text(json.dumps(unique,ensure_ascii=False,indent=2)+'\n')
report={'claims':len(claims),'mapped_claims':len(rows),'unique_query_rows':len(unique),'missing_claim_ids':missing,
        'qualification':'Search families are explicit assignments made by the readers after reading the claims; a shared search does not imply a shared exact fate. Each claim retains its own hypothesis comparison and dated conclusion.'}
(R/'audit/search_coverage.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
assert not missing,'Every claim must have an executed search record.'
