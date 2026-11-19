#!/usr/bin/env python3
"""Expose existing claim-to-search mappings. No search or fate is invented here."""
import csv,json,collections,datetime
from pathlib import Path
W=Path(__file__).resolve().parents[1]
aliases=json.loads((W/'SA23_id_aliases.json').read_text())['aliases']
claims=json.loads((W/'SA23_claims.json').read_text())
ids={c['id']for c in claims}
mapped=collections.defaultdict(list)
unknown=[]; total=0; owner_counts={}
for p in sorted((W/'parts').iterdir()):
 f=p/'search_log.jsonl'
 if not f.exists():continue
 rows=[json.loads(s)for s in f.read_text().splitlines()if s.strip()]
 owner_counts[p.name]=len(rows);total+=len(rows)
 for lineno,row in enumerate(rows,1):
  oldids=row.get('claim_ids',row.get('claims',[row['claim']]if'claim'in row else[]))
  if isinstance(oldids,str):oldids=[oldids]
  for old in oldids:
   targets=aliases.get(old,[old])
   for target in targets:
    if target not in ids:unknown.append({'owner':p.name,'line':lineno,'claim':old,'target':target});continue
    # The path and JSONL line give a stable route even when an owner did not
    # assign a separate search-record ID. A mapped family is not falsely
    # represented as a distinct new query for each individual claim.
    mapped[target].append({'original_claim_id':old,'file':str(f.relative_to(W)),'line':lineno,'search_record_id':row.get('id',f'{p.name}:line{lineno}'),'date':row.get('date',''),'record_keys':list(row)})
out=[]
for c in claims:
 rows=mapped[c['id']]
 out.append({'claim_id':c['id'],'class':c['class'],'search_rows':len(rows),'source_claim_ids':'; '.join(sorted({r['original_claim_id']for r in rows})),'search_locations':'; '.join(f"{r['file']}:{r['line']} [{r['search_record_id']}]"for r in rows),'fate_date':c['fate_date'],'confidence':c['confidence']})
with(W/'SA23_fate_coverage.tsv').open('w')as f:
 writer=csv.DictWriter(f,fieldnames=['claim_id','class','search_rows','source_claim_ids','search_locations','fate_date','confidence'],delimiter='\t');writer.writeheader();writer.writerows(out)
report={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'purpose':'Trace final claims to actual preserved search records. Grouped searches are counted as recorded rows, not fabricated individual searches. Read each row for exact query, opened result, scope and limitations.','claims':len(claims),'preserved_search_records':total,'owner_search_records':owner_counts,'missing_claims':[c['id']for c in claims if not mapped[c['id']]],'unknown_claim_targets':unknown,'mappings':dict(mapped)}
(W/'outputs'/'fate_coverage.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items()if k!='mappings'},ensure_ascii=False))
