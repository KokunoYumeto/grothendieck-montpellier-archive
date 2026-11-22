#!/usr/bin/env python3
"""Reproduce the explicit resumed checkpoint07 render and contact sheet."""
from pathlib import Path
from PIL import Image, ImageDraw
import argparse, json, re, subprocess

p = argparse.ArgumentParser()
p.add_argument('render_directory')
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
out = Path(a.render_directory).resolve()
subprocess.run(['pdftoppm', '-f', '151', '-l', '154', '-png', '-scale-to',
                '900', str(out/'render_input.pdf'), str(out/'page')], check=True)
files = sorted(out.glob('page-*.png'))
selected = [1,7,12,14,15,19,24,28,30,34,40,46,52,58,63,66,70,76,82,88,
            94,101,106,112,119,124,127,131,134,138,143,147,151,154]
w, h, cols = 360, 530, 4
contact = Image.new('RGB', (cols*w, ((len(selected)+cols-1)//cols)*h), '#d7d7d7')
draw = ImageDraw.Draw(contact)
for i, n in enumerate(selected):
    im = Image.open(out/f'page-{n:03}.png').convert('RGB')
    im.thumbnail((w-12,h-30))
    x = (i%cols)*w+(w-im.width)//2
    y = (i//cols)*h+24
    contact.paste(im, (x,y))
    draw.text(((i%cols)*w+10,(i//cols)*h+6), f'Page {n}', fill='black')
contact.save(out/'contact.png')
log = (root/'RESEARCH_SA08_C3_D031_paper.log').read_text()
data = {'rendered_pages':len(files), 'sample_pages':selected,
        'overfull_boxes':len(re.findall('Overfull',log)),
        'undefined_reference_warnings':len(re.findall('undefined',log)),
        'latex_warnings':len(re.findall('LaTeX Warning',log)), 'seconds':None,
        'render_note':'Initial process ended after page150 without a final timing record; last four pages rendered by an explicit resume. No runtime is invented.',
        'visual_inspection':'Requires explicit image review.'}
(out/'render_log.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data))
