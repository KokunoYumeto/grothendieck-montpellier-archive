#!/usr/bin/env python3
"""Render a spread sample and every corrected-layout page for human visual QA."""
from pathlib import Path
import hashlib,json,re,subprocess
import fitz
from PIL import Image,ImageOps,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
pdf=ROOT/'RESEARCH_SA20_paper.pdf';doc=fitz.open(pdf)
def compiled_sources():
    """Hash the actual TeX input graph, excluding independent draft notes."""
    seen=set();todo=[ROOT/'RESEARCH_SA20_paper.tex']
    while todo:
        p=todo.pop()
        if p in seen:continue
        seen.add(p)
        for rel in re.findall(re.escape(chr(92))+r'(?:input|include)\{([^}]+)\}',p.read_text()):
            q=ROOT/rel
            if not q.suffix:q=q.with_suffix('.tex')
            if q.exists():todo.append(q)
    seen.add(ROOT/'RESEARCH_SA20_references.bib')
    seen.add(ROOT/'notes/root_references.bib')
    seen.update((ROOT/'agents').glob('*/references.bib'))
    return sorted(seen)
qa=ROOT/'qa';qa.mkdir(exist_ok=True)
pages=sorted({1,2,3,5,12,16,27,34,45,50,60,85,100,125,150,175,200,225,250,275,301,320,321,len(doc),*range(72,85),*range(133,143),*range(322,346),*[i+1 for i,p in enumerate(doc) if 'C.023.' in p.get_text()]})
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
record={'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pages':len(doc),'rendered_pages':pages,'render_method':'Poppler pdftoppm at105dpi; contact sheets generated with PIL','visual_review':'pending','before':{'build':'build_root_31c final pass, before certificate-display correction','overfull_boxes':2,'over_2pt':1,'max_overflow_pt':69.05551,'missing_glyphs':0,'undefined_refs':0,'bib_warnings':0,'layout_changes':'Build31 adds complete A139--A141 and A5.016--A5.017 proofs, exact gates and opened-source bibliography. The first build stopped at a paragraph heading inside the A139 proof; the six headings were changed to bold inline headings. Build31b then had a39.46568pt overflow from an A5.016 checker filename; path formatting corrected it. Build31c added A5.017 and exposed a69.05551pt certificate-display overflow. Build31d splits that formula into short aligned lines. The only remaining overflow is1.1506pt on page301, below the required2pt threshold.'},'after':{'build':'build_root_31d final pass','overfull_boxes':len(widths),'over_2pt':sum(x>2 for x in widths),'max_overflow_pt':max(widths,default=0),'missing_glyphs':log.count('Missing character'),'undefined_refs':log.count('undefined'),'bib_warnings':(ROOT/'RESEARCH_SA20_paper.blg').read_text().count('Warning')},'corrected_layout_pages':[138,139,301],'newly_typeset_pages':[*range(73,84),*range(133,142),*range(322,346)],'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in compiled_sources()}}
(ROOT/'logs/pdf_qa.json').write_text(json.dumps(record,indent=2))
print(json.dumps({k:v for k,v in record.items() if k!='source_sha256'},indent=2))
