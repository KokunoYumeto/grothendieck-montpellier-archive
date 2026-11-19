"""Download publicly accessible primary reference into a reading cache.
The cache is not a deliverable and must be excluded from checkpoint/final ZIPs.
"""
import urllib.request,subprocess,hashlib,json
from pathlib import Path
from datetime import datetime,timezone
OUT=Path(__file__).resolve().parent
CACHE=OUT/'reference_cache';CACHE.mkdir(exist_ok=True)
refs=[('SGA7-I','https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf')]
for key,url in refs:
    pdf=CACHE/(key+'.pdf');txt=CACHE/(key+'.txt')
    if not pdf.exists():
        with urllib.request.urlopen(url,timeout=45) as r:
            data=r.read();status=r.status
        pdf.write_bytes(data)
    else: data=pdf.read_bytes();status='cached prior HTTP 200'
    cp=subprocess.run(['pdftotext','-layout',str(pdf),str(txt)],capture_output=True,text=True)
    print(json.dumps(dict(key=key,url=url,status=status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
       opened_utc=datetime.now(timezone.utc).isoformat(),pdf=str(pdf),text=str(txt),
       extract_returncode=cp.returncode,extract_stderr=cp.stderr),ensure_ascii=False))
