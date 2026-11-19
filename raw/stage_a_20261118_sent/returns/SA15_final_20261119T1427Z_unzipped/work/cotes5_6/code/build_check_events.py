from build_dossier import ROOT,DATE,RUN,items
from build_claims import claims,claimkeys
import json,csv
events=[]
def E(ident,typ,outcome):events.append(dict(statement_id=ident,date=DATE,who=RUN,type=typ,outcome=outcome))
# All source-entry comparisons were performed against the actual transcription,
# not against each entry's own paraphrase. This event does not certify the ink or proof.
for i in items:
    E(i['id'],'used and rechecked in this run','Textual cross-check only: the cited manuscript scanblock and source notes were read; '+i['check_reason']+' No scan/ink verification or theorem proof is implied.')
reproof={
 'q_valuation','pd_monic_normalform','pd_weighted_ideal','pd_length','pd_weight_nilpotent','pd_translation',
 'height_dimension','height_dyadic','legendre','valuation_threshold','topos_exists','topos_universal','topos_action_test',
 'nilpotent_bound','principal_annihilator','gamma_p_unique','principal_pd_construction','dvr_existence','dvr_pd_nilpotence',
 'graded_derham','local_m3','continuous_derivations','finite_target_quotient','formal_series_differentials','duality_coefficients',
 'discrete_zp_test','frob_chain','evaluation_nonfaithful','integral_connection_counterexample','rational_bicrystal','isogeny_quotient',
 'unbounded_torsion','rational_dual','integral_dual_failure','bounded_f_lattice','bounded_fv_lattice','tate_effectivity',
 'proper_algebraization','connection_not_free','frobenius_lifts','bt_hom_additive','potential_ordinary_image',
 'gamma_unit_refinement','spin_11_refinement','cm_image_refinement','twist_refinement'}
computations={
 **dict.fromkeys(['q_valuation','legendre','valuation_threshold','gamma_p_unique','gamma_p_exists'],'factorial_identities; finite p=2,3,5,7 and n≤100 arithmetic only, not an existence proof for a PD structure'),
 **dict.fromkeys(['pd_monic_normalform','pd_weighted_ideal','pd_length','pd_weight_nilpotent','pd_translation'],'normal_form_checks; 20 finite (p,ν,r) cases, coordinate containment and Smith valuations; the all-parameter argument is separate'),
 **dict.fromkeys(['gamma_coefficient_modp','gamma_unit_refinement'],'c_n_mod_p_counterexample; p=3,n=2 gives residue2'),
 'principal_pd_bad':'principal_ideal_counterexample; exact multiplication/associativity and missing ideal membership',
 **dict.fromkeys(['dvr_existence','dvr_pd_nilpotence'],'DVR_boundary; the listed p,e values and n=p^r subsequences only'),
 'graded_derham':'graded_monomial_de_rham; five finite quotient differential matrices',
 'artin_derham_counterexample':'artinian_de_rham_H0_counterexample; exact Gröbner reduction and dimension16',
 'pd_log_literal':'log_sign_counterexample; exact dual-number calculation',
 **dict.fromkeys(['spin_components','spin_11_refinement'],'Spin_1_1_check; norm and image computation in signature(1,1) only'),
 **dict.fromkeys(['frob_chain','frob_closed'],'characteristic_p_affine_line and char_p_nonreduced_Frobenius; explicit polynomial/dual-number tests'),
 **dict.fromkeys(['supersingular_open_image','cm_image_refinement'],'supersingular_CM_counterexample; discriminant, point count and centralizer linear equations'),
 **dict.fromkeys(['nonintegral_j_multiplicative','tate_valuation','twist_refinement'],'ramified_Tate_twist_counterexample; valuation arithmetic for q=d=5, with theoretical uniformization premise stated')}
refutations={
 'pd_log_literal':'pd_exp','principal_pd_bad':'principal_pd_construction','gamma_coefficient_modp':'gamma_unit_refinement',
 'frob_closed':'frob_kernel_smooth','spin_components':'spin_11_refinement','supersingular_open_image':'cm_image_refinement',
 'nonintegral_j_multiplicative':'twist_refinement','fv_literal':'rational_bicrystal'}
published_checks={
 'q_connection','chern_necessary','cm_conductor','pd_free','pd_envelope','pd_quotient','gamma_p_exists','ega_normality','kuiper',
 'polynomial_coefficients','etale_poincare_duality','period_poincare','cartesian_crystals','global_pushout','stratification_cocycle',
 'cartier_descent','iterated_frobenius','localized_site_cohom','site_hypercohomology','f_crystal_family','h1_dieudonne',
 'qc_site_crystals','ordinary_cohomology','gauss_manin_integrability','derham_leray','derived_crys','hodge_lift_deformation',
 'serre_tate','universal_abelian_extension','modular_obstruction','universal_bt_extension','tate_recovery','ordinary_tate_extension',
 'canonical_ordinary_parameter','potential_good','bt_good_reduction','frob_kernel_smooth'}
targeted_checks={
 'stratified_free_smooth':'BO1978 Proposition2.16 and Note2.17: full Artin-neighborhood descent proof and no-smoothness hypothesis checked; reconstructed audit in reviews/independent_proofs.md.',
 'exact_left_adjoint':'Stacks12.29.1: apply adjunction to the exact Hom functor of an injective and use exactness of the left adjoint; this checks precisely the preservation-of-injectives lemma, not the manuscript’s missing exactness.',
 'pd_quotient':'Stacks23.4.2–4: addition/scalar/iteration proof of PD-stability of the generated ideal read and compared, with positive-degree indices retained.',
 'principal_pd_construction':'Stacks23.2.2: torsion-free embedding into the rational algebra checks both necessity and sufficiency of ideal membership.'}
for c in claims:
    k=c['internal_key'];ident=c['id']
    if k in reproof:
        E(ident,'independent re-proof','The general argument is recorded in reviews/independent_proofs.md or the claim statement/hypothesis analysis. Scope is the explicitly formulated restricted assertion; standard background is identified, not freshly reproved.')
    if k in computations:
        E(ident,'computation or formal certificate','Executed code/recheck_algebra.py; exact output in outputs/algebra_checks.json and .txt. Checked part: '+computations[k]+'. Finite tests are corroborative where a general assertion is involved. No Lean or other proof-assistant certificate executed.')
    if k in targeted_checks:
        E(ident,'targeted proof check',targeted_checks[k])
    if k in refutations:
        target=refutations[k]
        typ='refuted, with the refined statement’s id'
        out='Literal assertion refuted by the checked example or algebraic contradiction; refined statement '+claimkeys[target]+'. '+c['fate']
        E(ident,typ,out)
    elif k in published_checks:
        E(ident,'used and rechecked in this run','Published statement and relevant hypotheses matched to the manuscript, without claiming a complete proof audit: '+c['fate'])
    elif k not in reproof and k not in computations and k not in targeted_checks:
        E(ident,'carried as background without fault found','No new proof certificate claimed. Source formulation, explicit doubts/retractions and limits were checked; the present mathematical status is: '+c['fate'])
for r in json.loads((ROOT/'reference_evidence.json').read_text()):
    E(r['key'],'used and rechecked in this run',r['verification_scope']+' Locator: '+r['exact_locator']+'. '+r['limitations'])
with (ROOT/'check_events.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
print(f'Saved {len(events)} scoped check events.')
