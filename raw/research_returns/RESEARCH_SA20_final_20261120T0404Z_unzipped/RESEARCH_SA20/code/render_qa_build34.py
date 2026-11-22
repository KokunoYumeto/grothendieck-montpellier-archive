#!/usr/bin/env python3
"""Render all changed pages, new theorem, overflow pages and a spread."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import re
import subprocess
import fitz
from PIL import Image, ImageDraw

root=Path(__file__).resolve().parents[1]
pdf=root/'RESEARCH_SA20_paper.pdf'
doc=fitz.open(pdf)
old_path=Path('/tmp/RESEARCH_SA20_build33c_before34.pdf')
old=fitz.open(old_path)
def normalized(page):
    text=re.sub(r'\n\s*\d+\s*$', '', page.get_text())
    return re.sub(r'\s+',' ',text).strip()
old_texts={normalized(p) for p in old}
changed=[i+1 for i,p in enumerate(doc) if normalized(p) not in old_texts]
texts=[re.sub(r'\s+',' ',p.get_text()) for p in doc]
def locate(fragment,after=10):
    hits=[i+1 for i,t in enumerate(texts) if i+1>after and fragment in t]
    assert hits,fragment
    return hits[0]
start=locate('A.163. Relative comparison')
end=locate('Hausdorff continuity does not provide face parameterizations',start)
gates=locate('Unsettled statements and exact remaining gates',end)
log=(root/'RESEARCH_SA20_paper.log').read_text(errors='replace')
widths=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
overflow=set()
for match in re.finditer(r'Overfull \\[hv]box \(([0-9.]+)pt',log):
    following=re.search(r'\[(\d+)\]',log[match.end():])
    if following:overflow.add(int(following.group(1)))
after={'build':'build_root_34b final pass','overfull_boxes':len(widths),
       'over_2pt':sum(w>2 for w in widths),'max_overflow_pt':max(widths,default=0),
       'missing_glyphs':log.count('Missing character'),
       'undefined_refs':log.count('undefined'),
       'bib_warnings':(root/'RESEARCH_SA20_paper.blg').read_text().count('Warning')}
for key in ['over_2pt','missing_glyphs','undefined_refs','bib_warnings']:
    assert after[key]==0,(key,after[key])
pages=sorted(set(changed)|set(range(start,end+1))|overflow|
             {1,2,3,4,5,6,len(doc),*range(15,len(doc)+1,23)}|
             set(range(gates,len(doc)+1)))
qa=root/'qa/build34';qa.mkdir(parents=True,exist_ok=True)
def render(n):
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-singlefile','-r','105','-png',str(pdf),str(qa/f'page_{n:03d}')],
                   check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
with ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(render,pages))
sheets=[]
for j in range(0,len(pages),12):
    group=pages[j:j+12]
    sheet=Image.new('RGB',(1600,1764),'#d9dde2');draw=ImageDraw.Draw(sheet)
    for k,n in enumerate(group):
        im=Image.open(qa/f'page_{n:03d}.png').convert('RGB');im.thumbnail((388,550))
        x=(k%4)*400+6;y=(k//4)*588+27
        sheet.paste(im,(x,y));draw.text((x,y-19),f'Page {n}',fill='black')
    path=qa/f'sheet_{j//12+1:02d}.png';sheet.save(path);sheets.append(str(path.relative_to(root)))
seen=set();todo=[root/'RESEARCH_SA20_paper.tex']
while todo:
    p=todo.pop()
    if p in seen:continue
    seen.add(p)
    for rel in re.findall(re.escape(chr(92))+r'(?:input|include)\{([^}]+)\}',p.read_text()):
        q=root/rel
        if not q.suffix:q=q.with_suffix('.tex')
        if q.exists():todo.append(q)
seen.update([root/'RESEARCH_SA20_references.bib',root/'notes/root_references.bib'])
seen.update((root/'agents').glob('*/references.bib'))
method='Compare complete extracted page text with every old page after removing only the final page number; retain section-number and text-reflow changes.'
change_record={'before_pdf':str(old_path),'method':method,'changed_pages':changed}
(root/'logs/build34_changed_pages.json').write_text(json.dumps(change_record,indent=2)+'\n')
before=json.loads((root/'logs/pdf_qa_before_build34.json').read_text())
record={'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pdf_bytes':pdf.stat().st_size,
        'pages':len(doc),'rendered_pages':pages,
        'render_method':'Poppler pdftoppm at105dpi; six independent page workers; PIL contact sheets',
        'visual_review':'pending','before':before['after'],'after':after,
        'all_changed_body_pages':changed,'changed_page_detection':method,
        'new_proof_page_ranges':[[start,end]],'current_gates_and_bibliography_range':[gates,len(doc)],
        'remaining_overflow_pages':sorted(overflow),'contact_sheets':sheets,
        'source_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(seen)}}
(root/'logs/pdf_qa.json').write_text(json.dumps(record,indent=2)+'\n')
(root/'logs/render_qa_build34_pending.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='source_sha256'},indent=2))
