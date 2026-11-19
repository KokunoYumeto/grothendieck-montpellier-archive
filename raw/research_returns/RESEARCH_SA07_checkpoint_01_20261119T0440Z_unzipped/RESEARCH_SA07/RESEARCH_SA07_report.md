INCOMPLETE

# RESEARCH_SA07 research report

## Outcome table

This is the current research state, not a completion certificate. A row containing an unresolved component remains an open item even when some of its statements have been proved or refuted. AI-produced by GPT-6 Astra (OpenAI); no priority claimed.

| Item | Current outcome and proof location |
|---|---|
| A.1 | Typed constructions and both readings proved in `work/agent_triangle.md`; integration underway. |
| A.2 | Real-model strong list false; joint image bounds and explicitly requested period-conjecture implications proved in the triangle record. General unconditional equalities unresolved. |
| A.3 | CM and conjugate-isogenous elliptic cases proved; nonisogenous conjugate flag field remains of transcendence degree 1 or 2. A.3.1–A.3.4. |
| A.4a | CM degree 2 known and derived with exact field normalization. A.4.3. |
| A.4b | Elliptic period-locus generation proved from coefficient de Rham–Betti theorem; `work/agent_generation.md`. |
| A.4c | CM direction proved; h=0 fully classified; nonzero algebraic h for a non-CM curve unresolved. A.4.1–A.4.8 and explicit gate. |
| A.5 | Actual cocycle image criterion proved; replacing actual-image density by generated-subgroup density is false. Generation record. |
| B.1 | Precise good-reduction classifications and counterexamples to unrestricted readings assembled; `work/agent_comparison.md`. |
| B.2 | Rational/relative and integral comparisons assembled with rings and hypotheses; source audit continuing. |
| B.3 | Scope corrections for 18:43 assembled; general real-splitting algebraicity retains A.4c. |
| B.4 | Splitting/cocycle/kernel corrections and Sen comparison assembled. |
| C.1 | Full faithfulness and abelian degree-one image proved; general geometric essential image unresolved. C.1.1–C.1.3. |
| C.2 | Tensor structure and exact torsor obstruction proved; all requested elementary and elliptic cases checked. C.2.1–C.2.2. |
| C.3 | Even-Tate-only claim false; precise replacement and reality/centrality criteria proved in the stated categories. C.3.1–C.3.3. |
| C.4 | Fixed-topology semilinear transport and correct scalar-field interpretation proved. C.4.1. |
| C.5 | Positive Weil form and real-Frobenius invariance proved in the specified polarization convention. C.5.1. |
| D.1 | Relative quotient bound proved; universal equality not established. Lattices record. |
| D.2 | The transcriptions do not define the requested K; interpretations and counterexamples to H5 are recorded. Exact requested value remains unresolved without a specified field. |
| D.3 | Haar-generic cosets, non-CM elliptic open images, products and strong approximation assembled. Lattices record. |
| D.4 | Plain integral functors need not distinguish places; both readings must be tied to E.1/E.2. |
| D.5 | Cocycles/descent/change formulas proved; integral comparison false for a CM ideal; open-closure expectation false for Q(2). |
| E.1 | Finite diagrams and finitely generated fields proved; universal countable integral assertion false; uncountable positive and negative examples proved. E.1.1–E.1.4. |
| E.2 | Plain-functor injectivity refuted in broad generality; full torsor image and all single-M claims remain under audit. |
| E.3 | Labelled integral Hodge data recover embeddings, including j-family; enriched-functor essential image unresolved. E.3.1–E.3.2. |
| F.1 | Global comparison/sign/correspondence proof still being assembled. |
| F.2 | Correct shift is Gr_i^W(E(n))=(Gr_{i+2n}^W E)(n); write-up pending. |
| F.3 | Exhaustive remaining-note audit pending; no unlisted row is treated as settled. |
| G.1 | Companion results table being populated. |
| G.2 | Opened sources and exact locators being merged; historical date gate remains. |
| Lead A | Proved in the pure reductive setting, with exact maps and real GL2 counterexample. |
| H1 | Unresolved after CM direction, zero classification, and exact nonzero-algebraic-value gate. |
| H2 | Joint period genericity implies splitting genericity; asserted equivalence needs a stronger converse not supplied. Full reading audit in triangle record. |
| H3 | Literal identification with Sen's theorem fails; exact algebraic identities and corrected inertia scope proved. |
| H4 | Earliest-written priority unsupported: Nice 1970 already printed the precise problem, while relative manuscript date is unproved. |
| H5 | Literal universal equality claim false under tested precise interpretations; manuscript K itself remains undefined. |
| H6 | Proved for the requested number-field non-CM elliptic cases using opened open-image results, subject to geometric non-isogeny qualifications. |
| H7 | Proved with exact tensor structure; C-isomorphism always and Q-obstruction demonstrated by the sign Artin object. |

## Evidence and scope

Work started 19 November 2026 at approximately 04:55 Europe/Berlin (03:55 UTC). The first timed stagnation review is due at approximately 07:55 Berlin. Working updates before then are not counted as those reviews. Checkpoints are due every 45 minutes of work.

The supplied transcriptions are textual witnesses; manuscript scans were not supplied. Mathematical interpretations and corrections are distinguished from palaeographic readings. Each result specifies its category. In particular an integral realization is formulated on the integral geometric correspondence diagram: a nonzero additive functor from a Q-linear category to free Z-modules cannot exist, since multiplication by every nonzero integer is invertible in the source.

The principal unresolved calculation is algebraicity of the normalized Hodge-splitting scalar h for a non-CM elliptic curve. The proof record contains the exact relation in periods, the CM calculation, the complete zero case, isogeny transport, the chi-star reformulation, and the precise points at which the currently checked transcendence theorems stop. Numerical calculations are diagnostics only.

## Computations

Every mathematical script and its output is retained in `code/` or the checkpoint's `work/code_*` directories. `verify_exact.py` checks exact real-GL2 triangle identities, discriminants, small finite-field point counts, Artin projectors, coboundaries and the polarization identity. `verify_places.py` checks the factorial residue construction, finite scalar-line certificates, unipotent matrix powers and the exact j-family invariants; the infinite assertions have separate proofs and are not inferred from finite tests. Elliptic scripts check the degree-two CM isogeny, nonreal conjugate-isogeny examples, rigorous rational constants in the zero proof, and 80/160-digit numerical consistency. The latter do not certify transcendence.

## Corrections already established

- R2's checked direction holds. Its proposed converse fails for the real Artin sign tensored with Q(-1); C.3.1 gives the exact replacement.
- R3 records internal dimension consistency only. For a real model K=k(alpha), and the strong value g+u fails when u is positive.
- R5 needs the displayed weight-index shift.
- The countable-field path-limit argument requires an actual compatible integral path; finite compatibility alone does not provide it. E.1.2 gives a geometric obstruction and E.1.3 displays the failed inverse-limit step.
- The proposed adelic open-closure conclusion fails already for Q(2), whose finite cyclotomic image is a closed infinite-index square subgroup.
- A general integral Betti comparison on the CM category fails for the nonprincipal ideal (2,1+sqrt(-5)) of Z[sqrt(-5)]. Rational and local comparisons are separately constructed.

## Source and historical checks

Original sources inspected include Deligne–Milne (corrected 2012), Charles–Schnell, Katz 1976 Question 4.0.8, Masser 1975 Appendix One, Schneider 1937 section I result IIc, Chudnovsky's ICM 1978 section 2A, and the exact sources in the agent proof records. Bibliography status and full locators are being consolidated; an unfinished citation audit is not represented as complete.

Grothendieck's Nice 1970 address, printed p.435, asks how to recover the generic-fibre Galois representation from the filtered Dieudonne module and conversely. His 1966 article's note10 concerns algebraic relations among elliptic periods and quasi-periods. The latter does not supply the claimed local-comparison priority. No relative dating of manuscript leaf18:5 and the Nice address has yet been proved.

## Typesetting audit

The current 41-page integration build completed in LuaLaTeX. One overfull box of 11.73135pt was repaired by breaking the computation-file sentence; final overfull count is zero, with no missing characters or undefined citations. Pages 1, 8, 15 (the repaired overflow), 22, 31, 37 and 41 were rendered and visually inspected. The runtime needed a local format and the official luaotfload/lualibs/lua-uni-algos dependencies; these are reproducible runtime dependencies, not mathematical evidence. Subsequent added sections will receive a new build check.

## Dropped or superseded work

No mathematical obligation has been dropped. Temporary compiler files, downloaded reference sources, rendered page samples and supplied attachments are excluded from checkpoints; source identities and locators are retained. The manuscript scan dates and ambiguous readings remain explicitly qualified.

### First checkpoint integration

The integrated Part A triangle expands the paper to 50 pages. The final log still has zero overfull boxes, zero undefined citations and zero missing characters. Additional pages 3, 5, 7 and 9 were rendered and inspected for the triangle tables and displays. Parts B and F remain openly pending in the PDF; the complete current Part B proof record is included as work/agent_comparison.md.
