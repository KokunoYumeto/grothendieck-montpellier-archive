"""Render every newly promoted subsection and a spread for actual image review."""
from pathlib import Path
import json,re
import fitz
w=Path(__file__).resolve().parents[1];d=fitz.open(w/'RESEARCH_SA15_paper.pdf');toc=d.get_toc()
rels=['agents/monodromy/nonordinary_ppav_uniform_Q_inertia.tex','sections/A_nonordinary_ppav_Coble_ranks.tex','agents/obstructions_crystals/A3_mixed_positive_index_cup_derivative.tex','agents/obstructions_crystals/A3_mixed_positive_index_trace_zero.tex','agents/reduction_descent/B_tame_cubic_wild_layer.tex','agents/reduction_descent/B_tame_cubic_wild_exhaustion.tex']
titles=[]
for rel in rels:titles.extend(re.findall(r'\\subsection\{([^}]+)\}',(w/rel).read_text()))
pages={1,14,24,28,39,55,70,85,len(d)-1,len(d)};matched=[]
for j,(level,title,start) in enumerate(toc):
    if title in titles:
        end=next((r[2] for r in toc[j+1:] if r[0]<=level),len(d)+1)
        pages.update(range(start,min(end+1,len(d)+1)))
        matched.append({'title':title,'start':start,'end_inclusive':min(end,len(d))})
assert len(matched)==6,{'titles':titles,'matched':matched}
folder=w/'outputs/qa21';assert not folder.exists();folder.mkdir()
for n in sorted(pages):d[n-1].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(folder/f'page_{n:03d}.png')
record={'pages_in_pdf':len(d),'pages_rendered':sorted(pages),'new_subsections':matched,'manual_visual_review':'PENDING'}
(w/'outputs/visual_qa21_pending.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
