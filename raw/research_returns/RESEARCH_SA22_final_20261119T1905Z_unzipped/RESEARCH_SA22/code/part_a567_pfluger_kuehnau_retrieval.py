"""Retrieve the observed public GDZ later original; never a proxy for Pfluger 1960."""
from pathlib import Path
import hashlib, json, time, urllib.request
import fitz

base = Path(__file__).resolve().parents[1]
url = 'https://gdz.sub.uni-goettingen.de/download/pdf/PPN358147735_0069/LOG_0024.pdf'
dest = base / 'sources/part_a567_pfluger_kuehnau1994.pdf'
started = time.perf_counter()
record = {'url': url, 'scope': 'Later joint 1994 original, first and final mathematical pages; not target 1960 original.'}
try:
    with urllib.request.urlopen(url, timeout=50) as response:
        data = response.read()
        record.update(status=response.status, final_url=response.url, content_type=response.headers.get('Content-Type'), bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    if not data.startswith(b'%PDF'):
        raise ValueError('Response is not PDF; no further endpoint requested')
    dest.write_bytes(data)
    doc = fitz.open(dest)
    record['pdf_pages'] = len(doc)
    record['rendered_pdf_pages_one_based'] = [2, len(doc)]
    for index in [1, len(doc)-1]:
        doc[index].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(base / f'sources/part_a567_pfluger_kuehnau1994_pdf{index+1}.png')
except Exception as error:
    record['error'] = str(error)
record['runtime_seconds'] = time.perf_counter() - started
(base / 'code/part_a567_pfluger_kuehnau_retrieval_output.json').write_text(json.dumps(record, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(record, ensure_ascii=False, indent=2))
