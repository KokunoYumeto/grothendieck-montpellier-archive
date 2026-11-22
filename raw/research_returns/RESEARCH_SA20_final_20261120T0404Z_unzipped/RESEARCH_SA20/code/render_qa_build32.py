#!/usr/bin/env python3
"""Render every new proof block, current gate and bibliography, plus a spread."""
from pathlib import Path
import hashlib, json, re, subprocess
from concurrent.futures import ThreadPoolExecutor
import fitz
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
pdf=ROOT/'RESEARCH_SA20_paper.pdf'
doc=fitz.open(pdf)
texts=[re.sub(r'\s+',' ',p.get_text()) for p in doc]
def locate(fragment, after=10):
    hits=[i+1 for i,t in enumerate(texts) if i+1>after and fragment in t]
    if not hits: raise ValueError('Missing proof boundary: '+fragment)
    return hits[0]

start_a=locate('A.142. Failure')
end_a=locate('Hausdorff continuity does not provide face parameterizations',start_a)
start_a5=locate('A5.018. Finite-format')
end_a5=locate('Gluing, resolution, and the information in groupoids',start_a5)
gates=locate('Unsettled statements and exact remaining gates',end_a5)
new_pages=set(range(start_a,end_a+1)) | set(range(start_a5,end_a5+1)) | set(range(gates,len(doc)+1))
spread={1,2,3,4,5,6,len(doc),*range(15,len(doc)+1,23)}
log=(ROOT/'RESEARCH_SA20_paper.log').read_text(errors='replace')
widths=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt',log)]
overflow_pages=set()
for match in re.finditer(r'Overfull \\[hv]box \(([0-9.]+)pt',log):
    following=re.search(r'\[(\d+)\]',log[match.end():])
    if following: overflow_pages.add(int(following.group(1)))
pages=sorted(new_pages | spread | overflow_pages)
qa=ROOT/'qa/build32';qa.mkdir(parents=True,exist_ok=True)
def render(n):
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-singlefile','-r','105','-png',str(pdf),str(qa/f'page_{n:03d}')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
with ThreadPoolExecutor(max_workers=6) as pool:
    list(pool.map(render,pages))
sheets=[]
for j in range(0,len(pages),12):
    group=pages[j:j+12]
    sheet=Image.new('RGB',(1600,1764),'#d9dde2');draw=ImageDraw.Draw(sheet)
    for k,n in enumerate(group):
        im=Image.open(qa/f'page_{n:03d}.png').convert('RGB');im.thumbnail((388,550))
        x=(k%4)*400+6;y=(k//4)*588+27
        sheet.paste(im,(x,y));draw.text((x,y-19),f'Page {n}',fill='black')
    path=qa/f'sheet_{j//12+1:02d}.png';sheet.save(path)
    sheets.append(str(path.relative_to(ROOT)))

def compiled_sources():
    seen=set();todo=[ROOT/'RESEARCH_SA20_paper.tex']
    while todo:
        p=todo.pop()
        if p in seen:continue
        seen.add(p)
        for rel in re.findall(re.escape(chr(92))+r'(?:input|include)\{([^}]+)\}',p.read_text()):
            q=ROOT/rel
            if not q.suffix:q=q.with_suffix('.tex')
            if q.exists():todo.append(q)
    seen.update([ROOT/'RESEARCH_SA20_references.bib',ROOT/'notes/root_references.bib'])
    seen.update((ROOT/'agents').glob('*/references.bib'))
    return sorted(seen)

record={
 'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
 'pdf_bytes':pdf.stat().st_size,'pages':len(doc),'rendered_pages':pages,
 'render_method':'Poppler pdftoppm at105dpi; six independent page workers; PIL contact sheets',
 'visual_review':'pending',
 'before':json.loads((ROOT/'logs/pdf_qa_build32_before.json').read_text()),
 'after':{'build':'build_root_32g final pass','overfull_boxes':len(widths),'over_2pt':sum(x>2 for x in widths),'max_overflow_pt':max(widths,default=0),'missing_glyphs':log.count('Missing character'),'undefined_refs':log.count('undefined'),'bib_warnings':(ROOT/'RESEARCH_SA20_paper.blg').read_text().count('Warning')},
 'new_proof_page_ranges':[[start_a,end_a],[start_a5,end_a5]],
 'current_gates_and_bibliography_range':[gates,len(doc)],
 'corrected_layout_pages':[n for n,t in enumerate(texts,1) if n>10 and ('A.147. Parameter regularity' in t or 'A5.19.2' in t or 'Theorem 2.2(1), printed p. 6' in t)],
 'remaining_overflow_pages':sorted(overflow_pages),
 'contact_sheets':sheets,
 'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in compiled_sources()},
}
(ROOT/'logs/pdf_qa.json').write_text(json.dumps(record,indent=2)+'\n')
(ROOT/'logs/render_qa_build32_pending.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='source_sha256'},indent=2))
