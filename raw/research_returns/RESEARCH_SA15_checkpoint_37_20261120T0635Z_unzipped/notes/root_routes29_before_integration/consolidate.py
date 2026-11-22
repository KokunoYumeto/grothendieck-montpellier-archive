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
for e2name in ['E2_cusps_flat_addition.tex','E2_relative_frobenius_addition.tex','E2_counterexample_addition.tex','E2_coherent_faithfulness.tex','E2_flat_relative_addition.tex','E2_coherent_Noetherian_equivalence.tex']:
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
\\path{notes/ROOT_SEARCH_LOG_10.md}, \\path{notes/ROOT_SEARCH_LOG_11.md}, and
\\path{notes/ROOT_SEARCH_LOG_12.md}, and
\\path{notes/ROOT_SEARCH_LOG_13.md}, and
\\path{notes/ROOT_SEARCH_LOG_14.md}, and
\\path{notes/ROOT_SEARCH_LOG_15.md}, and
\\path{notes/ROOT_SEARCH_LOG_16.md}, and
\\path{notes/ROOT_SEARCH_LOG_17.md}, and
\\path{notes/ROOT_SEARCH_LOG_18.md}, and
\\path{notes/ROOT_SEARCH_LOG_19.md}, and
\\path{notes/ROOT_SEARCH_LOG_20.md}, and
\\path{notes/ROOT_SEARCH_LOG_21.md}, and
\\path{notes/ROOT_SEARCH_LOG_22.md}, and
\\path{notes/ROOT_SEARCH_LOG_23.md}, and
\\path{notes/ROOT_SEARCH_LOG_24.md}, and
\\path{notes/ROOT_SEARCH_LOG_25.md}, and
\\path{notes/ROOT_SEARCH_LOG_26.md}, and
\\path{notes/ROOT_SEARCH_LOG_27.md}, and
\\path{notes/ROOT_SEARCH_LOG_28.md}
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
   if name=='monodromy/ppav_theta_cartier_symmetrizer.tex':
    out.write('\n\\input{sections/A_ppav_two_jets}\n')
    fixed_jets=a/'monodromy/nonordinary_ppav_fixed_point_jets.tex'
    if fixed_jets.exists() and '\\status{Candidate' not in fixed_jets.read_text():
     out.write('\n'+fixed_jets.read_text()+'\n')
   if path.exists(): out.write('\n'+path.read_text()+'\n')
  if target=='A_monodromy.tex':
   for extra in ['monodromy/supersingular_product_degree_two.tex',
                 'monodromy/supersingular_product_degree_three.tex',
                 'obstructions_crystals/A3_ppav_surface_ranks.tex',
                 'obstructions_crystals/A3_separable_polarization_ranks.tex',
                 'obstructions_crystals/A3_ordinary_all_polarizations.tex',
                 'obstructions_crystals/A3_ordinary_arbitrary_embedding.tex',
                 'obstructions_crystals/A3_mixed_all_product_ranks.tex',
                 'obstructions_crystals/A3_mixed_nonproduct_ranks.tex',
                 'obstructions_crystals/A3_mixed_axis_norms.tex',
                 'obstructions_crystals/A3_mixed_thin_strip_residues.tex',
                 'obstructions_crystals/A3_mixed_positive_index_bounds.tex',
                 'obstructions_crystals/A3_mixed_positive_index_variation.tex',
                 'obstructions_crystals/A3_mixed_positive_index_bundles.tex',
                 'obstructions_crystals/A3_mixed_positive_index_trace_radicals.tex',
                 'obstructions_crystals/A3_mixed_positive_index_pencil.tex',
                 'obstructions_crystals/A3_mixed_positive_index_cup_derivative.tex',
                 'obstructions_crystals/A3_mixed_positive_index_trace_zero.tex',
                 'obstructions_crystals/A3_mixed_positive_index_monad.tex',
                 'obstructions_crystals/A3_mixed_common_polarization_power.tex',
                 'obstructions_crystals/A3_mixed_positive_index_Petri.tex',
                 'obstructions_crystals/A3_mixed_positive_index_smooth_pencil.tex',
                 'obstructions_crystals/A3_mixed_positive_index_residual_boundary.tex',
                 'obstructions_crystals/A3_mixed_positive_index_unipotent.tex',
                 'obstructions_crystals/A3_mixed_positive_index_boundary_kernel.tex',
                 'obstructions_crystals/A3_mixed_positive_index_twisted_pencil.tex',
                 'monodromy/supersingular_self_tacnode.tex',
                 'monodromy/supersingular_triple_point.tex',
                 'monodromy/supersingular_global_contact_witness.tex',
                 'monodromy/supersingular_global_tangent_triples.tex',
                 'monodromy/supersingular_level3_collision_reduction.tex',
                 'monodromy/supersingular_uniform_contact.tex',
                 'monodromy/supersingular_uniform_source_smoothness.tex',
                 'monodromy/supersingular_uniform_collision_exclusion.tex',
                 'obstructions_crystals/A4_contact_third_value_smoothness.tex',
                 'obstructions_crystals/A4_uniform_tangent_triple_type.tex',
                 'monodromy/supersingular_uniform_tangent_triples.tex',
                 'monodromy/supersingular_all_odd_groups.tex',
                 'monodromy/supersingular_even_image_sheaf.tex',
                 'monodromy/supersingular_all_even_groups.tex',
                 'monodromy/generic_mixed_product_all_groups.tex',
                 'monodromy/mixed_degree_one_uniform_full_groups.tex',
                 'monodromy/mixed_degree_two_uniform_full_groups.tex',
                 'monodromy/mixed_three_by_b_strip_groups.tex',
                 'monodromy/mixed_degree_three_norm_groups.tex',
                 'monodromy/mixed_all_odd_norm_groups.tex',
                 'monodromy/mixed_all_even_groups.tex',
                 'monodromy/nonordinary_ppav_uniform_Q_inertia.tex']:
    path=a/extra
    if path.exists() and '\\status{Candidate' not in path.read_text():
     if extra=='obstructions_crystals/A3_mixed_axis_norms.tex':
      seed=s/'A_mixed_six_three_seed.tex'
      assert seed.exists() and '\\status{Candidate' not in seed.read_text()
      out.write('\n\\input{sections/A_mixed_six_three_seed}\n')
     out.write('\n'+path.read_text()+'\n')
   out.write('\n\\input{sections/A_nonordinary_ppav_Coble_ranks}\n')
   for extra in ['monodromy/nonordinary_ppav_polar_Lang_conditional.tex',
                 'monodromy/p_rank_zero_ppav_degree_one_groups.tex',
                 'monodromy/p_rank_one_ppav_degree_one_groups.tex',
                 'monodromy/nonordinary_ppav_odd_natural_blocks.tex',
                 'monodromy/nonordinary_three_theta_graph_reduction.tex',
                 'monodromy/nonordinary_genus_two_triple_ramification.tex',
                 'monodromy/nonordinary_ppav_degree_three_node_gluing.tex']:
    path=a/extra
    if path.exists() and '\\status{Candidate' not in path.read_text():
     out.write('\n'+path.read_text()+'\n')
   for root_section in ['A_nonordinary_trigonal_direct', 'A_nonordinary_three_neighbor_boundary', 'A_nonordinary_degree_three_full']:
    rp=s/(root_section+'.tex')
    if rp.exists() and '\\status{Candidate' not in rp.read_text():
     out.write('\n\\input{sections/'+root_section+'}\n')
   for late_a in ['reduction_descent/A_nonordinary_powers_three.tex',
                  'monodromy/nonordinary_ppav_degree_two_wreath_theta.tex',
                  'monodromy/nonordinary_ppav_even_addition.tex',
                  'monodromy/nonordinary_five_theta_self_isogenies.tex',
                  'monodromy/nonordinary_uniform_five_theta_geometry.tex',
                  'monodromy/nonordinary_good_theta_norm_transfer.tex',
                  'monodromy/nonordinary_odd_theta_nodality_reduction.tex',
                  'monodromy/nonordinary_uniform_seven_theta_geometry.tex',
                  'monodromy/nonordinary_rank_one_bad_five_kernel.tex',
                  'monodromy/nonordinary_nine_theta_norm_transfer.tex',
                  'monodromy/nonordinary_arbitrary_odd_neighbors.tex',
                  'monodromy/nonordinary_cubic_component_norm_transfer.tex',
                  'monodromy/nonordinary_uniform_eleven_theta_geometry.tex']:
    lp=a/late_a
    if lp.exists() and '\\status{Candidate' not in lp.read_text():
     out.write('\n'+lp.read_text()+'\n')
   out.write('\n\\input{sections/A_route_limitations}\n')
   interpolation=a/'obstructions_crystals/A4_product_Frobenius_interpolation.tex'
   if interpolation.exists() and '\\status{Candidate' not in interpolation.read_text():
    out.write('\n'+interpolation.read_text()+'\n')
   out.write('\n\\input{sections/A_nonordinary_ppav_covectors}\n')
   generic_ppav=a/'monodromy/generic_nonordinary_ppav_groups.tex'
   if generic_ppav.exists() and '\\status{Candidate' not in generic_ppav.read_text():
    out.write('\n'+generic_ppav.read_text()+'\n')
   rectangular=s/'A_supersingular_rectangular_ranks.tex'
   if rectangular.exists() and 'Candidate proof' not in rectangular.read_text():
    out.write('\n\\input{sections/A_supersingular_rectangular_ranks}\n')
   all_rectangles=a/'obstructions_crystals/A3_supersingular_all_rectangular_ranks.tex'
   if all_rectangles.exists() and 'Candidate proof' not in all_rectangles.read_text():
    out.write('\n'+all_rectangles.read_text()+'\n')
  if target=='B.tex':
   for extra in ['B_height_two_graph_gate.tex','B_height_two_logarithm_gate.tex','B_height_two_elliptic_realization.tex','B_height_two_discriminant_gate.tex','B_height_two_scalar_residual_gate.tex','B_height_two_c4_residual_gate.tex','B_height_two_c3_residual_gate.tex','B_height_two_c4_orientation_gate.tex','B_height_two_c3_quotient_exclusion.tex','B_height_two_c4_final_exclusion.tex','B_p2_character_level3.tex','B_p2_height_two_mixed_gate.tex','B_p2_height_two_log_gate.tex','B_p2_residual_trivial_gate.tex','B_p2_residual_c2_gate.tex','B_p2_residual_c3_final.tex']:
    path=a/'reduction_descent'/extra
    if path.exists() and '\\status{Candidate' not in path.read_text(): out.write('\n'+path.read_text()+'\n')
for late_b_name in ['B_tame_minimal_height_two.tex',
                    'B_tame_norm_square_boundary.tex',
                    'B_tame_primitive_norm_orbits.tex',
                    'B_tame_CM_gate.tex',
                    'B_tame_residual_cycle.tex',
                    'B_tame_CM_neighborhood.tex',
                    'B_tame_minimal_wild_layer.tex',
                    'B_tame_cubic_wild_layer.tex',
                    'B_tame_cubic_wild_exhaustion.tex',
                    'B_tame_full_wild_projective.tex',
                    'B_tame_full_wild_quadratic.tex',
                    'B_tame_reducible_newton.tex',
                    'B_tame_reducible_recovery.tex',
                    'B_tame_cyclic_level_counterexamples.tex',
                    'B_cyclic_torsion_threshold.tex',
                    'B_tame_quotient_weight_gate.tex',
                    'B_p5_e12_high_quotient.tex',
                    'B_middle_tame_quotient.tex',
                    'B_tame_irreducible_arbitrary_index.tex',
                    'B_initial_tame_sector.tex',
                    'B_one_slope_quotient.tex',
                    'B_next_tame_boundary.tex',
                    'B_marked_quotient_sector.tex',
                    'B_first_level_mixed_boundary.tex',
                    'B_rational_high_line.tex',
                    'B_iterated_high_quotient.tex',
                    'B_terminal_frobenius_pair.tex',
                    'B_wild_cyclic_point.tex',
                    'B_first_wild_finite_patterns.tex',
                    'B_wild_CM_layer.tex',
                    'B_first_wild_irreducible_image.tex']:
 late_b=a/'reduction_descent'/late_b_name
 if late_b.exists() and '\\status{Candidate' not in late_b.read_text():
  with (s/'B.tex').open('a') as out: out.write('\n'+late_b.read_text()+'\n')
bibs=[rootbib,a/'monodromy/references.bib',a/'monodromy/references_post_CP16.bib',a/'reduction_descent/reduction_descent.bib',a/'obstructions_crystals/D_E_references.bib']
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
