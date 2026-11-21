"""Render the final paper and contact sheets for human layout inspection."""
from pathlib import Path
import json
import fitz
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parent.parent
out = root / 'work' / 'pdf_qa_build23'
out.mkdir(exist_ok=True)
source = root / 'deliverables' if (root / 'deliverables').is_dir() else root
doc = fitz.open(source / 'TRACE_DET.pdf')
thumbs = []
for i, page in enumerate(doc):
    dest = out / f'page_{i+1:02d}.png'
    page.get_pixmap(matrix=fitz.Matrix(1.25, 1.25), alpha=False).save(dest)
    im = Image.open(dest).convert('RGB')
    im.thumbnail((360, 510))
    thumbs.append(im)

for start in range(0, len(thumbs), 12):
    count = min(12, len(thumbs)-start)
    rows = (count + 2)//3
    sheet = Image.new('RGB', (1140, rows*550+20), '#d8dde3')
    draw = ImageDraw.Draw(sheet)
    for j in range(count):
        x = 10 + (j%3)*380
        y = 10 + (j//3)*550
        draw.text((x+4, y+3), f'Page {start+j+1}', fill='black')
        sheet.paste(thumbs[start+j], (x+5, y+24))
    sheet.save(out / f'contact_{start+1:02d}.png')
print(json.dumps({'pages':len(doc),'directory':str(out),
                  'contacts':[p.name for p in sorted(out.glob('contact_*.png'))]}))
