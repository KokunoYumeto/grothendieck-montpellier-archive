#!/usr/bin/env python3
"""Render every manuscript page and make a labelled inspection contact sheet."""
from pathlib import Path
import argparse, json, re, shutil, subprocess, time
from PIL import Image, ImageDraw
p=argparse.ArgumentParser()
p.add_argument('output');p.add_argument('--pages',default='1,10,17,19,21,23,25,30,35,40,46,48,50,52,60,62,64')
a=p.parse_args();root=Path(__file__).resolve().parents[1]
out=Path(a.output).resolve();out.mkdir(parents=True,exist_ok=True)
t=time.monotonic()
# Render a fixed copy so a later independent build cannot change this input
# halfway through pdftoppm. Invoke only after the selected build has finished.
snapshot=out/'render_input.pdf'
shutil.copyfile(root/'RESEARCH_SA08_C3_D031_paper.pdf',snapshot)
build_log=(root/'RESEARCH_SA08_C3_D031_paper.log').read_text()
subprocess.run(['pdftoppm','-png','-scale-to','900',str(snapshot),str(out/'page')],check=True)
files=sorted(out.glob('page-*.png'))
selected=[int(n) for n in a.pages.split(',') if 1<=int(n)<=len(files)]
width,height=360,530;cols=4
contact=Image.new('RGB',(cols*width,((len(selected)+cols-1)//cols)*height),'#d7d7d7')
draw=ImageDraw.Draw(contact)
for i,n in enumerate(selected):
 im=Image.open(files[n-1]).convert('RGB');im.thumbnail((width-12,height-30))
 x=(i%cols)*width+(width-im.width)//2;y=(i//cols)*height+24
 contact.paste(im,(x,y));draw.text(((i%cols)*width+10,(i//cols)*height+6),f'Page {n}',fill='black')
contact.save(out/'contact.png')
log=build_log
data={'rendered_pages':len(files),'sample_pages':selected,'overfull_boxes':len(re.findall(r'Overfull',log)),
      'undefined_reference_warnings':len(re.findall(r'undefined',log)),
      'latex_warnings':len(re.findall(r'LaTeX Warning',log)),
      'seconds':time.monotonic()-t,
      'visual_inspection':'Pending explicit image review; this script does not assess appearance.'}
(out/'render_log.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data))
