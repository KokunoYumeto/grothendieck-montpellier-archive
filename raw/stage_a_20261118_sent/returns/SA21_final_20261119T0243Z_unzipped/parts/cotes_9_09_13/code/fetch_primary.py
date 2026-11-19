"""Retrieve named public primary sources with logged HTTP/extraction outcomes."""
from pathlib import Path
import urllib.request,subprocess,datetime,json,sys
ROOT=Path(__file__).resolve().parents[1]
catalog={'shmuely1974':'https://msp.org/pjm/1974/54-2/pjm-v54-n2-p15-p.pdf','ischi2010':'https://arxiv.org/pdf/1109.1658','coecke_moore2000':'https://arxiv.org/pdf/quant-ph/0008021','paseka_vetterlein2025':'https://arxiv.org/pdf/2501.04482v3'}
for key in sys.argv[1:]:
    rec={'key':key,'url':catalog[key],'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        req=urllib.request.Request(catalog[key],headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=40) as r:
            data=r.read();rec.update(status=r.status,final_url=r.url,bytes=len(data),content_type=r.headers.get('Content-Type'))
        if data.startswith(b'%PDF'):
            p=ROOT/'outputs'/f'{key}.pdf';p.write_bytes(data)
            q=subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True,text=True)
            rec.update(extract_exit=q.returncode,extract_stderr=q.stderr)
    except Exception as e:rec['error']=str(e)
    (ROOT/'outputs'/f'{key}_fetch.json').write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps(rec),flush=True)
