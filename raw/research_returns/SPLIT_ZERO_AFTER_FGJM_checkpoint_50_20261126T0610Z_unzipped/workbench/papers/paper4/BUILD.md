# Build Paper 4

Engine: pdfLaTeX (TeX Live 2025 or a compatible standard installation).

From this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography is inline. No local style, image, or external input is required. Standard packages: amsmath, amssymb, amsthm, mathtools, microtype, geometry, natbib, hyperref, enumitem, lmodern, fontenc, inputenc. The output is main.pdf. All mathematical figures are expressed in the text; there are no figure-source dependencies.

Finite checks from the workbench root:

```sh
python programs/paper4_checks.py --output checks/paper4_results.json
python programs/paper4_witness_examples.py --output checks/paper4_witness_examples.json
python programs/paper4_matching_injection.py --output checks/paper4_matching_injection.json
python programs/paper4_smt_search.py --directory checks/paper4_smt --timeout-ms 30000 --large
```

The first command uses Python's standard library and returns PASS, including 384000 exact gate/input checks, all 7 nonempty three-vertex simple graphs, and all 53 nonempty four-vertex C4-free simple graphs. The second independently expands the two sharp examples, checks all 16 inputs of each, and counts exactly the gates discarded by lower-envelope extraction and pruning. The third checks all4096inputs of a valid19gate matching-injection circuit and refutes its tempting18gate shortcut; it also verifies the three discarded gates despite two missing edges and cover-number drop two. It imports the adjacent `paper4_witness_examples.py`. The fourth needs the Z3 shared library discoverable by ctypes; it writes exact SMT-LIB2 instances and distinguishes sat, unsat, and unknown. A timeout is not a mathematical conclusion. These programs do not certify the unrestricted infinite graph conjecture.

## Additional independent example verifier

```sh
python programs/paper4_induced_matching_d5.py
```

Run this from the workbench root. It uses only Python's standard library and writes checks/paper4_induced_matching_d5.json. It verifies all2048inputs of the eleven-vertex example, expands the polynomial, independently performs minimum-degree extraction, exhausts vertex covers, and tests the exact four-cycle criterion. It proves the scope distinction in Example5.29; it does not refute the full star lower bound.

## Additional different-method scope-example checks

From the workbench root, run `python programs/paper4_one_product_nonminimal_counterexample.py` and `python programs/paper4_one_product_nonminimal_independent.py`. The first uses polynomial expansion and exhaustive finite checks; the independent verifier uses ROBDDs, second derivatives and graph matching/cover certificates. These verify Example5.45, not the unrestricted conjecture.

## Latest standalone build

Checkpoint49 synchronized 2026-11-26T05:08:59.963373+00:00: **302 pages**, three successful pdfLaTeX passes, zero warnings. Source SHA-256 `e3ac1d2bad22b47bd3a1c08e4c2b725f59a4598e9b424692b9f91f672b6a8f59`; PDF SHA-256 `519786095fe8df8990ee1c4253ae004a98d9e5527d84d2e406a74012348275b3`. Exact report: `workbench/checks/paper4_checkpoint49_build.json`.

Every changed final page was directly displayed and inspected or inherits an actual prior view through explicit exact full-pixel equality; other pages exactly match the reviewed302-page checkpoint48. Separate expert/newcomer full readings cover every new statement/proof and amended opening/residual/live paragraph. Exact reviewer attribution is in the report. Historical checkpoints remain unchanged.

Historical recovery drivers: `programs/maintenance/paper4_checkpoint49_build.py`, `paper4_checkpoint49_aggregate_reviews.py` and `paper4_finalize_checkpoint49.py`; the documented local recovery environment is required. Ordinary TeX installations use the standard three-pass command above. No binary format/map/package is bundled.
