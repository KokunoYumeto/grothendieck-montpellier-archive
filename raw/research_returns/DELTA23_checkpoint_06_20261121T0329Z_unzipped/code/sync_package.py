"""Stage the current research documents. This does not create/save a checkpoint."""
from pathlib import Path
import shutil, csv, json, hashlib

root=Path(__file__).resolve().parents[2]
work=root/'work'; out=work/'package'
for name in ('proofs','agents','records','code','notes'):
    (out/name).mkdir(parents=True,exist_ok=True)
sources={
 'local_symbols.tex':work/'notes/local_symbols.tex',
 'kubota_test.tex':work/'notes/kubota_test.tex',
 'second_quaternion.tex':work/'notes/second_quaternion.tex',
 'prime_three_symbols.tex':work/'notes/prime_three_symbols.tex',
 'transvection_rigidity.tex':work/'notes/transvection_rigidity.tex',
 'order_five_frame.tex':work/'agents/five_level_six/order_five_frame.tex',
 'order_five_arithmetic.tex':work/'agents/five_level_six/order_five_arithmetic.tex',
 'order_five_comparison_draft.tex':work/'agents/five_level_six/order_five_comparison_draft.tex',
 'level_six.tex':work/'agents/five_level_six/level_six.tex',
 'symplectic_collapse.tex':work/'agents/five_level_six/symplectic_collapse.tex',
 'descendant_characters.tex':work/'agents/characters/proofs/descendant_characters.tex',
 'adelic_frames.tex':work/'agents/characters/proofs/adelic_frames_draft.tex',
 'four_point_central_flips.tex':work/'agents/pentagon/four_point_central_flips.tex',
 'affine_cubic_detector.tex':work/'agents/pentagon/affine_cubic_detector.tex',
 'twisted_affine_obstruction.tex':work/'agents/pentagon/twisted_affine_obstruction.tex',
 'krammer_cubic_extension.tex':work/'agents/pentagon/krammer_cubic_extension.tex',
 'krammer_quotient_extension.tex':work/'agents/five_level_six/krammer_quotient_extension.tex',
 'krammer_mixed_correlation.tex':work/'agents/characters/proofs/krammer_mixed_correlation.tex',
 'krammer_pentagon_count.tex':work/'agents/pentagon/krammer_pentagon_count.tex',
 'krammer_three_pair_commonword.tex':work/'agents/pentagon/krammer_three_pair_commonword.tex',
 'krammer_all_five_commonword.tex':work/'agents/pentagon/krammer_all_five_commonword.tex',
 'cubic_detector_216.tex':work/'agents/pentagon/cubic_detector_216.tex',
 'krammer_s4_obstruction.tex':work/'agents/five_level_six/krammer_s4_obstruction.tex',
 'krammer_solvable_correlation.tex':work/'agents/five_level_six/krammer_solvable_correlation.tex',
 'krammer_induced_frame_ambiguity.tex':work/'agents/five_level_six/krammer_induced_frame_ambiguity.tex',
 'krammer_s3_obstruction.tex':work/'agents/five_level_six/krammer_s3_obstruction.tex',
 'level_six_congruence.tex':work/'agents/five_level_six/level_six_congruence.tex',
 'krammer_harmonic_cover.tex':work/'agents/five_level_six/krammer_harmonic_cover.tex',
 'cyclic12_cover.tex':work/'agents/five_level_six/cyclic12_cover.tex',
 'induced_s4_and_relative_homology.tex':work/'agents/characters/proofs/induced_s4_and_relative_homology.tex',
 'cubic_dessin_rational_quotient.tex':work/'agents/characters/proofs/cubic_dessin_rational_quotient.tex',
 'distribution_no_go.tex':work/'notes/distribution_no_go.tex',
 'cubic_descent.tex':work/'agents/five_level_six/cubic_descent.tex',
 'hurwitz_finite_escape.tex':work/'agents/pentagon/hurwitz_finite_escape.tex',
 'krammer_nielsen_perfect.tex':work/'agents/characters/proofs/krammer_nielsen_perfect.tex',
 'cubic_descent_harmonic.tex':work/'agents/pentagon/cubic_descent_harmonic.tex',
 'cubic_descent_full.tex':work/'agents/five_level_six/cubic_descent_full.tex',
 'krammer_solvable_s3.tex':work/'agents/five_level_six/krammer_solvable_s3.tex',
 'joint_hurwitz_krammer_escape.tex':work/'agents/pentagon/joint_hurwitz_krammer_escape.tex',
 'relative_seed_obstruction.tex':work/'agents/pentagon/relative_seed_obstruction.tex',
 'cubic_descent_iterate.tex':work/'agents/pentagon/cubic_descent_iterate.tex',
 'orbital_cubic_pentagon.tex':work/'agents/characters/proofs/orbital_cubic_pentagon.tex',
 'orbital_harmonic_pentagon.tex':work/'agents/characters/proofs/orbital_harmonic_pentagon.tex',
 'krammer_orbital_unitary.tex':work/'agents/five_level_six/krammer_orbital_unitary.tex',
 'krammer_orbital_sign.tex':work/'agents/five_level_six/krammer_orbital_sign.tex',
 'orbital_affine216.tex':work/'agents/five_level_six/orbital_affine216.tex',
 'krammer_harmonic_orbital.tex':work/'agents/five_level_six/krammer_harmonic_orbital.tex',
 'hurwitz_cubic216_extension.tex':work/'agents/pentagon/hurwitz_cubic216_extension.tex',
 'hurwitz_gt_stability.tex':work/'agents/pentagon/hurwitz_gt_stability.tex',
 'hurwitz36_stability.tex':work/'notes/hurwitz36_stability.tex',
 'galois_normalization.tex':work/'notes/galois_normalization.tex',
 'hurwitz_mixed72_quotient.tex':work/'agents/characters/proofs/hurwitz_mixed72_quotient.tex',
 'hurwitz_orthogonal_geometry.tex':work/'agents/characters/proofs/hurwitz_orthogonal_geometry.tex',
 'hurwitz_block_structure.tex':work/'agents/five_level_six/hurwitz_block_structure.tex',
 'hurwitz_cup_pairing.tex':work/'agents/pentagon/hurwitz_cup_pairing.tex',
 'hurwitz_h1_orthogonal_lifts.tex':work/'notes/hurwitz_h1_orthogonal_lifts.tex',
 'hurwitz_block11_harmonic.tex':work/'notes/hurwitz_block11_harmonic.tex',
 'hurwitz_global_innerness.tex':work/'agents/pentagon/hurwitz_global_innerness.tex',
 'hurwitz_normalized_socle.tex':work/'agents/five_level_six/hurwitz_normalized_socle.tex',
 'hurwitz_first_four_block_lifts.tex':work/'agents/pentagon/hurwitz_first_four_block_lifts.tex',
 'hurwitz_mixed_solvable.tex':work/'agents/five_level_six/hurwitz_mixed_solvable.tex',
 'hurwitz_mixed72_actual_covariance.tex':work/'agents/characters/proofs/hurwitz_mixed72_actual_covariance.tex',
 'hurwitz_global_conjugators.tex':work/'agents/pentagon/hurwitz_global_conjugators.tex',
 'hurwitz_first_pair_covariance.tex':work/'agents/five_level_six/hurwitz_first_pair_covariance.tex',
 'hurwitz_product_fixed_cover.tex':work/'notes/hurwitz_product_fixed_cover.tex',
 'hurwitz_raw_linear_lifts.tex':work/'agents/pentagon/hurwitz_raw_linear_lifts.tex',
 'hurwitz_solvable_commonword.tex':work/'notes/hurwitz_solvable_commonword.tex',
 'hurwitz_mixed_full_covariance.tex':work/'agents/characters/proofs/hurwitz_mixed_full_covariance.tex',
 'hurwitz_first_maximal_solvable.tex':work/'agents/five_level_six/hurwitz_first_maximal_solvable.tex',
 'hurwitz_first_value_uniqueness.tex':work/'agents/five_level_six/hurwitz_first_value_uniqueness.tex',
 'hurwitz_pentagon45_reduction.tex':work/'notes/hurwitz_pentagon45_reduction.tex',
 'hurwitz_required_f45.tex':work/'agents/pentagon/hurwitz_required_f45.tex',
 'hurwitz_raw_simultaneous_covariance.tex':work/'agents/pentagon/hurwitz_raw_simultaneous_covariance.tex',
 'hurwitz_raw_pentagon45.tex':work/'agents/pentagon/hurwitz_raw_pentagon45.tex',
 'hurwitz_raw_survivor_covariance.tex':work/'agents/pentagon/hurwitz_raw_survivor_covariance.tex',
 'hurwitz_raw_solvable_quotient.tex':work/'agents/five_level_six/hurwitz_raw_solvable_quotient.tex',
 'hurwitz_mixed72_gentle_core.tex':work/'agents/characters/proofs/hurwitz_mixed72_gentle_core.tex',
 'hurwitz_full_mixed_gentle_core.tex':work/'agents/characters/proofs/hurwitz_full_mixed_gentle_core.tex',
 'hurwitz_mixed45_cycle_link.tex':work/'agents/characters/proofs/hurwitz_mixed45_cycle_link.tex',
 'hurwitz_full_commonword.tex':work/'notes/hurwitz_full_commonword.tex',
 'pure_frame_abelian_constraints.tex':work/'notes/pure_frame_abelian_constraints.tex',
 'hurwitz_mixed_source_intertwiners.tex':work/'agents/pentagon/hurwitz_mixed_source_intertwiners.tex',
 'hurwitz_candidate_power_normalization.tex':work/'agents/characters/proofs/hurwitz_candidate_power_normalization.tex',
 'hurwitz_complex_conjugation_normalization.tex':work/'agents/characters/proofs/hurwitz_complex_conjugation_normalization.tex',
 'hurwitz_conjugate_closure_normalization.tex':work/'agents/characters/proofs/hurwitz_conjugate_closure_normalization.tex',
 'hurwitz_spherical_order5.tex':work/'agents/pentagon/hurwitz_spherical_order5.tex',
 'hurwitz_spherical_socle.tex':work/'agents/five_level_six/hurwitz_spherical_socle.tex',
 'hurwitz_full_spherical_covariance.tex':work/'agents/pentagon/hurwitz_full_spherical_covariance.tex',
 'hurwitz_last_coordinate.tex':work/'agents/five_level_six/hurwitz_last_coordinate.tex',
 'hurwitz_central_extension_obstruction.tex':work/'agents/pentagon/hurwitz_central_extension_obstruction.tex',
 'affine216_last_meridian_gate.tex':work/'agents/characters/proofs/affine216_last_meridian_gate.tex',
 'affine216_pure_pentagon_obstruction.tex':work/'notes/affine216_pure_pentagon_obstruction.tex',
 'hurwitz_colored_raw_gate.tex':work/'agents/pentagon/hurwitz_colored_raw_gate.tex',
 'hurwitz_colored_raw_unique_lift.tex':work/'agents/pentagon/hurwitz_colored_raw_unique_lift.tex',
 'hurwitz_first_cabling.tex':work/'agents/five_level_six/hurwitz_first_cabling.tex',
 'hurwitz_multiplier5_global.tex':work/'agents/characters/proofs/hurwitz_multiplier5_global.tex',
 'binary_tetrahedral_half_character.tex':work/'agents/characters/proofs/binary_tetrahedral_half_character.tex',
 'hurwitz_source_commonword.tex':work/'agents/five_level_six/hurwitz_source_commonword.tex',
 'hurwitz_cabling_finite_closure.tex':work/'agents/five_level_six/hurwitz_cabling_finite_closure.tex',
 'hurwitz_prefix_recursion.tex':work/'agents/five_level_six/hurwitz_prefix_recursion.tex',
 'affine216_universal_gate.tex':work/'notes/affine216_universal_gate.tex',
}
for name,path in sources.items():
    if path.exists(): shutil.copy2(path,out/'proofs'/name)
for name in ('agents','records','code','notes'):
    for path in (work/name).rglob('*'):
        if not path.is_file() or '__pycache__' in path.parts: continue
        if path.suffix in ('.pyc','.zip'): continue
        dest=out/name/path.relative_to(work/name)
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(path,dest)
shutil.copy2(work/'RUN_START.txt',out/'RUN_START.txt')
events=[]
for path in [work/'records/root_check_events.tsv',*sorted((work/'agents').glob('*/CHECK_EVENTS.tsv'))]:
    if not path.exists(): continue
    with path.open(newline='') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            events.append({
              'statement_id':row.get('statement_id',''),
              'date':row.get('date',row.get('date_utc','')),
              'who_model_effort_run':row.get('who_model_effort_run',row.get('who','')),
              'type':row.get('type',''),
              'outcome':row.get('outcome',''),
              'locator_or_method':row.get('locator_or_method',row.get('locator',''))})
keys=['statement_id','date','who_model_effort_run','type','outcome','locator_or_method']
with (out/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=keys,delimiter='\t');writer.writeheader();writer.writerows(events)
manifest=[]
for path in sorted(out.rglob('*')):
    if path.is_file() and path.name!='PACKAGE_MANIFEST.json':
        manifest.append({'path':str(path.relative_to(out)),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
(out/'PACKAGE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(f'Staged {len(manifest)} files and {len(events)} check events; no checkpoint saved.')
