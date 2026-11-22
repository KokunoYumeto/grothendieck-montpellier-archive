"""Render every new CP18 subsection and a spread of older pages for actual QA."""
from pathlib import Path
import json
import fitz
w=Path(__file__).resolve().parents[1]
d=fitz.open(w/'RESEARCH_SA15_paper.pdf')
titles=['A wreath and grid argument in degree two on every mixed product',
        'The logarithm equality boundary and square finite determinants',
        'The exact finite-character list after primitive-norm normalization',
        'A rank-two bundle model for the remaining trace variation',
        'Two zero trace directions and the remaining matrix alternative']
pages={1,14,24,28,39,55,70,85,243,245,len(d)}
toc=d.get_toc();matched=[]
for j,(level,title,start) in enumerate(toc):
    if any(q.lower() in title.lower() for q in titles):
        end=next((row[2] for row in toc[j+1:] if row[0]<=level),len(d)+1)
        pages.update(range(start,min(end+1,len(d)+1)))
        matched.append({'title':title,'start':start,'end_inclusive':min(end,len(d))})
assert len(matched)>=4,matched
folder=w/'outputs/qa18';folder.mkdir(exist_ok=True)
for num in sorted(pages):
    d[num-1].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(folder/f'page_{num:03d}.png')
record={'pages_in_pdf':len(d),'pages_rendered':sorted(pages),'new_subsections':matched,
        'prior_overflow_pages':[243,245], 'manual_visual_review':'PENDING'}
(w/'outputs/visual_qa18_pending.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
