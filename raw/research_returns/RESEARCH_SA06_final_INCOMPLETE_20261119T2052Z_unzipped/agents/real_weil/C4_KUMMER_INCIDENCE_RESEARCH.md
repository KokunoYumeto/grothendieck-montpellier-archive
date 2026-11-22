# The generalized Kummer fourfold incidence route: an exact integral exclusion

**Status: complete auxiliary proof with independent mathematical passes conditional on the geometric input; that input's normalization is explicitly reconstructed in Section3.1 and the primary-source read scope is finalized in Section8. No main-gate movement, no algebraicity counterexample, and no priority claim.**

Credit: GPT-6 Astra (OpenAI), ChatGPT Pro mode, RESEARCH_SA06, run `/root/component_families`; effort setting not separately exposed. Research date: 19 November 2026, after checkpoint22.

## 1. Why this is a different construction

The current C.4ab gate asks for an integral codimension-two correspondence on a type-(1,2) abelian surface whose actions t on H1 and s on the transcendental H2 satisfy t−s odd. The preceding semihomogeneous, fixed-surface Orlov, graph, Prym, and Lagrangian-divisor methods do not exhaust positive-square sheaf moduli. A natural next construction is the Albanese fibre of the Hilbert scheme of three points: the generalized Kummer fourfold K=K2(A). Its universal length-three subscheme is an actual integral incidence correspondence and induces an isometry on second cohomology from A into K.

One may cut this moduli space by a surface cycle and compose its incidence correspondence with its transpose. This is not a semihomogeneous bundle construction and is not the fixed-A exterior-product Orlov ring previously excluded. The result below controls **every integral Hodge surface class used for that cut**, rather than only complete intersections or the familiar canonical K3 surfaces.

## 2. Precise theorem

Let A be a complex abelian surface with a primitive polarization ell of type (1,2), with

    NS(A)=Z ell,       End_HS(T(A)_Q)=Q,

where T(A)_Q=ell-perp in H2(A,Q). For the deduction via C.4ab also retain its hypothesis End_HS H1(A,Q)=Q. Put K=K2(A), and let U in CH2(A×K) be the universal length-three subscheme restricted from A×A^[3]. For any integral surface cycle z in CH2(K), form the integral correspondence

    Z_z = (p13)_*(p12^*U · p2^*z · p23^*(transpose U)) in CH2(A×A),

where the ambient product is A×K×A. Its action on H1(A,Q) is zero and its action on T(A)_Q is multiplication by an **even integer**.

The same statement about the two actions holds if z is any integral Hodge class in H4(K,Z); no algebraicity assertion for that arbitrary class is needed. Conversely an actual integral surface Y_p in K realizes transcendental scalar two. Thus the subgroup of transcendental scalars produced by this construction is exactly 2Z. In particular t−s is always even, and this entire incidence construction fails the C.4ab test.

This is a construction exclusion. It makes no claim that every correspondence on A×A factors through this construction, and no claim that P²/2 is nonalgebraic.

## 3. The geometric cohomology input and its normalization

Write R=Z_(2). The normalized incidence map is

    mu = U_* : H2(A,Z) → H2(K,Z).

The standard integral second-cohomology decomposition and Beauville form are

    H2(K,Z)=mu H2(A,Z) perpendicular-sum Z e,
    q(e,e)=−6,

where 2e is the exceptional divisor of the Hilbert–Chow map, up to a harmless simultaneous sign convention for e. The restriction of q to H2(A,Z) is the ordinary intersection form. The map mu is the divisor incidence map: the locus of length-three subschemes meeting a divisor on A. Its Nakajima normalization is explicitly 1/2 times theta^*(q1(a)q1(1)^2|0>), not the unnormalized Nakajima expression. K has H1(K,Q)=0.

Choose the integral hyperbolic basis

    u1,u2,v1,v2,w1,w2

of H2(A,Z), with q(u1,u2)=q(v1,v2)=q(w1,w2)=1 and all other pairings zero. Since ell has type (1,2), a symplectic basis of H1(A,Z) gives

    ell = u1+2u2.

We identify these six classes with their images in H2(K,Z), and put

    Q = u1u2+v1v2+w1w2 in Sym² H2(K,Q).

The Fujiki relation, polarized in four variables, is

    integral_K abcd = 3(q(a,b)q(c,d)+q(a,c)q(b,d)+q(a,d)q(b,c)).     (KI.1)

The integral classes from Kapfer–Menet, Proposition6.30, needed below are

    B_y = (y² − e y/3)/2,  for y in {u1,u2,v1,v2,w1,w2},
    Q/6 = [Y_p].                                                   (KI.2)

Here Y_p is the actual surface of length-three subschemes with fixed support point p and sum zero, for p outside A[3]. The equalities of cohomology classes are all that we use. Multiplication by three makes Q/2 integral. We do not assert that the B_y are algebraic for a general A: most y are not Hodge classes. Their **topological integrality** supplies the required lattice bound on all integral Hodge classes.

### 3.1. Explicit repair of the printed incidence normalization

There is a normalization inconsistency in the displayed derivation of Kapfer and Menet (2018, Proposition6.30, p.545): it writes y=theta^*(q1(a)q1(1)^2|0>) although their Notation5.13 gives the correct expression with the factor 1/2. We do not infer that the conclusion is correct merely from its appearance in the proposition. Here is a derivation with the correct normalization.

Use the Nakajima creation operators q_n, and the multiplication operators G0(gamma) and d from their Section3. Commutators below are graded. Their equations(3.2)–(3.4) give

    [G0(gamma),q1(eta)] = q1(gamma eta),
    [d,q1(eta)] = L1(eta),
    [L1(gamma),q1(eta)] = −q2(gamma eta).

Since G0(gamma) and the even multiplication operator d commute, the graded Jacobi identity applied to

    q2(eta)=−[[d,q1(1)],q1(eta)]

gives

    [G0(gamma),q2(eta)]=2q2(gamma eta).                    (KI.N1)

This verifies precisely the weight-two commutator used below from the printed relations, without appealing to an additional unverified general-weight formula. Proposition5.3 identifies G0(alpha)1 with the summation pullback of alpha for every alpha in H1(A). Its restriction to the zero-sum fibre K therefore vanishes.

Each of the six hyperbolic basis classes a on A is alpha beta for integral degree-one classes alpha,beta; in particular a²=0. For this paragraph only, write rho=theta^* and suppress the vacuum. Apply G0(beta) to q2(alpha)q1(1), then restrict to K. The graded sign and beta alpha=−a give

    0=rho(−2q2(a)q1(1)−q2(alpha)q1(beta)).

Applying G0(alpha) to q2(1)q1(beta) gives

    0=rho(2q2(alpha)q1(beta)+q2(1)q1(a)).

Consequently

    rho(q2(1)q1(a))=4rho(q2(a)q1(1)).                     (KI.N2)

The normalizations in Proposition4.4 and Notation5.13 are

    e=(1/2)rho(q2(1)q1(1)),
    y=(1/2)rho(q1(a)q1(1)^2)=rho(G0(a)1).

Multiplication by G0(a), using (KI.N1)–(KI.N2), now yields

    ey=(1/2)rho(2q2(a)q1(1)+q2(1)q1(a))
      =3rho(q2(a)q1(1)).

Likewise, [G0(a),q1(a)]=q1(a²)=0, so

    y²=rho(q1(a)^2 q1(1)).

Thus the printed subsequent identities are correct with the corrected normalization, and

    B_y=rho(((q1(a)^2−q2(a))/2) q1(1)|0>).               (KI.N3)

For a divisor class a, the operator in parentheses is Qin and Wang's m_(1,1),a, because the symmetric-function identity is m_(1,1)=(p1²−p2)/2. It is integral by their Theorem4.5; their Sections4.1–4.2 construct the integral geometric class for a smooth curve, prove the sign and addition rules, and treat a general divisor as a difference of very ample divisors. The conversion of an integral creation class to an integral operator is Proposition3.5, whose proof and prerequisite Lemmas3.2–3.4 were also freshly read. Kapfer and Menet's Corollary4.3 extends this operator to every integral a on a torus by deformation and monodromy. Applying it to the integral class q1(1)|0> and pulling back proves (KI.N3) integral. This is the exact integrality input needed in (KI.2), including the non-Hodge basis vectors.

The independent source chain for Q/6 is Kapfer and Menet's Corollary6.28, obtained from their preceding explicit Chern-class and surface computations, together with the actual Y_p construction and pairings in Hassett and Tschinkel (2013, Section4). No divisibility assertion from the full integral-basis theorem in Section6.6 is used.

## 4. A complete localization-at-two calculation

Let S=Sym² H2(K,Q) inside H4(K,Q). The pairing on S is nondegenerate by (KI.1). In the 28 ordinary quadratic monomials in the seven displayed basis vectors, its Gram determinant is

    det(Sym² lattice) = 2^14 · 3^38.                              (KI.3)

For completeness, this determinant does not require accepting a numerical program. If a rank-n symmetric form has determinant d and the induced pairing on its symmetric-square monomials is

    c(qij qkl+qik qjl+qil qjk),

diagonalize over an extension of Q. The off-diagonal monomials contribute c^(n(n−1)/2) times d^(n−1). The diagonal block is c D(2I+J)D, and contributes c^n 2^(n−1)(n+2)d². The determinant is therefore

    c^(n(n+1)/2) 2^(n−1)(n+2)d^(n+1).

The identity is invariant under change of basis and hence holds before diagonalizing. With n=7, c=3 and d=det(U³ perpendicular-sum <-6>)=6, it gives (KI.3).

Replace the six monomials y² by B_y from (KI.2), and replace u1u2 by Q/2, retaining the other 21 monomials. These are 28 independent integral cohomology classes. The change-of-basis determinant has absolute value 2^(-7): each square replacement contributes 1/2, and the Q/2 replacement contributes another 1/2. The extra e y/6 terms and the other two terms of Q/2 do not change that triangular determinant. Consequently the new integral lattice L has

    det(L)=3^38,

which is a unit in R. Thus L_R is self-dual for the intersection pairing in S_Q.

Let h be any integral class in H4(K,Z), and let h_S be its rational orthogonal projection to S. It pairs integrally with every element of L, because h does and its orthogonal complement pairs trivially with S. Self-duality therefore gives

    h_S belongs to L_R.                                         (KI.4)

This argument uses neither a computation of the complementary 80-dimensional lattice nor the full 3-primary gluing of H4(K,Z). It also works modulo torsion and hence does not rely on the torsion-freeness statement corrected in the later Kapfer–Menet erratum. The source's full integral-basis theorem is compatible with (KI.4), but its finite F3 orbit computations are not dependencies of this proof.

## 5. Hodge classes and the even scalar

S is a rational sub-Hodge structure, and the intersection pairing makes its orthogonal projection a Hodge morphism. Hence if h has Hodge type (2,2), h_S does too. The assumptions on NS(A) and End_HS(T(A)_Q) imply that all rational Hodge classes in S have the form

    h_S = a ell² + b ell e + c e² + d Q,       a,b,c,d in Q.       (KI.5)

Indeed H2(K,Q)=Q ell + Q e + T(A)_Q orthogonally. There are no Hodge classes in the T cross terms, and the Hodge classes in Sym²T form the one-dimensional line of the inverse intersection form, because End_HS(T_Q)=Q. The class Q differs from that inverse-form line by a multiple of ell². This proves (KI.5) without a claim about algebraic generation.

Expand (KI.5) in the 28-element basis of L. The only nonzero coordinates are

| Basis element | Coordinate |
|---|---:|
| B_u1 | 2a |
| B_u2 | 8a |
| u1 e | a/3+b |
| u2 e | 4a/3+2b |
| v1v2 | −4a |
| w1w2 | −4a |
| e² | c |
| Q/2 | 8a+2d |

By (KI.4), all these coordinates belong to R. In particular

    2a in R,      c in R,      2d in R.                         (KI.6)

The last assertion follows from the Q/2 coordinate and 8a=4(2a). No integral decomposition of all of H4 into Hodge summands has been assumed.

For alpha,beta in T(A)_Q, the four-variable formula (KI.1) gives

    integral_K mu(alpha)mu(beta)ell² = 12 q(alpha,beta),
    integral_K mu(alpha)mu(beta)ell e = 0,
    integral_K mu(alpha)mu(beta)e² = −18 q(alpha,beta),
    integral_K mu(alpha)mu(beta)Q = 12 q(alpha,beta).

For the final identity, the three hyperbolic products contribute 3q(alpha,beta) from their internal contractions, and their two cross-contractions sum to q(alpha,beta); multiply by the Fujiki factor three. The component h−h_S is orthogonal to every product of two degree-two classes and contributes zero. Therefore the scalar induced by the incidence composition is

    s_h = 12a−18c+12d
        = 6(2a)−18c+6(2d) in 2R.                              (KI.7)

The composition is an integral cohomological correspondence, so it preserves H2(A,Z). Its restriction to the nonzero transcendental lattice is scalar, making s_h an integer. Thus s_h belongs to 2R intersect Z = 2Z. Its H1 action factors through H1(K,Q)=0 and is zero. This proves the claimed parity for every integral Hodge class, and in particular every integral algebraic surface cycle.

For h=[Y_p]=Q/6, (KI.7) gives s_h=2. Its transpose-incidence composition is an actual integral Chow correspondence, so two is attained. Taking integral sums and differences gives exactly 2Z. This completes the theorem.

## 6. Failed extensions and what the result does not do

The preliminary divisor-only calculation gives s=3q(h1,h2). Since NS(K)=Z ell+Z e has Gram matrix diag(4,−6), all such values are even. Canonical K3 surfaces also give scalar two. Those preliminary observations alone would leave possible half-integral combinations of divisor and canonical classes untreated. Sections4–5 close that exact gap by using an odd-discriminant lattice in Sym²H2 and its orthogonal projection. They exclude arbitrary integral Hodge cuts, so invoking the rational Hodge conjecture on K does not improve this construction.

A possible expansion to all Albanese fibres of positive-square sheaf moduli was considered but is **not proved here**. One must control the actual universal or quasi-universal class, its integral multiplier, and the embedding of T(A) in the second-cohomology lattice of each fibre. No statement about arbitrary twisted universal kernels follows from the K2(A) calculation. Likewise no conclusion is asserted for different-dimensional Kummer varieties, non-tautological correspondences that do not have the displayed incidence factorization, or arbitrary cycles on A×Ahat.

The desired ordinary integral numerical P²/2 class remains unresolved by this work. The theorem is a genuinely different and stronger method exclusion than the prior fixed-A Orlov or semihomogeneous exclusions, but it is not a strictly smaller main existence gate and is not counted as qualifying movement.

## 7. Exact certificate and failed-run retention

The independent exact-rational script `code/check_kummer_incidence_parity.py` constructs the full 28×28 Gram matrix from (KI.1), verifies both determinant factorizations and the change determinant, verifies integrality of every entry in the enlarged Gram matrix, expands all coordinates in (KI.5), and checks the universal symbolic expression (KI.7) and Y_p's scalar. The successful run started at 19:32:20.908876UTC, with measured internal runtime **0.057556767998903524 seconds**. Its JSON and full stdout are in `output/kummer_incidence_parity.json` and `.out`.

The initial run stopped on a mistaken certificate assertion that the Q/2 coordinate was 2d. Its actual coordinate is 8a+2d, as the complete table above now records. The deduction 2d in R remains valid because 2a in R. The failed initial script and a failure receipt are retained separately; the observed exec wall time was 0.292503707seconds. No failed experiment is relabeled as a successful run. The symbolic program checks the lattice arithmetic, not the geometric integrality input (KI.2).

## 8. Final source-read receipt and precise boundaries

All three initially acquired PDFs, extracted texts, exact URLs, SHA256 hashes, byte lengths, pdftotext exit statuses, and actual acquisition times are retained in `output/kummer_incidence_sources_acquisition.json`. Total acquisition runtime was 22.104002408996166seconds, 19:29:35.339490–19:29:57.443460UTC. Additional acquisition of the published Kapfer–Menet article and its erratum has a separate manifest and timing; it does not replace the initial record.

Freshly read complete displayed proofs in both the retained Kapfer–Menet author v2 and the published 45-page article: Corollary4.3 (published pp.532–533); the H2 normalization in Theorem5.11, formula(5.5), Proposition5.12 and Notation5.13 (pp.537–538); all of Sections6.4–6.5 through Proposition6.30, including the displayed proofs of Propositions6.23–6.25 and6.30 and Corollaries6.27–6.28 (pp.542–545). The published Section3 definitions and commutator relations (pp.530–532), the displayed definition of delta in Proposition4.4 (p.533), and Proposition5.3 with its complete proof were additionally read for Section3.1. The independent determinant/self-duality argument above replaces the full Section6.6 saturation proof; only its initial determinant comparison was inspected. The printed normalization inconsistency in Proposition6.30 is retained explicitly rather than silently corrected.

Freshly read Qin and Wang's arXiv v2, dated1October2004, printed pp.5–11: the entire Sections3.1–3.2 and4.1–4.2, including all proofs of Lemmas3.2–3.4, Proposition3.5, Lemma3.6, Lemmas4.1/4.3/4.4 and Theorem4.5. The introduction and Section2 through the Heisenberg definitions, commutation convention and fundamental classes were also inspected; Proposition3.5's use of the stated Stability Theorem2.1 was checked. The geometric identification with monomial symmetric functions cites Nakajima, and the stability/Chern-class foundations cite earlier Li–Qin–Wang and Lehn work. Their complete original proofs, and the original Beauville/Fujiki and Shioda/Borcea monodromy foundations, were not freshly reopened in this continuation. The report uses these standard cited geometric inputs at the exact scope displayed in the primary sources; it does not claim a complete independent reconstruction of the Hilbert-scheme theory.

Freshly read Hassett–Tschinkel author version dated11June2012, Section3 equation(1), and all of Section4 through Theorem4.4 and its proof, including the explicit Y_p and Z_tau intersection computations. Some subsidiary computations there cite Nakajima/excess-intersection foundations; those external proofs are not claimed as freshly independently audited here. The construction of Y_p and its pairing identity are used only to exhibit the attainable scalar two and to cross-check the normalization of Q/6.

The current published Floccari–Varesco PDF was freshly opened and its introduction through Corollaries1.2–1.3 and the rational coefficient convention in Section2 were read. It is a rational Hodge/Tate theorem. No integral algebraicity theorem or full proof audit of that paper is claimed, and none is an input to the parity result.

The entire five-page author version of the Kapfer–Menet erratum, arXiv:1907.07031v1 (July2019), was read, including Lemmas1–3, Proposition1 and Theorem1 with their displayed proofs. It corrects the torsion-freeness reference and retains the other results. The external transfer theorem cited there was not independently reopened. The later journal corrigendum is identified bibliographically as Algebraic Geometry7(4)(2020),482–485, DOI10.14231/AG-2020-014; that final four-page layout was not separately read. The present proof works modulo torsion and does not use its theorem.

The additional published-article/erratum acquisition took 12.970759333002206seconds (19:32:29.869994–19:32:42.840646UTC), retained in `output/kummer_published_sources_acquisition.json`. Qin–Wang acquisition took 11.928257534003933seconds (19:36:30.527626–19:36:42.455877UTC), retained in `output/qin_wang_source_acquisition.json`; PDF SHA256 aa0d713c0e382cdb7a738421066aa20495bdbc33d5677b93cc44bc7b33a12dd1. These are measured acquisition/extraction times, not claimed proof-reading durations. Source scopes were finalized after the successful local re-reads beginning19:39:32UTC; an output lost during context truncation was reread and is not counted as observed evidence.

### References (APA metadata; exact opened versions above)

Hassett, B., & Tschinkel, Y. (2013). Hodge theory and Lagrangian planes on generalized Kummer fourfolds. *Moscow Mathematical Journal, 13*(1), 33–56. https://www.math.brown.edu/bhassett/papers/hodge/hodge13.pdf

Kapfer, S., & Menet, G. (2018). Integral cohomology of the generalized Kummer fourfold. *Algebraic Geometry, 5*(5), 523–567. https://doi.org/10.14231/AG-2018-014

Kapfer, S., & Menet, G. (2020). Corrigendum: Integral cohomology of the generalized Kummer fourfold. *Algebraic Geometry, 7*(4), 482–485. https://doi.org/10.14231/AG-2020-014

Qin, Z., & Wang, W. (2005). Integral operators and integral cohomology classes of Hilbert schemes. *Mathematische Annalen, 331*(3), 669–692. https://doi.org/10.1007/s00208-004-0602-6

Floccari, S., & Varesco, M. (2025). Algebraic cycles on hyper-Kähler varieties of generalized Kummer type. *Mathematische Annalen, 391*(3), 4443–4453. https://doi.org/10.1007/s00208-024-03027-z (Published online5November2024; scope check only, not a theorem input.)

## 9. Independent mathematical reviews

Before the normalization reconstruction was added, `/root` and `/root/cycles_continuation` separately read the complete original Sections1–8 or1–7, respectively, and reconstructed the determinant formula, index2^7 replacement, self-dual projection over Z_(2), full Hodge coordinate table, scalar parity and the integer-scalar step. Both returned mathematical PASS **conditional on the geometric integrality input (KI.2) and the incidence normalization**. The cycles reviewer also read the complete successful JSON certificate. Neither review is relabeled here as a fresh complete primary-source audit. Section3.1 and the finalized source receipt have been sent to root for the remaining normalization review. The current result remains an auxiliary method exclusion, with no promotion of the C.4 main existence gate.
