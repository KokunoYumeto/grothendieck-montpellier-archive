#!/usr/bin/env python3
"""Package all authored work, excluding supplied/full-text source caches.
Web retrieval bodies are replaced inside the ZIP by a source-access audit:
the authors' results are described in our own ledgers, not redistributed whole.
"""
import json,sys,hashlib,re,zipfile,datetime
from pathlib import Path
root=Path(__file__).resolve().parents[2];base=root/'SA05'
name=sys.argv[1]
if not re.fullmatch(r'SA05(?:_checkpoint_\d\d)?\.zip',name):raise ValueError(name)
out=root/name
if out.exists():raise FileExistsError('Never overwrite a checkpoint or delivered archive: '+str(out))
entries=[];omitted=[]
def audit_web(data):
 text=data.decode('utf-8',errors='replace')
 urls=sorted(set(re.findall(r'https?://[^\s"<>\\)]+',text)))
 ids=sorted(set(re.findall(r'turn\d+(?:view|search|academia)\d+',text)))
 return json.dumps({'source_access_audit':True,'raw_result_sha256':hashlib.sha256(data).hexdigest(),
  'urls':urls,'retrieval_ids':ids,'note':'Published source text is not redistributed. Exact checked statements, locators, access limits and judgments are in the authored reference/search/proof ledgers.'},ensure_ascii=False,indent=2).encode()+b'\n'
with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=8) as z:
 for p in sorted(base.rglob('*')):
  if not p.is_file():continue
  rel=p.relative_to(base)
  if '__pycache__' in rel.parts or 'readouts' in rel.parts or p.suffix in {'.pyc','.zip','.pdf','.png'}:
   omitted.append(str(rel));continue
  data=p.read_bytes();mode='authored file or program output'
  if p.suffix=='.json' and ('searches' in rel.parts or 'web' in rel.parts) and not (p.name.startswith('search_queries') or p.name=='search_ledger.json'):
   data=audit_web(data);mode='source-access audit replacing fetched copyrighted source body'
  z.writestr('SA05/'+str(rel),data)
  entries.append({'path':str(rel),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'mode':mode})
 manifest={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
  'archive':name,'entries':entries,'source_cache_and_generated_bytecode_exclusions':omitted,
  'restore':'Unzip beside the supplied attachments; run bootstrap.py if the source folders need reconstructing. Original attachments and full published source caches are intentionally not included.'}
 z.writestr('SA05/ARCHIVE_MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
receipt={'archive':str(out),'bytes':out.stat().st_size,'files':len(entries),'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}
(base/'programs'/'outputs'/('pack_'+out.stem+'.json')).write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
