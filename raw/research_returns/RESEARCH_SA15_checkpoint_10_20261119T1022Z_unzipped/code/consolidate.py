from pathlib import Path
import re,csv,json,datetime
w=Path(__file__).resolve().parents[1]; s=w/'sections'; a=w/'agents'
rootbib=w/'notes/root_references.bib'
(s/'A_surface_counterexample.tex').write_text((a/'obstructions_crystals/A_surface_counterexample.tex').read_text())
(s/'A_integral_counterexample.tex').write_text((a/'obstructions_crystals/A_integral_counterexample.tex').read_text())
(s/'A_injectivity_counterexample.tex').write_text((a/'obstructions_crystals/A_injectivity_counterexample.tex').read_text())
(s/'A_injectivity_degrees.tex').write_text((a/'obstructions_crystals/A_injectivity_degrees.tex').read_text())
(s/'A_product_degrees.tex').write_text((a/'obstructions_crystals/A_product_degrees.tex').read_text())
if not rootbib.exists():rootbib.write_text((w/'RESEARCH_SA15_references.bib').read_text())
(s/'A_monodromy.tex').write_text(''.join((a/f'monodromy/{x}.tex').read_text()+'\n' for x in ['results','relative_ordinarity_counterexample','quintic_exact','sextic_exact','septic_exact','all_degree_char2_contact'] if (a/f'monodromy/{x}.tex').exists())+'\n\\input{sections/A_char2_uniform}\n'+(a/'monodromy/odd_characteristic_plane.tex').read_text()+'\n'+(a/'monodromy/projective_space_odd.tex').read_text()+'\n'+(a/'monodromy/projective_space_char2.tex').read_text())
(s/'B.tex').write_text('\\section{B. Good reduction and inertia characters}\n'+''.join((a/f'reduction_descent/{x}.tex').read_text()+'\n' for x in ['B_reduction','B_ranges','B_wild12','B_p3_ranges','B_higher_tame','B_general_bounds','B_character'] if (a/f'reduction_descent/{x}.tex').exists()))
(s/'C.tex').write_text('\\section{C. Extension and descent}\n'+''.join((a/f'reduction_descent/{x}.tex').read_text()+'\n' for x in ['C_effectivity','C_normal','C_nonfinite_counterexample','C_descent','C_local_systems','C_nilpotent_local_systems','C_counterexample'] if (a/f'reduction_descent/{x}.tex').exists()))
(s/'D.tex').write_text((a/'obstructions_crystals/D_E_partial.tex').read_text())
for e2name in ['E2_cusps_flat_addition.tex','E2_relative_frobenius_addition.tex','E2_counterexample_addition.tex']:
 e2=a/'obstructions_crystals'/e2name
 if e2.exists():
  target=s/'D.tex';text=target.read_text()
  text=text.replace('\\subsection{E.3. Integral infinitesimal cohomology without divided powers}',e2.read_text()+'\n\\subsection{E.3. Integral infinitesimal cohomology without divided powers}')
  target.write_text(text)
fparts=[s/'F_A_quotes.tex',a/'reduction_descent/F_BC_manuscript_quotes.tex',a/'obstructions_crystals/F_DE_manuscript_quotes.tex',a/'obstructions_crystals/R7_R10_audit.tex']
ftext='\\section{F. Companion statement map and literature record}\n'+''.join(p.read_text()+'\n' for p in fparts if p.exists())
ftext=ftext.replace('The missing reference is identified with','An exact printed parallel, and a plausible identification of the missing reference, is')
ftext+='''
\\subsection{F.2. Source access and literature searches}
Every bibliographic entry below records its actual access state and the
precise checked passages. An opened metadata page is not described as
an opened theorem. The accompanying \\path{notes/SOURCE_CENSUS.tsv}
and \\path{notes/SOURCE_CENSUS.md} give one row per named or used source,
including unsuccessful attempts. The report incorporates that census.
The three agent search logs and the dated root search logs
\\path{notes/ROOT_SEARCH_LOG_04.md}, \\path{notes/ROOT_SEARCH_LOG_05.md},
\\path{notes/ROOT_SEARCH_LOG_06.md}, \\path{notes/ROOT_SEARCH_LOG_07.md},
\\path{notes/ROOT_SEARCH_LOG_08.md}, \\path{notes/ROOT_SEARCH_LOG_09.md}, and
\\path{notes/ROOT_SEARCH_LOG_10.md}
record the searches for the requested topics. We make no priority claim.
The source list includes unopened originals to make the limits visible;
their presence is not an assertion that their theorems have been checked.
'''
(s/'F.tex').write_text(ftext)
for target, files in {
 'A_monodromy.tex': ['monodromy/general_X_residues.tex','monodromy/effective_rank_determinant.tex','monodromy/adjunction_covector.tex','monodromy/ordinary_abelian_covectors.tex','monodromy/product_surface_obstruction.tex','monodromy/product_exact_covectors.tex','monodromy/effective_monodromy.tex','monodromy/perfect_field_monodromy.tex','monodromy/product_full_groups.tex','monodromy/product_uniform_structure.tex','monodromy/product_irreducible_hasse_reduction.tex','monodromy/product_hasse_irreducibility.tex','monodromy/ordinary_products_general_structure.tex','monodromy/ordinary_products_isogeny_full_groups.tex','obstructions_crystals/A3_supersingular_product_ranks.tex','monodromy/supersingular_product_degree_one.tex','monodromy/supersingular_exact_covectors.tex','monodromy/supersingular_uniform_GL8_block.tex','obstructions_crystals/A3_mixed_generic_ranks.tex','monodromy/ppav_theta_cartier_symmetrizer.tex','monodromy/ordinary_ppav_surface_full_groups.tex'],
 'B.tex': ['reduction_descent/B_character_upper.tex','reduction_descent/B_BT_lower.tex','reduction_descent/B_higher_wild_gates.tex','reduction_descent/B_p2_character_gate.tex','reduction_descent/B_full9.tex','reduction_descent/B_finite_decision.tex','reduction_descent/B_level27_obstruction.tex','reduction_descent/B_wild_sufficiency.tex','reduction_descent/B_character_wild_lower.tex','reduction_descent/B_p3_character_level2.tex','reduction_descent/B_character_sharper_upper.tex','reduction_descent/B_height_two_small_gate.tex','reduction_descent/B_height_two_tame_gate.tex'],
 'C.tex': ['reduction_descent/C_formal_nilpotent.tex','reduction_descent/C_absolute_image.tex'],
}.items():
 with (s/target).open('a') as out:
  for name in files:
   path=a/name
   if name=='monodromy/ppav_theta_cartier_symmetrizer.tex': out.write('\n\\input{sections/A_ppav_two_jets}\n')
   if path.exists(): out.write('\n'+path.read_text()+'\n')
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
