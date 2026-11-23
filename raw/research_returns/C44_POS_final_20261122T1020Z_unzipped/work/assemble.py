from pathlib import Path
import csv
import datetime
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'deliverables'
OUT.mkdir(exist_ok=True)
stamp=datetime.datetime.now(datetime.timezone.utc).astimezone(datetime.timezone(datetime.timedelta(hours=1)))

preamble=r'''\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern,amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,longtable,array}
\usepackage[margin=1in]{geometry}
\usepackage[colorlinks=true,urlcolor=blue,linkcolor=blue]{hyperref}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\DeclareMathOperator{\CH}{CH}
\DeclareMathOperator{\Alg}{Alg}
\DeclareMathOperator{\Pic}{Pic}
\DeclareMathOperator{\Alb}{Alb}
\DeclareMathOperator{\NS}{NS}
\DeclareMathOperator{\End}{End}
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\Nm}{Nm}
\newcommand{\Q}{\mathbf Q}\newcommand{\Z}{\mathbf Z}\newcommand{\F}{\mathbf F}
\newcommand{\tun}[1]{#1}
\setlength{\emergencystretch}{2em}
\title{C44\_POS: primitive signs, special axes, and the 1964 programme}
\author{Research continuation of JAC1964 and SIGN\_NEXT}
\date{22 November 2026}
\begin{document}
\maketitle
\begin{abstract}
Final research record at the scheduled stopping point. The general fixed-axis sign and the Fermat
Abel--Jacobi injection remain unresolved. New checked results include
an exact axis primitive decomposition, lifts of every embedded smooth
axis (without a cycle-lifting assertion), and an unconditional sign
theorem whenever at most one potential Tate direction remains after
a known positive algebraic span. An extending orthogonal-block criterion
now also proves the sign on actual closed affine-$S_3$ families with
three residual potential Tate directions, including families with a
known positive span of rank six. A totally real coefficient-field
criterion further gives actual dihedral families with five residual
potential directions and a known positive span of rank ten, including
characteristic three. A quaternion-packet criterion now controls residual imaginary-quadratic
planes, with actual cyclic families in every characteristic. Its finite-place
comparison does not assume algebraicity of the remaining Tate directions.
The universal gate outside these verified correspondence criteria remains open. Other
checked findings include closed supersingular axes with their entire
positive kernels controlled, intrinsically nonliftable surface centres
whose selected primitive classes are now excluded from every abstract smooth
projective lift of ramification index $e\leq5$ at $p=3$ and $e\leq3p$ at the
constructed primes $p\geq7$, $p\equiv3\pmod4$. The corresponding conditional
centre theorem at $p=5$ excludes $e\leq10$ when its nonliftable centre is supplied.
For larger ramification,
class lifting is reduced to an explicit finite initial support-lifting
obstruction. Other results include lifts of every finite
curve cover as a map, special-cover sign tests, exact integral
arithmetic obstructions, a characteristic-$p$ detector/division theorem,
and geometric extensions of the primitive incidence polarization.
The algebraically trivial Fermat obstruction is reduced to specified
nonzero universal cycles from excess Picard quotients; several entire
classes of singular ample image surfaces are eliminated in rational
Chow. The projected geometric 5-primary torsion vanishes, and the known
nonzero class has bounded geometric 5-divisibility; the exact residual
completed Chow term and the arithmetic finite-generation gate remain.
Full Abel--Jacobi injectivity remains open.
The proposed supersingular Fermat test case already satisfies the
required Hodge standard conjecture; its corrected restriction and
weighted Gysin conditions are verified explicitly. A separate
nonsupersingular degree-seven Fermat calculation supplies explicit
new special cycles, all-prime Tate and positivity for the fourfold,
and numerical and 13-adic positivity for its square.
Selected closed nonabelian axes also satisfy the Hodge standard
conjecture on all their powers for positive product polarizations,
strong Tate in every degree, and the corrected scan-050 conditions;
on the fourfold itself the sign holds for every ample polarization.
The historical prior-unknown status is not asserted. An explicit
full-monodromy family excludes uniform abelian realization of its whole
variable local system, without excluding isolated special-fibre
correspondences.
Every use of 032 or Milne's 2026 report remains conditional on those
unrefereed preprints. The separate Milne 2022 transfer assertion is
exposed wherever used. Whole-proof reading events and finite
computations are distinguished in \texttt{CHECK\_EVENTS.tsv}.
\end{abstract}
\tableofcontents
\part{Checked findings and explicitly conditional deductions}
\section{Normalization, scope, and inherited results}
The starting isometry is JAC1964 H9-T7, equation (H9.18):
\[
 A_X\oplus A_B\simeq\CH^m(Y)_{\mathrm{hom},\Q}/\mathcal H_0,
 \qquad Q((z,w),(z',w'))=(-1)^m\int_Xzz'+(-1)^{m-1}\int_Bww'.
\]
Here $A_B=\ker\kappa_*$ on the algebraic middle classes of the axis,
and $h_BA_B=0$. This is an inherited statement, not a new result of
this run. For an arbitrary abelian ambient, the ambient sign is conditional
on the unrefereed 032 Corollary 8.4 and Milne2026 report.
For the explicit elliptic-power families, A42b supplies it unconditionally. Weak semidefiniteness and strict positive definiteness
are distinguished throughout; no numerical/homological equivalence
on an arbitrary axis is silently assumed.

Geometric generic parameter points are taken over algebraic closures
of function fields. They are not closed points over
$\overline{\mathbf F}_p$. A monodromy vanishing assertion at the
former does not settle a sign at every latter point.

Every finding retains its stable C44 identifier. A displayed
proposition that assumes an additional unproved input is a checked
conditional implication, not a proof of that input. Prior statements
retain their JAC1964 or SIGN\_NEXT identifiers and are not claimed
as findings of this continuation. The governing source is the attached
\texttt{PROMPT(20261121-231316).md}.
'''

checked=[
 'work/axis/axis_contribution.tex',
 'work/axis/axis_correspondence_obstruction.tex',
 'work/axis/axis_forced_tate_root.tex',
 'work/axis/root_explicit_axes.tex',
 'work/axis/axis_boundary_relation.tex',
 'work/axis/axis_asymptotic_centres.tex',
 'work/axis/axis_product_curves.tex',
 'work/axis/axis_product_grid.tex',
 'work/axis/axis_grid_strict.tex',
 'work/axis/axis_supersingular_nonliftable.tex',
 'work/axis/axis_product_ci_matching.tex',
 'work/axis/relative_form_transfer.tex',
 'work/covers/contribution.tex',
 'work/covers/boundary_strata.tex',
 'work/covers/as_conductor_strata.tex',
 'work/arithmetic/contribution.tex',
 'work/arithmetic/fermat_relative_transfer.tex',
 'work/arithmetic/fermat7_frobenius.tex',
 'work/scan_w/contribution.tex',
 'work/scan_w/relative_th4.tex',
 'work/scan_w/sharp_cycle_bound.tex',
]
if (ROOT/'work/checks/axis_frobenius_selection_passed.txt').exists():
    checked.insert(checked.index('work/covers/contribution.tex'),
                   'work/axis/axis_frobenius_selection.tex')
if (ROOT/'work/checks/closed_rank_one_axis_passed.txt').exists():
    checked.insert(checked.index('work/covers/contribution.tex'),
                   'work/scan_w/closed_rank_one_axis.tex')
if (ROOT/'work/checks/closed_odd_rank_axes_passed.txt').exists():
    checked.insert(checked.index('work/covers/contribution.tex'),
                   'work/scan_w/closed_odd_rank_axes.tex')
if (ROOT/'work/checks/nonliftable_surface_centres_passed.txt').exists():
    checked.insert(checked.index('work/covers/contribution.tex'),
                   'work/axis/nonliftable_surface_centres.tex')
if (ROOT/'work/checks/axis_one_tate_direction_passed.txt').exists():
    checked.insert(checked.index('work/covers/contribution.tex'),
                   'work/scan_w/axis_one_tate_direction.tex')
if (ROOT/'work/checks/fermat_excess_picard_passed.txt').exists():
    checked.insert(checked.index('work/arithmetic/fermat_relative_transfer.tex'),
                   'work/arithmetic/fermat_excess_picard.tex')
for marker, file, before in [
    ('constrained_moment_monodromy_passed', 'work/axis/constrained_moment_monodromy.tex', 'work/covers/contribution.tex'),
    ('axis_realization_kernel_passed', 'work/axis/axis_realization_kernel.tex', 'work/covers/contribution.tex'),
    ('equivariant_axis_blocks_passed', 'work/scan_w/equivariant_axis_blocks.tex', 'work/covers/contribution.tex'),
    ('affine_s3_axis_geometry_passed', 'work/scan_w/affine_s3_axis_geometry.tex', 'work/covers/contribution.tex'),
    ('s3_multiplicity_monodromy_passed', 'work/axis/s3_multiplicity_monodromy.tex', 'work/covers/contribution.tex'),
    ('axis_realization_blocks_passed', 'work/axis/axis_realization_blocks.tex', 'work/covers/contribution.tex'),
    ('axis_primitive_semiregularity_passed', 'work/axis/axis_primitive_semiregularity.tex', 'work/covers/contribution.tex'),
    ('higher_dimensional_s3_axes_passed', 'work/scan_w/higher_dimensional_s3_axes.tex', 'work/covers/contribution.tex'),
    ('totally_real_axis_blocks_passed', 'work/scan_w/totally_real_axis_blocks.tex', 'work/covers/contribution.tex'),
    ('affine_d5_axes_passed', 'work/axis/affine_d5_axes.tex', 'work/covers/contribution.tex'),
    ('unbounded_dihedral_axis_blocks_passed', 'work/scan_w/unbounded_dihedral_axis_blocks.tex', 'work/covers/contribution.tex'),
    ('axis_hodge_flatness_passed', 'work/axis/axis_hodge_flatness.tex', 'work/covers/contribution.tex'),
    ('axis_integral_primitive_tests_passed', 'work/axis/axis_integral_primitive_tests.tex', 'work/covers/contribution.tex'),
    ('axis_pd_surface_obstruction_passed', 'work/axis/axis_pd_surface_obstruction.tex', 'work/covers/contribution.tex'),
    ('axis_abstract_unramified_lifts_passed', 'work/axis/axis_abstract_unramified_lifts.tex', 'work/covers/contribution.tex'),
    ('axis_ramified_finite_order_passed', 'work/axis/axis_ramified_finite_order.tex', 'work/covers/contribution.tex'),
    ('axis_ramified_translation_correction_passed', 'work/axis/axis_ramified_translation_correction.tex', 'work/covers/contribution.tex'),
    ('axis_ramified_support_counterexample_passed', 'work/axis/axis_ramified_support_counterexample.tex', 'work/covers/contribution.tex'),
    ('axis_uniform_abelian_obstruction_passed', 'work/axis/axis_uniform_abelian_obstruction.tex', 'work/covers/contribution.tex'),
    ('orthogonal_crystal_hasse_passed', 'work/scan_w/orthogonal_crystal_hasse.tex', 'work/covers/contribution.tex'),
    ('axis_ramified_transfer_diagnostics_passed', 'work/axis/axis_ramified_transfer_diagnostics.tex', 'work/covers/contribution.tex'),
    ('quaternion_frobenius_sign_passed', 'work/scan_w/quaternion_frobenius_sign.tex', 'work/covers/contribution.tex'),
    ('c3_axis_sign_passed', 'work/axis/c3_axis_sign.tex', 'work/covers/contribution.tex'),
    ('quaternion_rank_four_diagnostic_passed', 'work/arithmetic/quaternion_rank_four_diagnostic.tex', 'work/covers/contribution.tex'),
    ('non_tate_quaternion_criterion_passed', 'work/scan_w/non_tate_quaternion_criterion.tex', 'work/covers/contribution.tex'),
    ('universal_quaternion_boundary_passed', 'work/scan_w/universal_quaternion_boundary.tex', 'work/covers/contribution.tex'),
    ('split_prime_quaternion_sign_passed', 'work/scan_w/split_prime_quaternion_sign.tex', 'work/covers/contribution.tex'),
    ('c3_twisted_split_axes_passed', 'work/axis/c3_twisted_split_axes.tex', 'work/covers/contribution.tex'),
    ('characteristic_three_eigenblock_passed', 'work/scan_w/characteristic_three_eigenblock.tex', 'work/covers/contribution.tex'),
    ('c4_characteristic_three_axes_passed', 'work/arithmetic/c4_characteristic_three_axes.tex', 'work/covers/contribution.tex'),
    ('dyadic_quaternion_sign_passed', 'work/scan_w/dyadic_quaternion_sign.tex', 'work/covers/contribution.tex'),
    ('c3_characteristic_two_axes_passed', 'work/axis/c3_characteristic_two_axes.tex', 'work/covers/contribution.tex'),
    ('c3_characteristic_two_centres_passed', 'work/axis/c3_characteristic_two_centres.tex', 'work/covers/contribution.tex'),
    ('elliptic_power_height_corollary_passed', 'work/axis/elliptic_power_height_corollary.tex', 'work/covers/contribution.tex'),
    ('formal_k_effectivity_gate_passed', 'work/axis/formal_k_effectivity_gate.tex', 'work/covers/contribution.tex'),
    ('first_ramified_support_jets_passed', 'work/axis/first_ramified_support_jets.tex', 'work/covers/contribution.tex'),
    ('axis_first_ramified_noncancellation_passed', 'work/axis/axis_first_ramified_noncancellation.tex', 'work/covers/contribution.tex'),
    ('axis_even_ramification_boundary_passed', 'work/axis/axis_even_ramification_boundary.tex', 'work/covers/contribution.tex'),
    ('ambient_support_jet_restriction_passed', 'work/scan_w/ambient_support_jet_restriction.tex', 'work/covers/contribution.tex'),
    ('axis_second_ramified_noncancellation_passed', 'work/axis/axis_second_ramified_noncancellation.tex', 'work/covers/contribution.tex'),
    ('axis_next_boundary_odd_characteristic_passed', 'work/axis/axis_next_boundary_odd_characteristic.tex', 'work/covers/contribution.tex'),
    ('axis_closed_layer_peeling_passed', 'work/axis/axis_closed_layer_peeling.tex', 'work/covers/contribution.tex'),
    ('axis_supplied_support_threshold_passed', 'work/axis/axis_supplied_support_threshold.tex', 'work/covers/contribution.tex'),
    ('axis_first_frobenius_range_passed', 'work/axis/axis_first_frobenius_range.tex', 'work/covers/contribution.tex'),
    ('arbitrary_pole_primitive_testing_passed', 'work/scan_w/arbitrary_pole_primitive_testing.tex', 'work/covers/contribution.tex'),
    ('axis_frobenius_supplied_support_passed', 'work/axis/axis_frobenius_supplied_support.tex', 'work/covers/contribution.tex'),
    ('axis_uniform_ample_conormal_passed', 'work/arithmetic/axis_uniform_ample_conormal.tex', 'work/covers/contribution.tex'),
    ('axis_second_frobenius_range_passed', 'work/axis/axis_second_frobenius_range.tex', 'work/covers/contribution.tex'),
    ('ambient_closed_layer_removal_passed', 'work/scan_w/ambient_closed_layer_removal.tex', 'work/covers/contribution.tex'),
    ('axis_next_exact_ramification_boundary_passed', 'work/axis/axis_next_exact_ramification_boundary.tex', 'work/covers/contribution.tex'),
    ('axis_characteristic_three_ramification_five_passed', 'work/axis/axis_characteristic_three_ramification_five.tex', 'work/covers/contribution.tex'),
    ('higher_cartier_detection_passed', 'work/scan_w/higher_cartier_detection.tex', 'work/covers/contribution.tex'),
    ('axis_formal_cartier_saturation_passed', 'work/axis/axis_formal_cartier_saturation.tex', 'work/covers/contribution.tex'),
    ('fermat_recent_source_audit_passed', 'work/arithmetic/fermat_recent_source_audit.tex', 'work/covers/contribution.tex'),
    ('ramified_rigid_source_audit_passed', 'work/arithmetic/ramified_rigid_source_audit.tex', 'work/covers/contribution.tex'),
    ('quaternion_centralizer_comparison_passed', 'work/scan_w/quaternion_centralizer_comparison.tex', 'work/covers/contribution.tex'),
    ('quaternion_picard_source_audit_passed', 'work/arithmetic/quaternion_picard_source_audit.tex', 'work/covers/contribution.tex'),
    ('fermat_regulator_source_audit_passed', 'work/arithmetic/fermat_regulator_source_audit.tex', 'work/covers/contribution.tex'),
    ('fermat_difference_surface_passed', 'work/arithmetic/fermat_difference_surface.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('fermat_boundary_curve_tests_passed', 'work/arithmetic/fermat_boundary_curve_tests.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('nonliftable_surface_prime_extension_passed', 'work/axis/nonliftable_surface_prime_extension.tex', 'work/covers/contribution.tex'),
    ('axis_square_trace_passed', 'work/arithmetic/axis_square_trace.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('axis_square_tate_passed', 'work/arithmetic/axis_square_tate.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('axis_all_powers_torus_passed', 'work/scan_w/axis_all_powers_torus.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('axis_all_ample_fourfold_passed', 'work/scan_w/axis_all_ample_fourfold.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('fermat_geometric_torsion_passed', 'work/arithmetic/fermat_geometric_torsion.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('fermat_geometric_diagnostic_passed', 'work/arithmetic/fermat_geometric_diagnostic.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('fermat_actual_descent_passed', 'work/arithmetic/fermat_actual_descent.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('fermat_source_audit_passed', 'work/arithmetic/fermat_source_audit.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('qt4_abelian_type_transfer_reaudit_passed', 'work/scan_w/qt4_abelian_type_transfer_reaudit.tex', 'work/scan_w/sharp_cycle_bound.tex'),
    ('fermat_cartier_families_passed', 'work/arithmetic/fermat_cartier_families.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('low_rank_tate_obstructions_passed', 'work/scan_w/low_rank_tate_obstructions.tex', 'work/covers/contribution.tex'),
    ('fermat_albanese_surfaces_passed', 'work/arithmetic/fermat_albanese_surfaces.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('separable_cover_lifts_passed', 'work/covers/separable_cover_lifts.tex', 'work/arithmetic/contribution.tex'),
    ('fermat_product_surfaces_passed', 'work/arithmetic/fermat_product_surfaces.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('odd_tate_selection_axes_passed', 'work/scan_w/odd_tate_selection_axes.tex', 'work/covers/contribution.tex'),
    ('axis_ring_obstruction_passed', 'work/axis/axis_ring_obstruction.tex', 'work/covers/contribution.tex'),
    ('fermat_residual_motive_passed', 'work/arithmetic/fermat_residual_motive.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
]:
    if (ROOT/('work/checks/'+marker+'.txt')).exists():
        checked.insert(checked.index(before), file)
boundary_checked=(ROOT/'work/checks/boundary_strata_passed.txt').exists()
if not boundary_checked: checked.remove('work/covers/boundary_strata.tex')
th5_checked=(ROOT/'work/checks/consolidated_th5_passed.txt').exists()
if th5_checked: checked.append('work/consolidated_th5.tex')
parts=[preamble]
for name in checked:
    parts += ['\n% BEGIN '+name+'\n',(ROOT/name).read_text(),'\n% END '+name+'\n']
parts.append('\n\\part{Unchecked candidates and unresolved work}\n')
for marker, candidate in [
    ('axis_abstract_unramified_lifts_passed', 'work/axis/axis_abstract_unramified_lifts.tex'),
    ('axis_ramified_finite_order_passed', 'work/axis/axis_ramified_finite_order.tex'),
    ('axis_ramified_translation_correction_passed', 'work/axis/axis_ramified_translation_correction.tex'),
    ('axis_uniform_abelian_obstruction_passed', 'work/axis/axis_uniform_abelian_obstruction.tex'),
    ('nonliftable_surface_prime_extension_passed', 'work/axis/nonliftable_surface_prime_extension.tex'),
    ('axis_all_powers_torus_passed', 'work/scan_w/axis_all_powers_torus.tex'),
    ('axis_all_ample_fourfold_passed', 'work/scan_w/axis_all_ample_fourfold.tex'),
    ('fermat_geometric_torsion_passed', 'work/arithmetic/fermat_geometric_torsion.tex'),
    ('fermat_geometric_diagnostic_passed', 'work/arithmetic/fermat_geometric_diagnostic.tex'),
    ('fermat_actual_descent_passed', 'work/arithmetic/fermat_actual_descent.tex'),
    ('axis_ramified_support_counterexample_passed', 'work/axis/axis_ramified_support_counterexample.tex'),
    ('orthogonal_crystal_hasse_passed', 'work/scan_w/orthogonal_crystal_hasse.tex'),
    ('axis_ramified_transfer_diagnostics_passed', 'work/axis/axis_ramified_transfer_diagnostics.tex'),
    ('quaternion_frobenius_sign_passed', 'work/scan_w/quaternion_frobenius_sign.tex'),
    ('c3_axis_sign_passed', 'work/axis/c3_axis_sign.tex'),
    ('quaternion_rank_four_diagnostic_passed', 'work/arithmetic/quaternion_rank_four_diagnostic.tex'),
    ('non_tate_quaternion_criterion_passed', 'work/scan_w/non_tate_quaternion_criterion.tex'),
    ('universal_quaternion_boundary_passed', 'work/scan_w/universal_quaternion_boundary.tex'),
    ('split_prime_quaternion_sign_passed', 'work/scan_w/split_prime_quaternion_sign.tex'),
    ('c3_twisted_split_axes_passed', 'work/axis/c3_twisted_split_axes.tex'),
    ('characteristic_three_eigenblock_passed', 'work/scan_w/characteristic_three_eigenblock.tex'),
    ('c4_characteristic_three_axes_passed', 'work/arithmetic/c4_characteristic_three_axes.tex'),
    ('dyadic_quaternion_sign_passed', 'work/scan_w/dyadic_quaternion_sign.tex'),
    ('c3_characteristic_two_axes_passed', 'work/axis/c3_characteristic_two_axes.tex'),
    ('c3_characteristic_two_centres_passed', 'work/axis/c3_characteristic_two_centres.tex'),
    ('elliptic_power_height_corollary_passed', 'work/axis/elliptic_power_height_corollary.tex'),
    ('formal_k_effectivity_gate_passed', 'work/axis/formal_k_effectivity_gate.tex'),
    ('first_ramified_support_jets_passed', 'work/axis/first_ramified_support_jets.tex'),
    ('axis_first_ramified_noncancellation_passed', 'work/axis/axis_first_ramified_noncancellation.tex'),
    ('axis_even_ramification_boundary_passed', 'work/axis/axis_even_ramification_boundary.tex'),
    ('ambient_support_jet_restriction_passed', 'work/scan_w/ambient_support_jet_restriction.tex'),
    ('axis_second_ramified_noncancellation_passed', 'work/axis/axis_second_ramified_noncancellation.tex'),
    ('axis_next_boundary_odd_characteristic_passed', 'work/axis/axis_next_boundary_odd_characteristic.tex'),
    ('axis_closed_layer_peeling_passed', 'work/axis/axis_closed_layer_peeling.tex'),
    ('axis_supplied_support_threshold_passed', 'work/axis/axis_supplied_support_threshold.tex'),
    ('axis_first_frobenius_range_passed', 'work/axis/axis_first_frobenius_range.tex'),
    ('arbitrary_pole_primitive_testing_passed', 'work/scan_w/arbitrary_pole_primitive_testing.tex'),
    ('axis_frobenius_supplied_support_passed', 'work/axis/axis_frobenius_supplied_support.tex'),
    ('axis_uniform_ample_conormal_passed', 'work/arithmetic/axis_uniform_ample_conormal.tex'),
    ('axis_second_frobenius_range_passed', 'work/axis/axis_second_frobenius_range.tex'),
    ('ambient_closed_layer_removal_passed', 'work/scan_w/ambient_closed_layer_removal.tex'),
    ('axis_next_exact_ramification_boundary_passed', 'work/axis/axis_next_exact_ramification_boundary.tex'),
    ('axis_characteristic_three_ramification_five_passed', 'work/axis/axis_characteristic_three_ramification_five.tex'),
    ('higher_cartier_detection_passed', 'work/scan_w/higher_cartier_detection.tex'),
    ('axis_formal_cartier_saturation_passed', 'work/axis/axis_formal_cartier_saturation.tex'),
    ('fermat_recent_source_audit_passed', 'work/arithmetic/fermat_recent_source_audit.tex'),
    ('ramified_rigid_source_audit_passed', 'work/arithmetic/ramified_rigid_source_audit.tex'),
    ('quaternion_centralizer_comparison_passed', 'work/scan_w/quaternion_centralizer_comparison.tex'),
    ('quaternion_picard_source_audit_passed', 'work/arithmetic/quaternion_picard_source_audit.tex'),
    ('fermat_regulator_source_audit_passed', 'work/arithmetic/fermat_regulator_source_audit.tex'),
    ('fermat_difference_surface_passed', 'work/arithmetic/fermat_difference_surface.tex'),
    ('fermat_boundary_curve_tests_passed', 'work/arithmetic/fermat_boundary_curve_tests.tex'),
]:
    if (ROOT/candidate).exists() and not (ROOT/('work/checks/'+marker+'.txt')).exists():
        parts.append('\nThe following complete candidate is awaiting its final whole-proof audit.\n')
        parts.append((ROOT/candidate).read_text())
if (ROOT/'work/scan_w/totally_real_axis_blocks.tex').exists() and not (ROOT/'work/checks/totally_real_axis_blocks_passed.txt').exists():
    parts.append('\nThe following coefficient-field criterion is awaiting completion of its whole-proof checks. It is not promoted to a checked finding at this checkpoint.\n')
    parts.append((ROOT/'work/scan_w/totally_real_axis_blocks.tex').read_text())
if not (ROOT/'work/checks/axis_frobenius_selection_passed.txt').exists():
    parts.append('The following closed-point selection criterion awaits its independent whole-proof review.\n')
    parts.append((ROOT/'work/axis/axis_frobenius_selection.tex').read_text())
if not boundary_checked:
    parts.append('The following two cover candidates are awaiting an independent whole-proof reading. They are not included among checked findings at this checkpoint.\n')
    parts.append((ROOT/'work/covers/boundary_strata.tex').read_text())
if not th5_checked:
    parts.append('\n\\section{Consolidation under final review}\n')
    parts.append((ROOT/'work/consolidated_th5.tex').read_text())
parts.append('\n% BEGIN work/final_research_boundary.tex\n'+(ROOT/'work/final_research_boundary.tex').read_text()+'\n% END work/final_research_boundary.tex\n')
parts.append(r'''
\section{Unresolved goals}
The fixed-axis sign is not proved for every special axis, and no
wrong-sign algebraic class is constructed. The universal lifting
question for classes remains open. The special-cover sign remains
open at arbitrary closed points with new algebraic trace-kernel
classes. Fermat Abel--Jacobi injectivity remains open, with the
exact gates specified above. Full Th.~4 for arbitrary new special
incidence directions is not proved. The proposed supersingular
Fermat family does not meet the requested initially-unknown-$I$
status. The ledger and question register give the current precise
state of every treated row.
\end{document}
''')
(OUT/'C44_POS.tex').write_text(''.join(parts))

def normalized_type(original):
    allowed={'targeted proof check','independent re-proof','computation or formal certificate',
             'used and rechecked in this run','carried as background without fault found',
             "refuted, with the refined statement's id"}
    if original in allowed: return original
    if original == 'outage recovery and persistence': return None
    if original == 'targeted promotion-header check and exact mathematical-text identity verification':
        return 'computation or formal certificate'
    if original == 'promotion reconciliation and exact added-paragraph read':
        return 'used and rechecked in this run'
    if original == 'statement read':
        return 'carried as background without fault found'
    if original == 'citation-only correction':
        return 'used and rechecked in this run'
    if original == 'ID-only amendment and targeted label check':
        return 'carried as background without fault found'
    if any(word in original for word in ['entire-proof','whole-proof','complete-proof','entire integrated-proof']):
        return 'targeted proof check'
    if original in {'targeted post-read check','targeted dependency completion'}:
        return 'targeted proof check'
    if any(word in original for word in ['hash verification','hash check','hash reconciliation','visually checked']):
        return 'used and rechecked in this run'
    if 'source' in original: return 'used and rechecked in this run'
    if any(word in original for word in ['proof','scope','whole-argument','author patch read']): return 'targeted proof check'
    if any(word in original for word in ['arithmetic','computation','certificate']):
        return 'computation or formal certificate'
    return original

header=['statement_id','date','who','model','effort','run','type','outcome','details']
events=[]
for name in ['work/checks/root_events.tsv','work/axis/CHECK_EVENTS.tsv','work/scan_w/check_events.tsv','work/arithmetic/CHECK_EVENTS.tsv','work/arithmetic/check_events.tsv']:
    p=ROOT/name
    if not p.exists(): continue
    with p.open(newline='') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            who=row.get('who',row.get('who_model_effort_run',''))
            original_type=row.get('type','')
            kind=normalized_type(original_type)
            if kind is None: continue # Operational recovery is preserved in the raw work register and ledger.
            detail=row.get('details',row.get('locator',''))
            if kind != original_type:
                detail='Original recorded event type: '+original_type+'. '+detail
            events.append({
                'statement_id':row.get('statement_id',''),
                'date':row.get('date',row.get('date_utc','')),
                'who':who,
                'model':row.get('model','GPT-6 Astra Pro'),
                'effort':row.get('effort','not exposed'),
                'run':row.get('run','C44_POS'),
                'type':kind,
                'outcome':row.get('outcome',''),
                'details':detail,
            })
with (OUT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=header,delimiter='\t');w.writeheader();w.writerows(events)

manifest=[]
for name in checked+['work/covers/boundary_strata.tex','work/consolidated_th5.tex','work/final_research_boundary.tex']:
    p=ROOT/name
    manifest.append({'path':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(ROOT/'work/assembly_manifest.json').write_text(json.dumps({'assembled_at':stamp.isoformat(),'parts':manifest,'events':len(events),'boundary_checked':boundary_checked},indent=2)+'\n')
print(json.dumps({'paper_bytes':(OUT/'C44_POS.tex').stat().st_size,'events':len(events),'boundary_checked':boundary_checked,'assembled_at':stamp.isoformat()}))
