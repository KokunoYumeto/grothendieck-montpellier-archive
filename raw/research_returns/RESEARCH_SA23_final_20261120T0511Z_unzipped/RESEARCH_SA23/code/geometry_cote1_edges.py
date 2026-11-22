"""Readable header/footer finding sheets for physical cote1 PDF pages1--72."""
from pathlib import Path
import time, json, hashlib
import fitz
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
source = root/'sources/root_manuscript1_ranged.pdf'
out = root/'notes/geometry_cote1_edges'
out.mkdir(exist_ok=True)
started = time.perf_counter()
doc = fitz.open(source)
files = []
panel_w, panel_h = 1400, 850
for first in range(1, 73, 8):
    sheet = Image.new('RGB', (panel_w*2, panel_h*4), 'white')
    draw = ImageDraw.Draw(sheet)
    for k, number in enumerate(range(first, min(first+8, 73))):
        page = doc[number-1]
        scale = panel_w/page.rect.width
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
        full = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
        w, h = full.size
        top = full.crop((0, int(h*.055), w, int(h*.255)))
        bottom = full.crop((0, int(h*.64), w, int(h*.85)))
        x, y = (k%2)*panel_w, (k//2)*panel_h
        draw.text((x+12,y+6), f'Physical PDF page {number}: upper and lower strips', fill='black')
        sheet.paste(top, (x,y+28))
        sheet.paste(bottom, (x,y+28+top.height+12))
        draw.line((x,y+28+top.height+5,x+panel_w,y+28+top.height+5),fill='red',width=2)
    target = out/f'edges_{first:03d}_{min(first+7,72):03d}.jpg'
    sheet.save(target, quality=92)
    files.append(str(target.relative_to(root)))
record = {'source':str(source.relative_to(root)),
          'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
          'physical_pages':list(range(1,73)),
          'strip_fractions':[[.055,.255],[.64,.85]],
          'files':files, 'elapsed_seconds':time.perf_counter()-started,
          'scope':'Finding aid only. Omits page middles; absence of a date here proves no absence on complete sheets.'}
(root/'logs/geometry_cote1_edges.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
