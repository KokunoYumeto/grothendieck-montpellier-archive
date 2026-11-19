"""Finalize the first timed snapshot before its first persistent upload.
A duplicate pending process captured raw external tool excerpts; omit those cache
bodies from this still-unpublished first artifact. No saved checkpoint is changed.
"""
import zipfile,io,pathlib,json,datetime,hashlib,re
p=pathlib.Path('SA08_checkpoint_01.zip');data=p.read_bytes();out=io.BytesIO();removed=[];audit={}
with zipfile.ZipFile(io.BytesIO(data)) as src,zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=8) as dst:
 for name in src.namelist():
  body=src.read(name)
  if (name.startswith('logs/') and 'search' in name) or name=='work/late/Garvin1998.txt':
   removed.append(name)
   if name.endswith('.json'):
    try:r=json.loads(body)
    except Exception:r={}
    raw=body.decode(errors='replace');audit[name]={'request':r.get('request',r.get('query',r.get('queries'))) if isinstance(r,dict) else None,'urls':sorted(set(re.findall(r'https?://[^\s<>"\\)]+',raw))),'source_refs':sorted(set(re.findall(r'turn\d+(?:search|view|fetch)\d+',raw))),'sha256':hashlib.sha256(body).hexdigest()}
   continue
  dst.writestr(name,body)
 dst.writestr('research/additional_retrieval_audit.json',json.dumps(audit,indent=2,ensure_ascii=False))
 dst.writestr('FIRST_SNAPSHOT_FINALIZATION.json',json.dumps({'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'omitted_external_source_cache':removed,'reason':'Keep retrieval metadata and original authored analyses; do not redistribute published full texts or extended tool excerpts. First persistent upload follows this finalization.'},indent=2))
 dst.writestr('programs/finalize_first_snapshot.py',pathlib.Path(__file__).read_text())
p.write_bytes(out.getvalue())
with zipfile.ZipFile(p) as z:assert z.testzip() is None
print(json.dumps({'archive':str(p.resolve()),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'finalized_before_first_upload':True}))
