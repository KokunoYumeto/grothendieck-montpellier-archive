# GCT_OBS research package

This package contains the current paper, question register, dated ledger, check events, mathematical proofs, exact programs, results, and ongoing research notes. A checkpoint is an active-work snapshot; the precise unresolved questions remain listed in QUESTIONS.tsv.

## Directory layout

- `GCT_OBS.tex` is the main paper. Its included LaTeX files are under `work/`.
- `work/root` contains the nested determinant jets, exact plethysm sieve, symmetric Kronecker calculation, and primary-source audit.
- `work/support_lmr` contains the support proof, dependency inventory, explicit six-function LMR comparison, external-padding correction, and the 804-dimensional reduction.
- `work/quaternary` contains independent reconstruction of the permanent projection and uniform endpoint certificates, plus current symbolic-polynomial experiments.
- `work/border` contains independent integral border-rank checkers and current ten-plane calculations. Its validated representative lists are included.
- `instructions/PROMPT.md` reproduces the supplied task. The large unchanged input archive is not copied into each checkpoint; it remains the separate user attachment.

## Reproducible commands

Run these from the package root using Python3.10 or later. The mathematical checkers require only the standard library unless an optional SymPy comparison is explicitly invoked.

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

The paper can be compiled with an ordinary current LaTeX installation by running `pdflatex GCT_OBS.tex` twice. The current execution environment required local TeX format setup; its compilation logs are retained as documentation rather than mathematical evidence.

## Claim discipline

A nonzero modular evaluation proves a characteristic-zero nonzero polynomial after the specified denominators are cleared. It does not prove characteristic-independent vanishing or full multiplicity comparison. The all-characteristic border-rank proof separately records localization primes and checks the exceptional characteristics. Every rank marked as still open is genuinely uncomputed.

For continuation, retain the latest checkpoint together with the two original attachments. Recreate the input archive as the `project/` directory only when a source comparison is needed. The new mathematical checkers do not require unpacking nested ZIPs.
