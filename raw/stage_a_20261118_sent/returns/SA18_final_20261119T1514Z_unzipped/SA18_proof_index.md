# Proof and computation index

These are the actual programs and outputs used to check the source statements. Finite calculations certify their stated cases; the universal arguments are in the proof records. A reference match, source-alignment check, independent proof and counterexample are distinguished in CHECK_EVENTS.tsv.

## Mathematical proof records

### research/root_proofs.md

[Read the proof record](research/root_proofs.md)

- R1. Correspondences, actions, associativity and units
- R2. Products of diagonal classes
- R3. The reused configuration typescript
- R4. Integral quadric intersections and punctured cones
- R5. Affine quadrics and monodromy
- R6. Nested tori and the missing maximality hypothesis
- R7. A smooth G_m-to-G_a family
- R8. Delzant's augmentation filtration and degree-two symbol
- R9. The abstract Lemma A on ringed spaces
- R10. Cote55's torus and dimension counterexamples
- R11. A direct negative answer to the coherent-ring elimination question

### parts/agent16/source_review.md

[Read the proof record](parts/agent16/source_review.md)

- Coverage and source discipline
- What the four cotes contain
- The operator algebra: two models that must remain distinct
- Standard conjectures and the limits of later solutions
- Brauer text: a published gap is still a gap
- Fourier transform: precise later theorems and precise surviving errors
- De Rham reconstruction and intermediate Jacobians
- Auxiliary findings and attribution limits
- Research audit, project links and integration
- Final manual source-status audit, 19 November 2026

### parts/agent16/root_independent_audit.md

[Read the proof record](parts/agent16/root_independent_audit.md)

- Scope and result
- Changes recommended to the parent
- Independently confirmed mathematical checks
- Merge decisions
- Audit evidence

### parts/agent45/source_review.md

[Read the proof record](parts/agent45/source_review.md)

- What these folders contain
- The earlier notes: what survives and what must be kept apart
- Results that sharpen the dossier
- Search, attribution and verification limits
- Integration notes

### parts/agent46/proofs.md

[Read the proof record](parts/agent46/proofs.md)

- 1. Rigidified torsors
- 2. The Lang map, quotient, and finiteness boundary
- 3. Frobenius-fixed modules and local systems
- 4. Frobenius formularium and ideal powers
- 5. A homeomorphism onto a closed subset is affine
- 6. Units, Pic[p], and logarithmic differentials
- 7. Restricted p-power and height-one duality
- 8. Verschiebung and symmetric tensors
- 9. Uniform structures on a reused sheet
- 10. Étale Frobenius and the gluing fragments
- 11. Brauer–Severi geometry, Picard, and linear systems
- 12. Coxeter and graph calculations on reused pages
- 13. Divisible modules over a PID
- 14. p-adic cosets and Haar measure
- 15. Pro-groups
- 16. Relative effective Cartier divisors
- 17. Matrix bundles and topological Brauer groups
- 18. Projective representations and multipliers
- 19. Restriction of scalars and inseparable norms
- 20. Hilbert90, averaging, and twisting
- 21. Cyclic cohomology and the corrected twisted norm
- 22. Semilocal descent, invariant rings, and Sylow detection
- 23. The quotient counterexample attempt
- 24. Components and images of group schemes
- 25. Geometric properties and missing qualifiers
- 26. Étale dictionaries and the component-space boundary
- 27. Characters and finite Cartier duality
- 28. Monoids, GL_n, and the cancellative side remark
- 29. The full distribution functor and Hopf identities
- 30. Actions, coactions, submodules, and intersections
- 31. Finite coefficient spaces and affine approximation
- 32. V(M), W(M), and endomorphism functors

## Executed calculations

### Root exact certificates

[Program](scripts/root_certificates.py) · [Actual output](outputs/root_certificates.json)

Named output sections; see each section for its exact mathematical scope.

- `P1_diagonals`
- `nested_tori`
- `quadrics`
- `quadric_middle_lattice`
- `quadric_Q0`
- `Gm_Ga_group_law`
- `SW_rankzero_product`
- `real_signature_binary_check`
- `RP2_LemmaA_counterexample`
- `literal_torus`
- `alternative_torus`
- `Clifford_normalization_alarm`
- `sorted_cone`
- `separation_missing_nonzero`

### Root supplemental certificates

[Program](scripts/root_extra_certificates.py) · [Actual output](outputs/root_extra_certificates.json)

Named output sections; see each section for its exact mathematical scope.

- `GIT_chart_inverse`
- `coherent_elimination`
- `continuous_image_dimension`

### Cotes16/47/54/44 exact certificates

[Program](parts/agent16/scripts/computations.py) · [Actual output](parts/agent16/outputs/computations.json)

Named output sections; see each section for its exact mathematical scope.

- `exterior_rank2`
- `exterior_rank4`
- `exterior_rank6`
- `exterior_rank8`
- `exterior_rank10`
- `forget_grading`
- `normalized_strings_n1`
- `normalized_strings_n2`
- `normalized_strings_n3`
- `normalized_strings_n4`
- `normalized_strings_n5`
- `scan17_wrong_projector`
- `scan53_projective_plane`
- `same_top_power_not_lefschetz`
- `discriminant_pairing`
- `F2_cube`
- `different_tower`
- `chern_coefficients`
- `elliptic_product`
- `koszul_fibre`
- `hodge_associativity`
- `six_dimensional_model`
- `cyclic_family_m1`
- `cyclic_family_m2`
- `cyclic_family_m3`
- `cyclic_family_m4`
- `cayley_hamilton_inverse`
- `root_torus_check`

### Cotes16/47/54/44 status supplements

[Program](parts/agent16/scripts/status_certificates.py) · [Actual output](parts/agent16/outputs/status_certificates.json)

Named output sections; see each section for its exact mathematical scope.

- `normalized_phi_square_class`
- `raw_exterior_string_order_mod2`
- `elliptic_fourier_literal_product`

### Independent checks of root reconstructions

[Program](parts/agent16/scripts/root_counterexample.py) · [Actual output](parts/agent16/outputs/root_counterexample.json)

Named output sections; see each section for its exact mathematical scope.

- `roots`
- `lattice`
- `all_reflections_permute_roots`
- `reduced`
- `dual_invariant_form`
- `root`
- `coroot`
- `pairing_with_e1_plus_e2`
- `conclusion`

### Cotes45/48–52 algebraic certificates

[Program](parts/agent45/scripts/math_checks.py) · [Actual output](parts/agent45/outputs/math_checks.json)

Named output sections; see each section for its exact mathematical scope.

- `pgl2_F2`
- `sl2_F2`
- `pgl2_counterexample`
- `V4_into_S4_H1_R`
- `quadratic_tensor_obstruction`
- `same_polar_different_quadratic`
- `dual_numbers`
- `ordered_ray_determinant`
- `exterior_gram_determinant`
- `Dist_Gm_product`
- `hermitian_sign`
- `Rosati_not_integral`
- `characteristic_coefficients`
- `hyperelliptic_multiplication`
- `hyperelliptic_reason`
- `alpha_p_moving_lines`
- `nonample_isogeny`
- `perfect_not_centerless`
- `rank_one_torus_isomorphisms`
- `contraction_nonuniqueness`

### Cote45 exterior identities

[Program](parts/agent45/scripts/exterior_checks.py) · [Actual output](parts/agent45/outputs/exterior_checks.json)

Named output sections; see each section for its exact mathematical scope.

- `integer_basis_checks`
- `equation32_symbolic_checks`
- `minors_symbolic_checks`
- `all_failures`
- `universal_proof`
- `scope`

### Cotes46/53 exact checks

[Program](parts/agent46/scripts/checks.py) · [Actual output](parts/agent46/outputs/computations.json)

Reported checks: 65; all_passed=True.

- `rigidified_S3`
- `free_word_twisting`
- `frobenius_fixed_basis`
- `perfect_valuation_chain`
- `frobenius_ideal`
- `freshman_dream`
- `frobenius_ring_formulas`
- `nonflat_frobenius`
- `transition_cocycle_p`
- `homogeneous_degrees`
- `semilinear_scalar`
- `finite_field_F4_iterate`
- `frobenius_neighbourhood_lengths`
- `dlog_p_power`
- `restricted_derivations`
- `symmetric_orbits`
- `FV_Ga_Gm_alpha`
- `finite_uniformity_axiom`
- `coxeter_free_word_rotation`
- `Sn_generators`
- `forests`
- `central_cocycle_additivity`
- `Veronese_relation`
- `padic_cosets`
- `symmetric_scalar_weight`
- `symmetric_pairing_char2`
- `brauer_degree_obstruction`
- `matrix_opposite_action`
- `pauli_blocks`
- `determinant_multiplier`
- `inseparable_norm`
- `local_invariant_kernel`
- `cocycle_averaging`
- `determinant_polynomial`
- `twisted_norm_freewords`
- `quotient_norm_correction`
- `cyclic_cocycle`
- `C5_twist_pointwise`
- `semilocal_laurent_cocycle`
- `square_zero_units`
- `dual_number_invariants`
- `sylow_transfer`
- `PGL_stabilizer_dimensions`
- `free_word_action_inverse`
- `additive_translation_zero`
- `dual_numbers_nonsmooth`
- `inseparable_group_factorization`
- `disconnected_X_counterexample`
- `real_cone_factorization`
- `inseparable_tensor_nilpotent`
- `separable_tensor_split`
- `connected_quantifier_counterexample`
- `alpha_p_duality`
- `finite_Hopf_duality`
- `counit_nonzero`
- `two_point_monoid`
- `two_point_bialgebra`
- `matrix_coefficients`
- `finite_dual_tensor`
- `group_algebra_C3`
- `primitive_derivation`
- `coaction_associativity`
- `tensor_noninjectivity`
- `flat_tensor_intersection_boundary`
- `matrix_inverse_hopf`

## Reproducibility boundary

The programs and outputs are retained exactly as research evidence. Root integration scripts expect the original extracted attachment in the sibling sources directory. Some source-owner acquisition scripts preserve the original run paths; their saved outputs and manifests identify what was actually read. Re-running a search later is not guaranteed to return the same web content. External PDFs and the user attachment are deliberately excluded from this archive.
