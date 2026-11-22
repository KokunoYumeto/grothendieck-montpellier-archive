# GCT_POS research package

This continuation uses the supplied prompt and the once-extracted source archive. Its mathematical status is recorded per question in `QUESTIONS.tsv`, with dated movement reviews in `LEDGER.md`. The paper includes only findings whose complete proofs have received recorded checks. Exploratory files remain explicitly labelled; an arithmetic pass alone is not a proof of a general conjecture.

## Read first

- `GCT_POS.tex` and `GCT_POS.pdf`: integrated paper. The PDF is rebuilt periodically; the source, question register and check ledger govern the latest checkpoint status.
- `QUESTIONS.tsv`: each requested question and its proved result, refutation or remaining gate.
- `CHECK_EVENTS.tsv`: proof readings, independent reconstructions, computations and source checks, with actual scope. Imported branch records preserve provenance and may also describe a check recorded directly by the root; rows are not a count of independent proofs.
- `SOURCE_AUDIT.md`: exact inspected literature locators, known-result attribution and access limitations.
- `IMPLICATIONS.md`: consequences for GCT and the separate Grothendieck dictionary.
- `reviews/`: detailed whole-proof and computational receipts, plus formal movement reviews.

## Main checked results

Numerical PH3 is false for triple-rectangular Kronecker coefficients: for every n≥2 an actual Hilbert pole has order2^(n−1)·3^r for some r≥0. Every product denominator therefore contains an exponent at least2^(n−1), versus unified parameter rank(x)=n²+5n (and also the introductory h=n⁴+O(n)). The exact dyadic pole and strict positivity/saturation index bounds remain open in variable dimension. The proof is K-023, R-NEW-004, K-024 and PNEW-013.

Other checked results and their limits include the complete n4/n5 fixed-locus sums; the inherited plethysm refutation with sharper witnesses and threshold; mixed-characteristic nonfreeness of the actual integral rank-four order; the fixed-q rank-three stalk construction; the canonical-map rank consequences; the outer-six scalar evaluator; and the precise failures of the tested canonical-basis repairs. Consult the question register for each scope.

K-026–K-031 reduce exact dyadic cancellation to an integral coherent class supported only on component closures meeting the higher colliding fixed locus. Every stabilizer exception is removed, and K-029 proves that actual amplified components have the remaining collision property. The class is not determined. PNEW-014 supplies a scoped formal-character countermodel to a strict-index transfer from the listed trace data. N-019 gives a different maximal-scaling rational-order basis, a balanced triple and every12,996 product; the coefficient D−9/2 disproves the requested signed positivity for this basis.

## Reproduction

Python scripts retain exact rational arithmetic and certificates. Core dependencies are Python3, SymPy and, for the nonstandard polynomial-module computations, python-flint. The latter was installed in the task-local `runtime_nonstandard` environment during the run; it is a runtime dependency, not a mathematical certificate. Some source-comparison scripts refer to the supplied archive under `sources/`; place the once-extracted attachment there to reproduce those reads. Do not re-extract the already expanded nested ZIP directories.

The main LaTeX build runs `pdflatex GCT_POS.tex` from this directory; standard AMS, hyperref, geometry, lmodern and URL packages are used. All source fragments referenced by the manuscript are included. The standalone plethysm manuscript and its scripts are under `branches/plethysm/`.

Important exact checks include `branches/kronecker/verify_cyclic_trace_hook.py`, `branches/root/verify_hook_chain_lie.py`, and the modular transfer verifier; the branch review documents identify the larger finite classification and nonstandard order certificates. Check receipts state whether the script was merely constructed, replayed by its author, or independently read and replayed by another reviewer.

## Provenance and timing

Model: GPT-6 Astra Pro. Effort setting: not exposed. Research began21November2026 at20:01UTC/21:01Europe/Berlin. Machine event rows use UTC; user-facing schedules use Europe/Berlin. Checkpoints are created only at the requested45-minute intervals, never overwrite earlier ZIPs and never contain earlier checkpoint ZIPs. The original attachments are not duplicated in the package.

N-020 now also gives the complete abstract sign fibre: dimension114, radical109, split quotient Q⊕Mat2(Q), and a corrected actual parabolic matrix cell. The55-dimensional ambient image is explicitly separated. Exact whole-table and peer proof checks pass.

K-032 identifies the finite normalization and exact graded-piece formula for the amplified collision family in dimensions2+56l. It does not compute its density or the lower Laurent contribution. N-021 gives an all-degree finite reduction for the rank-three cancelling-pair minimum: some minimizer has |e|≤43656·4^7276; the symmetric unimodal class has the direct bound9327. Whole-proof checks and exact implementation replays pass. Neither displayed rank-three score is claimed globally optimal.
