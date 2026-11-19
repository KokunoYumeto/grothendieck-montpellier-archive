"""Render every PDF page and create labelled contact sheets for visual QA.

Operational helper only; this does not certify mathematical statements.
GPT-6 Astra (OpenAI), /root/maquettes, 2026-11-19.
"""
import argparse, json, subprocess
from pathlib import Path
from time import perf_counter
from PIL import Image, ImageDraw, ImageFont

p = argparse.ArgumentParser()
p.add_argument('pdf')
p.add_argument('output')
a = p.parse_args()
out = Path(a.output)
out.mkdir(parents=True, exist_ok=True)
start = perf_counter()
subprocess.run(['pdftoppm', '-png', '-r', '125', a.pdf, str(out/'page')], check=True)
pages = sorted(out.glob('page-*.png'))
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 24)
for first in range(0, len(pages), 9):
    group = pages[first:first+9]
    width, height = 530, 775
    sheet = Image.new('RGB', (3*width, 3*height), '#d8d8d8')
    draw = ImageDraw.Draw(sheet)
    for k, file in enumerate(group):
        im = Image.open(file).convert('RGB')
        im.thumbnail((width-20, height-48), Image.Resampling.LANCZOS)
        x, y = (k%3)*width, (k//3)*height
        sheet.paste(im, (x+(width-im.width)//2, y+38))
        draw.text((x+15, y+7), f'Page {first+k+1:02}', font=font, fill='black')
    sheet.save(out/f'contact_{first+1:02}_{first+len(group):02}.png')
print(json.dumps({'pdf':a.pdf,'pages_rendered':len(pages),'dpi':125,
                  'contact_sheets':(len(pages)+8)//9,
                  'runtime_seconds':perf_counter()-start},indent=2))
