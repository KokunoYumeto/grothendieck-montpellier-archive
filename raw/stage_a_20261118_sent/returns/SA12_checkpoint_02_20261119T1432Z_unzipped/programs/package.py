#!/usr/bin/env python3
"""Package a complete work snapshot; do not redistribute external source texts.

Public-source retrieval responses are represented by request, URL, citation ID,
and response hash. User-provided transcription excerpts remain in the audit.
External books, rendered source pages, earlier archives, and attachments are not
part of the deliverable. Run with --checkpoint N only when the interval is due.
"""
from pathlib import Path
import argparse,datetime,hashlib,json,re,zipfile
p=argparse.ArgumentParser();p.add_argument('--checkpoint',type=int);p.add_argument('--final',action='store_true');a=p.parse_args()
root=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc)
start=datetime.datetime.fromisoformat('2026-11-19T13:01:58.167443+00:00')
if a.checkpoint:
    due=start+datetime.timedelta(minutes=45*a.checkpoint)
    if now<due:raise SystemExit('Checkpoint interval has not elapsed: '+due.isoformat())
    name=f'SA12_checkpoint_{a.checkpoint:02}.zip'
elif a.final:name='SA12.zip'
else:raise SystemExit('Choose --checkpoint N or --final')
target=root.parent/name
if target.exists():raise SystemExit('Refusing to overwrite '+str(target))
manifest=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def source_metadata(path,data):
    obj=json.loads(data)
    request=obj.get('args',obj.get('request',obj.get('queries',None))) if isinstance(obj,dict) else None
    raw=json.dumps(obj,ensure_ascii=False)
    urls=sorted(set(x.rstrip('.,;)\\') for x in re.findall(r'https?://[^\s<>"\x00]+',raw)))
    refs=sorted(set(re.findall(r'turn\d+[a-z]+\d+',raw)))
    return (json.dumps({'retrieval_file':str(path),'request':request,'urls':urls,'citation_ids':refs,'raw_response_sha256':sha(data),'raw_response_bytes':len(data),'note':'External source prose omitted from distributed audit; queries, source locators, hashes, and the researchers\' own evaluations are retained.'},ensure_ascii=False,indent=2)+'\n').encode()
with (root/'progress.log').open('a') as f:f.write(now.isoformat()+'\t'+('CHECKPOINT '+str(a.checkpoint) if a.checkpoint else 'FINAL PACKAGE')+'\t'+name+'\n')
with zipfile.ZipFile(target,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for path in sorted(root.rglob('*')):
        if not path.is_file():continue
        rel=path.relative_to(root)
        if any(s in rel.parts for s in ('reference_cache','external','__pycache__')):continue
        if path.suffix.lower() in ('.zip','.pdf','.png','.jpg','.jpeg','.pyc'):continue
        data=path.read_bytes();mode='original'
        if path.suffix=='.json' and (path.name.startswith('web') or path.name.startswith('search_audit_')):
            try:data=source_metadata(rel,data);mode='source-metadata'
            except (ValueError,TypeError):pass
        elif path.suffix=='.txt' and path.name.startswith('primary_'):
            data=(json.dumps({'output_file':str(rel),'sha256':sha(data),'bytes':len(data),'note':'External-source excerpt output omitted; source and line locators are recorded in primary_read_log.tsv; the executable reader is included.'},indent=2)+'\n').encode();mode='source-metadata'
        z.writestr(str(rel),data)
        manifest.append({'path':str(rel),'bytes':len(data),'sha256':sha(data),'mode':mode})
    z.writestr('ARCHIVE_MANIFEST.json',json.dumps({'archive':name,'utc':now.isoformat(),'files':manifest,'excluded':'Supplied attachments and extracted sources; external full books and source-page images; earlier checkpoints; transient bytecode.'},indent=2)+'\n')
result={'path':str(target),'bytes':target.stat().st_size,'sha256':sha(target.read_bytes()),'files':len(manifest),'utc':now.isoformat()}
(root/'outputs'/(target.stem+'_package.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
