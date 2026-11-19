from pathlib import Path
import re,csv,json,datetime
w=Path(__file__).resolve().parents[1]; s=w/'sections'; a=w/'agents'
rootbib=w/'notes/root_references.bib'
if not rootbib.exists():rootbib.write_text((w/'RESEARCH_SA15_references.bib').read_text())
(s/'A_monodromy.tex').write_text(''.join((a/f'monodromy/{x}.tex').read_text()+'\n' for x in ['results','relative_ordinarity_counterexample','quintic_exact','sextic_exact','septic_exact','all_degree_char2_contact'] if (a/f'monodromy/{x}.tex').exists())+'\n\\input{sections/A_char2_uniform}\n'+(a/'monodromy/odd_characteristic_plane.tex').read_text()+'\n'+(a/'monodromy/projective_space_odd.tex').read_text()+'\n'+(a/'monodromy/projective_space_char2.tex').read_text())
(s/'B.tex').write_text('\\section{B. Good reduction and inertia characters}\n'+''.join((a/f'reduction_descent/{x}.tex').read_text()+'\n' for x in ['B_reduction','B_ranges','B_wild12','B_p3_ranges','B_higher_tame','B_general_bounds','B_character'] if (a/f'reduction_descent/{x}.tex').exists()))
(s/'C.tex').write_text('\\section{C. Extension and descent}\n'+''.join((a/f'reduction_descent/{x}.tex').read_text()+'\n' for x in ['C_effectivity','C_normal','C_nonfinite_counterexample','C_descent','C_local_systems','C_nilpotent_local_systems','C_counterexample'] if (a/f'reduction_descent/{x}.tex').exists()))
(s/'D.tex').write_text((a/'obstructions_crystals/D_E_partial.tex').read_text())
bibs=[rootbib,a/'monodromy/references.bib',a/'reduction_descent/reduction_descent.bib',a/'obstructions_crystals/D_E_references.bib']
seen=set();out=[]
for b in bibs:
 for e in re.split(r'(?=^@)',b.read_text(),flags=re.M):
  if not e.strip():continue
  m=re.match(r'@\w+\{([^,]+)',e)
  if m and m[1] not in seen:seen.add(m[1]);out.append(e)
(w/'RESEARCH_SA15_references.bib').write_text('\n'.join(out))

for q in s.glob('*.tex'):
 t=q.read_text(); t=t.replace('\\paragraph{','\\par\\smallskip\\noindent\\textbf{'); q.write_text(t)
print('Integrated four sections and',len(seen),'bibliography records')
