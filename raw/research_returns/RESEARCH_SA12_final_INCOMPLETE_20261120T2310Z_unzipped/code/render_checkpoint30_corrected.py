"""Inspect the corrected CP30 proof blocks without overwriting earlier images."""
from pathlib import Path
import hashlib
import json
import re
import time
import fitz
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
start = time.perf_counter()
doc = fitz.open(root / 'build/RESEARCH_SA12_paper.pdf')
aux = (root / 'build/RESEARCH_SA12_paper.aux').read_text()
label_pages = {key: int(page) for key, page in re.findall(r'\\newlabel\{([^}]+)\}\{\{[^}]*\}\{(\d+)\}', aux)}
pages = {1, 2, 3, 4, 5, 75, 175, 275, 375, 475, len(doc)}
added = set()
for p in sorted((root / 'code/output').glob('integrate_post19_post29*.json')):
    added.update(json.loads(p.read_text())['labels'])
assert added and all(key in label_pages for key in added)
first, last = min(label_pages[key] for key in added), max(label_pages[key] for key in added)
end = min(i + 1 for i, page in enumerate(doc) if i + 1 > last and any(
    s in page.get_text() for s in ['Remaining proof gates', 'Remaining unchecked', 'Unresolved statements']))
pages.update(range(first - 1, end + 5))
cf = label_pages['D:A-chain-finite-jet-framing']
af = label_pages['D:RDP-Artinian-full-bundle-framing']
pages.update(range(cf - 1, af + 4))
for i, page in enumerate(doc):
    if i + 1 <= end:
        continue
    if any(s in page.get_text() for s in ['Quadratic forms over fraction fields',
                                         'On the equations defining abelian varieties',
                                         'Central Simple Algebras and Galois Cohomology']):
        pages.add(i + 1)
pages = sorted(p for p in pages if 1 <= p <= len(doc))
prefix = 'checkpoint30_corrected'
checks, images, cards = [], [], []
for number in pages:
    pix = doc[number - 1].get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)
    im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    rel = f'qa/{prefix}_page_{number:02d}.webp'
    out = root / rel
    assert not out.exists()
    im.save(out, 'WEBP', lossless=True, quality=100, method=4)
    assert Image.open(out).convert('RGB').tobytes() == im.tobytes()
    checks.append(rel)
    images.append({'path': rel, 'sha256': hashlib.sha256(out.read_bytes()).hexdigest(), 'bytes': out.stat().st_size})
    thumb = im.copy()
    thumb.thumbnail((398, 565))
    card = Image.new('RGB', (418, 601), '#dddddd')
    card.paste(thumb, ((418 - thumb.width) // 2, 26))
    ImageDraw.Draw(card).text((10, 7), f'Page {number}', fill='black')
    cards.append(card)
for group in range((len(cards) + 8) // 9):
    items = cards[group * 9:group * 9 + 9]
    sheet = Image.new('RGB', (1254, 601 * ((len(items) + 2) // 3)), 'white')
    for i, card in enumerate(items):
        sheet.paste(card, ((i % 3) * 418, (i // 3) * 601))
    rel = f'qa/{prefix}_contact_{group + 1}.webp'
    out = root / rel
    assert not out.exists()
    sheet.save(out, 'WEBP', lossless=True, quality=100, method=4)
    assert Image.open(out).convert('RGB').tobytes() == sheet.tobytes()
    checks.append(rel)
    images.append({'path': rel, 'sha256': hashlib.sha256(out.read_bytes()).hexdigest(), 'bytes': out.stat().st_size})
record = dict(pdf_pages=len(doc), rendered_pages=pages, seconds=time.perf_counter() - start,
              artifact_prefix=prefix, image_format='webp', lossless_pixel_roundtrip_checks=checks,
              images=images, total_image_bytes=sum(i['bytes'] for i in images),
              prior_inspection_record='qa/checkpoint30_pre_coordinate_correction_actual_inspection.json',
              note='Every original CP30 image remains untouched. These are fresh corrected-PDF page and contact images with exact RGB equality checks; actual human-visible output inspection is recorded separately.')
(root / 'qa/checkpoint30_render.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({k: v for k, v in record.items() if k not in ['images', 'lossless_pixel_roundtrip_checks']}, indent=2))
