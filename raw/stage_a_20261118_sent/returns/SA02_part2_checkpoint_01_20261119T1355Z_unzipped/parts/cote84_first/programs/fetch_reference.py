"""Fetch an already opened public reference and optionally extract text.
All requests and statuses are retained, including errors; not an evidence grader.
"""
import argparse,datetime,json,urllib.request,subprocess
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('url');p.add_argument('name');p.add_argument('--first',type=int);p.add_argument('--last',type=int);a=p.parse_args()
out=Path(__file__).resolve().parent.parent/'outputs';target=out/a.name
event={'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':a.url,'name':a.name}
try:
 data=urllib.request.urlopen(a.url,timeout=45).read();target.write_bytes(data);event['bytes']=len(data)
 if a.name.endswith('.pdf'):
  cmd=['pdftotext','-layout']
  if a.first:cmd+=['-f',str(a.first)]
  if a.last:cmd+=['-l',str(a.last)]
  cmd+=[str(target),str(target.with_suffix('.txt'))]
  subprocess.run(cmd,check=True);event['text']=str(target.with_suffix('.txt'))
 event['result']='success'
except Exception as e:event.update(result='error',error=repr(e))
with(out/'fetch_log.jsonl').open('a')as f:f.write(json.dumps(event)+'\n')
print(json.dumps(event))
