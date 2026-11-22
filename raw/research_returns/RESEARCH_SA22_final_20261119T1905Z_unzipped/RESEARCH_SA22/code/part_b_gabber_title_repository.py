#!/usr/bin/env python3
"""Public title/author query, allowing records without the published DOI."""
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen,Request
import json,time
root=Path(__file__).resolve().parents[1];start=time.monotonic()
url='https://api.openaire.eu/search/publications?'+urlencode({'title':'affine base change','author':'Gabber','format':'json','size':25})
r={'url':url,'scope':'Public metadata search by title keywords and author; no DOI/year/OA restriction, allowing earlier preprints and variant analog/analogue spellings','documentation':'https://graph.openaire.eu/docs/10.2.0/apis/search-api/research-products/'}
try:
 with urlopen(Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0','Accept':'application/json'}),timeout=30) as f:raw=f.read(2*1024*1024+1);r.update(http_status=f.status,bytes=len(raw),content_type=f.headers.get('Content-Type',''))
 if len(raw)>2*1024*1024:r['status']='Response cap reached; no complete result'
 else:r.update(status='Metadata read',metadata=json.loads(raw))
except Exception as e:r.update(status='error',error=str(e))
r['elapsed_seconds']=time.monotonic()-start
(root/'code/part_b_gabber_title_repository_output.json').write_text(json.dumps({'results':[r],'elapsed_seconds':r['elapsed_seconds']},indent=2)+'\n')
print(json.dumps({k:v for k,v in r.items() if k!='metadata'},indent=2))
if 'metadata' in r:print('total',r['metadata'].get('response',{}).get('header',{}).get('total'))
