# Reproducible checks and builds

Run the following commands from this `workbench/` directory. Python checks
use only the standard library, except for the optional SAT experiment.

## Checked witnesses and graph certificates

```sh
python3 programs/verify_theta.py
python3 programs/independent_main_check.py
python3 programs/branch_verify_certificate.py
python3 programs/adjacent_graph_checks.py
python3 programs/c8_two_leaves_check.py
python3 programs/c9_three_leaves_check.py
python3 programs/carrier_scope_check.py
python3 programs/hazard_pair_check.py
python3 programs/branch_restriction_check.py
python3 programs/theta_general_cover_check.py
python3 programs/theta_general_cover_check.py --dynamic-only 128
```

The successful results are recorded under `certificates/` and in
CHECK_EVENTS.tsv. These programs check explicit objects, all Boolean rows
for specified witnesses, graph covers, or bounded contraction families.
None exhausts all seventeen-gate DAGs. Some programs regenerate their own
certificate; the immutable return manifest identifies the deposited version.

Expected principal counts:

| Check | Expected result |
|---|---|
| Theta witness |4096 rows;3799true,297false;65 deliberate-mutation failures|
| Independent theta evaluator |4096 rows; zero mismatches;65 mutation failures|
| Residual graph certificate |frontiers1,13,79,283,642,939,999;17,440 residual checks|
| C8 leaves0,3 |14gates;1024 rows;885true,139false;27 mutation failures|
| Even-cycle family |32graphs;225,536 truth rows|
| C9 leaves0,3,6 |17gates;4096 rows;3711true,385false;74 mutation failures|
| Odd-cycle three-root family |4distance triples;348,160 truth rows|
| Carrier scope counterexample |8rows; first carrier branches3,3,3; unnormalized assertion refuted|
| Local branch contractions |33,867 DAGs;60,129 contractions;0 increases|
| Small theta covers |57graphs;296minimum covers;0 slot exceptions|
| Path-cover DP |365,759 parameter triples;8,127 direct-edge and126 triangular cases|

## Optional solver experiment

Dependency: `python-sat==1.9.dev25`.

```sh
python3 programs/synthesize.py --gates 18 --pin-witness --seconds 10 --output certificates/synthesis_positive.json
python3 programs/synthesize.py --gates 17 --not-count 1 --seconds 120 --output certificates/synthesis_one_not.json
```

The positive control returns SAT and zero full-cube mismatches. The recorded
second run was UNKNOWN after its120-second limit (122.16s observed), and
provides no negative certificate. It searches exactly-one-NOT normalized
seventeen-gate DAGs on139 necessary truth rows. A sampled SAT model must
pass the independent full-cube evaluation. The paper lower bound, not the
solver timeout, resolves the unrestricted target.

## Standalone paper

See `papers/theta/BUILD.md`. Copy the complete paper directory to a fresh
location and run its build commands; all local TeX inputs are included.
The final layout/read records are in `research/paper_review.md`.

## Successfully compiled graph certificate

Install official Lean `leanprover/lean4:v4.36.0`, then run:

```sh
lean --version
lean lean/BranchCoverCore.lean
```

Expected exit code0. Each of four `#print axioms` outputs must list exactly
`propext`, `Classical.choice`, `Quot.sound`. The actual compiler log and
source hash are in `research/formal_core_compile.log` and
`research/formal_core_status.json`. This file imports Std and the Lean Omega
tactic. It proves the ordered-partition-to-cover graph step under explicit
hypotheses. It does not formalize the circuit-to-partition construction.

## Uncompiled project-shaped sources

The pinned environment is Lean4.36.0, Mathlib commit
`fc4f59e577feb1a4956671bc04ac18aaaf8cd842`, project revision
`554253c04c90db722fc689346a6947081d8c4dbc`. Match the original frozen
source hashes before building.

```sh
cd /path/to/pequalnp-proofs/lean
lake exe cache get
lake env lean /absolute/path/to/workbench/lean/BranchCover.lean
lake env lean /absolute/path/to/workbench/lean/ThetaDecisionConditional.lean
```

These last two files are **uncompiled in this run**. The first is a
Mathlib/Defs graph helper. The second is a conditional literal target theorem
with the binary lower bound and positive lower bound as explicit formal
hypotheses. They are not unconditional certificates for the exact target.
Only the three permitted axioms above may occur; no sorryAx or native
reduction axiom is acceptable. The bootstrap failure and next formalization
steps are recorded in `research/formal_build.md`.

## Summary hypothesis regression check

Run `python3 programs/summary_scope_check.py`. It checks all64 inputs of
the six-gate C4-with-opposite-leaves witness, refuting the unqualified
even-cycle summary. The correct family theorem requires k>=3, as the
paper and THETA-015 already stated. Expected:6gates,64rows checked.
