#!/usr/bin/env python3
"""Apply returned Library metadata to a newly uploaded checkpoint/final ZIP."""
import sys,json,subprocess
from pathlib import Path
data=json.loads(Path(sys.argv[1]).read_text());path=Path(sys.argv[2]).resolve()
def walk(x):
 if isinstance(x,dict):
  yield x
  for v in x.values():yield from walk(v)
 elif isinstance(x,list):
  for v in x:yield from walk(v)
 elif isinstance(x,str) and x.lstrip().startswith(('{','[')):
  try:yield from walk(json.loads(x))
  except (ValueError,TypeError):pass
objs=list(walk(data));ids=[o['library_file_id'] for o in objs if isinstance(o.get('library_file_id'),str)]
if not ids:raise RuntimeError('Upload result did not supply a Library file ID')
ids=list(dict.fromkeys(ids))
if len(ids)!=1:raise RuntimeError('Ambiguous Library IDs in single-file upload result')
attrs=[]
for o in objs:
 if isinstance(o.get('xattrs'),list):attrs.extend(o['xattrs'])
attrs=list({a['name']:a for a in attrs if isinstance(a,dict) and 'name'in a and'value'in a}.values())
helper=Path(__file__).parent/'library_file_transfer.py'
subprocess.run([sys.executable,str(helper),'apply-xattrs',str(path),ids[0]],input=json.dumps(attrs),text=True,check=True)
record={'file':path.name,'library_file_id':ids[0],'metadata_applied':True,'url':'https://chatgpt.com/library?file_id='+ids[0]+'&account_id=personal'}
(path.parent/(path.stem+'_saved.json')).write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
