# What the findings change

**Research status:** both clauses of ordinary plethysm PH3 are refuted: P-F19 treats canonical parameter degrees, and P-F30–P-F31 prove actual exponential-order Hilbert poles that refute the numerical positive-form clause. Narrow PH2/SH, uniform effective shifted counting and the asymptotic determinant/permanent obstruction remain open. P-F14–P-F15 also refute the broader rank-only subgroup-restriction index hypotheses. The supplied Alpöge and OpenAI results are used as cited theorems with their stated scopes. No P versus NP or ordinary complex-field VP versus VNP resolution is claimed. “Finding” denotes a deduction proved here, not a certified claim of historical priority.

All GCT VI hypothesis numbers below refer to the supplied arXiv:0704.0229v4 text. Its broad subgroup-restriction problem, irreducible-inner problem and ordinary GL_n plethysm subfamily are kept distinct.

## Priority of the conclusions

| Rank for the requested program | Findings | What they settle |
|---|---|---|
| 1 | P-F19, P-F30–P-F31 | Both printed PH3 clauses fail inside ordinary cubic plethysm. No purity proof can establish those false bounds. |
| 2 | P-F1, PLE-F5–PLE-F8, P-F7, P-F10 | Qualitative purity, even for the actual positive-basis multiplicity algebra, does not repair homogeneous PH1 or supply quantitative counting and index bounds. |
| 3 | P-F11–P-F12 | A fully proved polynomial numerical estimate gives the valid conditional implication from bounded positive Hilbert data to PH2. Its printed PH3 premise is false in general. |
| 4 | P-F34, P-F36–P-F42, P-F44, P-F51–P-F53 | The ordinary index route now has an actual upper bound and an exact signed global decomposition. The nonstandard route has an actual positive operator and exact normalized coefficients. A named theta output equals the cubic discriminant. The remaining comparisons and estimates are explicit. |
| 5 | P-F2, P-F13, P-F16–P-F18, P-F32–P-F35 | Shifted models, finite reconstruction and fixed-dimension bounds are proved; exterior duality, a zero-index large-period countermodel and exact four-variable indices clarify their limits. |
| 6 | PL-01–PL-08, B3.1–B7.3, P-F8 | The archive and seven bridges have explicit dictionaries, counterexamples and exact quotient-rank, normalization or integral-specialization requirements. |
| 7 | C-GRH, C-SAT, C-COUNT, C-PIT and circuit-scope findings | Exact analytic hypotheses and reduction costs are tracked. Dirichlet-GRH and the supplied ETH theorem discharge their stated premises but do not produce the missing GCT separator. |

## 0. A refutation inside ordinary cubic plethysm

**P-F19 and P-F30–P-F31 refute both clauses of GCT VI Hypothesis 1.6.7.** Put g=gcd(n,3), d0=n/g and W=Sym³ C^n. The family has fixed inner shape (3), outer partition (d0), and target partition ((3/g)^n). Its canonical algebra is the entire SL_n invariant ring of cubic forms, with its coefficient grading divided by d0. This identification preserves the actual multiplication.

The explicit point is the chain cubic

`F_n = x1² x2 + x2² x3 + ... + x_(n-1)² xn + xn³`.

Its gradient has no common nonzero zero, so its discriminant is nonzero. If an invariant of stretch degree s is nonzero at this point, its coefficient monomials must balance the diagonal-torus weights. The resulting recurrence forces `2^(n-1)` to divide s. A separate diagonal-stabilizer calculation gives the same divisibility. Every homogeneous system of parameters must contain an invariant nonzero at this point: otherwise its finite-dimensional quotient would force a power of the nonzero discriminant to vanish there. Consequently

`canonical modular index >= 2^(n-1)`.

The parameter in the printed hypothesis is `h = binomial(n+2,3)^2 + n + 1 = O(n^6)`. The lower bound is therefore superpolynomial in h, despite the inner shape remaining (3). It applies to every parameter system, so it applies in particular to the lexicographically minimal one used in the source's definition.

This settles a substantial part of the main positivity question negatively. A purity argument cannot establish this false canonical degree bound. The chain forms themselves occur in earlier literature, including Busé–Jouanolou Example 4.12, which cites Demazure; no priority claim is made for the forms or this consequence.

**The numerical positive-form clause also fails, by a further argument.** P-F30 classifies all cubic supports admitting a finite two-power stabilizer with determinant order `M=2^(n-1)` and a nonzero invariant: equality forces the smooth chain. This includes rank-deficient supports, mixed square-linear and squarefree monomials, and lifts whose order was not initially assumed to be M. Thus the chain curve is the entire support of the grading-fixed scheme. The ambient quotient is smooth along its nonzero orbit. P-F23 and P-F28 then give an actual simple pole at every primitive Mth root of unity, with a nonzero leading coefficient. Possible structure at the origin contributes no pole and cannot cancel it.

Every rational form with polynomial numerator and denominator factors `(1-t^a)` must therefore have some weight a divisible by M. This is stronger than a lower bound on parameter degrees: it applies even when the numerator has arbitrary complex coefficients. It refutes the first, numerical positive-form existence clause of PH3 as well.

**The remaining distinction is between poles and indices.** The argument forces an exponentially large quasipolynomial period, but does not establish a superpolynomial positivity or saturation index. Those narrower PH2/SH questions remain open. Section 7 explains the intervening failed transfers and the proof that closes the actual-pole gate.


## 1. The strongest new implication in the main positivity question

**P-F11–P-F12 prove revised PH3 ⇒ revised PH2.** Let a nonzero global quasi-polynomial have generating function

`F(T) = H(T) / product_i (1 - T^{a_i})`,

with nonnegative integer numerator, `r` denominator factors, `A = max a_i` and `h = degree H`. The proved bound is

`positivity_index(F) <= h + 128 r^3 A^3 < r A + 128 r^3 A^3`.

This is coefficient positivity of every constituent polynomial after one integer shift. It does not merely assert eventual positivity of the values along each residue class. The proof controls every root-of-unity pole by Cauchy's estimate and compares its contribution coefficient by coefficient with the positive highest-order pole. Common divisors and numerator translations are treated explicitly. Two independent agents checked the complete argument.

For a branching multiplicity from `V_{n lambda}(G)`, Weyl's dimension formula bounds its growth degree by the number of positive roots of G. Positivity of the rational form forces `r = degree(F) + 1`. Thus `r <= dim G + 1`. A polynomial bound on the numerical denominator weights in the parameter of GCT VI Hypothesis 1.6.7 gives the polynomial positivity-index bound required by Hypothesis 1.6.6. The connected classical restriction version follows with the rank parameter of Hypotheses 3.3.3–3.3.4. This includes Kronecker coefficients in their GL restriction realization.

The implication only needs a positive rational form with small numerical denominator weights; it does not require those weights to be degrees of canonical parameters. P-F31 now refutes that weaker clause in general, so the implication remains valid but cannot prove PH2 from the printed PH3 premise. A direct PH2 argument or a genuinely different sufficient hypothesis is required. GCT VI itself proposes this possibility in Section 4.2.2; we make no assertion that nobody previously considered it.

For GL_m, the numerator degree is less than `r A`, and its coefficient at i is at most `dim V_{i lambda}(GL_m)`. P-F12 therefore bounds the entire positive form's binary description polynomially in `m`, numerical `A`, and `log(lambda_1+1)`. Together with P-F2, PH3 gives existence of a small **shifted** polytope in those expanded parameters. It does not give an algorithm to find the positive form, and `dim G` may be very large relative to the compressed inner partition. Those distinctions are essential to the flip's algorithmic requirements.


### Reconstruction and qualitative uniformity

**P-F13** turns a denominator promise into a finite reconstruction problem. If r<=R and all denominator weights are <=A, the common denominator D(T)=product_(a=1)^A(1-T^a)^R has degree M=R A(A+1)/2. The first M multiplicities determine the whole rational series. A proposed positive numerator and bounded denominator can then be checked by an exact polynomial identity. This does not provide a fast multiplicity oracle, a fast search through all denominators, or a proof of the denominator promise from a short prefix alone.

**P-F16–P-F17** give a finite bound for each fixed semisimple embedding. A finitely generated positive multigraded branching algebra contains the actual canonical ray algebras. A bound from its generator-degree matrix and minors gives bounded ray generators; a common multiple of their degrees supplies parameters in one degree. Rational singularities give Cohen–Macaulayness, and the positive Hilbert form gives bounded positivity and saturation indices. A prime-avoidance argument additionally bounds the source's lexicographically minimal parameter degrees. The graded GL-to-SL reduction preserves the canonical algebra on centrally balanced rays.

**P-F18** removes the remaining qualitative dependence on n and determinant twists when the inner dimension m is fixed. A nontrivial irreducible S^mu C^n of dimension m has n<=m and every consecutive highest-weight difference <=m-1. Only finitely many normalized SL_n representations remain. Thus one finite function of m bounds the indices and canonical parameter degrees for all ordinary plethysm rays of inner dimension m. P-F19 proves that the optimal canonical bound has an exponential subsequence, and P-F31 proves the same obstruction for numerical denominator weights. Qualitative finiteness does not supply the polynomial growth conjectured in PH3.

### The broader rank-only hypotheses

**P-F14** uses the faithful torus embedding t↦diag(t^(N+1),t), with fixed λ=(1), π=2. Its stretch series is 1/(1-T^N), forcing a denominator weight at least N in every rational form of the indicated kind. Its source rank parameter stays 5. This refutes the broad rank-only PH3 of Hypothesis 3.3.4.

**P-F15** uses t↦diag(t,t³,t^(N+1)) for odd N. The actual multiplicity algebra is a polynomial ring on generators of degrees 2 and N, with series 1/((1-T²)(1-T^N)) and exact positivity and saturation indices N-2. The source rank parameter stays 6. Hence Hypotheses 3.3.2(a) and 3.3.3 fail in that broad formulation. The coefficients are nevertheless easy to compute, and this does not refute the density clause 3.3.2(b). These are reducible torus representations, so they must not be substituted for the ordinary irreducible-inner examples in P-F19. Including only the bit length of N in a repaired parameter still leaves exponentially large numerical indices.

## 2. What is actually refuted about purity and positivity

The homogeneous PH1 of GCT VI Hypothesis 1.6.4 is already false on the Kahle–Michałek ray (Theorem 5 and Remark 6):

`phi(s) = p_(4s),(3)^(7s,5s) = floor(s/3) + 1_(s even)`.

Its quasi-polynomial extension violates Ehrhart reciprocity. The old strong zero-index Kronecker SH and PH2 also have cited counterexamples (Briand–Orellana–Rosas Theorem 2.4). These do not refute the revised polynomial-index hypotheses.

The work proves several sharper statements about this exact ray:

- **P-F1:** it counts the integer points in the single two-dimensional shifted polytope `0 <= z <= 1`, `3t+4z >= s`, `2t+4z <= s`. No eventually one-dimensional shifted model exists, even in a larger fixed ambient lattice.
- **PLE-F5:** it is the half-graded Hilbert function of the normal binary-dihedral invariant ring `C[U,V,Z]/(Z² - U V² - 4 U⁴)`, with degrees 2, 3 and 4. Its Hilbert series is `(1+T⁴)/((1-T²)(1-T³))`.
- **PLE-F6:** `phi(qs)` is a homogeneous rational Ehrhart function exactly when `gcd(q,6)>1`. The least repairing rescaling is 2. The general degree-one rescaling question was already discussed by Kahle–Michałek, Question 15; the exact classification here is proved for this ray.
- **PLE-F7:** over a field of order `q = 1 mod 12`, the same cone is a finite quotient of the affine plane. Its ordinary compactly supported cohomology is only `Q_l(-2)` in degree 4. Its perverse-normalized intersection complex is the constant sheaf shifted by 2, so its intersection-cohomology version is pure and even as well. This is proved using finite pushforward, averaging and local purity, independently of the supplementary point-count calculation.

**PLE-F8** identifies that ring with the actual canonical highest-weight multiplicity algebra of the obstructing plethysm ray. Explicit cubic covariants supply the generators; an irreducible quadratic relation and a graded-dimension comparison prove the isomorphism. The basis U^i V^j Z^epsilon has nonnegative integral multiplication constants because Z²=UV²+4U⁴. The monic equation gives a flat model over Z, with the claimed finite-field geometry. It is not identified with the naive Lie-derivation kernel in every characteristic.

Thus the actual plethysm multiplicity algebra has normality, a positive multiplicative basis, and a pure even Tate model, while its graded Hilbert function violates homogeneous PH1. The grading is a different datum from the cohomological degree. A new proof of a purity theorem cannot by itself identify those gradings or reverse the counterexample.

**P-F10** provides the separate quantitative test. Give the fixed smooth affine plane coordinate weights a and b, with a,b>1 coprime. Its Hilbert quasi-polynomial has exactly `p = s = ab-a-b` as its positivity and saturation indices. The underlying variety and its pure cohomology do not change, but the indices are unbounded. P-F15 subsequently realizes this sequence inside the broad subgroup-restriction problem with fixed ranks, refuting its printed rank-only SH(a) and PH2 bounds. It does not refute the narrower irreducible-inner plethysm bounds. The embedding weights must enter a corrected general statement.

**P-F7** gives a computational test: polynomially many degree-at-most-three equations define a finite smooth proper scheme consisting of exactly the satisfying assignments of an arbitrary 3-CNF formula. All its cohomology is pure Tate in degree zero. Exact counting on this presented family is #P-complete, and nonemptiness is NP-complete. This is a reduction, not an assumption that P differs from NP.

## 3. What an Alpöge-method transfer must still provide

The exact analytic premises are the five declarations in ALPOGE_Main.lean, with the Dirichlet types in ALPOGE_Statements.lean. The determinant sign is Remark p.3 item4; the sign-only finite-field argument is p.3 footnote3, not the note's numbered item5. GGP interlacing, theta lifts and the seesaw occur in items7,8,12.

**P-F3** already gives an unconditional positive determinant for each Kronecker or plethysm coefficient: the compact-group averaging projector P has `det(I+tP)=(1+t)^m`, where m is the multiplicity. Its matrix can be enormous and its rank is the unknown quantity. Another positive determinant requires a size and identification theorem before it supplies an efficient counting rule.

**P-F4** shows that pointwise nonnegative virtual characters can have negative irreducible coefficients. **P-F5** shows that Sym² restriction GL₂→GL₃ is different from ordinary block interlacing. **P-F6** gives the sufficient categorical transfer: an actual semisimple graded product, a specified basis, and a verified specialization produce nonnegative structure coefficients. Purity is one ingredient of such a construction; it does not construct the category, the basis identification or its efficient description.

**P-F36 strengthens the requirement using the actual nonstandard cubic algebra.** In the worked GL₂→GL₄ example of GCT VII–VIII, a displayed coefficient involves a square root of a rational function that remains nonsquare over C(t) after every power regrading q=t^k. It therefore cannot be a finite Laurent character, even with virtual signs, fractional grading or a nonzero rational scalar normalization. The Galois involution exchanges two simple bimodule blocks. An object or projector defined over the rational function field cannot select either block separately; a descended graded bimodule has equal multiplicities for the two conjugate blocks in each degree.

A proposed comparison must carry the quadratic extension and its descent datum, or recover the separate objects from a conjugate sum. This is not an objection to arbitrary theta lifts with coefficient systems, and it does not refute GCT VIII's relaxed positivity assertions about minimal-polynomial coefficients.

**P-F37 supplies an actual automorphic dictionary in one fixed dimension.** Looijenga–Swierstra's Theorem3.1 identifies the five-variable cubic invariant ring with meromorphic automorphic forms on an arithmetic complex10-ball, allowing poles along its specified hyperplane arrangement. Automorphic weight3s corresponds to ordinary invariant degree5s and hence to stretch s. This preserves multiplication, so it identifies the actual canonical plethysm algebra. P-F31 then gives simple primitive48 poles in the original automorphic-weight series and forces a denominator weight divisible by48. Every homogeneous parameter system contains a weight at least48.

This supplies a specific unitary automorphic object for a proposed comparison. The comparison must still connect the supplied note's theta-lift outputs with these meromorphic spaces, their weight grading, permitted arrangement poles and multiplication. The ball has signature(10,1), and this fixed-dimensional theorem does not identify a uniform family for growing n.

The remaining nonstandard-quantum-group task is therefore specific: realize the intended bases and products of GCT VII–VIII, identify the relevant multiplicity spaces, control shifts and specialization, and bound the data. This paper proves neither nonexistence nor a logical independence claim about a future construction.

## 4. The surviving obstruction problem

Bürgisser–Ikenmeyer–Panova Theorem1.4 rules out the specified occurrence-obstruction strategy for determinant versus padded permanent when `n >= m^25`. It does not rule out every GCT strategy.

**P-F8** proves the remaining multiplicity test: if the permanent-side actual coordinate-ring multiplicity exceeds the determinant-side one, containment fails. In the no-occurrence range, both multiplicities in such a test are positive. Equal multiplicities do not imply containment; two coordinate axes under the scalar torus give a counterexample.

**PL-06** makes the missing quotient information concrete for Chow: the multiplicity in its coordinate ring is the rank of the corresponding Foulkes–Howe map between multiplicity spaces. Source and target plethysm coefficients are not that rank. The known h_(5,5) kernel for W=C^5 prevents an automatic injectivity inference.

**B7.1–B7.2** provide a positive integral transfer. A fixed characteristic-zero orbit-closure separator for an integral GL action can be taken integral and survives modulo every prime not dividing its nonzero evaluation. At fixed degree, separation is an augmented-matrix rank condition, and two nonzero minors control bad primes. Uniform degree, succinctness and prime bounds remain the GCT gate.

## 5. Consequences of the supplied analytic and ETH theorems

**Directly discharged analytic hypotheses:** Bach's rational-field Theorems2–3 in Section6 use Dirichlet characters and zeta. Under the supplied statements, the explicit Miller witness bound `2(ln m)^2` and unit-generator bound `3(ln m)^2` apply. Polynomial-time primality itself was already unconditional by AKS.

**Partially transferred:** C-GRH-01 proves Dedekind GRH for every subfield of a cyclotomic field, including ramified Euler factors. Koiran's arbitrary-system HN∈AM proof instead uses arbitrary primitive solution fields (DIMACS long version Theorem2, Section5 Theorem9 and Corollary1). C-GRH-03 shows that x³−2=0 cannot be forced into an abelian solution field. This is a precise obstruction to that proposed restriction, not a proof that Dirichlet GRH has no other route to HN. GCT V's Koiran-based conditional bounds retain this gate; its PIT equivalences retain their separate hitting-set or border-hardness hypotheses.

**ETH and SETH:** the supplied fixed-k counting theorem gives deterministic `2^{o(n)}` counting for every fixed width, with the sharper sparse exponent `O(n/sqrt(log n))`. C-SAT-01 spells out the refutations of ETH, #ETH, standard SETH and the corresponding variants treated there. An ETH-conditional lower-bound proof remains a valid implication whose hypothesis is false. It does not automatically produce a fast algorithm for the target problem.

**Method transfer:** C-COUNT-01 gives a parsimonious verifier-to-3CNF conversion with explicit gate and clause counts. C-SIZE-01 tracks arbitrary-width formula size. C-COUNT-02 applies the supplied contraction theorem to signed sparse integer permanents, including precision sufficient for exact signed recovery. C-PIT-01 gives a bounded-degree finite-field identity test through a bit verifier. These are exact model-specific deductions, with quantitative reduction costs; they do not produce a positive plethysm formula or a polynomial-time algorithm by changing the meaning of input size.

The supplied circuit corollary yields an infinitely-often superlinear lower bound for E^NP. The November2026 Chukhin–Gajulapalli–Golovnev–Mihajlin Theorem1 gives a separately cited disjunction between a strong NE Boolean lower bound and `VP_Z^0 != VNP_Z^0`. It neither selects the arithmetic branch nor identifies that constant-free integer class with ordinary complex-field VP. Its Theorem6 already studies the permanent-to-3UNSAT protocol connection; that bridge must not be represented as previously unconsidered.

## 6. Grothendieck's pages and the other bridges

Cote133 scan19 requires separating subsets, symmetric multisets and the exterior-compatible opposite-series structure. **PL-01** refutes the study's order-two equivariant check on the free two-point C₂-set. **PL-02** supplies C₂ and C₂×C₂ counterexamples to the unrestricted special-lambda interpretation. Cardinalities can agree when equivariant classes do not.

Cote133 scan28 yields the proved tensor-power expansion **PL-03**, with monomial symmetric coefficients and induced trivial symmetric-group representations. Its degree-two coefficient is `Sym²(V) - exterior²(V)`, so the chosen coefficients can be virtual. **PL-04** gives the exact modular relation over F₂; **PL-05** shows why effective permutation sets cannot produce every irreducible representation; **PL-07** gives the explicit small Kronecker saturation counterexample. **PL-08** distinguishes strict characteristic-two quadratic-form hypotheses and the failure of exterior operations to descend to the Witt quotient. The paper inventories every supplied cote/scan and does not attribute modern Grothendieck polynomials to the manuscript author.

For Schubert K-theory, **B3.1** performs the sign change giving a positive based multiplication and isolates the ordinary LR degree slice. **B3.2** proves an actual failure of dilation support for K-theoretic coefficients. Nonnegative structure coefficients alone do not supply LR saturation.

For Grothendieck's inequality and tensor norms, **B4.1–B4.2** isolate the realization and precision gates: exact norm nonzero detection is already entry nonzero detection, and fixed-factor approximation cannot distinguish all adjacent integer multiplicities. **B5.1–B5.3** prove the scaling obstruction, a valid contraction-model monotonicity theorem and the absence of a uniform normalized nuclear/Frobenius gap in an explicit rank-two orbit. These results explain exactly what the bridges carry and which additional invariant or gap an algebraic orbit obstruction would require.

## 7. How the actual-pole question was closed

**P-F20** proves that the cubic chain forces a cyclotomic factor of exponential order in the universal denominator and hence in an actual fixed-target covariant Hilbert series. Neither statement identifies a pole of the ordinary stretching Hilbert series. An explicit connected semisimple invariant ring that is factorial, rational and Gorenstein has a universal cyclotomic factor that cancels from its ordinary series. A separate quasi-polynomial example prevents a transfer from affine slices to simultaneous rays without further algebraic structure.

**P-F21–P-F22** make the parameter-versus-series distinction quantitative. Normal rational Cohen–Macaulay three-dimensional semigroup domains can have unbounded necessary parameter degrees while their ordinary Hilbert denominator has only weight one. The Gorenstein family in P-F22 has the same entire Hilbert series `(1+7t+t²)/(1-t)³` for every member. These examples do not identify a counterexample inside the cubic plethysm family; they rule out generic transfer arguments using only those geometric properties.

**P-F23** proves an exact noncancellation criterion. If the grading action of a primitive Mth root has a unique largest fixed component, and the ambient affine variety is generically smooth along it, the ordinary Hilbert series has a pole there. The leading coefficient is the positive regraded multiplicity divided by the determinant of one minus the conormal action. With several largest components these coefficients must be summed, so their phases matter.

**P-F24** verifies the local hypothesis for the actual cubic chain: for n at least four, its full projective automorphism group is cyclic of order `M=2^(n-1)`, its effective stabilizer in the special linear group is trivial, its quotient point is smooth, and the grading-fixed component through it has dimension one. **P-F26** proves that the entire fixed locus represented by smooth cubic hypersurfaces is this one chain orbit. Every competing component is confined to the discriminant boundary; a finite two-power exact-form lift with primitive determinant exists even there.

**P-F27** then excludes all competing graph supports. If the supported cubic monomials use only cubes and squared-variable times another variable, the extremal determinant order forces the smooth chain itself. The proof covers deficient-rank support lattices and finite lifts whose order was not assumed to equal M. Thus a singular competitor must contain a three-distinct-variable monomial in every finite-lift eigenbasis. The connected-graph extension of P-F27 also forces the graph part of every remaining support to be disconnected. P-F29 excludes supports containing only cubes and squarefree triples; both square-linear and triple monomials must occur. P-F28 computes the chain coefficient exactly: its regraded multiplicity is one and its normalized cyclotomic valuation is `binom(n+2,2)-3*2^(n-1)`. **P-F30 closes those remaining mixed-support cases.** It compresses the square-linear graph components by their cofactor vectors and bounds every remaining triple column by a precise Euclidean norm. Cramer denominators, a maximal-minor expansion and the odd factor three in the full-rank case force every non-chain determinant order strictly below M. The argument covers deficient rank and arbitrary two-power lift order.

**P-F31 therefore proves the ordinary-series pole.** The fixed scheme has just one one-dimensional component, the chain curve, and the quotient is smooth at its generic point. The exact local coefficient from P-F28 is now the actual leading coefficient. The pole at every primitive Mth root is simple. Every allowed rational denominator has a weight divisible by M, and every quasipolynomial period is divisible by M. This closes the earlier geometric gate and refutes the weaker PH3 clause. It does not assert that M is the entire minimal period.

**P-F25** separately treats the binary determinant subfamily. The largest realized missing stretch is thirteen in the source classification. This is not a bound for the strict saturation index in GCT VI, which also tests constituent polynomials away from their own residue classes. A direct least-common-multiple parameter envelope is proved, with no polynomial bound inferred from generator degrees alone.

## 8. A direct reduction for the surviving index question

**P-F32** rewrites the cubic invariant multiplicity as a determinant multiplicity in an exterior power. Put `g=gcd(n,3)`, `k=3s/g`, `d=ns/g` and `N(k)=binomial(k-1,2)`. Then

`f_n(s) = multiplicity of det^n in exterior^d(exterior^3 C^k)`.

It follows that `f_n(s)=0` when `n>N(k)`, and `f_n(s)=1` when `n=N(k)`. Exterior duality replaces n by `N(k)-n` when that number is positive, with the exact regrading stated in the paper. For `n=N(k)` and `k>=5`, the first positive stretch is exactly `s*=gk/3` and its value is one. The generic degree monoid has greatest common divisor one, so every quasipolynomial constituent is nonzero; the preceding realized zero therefore gives strict saturation and positivity indices at least `s*-1 = Theta(sqrt(n))`.

This is a direct index statement, unlike the period lower bound. It is compatible with polynomial PH2 and SH(a). It does not settle their upper bounds or the separate saturation-density clause.

## 9. A direct Fourier test, and why its remaining estimate matters

**P-F33** rules out another general shortcut. For every M>=3, the weighted hypersurface

`R_M = C[x,y,z,w] / (w(xy-z²)+x^(M+2)+y^(M+2))`, with weights `(1,1,1,M)`,

is a normal Cohen–Macaulay Gorenstein domain of dimension three with rational singularities and a-invariant −1. Its Hilbert series has genuine simple primitive-M poles. Nevertheless all its constituent polynomials have positive coefficients, so both strict indices are zero. Their average constant is `(M+1)(M+2)/(6M)`, although the first M actual coefficients agree with the ordinary three-variable polynomial ring. Thus even these geometric properties and a long small prefix do not bound the off-residue average that an index argument needs.

**P-F34** uses the actual cubic family more precisely. Let B_n(x) be the average of its constituent polynomials; this is independent of the chosen period and is determined by the principal part of H_n(t) at t=1. Its degree is `D=binomial(n,3)`. Let C_n(ζ) be the nonzero coefficient in P-F31 and put A_n(ζ)=C_n(ζ)/M. Fourier inversion proves

`B_n(p(f_n)) >= |A_n(ζ)|` and `B_n(s(f_n)+1) >= |A_n(ζ)|`.

For the specified complex embedding ζ=exp(2πi/M), an explicit sine-product estimate proves `|A_n(ζ)| >= 2^(n^4/192)` for n>=250. This is an absolute-value bound, independently established from the moving cubic and adjoint weight lists; it is not inferred from a two-adic valuation.

If the coefficient norm `U_n=sum_j |[x^j]B_n(x)|` satisfied `U_n <= 2^(C n³ log₂(n+2))` with an absolute C, then both p(f_n) and s(f_n)+1 would be at least `2^(n/32)/(n+2)^(6C)` for all sufficiently large n. That would refute narrow polynomial PH2 and SH(a). **This stronger U_n estimate is unproved.** P-F42 now gives an unconditional bound with quartic logarithmic constant log2(5)/12, still above the required threshold. Its refined tail estimate reduces the sufficient norm gate to the lower four fifths of coefficient indices. The result gives a necessary inequality and a precise sufficient remaining condition, not an equivalence or a completed refutation. P-F33 prevents replacing this missing estimate by a generic normality, rationality or Gorenstein argument.

**P-F35** supplies an exact small-dimensional calibration. Salmon's quaternary-cubic ring gives

`H_4(t)=(1+t^25)/((1-t²)(1-t⁴)(1-t⁶)(1-t⁸)(1-t^10))`.

The written proof extracts closed constituent formulas and checks every shifted coefficient uniformly. It proves `p(f_4)=s(f_4)=23` and minimal period120. The lower bound uses the actual hole at23 and nonzero degree-four constituents; the upper bound is coefficientwise positivity after that shift. No extrapolation to larger n is made.

## Next main step

Attack the explicit cubic average-polynomial estimate in P-F34, while retaining direct PH2/SH and effective shifted-counting routes that do not depend on it. Both canonical parameter degrees and numerical positive-form denominator weights fail the printed polynomial PH3 bound in general. P-F11–P-F12 remain valid conditional tools, and P-F13 makes candidate verification finite when an appropriate bound is supplied. The nonstandard route must additionally handle the descent requirement proved in P-F36. To reach an obstruction, an index or counting result must still be joined to control of actual coordinate-ring quotient ranks and a strict asymptotic comparison. Those tasks remain open in this run.

### Sharper remaining ordinary-index gate (P-F34, P-F38)

The actual complex pole amplitude has log2|A_n|=n^4/24+O(n^3). A sufficient condition for exponential positivity and saturation indices is limsup(log2 U_n)/n^4<1/24, where U_n is the coefficient l1 norm of the pole-at-one polynomial. This condition is unproved. P-F38 constructs explicit nonnegative 0/1/2 vector-partition matrices with column sums at most3, cubic-scale dimension, and unit-box polytopes whose corresponding norm is at least2^(n^4/2). The actual complete cubic weight list and Weyl alternating numerator are therefore essential to any proposed smaller bound; small entries and dimension alone do not suffice.


## 12. Actual positive operators, named theta outputs, and global cancellation

**P-F39** handles the displayed nonstandard cubic coefficient itself. Its two conjugates are eigenvalues, up to the specified sign, of an explicit two-by-two rational matrix that is positive and self-adjoint for an explicit positive Gram form for every real q>0. Nevertheless its unnormalized determinant has negative Laurent coefficients. Multiplying by precisely the source's normalization produces the positive trace and norm vectors printed in GCT VIII. The proof realizes these two vectors by finite direct sums of twisted projective-space cohomology with Lefschetz symmetry. These are coefficient models. P-F52 now realizes the operator by an actual central word and a source-basis intertwiner; a geometric/theta identification of the coefficient models and compatibility with all products remains to be constructed. If q is instead treated as a base coordinate, the nonconstant trace prevents this multiplication from being a horizontal endomorphism of a finite local system, even after finite dominant covering.

**P-F41** identifies a concrete theta image in the actual five-variable cubic plethysm algebra. The E6 quasi-pullback of the weight12 Borcherds form, restricted to the cubic-threefold ball, has weight48 and trivial multiplier on the relevant group. The graded period-ring isomorphism sends it to a nonzero scalar multiple of the degree80 cubic discriminant, in stretch16 and GL5 character det48. This identifies all products in the polynomial subalgebra generated by that form. The construction begins with the regularized multiplicative orthogonal theta lift of the reciprocal elliptic discriminant; the integral computes a logarithmic norm. The remaining comparison with the supplied iterated totally definite unitary lift is now about a named form and specified operations. It does not yet give a basis for all multiplicity spaces or a uniform counting formula.

**P-F42** proves an unconditional upper bound for the coefficient norm of the actual cubic average polynomial. With m=binomial(n+2,3),

`U_n <= 8 n! m^(3n) (1152 n^4 5^(n/2))^(m-n)`.

Consequently `limsup log2(U_n)/n^4 <= log2(5)/12`. The proof uses the actual cubic exponent matrix and Weyl alternating numerator, rational perturbations preserving lattice points, finite-character cone formulas and an analytic coefficient estimate. It proves existence of a bounded common specialization direction; no efficient construction algorithm is claimed. Since log2(5)/12 is greater than1/24, this estimate does not settle either remaining polynomial index bound. A coefficient-sensitive refinement proves that the sum over j>=ceil(4D/5), D=binomial(n,3), has quartic logarithmic constant at most log2(5)/60<1/24. The sufficient strict U_n gate is therefore equivalent to that same bound for only the complementary lower coefficients. The proof distinguishes the finite-character group order from a smaller annihilator obtained by removing pure-cube columns.

**P-F40 and P-F44** show why unsigned local estimates lose information. For the actual Klein cubic, inverse primitive stabilizer elements cancel their local simple-pole contributions when binomial(n,3) is odd. Even moving dimension can have opposite signs, explicitly at n=8. P-F44 derives the exact contribution to the full average polynomial by grouping balanced Brion characters over directed-cycle bases and Weyl permutations. Put P=(2^n−(−1)^n)/3 for3∤n. Its contribution is

`K_n = (1/(n P)) Tr_{Q(zeta_P)/Q}( product_{i<j<k} (1−zeta_P^{−((-2)^i+(-2)^j+(-2)^k)})^(−1) )`.

The moving normal representation is exactly the third exterior power of the specified cyclic representation. The complete global polynomial decomposes as `B_n=K_n+R_n`, with R_n an explicitly specified complementary balanced-cone sum. K_n vanishes for odd binomial(n,3). Neither a single large conjugate nor the trace gives a lower bound for U_n without control of the remaining signed coefficients and the possible constant-term cancellation.

**P-F43** resolves the previously quarantined binary-order12 source discrepancy. An actual homogeneous parameter system exists with five degrees5,544,000,000,005,544 and five degrees3,465,000,000,003,465. None is divisible by10. The proof combines scalar stabilizer orders, complementary degree-space base loci, a full incidence selection argument and an explicit generator/conductor bound. It refutes the literal necessity in BDPTheorem3.4(ii) at this input. It does not decide the much smaller degree tuple listed on Brouwer's page and makes no historical priority claim. Earlier quarantine notes remain as an audit history; the current B12-Q1 status is refuted.


**P-F45** proves the exact scope of the full cyclic-cubic-cover eigenspace model. Its Hodge numbers are binomial(n,3p+2−n). The full polarized classifying domain is a ball exactly at n4 and n5; at n6 it is typeI15,6, and at every n>=7 it contains a compact holomorphic projective line. This limits that particular growing-dimension proposal. It neither describes the actual restricted horizontal period image nor excludes selected Hodge structures, half twists or other theta constructions.


**P-F46** identifies the input of the named discriminant construction exactly. Ma's quasi-pullback theorem gives the vector-valued form `g=Theta_E6/delta`, of weight−9, with the discriminant groups glued with coefficient one. The zero component begins `q^−1+96`, and each nonzero component begins `27q^(−1/3)`. Every input coefficient counts pairs of an E6-coset vector and a24-colored partition; these are literal nonnegative integers. Its regularized multiplicative Borcherds lift restricts to the same weight48 form and hence to the degree80 discriminant. This supplies the exact positive-definite theta factor, not merely a group analogy.

Two precise limits are also proved. The unchanged input has an exponentially growing cusp term, so its ordinary Petersson norm diverges. Its input coefficient counts dominate the ordinary partition function and eventually exceed the polynomially bounded T5 Hilbert function under every positive affine reindexing. Consequently those coefficient spaces cannot themselves be all the graded plethysm spaces under that proposed dictionary. A comparison with the supplied unitary operations must identify the regularization and multiplicative transformation or a different explicit coefficient-space map. Subquotients, nonlinear transforms and other theta constructions remain open.


The same P-F46 form is exactly a **unitary Borcherds lift** in HofmannTheorem8.1. The complete lattice check gives Hermitian signature(1,10), trace latticeM without rescaling, the same dual/Weil representation, and the required isotropic pair. Hofmann's defining pullback equals phi; its multiplicativity identifies the inputs r*g with discriminant powers. Its initial discriminant-kernel group is not silently equated with the full period group; the latter follows from the already checked equality with phi. The remaining comparison is specifically with the supplied iterated totally definite unitary lifts, rather than a distinction between orthogonal and unitary group names.


## 13. Actual Fermat nonvanishing and its precise limits

**P-F47** proves an exact coefficient identity: the nth exterior power of the canonical volume tensor in the qth exterior power of the third exterior power of C^(3q) is nonzero exactly when an ordinary degree-nq cubic invariant is nonzero at the Fermat cubic. The proof matches the signed perfect-matching factorizations with determinant contractions, including every sign and factorial. This tests evaluation at one point, rather than nonvanishing of the whole invariant space.

**P-F49** gives actual invariants for every dimension. For a prime p congruent to1 modulo n, apply Cayley's degree-n contraction to the (p−1)/n power of the normalized Hessian determinant. The resulting cubic invariant has coefficient degree n(p−1), GL character det^(3(p−1)), and a proved nonzero Fermat value. A characteristic-p top-line calculation proves the needed determinant coefficient is a unit. Xylouris Theorem1.1 gives p=O(n^5.18) unconditionally. The supplied Dirichlet theorem discharges the precise GRH premise of Lamzouri–Li–Soundararajan Corollary1.2, giving p<=(phi(n)log n)^2 for n>=4. Thus the canonical realized stretch is less than gcd(n,3)(phi(n)log n)^2. This is a direct quantitative consequence of the supplied theorem in an actual plethysm family. The explicit contraction is not proved to have a small arithmetic evaluation circuit.

**P-F50** strengthens occurrence to an eventual-support theorem at Fermat. Two specified mixed-Hessian invariants have degrees2nu and2nv with gcd(u,v)=1. Their products show that every degree2nr with r>=(u−1)(v−1) occurs nontrivially at Fermat. Stabilizer characters exclude all other degree classes at this point. The conductor is O(n^20.72) unconditionally and less than (phi(Q)log Q)^4/4 under the supplied theorem, where Q<16n². The latter is O(n^8 log^4 n). Combining the conductor with the odd top-exterior invariant gives full actual support at every stretch s>=2C_n+r0 on the infinite family n=binomial(3r0−1,2), odd r0>=3. These results do not bound GCT VI's strict indices, which test constituent polynomials outside their own residue classes.

**P-F48** closes the proposed density amplification using cubic rectangles and their inner/outer determinant twists. In the exact bit-length shells used by narrow SH(b), their conditional densities are bounded respectively by16N*2^(−3N/10) and16N(N+1)^3*2^(−N/4). For the canonical unified input specification, the ambient rank contributes to length; allowing all admissible padded ranks adds at most one factor of N, with the explicit constants proved in the paper. The unscaled cubic family has initial multiplicity zero and is excluded from the source's nonzero population. Neither these sparse families nor a redefinition of the input distribution settles SH(b).


## 14. An exact definite-unitary source for the E6 factor

**P-F51** realizes the particular positive theta vector in P-F46 as a normalized ordinary theta integral from a definite U(3) group. The Hermitian space has exactly E6 as its trace lattice. A compact open subgroup fixes every discriminant coset, and the source function is the nonnegative normalized indicator of the identity lattice double class. Integrating against it selects the individual lattice theta series, with no genus average or omitted mass factor. The displayed identity includes the exact y^(−3/2) factor.

The underlying symplectic space carries the explicitly checked seesaw pairs (O(6),SL2) and (U(3),U(1,1)). The classical target is the derived split unitary group SL2, with the canonical orthogonal Weil action fixed. Component theta series have weight3 and levelGamma(3). The paper does not presume compatible splitting characters for an unspecified full-unitary lift.

This closes the previously missing definite source for the actual E6 factor. To identify the full discriminant construction with the supplied method, the remaining operations are now explicit: selected-vector/splitting comparison with the note's totally definite chains, multiplication by the inverse elliptic discriminant, and the regularized multiplicative lift. Convergence of the E6 theta integral does not remove the full input's cusp divergence proved in P-F46. The output currently identified is the cubic discriminant and its powers, not all multiplicity-space basis vectors.


## 15. Actual nonstandard central action and geometric full-input coefficients

**P-F52** closes the missing finite operator comparison from P-F39. The explicit word `Z=(Q1−Q2)^2+S−f²` is central in the actual cubic nonstandard algebra. A complete factorization of the source relation and cell element proves that it acts by the two required conjugate scalars. The descended source basis gives exactly the earlier two-by-two matrix, and four copies occur on the eight-dimensional descended two-sided ideal. An explicitly verified positive tensor Gram form makes Z strictly positive for every real q>0. The proof does not use the source's inconsistent printed triangular generator matrices; their discrepancy is recorded.

The unscaled trace and norm still have negative Laurent coefficients. Moreover the different normalization `H=(q+1+q^−1)^4` produces positive symmetric Lefschetz trace and norm, although it is not divisible by the prescribed factor F. Thus these finite positive-action and determinant conditions do not determine the canonical normalization. The remaining comparison needs the prescribed integral/lattice or canonical-basis data, product compatibility, and uniform tensor-degree control.

**P-F53** gives actual smooth projective coefficient spaces for the entire exact input `Theta_E6/delta`. For each coset and exponent, take the finite disjoint union of K3 Hilbert schemes indexed by lattice vectors x with Hilbert-scheme length a+1−Q(x). Goettsche's formula proves that its total cohomology dimension is exactly the input coefficient and that its odd cohomology vanishes. Purity holds separately in each cohomological degree; the spaces are not generally Tate. The principal-part spaces are one point, a K3 surface together with72points, and27points in each nonzero coset, yielding1,96,27,27.

The inverse-discriminant factor is also the completed product of symmetric-power operations on the24-dimensional ungraded cohomology of the K3 surface. This is a precise lambda-ring identity at the level stated in the proof. The model gives geometric sources for both factors of the named input, but the regularized multiplicative transformation and a map to all GCT multiplicity spaces remain unresolved. The earlier growth obstruction rules out simply identifying these full coefficient spaces with the cubic grades by affine reindexing.


## 16. Polynomial actual support in every large cubic dimension

**P-F54** proves a uniform unconditional actual-support theorem for every n>=33. The paper specifies one cubic F_n by a Fermat tensor plus a small, phase-labelled linear-hypergraph perturbation. Its one-factor partial trace is exactly scalar, so no unquantified balancing step is used. For every d>=(10n)^200 satisfying n|3d, a homogeneous degree-d SL_n invariant is nonzero at F_n. Equivalently, every canonical stretch s>=ceil(gcd(n,3)(10n)^200/n) has f_n(s)>0.

The proof separates all noncentral Fermat symmetries quantitatively, proves a global overlap gap, and compares the compact average's positive central neighborhoods against its tail. The phase estimates and Haar-volume bound retain their full dependence on n. The resulting normalized integral is the squared norm of an invariant projection and is strictly positive. This gives existence and an explicit averaging formula, not an efficient evaluation circuit.

This closes the remaining full actual-support question for this asymptotic cubic family. Strict PH2/SH still require positivity or coefficient positivity of every constituent polynomial at common arguments, including arguments outside that constituent's own residue class. P42's refined tail bound now leaves an exact signed lower-polynomial test at every polynomial argument; it does not supply that last comparison.

### Additional ordinary-lambda and Frobenius limits in P-F52

The exact prescribed normalization has now been traced to the actual braid operator's spectral-denominator product. After its specified cancellation and centering, F=q^(-16)(1+q+...+q^9)^2(1+q²)(1+q^12). Its provenance is fixed by that source rule, while positivity alone does not force the rule.

There is also an exact obstruction to combining the two positive coefficient models as ordinary lambda operations on one object. If JT and J²N were the characters of V and its second exterior power for a common scalar J regular and nonzero at1, their dimensions would force65 dim(V)=121. This is impossible, including for virtual ordinary graded classes. For the prescribed F, the two dimensions are17600 and71680000, whereas the second exterior dimension would be154871200. Newton's trace identity also excludes a single fixed Frobenius whose traces and exterior-square traces equal this pair at q=p^r for every r. These statements leave different operations and traces of additional endomorphisms open; they do not contradict the actual central determinant.


## 17. The same input gives the six-variable discriminant

**P-F55** identifies a second actual invariant output of the exact E6/discriminant theta input. On the orthogonal domain of signature (2,20), the weight48 quasi-pullback has determinant multiplier. Its square has trivial multiplier and weight96. Looijenga's cubic-fourfold ring isomorphism doubles automorphic weight, so the square maps to the degree192 discriminant of six-variable cubics, in canonical stretch96 and GL6 character det96. A full nodal-incidence argument and equality of degrees identify the polynomial without assuming an orbifold divisor convention.

The known cyclic discriminant formula of Buse-Jouanolou Example4.10 becomes Delta6(a w³−f)=3^33 a^32 Delta5(f)^2 in that source's normalization. Restriction of the same orthogonal form to the existing cubic-threefold ball gives precisely the matching square of the five-variable discriminant. This is compatibility of the named forms and their powers; the affine substitution a=1 is not asserted to preserve grading on the full rings. The comparison remains fixed-dimensional and does not settle the uniform multiplicity or strict-index questions.


## 18. A direct signed-wave test for the strict cubic indices (2026-11-21T03:56:05.691414+00:00)

P-F56 proves the maximal two-part of the actual Hilbert-pole period and shows that subtracting constituents half a period apart leaves only the primitive2^(n-1) wave. Every valid positivity or strict-saturation shift forces f_n(x)>=2W_n(x) at every later integer. This compares a signed cyclotomic trace with an actual multiplicity, which has an elementary ambient-dimension upper bound; the average polynomial and all other Hilbert poles cancel exactly.

The specified conjugate pair a*=(3g)^(-1) has amplitude at least2^(n^4/24-2n^3). If the summed absolute magnitude of all other primitive coefficients is at most one quarter of that amplitude on an unbounded dimension set, a positive witness occurs in every window of at most9 consecutive integers. This would force p(f_n)>2^(cn) and s(f_n)>=2^(cn) for every fixed c<1/4. The remainder estimate is unproved. Exact finite experiments show strong sign variation and do not prove its asymptotic version. P56 also gives the complete positive normal-weight multiset and an exact coefficient formula in Q[t]/(t^(2^(n-2))+1), making the remaining signed calculation explicit.

## 19. Completed theta operations and an actual positive central order

P53h-p now expresses the known normalized Borcherds cusp product as the completed exterior Euler character of the actual K3-Hilbert coefficient cohomologies. A rational chamber height makes every truncation finite, and a formal Mobius inverse recovers all input coefficients. A finite virtual positive-height graded object cannot give the same exterior character. This identifies the operation at the completed character level; it does not construct a map to all cubic multiplicity spaces or identify the supplied totally definite theta chain.

P52y-as realizes the source-normalized central operator through an explicit positive Laurent quadratic order and an additive functor built from finite Tate-Lefschetz coefficient spaces. The Grothendieck-group action is intertwined with the actual source action. The positive basis lies in a genuine integral internal-bar-fixed source word lattice. Its global generator does not belong to the two specified rescaled generator forms, and the change to the displayed candidate canonical basis has a negative coefficient. These results close the finite central comparison while leaving full canonical products, external minimum-degree compatibility, monoidal structure and uniform families open.


## 20. Two smaller comparisons in the actual dyadic and nonstandard models

P56aa-aj gives an exact recursion of the positive normal-weight product as dimension increases. Each increment has binomial(n-1,2) factors. A uniform bound on the sum of the two child increments, with a fixed contraction factor below one, would force the complete unwanted mass to tend to zero. The two selected sibling errors are already at most2^(-n³/12) for n>=48. The uniform contraction is not proved. A maximum-child estimate without the sum would lose a factor of two and is not substituted for it.

P56ak-au proves a separate unconditional reduction of that mass: all normalized multipliers3<=J<=2^(delta n), for every fixed delta<1/600, contribute a negligible total compared with the selected pair. The proof uses an odd-numerator separation estimate for sparse dyadic sums, retains all omitted normal weights, and gives an explicit100n²ceil(log2(16J))² error. ForJ<=2^(n/100000) the total ratio is at most2^(1+n/100000-(log2 3)n³/36). The far multipliers remain unbounded. This is a strictly smaller remainder estimate, not a proof of PH2/SH failure.

P52av-bc extends the actual central comparison to a four-dimensional source left ideal. Four specified integral, internal-bar-fixed vectors form a lattice stable under both chosen rescaled generatorsFQ1,FQ2, with nonnegative Laurent matrices. All positive words inherit that property, and explicit additive functors have precisely those matrices on their Grothendieck group, with the actual source intertwiner. This closes the finite full-generator action substep. It does not establish coherent mixed relations, source canonical products, or a uniform geometric/theta family. The complementary generatorsFPi cannot be simultaneously nonnegative in the same basis when the actualQi do not commute, becauseFQi+FPi=FfI would force all four matrices to be diagonal.


## 21. Quadratic functor relations and compatible positive Gram data

P52bd-bl improves the finite nonstandard comparison in two precise ways. The two explicit matrix functors have natural quadratic isomorphismsE_i² ≅ H⊗E_i, compatible with every run of equal generators. Their ordinary adjoints in the direct sum of graded vector-space categories do not match the source involution, because transpose-dual matrices reverse their one-way nonzero blocks. This limitation belongs to that explicit categorical model.

The actual four-dimensional matrices nevertheless admit an explicit symmetric, reciprocal Gram matrix with nonnegative integer Laurent coefficients, andH A_i=A_i^T H. The form is positive definite for q>0,q≠1 and positive semidefinite of rank3 atq1. The proof uses the two real embeddings of the actual quadratic source field and exact positive factorizations for the source eigenvalues and their complements. Thus there is no numerical adjoint obstruction at generic positive parameters. The remaining question is a category whose Hom compositions, adjunctions and mixed length-eleven relations realize these exact data compatibly with the source canonical construction. Pairwise coefficient spaces alone do not supply those operations.
