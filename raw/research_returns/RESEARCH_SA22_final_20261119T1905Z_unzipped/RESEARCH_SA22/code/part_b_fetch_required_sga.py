#!/usr/bin/env python3
"""Fetch explicitly required original SGA scans from named public archives.

No theorem is certified by downloading a file. Exact opened passages are
recorded separately. Existing files are preserved and hash-checked.
"""
from pathlib import Path
import concurrent.futures, hashlib, json, subprocess, sys, time, urllib.request
root=Path(__file__).resolve().parents[1]
jobs=[
 ('sga4_original_tome1','https://wstein.org/sga/sga/pdf/sga4-1.pdf'),
 ('sga4_original_tome2','https://wstein.org/sga/sga/pdf/sga4-2.pdf'),
 ('sga4_original_tome3','https://wstein.org/sga/sga/pdf/sga4-3.pdf'),
 ('sga4half_original','https://publications.ias.edu/sites/default/files/Number32.pdf'),
 ('sga5_original','https://wstein.org/sga/sga5/SGA5.pdf'),
 ('sga6_original','https://wstein.org/sga/sga/pdf/sga6.pdf'),
]
output_name='part_b_fetch_required_sga_output.json'
if '--public-mirrors' in sys.argv:
 jobs=[
  ('sga4_complete_reedition','https://www.normalesup.org/~forgogozo/SGA4/tomes/SGA4.pdf'),
  ('sga4half_original','https://library.slmath.org/nonmsri/sga/sga/pdf/sga4h.pdf'),
  ('sga5_original','https://library.slmath.org/nonmsri/sga/sga5/SGA5.pdf'),
  ('sga6_original','https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf'),
 ]
 output_name='part_b_fetch_required_sga_mirrors_output.json'
started=time.monotonic()
def fetch(job):
 name,url=job;now=time.monotonic();p=root/'sources'/f'{name}.pdf';row={'name':name,'url':url}
 try:
  if not p.exists():
   with urllib.request.urlopen(url,timeout=60) as response:
    data=response.read();row['http_status']=response.status;row['content_type']=response.headers.get('Content-Type')
   if not data.startswith(b'%PDF'):raise ValueError('Response is not a PDF')
   p.write_bytes(data);row['fetch_status']='downloaded'
  else:data=p.read_bytes();row['fetch_status']='existing'
  row['bytes']=len(data);row['sha256']=hashlib.sha256(data).hexdigest()
  info=subprocess.run(['pdfinfo',str(p)],capture_output=True,text=True,timeout=30,check=True).stdout
  row['pages']=int(next(line.split(':',1)[1] for line in info.splitlines() if line.startswith('Pages:')))
  subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True,timeout=45,check=True)
  row['text_characters']=len(p.with_suffix('.txt').read_text())
 except Exception as exc:row['error']=str(exc)
 row['elapsed_seconds']=time.monotonic()-now
 print(json.dumps({k:v for k,v in row.items() if k!='sha256'}),flush=True)
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 results=list(pool.map(fetch,jobs))
output={'elapsed_seconds':time.monotonic()-started,'results':results}
(root/'code'/output_name).write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'completed':len(results),'errors':sum('error' in r for r in results),'elapsed_seconds':output['elapsed_seconds']}),flush=True)
