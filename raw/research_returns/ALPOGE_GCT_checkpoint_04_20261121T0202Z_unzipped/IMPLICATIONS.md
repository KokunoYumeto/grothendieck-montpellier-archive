# What the findings change

**Research status:** both clauses of ordinary plethysm PH3 are refuted: P-F19 treats canonical parameter degrees, and P-F30–P-F31 prove actual exponential-order Hilbert poles that refute the numerical positive-form clause. Narrow PH2/SH, uniform effective shifted counting and the asymptotic determinant/permanent obstruction remain open. P-F14–P-F15 also refute the broader rank-only subgroup-restriction index hypotheses. The supplied Alpöge and OpenAI results are used as cited theorems with their stated scopes. No P versus NP or ordinary complex-field VP versus VNP resolution is claimed. “Finding” denotes a deduction proved here, not a certified claim of historical priority.

All GCT VI hypothesis numbers below refer to the supplied arXiv:0704.0229v4 text. Its broad subgroup-restriction problem, irreducible-inner problem and ordinary GL_n plethysm subfamily are kept distinct.

## Priority of the conclusions

| Rank for the requested program | Findings | What they settle |
|---|---|---|
| 1 | P-F19, P-F30–P-F31 | Both printed PH3 clauses fail inside ordinary cubic plethysm. No purity proof can establish those false bounds. |
| 2 | P-F1, PLE-F5–PLE-F8, P-F7, P-F10 | Qualitative purity, even for the actual positive-basis multiplicity algebra, does not repair homogeneous PH1 or supply quantitative counting and index bounds. |
| 3 | P-F11–P-F12 | A fully proved polynomial numerical estimate gives the valid conditional implication from bounded positive Hilbert data to PH2. Its printed PH3 premise is false in general. |
| 4 | P-F34, P-F36 | Two concrete remaining requirements: a cubic average-polynomial bound for an index refutation, and a nontrivial quadratic descent datum for a direct nonstandard realization. Neither missing construction is assumed. |
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

If the coefficient norm `U_n=sum_j |[x^j]B_n(x)|` satisfied `U_n <= 2^(C n³ log₂(n+2))` with an absolute C, then both p(f_n) and s(f_n)+1 would be at least `2^(n/32)/(n+2)^(6C)` for all sufficiently large n. That would refute narrow polynomial PH2 and SH(a). **The U_n estimate is unproved.** The result gives a necessary inequality and a precise sufficient remaining condition, not an equivalence or a completed refutation. P-F33 prevents replacing this missing estimate by a generic normality, rationality or Gorenstein argument.

**P-F35** supplies an exact small-dimensional calibration. Salmon's quaternary-cubic ring gives

`H_4(t)=(1+t^25)/((1-t²)(1-t⁴)(1-t⁶)(1-t⁸)(1-t^10))`.

The written proof extracts closed constituent formulas and checks every shifted coefficient uniformly. It proves `p(f_4)=s(f_4)=23` and minimal period120. The lower bound uses the actual hole at23 and nonzero degree-four constituents; the upper bound is coefficientwise positivity after that shift. No extrapolation to larger n is made.

## Next main step

Attack the explicit cubic average-polynomial estimate in P-F34, while retaining direct PH2/SH and effective shifted-counting routes that do not depend on it. Both canonical parameter degrees and numerical positive-form denominator weights fail the printed polynomial PH3 bound in general. P-F11–P-F12 remain valid conditional tools, and P-F13 makes candidate verification finite when an appropriate bound is supplied. The nonstandard route must additionally handle the descent requirement proved in P-F36. To reach an obstruction, an index or counting result must still be joined to control of actual coordinate-ring quotient ranks and a strict asymptotic comparison. Those tasks remain open in this run.

### Sharper remaining ordinary-index gate (P-F34, P-F38)

The actual complex pole amplitude has log2|A_n|=n^4/24+O(n^3). A sufficient condition for exponential positivity and saturation indices is limsup(log2 U_n)/n^4<1/24, where U_n is the coefficient l1 norm of the pole-at-one polynomial. This condition is unproved. P-F38 constructs explicit nonnegative 0/1/2 vector-partition matrices with column sums at most3, cubic-scale dimension, and unit-box polytopes whose corresponding norm is at least2^(n^4/2). The actual complete cubic weight list and Weyl alternating numerator are therefore essential to any proposed smaller bound; small entries and dimension alone do not suffice.
