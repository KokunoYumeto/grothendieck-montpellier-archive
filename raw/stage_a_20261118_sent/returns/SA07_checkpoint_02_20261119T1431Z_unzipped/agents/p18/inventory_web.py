"""Navigation inventory of retained web calls, with no verdict inference."""
from pathlib import Path
import json,csv,re
P=Path(__file__).parent
rows=[]
for path in sorted((P/'evidence').glob('web*.json')):
 data=json.loads(path.read_text())
 params=data.get('params',data.get('parameters',data.get('request',{})))
 if not params and any(k in data for k in ['open','find','system2_search_query','system1_search_query']):params=data
 result=data.get('response',data.get('result'))
 rows.append(dict(batch=path.stem,commands=json.dumps(params,ensure_ascii=False),response_present=result is not None))
with (P/'evidence/web_inventory.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['batch','commands','response_present'],delimiter='\t');w.writeheader();w.writerows(rows)
for r in rows:print(r['batch'],r['commands'])
