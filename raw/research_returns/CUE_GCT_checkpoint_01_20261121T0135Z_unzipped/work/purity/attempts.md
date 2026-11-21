# Purity-track attempts and gates

Run CUE_GCT-20261121-purity, GPT-6 Astra Pro, effort not exposed. The P-identifiers denote deductions developed and checked in this run, not historical-priority claims. All explicit proof checks are self-review unless an independent agent records otherwise.

## 1. Translate square-root cancellation into a hitting assertion

Started with the strongest directly useful consequence of pairwise small bias: positivity of the monomial-evaluation Gram matrix. Expansion and Cauchy–Schwarz give P-01. The sufficient error is inverse in the number of participating monomials (or a coefficient-energy ratio), which is the first quantitative gate. Width is not a bound on that quantity.

Applied the quadratic-character trace sampler (AGHP §4) and proved the explicit O(n²s²) sparse multilinear hitting set P-02, including an integral-minor argument to transfer from complex positivity to arbitrary characteristic-zero coefficient fields. This is a positive result and uses no number-field RH.

## 2. Attack the direct small-bias-to-ROABP claim

A proper sign sampler misses the width-one polynomial concentrated on any omitted cube point: P-03(a). This is an exact, structural counterexample and persists even if the sampler has excellent linear bias. The proposed common affine shift/scale repair was then tested. All outputs still use at most two values, so the nonzero three-variable Vandermonde vanishes. An explicit width-three, individual-degree-two ROABP was constructed and symbolically checked: P-03(b). These attacks concern specified samplers, not general ROABP hitting-set impossibility.

## 3. Attempt Schwartz–Zippel on geometric grids

For a curve-based grid, replace the usual product-grid root count by a divisor degree bound plus Weil's rational-point estimate. This proves P-04 precisely when the restriction of f to the curve survives. It does not show survival. To quantify that missing condition, a finite union of rational-function curve images was attacked by a bivariate dimension count: P-05 constructs a nonzero annihilator with individual degree at most twice the total pole budget and correspondingly small ROABP width. Hence a low-complexity geometric image can impose algebraic identities even though every available trace sum exhibits cancellation.

## 4. Retain the actual monodromy function space

P-06 uses pairwise geometrically inequivalent pure irreducible sheaves rather than an unspecified claim of equidistribution. The cohomological Gram estimate is proved with explicit B=max h_c¹ and threshold q>s²B². Added the exact Euler–Poincare formula B_ij=δ_ij+r_i r_j(2g−2+b)+Σ Swan(G_ij), exposing the rank, genus, boundary, and conductor budget. A Kummer example at p=101 was checked exactly, with Q=98 and Gram determinant940800. This checks a concrete example; it is not a computational proof of the general sheaf statement.

The unresolved step is to realize an entire ROABP class, with its arbitrary cancellation, as a controlled independent trace-function space on one explicit sampler. Neither purity nor monodromy terminology constructs that realization. Products of sheaves can increase representation count and conductor; replacing all of these by a polynomial in width without proof is invalid.

## 5. Continue with an explicit support-sensitive weight family

Instead of stopping at counterexamples, constructed P-07: w_i(t)=1+rep_p(t^i), with p>max(2,d,n binom(s,2)). Pair collisions imply roots of a nonzero degree-n polynomial; a union bound leaves a seed distinguishing all support weights. Univariate evaluation gives p(ndp+1) hitting points. Exact finite-support checks passed for 126 and2925 supports in two sample parameter sets. The construction is polynomial for bounded sparsity, permits arbitrary coefficients, and is elementary; the missing extension is to compressed coefficient dependencies/basis isolation for general ROABPs.

## 6. Make a conditional number-field transfer precise

P-08 isolates the precise arithmetic gate: one common finite Galois extension, polynomial log-discriminant/degree, and a uniform evaluation map such that a conjugacy class certifies each nonzero polynomial. Effective Chebotarev then yields an enumerably small hitting set. For abelian extensions the stipulated Alpöge input discharges the required Dedekind GRH through Dirichlet factorization; for arbitrary extensions the claimed Masullo Hecke statement would do so conditionally. The common encoding and nonvanishing implication remain unconstructed. A polynomial-dependent field would not define a uniform black-box hitting set.

## 7. Audit the zero-statistics consequences

Exact supported Montgomery normalization was derived from its form-factor theorem. Hughes–Rudnick's principal analytic formulas were found already unconditional; only their real-zero interpretation and §8 GRH applications are newly discharged under the input convention. ILS target cuspidal and symmetric-square RH is outside Dirichlet/general Hecke-character GRH, and its Hypothesis S is a separate prime-sum assumption. Gao–Zhao gives an explicit conditional-on-M Hecke-family example. Fixed-parameter function-field equidistribution was kept separate from Sawin's stronger cohomological/degree-aspect gates. CFKRS arithmetic moment conjectures and quantum-chaos spectral constructions are not consequences supplied by RH alone.

## 8. Independent cross-review performed

Read root G-01–G-06 completely, requested three precision repairs, and reread/accepted the revisions. Reports/events are in work/root/independent_review_purity*.

Read isolation I-01–I-11 completely, independently checked the key rank/probability/conditional-transfer arguments, requested V=span coefficients explicitly in I-03, and accepted the revised wording. Reports/events are in work/isolation/independent_review_purity*. These are targeted whole-proof reviews, not claims of independent reproof or formal verification.

Further source audit: Sawin Corollary1.8 already proves the unbalanced r_-=1 case with an explicit degree-aspect error. This was added to avoid implying all stronger degree-aspect instances remain conditional. CFKRS main conjecture/CUE theorem are §1.5, Conjecture1.5.1 and Theorem1.5.2; recipe §2.1 is distinct.

## 9. Attack approximate positive energy, then weaken the target

Parent proposed the product-vector leverage/trace argument. Verified it and strengthened its presentation to arbitrary two-sided constants a,b: M≥D a/b, D=(δ+1)^n, already for width-one products and arbitrary complex evaluation nodes with nonnegative weights. Summing the D normalized product monomial inputs replaces the proposed Haar average exactly. At each node the conjugate normalized evaluation tensor is itself an allowed product input, proving its leverage bound. This is P-09. The exact ε=0 barrier was already in isolation I-13; P-09 supplies the quantitative approximate extension.

Primary literature check found a related matrix statement in Cai–Zhang (2015), Lemma2.1, p109, for Gaussian rank-one measurements. Their ℓ₁ alternative illustrates why an ℓ₂ energy obstruction need not obstruct recovery. Did not read the supplemental proof or claim the exact weighted tensor statement appears there. A 2024 search hit made a broad rank-one RIP claim; it was not used as authority for this deduction, whose deterministic proof is explicit.

P-10 switches to the exact hitting criterion: the evaluation kernel avoids the closed cone of bounded TT rank. On its compact unit sphere, this is equivalent to some positive energy lower bound, but any such sampler has energy condition ratio at least D/M. Generic dimension-cutting supplies q_w=dim(TT cone) points, with q_w≤n(δ+1)w², and hence proves that the obstruction is not polynomial cardinality in characteristic zero. It does not derandomize the construction or bound integer coordinate heights. The fixed-width-one case is completely explicit and optimal: nδ+1 diagonal evaluations suffice; ≤nδ arbitrary evaluations are killed by partitioning their indices among the n root factors. Parthasarathy's known completely-entangled-subspace construction was located and credited, and the full short proposition proofs were read. Oseledets Theorem2.1 supplies the standard exact TT-rank characterization; its complete proof was read as well.

## 10. A number-field refinement that collapses to elementary interpolation

Initially pursued a legitimate refinement of P-08 allowing finitely many f-dependent bad primes. Given a common Galois field E and a nonzero integral value β_f, put R_f=Norm(β_f). For a known bad-prime integer B, the auxiliary quadratic field Q(sqrt(2 rad_odd(|B R_f|))) makes every prime dividing B R_f ramified. Its discriminant is at most8|B R_f|; the compositum with E has degree at most2[E:Q] and logarithmic discriminant at most2log|Δ_E|+[E:Q]log(8|B R_f|), by the product-integral-basis discriminant bound when the quadratic field is disjoint, and immediately otherwise. A splitting prime supplied by Chebotarev avoids all bad primes. A uniform norm-height bound would let the algorithm enumerate a fixed small prime interval without factoring R_f or constructing the auxiliary field. This route would need Dedekind GRH for the auxiliary composita; abelian E would let the stipulated Dirichlet GRH suffice.

Before promoting this to a main result, checked whether its encoding assumption already solved the problem. It does. With explicit primitive-element coordinates α_i=A_i(θ)/b of polynomial degree, nonvanishing f(α) implies the bivariate polynomial f(U A_1(T),…,U A_n(T)) is nonzero at (1/b,θ). Its separate degrees are nδ and nδ·max degA_i, so a small integer product grid produces an unconditional hitting set. The additional U variable clears all coordinate denominators without needing integer-valued interpolation. This removes every analytic, discriminant, height-of-f, and bad-prime requirement of the proposed number-field specialization. It is P-11; the dominated Chebotarev refinement is retained here only as the actual attempted route.

Parent suggested the reverse construction: interpolate an existing integer hitting set by rational coordinate polynomials and evaluate at a cyclotomic root whose minimal-polynomial degree exceeds the composition's degree. Proved the converse with common denominator (M−1)!, explicit polynomial coefficient heights, and prime cyclotomic degree/discriminant bounds. Therefore explicit polynomial-degree common algebraic-point encodings and polynomial-size integer hitting sets with polynomial coordinate heights are polynomially interconvertible for rational-coefficient classes. This is a reformulation of the gate, not a new derandomization supplied by GRH. The reverse implication is expressly restricted to rational coefficients.

Actual restricted constructions remain available: a common cyclotomic coordinate hits every rational width-one product when its minimal-polynomial degree exceeds δ, but x1−x2 defeats it already at width two. P-07's bounded-sparsity hitting set gives a larger restricted cyclotomic encoding via interpolation, again without GRH. No genuinely broader general-width class was obtained from arithmetic alone.

## 11. Later independent reviews

Read complete R-09, including exact Bump–Gamburd stable denominator parameters, all determinant twists, power2nd, factorial normalization, and full-character-norm cutoff. Requested and then reread S_0=0 and ℓ(λ)>n² vanishing repairs; the revised proof passes. Reports/events are in work/rectangular/independent_review_purity_R09*.

Read and attacked complete root G-09: quotient/remainder exponent routing, path uniqueness, tree and chain counts, homogenization, arbitrary field-linear padding, and O_k(m^((k−1)/2)) asymptotics. Finite exact path/count and determinant checks were run and recorded separately. Located the pre-existing sharp asymptotic theorem of Boralevi et al. (2017), Theorem1.3, p417, so no priority is claimed for the order bound. Reports/events are in work/root/independent_review_purity_G09* and G09_purity_computation_results.txt.
