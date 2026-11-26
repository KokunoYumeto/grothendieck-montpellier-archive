# Exact circuit sizes for theta graphs and cycles with pendant leaves

**The primary graph requires exactly 18 charged gates.** The proposition
`HasCircuitSize 12 F 17` is false. The 18-gate witness is verified on all 4096
inputs; the all-DAG lower bound is proved in the paper and independently
re-proved by a fresh worker before seeing that proof.

The requested follow-on also closes: the eight-cycle with leaves at 0 and 3
needs exactly 14 gates. More generally, for k >= 3, C_(2k) with two distinct pendant leaves needs
3k+1 gates for roots in the same bipartition and3k+2 for opposite roots.

## Mathematical mechanism

For any nonempty finite simple graph of minimum degree≥2 and no4-cycle, its
edge function needs at least n−1+τ(G) AND/OR gates, regardless of internal
negation. First branching wires yield an ordered partition into independent
residual twin groups; one vertex per group covers their remaining edges.
The operand-incidence count then proves the binary bound. For the target,
this is17 binary gates. A17-total circuit would be positive, but its positive
minimum is 18. The paper now includes a full attributed re-proof of the
known positive theorem for every theta without a four-cycle.

The next three-root case also closes: the nine-cycle with leaves at 0, 3
and 6 requires exactly 17 gates. More generally, for k >= 4, an odd cycle C_(2k+1)
with three pairwise nonadjacent roots at odd cyclic distances requires
3k+5 gates after attaching one fresh leaf to each root.

## What has and has not been formally checked

`lean/BranchCoverCore.lean` compiled with official Lean4.36.0. Its four theorem
axiom lists contain exactly propext, Classical.choice and Quot.sound. This
checks the ordered-group-to-cover step. The circuit-to-partition argument
and literal project-model lower bound are mathematical proofs, not complete
new Lean certificates. `ThetaDecisionConditional.lean` states the exact target
with the two formal bridge bounds as explicit hypotheses and is uncompiled.
`BranchCover.lean` is a separate uncompiled Mathlib-shaped graph helper.

## First replay commands

From this workbench directory:

```sh
python3 programs/verify_theta.py
python3 programs/independent_main_check.py
python3 programs/branch_verify_certificate.py
python3 programs/adjacent_graph_checks.py
python3 programs/c8_two_leaves_check.py
python3 programs/c9_three_leaves_check.py
lean lean/BranchCoverCore.lean
```

Python checks use the standard library. See BUILD.md for the precise Lean
version, expected outputs, paper build, and optional solver replay. The
solver run on17-gate one-NOT circuits timed out and provides no exclusion.

## Contents and scope

The editable paper and its built PDF are in papers/theta/. Statements,
proof obligations, source credits and actual checks are recorded in
STATEMENTS.tsv, CHECK_EVENTS.tsv, CROSSWALK.tsv and SOURCES.tsv. Research
history is outside the reader paper. The mathematical results do not settle
the universal subcubic girth-seven conjecture with arbitrarily many hubs.

The workbench is ready for the editor's repository:
<https://github.com/KokunoYumeto/arithmetic-geometry-complexity-workbench>.
No public repository, assignment, message or publication has been changed.
No unchanged input attachment or other author's paper is included.

Original text and code: CC0 1.0 Universal.
<https://creativecommons.org/publicdomain/zero/1.0/>
