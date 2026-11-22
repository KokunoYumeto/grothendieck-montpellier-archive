#!/usr/bin/env python3
"""Extract original printed pp32-51 from PDF pages40-59 of PLMS33."""
import hashlib
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source = root/'sources/gabriel1932_volume33.pdf'
outdir = root/'sources/gabriel1932_pages'
outdir.mkdir(exist_ok=True)
start=time.perf_counter()
out={'started_utc':datetime.now(timezone.utc).isoformat(),'commands':[]}

def run(cmd):
    t=time.perf_counter()
    p=subprocess.run(cmd,capture_output=True,text=True)
    out['commands'].append({'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'runtime_seconds':time.perf_counter()-t})
    if p.returncode:
        raise RuntimeError('Extraction command failed')

try:
    run(['pdfseparate','-f','40','-l','59',str(source),str(outdir/'sheet-%d.pdf')])
    article=root/'sources/gabriel1932.pdf'
    run(['pdfunite']+[str(outdir/f'sheet-{i}.pdf') for i in range(40,60)]+[str(article)])
    run(['pdftotext','-layout',str(article),str(root/'sources/gabriel1932.txt')])
    for printed in (32,33,34,38,40,42,46,49,51):
        page=printed-31
        run(['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-r','145','-png',str(article),str(outdir/f'printed-{printed}')])
    out.update(article=str(article.relative_to(root)),article_bytes=article.stat().st_size,article_sha256=hashlib.sha256(article.read_bytes()).hexdigest(),printed_pages='32-51',pdf_pages_in_volume='40-59',rendered_pages=[32,33,34,38,40,42,46,49,51])
except Exception as e:
    out['error']=f'{type(e).__name__}: {e}'
out['runtime_seconds']=time.perf_counter()-start
Path(__file__).with_name('part_c_gabriel_article_extract_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
