# Zeta and L-functions workbench

This predeposit work studies deterministic constructions of finite fields and the exact analytic hypotheses used by the algorithms. Its two principal bounds are an unconditional construction polynomial in the prime degree, log characteristic and a numerical cyclotomic cofactor, and an A-only polynomial-logarithmic construction for each fixed prime degree and fixed valuation. The threshold construction now removes full prime-power factors at small primes ell with r not dividing ell−1 before charging its residual cofactor; under A, for each fixed degree r and congruence depth t, it also removes every small prime ell with v_r(ell−1)<=t. The numerical residual and the fixed-parameter dependence of the exponent remain explicit. The uniform growing-parameter problem remains open.

Tang's separate interfaces accept the named OpenAI and Cureton–Thorner 2026 preprint statements, including Tang's revision of the latter's Lemma 8.1. They are not an independent certification of those preprints.

## Read and reproduce

The current version is in `work/unfiled/v1/`. Start with `papers/grh_algorithms.pdf`; the adjacent TeX file is fully standalone, with every proof and its bibliography. `papers/BUILD.md` gives exact three-pass build and page-render commands.

From that version directory:

```sh
python3 build_paper.py
python3 run_checks.py --include-probe
```

The computations require Python 3.10 or later and SymPy for the fixed-r=5 example. The other programs in that canonical suite use the standard library. Additional Part4 checks and their dependencies are listed in `checks/reviews/README.md`. Stable JSON envelopes identify the program source and serializer hashes, statement scope, and exact arithmetic result. The suite runs in an isolated temporary directory and compares against `checks/expected/`. The cubic probe recomputes the range through 100,000. These finite examples do not implement the full CM recognition/Pila construction or certify its asymptotic complexity.

## Find a claim and its evidence

`STATEMENTS.tsv` preserves GRH-P001–GRH-P142 and appends GRH-P143–GRH-P164. Its current-proof column points to the complete paper proof; finishing-review columns distinguish completed checks from pending work. Cumulative `CHECK_EVENTS.tsv` never relabels a historical check as new, an exposed review as blind, or a finite calculation as a theorem proof. Sealed reports, exposure records and separately dated errata are in `checks/reviews/`; its README maps the proofs and gives exact commands for the supplementary verification.

Historical paths in inherited columns and older events refer to the supplied cp08 attachment. Unchanged historical files are not duplicated. The current complete proofs, fresh reports, revised programs and new documentation are included. Earlier IDs stay stable when a stronger result supersedes their bound.

`SOURCES.tsv` gives primary citations, exact pages, original-byte SHA-256 where obtained, and audit scope. Third-party papers, scans, archives and extractions are excluded. Source manifests distinguish direct downloads from web-only reads and retrieval failures.

## Format 1 and filing

The owner assigns the permanent WB number, record page and repository commit at filing. The predeposit path `work/unfiled/v1/` makes no registry claim. Replace `unfiled` with the assigned number, map the preserved IDs to permanent WB tags, update the paper's record address, regenerate the version manifest, and record the filing commit. A deposited version then stays immutable. No public repository has been changed.

The paper leaves its author line empty. The paper and the workbench's own new text are dedicated to CC0 1.0. Third-party works retain their rights and appear only as citations. No human review is asserted.
