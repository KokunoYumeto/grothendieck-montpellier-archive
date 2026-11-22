"""Download the publicly listed original Lidskii issue PDF and render pp.485–487."""
from pathlib import Path
import urllib.request,json,time,hashlib,subprocess
root=Path(__file__).resolve().parents[1]
ident='rossiiskaya-akademiya-nauk-doklady_1959-03-21_125_3'
url='https://archive.org/download/'+ident+'/'+ident+'.pdf'
record={'url':url}; start=time.perf_counter()
try:
    with urllib.request.urlopen(url,timeout=30) as f:
        data=f.read(); record.update(status=f.status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    p=root/'sources/algebra_history_lidskii_original_issue.pdf';p.write_bytes(data)
    record['file']=str(p.relative_to(root))
    r=subprocess.run(['pdfinfo',str(p)],capture_output=True,text=True);record['pdfinfo']=r.stdout
    for page in (22,23,24):
        out=root/('sources/algebra_history_lidskii_original_pdfp%03d'%page)
        r=subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','2200','-png',str(p),str(out)],capture_output=True,text=True)
        record.setdefault('renders',[]).append({'page':page,'output':str(out)+'.png','returncode':r.returncode,'stderr':r.stderr})
except Exception as e: record['error']=repr(e)
record['elapsed_seconds']=round(time.perf_counter()-start,6)
(root/'logs/algebra_history_fetch06.json').write_text(json.dumps(record,indent=2,ensure_ascii=False))
print(json.dumps(record,indent=2,ensure_ascii=False))
