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

## Closure of the ordinary cubic pole gate (2026-11-21, after P-F30/P-F31)

The earlier research notes above record gates at the stage when they were investigated. The irreducible cubic gate is now closed by the complete support theorem in positivity_full_cubic_support.tex (P-F30), independently derived in parallel with plethysm and checked in its complete written form by bridges, plethysm, and this agent. The compressed-Hadamard argument covers every mixed cubic support and rank-deficient support matrix. An exact-form finite two-power stabilizer whose determinant has the extremal order2^(n-1) forces the smooth chain support.

Combining the finite-lift theorem P-F26 with P-F30 shows that every nonzero fixed quotient point is on the chain grading orbit. The support of the entire fixed scheme is consequently the single generically smooth curve Y, with only possible origin-supported extra scheme structure. P-F23 applies, and the local coefficient computed in P-F28 becomes the actual simple-pole coefficient. P-F31, independently whole-proof checked, gives a primitive2^(n-1) pole of the ordinary cubic plethysm stretch Hilbert series. Every polynomial-numerator/binomial-denominator expression therefore has a weight divisible by2^(n-1). Since the source parameter h=binomial(n+2,3)^2+n+1 is polynomial in n, this refutes the first positive-form existence clause of ordinary GCTVI Hypothesis1.6.7, in addition to its canonical clause already refuted by P-F19.

This does not infer a large positivity or saturation index, and does not provide a counting or circuit complexity lower bound. P-F20's cancellation examples remain valid: the successful transfer for this cubic family requires the additional classification and smoothness argument, not only the universal factor.


## 2026-11-21: post-pole index and average-polynomial audit

P-F33 is complete at `positivity_large_period_zero_indices.tex`: explicit normal CM Gorenstein rational hypersurfaces of dimension3 and fixed a=-1 have actual minimum period M but strict p=s=0. Its rationality proof checks the full singular axis, punctured blowup resolution, conormal and formal-functions vanishing, then the exact KSSW graded criterion. Bridges independently passed the entire proof.

P-F34 supplies a genuine quantitative surviving gate for the actual cubic ring: its distinguished primitive-root amplitude has base-two logarithm n^4/24+O(n^3), while p and s+1 must be large enough for the average polynomial B_n to dominate that amplitude. The sufficient estimate limsup(log2 U_n)/n^4<1/24 remains unproved. I independently whole-proof checked the original proposition and the sharper appended asymptotic. P-F35 gives exact p=s=23 for n=4; it is only a calibration.

P-F38, at `positivity_bounded_entry_average.tex`, refutes a concrete proposed shortcut to the U_n estimate. A unit-box polytope defined by a coefficient-two doubling chain has exact integer-point series 1/((1-t)^r(1-t^M)), with M=2^n and even r approximately n^3. The average constant is dominated by its leading Bernoulli term and has logarithm at least n^4-3n^3-2n+3. Adding uniquely determined slacks gives a nonnegative0/1/2 constraint matrix, all-one right-hand-side direction, and column sums at most3, with only2n+1 independent equations. Both peers fully checked the main proof and this addition. Under N=2n+1, the norm has liminf log2(U)/N^4 at least1/16, so even the sharper1/24 generic shortcut is blocked at the rank scale. This remains an abstract vector-partition counterexample; the complete cubic weight set, multiplicity-one weights, and Weyl alternating numerator are not present. No actual cubic U_n bound follows in either direction.

P-F36 source audit correction is explicitly logged: raw text extraction lost the discriminant layout; actual rendered GCT VII p19 and GCT VIII p31 show q^24 multiplying, not dividing. The source formula is corrected. Its square class, nonsquare under power regrading, and descent conclusions are unaffected.


## 2026-11-21: actual cubic coefficient bound (P-F42)

The actual-ring norm gate is now quantitatively narrower. `positivity_cubic_average_upper.tex` proves

  U_n <= 8 n! m^(3n) [288 n^3 3^n]^(m-n),  m=binomial(n+2,3),

and therefore limsup(log2 U_n)/n^4 <= log2(3)/6, approximately0.26416. This is above the sufficient1/24 threshold in P-F34, so no PH2/SH refutation follows. The proof uses the complete cubic monomial weight matrix and the exact Weyl alternant, a single rational perturbation preserving every relevant integer point set and avoiding all translated walls, Brion tangent cones, an exact finite quotient-lattice character filter, and averaging of constituent polynomials. A fractional-moment argument gives one bounded real specialization direction whose reciprocal small-factor product is controlled for every basis simultaneously. Retaining the determinant in inverse-matrix estimates yields a common analytic radius and avoids an extraneous log n in the leading exponent. The norm bound finally discards Weyl signs; a sharper signed comparison remains open.

Fresh primary locators are GCT VI Section5.1 equation(5.1) for the Weyl character formula and Barvinok, The Complexity of Generating Functions for Integer Points in Polyhedra and Beyond, Theorem2.5 printedp9 for rational-polyhedron Brion identities. Own full-proof reread and bridges independent full-proof reconstruction both passed. Plethysm review was requested and is pending at this entry. No computation-time guarantee is attached to the existential direction selection.

P-F40 has also been independently checked in its full current form, including the exact n8 mixed-sign table and the three-fixed-variable block-Klein extension. These are actual stabilizer normal representations, with exact large local amplitudes and cancellation/sign phenomena, but are not identified with the global stretching Hilbert series. They cannot be substituted for B_n or U_n.


## 2026-11-21: exact primitive Klein terms inside the actual average (P-F44)

`positivity_klein_global_contribution.tex` now gives B_n(X)=K_n+R_n(X), for3 not dividingn, with K_n=(nP)^(-1)Tr(C1), P=(2^n-(-1)^n)/3. R_n is the exact complementary balanced-character cone sum from P42. The orbit count includes all three central lifts and divides by the n cycle rotations; the primal cone determinant is C_-a before reindexing. This is a proved contribution to actual B_n, not an identification of a local normal-model Hilbert series with the global series. It vanishes for odd D=binomial(n,3). Both peers and root passed the full initial proof.

The moving Klein normal cyclic module has a squarefree cubic eigenbasis, hence is Lambda^3 of the diagonal variable representation. This reduces C_a to the reciprocal product over distinct triple weights. The full Jacobian reduction, including n4 wraparound and the GL/SL Euler-line split, was checked by both peers. Exact finite certificates give K4=1/25, K5=2/121, K8=-624/85. The n8 certificate is fully displayed in P44u-w and independently checked by `verify_klein85_certificate.py`, which uses only integer polynomial multiplication and monic division. The exploratory n10 inverse computation was interrupted with no result; no statement is drawn from it.

### Failed dominance heuristic and its normalization

The proposed dominance of the primitive orbit containing a=1 is false as a termwise absolute-dominance assertion. Each integer squarefree triple weight b=(-2)^i+(-2)^j+(-2)^k is divisible by3, and the triple(0,1,2) has b=3, so the common gcd is exactly3. For a*=3^(-1) modP, the exact ratio is

  |C_(a*)/C1| = product_(i<j<k) |1+2*cos(2*pi*b/(3P))|.

Its logarithm is D*log(3)+O(n^2). A short uniform argument is available: the normalized b/2^n lie in the compact set of sums of at most three signed dyadic terms, restricted to absolute value<=7/8. This set contains neither plus/minus1/3 nor plus/minus2/3; its distance from those numbers is positive. Since3P/2^n tends to1, all exceptional factors in the displayed ratio are uniformly bounded away from0. For maximum triple index k<=n-4, the logarithm of a factor is log3+O(4^(k-n)); summing the binomial(k,2) such factors gives O(n^2) total error. Only O(n^2) factors remain. Thus the a* orbit is larger by exp(D log3+O(n^2)), even though this changes no n^4 leading constant. This observation is retained as a failed-route note, not a new paper theorem or a bound for the complete trace.

After this necessary normalization, no second explicit family defeating a* was found. Fixed odd multiples of the normalized orbit have the expected a^(-D) bulk suppression, while fixed odd-denominator inverse families split the triple weights into residue classes and lose a positive fraction of small-angle factors. These observations do not control all exponentially many primitive residues uniformly, and do not control cancellation against R_n. No dominance conclusion for the normalized orbit, trace lower bound, or U_n lower bound is asserted.

## P-F48: exact density audit and a closed amplification route

The narrow SH(b) in GCT VI Hypothesis1.6.5(b), printedp25, conditions on nonzero coefficients among triples of exact total binary length N. Its input convention on printedp9 sums the lengths of positive parts and omits zero parts. The unified clause in Hypothesis3.3.2(b), printedp51, uses length at mostN, and its canonical ordinary-plethysm specification on p53 also charges n for the ambient group. These populations were initially conflated in the draft; the own reread and bridges follow-up caught this before integration. The final proof handles both separately, including all admissible rank padding in the unified setting.

P-F48 proves that every rescaled cubic triple, together with arbitrary nonnegative determinant twists of the inner and outer representations, occupies an exponentially negligible fraction of either specified population. The full proof is in positivity_density_scope.tex. The key disjoint budget is (n+1)ell(r)+n ell(q)+(m-1)ell(b), n>=4 and m>=20. No repeated partition entry is counted twice. Even if every such constructed nonzero input were an SH(b) exception, its narrow density is at most16N(N+1)^3 2^(-N/4); canonical augmented input density is at most32N²(N+1)^3 2^(-N/4). The unscaled family has f_n(1)=0 by P32 and is excluded outright. No proof of SH(b) or strict saturation of the rescalings is asserted.

## P-F49 arithmetic source audit (construction review pending)

Lamzouri–Li–Soundararajan, arXiv1309.3595v3, Corollary1.2 printedp3, proves under GRH that for q>3 and gcd(a,q)=1 the least prime P(a,q) is at most(phi(q) log q)^2. Its Section2 pp4–5 uses RH for zeta and GRH for primitive Dirichlet L-functions, exactly within the supplied theorem scope; arbitrary Dedekind GRH is not needed. Fresh web source: https://arxiv.org/pdf/1309.3595, exact theorem retrieved as turn803211482view0.

Xylouris, On the least prime in an arithmetic progression and estimates for the zeros of Dirichlet L-functions, Acta Arithmetica150.1(2011), Theorem1.1 printedp66, gives P(a,q)<=Cq^5.18 with an effectively computable absolute constant C. The original journal PDF is https://www.impan.pl/shop/en/publication/transaction/download/product/83078, retrieved as turn108414115view0. Thus, once the proposed P49 coefficient construction is proved, its stretch g(p−1) has an unconditional polynomial existence bound and the sharper supplied-Dirichlet-GRH bound<g(phi(n)logn)^2<=3n²log²n. This is a bound for a specified realized nonzero coefficient/Fermat evaluation, not a strict saturation or positivity-index bound.

The full P49 construction has now been read and independently reproved, not just its number-theoretic input. The local Cayley tensor normalization, truncated-ring socle polynomial identity, exact balanced determinant coefficient, factorial cancellation to1 modulo p, Hessian chain rule and all output gradings passed. Thus the arithmetic consequence recorded above is now proved through an actual explicit invariant nonzero at Fermat and a corresponding nonzero plethysm coefficient. The old label construction-review-pending describes only the earlier source-audit stage; it is closed by this event. The next distinct gates remain strict off-residue indices, full positive coefficient spaces and efficient evaluation.

## P-F42 coefficient-sensitive and pure-cube refinements

The original actual-ring cone proof has now been strengthened without an unsigned dominance assumption. Eventual feasibility gives C^-1(1)>=0 and total n/3, hence |lambda|<=n. Keeping j in the Cauchy estimate bounds individual coefficients. Separating selected pure-cube columns into C=[3I B;0 D0] then gives annihilator E=3|det D0|, while the filter retains order d=3^q|det D0|. Noncube columns have norm<=sqrt5. The resulting actual norm bound is 8*n!*m^(3n)*(1152*n^4*5^(n/2))^(m-n), with leading constant log2(5)/12. Coefficients j>=theta*D have leading tail constant (1-theta)log2(5)/12. Thus the highest fifth is already strictly below1/24, and the remaining norm gate is exactly equivalent to the same threshold for lower coefficients j<ceil(4D/5). The lower-coefficient bound remains unproved; no strict-index conclusion follows yet. Full proofs are P42t-ah, independently reviewed as recorded.

## Failed reciprocity shortcut (scope deliberately conditional)

The tentative exact cubic shift A=m/d0 was not used as an established input: its canonical-module criterion must be checked, and semisimple invariance alone does not identify that a-invariant. More basically, even granting B(X)=(-1)^D B(-A-X), this functional equation only fixes parity around -A/2. For even D>=2, adding an arbitrary constant preserves it and the leading coefficient; for odd D>=3, adding an arbitrary multiple of X+A/2 does the same. Hence that symmetry alone supplies no coefficient-norm upper bound or comparison with the large chain amplitude. This is a failure of the proposed inference, not an assertion that these arbitrary polynomials occur as actual cubic Hilbert averages. No actual U_n lower bound or global cancellation identity has been obtained from reciprocity.

The final P42ai-ak refinement controls the upper-degree tail uniformly at all real arguments0<=x<=n^K, for every fixed K: its ratio to the actual chain amplitude is at most2^(-eta*n^4/2), eta=1/24-log2(5)/60>0. Thus any polynomially bounded positivity shift p or saturation-test point s+1 must make the signed lower polynomial reach(1-o(1))|A_n|. A b0 fractional gap together with a small weighted positive-degree part is a sufficient route even when the norm has critical quartic exponent1/24. Neither such b0 comparison nor the needed weighted bound is proved.

## 2026-11-21T03:55:48.138154+00:00 — paired dyadic route and precise remaining estimate

P56 was independently whole-read and passed, including arbitrary two-power closed-orbit lifts, the Artinian Koszul no-pole criterion, exact maximal two-part classification, least-period valuation, half-period Fourier subtraction, and monotonic index tests. The new route cancels the entire smaller-two-part contribution before estimating anything, so it bypasses the average-polynomial low-coefficient problem. It remains a sufficient route, not an equivalence to PH2/SH.

I added and wholly reread P56l-z. A specified pair a*=(3g)^(-1) mod M has actual normalized amplitude at least 2^(n^4/24-2n^3). An explicit still-unproved total remainder bound E<=|Z|/4 would force a positive wave in every3g-step window regardless of initial phase, and would imply exponential strict-index lower bounds with every exponent c<1/4. The exact positive normal multiset cancels all numerator factors: nonzero singleton weights plus squarefree triples excluding {0,1,k} and {0,2,3}. Its determinant gives the exact a0 reciprocity, and the dyadic trace equals a signed negacyclic coefficient.

Failed/unfinished routes retained: (1) reciprocity alone constrains centered parity but does not bound the lower coefficients; (2) changing between coefficient norm and a supremum on polynomial intervals costs only exp(O(n^3 log n)), so cannot improve a quartic leading constant; (3) higher-dimensional derivative Fourier tests apply to coefficient positivity but not automatically to strict saturation, and the current block-stratum amplitude heuristic loses against the coefficient bound; (4) ordinary Thue-Morse/Gelfond sine-product maxima concern a one-body doubling potential, whereas the present denominator is a weighted three-body product, so those theorems cannot be imported as a dominance proof. The current open task is a uniform product comparison for all primitive dyadic embeddings, or another proved positive-window lower bound.

## Update recorded 2026-11-21T04:41:36.531990+00:00


## Closure of the strict cubic index gate: P-F57 and P-F62

The preceding conditional dyadic notes record the investigation at their dates. The full uniform comparison has now been proved. P-F57 (`positivity_dyadic_dominance.tex`) combines the exact O(n^2)-factor dimension increment with a near-multiplier estimate and a far-multiplier layer-cake loss. The near estimate has error at most100 n R^2; the far estimate is at most7 n^2-(log2 J-8)_+^3/24 relative to the selected peak. They cover every nonselected residue and give a uniform two-child contraction. The exact recurrence then proves E_n/|Z_n|->0. The original actual-coefficient test supplies p(f_n)>2^(cn) and s(f_n)>=2^(cn) for every c<1/4 and all sufficiently large n. All four agents wholly read and reconstructed the written proof. The explicit corollary gives p>2^(n/8), s>=2^(n/8) for n>=2*10^80. The former average-polynomial and signed lower-coefficient estimates remain open alternative routes; they are not needed for this conclusion.

P-F62 (`positivity_positive_start_dilation.tex`) strengthens the actual inputs. For gcd(t,6)=1, retain the original period L and define Q_a(X)=q_(ta)(tX). Since t is odd, Q_a-Q_(a+L/2)=2W_n(ta) identically. This avoids a new claim about cancellation among preimage poles under Veronese extraction. Uniformly for t<=2^(epsilon n), epsilon+c<1/4, the same selected-pair phase grid yields a witness in every3g-step window and proves exponential strict indices. The explicit t_n=6*10^200*n^199+1 lies beyond P54's actual-support threshold for n>=33. Hence f_n(t_n)>0 and every realized positive stretch is positive by powers in the invariant domain, while the literal constituent indices are still exponential. Its source bit length is199n log2 n+O(n). This gives actual nonzero-population SH(b) exceptions; P48 still proves the whole containing rescaled family exponentially sparse. SH(b) is not refuted.

## Exact Kronecker transfer audit and constructive adjoint calibration

Manivel, arXiv0907.3351, Theorem1 printedp1 and Remark1 p4, gives a genuine complete stretch identity: for fixed r>=2, rho and D>=|rho|, g(s(rD-|rho|,rho),(sD)^r,(sD)^r)=dim S_(s rho)(sl_r)^SL_r. The weaker range2D>=|rho|+rho_1 also scales homogeneously. Its inner representation is adjoint, and no identity with the cubic Sym^3 inner module has been obtained. Ikenmeyer--Panova1512.03798 Proposition2.8 printedp7 supplies only a stable-range inequality. Fischer--Ikenmeyer2002.00788 Theorem7.1 printedp15 gives tomography-specific equalities with additive pyramid padding and transposition, not a general ray encoding. The direct height-three rectangle candidate for the cubic family vanishes when n>9 by the exact Schur--Weyl length bound, while cubic discriminant powers give nonzero plethysm values. P58 contains the complete scope proof and was independently reviewed here.

P59 (`positivity_rectangular_adjoint.tex`) gives a constructive positive comparison inside actual rectangular Kronecker theory. For d>=A>=1, g(s(rd-A,A),(sd)^r,(sd)^r) is the coefficient of t^(As) in product_(j=2)^r(1-t^j)^(-1). The monomial residue decomposition modulo A/gcd(A,j) gives a positive numerator of degree below sum_j j/gcd(A,j), denominator weights at most r, and numerator coefficients at most A^(r-1). P11 plus constituent dilation gives strict indices <=ceil(C_r/A), C_r=(r-1)r+128(r-1)^3r^3. A rational recurrence of order O(r^2), with an explicitly proved polynomial integer bit bound, constructs the whole positive numerator and computes individual values in polynomial time in r and the binary parameters. At A=1 the exact minimum period is lcm(2,...,r)>=2^(r-1). No canonical Kronecker h.s.o.p. inference is made from the dimension identity. Root and bridges independently passed the complete proof and exact Manivel source scope.

## 2026-11-21T04:54:52.689806+00:00 — broad subgroup density padding (P-F63)

The fixed polynomial torus factor rho0(u,v)=diag(uv,u,1,v^4), lambda0=(4), pi0=(2,5) has h(s)=2 floor(s/4)+1, h(1)=1, and constituent h3(X)=(X−1)/2. Product with every positive subgroup input yields a nonzero constituent vanishing at1, because the canonical domain makes every original positive stretch nonzero. Under the source additive ordered finite specification convention, this is an injective constant-cost padding, giving E(N+C)>=A(N). The generous finite-code bound A(N)<=exp(O(N logN)) contradicts decay E/A<=N^(−c) for every c by iterating a single c>BC. The full draft and proof are in positivity_subgroup_density_padding.tex. Bridges independently whole-proof/source checked, then reread the explicit special-basic-cost and DAG-occurrence clarifications. Exact general composite delimiters and reductive-target codes are not fully prescribed in the source, so the result states its finite additive specification scope explicitly. Narrow ordinary SH(b) remains separate and open.


## 2026-11-21T05:07:36.441759+00:00 — logarithmic-overhead narrow density gate (P67)

A complete proof is in `positivity_logarithmic_density_padding.tex`. Unlike the broad product proof P63, this remains a conditional criterion: a map from every nonzero narrow input of raw length at most N to a strict-saturation exception of length at most N+O(log N), with polynomially bounded fibers, would refute the conditional narrow density claim. An explicit prefix-free integer/partition code uses exactly2L+3 bits. Iterating the counting inequality at logarithmically separated cutoffs contradicts the resulting exponential input bound; one fixed density exponent suffices. The source exact-shell condition implies the cumulative condition through the coefficient-one row families and a sqrtN split. The actual representation-theoretic map is still missing. Own full-proof and fresh primary-source check completed at this timestamp; peer review requested.

## Narrow density-padding audit — 2026-11-21T05:24:24.547692+00:00

No actual narrow padding map has been proved. Ikenmeyer–Panova, All Kronecker coefficients are reduced Kronecker coefficients (Forum Math. Pi 2024, DOI 10.1017/fmp.2024.23), Theorem 2 has homogeneous first-row stability hypotheses; after replacing every partition and padding parameter by its s-multiple, it preserves the entire stretching function. Equation (2.1), Lemma 1 and Lemma 2 likewise preserve the coefficient, with repeated rectangular parts whose raw expanded bit cost can depend on the old heights. These identities therefore do not create a fixed bad factor. Fresh primary HTML read: https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/all-kronecker-coefficients-are-reduced-kronecker-coefficients/8D984A05F46D4690E6E994854972AE37 . Ressayre, Horn inequalities for nonzero Kronecker coefficients, Theorem 3, printed p4, Eq12, is a sum of five LR factors times one smaller Kronecker factor, not a product of two independent Kronecker factors.

Elementary attempted face construction fails as follows. Split each of the three tensor factors into an old and a new block; let delta_i be the one-parameter weight difference in factor i. Requiring both the all-old and all-new tensor blocks to have weight zero forces sum delta_i=0. The three mixed single-new blocks then have weights delta_i, so they cannot all be strictly positive. If all are nonnegative, all delta_i vanish and the mixed blocks remain. This only rejects that monomial nonnegative-face construction, not arbitrary flag reductions or all possible narrow padding maps.

Bounded diagnostic: exact constituent interpolation justified by the proper rational generating series for partitions with parts 2,...,r found no positive-initial strict-saturation failure for dilations c=2,...,30 and r=3,4,5,6. This finite diagnostic neither proves a general result nor advances the density gate. No theorem is inferred.

## P-F72: exact geometric component trace with Tate normalization — 2026-11-21T05:32:56.130947+00:00

Complete proof: positivity_nonstandard_tate_trace.tex. For q=3^e, gamma=beta/2 is integral because B is even and is a unit at every3-adic place. The Q=q^117 Honda–Tate surface is ordinary with quartic CM endomorphism field and K-linear H1 tracegamma. The actual Weil restriction has dimension234. A rational correspondence isolates its all-H1 multidegree117 and then the equal-K-embedding tensor; the resulting K-rank2^117 summand has cyclic geometric Frobenius tracegamma, with positive Koszul sign because117 is odd. Ordinary Tate twist26 over F_q yields alpha exactly, pure weight65. This is a trace, not an eigenvalue identification.

The equal-embedding projector is the explicit product of (1+u0*ui/A)/2, and averaging rational correspondences over the117 conjugates descends its cohomological action. No Chow-idempotence theorem is assumed. The source references are Tate Bourbaki352 p96 and Waterhouse7.1p553 (freshly audited in P69), Milne1972 Sec1 pp177–178 (original local renders now visually read), and Milne AV15.1p27/15.5p29. Local source files are in nonstandard_sources/milne_1972_restriction.pdf and milne_abelian_varieties.pdf, with relevant rendered pages.

The appended base-extension obstruction is proved: gcd(2,117)=1 gives trace C²=trace F²=gamma²−2Q; after twist the full rational twice-Frobenius trace is negative, whereas the separately constructed q² fiber has positive trace. Thus these projected cohomology models cannot be base-extension compatible. No claim about isogenies of the ambient restrictions is inferred. Actual author full reread and final-extension reread pass; bridges independently whole-read the entire final proof and original source renders and reported PASS. Parent is performing its own check.

## P-F73: full specialized source algebra and its geometric action (2026-11-21 05:45 UTC)

The complete proof is in `work/positivity_nonstandard_full_correspondence.tex`. At q=3^e it proves the actual tensor-image algebra is Q × M2(Q)^3 × M2(K), dimension21. The source scalar block has both Q_i=0; this was freshly read in GCT VII printedp20. Original pp18-19 give the free21 alternating-word form; central polynomial factorization, irreducibility modulo3 and strict inequalities separate all five rational simple factors. CRT and explicit matrix units prove the abstract specialization is the full stated product.

The actual tensor specialization requires a separate argument. GCT VII §7.1.3 Eq25-26 printedpp21-22 gives all six geometric simple modules in the actual generic tensor cube, with nonzero multiplicities16,4,4,8,2,6. Figure1p30 was visually re-read: every matrix denominator is a power of the parameter. Thus monic characteristic-polynomial division holds over the Laurent ring and survives q=3^e; distinct central factors exclude omission of any specialized simple component. This is a specific cubic-example argument, not a blanket assertion that all abstract nonstandard algebras act faithfully on their tensor images.

The geometric object is A² × E⁷ over F_(q^116), with A from P69 and E:y²=x³−x over F3. It is an11-dimensional abelian variety. Blockwise transposition followed by contravariant H1 pullback preserves the exact source left-word order, and H1 has dimension22, two copies of the11-dimensional rational sum of simple modules. No identification of generators with Frobenius or of the formal parameter with a cohomological grading is asserted.

Author actual whole-proof/source review and final generic-occurrence refinement were logged in cross_positivity_checks.tsv. Bridges and plethysm both independently whole-read the proof and passed; bridges additionally freshly read Eq25-26 after the wording refinement. Root whole-read passed mathematically and is checking the exact final paragraph. P75 was independently whole-read and passed by this agent: its local normalization/conductor bound is separate, with no claim on every conductor element.
