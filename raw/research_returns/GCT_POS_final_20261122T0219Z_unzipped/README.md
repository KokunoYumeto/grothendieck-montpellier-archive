# GCT_POS research package

**Final status: INCOMPLETE original programme; research stopped under the requested two-review rule at02:01UTC on22November2026.** Numerical PH3 is refuted for all triple rectangles. The exact primitive-dyadic pole and the strict tensor PH2/SH(a) bounds remain unresolved. The reviews at01:01UTC and02:01UTC both recorded no qualifying movement. Final verification and presentation of existing work followed that stop; no new research was undertaken.

Read `FINAL_STATUS.md` for every question's outcome, the attempted routes, their precise limitations and concrete next steps. It distinguishes a completed scoped theorem from a solved original question.

This continuation uses the supplied prompt and the once-extracted source archive. Its mathematical status is recorded per question in `QUESTIONS.tsv`, with dated movement reviews in `LEDGER.md`. The paper includes only findings whose complete proofs have received recorded checks. Exploratory files remain explicitly labelled; an arithmetic pass alone is not a proof of a general conjecture.

## Read first

- `GCT_POS.tex` and `GCT_POS.pdf`: final integrated paper, with checked findings and a separate part for unchecked observations and unresolved gates. The final PDF is rebuilt from the included source; historical checkpoint PDFs may lag their latest source additions.
- `QUESTIONS.tsv`: each requested question and its proved result, refutation or remaining gate.
- `CHECK_EVENTS.tsv`: proof readings, independent reconstructions, computations and source checks, with actual scope. Imported branch records preserve provenance and may also describe a check recorded directly by the root; rows are not a count of independent proofs.
- `SOURCE_AUDIT.md`: exact inspected literature locators, known-result attribution and access limitations.
- `IMPLICATIONS.md`: consequences for GCT and the separate Grothendieck dictionary.
- `reviews/`: detailed whole-proof and computational receipts, plus formal movement reviews.

## Main checked results

Numerical PH3 is false for triple-rectangular Kronecker coefficients: for every n≥2 an actual Hilbert pole has order2^(n−1)·3^r for some r≥0. Every product denominator therefore contains an exponent at least2^(n−1), versus unified parameter rank(x)=n²+5n (and also the introductory h=n⁴+O(n)). The exact dyadic pole and strict positivity/saturation index bounds remain open in variable dimension. The proof is K-023, R-NEW-004, K-024 and PNEW-013.

Other checked results and their limits include the complete n4/n5 fixed-locus sums; the inherited plethysm refutation with sharper witnesses and threshold; mixed-characteristic nonfreeness of the actual integral rank-four order; the fixed-q rank-three stalk construction; the canonical-map rank consequences; the outer-six scalar evaluator; and the precise failures of the tested canonical-basis repairs. Consult the question register for each scope.

For n≥4, K-026–K-031 reduce exact dyadic cancellation to an integral coherent class supported only on component closures meeting the higher colliding fixed locus. Every stabilizer exception is removed, and K-029 proves that actual amplified components have the remaining collision property. The class is not determined. PNEW-014 supplies a scoped formal-character countermodel to a strict-index transfer from the listed trace data. N-019 gives a different maximal-scaling rational-order basis, a balanced triple and every12,996 product; the coefficient D−9/2 disproves the requested signed positivity for this basis.

## Reproduction

Python scripts retain exact rational arithmetic and certificates. Core dependencies are Python3, SymPy and, for the nonstandard polynomial-module computations, python-flint. The latter was installed in the task-local `runtime_nonstandard` environment during the run; it is a runtime dependency, not a mathematical certificate. Some source-comparison scripts refer to the supplied archive under `sources/`; place the once-extracted attachment there to reproduce those reads. Do not re-extract the already expanded nested ZIP directories.

The main LaTeX build runs `pdflatex GCT_POS.tex` from this directory; standard AMS, hyperref, geometry, lmodern and URL packages are used. All source fragments referenced by the manuscript are included. The standalone plethysm manuscript and its scripts are under `branches/plethysm/`.

Important exact checks include `branches/kronecker/verify_cyclic_trace_hook.py`, `branches/root/verify_hook_chain_lie.py`, and the modular transfer verifier; the branch review documents identify the larger finite classification and nonstandard order certificates. Check receipts state whether the script was merely constructed, replayed by its author, or independently read and replayed by another reviewer.

## Provenance and timing

Model: GPT-6 Astra Pro. Effort setting: not exposed. Research began21November2026 at20:01UTC/21:01Europe/Berlin. Machine event rows use UTC; user-facing schedules use Europe/Berlin. Checkpoints are created only at the requested45-minute intervals, never overwrite earlier ZIPs and never contain earlier checkpoint ZIPs. The original attachments are not duplicated in the package.

N-020 now also gives the complete abstract sign fibre: dimension114, radical109, split quotient Q⊕Mat2(Q), and a corrected actual parabolic matrix cell. The55-dimensional ambient image is explicitly separated. Exact whole-table and peer proof checks pass.

K-032 identifies the finite normalization and exact graded-piece formula for the amplified collision family in dimensions2+56l. It does not compute its density or the lower Laurent contribution. N-021 gives an all-degree finite reduction for the rank-three cancelling-pair minimum: some minimizer has |e|≤23388·4^3898 after the N-024 improvement; the symmetric unimodal class has the direct bound9327. Whole-proof checks and exact implementation replays pass. The minimum over all tables is not claimed computed.

K-033 evaluates a different actual n10 component normalization: its series is (1+91067z+429033z²+416212z³+78249z⁴)/((1−z)^4(1+z)), z=t^512, with density507281. Root and peer whole-proof checks and the exact replay pass. This alone leaves the conductor and moving lower class open. R-DIAG-001 is a separate checked hypersurface example ruling out a proposed free-cyclic-action integrality shortcut.

N-022's4194 construction (bottom3614) is retained with its complete tables and verification. N-024 now proves exact all-degree minima3898 and4046 in a precisely specified Laurent family, respectively without and with bar invariance. The bounds also hold when its common cell scale is an arbitrary Laurent polynomial, with the other displayed relationships fixed. Each minimum has at least two distinct attaining tables. The3898 witness is an unrestricted upper bound and reduces the global finite-search exponent bound to23388·4^3898, a7811-bit integer. The separate unimodal upper bound remains9040. No global all-table optimum or categorical selection is claimed.

K-035 resolves the remaining incidence issue for K-033’s three n10 component closures: every nonzero grading stabilizer is μ512 or μ1024, including points of the conductor. None is among the components indexed in K-031’s collision support; the actual amplified collision family of K-029 is still unresolved. The complete proof, all536 balance vertices and all64 boundary kernels have root verification.

N-023 gives an all-degree obstruction to an ordinary positive split-Hecke comparison for every ten-label rank-three dimension ring with the stated effective sign–Tate evaluations. Two required images generate an algebra with an eleven-dimensional quotient. Derived/Koszul comparisons with virtual dimension classes remain open. PNEW-015 separately gives a conditional actual tensor coefficient-norm dichotomy; its coefficient upper bound is not proved.

PNEW-016 proves dim X_n^(μ_(2^(n−1)))≤n³/5 for n≥2000, including all stabilizer dimensions. A constituent shift removes every wave with smaller two-primary order, so the remaining actual covariant difference has degree at most n³/5−1. For n≥79004, either both tensor indices have the stated2^(n/16) lower bounds or its positive coefficient mass is at least2^((17/240)n⁴−6n³−4). The required upper bound on this smaller-degree oscillatory difference remains unproved. The full proof, exact calibrations, independent peer review and source-scope correction are retained.

K-036 gives a uniform geometric full-inertia criterion for rank-two fixed models, replacing the finite boundary enumeration under explicit frame subset-sum hypotheses. It applies to four-dimensional μ_D components in dimensions3+7k. At k>1 the order D exceeds the originally targeted M_n, so such a component can lie properly inside a larger target component; the global collision gate remains.

K-037 constructs an actual13-dimensional target-order collision component at n18 and computes a finite coherent module on its higher fixed locus. Its exact quadratic graded dimensions give a cyclic orbit module whose simple coefficient is4531295468/9 at a primitive2^17 root in the parameter1−t^(2^17). Thus arbitrary coherent orbit classes on the actual collision support need not be integral at3. This class is not identified with the specific exceptional moving Koszul class, and no global tensor pole follows from this calculation.

K-038 proves that the higher-order three-dimensional locus in this construction is an actual fixed component with the K-037 ring as its normalization. The displayed critical tensor has full stabilizer S times mu_(3D), D=2^17; the component's top density is9063377350. The moving leading coefficient has three-adic valuation-5 in1−t^(3D), or-8 in1−t/xi. Both full proof readings and exact replays pass. The global odd-root sum and the target-dyadic exceptional class remain uncomputed.
