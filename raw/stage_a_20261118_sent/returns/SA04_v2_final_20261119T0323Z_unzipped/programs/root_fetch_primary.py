"""Fetch a specified public primary source for local research, excluding its text from deliverables."""
import sys, urllib.request, hashlib, json, datetime
from pathlib import Path
url,name=sys.argv[1:]
dest=Path('/tmp/SA04_root_external');dest.mkdir(exist_ok=True)
record={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':url,'local_temporary_name':name}
try:
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (scholarly source verification)'})
    with urllib.request.urlopen(req,timeout=45) as response:
        data=response.read();record['content_type']=response.headers.get('Content-Type');record['resolved_url']=response.url
    file=dest/name;file.write_bytes(data)
    record.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    if data[:4]==b'%PDF':
        import fitz
        doc=fitz.open(file);record['pages']=len(doc)
        (dest/(name+'.txt')).write_text('\n'.join(f'\nPDF_PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc)))
        record['text_extracted']=True
    record['status']='downloaded'
except Exception as e:record.update(status='failed',error=str(e))
out=Path(__file__).resolve().parents[1]/'outputs'/('root_fetch_'+name+'.json')
out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
with (out.parents[1]/'progress.log').open('a') as log:log.write(record['utc']+'\tprimary_source_fetch\t'+url+'; '+record['status']+'\n')
