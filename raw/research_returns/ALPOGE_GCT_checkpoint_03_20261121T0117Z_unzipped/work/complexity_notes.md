# Complexity branch: findings, evidence, and remaining gates

Recorded 20 November 2026 UTC by GPT-6 Astra Pro, effort inherited/undisclosed, run `/root/complexity`.

## Deliverables

- `complexity.tex`: the GRH and ETH sections, with complete proofs of every newly derived statement.
- `complexity_bib.tex`: bibliography entries with exact theorem/section locators and primary-source URLs.
- `complexity_checks.tsv`: 33 actual check events, including all five supplied Alpöge declarations, every proof in this branch, and independent checks of P-F1, P-F2 and P-F7.
- `complexity_questions.tsv`: 23 questions with proved, refuted, or current-gate states.
- `complexity_computation.py` and `complexity_computation.json`: finite encoding checks; these are not formal proof certificates and do not execute the supplied ETH algorithm.
- `cross_positivity_checks.tsv`: additional independent whole-proof reviews of P-F3 through P-F15, with the prose parity issue recorded separately.

The parent agent owns the combined paper, global ledger, checkpoint timing, final ZIP, and persistence. These files are isolated branch contributions.

## High-impact conclusions

**The analytic quantifiers do not match automatically.** The supplied `DirichletLZerosOnLine` quantifies over every positive modulus and its Dirichlet characters. C-GRH-01 passes it to Dedekind zeta functions of cyclotomic subfields by an explicit local-factor proof, including ramification. Koiran's general primitive-element fields need not be abelian. His DIMACS long version, Theorem 2, uses the arbitrary-field prime-ideal input in Section 5, Theorem 9 and Corollary 1. His 8 August 1997 erratum corrects Theorem 8, leaving Theorems 1 and 2 intact. A missing premise is not a proof that the logical implication is false.

**GCT V has separate inputs.** The Koiran-based PH/EXPH bounds inherit that analytic gate. Theorem 4.1 additionally assumes that defining equations are computable in exponential time. The strengthened PIT and border-hardness hypotheses in Theorems 4.9 and 5.11 are different hypotheses. A theorem about zeros of Dirichlet L-functions does not provide the required hitting set for limits of small circuits.

**The rational Miller/Bach bounds do pass.** Bach Section 6 explicitly treats Dirichlet characters. The witness bound is `2(ln m)^2`; the least-unit-outside-a-subgroup bound is `3(ln m)^2`. Keeping those constants separate is necessary. General-number-field Theorem 4 remains outside the stated Dirichlet quantifier. Primality was already in P by AKS.

**Fixed-k is enough for standard SETH.** For every fixed k the exponent is o(n). Fixing one epsilon, for example 1/2, works for every fixed k, each with its own algorithm and threshold. This negates standard SETH. It does not give a useful bound in the original variable number for arbitrary growing-width encodings. C-SIZE-01 records the actual incidence-size bound.

**The count-to-GCT bridge is size-sensitive.** C-COUNT-01 transfers a positive verifier of size B to time `poly(B) 2^{O(B/sqrt(log B))}`. Constructing such a positive verifier for a representation coefficient is a separate hypothesis. A polynomial blowup B=O(L^a) does not imply subexponential time in L when a>1. The direction of the reduction matters.

**The supplied tensor method handles signed sparse permanents.** C-COUNT-02 gives a concrete new derived evaluation bound with effective size `S=max(2,E+n(b+1))`. Its exact-one gadgets are ternary, bipartite subdivision preserves the contraction, and a modulus with `P=E+nb+2` bits suffices for signed recovery. For dense bounded-entry matrices S is quadratic in n, giving an exponent worse than the existing exponential formula in Landsberg Section 8.2, equation (22). This does not construct symbolic polynomial-size arithmetic circuits.

**Neither modular arithmetic nor purity provides an efficient positive coefficient model.** C-SIGN-01 explicitly refutes the sign inference from modular contraction. The new positivity-family constructions elsewhere in the paper must supply their own coefficient identification, basis, parity, size, and orbit-boundary extension data.

**A recent paper already studies the arithmetic connection.** Chukhin–Gajulapalli–Golovnev–Mihajlin, arXiv:2611.07972v1 / ECCC TR26-313, Theorems 1, 5 and 6, is included as cited current background. Theorem 6 and its page-9 discussion explicitly compare the supplied SAT algorithm with a faster protocol gate. The theorem requires a nondecreasing, polynomial-time computable size bound s with s(N)<=2^N eventually. No claim that the connection was previously unconsidered is sustainable. Its constant-free integer disjunction does not identify either branch or settle the characteristic-zero GCT separation.

## What was proved here, and what it changes

| ID | New derived statement or checked form | Consequence for the main goal |
|---|---|---|
| C-GRH-01 | Dirichlet GRH passes to cyclotomic-subfield Dedekind zeta functions. | Enlarges the named analytic family; leaves arbitrary Koiran fields as the precise gate. |
| C-GRH-03 | The feasible instance x^3-2=0 has no solution in a finite abelian extension. | Refutes the universal restriction of HN solution fields to the cyclotomic-subfield case. |
| C-GRH-02 | Instantiates the Miller/Bach rational bounds with the supplied theorem. | Discharges those conditional witness guarantees; no new P versus NP separation. |
| C-SAT-01 | Full quantifier proof for ETH/SETH and related refutations already stated in the supplied paper. | Avoids a false growing-k requirement. Not claimed as a new source result. |
| C-COUNT-01 | Parsimonious verifier counting transfer with explicit Boolean size. | Applies when a positive coefficient verifier is independently available. |
| C-COUNT-03 | Constructive parsimonious #3SAT completeness through local computation tableaux. | Supplies the completeness fact used in P-F7 without an unspecified completeness citation. |
| C-SIZE-01 | Arbitrary-width counting in incidence size; near-linear incidence threshold for o(n). | Replaces an unjustified original-n conclusion by a proved quantitative range. |
| C-COUNT-02 | Signed weighted sparse permanent evaluation through bounded-degree contraction. | Improves the sparse evaluation range under the supplied theorem, with precision accounted for. |
| C-PIT-01 | Bounded finite-prime-field PIT in Boolean evaluation size. | Gives a conditional test, with no polynomial-time or border hitting-set conclusion. |
| C-SIGN-01 | A negative integer contraction has a positive canonical residue. | Refutes one proposed positivity transfer outright. |

Historical priority is not claimed for these elementary deductions. The user-requested novelty condition cannot be established by a finite literature search.

## Approaches tried and why the stronger conclusion did not follow

1. **Direct GRH instantiation:** read the actual Lean types, not just the theorem names. It works for rational Dirichlet applications. It stops at the arbitrary number fields used by Koiran. C-GRH-01 proves the largest explicit extension developed in this branch.
2. **Effective Chebotarev/prime-ideal replacement:** traced Koiran's proof to the exact root-mod-p discrepancy estimate and checked the erratum. Rojas Theorems 1 and 2 give weaker sufficient alternatives, DZH and GIPIT. Neither is supplied for arbitrary fields; this is the remaining analytic gate.
3. **GRH as a PIT derandomizer:** inspected GCT V's theorem-by-theorem hypotheses. The hierarchy bounds and the strengthened hitting-set assumptions are separate. No valid substitution was found, and no invalid logical nonimplication is claimed.
4. **ETH failure as a blanket fine-grained collapse:** checked quantifiers and reduction directions. This refutes the hypotheses, not every consequence previously derived from them. An algorithm transfers only through a target-to-SAT reduction with its quantitative blowup controlled.
5. **Generic NP/#P reduction:** proved the parsimonious gate construction and local verifier tableau explicitly. It gives a cost in witness-plus-circuit size; an arbitrary polynomial blowup cannot be erased.
6. **Permanent evaluation via the actual contraction interface:** constructed ternary exact-one gadgets and signed modular recovery. The method succeeds for sparse weighted matrices. It does not improve dense order-n evaluation because the effective wire count is quadratic.
7. **Finite-field PIT through exact counting:** obtained C-PIT-01 with the necessary degree<p hypothesis. The standard counterexample x^p-x explains why evaluation at all base-field points otherwise fails to distinguish formal polynomial zero.
8. **Contraction as a positivity certificate:** evaluated the smallest signed network. The proposed general sign inference fails. The source's modes are eliminated by divisibility and recovered by Hermite interpolation; no Schur basis or geometric category is built by that procedure.
9. **Arithmetic circuit lower bounds after ETH:** read the supplied circuit section and the newer primary CGGM paper. The supplied lower bound is Boolean and lies in E^NP. The newer trade-off requires a lower bound against a more powerful, faster input-oblivious MA protocol. The deterministic supplied algorithm itself is an empty-message protocol at its slower time scale.
10. **Global novelty:** a current primary source already discusses the ETH/arithmetic bridge. The report therefore gives exact cited results and local deductions, without claiming that nobody has considered the connection.

## Exact source map and retrieval notes

The supplied source folders remain authoritative for the requested premises. Retrieved research files are in `complexity_sources/`.

| Source | Exact locators used | Retrieval/provenance |
|---|---|---|
| Alpöge | Five declarations in `ALPOGE_Main.lean`; all four named proposition definitions in `ALPOGE_Statements.lean`. | Supplied files; accepted as cited premises. No missing imports were reconstructed. |
| Koiran | DIMACS 96-27 Theorem 2; Section 5 Theorem 9 and Corollary 1; complete 8 August 1997 erratum. | Author-hosted PostScript converted with ps2pdf, then pdftotext. `koiran_clean.txt` is the useful extraction. |
| Rojas | arXiv:math/0301111v2 Theorems 1 and 2. | Primary arXiv PDF through web retrieval. |
| Mulmuley GCT V | arXiv:1209.5993v5 Theorems 1.7, 1.9, 2.10, 3.4, 4.1, 4.7, 4.9, 4.10, 5.11 and 5.14. | Supplied TeX labels matched to PDF numbering; mapping in `gctv_locators.json`. |
| Miller | 1976 Theorem 2 and Appendix. | Author-hosted primary PDF. |
| Lenstra | 1979 Theorem 1. | Author-hosted primary PDF. |
| Bach | 1990 Section 6 pp.369–373, Theorems 2–3; Section 7 Theorem 4. | Original paper facsimile read from a mirror after official AMS endpoint failed. `bach_mirror.pdf` is valid; the initial failed download is retained as `bach_download_error.json`, not as a PDF. |
| AKS | 2004 Theorems 4.1 and 5.1; improved exponent in Theorem 5.3. | Primary Annals PDF. |
| OpenAI ETH | Theorem 1.1; Corollaries 1.2–1.4; Sections 1.1.1–1.1.3; Appendix C.1; Theorem D.1 and Lemmas D.2–D.5. | Read the complete supplied quantitative reduction, contraction and circuit files; official PDF confirms numbering. Mapping in `eth_locators.json`. |
| CGGM | arXiv:2611.07972v1 / ECCC TR26-313 Theorems 1, 5 and 6; Sections 5 and 8.2; page-9 ETH discussion. | Primary arXiv PDF and ECCC listing. The theorem statements and model hypotheses were checked; source proofs were not independently reconstructed. |
| Landsberg | arXiv:1305.7387v3 Section 8.2, equation (22), printed p.28. | Primary PDF independently opened and read; source historically calls its sign-sum formula Ryser, so the report cites the equation without repeating that attribution. |

Useful web references for the parent to reopen before citing in chat: Koiran author publication page `https://perso.ens-lyon.fr/pascal.koiran/publications.html`; Rojas `https://arxiv.org/pdf/math/0301111`; CGGM `https://eccc.weizmann.ac.il/report/2026/313/download/`; AKS `https://annals.math.princeton.edu/wp-content/uploads/annals-v160-n2-p12.pdf`; Landsberg `https://arxiv.org/pdf/1305.7387`. The bibliography contains stable URLs rather than internal retrieval IDs.

## Actual verification performed

All proofs in `complexity.tex` were read in full after drafting. The C-SIZE-01 initial logarithmic-density claim was corrected to `0<=a<1/2`; the earlier proof expression did not cover negative a. The Miller/Bach logarithms were made explicitly natural to preserve their constants. No proof-assistant run is claimed.

The finite script passed 128 gate-table assignments, 510 exact-one chain selections, 234 signed permanent matrices, 16,362 finite-field polynomial examples, and 121 values of the shifted positivity ray. Its output records the run identity and UTC time. These computations test encodings and edge cases, not asymptotic theorems.

Independent full-proof reviews of P-F1/P-F2/P-F7 reconstructed the proofs rather than merely reading the final claims. Further P-F3–P-F8 reviews identified a prose issue after P-F6: a general pure module need not have positive trace, so the odd-degree counterexample must specify the rank-one constant module with Frobenius 1. The main categorical proposition itself is correct. The parent was asked to make that local clarification; no edits to the parent's file were made.

An early LaTeX compile attempt could not start because the environment lacked `pdflatex.fmt`. The parent owns runtime repair and the final compile. No successful typesetting or PDF visual check is claimed by this branch.

## Next mathematical steps at the remaining gates

- For general HN: supply the arbitrary-field effective prime-ideal estimate, DZH, or GIPIT with the uniform parameters used in the reduction.
- For GCT V: construct the strengthened hitting set for the specified approximative circuit class, or prove the precise border-hardness hypothesis.
- For a positivity-to-algorithm transfer: provide the coefficient-identifying positive verifier/tensor description and its size in the partition encoding. The counting algorithm then applies at that size.
- For a useful dense permanent consequence: compress the effective Boolean incidence and precision budget enough to beat existing order-n exponential evaluation; no such compression is shown.
- For the cited arithmetic lower-bound trade-off: rule out faster perfectly complete input-oblivious MA protocols at a stated time scale; refuting ETH does not do so.
- For characteristic-zero GCT: identify the required actual orbit-closure quotient multiplicities or a separating equation, with an asymptotically adequate arithmetic/border lower bound. Numerical evaluation and modular sign data do not provide that identification.

## Additional main-positivity progress independently checked

After the branch was drafted, the parent proved P-F9 through P-F12. This run independently reconstructed every proof and logged those events in `cross_positivity_checks.tsv`. P-F11 replaces the common-period gate by the explicit polynomial bound `p(f)<=deg H+128*r^3*A^3` in expanded denominator length r and maximum weight A. P-F12 bounds r by Weyl growth and proves the stated PH3-to-PH2 implication, with a polynomial-size shifted-model existence consequence in the expanded group-size encoding. These are stronger gates than the earlier common-period condition. They do not prove PH3, provide a uniform algorithm to construct the positive form, or yield the stronger compressed-parameter model required by homogeneous PH1. The whole-proof check also verified the concrete numerator-index clash in the printed positive-form display.

## Finite reconstruction and subgroup counterexamples independently checked

P-F13 now narrows verification under a known denominator bound to a polynomial-length coefficient prefix and polynomial-time checks of candidate positive denominators. The coefficient values still have to be computed; the successful denominator still has to be found. A prefix without the denominator promise cannot certify the original series.

The complete primary-source audit and independent proofs of P-F14 and P-F15 confirm counterexamples inside the broad explicit polynomial subgroup-restriction problem. Positive torus characters and their direct sums are expressly allowed. The embeddings diag(t^(N+1),t) into GL2 and diag(t,t^3,t^(N+1)) into GL3 have fixed rank parameters 5 and 6, while the former has minimum modular index N and the latter has positivity and saturation indices N-2 for odd N. This refutes the uniform broad Hypotheses 3.3.4, 3.3.3 and 3.3.2(a), respectively. It does not refute the density clause or the narrower irreducible-inner plethysm hypotheses. These examples have polynomial descriptions in log N, so simply including the embedding bitlength would not rescue a polynomial index bound. All checks are recorded in cross_positivity_checks.tsv.


## Failed candidate and sharpened exact-transfer obstruction (2026-11-21)

The attempted alternating-group extension n=M or M+1, M a power of two, does cancel the primitive-M factor in the actual Hilbert series, but does **not** give the proposed quotient C[e_M]: specializing the elementary symmetric coordinates leaves x^M+c or x(x^M+c), whose discriminant is nonzero. Setting the alternating discriminant generator to zero therefore imposes a relation on e_M. This candidate was rejected before inclusion in any theorem.

A valid connected-semisimple replacement is recorded in P-F20f–g: SL2 x SL4 on Mat(2,4) plus Mat(4,4), whose invariant ring is a Plucker quadric cone times an independent degree-four determinant line. It is factorial, Gorenstein, normal, and rational; its actual Hilbert series is 1/(1-t²)^6, while its quotient C[d4] forces universal Phi4. This refutes exact prime-power transfer in that general category, without proving quantitative separation. The irreducible cubic case remains a distinct open gate.

## Chain fixed-component residue calculation (research note, 2026-11-21)

After the whole-proof check of P-F24, the following local quantities can be determined without classifying other fixed components. They do not prove a pole of the whole Hilbert series.

Let M=2^(n-1), g=gcd(n,3), and choose the chain diagonal generator with weights w_i=(-2)^i mod M for i=0,...,n-1. Normalize the unique cyclotomic valuation above 2 by v(1-zeta)=1. For a nonzero residue a mod M, v(1-zeta^a)=2^v2(a). This follows from the tower of 2-power cyclotomic fields: a root of exact order 2^b has 1 minus that root of valuation M/2^(b), while odd powers differ by a unit.

The adjoint moving eigenweights are w_i-w_j, i!=j. Their valuations are min(i,j) for nonzero w_i,w_j, and i if the other weight is zero. Hence their determinant valuation is

  2 sum_{i=0}^{n-2} (n-1-i)2^i = 4M-2n-2.

For a cubic monomial, order its three variable indices and let i be the least nonzero-weight index that occurs. If its multiplicity is one, the other two indices are strictly larger, giving binomial(n-i,2) monomials and valuation i. If its multiplicity is three, there is one monomial, also of valuation i. If its multiplicity is two, the next index i+1 gives a chain invariant and contributes no moving eigenvalue; every later index gives valuation i+1, with n-i-2 possibilities for 0<=i<=n-3. The final zero-weight cube is fixed. The moving cubic determinant valuation is therefore

  sum_{i=0}^{n-2} [binomial(n-i,2)+1]2^i
    + sum_{i=0}^{n-3} (n-i-2)2^(i+1)
  = 7M-(n^2+7n+6)/2.

By the exact tangent sequence in P-F24, the moving conormal determinant has valuation

  3M-binomial(n+2,2).

Taking duals or replacing the generator by any odd power does not change this value.

The chain orbit closure has the exact leading multiplicity e_Y=1 in P-F23. Indeed, its full actual linear stabilizer is cyclic of order 3M, and its determinant image has order 3M/g. Write any projective stabilizing transformation as cB with B fixing the form exactly. The determinant-one equation is c^n det(B)=1. Its scalar action on the form has factor c^3; after regrading by d0=n/g, the induced grading character is c^(3n/g)=det(B)^(-3/g), whose image has exact order M. Conversely every B supplies such a scalar c. Since the affine SL orbit is closed, equality of quotient points is equality of these orbits, so the grading stabilizer of the quotient point is exactly mu_M. The orbit closure has coordinate ring C[t^S] for a finitely generated additive subsemigroup S of N with gcd S=M. After division of all degrees by M, S is a numerical semigroup: choose any nonzero a in it, find an element of S in each residue modulo a using gcd S=1 and finite-group inverses as nonnegative multiples, and all larger representatives are obtained by adding a. Thus the graded dimensions are eventually1 and e_Y=1.

The chain's local summand in P-F23 consequently has valuation binomial(n+2,2)-3M. A proof that all other top-dimensional contributions have larger valuation would prove noncancellation, but no such comparison has been obtained.

### Checks on possible shortcuts

The Gorenstein canonical character fixes the product of normal eigenvalues. For normal exponents 0<a_i<M,

  det(1-g|N*) = (-2i)^c exp(pi i sum(a_i)/M) product sin(pi a_i/M).

For components of equal codimension and common canonical character this fixes the phase only up to sign; the parity of sum(a_i)/M is not determined. No general positivity conclusion follows.

A separate complete-intersection observation is valid but is not applied to the cubic invariant ring. If a positively graded complete intersection R=C[x_1,...,x_N]/(f_1,...,f_r) has a nonzero smooth mu_M-fixed point, let N_0 count generator degrees divisible by M and r_0 count relation degrees divisible by M. At that point the Jacobian is surjective onto the relation representation. Taking invariants is exact, so the fixed tangent dimension equals N_0-r_0. The Hilbert product has pole order N_0-r_0 at a primitive Mth root, exactly. The grading orbit through the nonzero point has dimension1, so this order is positive. This gives a route requiring a complete-intersection presentation, which is not available uniformly for growing-dimensional cubic invariant rings.

Primary caution against broad phase positivity: Kasprzyk--Wormleighton, Quasi-period collapse for duals to Fano polygons, Section3 Definition3.1 and Example3.2, printed p6, explicitly gives positive cancelling tuples of orbifold correction terms. URL https://kasprzyk.work/research/pdf/qperiod_collapse.pdf . This does not by itself furnish a counterexample with a smooth affine cone in the specific cubic setting.
