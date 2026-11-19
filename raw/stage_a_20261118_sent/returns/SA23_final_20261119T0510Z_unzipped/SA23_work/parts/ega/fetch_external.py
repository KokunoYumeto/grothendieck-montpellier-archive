#!/usr/bin/env python3
"""Fetch publicly accessible primary-source PDFs for local reading (not final redistribution)."""
from pathlib import Path
import urllib.request,hashlib,json,datetime,sys
base=Path(__file__).resolve().parents[3]
dest=base/'sources/external/ega'; dest.mkdir(parents=True,exist_ok=True)
urls={
 'EGAIII1.pdf':'https://www.numdam.org/article/PMIHES_1961__11__5_0.pdf',
 'SGA4_3.pdf':'https://library.slmath.org/nonmsri/sga/sga/pdf/sga4-3.pdf',
 'EGAIV1.pdf':'https://www.numdam.org/article/PMIHES_1964__20__5_0.pdf',
 'Cartier1956.pdf':'https://www.numdam.org/article/SSL_1955-1956__2__A4_0.pdf',
 'CartierExamples1956.pdf':'https://www.numdam.org/article/SSL_1955-1956__2__A5_0.pdf',
 'Nishimura2012.pdf':'https://projecteuclid.org/journals/kyoto-journal-of-mathematics/volume-52/issue-1/A-few-examples-of-local-rings-I/10.1215/21562261-1503754.pdf',
}
for name in sys.argv[1:] or urls:
    u=urls[name]
    try:
        if (dest/name).exists():data=(dest/name).read_bytes();status='existing'
        else:
            req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req,timeout=55) as r:data=r.read();status=r.status
            if not data.startswith(b'%PDF'):raise ValueError('Not PDF: '+data[:100].decode(errors='replace'))
            (dest/name).write_bytes(data)
        event=dict(file=name,url=u,status=status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    except Exception as e:event=dict(file=name,url=u,error=str(e),utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    with (Path(__file__).parent/'external_fetches.jsonl').open('a') as f:f.write(json.dumps(event)+'\n')
    print(json.dumps(event))
