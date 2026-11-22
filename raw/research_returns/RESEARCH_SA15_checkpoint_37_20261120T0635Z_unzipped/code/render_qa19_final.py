"""Render all six new CP19 subsections and a spread for actual visual QA."""
from pathlib import Path
import json
import fitz
w=Path(__file__).resolve().parents[1]
d=fitz.open(w/'RESEARCH_SA15_paper.pdf')
titles=['A cyclic norm','A norm pencil','Uniform mixed strips',
        'Residual irreducibility and a cycle',
        'The potentially CM','A curve pencil','Mixed strips of width three',
        'The CM formal subclass']
toc=d.get_toc()
print(json.dumps([r for r in toc if any(s in r[1].lower() for s in ['pencil','strip','cm','residual irreducibility'])],indent=2))
exact_file_titles=[]
import re
for rel in ['agents/monodromy/mixed_three_by_b_strip_groups.tex',
            'agents/reduction_descent/B_tame_CM_gate.tex',
            'agents/reduction_descent/B_tame_residual_cycle.tex',
            'agents/obstructions_crystals/A3_mixed_positive_index_pencil.tex',
            'agents/monodromy/mixed_degree_three_norm_groups.tex',
            'agents/reduction_descent/B_tame_CM_neighborhood.tex']:
    exact_file_titles.extend(re.findall(r'\\subsection\{([^}]+)\}',(w/rel).read_text()))
pages={1,14,24,28,39,55,70,85,len(d)};matched=[]
for j,(level,title,start) in enumerate(toc):
    if title in exact_file_titles:
        end=next((row[2] for row in toc[j+1:] if row[0]<=level),len(d)+1)
        pages.update(range(start,min(end+1,len(d)+1)))
        matched.append({'title':title,'start':start,'end_inclusive':min(end,len(d))})
assert len(matched)==6,{'expected':exact_file_titles,'matched':matched}
folder=w/'outputs/qa19_final';folder.mkdir(exist_ok=True)
for num in sorted(pages):
    d[num-1].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(folder/f'page_{num:03d}.png')
record={'pages_in_pdf':len(d),'pages_rendered':sorted(pages),
        'new_subsections':matched,'manual_visual_review':'PENDING'}
(w/'outputs/visual_qa19_final_pending.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
