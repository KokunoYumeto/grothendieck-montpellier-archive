# GCT_OBS research package

This package contains the current paper, question register, dated ledger, check events, mathematical proofs, exact programs, results, and ongoing research notes. A checkpoint is an active-work snapshot; the precise unresolved questions remain listed in QUESTIONS.tsv.

## Directory layout

- `GCT_OBS.tex` is the main paper. Its included LaTeX files are under `work/`.
- `work/root` contains the nested determinant jets, exact plethysm sieve, symmetric Kronecker calculation, and primary-source audit.
- `work/support_lmr` contains the support proof, dependency inventory, explicit six-function LMR comparison, external-padding corrections, complete804and2386-space comparisons, small degree-six nonic certificates, and padded injectivity proofs.
- `work/quaternary` contains independent reconstruction of the permanent projection and uniform endpoint certificates, plus current symbolic-polynomial experiments.
- `work/border` contains independent integral border-rank checkers and current ten-plane calculations. Its validated representative lists are included.
- `instructions/PROMPT.md` reproduces the supplied task. The large unchanged input archive is not copied into each checkpoint; it remains the separate user attachment.

## Reproducible commands

Run these from the package root using Python3.10 or later. The standalone mathematical checkers use the standard library or SymPy. Exploratory accelerated builders are separate. The exact ten-plane continuation requires SymPy; its optional faster arithmetic backend does not change the calculation.

```bash
python work/border/scripts/run_all.py
python work/support_lmr/scripts/check_lmr_ambient.py
python work/support_lmr/scripts/verify_lmr_explicit.py
python work/support_lmr/scripts/check_external_padding_bounds.py
python work/support_lmr/scripts/check_centered_jet_gate.py
python work/quaternary/scripts/check_projection.py 11 12 13 14 15 16 17 --workers 4 --output quaternary_projection_rerun.json
python work/quaternary/scripts/check_border18.py --workers 4 --output border18_rerun.json
python work/quaternary/scripts/check_endpoint.py --insertions 4 --output endpoint_rerun.json
python work/quaternary/scripts/check_ordinary.py --output ordinary_rerun.json
python work/root/scripts/check_nested_profiles.py 9 --scalar --output det9_nested_rerun.json
python work/root/scripts/check_nested_profiles.py 23 --workers 4 --output det23_nested_rerun.json
python work/root/scripts/search_four_row_candidates.py 9 6 7 8 9 10 --output nonic_sieve_rerun.json
python work/root/scripts/search_four_row_candidates.py 23 6 --output degree23_sieve_rerun.json
python work/root/scripts/plethysm_four_rows.py 9 15 114 9 6 6 --output ray9_rerun.json
python work/root/scripts/plethysm_four_rows.py 23 35 756 21 14 14 --output ray23_rerun.json
python work/root/scripts/symmetric_kronecker_candidate.py --output symmetric_kronecker_rerun.json
```

The recorded result files identify the parameters actually used. The large character sum and degree23 sieve take longer than the small LMR checks. Runtime depends on the machine; no fixed time is part of a mathematical certificate.

The determinant bound44 and exact19-term upper curve are reconstructed from the border working directory:

```bash
cd work/border
python scripts/check_det10_gate.py
python scripts/check_det10_refinement.py
python scripts/check_det10_last_case.py
python scripts/check_det10_upper19.py
```

The last-case continuation records every generic exceptional polynomial, rational fiber, quadratic number-field fiber and subsequent projective family. It returns OPEN if any branch is unhandled. The recorded complete run returned PASS; an independent root invocation is also retained when completed.

Additional small standalone checks, run from the package root:

```bash
python work/support_lmr/scripts/check_even_padding.py
python work/support_lmr/scripts/check_cubic_padding_boundary.py
python work/support_lmr/scripts/check_kl_counterexample.py
python work/support_lmr/scripts/check_equal_tail_stabilization.py
python work/quaternary/scripts/check_nonic_candidate.py
python work/quaternary/scripts/check_nonic_determinant.py
```

QC-008 records every full evaluation matrix and ordinary scalar Gaussian elimination for the804,1250and2030 spaces. S-010 completes the2386-space with all graph expansions, coefficient minors,5774120 evaluation entries and the ordinary scalar rank verified. The coefficient bases, profile certificates, sample seeds and byte hashes are included. QC-009's standard-library sampler regenerates the2420 determinant and2410 padded points; the root regenerated both complete sets independently and matched their tensor hashes.

The paper can be compiled with an ordinary current LaTeX installation by running `pdflatex GCT_OBS.tex` twice. The current execution environment required local TeX format setup; its compilation logs are retained as documentation rather than mathematical evidence.

## Claim discipline

A nonzero modular evaluation proves a characteristic-zero nonzero polynomial after the specified denominators are cleared. It does not prove characteristic-independent vanishing or full multiplicity comparison. The all-characteristic border-rank proof separately records localization primes and checks the exceptional characteristics. Every rank marked as still open is genuinely uncomputed.

For continuation, retain the latest checkpoint together with the two original attachments. Recreate the input archive as the `project/` directory only when a source comparison is needed. The new mathematical checkers do not require unpacking nested ZIPs.

## Relative second derivatives and low-degree padding

`python work/root/scripts/check_relative_second_jets.py` performs the complete fresh standard-library OBS-007 check, about132 seconds on the current executor. It reconstructs both Jacobian ranks, all80 second-coefficient vectors, both kernel systems, and the final ordinary scalar rank. `--resume` accepts only a source-and-input-hashed completed prefix. QC-011 is a complete symbolic proof in `work/quaternary/low_degree_padding.tex`; its method and exact primary locators are stated there.

For the complete permanent ten-plane orbit gate, run `python scripts/check_per10_global_gate.py` from `work/border`. It independently reconstructs all225702 symmetry orbits and every recorded Koszul witness, and reports all596 direct survivors; BR-008 separately removes P20.

## Bounded Hessians and the small degree-six components

These completed checks use the Python standard library:

```bash
python work/root/scripts/check_quadratic_relative_jets.py
python work/root/scripts/check_bounded_jet_windows.py work/root/results/bounded_window_n9_l7_b10
python work/root/scripts/check_bounded_jet_windows.py work/root/results/bounded_window_n9_l6_b11
python work/root/scripts/check_bounded_jet_windows.py work/root/results/bounded_window_n23_l16_b19
python work/quaternary/scripts/check_three_nonic_restrictions.py
python work/support_lmr/scripts/verify_four_nonic_certificate.py
python work/border/scripts/check_per10_unique_coupled.py --enumerate
```

The bounded-Hessian commands reconstruct the selected mixed derivatives, integral lowering words and every selected matrix entry, then perform ordinary scalar elimination. The stronger completed matrices have sizes2677and3220. The small component checkers reconstruct the explicit bracket contractions and ambient character counts. S-011's first completed output had a reporting-only loop-variable shadow in its ambient field; the original output, corrected field, fresh character recount and exact provenance are all preserved. Its matrix entries and minor21 were unaffected.

BR-011's projective search retains unfinished cases and is intentionally conservative. `merge_per10_projective_refinements.py` and `merge_per10_current_gate.py` check coverage, identities and hashes; they do not rerun the underlying ranks. The latter adds the two completely checked BR-012 coupled exclusions. The current exact retained list is `work/border/certificates/per10_current_gate.json`.

The third-relative-jet files are exploratory until explicitly promoted by a completed independent certificate and recorded whole-proof review. Their provisional criterion and exact remaining numerical obligations are separated in the paper. They are not additional claimed multiplicity obstructions.
