"""Read the public preview explicitly advertised by the actual chapter page."""
from pathlib import Path
import hashlib,json,subprocess,time,urllib.request
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
url='https://page-one.springer.com/pdf/preview/10.1007/BFb0059509'
out=dict(url=url,scope='Advertised public preview only; no full-book access claim')
try:
    with urllib.request.urlopen(url,timeout=30) as response:
        body=response.read();out.update(status=response.status,final_url=response.url,content_type=response.headers.get('content-type'))
    out.update(bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),pdf_magic=body.startswith(b'%PDF-'))
    target=ROOT/'sources/root_raynaud_picard_preview.pdf'
    if out['pdf_magic']:
        target.write_bytes(body)
        result=subprocess.run(['pdftotext','-layout',str(target),str(target.with_suffix('.txt'))],capture_output=True,text=True)
        out['text_exit']=result.returncode
        info=subprocess.run(['pdfinfo',str(target)],capture_output=True,text=True)
        out['pdfinfo']=info.stdout
        render=subprocess.run(['pdftoppm','-f','1','-l','1','-r','120','-singlefile','-png',str(target),str(ROOT/'qa/root_raynaud_picard_preview')],capture_output=True,text=True)
        out['render_exit']=render.returncode
    else:
        (ROOT/'sources/root_raynaud_picard_preview_response.bin').write_bytes(body)
except Exception as exc:out['error']=str(exc)
out['seconds']=time.perf_counter()-START
(ROOT/'code/root_raynaud_advertised_preview_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
