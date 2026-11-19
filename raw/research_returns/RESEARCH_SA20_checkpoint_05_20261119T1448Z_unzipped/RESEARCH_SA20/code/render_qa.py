#!/usr/bin/env python3
"""Render a spread sample and every corrected-layout page for human visual QA."""
from pathlib import Path
import hashlib,json,re,subprocess
import fitz
from PIL import Image,ImageOps,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
pdf=ROOT/'RESEARCH_SA20_paper.pdf';doc=fitz.open(pdf)
qa=ROOT/'qa';qa.mkdir(exist_ok=True)
pages=sorted({1,2,4,5,40,65,80,120,135,150,175,len(doc)-2,len(doc)-1,len(doc),*range(16,22),*range(29,34),*range(53,60),*range(103,116),*range(159,170),*range(180,184)})
for n in pages:
 subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-singlefile','-r','105','-png',str(pdf),str(qa/f'page_{n:03d}')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
for j in range(0,len(pages),12):
 group=pages[j:j+12];sheet=Image.new('RGB',(1600,1764),'#d9dde2');draw=ImageDraw.Draw(sheet)
 for k,n in enumerate(group):
  im=Image.open(qa/f'page_{n:03d}.png').convert('RGB');im.thumbnail((388,550))
  x=(k%4)*400+6;y=(k//4)*588+27
  sheet.paste(im,(x,y));draw.text((x,y-19),f'Page {n}',fill='black')
 sheet.save(qa/f'sheet_{j//12+1:02d}.png')
log=(ROOT/'RESEARCH_SA20_paper.log').read_text(errors='replace')
widths=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
record={'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':len(doc),'rendered_pages':pages,'render_method':'Poppler pdftoppm at105dpi; contact sheets generated with PIL','visual_review':'pending','before':{'build':'build_root_16 failed pass','overfull_boxes':2,'max_overflow_pt':13.696},'after':{'build':'build_root_18 final pass','overfull_boxes':len(widths),'over_2pt':sum(x>2 for x in widths),'max_overflow_pt':max(widths,default=0),'missing_glyphs':log.count('Missing character'),'undefined_refs':log.count('undefined'),'bib_warnings':(ROOT/'RESEARCH_SA20_paper.blg').read_text().count('Warning')},'corrected_layout_pages':[55,107,162],'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'RESEARCH_SA20_paper.tex',*(ROOT/'parts').glob('*.tex'),*(ROOT/'agents').glob('*/*.tex')]}}
(ROOT/'logs/pdf_qa.json').write_text(json.dumps(record,indent=2))
print(json.dumps({k:v for k,v in record.items() if k!='source_sha256'},indent=2))
