#!/usr/bin/env python3
"""Bounded original-volume text search; an OCR negative is not an absence proof."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, time, unicodedata
import urllib.request
import fitz

root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
record = {'started_utc':datetime.now(timezone.utc).isoformat(), 'local_volumes':[], 'remote_volumes':[]}
patterns = [r'morcel', r'morceaux', r'foncteur.{0,45}neron', r'neron.{0,45}foncteur', r'partition.{0,45}constructib']
def scan(text):
    normalized = ''.join(c for c in unicodedata.normalize('NFKD',text) if not unicodedata.combining(c)).lower()
    found=[]
    for pattern in patterns:
        for match in re.finditer(pattern,normalized):
            found.append({'pattern':pattern,'character':match.start(),
                          'context':normalized[max(0,match.start()-160):match.end()+220]})
    return found

for name in ['C_EGA_IV4.txt','C_SGA4_tome3.txt','B_SGA6_1971.txt','A567_SGA1_2003.txt','B_SGA2_2005.txt']:
    path=root/'literature'/name
    raw=path.read_bytes(); text=raw.decode('utf-8',errors='replace')
    record['local_volumes'].append({'path':str(path.relative_to(root)), 'bytes':len(raw),
      'sha256':hashlib.sha256(raw).hexdigest(),'hits':scan(text),
      'scope':'Text-layer search only. SGA6 has a sparse text layer; zero hits there are inconclusive.'})

url='https://www.iut-theory.org/divers/SGA7I.pdf'
entry={'url':url}
try:
    with urllib.request.urlopen(url,timeout=60) as response:
        payload=response.read()
        entry.update({'status':response.status,'final_url':response.url,
                      'content_type':response.headers.get('content-type'),'bytes':len(payload),
                      'sha256':hashlib.sha256(payload).hexdigest()})
    if entry['status']==200 and payload.startswith(b'%PDF'):
        path=root/'literature/ROOT_SGA7I.pdf'; path.write_bytes(payload)
        doc=fitz.open(path); text='\f'.join(p.get_text() for p in doc)
        path.with_suffix('.txt').write_text(text)
        entry.update({'pages':len(doc),'characters':len(text),'hits':scan(text),
                      'scope':'Full PDF text layer searched; relevant hits must still be read in page context.'})
    else:
        entry['scope']='No valid PDF obtained. No authentication or challenge workaround attempted.'
except Exception as error:
    entry['error']=repr(error)
record['remote_volumes'].append(entry)
record['seconds']=round(time.perf_counter()-started,4)
record['ended_utc']=datetime.now(timezone.utc).isoformat()
(root/'logs/ROOT_subject11_textsearch.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False,indent=2))
