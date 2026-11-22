"""Locate the exact residual overflow in the final PDF, then render it if absent."""
from pathlib import Path
import datetime, hashlib, json
import fitz
w = Path(__file__).resolve().parents[1]
d = fitz.open(w / 'RESEARCH_SA15_paper.pdf')
pending_path = w / 'outputs/visual_qa25_pending.json'
pending = json.loads(pending_path.read_text())
assert pending['pdf_sha256'] == hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
phrase = 'asserted integral inverse formula'
pages = [i+1 for i, p in enumerate(d) if phrase in ' '.join(p.get_text().split())]
assert len(pages) == 1, pages
new = sorted(set(pages) - set(pending['pages_rendered']))
for n in new:
    d[n-1].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(w/f'outputs/qa25/page_{n:03d}.png')
pending['pages_rendered'] = sorted(set(pending['pages_rendered']) | set(pages))
pending['exact_remaining_overflow_pages'] = pages
pending_path.write_text(json.dumps(pending, indent=2)+'\n')
record = {'actual_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'phrase': phrase, 'pages': pages, 'additional_pages_rendered': new,
          'scope': 'Text location and render only; subsequent actual image view required.'}
dest = w/'outputs/exact_overflow_location25.json'
assert not dest.exists()
dest.write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
