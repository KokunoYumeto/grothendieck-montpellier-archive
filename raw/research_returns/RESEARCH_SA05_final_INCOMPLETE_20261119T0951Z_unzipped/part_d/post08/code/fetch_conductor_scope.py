"""Archive primary conductor/Weil reconstruction sources and exact retrieval results.

Raw PDFs are kept outside the packaged research tree.  Extracted text, this
reproducible script, and a hash/status manifest are retained in the work tree.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import urllib.request

HERE = Path(__file__).resolve().parents[1]
RAW = HERE.parents[2] / 'pending_post08_sources_d'
TEXT = HERE / 'sources'
OUT = HERE / 'output'
for directory in (RAW, TEXT, OUT):
    directory.mkdir(parents=True, exist_ok=True)

SOURCES = [
    ('Ochiai1999TraceMonodromy',
     'https://www.math.titech.ac.jp/top/~ochiai/lind.pdf'),
    ('DokchitserDokchitser2025Weil',
     'https://discovery.ucl.ac.uk/id/eprint/10205744/1/weil2-ems.pdf'),
    ('Kisin2026ArtinCharacterV1',
     'https://hexagonmath.org/pdf/2610.00597v1'),
    ('BeraldoPippi2025LocalizedIntersectionV1',
     'https://arxiv.org/pdf/2511.10527v1'),
    ('BeraldoPippi2024DeligneMilnorV1',
     'https://arxiv.org/pdf/2410.02327v1'),
]

def fetch(item):
    name, url = item
    record = {'name': name, 'url': url,
              'retrieved_utc': datetime.now(timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (research-source-archive)'})
        with urllib.request.urlopen(request, timeout=35) as response:
            data = response.read()
            record['final_url'] = response.url
            record['content_type'] = response.headers.get('Content-Type', '')
        if not data.startswith(b'%PDF'):
            raise ValueError('Response was not a PDF')
        pdf = RAW / (name + '.pdf')
        txt = TEXT / (name + '.txt')
        pdf.write_bytes(data)
        proc = subprocess.run(['pdftotext', '-layout', str(pdf), str(txt)],
                              capture_output=True, text=True, check=True)
        record.update(status='obtained', byte_count=len(data),
                      sha256=sha256(data).hexdigest(),
                      raw_pdf_path=str(pdf), text_path=str(txt),
                      extraction_stderr=proc.stderr)
    except Exception as error:
        record.update(status='failed', error=repr(error))
    return record

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=5) as pool:
        records = list(pool.map(fetch, SOURCES))
    target = OUT / 'conductor_source_fetch.json'
    target.write_text(json.dumps(records, indent=2) + '\n')
    print(json.dumps(records, indent=2))
