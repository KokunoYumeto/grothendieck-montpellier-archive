"""Follow the actual archive playback links and one author-hosted interview."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
import urllib.request
import re,hashlib,json,time,subprocess

ROOT=Path(__file__).resolve().parents[1]
jobs=[]
for name in ['historical_roots1982','souvenirs_dieudonne1994']:
    wrapper=ROOT/'sources'/f'category_schwartz_{name}_archived.html'
    match=re.search(r'<iframe\s+id="playback"\s+src="([^"]+)"',wrapper.read_text())
    if match is None:raise ValueError('No advertised playback URL')
    url=match.group(1)
    if urlparse(url).hostname!='web.archive.org':raise ValueError('Unexpected playback host')
    jobs.append((name,url,'web.archive.org'))
jobs.append(('dialogues1997','https://cermics.enpc.fr/~bouleaun/DIALOGUES.juin97.pdf','cermics.enpc.fr'))

def fetch(job):
    name,url,host=job;start=time.monotonic()
    row={'name':name,'url':url,'started_utc':datetime.now(timezone.utc).isoformat()}
    class SafeRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self,req,fp,code,msg,headers,newurl):
            if urlparse(newurl).hostname!=host:raise ValueError('Unexpected redirect host')
            return super().redirect_request(req,fp,code,msg,headers,newurl)
    try:
        opener=urllib.request.build_opener(SafeRedirect)
        with opener.open(url,timeout=35) as response:
            data=response.read();row.update(status=response.status,final_url=response.url)
        if not data.startswith(b'%PDF'):raise ValueError('Response is not a PDF')
        pdf=ROOT/'sources'/f'category_schwartz_{name}.pdf';pdf.write_bytes(data)
        row.update(path=str(pdf.relative_to(ROOT)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        txt=pdf.with_suffix('.txt')
        command=['pdftotext','-layout',str(pdf),str(txt)]
        proc=subprocess.run(command,capture_output=True,timeout=40)
        row['extraction']={'command':command,'status':proc.returncode,'stderr':proc.stderr.decode(errors='replace')}
        info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,timeout=20)
        row['pdfinfo']=info.stdout.decode(errors='replace')
        row['extracted_text_path']=str(txt.relative_to(ROOT)) if txt.exists() else None
    except Exception as error:row['error']=repr(error)
    row['elapsed_seconds']=time.monotonic()-start
    return row

rows=[]
with ThreadPoolExecutor(max_workers=3) as pool:
    for future in as_completed([pool.submit(fetch,job) for job in jobs]):
        row=future.result();rows.append(row);print(json.dumps(row,ensure_ascii=False),flush=True)
        (ROOT/'logs/category_schwartz_primary_payloads.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
