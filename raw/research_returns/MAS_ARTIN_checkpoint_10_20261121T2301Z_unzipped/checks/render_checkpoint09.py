"""Render changed pages for explicit visual inspection; this does not certify them."""
from pathlib import Path
import hashlib
import json
import re
import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / 'MAS_ARTIN.pdf'
OUT = ROOT.parent / 'private_sources' / 'qa' / 'cp09final'
OUT.mkdir(parents=True, exist_ok=True)
doc = fitz.open(PDF)
texts = [page.get_text() for page in doc]
new_pages = []
for i, text in enumerate(texts):
    numbers = [int(x) for x in re.findall(r'MA-MO\.(\d+)', text)]
    if any(210 <= number <= 549 for number in numbers):
        new_pages.append(i + 1)
assert new_pages, 'Expected new operator modules were not located'
start, end = max(1, min(new_pages)-1), min(len(doc), max(new_pages)+2)
pages = set(range(1, 11)) | set(range(start, end+1))
pages.update(range(max(1, len(doc)-7), len(doc)+1))
for i, text in enumerate(texts):
    if 'Unchecked findings' in text or 'Unproved findings' in text:
        pages.update(range(max(1, i), min(len(doc), i+4)+1))
pages = sorted(pages)
for j in range(0, len(pages), 4):
    group = pages[j:j+4]
    sheet = Image.new('RGB', (1200, 1750), 'white')
    draw = ImageDraw.Draw(sheet)
    for k, number in enumerate(group):
        pix = doc[number-1].get_pixmap(matrix=fitz.Matrix(1.2, 1.2), alpha=False)
        im = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
        im.thumbnail((585, 835))
        x = (k % 2)*600 + (600-im.width)//2
        y = (k // 2)*875 + 25
        sheet.paste(im, (x, y))
        draw.text(((k % 2)*600+15, (k // 2)*875+5), f'Page {number}', fill='black')
    sheet.save(OUT / f'sheet_{j//4+1:02d}.png')
report = {'pdf_sha256': hashlib.sha256(PDF.read_bytes()).hexdigest(),
          'pdf_pages': len(doc), 'new_module_span_with_neighbors': [start, end],
          'rendered_pages': pages, 'sheets': (len(pages)+3)//4,
          'scope': 'Rendering only. An actual subsequent image inspection is required before any visual pass.'}
(OUT / 'render_report.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
