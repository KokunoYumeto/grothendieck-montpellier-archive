# Program and output index

All source programs are listed below. Contributor programs and their outputs also have byte-identical copies under `code/retained_programs/`; use the original locations in the table for execution so that relative input and output paths retain their documented meaning. Root programs already reside in `code/`.

Exact finite certificates establish only the scope stated in each program and its mathematical proof. Retrieval and layout scripts supply provenance and verification, not mathematical theorems. Instrumented durations are in the original outputs or `code/computation_timing_output.json`; the full timing-run stdout is retained. A still-running retrieval has no completed result and is not evidence of inspection.

| Executable source location | Stated scope |
|---|---|
| `code/assemble.py` | Assemble independently maintained fragments; no mathematical inference. |
| `code/build_paper.py` | Build the LuaLaTeX manuscript and record exact layout diagnostics. |
| `code/build_registers.py` | Assemble auditable research registers from the proof owners' records. |
| `code/catalog_programs.py` | Collect all contributed programs and exact outputs into the code deliverable. |
| `code/check_cubic_surface_line_cup.py` | Exact polynomial and rank checks for the cubic-line cup-product research note. |
| `code/check_dimension_six_incidence.py` | Exact algebra in C.3ag; no computational assertion about generic Hodge groups. |
| `code/check_fermat_boundary.py` | Exact finite certificates for the C.3r Fermat-join construction. |
| `code/check_local_cone.py` | Exact equation checks for C.3f; this does not certify Chow non-torsion. |
| `code/check_ordinary_divisor_quotient.py` | Exact finite certificates for C.3v; the geometric proof is separate. |
| `code/check_quartic_obstruction_independent.py` | Independently certify a nonzero maximal minor of the C.3ae matrix. |
| `code/check_quaternion_crystal.py` | Exact algebra certificates for SA06; no floating-point arithmetic. |
| `code/check_registers.py` | Check proof/register/check-event coverage, recording late separate fragments. |
| `code/check_segre_nonvanishing.py` | Finite symbolic checks for C.3s; no computed assertion of Chow non-torsion. |
| `code/check_small_automorphisms.py` | Enumerate automorphisms of y^2+y=x^3/F4 and y^2=x^3-x/F9. |
| `code/check_supersingular.py` | Exhaustive finite-field checks for SA06 A.1/A.8; pure Python. |
| `code/fetch_algebraization_sources.py` | Retain primary sources for the completion-algebraization transfer in C.3z. |
| `code/fetch_bloch_gdz.py` | Retrieve publicly indexed GDZ source evidence; no mathematical inference. |
| `code/fetch_bloch_gdz_article.py` | Download the article identified by the official volume METS record. |
| `code/fetch_fermat_boundary_sources.py` | Fetch primary mathematical sources for the C.3r proof and record provenance. |
| `code/fetch_levine1986_supported_k.py` | Acquire and render Levine's 1986 primary supported-K-theory sequences. |
| `code/fetch_milne_jacobian_sign.py` | Retain the exact official source and render the autoduality sign page. |
| `code/fetch_modulus_route_sources.py` | Acquire exact primary modulus-route PDFs and retain input/output timings. |
| `code/fetch_montpellier_cote14.py` | Retrieve the official cote14 PDF with verified byte ranges. |
| `code/fetch_montpellier_cote15.py` | Retrieve the official dossier to inspect the unfinished question on scan70. |
| `code/fetch_montpellier_ranges.py` | Retrieve the official cote 15 scan using verified HTTP byte ranges. |
| `code/fetch_motive_route_sources.py` | Retain motive-route primary versions and timings; no theorem check. |
| `code/fetch_proper_parameter_sources.py` | Retain three primary-source acquisitions and exact timings; no theorem check. |
| `code/fetch_proper_parameter_sources_requests_failed.py` | Retain three primary-source acquisitions and exact timings; no theorem check. |
| `code/fetch_sga6_specialization_pages.py` | Acquire original page scans and OCR a bounded SGA6 specialization range. |
| `code/finalize_research_record.py` | Mark the manuscript as a final incomplete record after a verified stop review. |
| `code/find_pdf_statement_pages.py` | Locate requested visible statement headings in the current PDF for visual QA. |
| `code/inspect_montpellier_cote15.py` | Render selected official manuscript scans for direct visual verification. |
| `code/normalize_check_events.py` | Conservative aggregate metadata normalization; original owner logs are untouched. |
| `code/ocr_bloch1976.py` | OCR the retrieved primary scan for locating passages; verify formulas visually. |
| `code/package_work.py` | Create a new immutable checkpoint/final ZIP with a SHA256 file register. |
| `code/probe_montpellier_archive.py` | Inspect the official public archive index for the cited dossier's scan URL. |
| `code/probe_montpellier_range.py` | Check byte-range support for targeted inspection of an official scan. |
| `code/record_computation_timings.py` | Supply missing wall-clock timings for the existing exact certificates. |
| `code/record_event_metadata_overrides.py` | Retain root's explicit eight-row supplement to the metadata audit. |
| `code/record_scheduled_review.py` | Record one due mathematical review, rejecting early or duplicate records. |
| `code/refine_checkpoint14_scope.py` | Apply the audited semilocal C.3be refinement to the main report register. |
| `code/render_qa.py` | Render named PDF pages and contact sheets for manual visual inspection. |
| `code/restore_tex_maps.py` | Restore a local PDF font map from installed AMS and RSFS Type1 font maps. |
| `code/update_checkpoint14_scope.py` | Update the master summaries for the independently audited C.3bd/be results. |
| `code/verify_deliverable_archive.py` | Verify an immutable archive against its manifest and required deliverables. |
| `code/verify_program_catalog.py` | Verify every original and consolidated program/output catalog checksum. |
| `agents/cycles/code/build_filtration_metadata.py` | Reproduce the exact Saito/Walker-generation refinement and source-audit ledger. |
| `agents/cycles/code/build_metadata.py` | Write reproducible research ledgers for the cycles agent's actual checks. |
| `agents/cycles/code/build_morphic_metadata.py` | Register the audited E.3s--u results and supersede current open-gate prose. |
| `agents/cycles/code/check_absolute_picard_kernel.py` | Finite algebraic checks for C.3ao, rerun after scratch loss. |
| `agents/cycles/code/check_blowup_positivity.py` | Exact finite sign, degree, and exceptional-relation certificates for C.1q. |
| `agents/cycles/code/check_critical_injectivity.py` | Exact defining-data certificate for C.3am; fresh rerun after scratch recovery. |
| `agents/cycles/code/check_cubic_exceptional_lattices.py` | Exact integral Chow-lattice certificates; not a finite proof of cycle existence. |
| `agents/cycles/code/check_cubic_exceptional_lattices_initial_145931.py` | Exact integral Chow-lattice certificates; not a finite proof of cycle existence. |
| `agents/cycles/code/check_cycles.py` | Finite checks for cycle-audit examples; no claims about Chow groups are tested. |
| `agents/cycles/code/check_edge_triple_correction.py` | Bounded exact checks for ET; no descent or geometric theorem is certified. |
| `agents/cycles/code/check_endpoint_image.py` | Record exact degree identities and the C.1n proof/source audit. |
| `agents/cycles/code/check_explicit_walker.py` | Finite data checks and reproducible ledger for the generic Walker example. |
| `agents/cycles/code/check_fermat_quintic_top.py` | Exact finite algebra behind the restricted Fermat-quintic argument. |
| `agents/cycles/code/check_henselian_branch_countermodel.py` | Finite identities only for the Artin--Schreier branch countermodel. |
| `agents/cycles/code/check_higher_local_geometry.py` | Finite symbolic checks accompanying the proved C.3ae geometry. |
| `agents/cycles/code/check_integral_divisor_table.py` | Exact polynomial checks for C.3bh; the Picard and universal proofs are separate. |
| `agents/cycles/code/check_morphic_counterexample.py` | Finite algebraic certificates for the specified E.3u construction. |
| `agents/cycles/code/check_nori_counterexamples.py` | Finite certificates accompanying C.1i; the general theorem is proved in TeX. |
| `agents/cycles/code/check_partial_fourier_parity.py` | Exact exterior-algebra checks for the proposed C4 correspondence test. |
| `agents/cycles/code/check_positivity_stabilization.py` | Exact finite sign, degree and SL2-string checks for C.1o--p. |
| `agents/cycles/code/check_quartic_column_pairs.py` | Check pairwise independent columns for the certified C.3ae matrices. |
| `agents/cycles/code/check_quartic_sections_basepoints.py` | Certify the selected four bilinear sections have no projective base point. |
| `agents/cycles/code/check_quintic_lines.py` | Exact finite certificates for C.1g; no numerical period approximation. |
| `agents/cycles/code/check_regular_ambient_calabi_yau.py` | Finite defining-data checks for C.3ah; not a Chow nonvanishing proof. |
| `agents/cycles/code/check_suspended_calabi_yau.py` | Exact finite defining-data certificate for the all-dimensional C.3ai proof. |
| `agents/cycles/code/check_unconditional_edge_kernel.py` | Bounded exact algebra for C.3bt; it does not certify descent or proper families. |
| `agents/cycles/code/compare_main_rows_review15_exact.py` | See program and accompanying report. |
| `agents/cycles/code/compile_all_degree_local.py` | Retain the complete four-pass standalone C.3af typesetting check. |
| `agents/cycles/code/compile_blowup_lowdegree.py` | Retain the complete four-pass standalone C.1q/C.2k typesetting check. |
| `agents/cycles/code/compile_dimension_six.py` | Retain the complete four-pass standalone C.3ag typesetting check. |
| `agents/cycles/code/compile_edge_triple_correction.py` | Retained four-stage standalone C.3bq typography verification. |
| `agents/cycles/code/compile_endpoint_image.py` | Compile the new C.1n fragment; preserve command output and diagnostics. |
| `agents/cycles/code/compile_exceptional_cubic_lattice.py` | Retained standalone typesetting check for the auxiliary integral Chow lemma. |
| `agents/cycles/code/compile_fermat_quintic_top.py` | See program and accompanying report. |
| `agents/cycles/code/compile_finite_field.py` | Retain the complete four-pass standalone C.3ac typesetting check. |
| `agents/cycles/code/compile_higher_local.py` | Retain the complete four-pass standalone C.3ae typesetting check. |
| `agents/cycles/code/compile_integral_divisor_table.py` | Retained standalone four-stage C.3bh typesetting check. |
| `agents/cycles/code/compile_local_surjectivity_classification.py` | Retained standalone C.3ak check; no external bibliography is cited. |
| `agents/cycles/code/compile_morphic.py` | Compile the independently audited E.3s--u fragments and retain diagnostics. |
| `agents/cycles/code/compile_partial_fourier.py` | See program and accompanying report. |
| `agents/cycles/code/compile_positivity_stabilization.py` | Compile C.1o--p once through the necessary bibliography passes. |
| `agents/cycles/code/compile_product_curve_top.py` | See program and accompanying report. |
| `agents/cycles/code/compile_recovered_injectivity.py` | Fresh four-pass wrappers for the reconstructed al/am/ao/ap proofs. |
| `agents/cycles/code/compile_regular_ambient_calabi_yau.py` | Four-pass standalone C.3ah typesetting check with retained logs. |
| `agents/cycles/code/compile_supported_K1_family.py` | Retained four-stage standalone supported higher-family typography verification. |
| `agents/cycles/code/compile_suspended_calabi_yau.py` | Retained four-pass C.3ai wrapper build. |
| `agents/cycles/code/compile_unconditional_edge_kernel.py` | Retained four-stage standalone C.3bt typography verification. |
| `agents/cycles/code/fetch_bigonal_source.py` | Retain the primary bigonal source and actual download timing. |
| `agents/cycles/code/fetch_explicit_walker_sources.py` | Preserve primary inputs for the generic Ottem--Suzuki counterexample. |
| `agents/cycles/code/fetch_fermat_quintic_sources.py` | See program and accompanying report. |
| `agents/cycles/code/fetch_filtration_sources.py` | Preserve primary PDFs opened for the late cycle/parameter-space audit. |
| `agents/cycles/code/fetch_generation_gate_sources.py` | Fetch exact primary sources explored for the remaining E.3 generation gate. |
| `agents/cycles/code/fetch_injectivity_sources.py` | Recover the five primary PDFs; retain fresh download runtimes and hashes. |
| `agents/cycles/code/fetch_k2_cohomology_sources.py` | See program and accompanying report. |
| `agents/cycles/code/fetch_late_sources.py` | Preserve primary PDFs opened for the late cycle/parameter-space audit. |
| `agents/cycles/code/fetch_morphic_walker_sources.py` | Preserve the primary sources used in the morphic-AJ obstruction audit. |
| `agents/cycles/code/fetch_one_motivic_sources.py` | Retrieve opened primary sources for the one-motivic quotient audit. |
| `agents/cycles/code/fetch_partial_fourier_sources.py` | See program and accompanying report. |
| `agents/cycles/code/fetch_product_curve_sources.py` | See program and accompanying report. |
| `agents/cycles/code/fetch_samuel_source.py` | Obtain Samuel's original ICM paper from the official proceedings. |
| `agents/cycles/code/fetch_soule1984.py` | Retrieve the public GDZ article identified in its volume METS record. |
| `agents/cycles/code/fetch_torsion_lifting_sources.py` | Fetch exact primary PDFs used in the local torsion-lifting source audit. |
| `agents/cycles/code/fetch_walker_sources.py` | Preserve the three primary PDFs opened for E.3g--i, with exact fetch outcomes. |
| `agents/cycles/code/fetch_weil_sources_1323.py` | See program and accompanying report. |
| `agents/cycles/code/ocr_soule1984.py` | Create a navigational OCR; decisive equations are checked on page images. |
| `agents/cycles/code/record_generation_audits.py` | Record source audits and retained failed approaches; no new closure row. |
| `agents/cycles/code/register_all_degree_local.py` | Register the audited product-K3 local restriction construction. |
| `agents/cycles/code/register_edge_triple_correction.py` | Register the fully audited restricted C.3bq theorem without changing master files. |
| `agents/cycles/code/register_fermat_quintic.py` | Register actual C.3au proof/source/build checks after independent review. |
| `agents/cycles/code/register_finite_field.py` | Register the separately qualified finite-field theorem and actual checks. |
| `agents/cycles/code/register_higher_local.py` | Register the audited ordinary codimension-two local counterexample. |
| `agents/cycles/code/register_local_surjectivity_classification.py` | Record the exact, independently checked C.3ak range partition. |
| `agents/cycles/code/register_partial_fourier.py` | See program and accompanying report. |
| `agents/cycles/code/register_product_curve_top.py` | See program and accompanying report. |
| `agents/cycles/code/register_recovered_injectivity.py` | Restore al/am/ao/ap statement and actual-check records after scratch loss. |
| `agents/cycles/code/register_regular_ambient_calabi_yau.py` | Register C.3ah after the root proof pass; retain actual checks. |
| `agents/cycles/code/register_suspended_calabi_yau.py` | Record the audited low-dimensional suspended Calabi–Yau theorem. |
| `agents/cycles/code/render_generation_sources.py` | Render exact source pages used in the remaining generation-gate audit. |
| `agents/cycles/code/render_saito_pages.py` | See program and accompanying report. |
| `agents/cycles/code/run_main_rows_preservation.py` | One scoped timed rerun of the preserved comparison; owned outputs only. |
| `agents/cycles/code/test_quartic_obstruction_rank.py` | Exact finite-field rank witness for the four-section obstruction matrix. |
| `agents/cycles/code/update_status_0550.py` | Update the dated cycles status after the exact Saito comparison. |
| `agents/cycles/code/update_status_0617.py` | Update own status and route ledger after the endpoint-image reduction. |
| `agents/cycles/code/update_status_0710.py` | Publish the current E.3 closure and retain dated earlier attempts. |
| `agents/cycles/code/update_status_recovery.py` | Update the current gate summary and recovery provenance without changing old checkpoints. |
| `agents/cycles/code/write_main_rows_receipt_original.py` | See program and accompanying report. |
| `agents/frobenius/code/acquire_C3bg_sources.py` | Reproduce the primary downloads used in C.3bg; each execution records fresh timing/hash. |
| `agents/frobenius/code/acquire_CJS_source.py` | Acquire the exact CJS author version used in C.3bd. |
| `agents/frobenius/code/acquire_N6_Hodge_sources.py` | See program and accompanying report. |
| `agents/frobenius/code/acquire_SNC_top_sources.py` | Retain the freshly opened SNC/top-Chow primary sources, with true timings. |
| `agents/frobenius/code/acquire_charzero_lifting_sources.py` | Retain exact primary-source download attempts for the finite-jet audit. |
| `agents/frobenius/code/acquire_residual_and_K2_sources.py` | Fresh recovery downloads; retain measured times, URLs and hashes. |
| `agents/frobenius/code/acquire_resolution_sources.py` | Acquire exact low-dimensional resolution sources with truthful metadata. |
| `agents/frobenius/code/acquire_surface_reduction_Fpbar_sources.py` | Retain newly opened C.3be primary sources, with actual hashes and runtimes. |
| `agents/frobenius/code/acquire_yu_hb_sources.py` | Reproduce the primary-source acquisition for C.4x. |
| `agents/frobenius/code/audit_quartic_certificates.py` | Independent exact checks of the cycles agent's selected four sections. |
| `agents/frobenius/code/audit_quartic_column_pairs.py` | Independent lexicographic check of the compressed C.3af section data. |
| `agents/frobenius/code/build_SNC_Albanese_matrix.py` | Build the proposed weighted Albanese matrix auxiliary. |
| `agents/frobenius/code/build_SNC_Fpbar.py` | Compile the owned standalone C.3bc proof and retain actual execution metadata. |
| `agents/frobenius/code/build_SNC_mixed_Albanese.py` | Build final C.3bp, the mixed-dimensional Albanese reduction. |
| `agents/frobenius/code/build_SNC_nonzero_period_combined.py` | Build the two audited, unregistered SNC nonzero-period research lemmas NP.1--9. |
| `agents/frobenius/code/build_SNC_nonzero_period_model.py` | Build the unregistered direct SNC nonzero-period research construction. |
| `agents/frobenius/code/build_lowdim_Fpbar.py` | Compile the owned standalone C.3bd proof and retain actual execution metadata. |
| `agents/frobenius/code/build_normal_base_K1_family.py` | Build only the normal-base whole K1-family auxiliary. |
| `agents/frobenius/code/build_primitive_exceptional.py` | Build the separate primitive exceptional-boundary auxiliary, not the master. |
| `agents/frobenius/code/build_relative_Milnor.py` | Compile the auxiliary relative Milnor proof; retain actual run details. |
| `agents/frobenius/code/build_surface_reduction_Fpbar.py` | Compile C.3be; retain exact commands, elapsed times, and all pass output. |
| `agents/frobenius/code/build_tetrahedral_auxiliary.py` | Build only the two unregistered negative-K/tetrahedral auxiliaries. |
| `agents/frobenius/code/build_uniform_integral_picard.py` | Compile C.3bg; retain exact commands, elapsed times, and all pass output. |
| `agents/frobenius/code/build_whole_proper_top_family.py` | Build only the whole proper top-family auxiliary. |
| `agents/frobenius/code/check_BT1_word_reversal.py` | See program and accompanying report. |
| `agents/frobenius/code/check_C3an_geometry.py` | Reconstructed six-check certificate; formulas, not finite tests, prove C.3an. |
| `agents/frobenius/code/check_SNC_Albanese_matrix.py` | Exact symbolic check of the two-vertex weighted matrix identity. |
| `agents/frobenius/code/check_SNC_energy_identity.py` | Exact local expansion and product-cycle degree-map check; no geometric extrapolation. |
| `agents/frobenius/code/check_SNC_nonzero_period_model.py` | Bounded exact algebra supporting NP.1--8; not a test of genericity or Chow classes. |
| `agents/frobenius/code/check_correlated_even_level.py` | Test a necessary mod-4 graph congruence at level 2 modulo 4. |
| `agents/frobenius/code/check_correlated_graph_identity.py` | Exact finite certificate for the abstract C.4z graph obstruction. |
| `agents/frobenius/code/check_correlated_monodromy.py` | Necessary finite graph congruences for the correlated type-(1,2) cone. |
| `agents/frobenius/code/check_cubic_incidence_geometry.py` | Exact finite certificate for the F_125 cubic/quartic incidence input. |
| `agents/frobenius/code/check_genus5_hom_parity.py` | Reconstructed exact mod-2 gluing calculation for the genus-five Prym method. |
| `agents/frobenius/code/check_graph_transfer_countermodel.py` | Exact finite identities for the ppav-surface transfer countermodel. |
| `agents/frobenius/code/check_primitive_exceptional_quotient.py` | Exact bounded checks of the integral primitive quotient in PB Step 3. |
| `agents/frobenius/code/check_semihomogeneous_parity.py` | Exact exterior-algebra identities and bounded arithmetic checks. |
| `agents/frobenius/code/check_tetrahedral_resolution.py` | Finite algebra checks for TG.1--TG.5; not a Chow/K-theory certificate. |
| `agents/frobenius/code/check_uniform_gysin.py` | Finite symbolic certificate for the explicit C.3t equations. |
| `agents/frobenius/code/check_uniform_integral_picard.py` | Finite algebra checks for proposed C.3bg; not a replacement for its uniform proof. |
| `agents/frobenius/code/derive_correlated_certificate.py` | Find an exact small polynomial dual certificate for the level-2 test. |
| `agents/frobenius/code/finalize_primitive_boundary.py` | Retain the Witt proof and make the shorter integral-quotient final auxiliary. |
| `agents/frobenius/code/find_small_characteristic_picard_pairs.py` | Find finite-field ordinary quartics and certify a nondegenerate KS cup form. |
| `agents/frobenius/code/orlov_surface_parity.py` | Exact exterior-algebra certificate for an Orlov-transform surface-cycle lead. |
| `agents/frobenius/code/run_BT1_word_reversal.py` | One instrumented replay of the exact previously untimed word-reversal program. |
| `agents/frobenius/code/test_cubic_incidence_pair.py` | See program and accompanying report. |
| `agents/frobenius/code/verify_c4_exterior.py` | Exact exterior-algebra certificates for C.4i and C.4l. |
| `agents/frobenius/code/verify_c4_prym_arithmetic.py` | Exact arithmetic checks for C.4n; no geometric existence is simulated. |
| `agents/frobenius/code/verify_c4t.py` | Exact matrix checks and a bounded binary-form reduction certificate for C.4t. |
| `agents/frobenius/code/verify_frobenius_cases.py` | Exact finite certificates for RESEARCH_SA06, Part B and E.2. |
| `agents/frobenius/code/verify_ramified_picard_counterexample.py` | Exact F_9 certificate for the ramified non-Picard base-change example. |
| `agents/real_weil/code/acquire_bt1_source_retry.py` | See program and accompanying report. |
| `agents/real_weil/code/acquire_determinantal_source.py` | Retain the exact author-authorized primary PDF and acquisition metadata. |
| `agents/real_weil/code/acquire_intrinsic_quotient_sources.py` | Acquire exact primary PDFs for the intrinsic proper-family source audit. |
| `agents/real_weil/code/acquire_kohrita_v2.py` | Retain the historical primary version for a parameter-scope check. |
| `agents/real_weil/code/acquire_kummer_incidence_sources.py` | See program and accompanying report. |
| `agents/real_weil/code/acquire_kummer_published_sources.py` | See program and accompanying report. |
| `agents/real_weil/code/acquire_modulus_component_sources.py` | Acquire exact primary sources for the post-C.3bt family-scope audit. |
| `agents/real_weil/code/acquire_nevins_source.py` | Retain the primary six-page Nevins v2 source; no theorem test. |
| `agents/real_weil/code/acquire_qin_wang_source.py` | See program and accompanying report. |
| `agents/real_weil/code/acquire_sources.py` | Reproduce this agent's primary-source downloads (read-only HTTP GETs). |
| `agents/real_weil/code/acquire_supersingular_bt1_sources.py` | See program and accompanying report. |
| `agents/real_weil/code/audit_event_metadata.py` | Read-only source-log audit; recommendations do not modify historical logs. |
| `agents/real_weil/code/build_fragments.py` | Compile the two contributed fragments to catch TeX errors and overflows. |
| `agents/real_weil/code/build_metadata.py` | Build this agent's statement and audit ledgers; no mathematical inference. |
| `agents/real_weil/code/check_C3bf_integral_picard.py` | Exact finite algebra for C.3bf; no formal/algebraization claim is tested. |
| `agents/real_weil/code/check_C3bj_uniform_kernel.py` | Finite algebra checks for C3bj; not a substitute for its geometric proof. |
| `agents/real_weil/code/check_C3bk_higher_product_kernel.py` | Exact finite coefficients for C.3bk; the geometric proof is not delegated to code. |
| `agents/real_weil/code/check_C3bl_primitive_boundary.py` | Finite integral checks for the complete C.3bl construction and boundary map. |
| `agents/real_weil/code/check_all_dimension_endpoint.py` | Exact finite checks for AE; these do not certify geometric existence. |
| `agents/real_weil/code/check_alpha_p_constant_complement.py` | Bounded symbolic checks accompanying BT.9, not a group-scheme proof. |
| `agents/real_weil/code/check_bt1_height6_fermat.py` | Finite combinatorial certificate for the Pries--Ulmer height-six input. |
| `agents/real_weil/code/check_divisor_endpoint.py` | Exact finite curve/divisor checks for C.3bb; geometry is proved in the text. |
| `agents/real_weil/code/check_dual_component_lifting.py` | Bounded rational matrix checks for DC.5; the universal proof is in the text. |
| `agents/real_weil/code/check_endpoint_family_algebra.py` | Exact finite checks of the universal identities used in the endpoint proof. |
| `agents/real_weil/code/check_high_range_incidence.py` | Exact finite checks for C.3aj; they do not certify Hodge genericity. |
| `agents/real_weil/code/check_kummer_five_point_detector.py` | Exact bounded exterior-algebra certificate for the five-point Kummer test. |
| `agents/real_weil/code/check_kummer_incidence_parity.py` | See program and accompanying report. |
| `agents/real_weil/code/check_kummer_incidence_parity_initial_failed.py` | See program and accompanying report. |
| `agents/real_weil/code/check_ordinary_cy_boundary.py` | Exact finite certificates for C.3at; no numerical smoothness tests. |
| `agents/real_weil/code/check_positive_characteristic_critical_injectivity.py` | Exact finite certificates for C.3ay, separate from its universal proof. |
| `agents/real_weil/code/check_positive_characteristic_low_injectivity.py` | Exact supplementary checks for C.3aw, with explicit scope boundaries. |
| `agents/real_weil/code/check_positive_characteristic_low_range.py` | Exact finite checks for C.3av; the universal proof is independent. |
| `agents/real_weil/code/check_segre_integral_quotients.py` | Finite exact algebra checks for C.3ba; no actual-cycle theorem is inferred. |
| `agents/real_weil/code/check_tetrahedral_spectrum.py` | Exact finite cochain checks for TS; no family-algebraization claim. |
| `agents/real_weil/code/check_top_all_dimensions.py` | Exact finite arithmetic and exterior-algebra certificate for proposed C3as. |
| `agents/real_weil/code/check_top_all_positive_characteristics.py` | Recovered finite certificate for C3aq; no extrapolation to all primes. |
| `agents/real_weil/code/check_top_p_tangent.py` | Recovered exact certificate for C3an; global proof and finite checks are separate. |
| `agents/real_weil/code/check_torsion_open_lemma.py` | Exact algebra/source check for the rejected open-complement lemma. |
| `agents/real_weil/code/check_triple_free_component_lifting.py` | Exact finite algebra checks for C.3br; no geometric theorem is delegated here. |
| `agents/real_weil/code/compile_all_dimension_endpoint.py` | Four-pass standalone check of the all-dimensional endpoint draft. |
| `agents/real_weil/code/compile_dual_component_lifting.py` | Timed four-pass standalone assembly of C.3bs. |
| `agents/real_weil/code/compile_endpoint_family.py` | Four-pass standalone formatting check for the full endpoint proof. |
| `agents/real_weil/code/compile_tetrahedral_auxiliaries.py` | Retained four-pass typesetting check for the unnumbered auxiliaries. |
| `agents/real_weil/code/compile_top_quotient_recovery.py` | Fresh four-pass verification of a recovered final top-quotient fragment. |
| `agents/real_weil/code/compile_triple_free_component_lifting.py` | Timed four-pass standalone assembly check for C.3br. |
| `agents/real_weil/code/fetch_C3bi_sources.py` | Acquire the three newly opened primary sources, retaining times and hashes. |
| `agents/real_weil/code/fetch_C3bi_sources_initial.py` | Acquire the three newly opened primary sources, retaining times and hashes. |
| `agents/real_weil/code/fetch_higher_restriction_sources.py` | See program and accompanying report. |
| `agents/real_weil/code/fetch_ordinary_cy_sources.py` | Retain exact primary sources consulted for C.3at, with hashes and timing. |
| `agents/real_weil/code/fetch_semipurity_sources.py` | Retain primary PDFs already opened during the semipurity investigation. |
| `agents/real_weil/code/finalize_C3br.py` | Promote the fully approved C.3br proof and append its canonical owner records. |
| `agents/real_weil/code/finalize_C3bs.py` | Promote fully audited C.3bs without editing root-owned integration files. |
| `agents/real_weil/code/recover_top_sources.py` | Recover the two opened Mukai primary preprints with fresh hashes and timings. |
| `agents/real_weil/code/verify_examples.py` | Exact finite checks used in D.1, D.2, D.3, E.4 and E.5. |
| `agents/real_weil/code/verify_local_picard.py` | Exact finite checks for C.3i; the all-dimension proof is in C3_picard.tex. |
| `agents/real_weil/code/verify_localization.py` | Finite checks of the actual chain matrices in E.4e--f, including m=1. |
| `agents/real_weil/code/verify_multiplicative_divisor_quotient.py` | Exact certificates for the explicit triangle quotient in C.3y. |
| `agents/real_weil/code/verify_picard_deformation.py` | Exact finite polynomial certificates for C.3m. |
| `agents/real_weil/code/verify_positive_characteristic_boundary.py` | Exact certificates for C.3x; finite samples do not prove non-torsion. |
| `agents/real_weil/code/verify_protorsor.py` | Exact finite checks of E.5f, supplementing its infinite-limit proof. |
| `agents/real_weil/code/verify_segre_nori_quotient.py` | Sign and degree certificates for C.3aa; no Chow group computation. |
| `agents/real_weil/code/verify_surface_cone_top.py` | Exact algebra checks used in C.3ab; these do not prove its K-theory inputs. |
| `agents/real_weil/code/verify_top_quotient_aux.py` | Exact finite certificates for the proper-K2 curve and C.3ad form formulas. |
| `agents/real_weil/code/verify_wild_purity.py` | Exact arithmetic checks for the E.4j quadratic torsor. |

The complete program/output correspondence, hashes and consolidated paths are in `code/program_files_output.json`. Bibliographic retrieval records retain failed attempts as well as later successful openings.
