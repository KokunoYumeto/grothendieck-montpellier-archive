"""Retrieve the complete cote 1 scan and make documentary contact sheets.

The sheets locate dated correspondence; they do not certify a reading of
small mathematical handwriting. Full-sized page renders are made separately.
"""
from pathlib import Path
import argparse
import hashlib, json, time, urllib.request
import fitz
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--source-filename', default='root_manuscript1.pdf')
source = root / 'sources' / parser.parse_args().source_filename
started = time.perf_counter()
url = 'https://grothendieck.umontpellier.fr/1.pdf'
if not source.exists():
    with urllib.request.urlopen(url, timeout=180) as response:
        content = response.read()
    source.write_bytes(content)
else:
    content = source.read_bytes()
doc = fitz.open(source)
output = root / 'sources' / 'root_cote1_contact'
output.mkdir(exist_ok=True)
paths = []
for first in range(0, len(doc), 24):
    sheet = Image.new('RGB', (1200, 1920), 'white')
    draw = ImageDraw.Draw(sheet)
    for offset in range(min(24, len(doc) - first)):
        page = doc[first + offset]
        pix = page.get_pixmap(matrix=fitz.Matrix(0.42, 0.42), alpha=False)
        im = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
        im.thumbnail((290, 290))
        x, y = (offset % 4) * 300, (offset // 4) * 320
        sheet.paste(im, (x + (300-im.width)//2, y + 25))
        draw.text((x+10, y+5), f'PDF scan {first+offset+1}', fill='black')
    path = output / f'contact_{first+1:03d}_{min(first+24,len(doc)):03d}.png'
    sheet.save(path)
    paths.append(str(path.relative_to(root)))
record = {'url':url, 'sha256':hashlib.sha256(content).hexdigest(),
          'bytes':len(content), 'pdf_pages':len(doc), 'contact_sheets':paths,
          'elapsed_seconds':time.perf_counter()-started}
(root/'logs'/'root_inspect_cote1.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2), flush=True)
