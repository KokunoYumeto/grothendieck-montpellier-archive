#!/usr/bin/env python3
"""Read public primary-source PDFs; cache excluded from deliverable archives."""
import argparse, json, datetime, subprocess, urllib.request
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('name');p.add_argument('url');p.add_argument('--pages',nargs='*',type=int,default=[]);a=p.parse_args()
w=Path(__file__).resolve().parents[1];d=w/'cache_sources';d.mkdir(exist_ok=True)
f=d/(a.name+'.pdf')
req=urllib.request.Request(a.url,headers={'User-Agent':'Mozilla/5.0 (scholarly source verification)'})
try:
 if not f.exists():
  with urllib.request.urlopen(req,timeout=40) as r:f.write_bytes(r.read())
 if f.read_bytes()[:4]!=b'%PDF':raise ValueError('Response is not a PDF')
 subprocess.run(['pdftotext','-layout',str(f),str(d/(a.name+'.txt'))],check=True,capture_output=True)
 imgs=[]
 for pg in a.pages:
  pref=d/(a.name+'_'+str(pg));subprocess.run(['pdftoppm','-f',str(pg),'-singlefile','-scale-to','1800','-png',str(f),str(pref)],check=True,capture_output=True);imgs.append(str(pref)+'.png')
 result={'name':a.name,'url':a.url,'bytes':f.stat().st_size,'pdf':str(f),'images':imgs,'status':'downloaded and rendered','at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
except Exception as e:result={'name':a.name,'url':a.url,'status':'failed','error':str(e)}
out=w/'research'/('source_'+a.name+'.json');out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
