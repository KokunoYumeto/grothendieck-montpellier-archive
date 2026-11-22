"""Render all four new CP20 subsections and a spread for actual image inspection."""
from pathlib import Path
import json,re
import fitz
w=Path(__file__).resolve().parents[1]
d=fitz.open(w/'RESEARCH_SA15_paper.pdf');toc=d.get_toc()
titles=[]
for rel in ['agents/monodromy/mixed_all_odd_norm_groups.tex',
            'agents/monodromy/mixed_all_even_groups.tex',
            'agents/monodromy/nonordinary_ppav_fixed_point_jets.tex',
            'agents/reduction_descent/B_tame_minimal_wild_layer.tex']:
    titles.extend(re.findall(r'\\subsection\{([^}]+)\}',(w/rel).read_text()))
pages={1,14,24,28,39,55,70,85,len(d)};matched=[]
for j,(level,title,start) in enumerate(toc):
    if title in titles:
        end=next((row[2] for row in toc[j+1:] if row[0]<=level),len(d)+1)
        pages.update(range(start,min(end+1,len(d)+1)))
        matched.append({'title':title,'start':start,'end_inclusive':min(end,len(d))})
assert len(matched)==4,{'expected':titles,'matched':matched}
folder=w/'outputs/qa20';assert not folder.exists();folder.mkdir()
for num in sorted(pages):
    d[num-1].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(folder/f'page_{num:03d}.png')
record={'pages_in_pdf':len(d),'pages_rendered':sorted(pages),
        'new_subsections':matched,'manual_visual_review':'PENDING'}
dest=w/'outputs/visual_qa20_pending.json';assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
