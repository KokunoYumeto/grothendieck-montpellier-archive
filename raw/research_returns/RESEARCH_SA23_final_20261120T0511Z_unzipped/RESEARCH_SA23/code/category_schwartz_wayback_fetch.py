"""Read public archive metadata and its advertised closest original copies."""
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlencode,urlparse
import urllib.request
import hashlib,json,time

ROOT=Path(__file__).resolve().parents[1]
targets=[('historical_roots1982','http://sites.mathdoc.fr/OCLS/pdf/OCLS_1982__63__11_0.pdf'),
         ('souvenirs_dieudonne1994','http://sites.mathdoc.fr/OCLS/pdf/OCLS_1994c.pdf')]
rows=[]
for name,target in targets:
    started=time.monotonic()
    api='https://archive.org/wayback/available?'+urlencode({'url':target})
    row={'name':name,'target':target,'api':api,'started_utc':datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(api,timeout=25) as response:
            data=response.read()
            row['metadata_status']=response.status
        metadata=json.loads(data)
        mp=ROOT/'sources'/f'category_schwartz_{name}_wayback.json'
        mp.write_bytes(data);row['metadata_path']=str(mp.relative_to(ROOT))
        closest=metadata.get('archived_snapshots',{}).get('closest',{})
        row['closest']=closest
        if closest.get('available') and str(closest.get('status'))=='200':
            url=closest['url']
            if urlparse(url).hostname!='web.archive.org':raise ValueError('Unexpected archived-copy host')
            with urllib.request.urlopen(url,timeout=35) as response:
                data=response.read();row.update(status=response.status,final_url=response.url)
                if urlparse(response.url).hostname!='web.archive.org':raise ValueError('Unexpected redirect host')
            row.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),pdf=data.startswith(b'%PDF'))
            path=ROOT/'sources'/f'category_schwartz_{name}_archived'+Path('') if False else None
            suffix='pdf' if data.startswith(b'%PDF') else 'html'
            path=ROOT/'sources'/f'category_schwartz_{name}_archived.{suffix}'
            path.write_bytes(data);row['path']=str(path.relative_to(ROOT))
    except Exception as error:
        row['error']=repr(error)
    row['elapsed_seconds']=time.monotonic()-started;rows.append(row)
    print(json.dumps(row,ensure_ascii=False),flush=True)
    (ROOT/'logs/category_schwartz_wayback_fetch.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
