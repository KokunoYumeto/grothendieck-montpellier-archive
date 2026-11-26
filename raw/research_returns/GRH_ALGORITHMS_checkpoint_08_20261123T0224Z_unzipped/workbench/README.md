# Deterministic finite-field constructions after Alpöge, Bach, von zur Gathen, Lenstra, Mumford, and Pila

This workbench accompanies one self-contained research paper. Read `papers/grh_algorithms.pdf` for the mathematical argument and `QUESTIONS.tsv` for the remaining questions. The current draft proves an unconditional construction polynomial in the prime degree r, log p, and the cyclotomic cofactor prime to2r. It also proves an A-only construction polynomial in log p for every fixed prime degree and fixed valuation, with constants depending on those fixed parameters. The uniform bound for arbitrary growing degree, valuation, and cofactor remains open by these methods. Tang's distinct polynomial-time route uses its separately named analytic inputs. Exact independent-check and final page-QA status is recorded in the check events and questions.

The work distinguishes a presented finite field from its promised prime-power order, and distinguishes an algorithm's output from the analytic assumptions in its proof. The classical table traces eighteen results or algorithmic stages to their exact L-functions. The principal algebraic reductions include complete proofs and same-model statement-alone re-proofs. The later polynomial-time conclusion is credited to Tang, OpenAI's prime-field theorem, and Cureton–Thorner's fixed zero-free theorem. Those large external theorems are background inputs, not independently certified here.

## Read and reproduce

Run the commands below from the **workbench root**, the directory containing `programs/`, `checks/`, and `papers/`.

- `papers/grh_algorithms.tex` is standalone LaTeX; its PDF is beside it.
- `STATEMENTS.tsv` records local statement identifiers, proofs, dependencies and check status.
- `CHECK_EVENTS.tsv` distinguishes independent re-proofs, targeted inspections, computations, and imported background, including dated resolutions of historical record pointers.
- `SOURCES.tsv` records source objects, URLs, hashes, versions and exact locations without including source papers.
- `programs/` and `checks/` contain exact finite computations and their expected output. The programs use Python's standard library and bundled sibling modules, except `check_fixed_wild_r5.py`, which also requires SymPy.
- `research/` contains original source audits and proof records, including failed routes and their precise obstructions.
- `CROSSWALK.tsv`, `DICTIONARY.md`, `QUESTIONS.tsv`, `LITERATURE.md`, and `LEDGER.md` accompany the mathematical text.

Each command in the table exits zero when its assertions hold and prints the listed expected JSON to stdout. Redirect stdout to a separate regenerated file to compare it; preserve the supplied expected file. These finite checks do not formally certify the uniform theorems.

| Command | Expected stdout |
| --- | --- |
| `python3 programs/check_tang_17_3.py` | `checks/check_tang_17_3_expected.json` |
| `python3 programs/check_kummer_examples.py` | `checks/check_kummer_examples_expected.json` |
| `python3 programs/check_elliptic_17_3.py` | `checks/check_elliptic_17_3_expected.json` |
| `python3 programs/derive_cm_inputs.py` | `checks/derive_cm_inputs_expected.json` |
| `python3 programs/check_cm_15_135.py` | `checks/check_cm_15_135_expected.json` |
| `python3 programs/verify_restricted_volcano.py` | `checks/verify_restricted_volcano_expected.json` |
| `python3 programs/verify_ordinary_quartic.py` | `checks/verify_ordinary_quartic_expected.json` |
| `python3 programs/verify_supersingular_point.py` | `checks/verify_supersingular_point_expected.json` |
| `python3 programs/check_sextic_cm_endpoint_17.py` | `checks/sextic_cm_endpoint_17.json` |
| `python3 programs/check_fixed_wild_r5.py` | `checks/fixed_wild_r5_expected.json` |
| `python3 programs/verify_higher_three_power.py` | `checks/verify_higher_three_power_expected.json` |
| `python3 programs/check_small_cofactor_cubic.py` | `checks/check_small_cofactor_cubic_expected.json` |
| `python3 programs/verify_fixed_cm_torsion.py` | `checks/verify_fixed_cm_torsion_expected.json` |

The elliptic program also writes its full certificate beside itself at `programs/elliptic_17_3_certificate.json`. The CM program imports `programs/derive_cm_inputs.py`, so retain these sibling files together.

Run the cubic comparison with:

```sh
python3 programs/probe_cubic_routes.py --limit 100000 --output-prefix ../checks/cubic_probe_regenerated
```

The output prefix is relative to the script directory, `programs/`. Compare `checks/cubic_probe_regenerated.csv` with `checks/cubic_probe.csv`, and `checks/cubic_probe_regenerated_summary.json` with `checks/cubic_probe_summary.json`.

Build with a normal TeX Live installation containing article, geometry, lmodern, amsmath, amssymb, amsthm, mathtools, booktabs, longtable, array, microtype, needspace, etoolbox, natbib, and hyperref. The explicit output directory updates the PDF beside its source:

```sh
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=papers papers/grh_algorithms.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=papers papers/grh_algorithms.tex
```

The final build must have no overfull box above 2 pt and all pages must be visually inspected. The separate build/review records state which stages are complete.

## Format and registration

The intended public home is https://github.com/KokunoYumeto/zeta-and-l-functions-workbench. Registration follows format 1 of https://github.com/KokunoYumeto/mathematics-workbenches. Only that central registry assigns permanent WB numbers. The identifiers here are provisional local identifiers, not invented permanent WB numbers. The number, permanent page, and deposited version tag remain unassigned until filing. No public repository has been changed and no author has been contacted.

At final packaging, a version manifest will record every included payload file except itself. Generated `__pycache__/` and `.pyc` files are excluded from the payload. No source papers, source extractions, unchanged attachments, or earlier checkpoint ZIPs belong in this workbench. The paper's source-version identity and final full-byte package identity will be recorded separately to avoid a self-referential hash.

## Method

Mathematics and text: GPT-6 Astra in ChatGPT Pro mode. Separate workers of the same model performed the recorded statement-alone re-proofs. Their configured reasoning effort was not separately exposed. Earlier project records report Claude Opus 5.5 at effort high checks of the earlier consequences; that provenance does not cover Tang's later theorem. No human has checked this work. Our new text and programs are dedicated to the public domain under CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/.

## Scope of the exact checks and average results

The restricted-volcano program checks the stated coordinate and root-transfer identities for p=17,53,71,107. It does not establish a uniform ordinary-curve construction. The ordinary and supersingular programs check their stated finite examples; the earlier checkpoint records document runs after integration. The record/documentation correction of 23 November did not rerun them.

The current paper also proves average-in-characteristic construction and factoring results with explicit exceptional-set bounds. The cubic average uses at most C log P parameters for each fixed C>1/log 3, outside O(sqrt(P) log log P) exceptional primes in (P/2,P]. It uses the classical quadratic-value product estimate and independent cubic characters. These results retain exceptional prescribed inputs and leave the uniform A-only gate open.

The sextic CM endpoint program checks z=12+3s, s²=-3 over F17, exact order9, and irreducibility of Y³−3Y−7. It does not implement the theta-recognition or Pila point-counting algorithm. The theorem is a proven theoretical polynomial-time composition with a large fixed exponent, not a practical CM implementation claim.
