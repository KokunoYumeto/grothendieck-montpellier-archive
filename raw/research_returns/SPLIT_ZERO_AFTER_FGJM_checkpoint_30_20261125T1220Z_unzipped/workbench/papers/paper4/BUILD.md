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

Exact source/PDF hashes, page count and complete visual-review evidence are in workbench/checks/paper4_checkpoint30_build.json and workbench/checks/paper4_build_review.md.

Final verified25November2026 standalone build: **169 pages**, three successful passes, all-page visual coverage, zero final warnings. Synchronized 2026-11-25T12:17:30.654869+00:00. Source SHA256 `204d86be8780f70e62e1a82c1602ac15df1af82408cf14d1260fc800c14d84b8`; PDF SHA256 `f45e4526a51f1dbc45fb01d7d6aedf5f1565015b5456e85e45a55e98c00ef7bd`.
