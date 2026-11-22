"""Follow the author's actual bibliographic link, preserving the retrieval.

Copies are retained for this private research audit, not for public reposting.
"""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urljoin
import re
import hashlib
import subprocess

root = Path(__file__).resolve().parents[1]
url = 'https://math.caltech.edu/simon/biblio.html'
with urlopen(url, timeout=28) as response:
    data = response.read()
    print('INDEX_STATUS', response.status)
    print('INDEX_URL', response.geturl())
path = root / 'notes/category_Simon_author_bibliography.html'
path.write_bytes(data)
text = data.decode('utf-8', errors='replace')
where = text.lower().find('notes on infinite determinants')
print('TITLE_POSITION', where)
paragraph = text[max(0, where-100):where+1400]
print('EXACT_LINK_CONTEXT', paragraph, flush=True)
links = re.findall(r'''href\s*=\s*["']([^"']+)["']''', paragraph, re.I)
print('LINKS_IN_CONTEXT', links, flush=True)
for candidate in links:
    if not candidate.lower().endswith('.pdf'):
        continue
    target = urljoin(url, candidate)
    print('REQUESTED_PDF', target, flush=True)
    try:
        with urlopen(target, timeout=28) as response:
            pdfdata = response.read()
            print('FINAL_PDF', response.geturl(), 'STATUS', response.status)
        if not pdfdata.startswith(b'%PDF'):
            print('NOT_A_PDF', len(pdfdata))
            continue
        destination = root / 'notes/category_Simon1977.pdf'
        destination.write_bytes(pdfdata)
        print('PDF_BYTES', len(pdfdata), 'SHA256', hashlib.sha256(pdfdata).hexdigest())
        result = subprocess.run(['pdftotext', '-layout', str(destination), str(destination.with_suffix('.txt'))], text=True, capture_output=True)
        print('PDFTOTEXT_STATUS', result.returncode, 'STDERR', result.stderr)
        break
    except Exception as exc:
        print('PDF_FAILED', type(exc).__name__, str(exc), flush=True)
