# What the findings change

## 1. The positive mathematical answer

Projective and injective norms do give certified lower bounds for rank and border rank, but the conversion must identify the decomposition model and the geometry being tested. The paper establishes three distinct mechanisms.

First, for a nonzero tensor of order d>=2, intrinsic support dimensions yield the valid inequality

BR(T) >= ceil((pi(T)^2 / HS(T)^2)^(1/(d-1))).

The analogous expressions using HS(T)^2/epsilon(T)^2 and pi(T)/epsilon(T) also work. This conversion is always dominated by a mode-flattening rank. Exact knowledge of the full Hilbert norms therefore does not, through this formula, improve a basic flattening (F-01).

Second, matrix nuclear/operator norm certificates for a specified linear map Phi give border-rank lower bounds after dividing by the pure-tensor matrix-rank cost. Finite positive-semidefinite witnesses certify the relevant norm bounds. With arbitrary invertible matrix preconditioning their optimal strength is exactly the rank certificate of that same map. This includes ordinary and Koszul flattenings; it does not say that every norm-assisted method is a linear flattening (F-02, F-12).

Third, norms on the entire flattening image give additional information. If U is a q-dimensional image with q>0 in b>=2 remaining factors and alpha(U) is the maximum squared length of the projection of a unit pure tensor to U, then

BR(T) >= q + ceil(alpha(U)^(-1/(b-1))) - 1.

The proof combines a uniform injective-norm estimate with border substitution. Equivalently, alpha(U) is the injective norm of the orthogonal projector regarded as a tensor with conjugate factors. This route depends nonlinearly on the image and tests a secant-incidence condition (F-13).

The explicit bounds include the following. For all four determinant/permanent rows, assume n>=3 and put h=floor(n/2), b=ceil(n/2).

| Tensor convention | Proved bound |
|---|---|
| Square matrix multiplication M_n | CP border rank at least n^2+n-1 |
| Row determinant D_n, h=floor(n/2), b=ceil(n/2), n>=3 | At least binomial(n,h)+b-1 |
| Row permanent P_n, n>=3 | At least binomial(n,h)+1 |
| Symmetric determinant polynomial tensor | At least binomial(n,h)^2 + ceil((n^b/binomial(n,b))^(1/(b-1))) - 1 |
| Symmetric permanent polynomial tensor | At least binomial(n,h)^2+1 |

All these are CP border-rank lower bounds over the complex numbers and also hold for real Euclidean border rank. The polynomial bounds consequently also apply to symmetric border rank. The calculations do not replace a complex image by its real points.

An additional coordinate restriction sharpens the image method for all four determinant/permanent families. Every nonzero element of a residual b-factor image restricts to a smaller size-b tensor of the same family, and a basis element realizes that minimum. Thus

min(nonzero u in U_(n,b)) BR(u) = BR(T_b),

and

BR(T_n) >= binomial(n,b)^s + BR(T_b) - 1,

where s=1 for row tensors and s=2 for polynomial tensors (F-23). This is an exact reduction to a smaller CP border-rank problem. It gives 39 for both degree-four polynomial tensors. Using the cited CP equalities BR(det_3)=17 and BR(per_3)=16 gives determinant size five at least 116 and permanent size five at least 115; at size six the corresponding bounds are 416 and 415. These comparisons carry no priority or current-record claim.

## 2. Why a large nuclear norm is not a large tensor rank

For M_n the three matrix-inspired ratios are all n^3. Yet M_2 has a seven-term decomposition. Its grouped tensor powers have rank at most 7^k while the ratios are 8^k. Therefore no fixed factor, including any fixed power of a Grothendieck constant, makes these ratios direct rank lower bounds (F-05).

The same failure occurs along the four determinant/permanent families. The finite sign averages in F-04 prove exact nuclear norms for the normalized polynomial tensors while also giving rank upper bounds that contradict the proposed constant-factor conversions asymptotically.

The rank-two approximation of W explains the geometric obstruction. The limit has rank three and border rank two; the total normalized-term weights of two-term approximating decompositions must tend to infinity. A duality certificate with a bound on each coefficient is valid for that bounded-summand model, but such a bound cannot be silently imposed on unrestricted border rank (F-06, F-07).

These are limitations of explicit formulas. They are not an impossibility theorem for every norm, every semidefinite hierarchy, every nonlinear construction, or every geometric method.

## 3. What Grothendieck's inequality actually certifies

The classical inequality compares the Boolean sign optimum Q(A) with the vector semidefinite optimum S(A). Exact primal and dual witnesses with values L and U give

L <= S(A) <= U, and L/K <= Q(A) <= U

for a valid upper bound K on the real Grothendieck constant (F-09). Dividing a primal value by K gives a lower bound on the sign norm. It does not give the Hilbert spectral upper bound needed in a naive tensor-rank calculation.

There is a valid dimension-sensitive rank test. A rank-q real matrix has an optimal vector solution in dimension at most q. Therefore a certified L>kappa_s U, with kappa_s>=K_G(s) and a separate upper certificate U for Q(A), proves matrix rank>s. The package includes rational Gram data and an exact Boolean SOS identity for a nontrivial example (F-11).

For the natural flattenings of the five tensor families, the signs can be removed blockwise and Q=S=sum of absolute entries. Their Grothendieck gap is one. The direct unscaled conversion to Hilbert tensor norms is also trivial for the precise reasons proved in F-10. Other maps, preconditioning, noncommutative inequalities, or stronger SOS relaxations are outside that negative statement.

The UGC threshold remains the one in Raghavendra–Steurer, Theorem 1.1 and the algorithm proof in section 3.3. Under UGC, a loss factor strictly below K_G is NP-hard; an impossibility statement for polynomial algorithms also assumes P!=NP. Algorithms achieve reciprocal guarantees arbitrarily close to 1/K_G. None of F-01–F-23 improves the constant or changes that threshold.

The numerical intervals in the paper are explicitly attributed to the primary 2026 preprints located during this run. Their large computational certificates were not rerun; no exhaustive best-bound claim is made. All rank proofs are independent of those endpoints.

## 4. Consequences for GCT and P versus NP

The report does not prove a separation of complexity classes, a matrix-multiplication exponent greater than two, or superpolynomial determinantal complexity.

The distinction is mathematical. A tensor decomposition into products, or a symmetric decomposition into powers, is a restricted representation. The determinant polynomial already has exponentially large central catalecticant ranks while admitting efficient arithmetic evaluation. Thus a large CP or Waring rank does not by itself imply hardness for unrestricted arithmetic circuits.

Similarly, a norm computed using a selected Euclidean metric is not invariant under the full general linear group relevant to the determinant–padded-permanent orbit problem. The group preserves rank but changes norm ratios (F-19). An orbit-closure obstruction needs equations or appropriately tensor-dependent representation data for those orbits.

Bürgisser–Ikenmeyer–Panova's no-occurrence result is kept in its exact range, n>=m^25 in the supplied v3 Theorem 1.4. Inclusion of occurrence supports is weaker than an equivariant coordinate-ring quotient and does not prohibit multiplicity obstructions. Nothing in the norm argument strengthens that theorem to orbit inclusion or to a universal GCT barrier.

The concrete further gate is now better specified: either certify stronger residual-image avoidance, or exploit F-23 and obtain sharper CP border-rank information for smaller members. A generic efficient projector-norm algorithm would require a new theorem; classical Grothendieck SDP alone does not supply it.

## 5. What transfers to Grothendieck's frameworks

The translation has genuine algebraic content:

- The universal sum of pure tensors defines an affine scheme-theoretic image over Z. Its integral equations vanish after every base change. Flat base change to the complex numbers gives the usual secant cone, while reduction modulo a prime requires care (F-15).
- Koszul flattenings are contraction-and-exterior-multiplication morphisms of locally free sheaves. Their minors and Fitting ideals express rank conditions integrally (F-16).
- A Hilbert–Grassmann graph closure retains a limiting zero-dimensional scheme together with its limiting span. The actual span of the limiting scheme need not equal that limiting plane (F-17).
- The image method is avoidance of a closed Segre-secant incidence locus in a Grassmannian. Coordinate quotients of free sheaves give the smaller-family restriction in F-23 (F-18).
- Lambda-operations and Schur functors describe the bundles and their representation types. K_0 classes of the source and target, even with all lambda/gamma operations, do not determine the rank of the arrow between them. Zero and identity are an exact counterexample (F-20).
- Constant étale stalks, weight-zero purity of abstract rational points, and their absolute unit motives do not retain the embedding information that distinguishes a zero tensor from a nonzero pure tensor. This does not rule out more informative tensor-dependent sheaves or relative motives (F-21).
- The normalized symmetric Hilbert tensor divides coefficients by n!. The integral polynomial and its Hasse catalecticant instead use the divided-power dual domain. These are kept distinct in small characteristic (F-22).

The analytic ingredient remains a metric on a real or complex fiber. It is not silently replaced by an algebraic norm over Z.

## 6. Exact historical anchors

The original Résumé is identified by the published-work catalogue identifier CSG17. The 1996 USP facsimile preserves the original internal pages. Its page 8-prime makes scan offsets nonconstant:

| Construction | Original locator | One-based scan leaf |
|---|---|---:|
| Projective/injective constructions | Section 1, no.1, Definition 1 and Theorem 1, printed p.8 | 8 |
| Universal property and duality | Section 1, no.1, Theorem 2 and its corollary, printed p.8-prime | 9 |
| Fundamental Grothendieck comparison | Section 4, no.2, Theorems 1–2, printed pp.59–60 | 60–61 |
| Inequality used in the dictionary | Corollary 1 after Theorem 3, inequality (8), printed p.61 | 62 |
| Beginning of proof | Section 4, no.3, printed p.62 | 63 |

Facsimile: https://revistas.usp.br/resenhasimeusp/en/article/download/74836/78406/100978

Catalogue: https://csg.igrothendieck.org/published-works/

CSG17 is not presented as an unpublished Montpellier manuscript shelfmark. No separate manuscript cote was established. The paper gives exact EGA I, SGA 3, SGA 6, FGA, SGA 4, and Weil II locators and scan leaves where verified. It does not invent a theorem in SGA 5 or a manuscript reference for a weight-to-rank implication that has not been proved.

## 7. Verification boundary

Every new finding has a full written proof and a recorded whole-proof model check. Separate agents reconstructed the principal image, norm, and certificate arguments. Exact computation scripts check Strassen's decomposition, the five-term D_3 identity, the rational W margin, and the rational SDP/SOS data. This is not proof-assistant verification or external peer review.

Cited deep results, including the recent computational rank results and numerical Grothendieck endpoints, remain cited background. Their statements, normalizations, scopes, and locators were checked as recorded; their complete proofs and large certificates were not all rerun.
