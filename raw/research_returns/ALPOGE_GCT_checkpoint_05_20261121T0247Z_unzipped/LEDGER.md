# ALPOGE_GCT research ledger

Started 21 November 2026, 00:02 CET (20 November 2026, 23:02 UTC).

This ledger records actual progress; it is not a claim that open problems are solved. Supplied Alpoge and ETH results are cited premises with their exact stated scopes. No Lean kernel build has been performed: imported proof modules and a Lean executable are absent from the supplied working set.

## Initial gates

| Question | State | Strongest gate / next approach |
|---|---|---|
| Main positivity transfer | Open | Identify the exact positivity object and an equivariant/categorical map to multiplicity spaces; distinguish PH0, PH1, PH2 and SH. |
| Homogeneous Ehrhart PH1 | Literature counterexample located | Match Kahle–Michalek Theorem 5 to GCT VI Hypothesis 1.6.4, including fixed inner weight. |
| Revised positivity/saturation | Open | Inspect revised hypotheses, counterexamples, complexity restrictions and possible shifted-polytope models. |
| GCT obstructions | Open | Compare actual coordinate-ring multiplicities, account for no-occurrence theorem. |
| Grothendieck plethysm | In progress | Read all transcriptions; verify Burnside identities and Chow natural-map rank. |
| GRH consequences | In progress | Match Dirichlet versus Dedekind hypotheses. |
| ETH consequences | In progress | Track fixed-k quantifiers, reduction sizes and circuit/algebraic class distinctions. |
| Other bridges | In progress | Exact K-positivity, norm and approximation statements; integral specialization. |

## Review schedule

Checkpoint ZIPs are due after each 45 minutes of actual work, starting approximately 00:47 CET, with immutable numbered names. No checkpoint has yet been made. Progress reviews are due after about three hours, then hourly. The two consecutive no-movement stopping rule will be applied if reached.

## Events

- 2026-11-21T00:05:18.339201+01:00: Initial sources extracted once; manifest recorded. Parallel branches launched for plethysm, complexity, and other bridges. Root owns the main positivity question.

## Progress by 00:45 CET (approximately 43 minutes of work)

The following are actual gate changes in this run, not a scheduled three-hour review.

| Main question | Current state | Movement and next gate |
|---|---|---|
| Literal homogeneous PH1 | Refuted, cited counterexample checked | Matched the exact fixed-inner stretch; P-F1 now supplies the minimal-dimensional shifted repair. |
| Revised PH3 to PH2 | Proved implication | P-F11's explicit polynomial modular-index bound and P-F12's Weyl growth argument replace the previous missing implication. Next: prove PH3 in the GCT family and construct its data. |
| Positive Hilbert data to counting | Proved | P-F2 gives one shifted convex polytope; P-F12 bounds description size under PH3 in expanded group parameters. Uniform construction and compressed-input bounds remain. |
| Pure geometry to homogeneous PH1 | Refuted as a general transfer | PLE-F5/F7 identify the same normal invariant cone, its PH1-violating Hilbert function and pure even Tate ordinary/IC cohomology. |
| Purity to quantitative indices | Refuted without grading bounds | P-F10 gives exact indices ab-a-b on a fixed smooth affine plane; P-F7 gives the pure finite-scheme #3SAT reduction. |
| Nonstandard quantum groups | Open | A specified graded category, basis/product/specialization identification, and quantitative control remain required; P-F6 states the sufficient criterion. |
| Actual GCT obstruction | Open | P-F8 and PL-06 reduce to strict actual quotient-multiplicity comparison or rank/separating-equation data. No family separating determinant and permanent has been constructed. |
| Archive identities | Proved/corrected/refuted item by item | PL-01–PL-08 distinguish equivariant versus cardinality identities, three products, characteristic-zero versus modular categories, and actual map ranks. |
| Dirichlet GRH consequences | Exact scope settled; HN gate open | C-GRH-01 gives cyclotomic subfields; C-GRH-03 prevents forcing every HN solution into that family. Bach/Miller rational-field bounds are discharged. |
| ETH consequences | Proved quantitative deductions | Fixed-width hypotheses, parsimonious verifier size, sparse signed permanent precision, and finite-field PIT are tracked; no polynomial-time or ordinary VP/VNP conclusion is substituted. |
| Other bridges | Ten proved deductions | K-theoretic dilation counterexample, norm/approximation limitations, and integral specialization with a fixed-degree rank test. |

### Approaches and checks

- Tested scalar signs, compact averaging determinants, standard interlacing, categorical positivity, smooth proper pure Tate examples, the exact invariant cone, and varying gradings. Their precise failures and next steps appear in Part II of the paper and IMPLICATIONS.md.
- Pursued positive Hilbert series beyond the initial common-period bound. The partial-fraction/Cauchy argument gives a polynomial bound in the numerical modular index; two independent agents reconstructed the whole proof, and a third subsequently checked it. This is substantive movement of the main positivity gate.
- The printed positive-form numerator index in GCT VI was not silently used as a degree bound. P-F12 proves the KM counterexample to that literal restriction and uses the correct unrestricted numerator with degree less than the denominator degree.
- Corrected during checking: the higher-ambient dimension-one exclusion in P-F1; specialization precisely at v=1 in P-F6; a rank-one Frobenius example in the parity discussion; Sym² described as a homomorphism; the KL source locator; the Weil II purity corollary number; lambda-ring unit axiom; h55 dimension and recent two-row formula scope. Earlier failed or qualified checks remain in the register.
- No Lean build was attempted or claimed. Finite computations are recorded separately from proofs. All completed findings have whole-proof readings; additional independent checks are retained by their actual type.
- A transient tool-runtime replacement occurred at about 00:42 CET. Files remained available; the completed TeX build log was inspected rather than blindly repeating a mutation. A missing TeX font mapping was repaired for PDF production. This was an execution issue, not a mathematical change.

### Next main approach in progress

Examine fixed-embedding multigraded branching rings: whether finite generation gives a uniform diagonal generator-degree bound, and which numerical generator/minor bounds would make PH3 effective. This work has not yet been promoted to a checked finding. It directly targets the remaining modular-index gate.

The first 45-minute checkpoint is due at approximately 00:47:04 CET. The three-hour review is not yet due. No claim is made that the requested no-movement stopping rule has been triggered.

- 2026-11-21T00:47:18+01:00: First 45-minute checkpoint assembled as ALPOGE_GCT_checkpoint_01.zip; includes the current standalone paper, all five required deliverables, authored proof/audit/computation files and supplied sources. PDF compiles (47 pages); final visual QA is still pending. P-F13 and the fixed-embedding generator-degree approach are in progress and are not yet asserted as checked findings.

## Progress by 01:30 CET (approximately 88 minutes of work)

This is a substantive progress entry, not the scheduled three-hour review.

| Main question | Changed state and strongest current gate |
|---|---|
| Canonical modular-index clause of ordinary plethysm PH3 | **Refuted by P-F19.** With fixed inner shape (3), the chain cubic forces every h.s.o.p. of the actual canonical multiplicity algebra to contain a stretch degree at least 2^(n-1), while the hypothesis parameter is O(n6). Both coefficient-weight and stabilizer proofs were fully checked by all four agents. |
| Weaker numerical positive-form clause | Still open. A positive Hilbert expression need not come from parameters of the canonical algebra. P-F11–P-F12 remain a valid sufficient route from this weaker clause to PH2. The new task is numerical poles/positive forms or a direct PH2 argument. |
| Broad subgroup-restriction PH3, PH2 and SH(a) | **Refuted by P-F14–P-F15.** Faithful torus embeddings with fixed rank produce denominator lower bound N or exact positivity/saturation index N-2. The density assertion SH(b) is not refuted. |
| Fixed-embedding uniformity | **Proved by P-F16–P-F17.** A single positively multigraded branching domain contains the actual canonical ray algebras; minor bounds give bounded ray generators, common-degree parameters and finite index bounds. A separate parameter-prefix extension argument controls the lexicographic modular index. |
| Fixed inner dimension in ordinary plethysm | **Proved by P-F18.** Weyl monotonicity bounds n and normalized highest-weight differences by m, leaving finitely many semisimple embeddings. The optimal canonical envelope is finite but has P-F19's exponential subsequence. |
| Finite construction/verification under bounded denominator data | **Proved by P-F13.** A prefix of length R A(A+1)/2 determines the rational series under the stated promise. Exact identity checking verifies proposed positive forms. Neither the coefficient oracle nor efficient denominator selection is supplied. |
| Purity counterexample as actual multiplicity algebra | **Strengthened by PLE-F8.** Explicit covariants identify the binary-dihedral ring with the actual canonical highest-weight multiplicity algebra, including its Cartan multiplication. It has a positive multiplicative basis, a flat integral model and the pure Tate fibers of PLE-F7, but violates homogeneous PH1. |

### New approaches, corrections and checks

- The fixed-embedding proof was strengthened twice during checking: equal Hilbert functions were replaced by a graded algebra isomorphism, and mere existence of an all-L h.s.o.p. was supplemented by a prime-avoidance completion argument for each parameter prefix. This is necessary to bound the lexicographically minimal degree sequence used in the source.
- The GL-to-SL reduction explicitly keeps the external grading for determinant characters and checks central balance. P-F18 is an ordinary GL_n statement; it does not silently cover every reductive group in Problem 1.1.2.
- Source wording around PH3 has an introductory S/T inconsistency. The precise canonical T algebra and modular-index definition in Sections 4.1.1–4.1.2 are used, with the inconsistency disclosed.
- P-F19's chain family and discriminant are supported by directly inspected primary sources. Busé–Jouanolou Example 4.12 already contains the chain form, attributed there to Demazure. No historical novelty claim is made.
- Tried to transfer a large period in a fixed-target covariant series to a simultaneous stretching ray through piecewise quasi-polynomiality. This general inference fails: for M a power of two, 1+1_{b odd and M divides a} has period at most two on every integer ray, but period M on the slice b=1. Independent agents found both this example and a trigonometric period-four variant. Additional algebraic structure is required; this route is still under investigation.
- A large canonical parameter degree is not treated as a large pole of the ordinary Hilbert series. The universal denominator controls quotients and covariant modules; those distinctions are being investigated directly.
- Current standalone PDF compiles to 68 pages. Final visual QA is pending. All newly stated findings through P-F19 and PLE-F8 have complete proof readings; finite symbolic checks remain separately labelled.

The second checkpoint is due at 01:32:04 CET. The first scheduled three-hour review is due at approximately 03:02 CET and has not occurred. There has been substantial mathematical movement since the first checkpoint; the no-movement stopping rule has not been triggered.

- 2026-11-21T00:32:05.577714+00:00: Second 45-minute checkpoint assembled as ALPOGE_GCT_checkpoint_02.zip. Includes the checked findings through P-F19 and PLE-F8, current standalone 68-page PDF, all required deliverables, proof/check notes, scripts and supplied sources. Original checkpoint01 is untouched; no checkpoint ZIP is nested. Final visual QA remains in progress.

## Progress by 02:11 CET (approximately 129 minutes of work)

This is a progress entry before the third checkpoint, not the scheduled three-hour review.

The main open numerical-positive-form gate has become strictly smaller. P-F23 supplies a checked local-to-global noncancellation criterion. P-F24 proves full chain stabilizers, quotient smoothness and a one-dimensional fixed component. P-F26 identifies the entire smooth-hypersurface fixed locus with the chain orbit and supplies finite two-power lifts for every nonzero fixed quotient point. P-F27 then excludes every graph-support competitor, including rank-deficient support lattices and larger-order lifts. Only singular polystable boundary representatives with three-distinct-variable support remain on this classification route. Their total contribution is not yet controlled.

P-F20 proves the universal factor and fixed-target covariant pole but also gives exact-transfer counterexamples, including a connected semisimple factorial rational Gorenstein invariant ring. P-F21–P-F22 refute generic quantitative parameter-to-series transfers even with fixed Hilbert series and Gorenstein geometry. These are proved limitations of particular approaches, not a negative solution of the weaker ordinary plethysm PH3 clause. P-F25 gives a checked binary support classification and finite lcm parameter bound, with the off-residue strict-saturation issue explicitly retained.

Whole proofs of the new findings have been read by the author and independent agents; actual events and source reads are recorded in CHECK_EVENTS.tsv. No Lean build is claimed. All 68 pages of the preceding PDF were rendered and inspected as five contact sheets without clipping or overlaps; the sparsely filled third table-of-contents page led to a more compact contents layout. The expanded paper is being rebuilt for this checkpoint. A source gap in an unused binary-degree-12 h.s.o.p. claim is quarantined in a separate note; no such claim enters the paper.

The third 45-minute checkpoint is due at 02:17:04 CET. The formal three-hour review remains due at approximately 03:02 CET. The stopping condition has not been triggered.

Further refinement before checkpoint03: P-F27's connected-graph extension excludes mixed supports whenever their square-linear graph is connected. P-F29 excludes supports with only cubes and squarefree triples. Thus any boundary competitor must have a disconnected graph part and contain both square-linear and three-distinct-variable monomials. P-F28 computes the chain's regraded multiplicity as one for all n>=4 and its local coefficient valuation as binom(n+2,2)-3*2^(n-1). No global dominance or ordinary-series pole follows without the remaining comparison. These refinements have complete proof readings and independent reviews. The 89-page intermediate PDF was rendered and every page inspected in six contact sheets; no clipping or overlap was seen, and the single line overflow was corrected.

- 2026-11-21T01:17:06.649519+00:00: Third 45-minute checkpoint assembled as ALPOGE_GCT_checkpoint_03.zip. Includes the checked paper through P-F29, the 94-page PDF, all required deliverables, authored proof and audit files, actual exploratory search code/results, visual QA contact sheets and supplied sources. P-F30, a proposed full support contraction argument, has just emerged and is IN PROGRESS, not a theorem in this checkpoint. Earlier checkpoint ZIPs are untouched and are not nested.

## Progress at 02:37 CET (approximately 155 minutes of work)

This is a substantive progress entry, not the scheduled three-hour review.

**The numerical PH3 row is now refuted, and the fixed-component row is proved.** P-F30 classifies all cubic supports that span the all-ones vector and admit a finite two-power exact-form stabilizer of extremal determinant order 2^(n-1). Equality forces the smooth chain. The proof covers rank-deficient support matrices, disconnected square-linear graphs, mixed squarefree triples and arbitrary two-power lift order. The author and three independent readers have read the entire proof.

P-F31 uses that theorem to show that the grading-fixed quotient scheme is supported only on the chain curve. The ambient quotient is smooth along its nonzero orbit. P-F23 and P-F28 give an actual simple pole at each primitive2^(n-1) root, with a nonzero explicitly valued leading coefficient. Possible origin-supported structure cannot cancel a one-dimensional contribution. Every rational expression with polynomial numerator and factors1-t^a in the denominator therefore has a divisible weight a>=2^(n-1), whereas the printed PH3 parameter is O(n6). This refutes the first numerical positive-form clause as well as the canonical clause already refuted by P-F19. Complete proof readings, primary-definition checks and independent reviews are recorded in the check register.

**The remaining main gate is now direct narrow PH2/SH or a different constructive counting hypothesis.** The valid P-F11-P-F12 implication cannot use the false printed PH3 premise to settle PH2. Large period alone is not a lower bound for a positivity or saturation index. P-F32 supplies an exterior-power complement identity and an infinite family with exact first positive stretch of order sqrt(n); all constituents are shown nonzero before deriving the strict-index lower bound. Its whole proof and sources passed independent review. This is useful direct information, but it does not close the polynomial upper-bound gate and is not counted as such movement.

The paper, current-state questions and implications have been updated; prior dated ledger entries remain unchanged as history. No extra checkpoint is saved at this time. Checkpoint04 and the first scheduled three-hour review remain due at approximately03:02CET (02:02UTC). The stopping condition has not been triggered.

## First scheduled three-hour review — 2026-11-21T02:02:05.312637+00:00

Movement: YES. Existing main ordinary numerical PH3 row is now REFUTED by the complete P-F30/P-F31 fixed-support and actual-pole proof. The former singular-boundary gate is closed. Narrow PH2/SH remain open with the sharper sufficient P-F34 limsup(log2 U_n)/n^4<1/24 gate, not a proved bound. P-F36 gives the exact quadratic descent requirement and P-F37 the fixed-dimensional automorphic dictionary. P-F33/P-F38 generic countermodels and P-F32/P-F35 calibrations are not counted as additional main resolutions.

Every open or partial row is reviewed in FORMAL_REVIEW_03H.md. Continue; consecutive scheduled reviews without main movement=0. Next formal review03:02:04UTC. No Lean build was performed. The corrected discriminant source reading and all actual proof checks remain in CHECK_EVENTS.tsv. Checkpoint04 contains the120-page checked paper through P-F38 and working files including the unintegrated P-F39 draft. Next45-minute checkpoint02:47:04UTC.


## Checked progress after the three-hour review — 2026-11-21T02:31:01.617250+00:00

P-F39 through P-F45 have complete proofs and are integrated into the paper. The nonstandard coefficient now has an exact normalization, trace/norm character models and an actual positive operator; comparison with the nonstandard modules remains open. P-F41 identifies the weight48 Borcherds form with the degree80 discriminant in the actual T5 algebra, closing the previous unnamed-output stage of the theta route. P-F45 proves the full cyclic-cover domain is a ball exactly at n4,5, without excluding other constructions.

P-F42 supplies an unconditional actual cubic norm upper bound with logarithmic quartic constant log2(3)/6, which remains above the sufficient1/24 threshold. P-F44 closes the earlier local-to-global comparison for the primitive Klein collection: B_n=K_n+R_n with an explicit balanced-cone remainder and a signed cyclotomic trace. The trace cancels for odd D; exact finite certificates give K4=1/25, K5=2/121 and K8=-624/85. No full U_n lower bound follows. The signed remainder estimate remains open.

P-F43 resolves B12-Q1 by a complete actual parameter-system counterexample with explicit degrees. This is a source-audit resolution and is not counted as an asymptotic main positivity resolution. All older quarantine and review records are preserved as history. The next formal movement decision remains at03:02:04UTC; this entry does not replace that review. Checkpoint05 remains due02:47:04UTC, with no intervening ZIP saved.


## Checkpoint05 preparation — 2026-11-21T02:45:43.207563+00:00

The checked paper now has153pages through P-F46, including the exact unitary Borcherds lift and all lattice hypotheses. The supplied iterated definite-unitary comparison is still open, now with a named positive input, regularized multiplicative operation and discriminant output. P47 and P48 are separate working fragments; their source locators/encoding conventions are being independently audited. A new actual Hessian/Cayley Fermat-nonvanishing route is under investigation and is not promoted as proved here.

All main index and obstruction gates remain explicit. No Lean build was run. The next scheduled review is03:02:04UTC; the previous formal stagnation counter is0. Checkpoint05 is due02:47:04UTC; the following checkpoint is03:32:04UTC. This preparation entry does not assert a save before its scheduled time.
