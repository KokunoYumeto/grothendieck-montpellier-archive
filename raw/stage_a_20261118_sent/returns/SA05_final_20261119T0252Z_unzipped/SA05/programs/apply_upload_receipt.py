#!/usr/bin/env python3
import sys,json,re,subprocess
from pathlib import Path
receipt_path,original_path=sys.argv[1:3]
data=json.loads(Path(receipt_path).read_text());objects=[]
def walk(x):
 if isinstance(x,dict):
  objects.append(x)
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
 elif isinstance(x,str):
  try:y=json.loads(x)
  except Exception:return
  if isinstance(y,(dict,list)):walk(y)
walk(data)
ids={x['library_file_id'] for x in objects if isinstance(x.get('library_file_id'),str)}
attrs=[x['xattrs'] for x in objects if isinstance(x.get('xattrs'),list)]
if len(ids)!=1:raise RuntimeError('Expected one exact uploaded Library id; found '+repr(ids))
file_id=next(iter(ids));applied=[]
helper=Path(__file__).resolve().parents[2]/'library_helpers'/'library_file_transfer.py'
for group in attrs:
 p=subprocess.run([sys.executable,str(helper),'apply-xattrs',original_path,file_id],input=json.dumps(group),text=True,capture_output=True)
 if p.returncode:raise RuntimeError(p.stderr or p.stdout)
 applied.append(p.stdout.strip())
result={'library_file_id':file_id,'original_path':original_path,'xattr_groups_applied':len(applied),'helper_output':applied}
out=Path(receipt_path).with_name(Path(receipt_path).stem+'_xattrs.json');out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
