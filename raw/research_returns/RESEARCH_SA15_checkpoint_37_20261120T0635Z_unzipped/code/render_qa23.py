"""Render every CP23 new subsection and every repaired-overflow location."""
from pathlib import Path
import json,re,hashlib,datetime
import fitz
w=Path(__file__).resolve().parents[1]
d=fitz.open(w/'RESEARCH_SA15_paper.pdf');toc=d.get_toc()
choices=[
 ['agents/obstructions_crystals/A3_mixed_positive_index_Petri.tex'],
 ['agents/obstructions_crystals/A3_mixed_common_polarization_power.tex'],
 ['agents/monodromy/nonordinary_three_theta_graph_reduction.tex'],
 ['agents/monodromy/nonordinary_genus_two_triple_ramification.tex'],
 ['agents/monodromy/nonordinary_ppav_degree_three_node_gluing.tex'],
 ['sections/A_nonordinary_trigonal_direct.tex'],
 ['sections/A_nonordinary_three_neighbor_boundary.tex'],
 ['agents/reduction_descent/B_tame_cyclic_level_counterexamples.tex'],
 ['agents/reduction_descent/A_nonordinary_powers_three.tex','agents/reduction_descent/A_nonordinary_powers_three_candidate.tex'],
 ['agents/monodromy/nonordinary_ppav_degree_two_wreath_theta.tex','agents/monodromy/nonordinary_ppav_degree_two_wreath_theta_candidate.tex']]
rels=[next(x for x in group if (w/x).exists()) for group in choices]
titles=[]
for rel in rels: titles.extend(re.findall(r'\\subsection\{([^}]+)\}',(w/rel).read_text()))
assert len(titles)==10,titles
pages={1,14,24,28,39,55,70,85,126,169,173,len(d)-1,len(d)};matched=[]
for j,(level,title,start) in enumerate(toc):
 if title in titles:
  end=next((r[2] for r in toc[j+1:] if r[0]<=level),len(d)+1)
  pages.update(range(start,min(end+1,len(d)+1)))
  matched.append({'title':title,'start':start,'end_inclusive':min(end,len(d))})
assert len(matched)==10,{'titles':titles,'matched':matched}
# Locate both B62 repaired contexts by final content, not stale build page numbers.
overflow_locations=[]
needles=['Lifting a finite rank-one extension','B-RD62.6']
for needle in needles:
 found=[i+1 for i,page in enumerate(d) if needle in page.get_text()]
 assert found,needle
 pages.update(found);overflow_locations.append({'final_text_needle':needle,'pages':found})
folder=w/'outputs/qa23';assert not folder.exists();folder.mkdir()
for n in sorted(pages):d[n-1].get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(folder/f'page_{n:03d}.png')
record={'rendered_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pages_in_pdf':len(d),'pdf_sha256':hashlib.sha256((w/'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest(),'pages_rendered':sorted(pages),'new_subsections':matched,'repaired_overflow_locations':overflow_locations,'manual_visual_review':'PENDING'}
(w/'outputs/visual_qa23_pending.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
