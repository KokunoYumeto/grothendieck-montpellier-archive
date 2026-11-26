# Arithmetic geometry and complexity: counting varieties

This workbench accompanies **Counting satisfying assignments on smooth projective varieties, after Katz**. It separates the mathematical statements from the computational presentation on which a reduction or algorithm depends.

## The central result

At every fixed prime, a polynomial-size arithmetic circuit can describe a smooth geometrically integral anticanonical projective hypersurface whose top coherent Frobenius scalar is the number of satisfying assignments modulo that prime. This is a modular-counting completeness result on a smoothness promise. A bounded number of explicitly sparse equations permits algorithms unavailable from the circuit description alone.

The paper also studies saturation, support bounds, projection, hidden split coordinates, affine arrangement complements, fixed-field root multiplicities, Artin--Schreier curves, and a smooth sparse cubic over the integers whose Tate multiplicity is an exact count.

## Formal groups and height

For every prime `p` and every finite height `h ≥ 1`, the paper constructs a smooth geometrically integral anticanonical hypersurface over `F_p` whose top Artin–Mazur formal group has exact height `h`. Its degree and number of homogeneous variables can both be taken to be `p^h + p + 1`. For each fixed `p` and fixed finite `h`, deciding exact height `h` from a division-free arithmetic circuit is unconditionally `Mod_p P`-complete under deterministic polynomial-time many-one reductions, on the stated smooth anticanonical promise with dimension allowed to grow.

At fixed `p`, the full height can be computed in polynomial space: the algorithm outputs the finite value in binary or identifies infinity, using `O_p(L² log(L+2))` working bits for complete binary input length `L`. Infinite-height decision therefore belongs to PSPACE. Its hardness classification remains open in this workbench.

Four standard-library Python programs accompany the formal-group results: **AllHeightSeedChecks**, **InvariantDerivativeChecks**, **SecondHeightExampleChecks**, and **ReplicaCountChecks**. They check finite exact seed coefficients, derivative constant terms, and replica-counting examples. Their commands, expected outputs, and the existing replay comparison are documented in `PROGRAMS.md`; the universal results are proved separately in the paper.

The precise statements are `fg:thm:all-heights`, `fg:cor:exact-height-complete`, and `fg:thm:space`; their original proofs, independent reconstructions, and scoped comparisons are linked in `STATEMENTS.tsv` and `CHECK_EVENTS.tsv`.

## Layout

| Path | Purpose |
|---|---|
| `papers/counting/` | Standalone LaTeX project, bibliography inputs, and compiled paper |
| `programs/` | Original Python verification programs; two require SymPy |
| `certificates/` | Exact computed outputs and finite test certificates |
| `STATEMENTS.tsv` | Stable predeposit statement keys, locations, dependencies, and check summaries |
| `CHECK_EVENTS.tsv` | Dated events with the scope of each check |
| `SOURCES.tsv` | Citations, locations, hashes, and pages used; no copied publications |
| `MANIFEST.sha256` | SHA-256 of each version's files |

The corresponding top-level `CROSSWALK.tsv`, `QUESTIONS.tsv`, `DICTIONARY.md`, `LITERATURE.md`, and `LEDGER.md` document provenance, questions, mathematical translations, searches, and changes of research status. A checkpoint may contain unfinished register rows; this is stated in its ledger.

## Reproduce the original calculations

Use Python 3.10 or later. The two fixed-field/invariant replays also require SymPy (checked with version 1.14.0); the other programs use the standard library. See `PROGRAMS.md` for each program name, certificate, and check scope. From this directory:

```sh
python3 programs/core_checks.py --output certificates/core_results.json
python3 programs/sparse_presentation_checks.py
python3 programs/structured_verify.py
python3 programs/structured_algorithms.py
python3 programs/fixed_field_replay.py
python3 programs/fixed_invariants_replay.py
python3 programs/distributed_padding_checks.py
python3 programs/sparse_line_gcd_checks.py
python3 programs/sparse_digit_deflation_checks.py
python3 programs/saturation_ci_checks.py
python3 programs/sliced_colon_checks.py
```

All programs use exact finite-field, integer, or rational arithmetic. Failed assertions or a nonzero exit are failures. Finite examples do not replace the universal proofs. Per-program readmes and certificates identify the enumerated ranges and expected outputs.

Selected independently reproduced values are the ternary quartic counts `13, 11, 15`, the positive-unit-clause projective count `9953`, the odd-prime linear-constraint example `10065`, and the two-variable OR cubic counts `56, 324, 3500` at field sizes `2, 3, 5`. The characteristic-two and characteristic-three unit root-of-unity examples have `(N,K,L)=(161,33,33)` and `(253,55,55)` respectively.

## Build the paper

```sh
cd papers/counting
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography is inline through local `refs_*.tex` inputs; BibTeX and network access are unnecessary. See `BUILD.md` for the verification procedure.

## Record format

The requested format is format 1 of the mathematics-workbenches repository, dated 22 November 2026. Its public `FORMAT.md` was retrieved and read after the initial attempts failed. This is a predeposit package: the user assigns its work number and permanent page at filing. The `CV-` keys identify statements consistently during that preparation and are not a claim that a `WB-nnnn` number has already been registered. The final version layout and filing map are prepared separately; checkpoints preserve the live working paths needed to continue the research. No `DEPOSITED.md`, public commit or registered work number is asserted before filing.

## Method and licence

GPT-6 Astra (ChatGPT Pro mode) produced the mathematics and text. Separate instances of the same model performed the independent re-proofs identified in the event register. Other checks were targeted proof readings or exact computations. No human has checked this paper; no formal verification is claimed. Earlier Claude Opus 5.5 checks are limited to their recorded scope. Original text and code: CC0 1.0 Universal, <https://creativecommons.org/publicdomain/zero/1.0/>.
