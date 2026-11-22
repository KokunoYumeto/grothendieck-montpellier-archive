#!/usr/bin/env python3
"""Fetch the observed public EGA I new-edition source and locate §7.2."""
from pathlib import Path
from datetime import datetime,timezone
import urllib.request,hashlib,json,time,re
import fitz
root=Path(__file__).resolve().parents[1]
url='https://wstein.org/sga/ega1.pdf'
record={'url':url,'started_utc':datetime.now(timezone.utc).isoformat()}
start=time.perf_counter()
try:
 with urllib.request.urlopen(url,timeout=60) as response:
  payload=response.read()
  record.update({'status':response.status,'final_url':response.url,
    'content_type':response.headers.get('content-type'),'bytes':len(payload),
    'sha256':hashlib.sha256(payload).hexdigest()})
 if payload.startswith(b'%PDF'):
  path=root/'literature/ROOT_EGAI_newedition.pdf';path.write_bytes(payload)
  doc=fitz.open(path); text='\f'.join(p.get_text() for p in doc)
  path.with_suffix('.txt').write_text(text)
  hits=[]
  for n,page in enumerate(doc):
   t=page.get_text()
   if re.search(r'morcel|morceaux|Néron|NÉRON|7\.2\.3',t,re.I):
    hits.append({'pdf_page':n+1,'text':t})
  record.update({'pages':len(doc),'characters':len(text),'hits':hits})
 else:record['error']='Not a PDF; source not opened.'
except Exception as error:record['error']=repr(error)
record['seconds']=round(time.perf_counter()-start,4)
(root/'logs/ROOT_EGAI_newedition_fetch.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='hits'},indent=2))
print('Matching PDF pages:',[x['pdf_page'] for x in record.get('hits',[])])
