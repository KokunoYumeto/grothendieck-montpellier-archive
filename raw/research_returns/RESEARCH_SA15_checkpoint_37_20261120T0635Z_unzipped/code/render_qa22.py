"""Render all nine new subsections and a spread for actual visual review."""
from pathlib import Path
import json,re,hashlib
import fitz
w=Path(__file__).resolve().parents[1]
d=fitz.open(w/'RESEARCH_SA15_paper.pdf')
toc=d.get_toc()
rels=['agents/monodromy/nonordinary_ppav_polar_Lang_conditional.tex',
      'agents/monodromy/p_rank_zero_ppav_degree_one_groups.tex',
      'agents/monodromy/p_rank_one_ppav_degree_one_groups.tex',
      'agents/monodromy/nonordinary_ppav_odd_natural_blocks.tex',
      'agents/obstructions_crystals/A3_mixed_positive_index_monad.tex',
      'agents/reduction_descent/B_tame_full_wild_projective.tex',
      'agents/reduction_descent/B_tame_full_wild_quadratic.tex',
      'agents/reduction_descent/B_tame_reducible_newton.tex',
      'agents/reduction_descent/B_tame_reducible_recovery.tex']
titles=[]
for rel in rels:titles.extend(re.findall(r'\\subsection\{([^}]+)\}',(w/rel).read_text()))
pages={1,14,24,28,39,55,70,85,173,len(d)-1,len(d)}
matched=[]
for j,(level,title,start) in enumerate(toc):
    if title in titles:
        end=next((r[2] for r in toc[j+1:] if r[0]<=level),len(d)+1)
        pages.update(range(start,min(end+1,len(d)+1)))
        matched.append({'title':title,'start':start,'end_inclusive':min(end,len(d))})
assert len(matched)==9,{'titles':titles,'matched':matched}
folder=w/'outputs/qa22';assert not folder.exists();folder.mkdir()
for n in sorted(pages):d[n-1].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(folder/f'page_{n:03d}.png')
record={'pages_in_pdf':len(d),'pdf_sha256':hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest(),'pages_rendered':sorted(pages),'new_subsections':matched,'manual_visual_review':'PENDING'}
(w/'outputs/visual_qa22_pending.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
