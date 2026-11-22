# Target 2: the cyclic sixfold source, its exact scope, and effective bounds

Run: HODGE_DIVISION, /root/sixfolds. Author/checker: GPT-6 Astra Pro; inherited effort not exposed. Date: 2026-11-21. This note distinguishes published inputs from new consequences and records unresolved questions rather than claiming all sixfold families are solved.

## Results available for incorporation

1. **The proposed universal dominance is false for the natural cyclic construction.** A six-dimensional nontrivial rational isotypic factor of a cyclic étale cover of a genus-four curve, with quadratic coefficient field, has character order 3, 4, or 6. Thus its field is Q(sqrt(-3)) or Q(i). Its rational Hermitian space is split: determinant class [-1] in Q*/N(K*). No nonsplit determinant family is reached by this source. This restriction does not use h_K=1.
2. The cubic and quartic constructions have image dimension exactly **9** and period differential rank **9** generically. These are published results: Schoen 1998, Lemma 13, pp. 334–335, and Koike 2004, Theorem 2.1, pp. 568–572. Exact finite data have been recomputed; see SF-CW and SF-KO below.
3. For the **principal Gaussian Prym sixfold component**, a safe new detector bound is
   
   D_G,6 = 121,993,819,950,101,299,200.
   
   The proof uses the **nine-dimensional full norm fibre** in J(C_13), then projects to the six-dimensional primitive Prym. Using the six-dimensional primitive Prym as the original supplier support would require an additional argument and is not used.
4. The supplied GHOSTS R20 bound for the Eisenstein sixfold source is consistent with the exact degree calculation:
   
   D_E,6 = 57,854,793,024,000.
   
   This is cited as a supplied result, not claimed new.
5. Either bound transfers to every fixed polarized lattice in the same rational split Hermitian class with the explicit cost m^6, where m clears a chosen rational K-linear polarization isometry. It does not transfer to a different determinant class.

## SF-01 — Character-field restriction (proved)

Let p:C→X be a connected étale cyclic cover, with g(X)=4 and group G=C_d. For a divisor e>1 of d, let B_e be the abelian subvariety corresponding to the rational irreducible cyclotomic character of exact order e. Then

    dim B_e = 3 φ(e).

Consequently, if dim B_e=6, then e∈{3,4,6}, and the coefficient field is Q(ζ_e)∈{Q(sqrt(-3)),Q(i)}. Equivalently, passing to the order-e quotient cover reduces the question to one of these three orders. Any purported construction of a general Weil sixfold for another imaginary quadratic field from one such rational isotypic factor fails at the coefficient-field step.

**Proof.** For an étale cyclic cover, p_*ω_C is the direct sum of ω_X⊗L^j, with L of exact order d. For each nontrivial character, Riemann–Roch gives

    h^0(X,ω_X⊗L^j)=g(X)-1=3,

because h^0(X,L^(-j))=0. There are φ(e) characters of exact order e; their holomorphic eigenspaces give dim B_e=3φ(e). The elementary equation φ(e)=2 has exactly the solutions 3,4,6. Its rational character field is Q(ζ_e). ∎

This is a restriction on the natural rational isotypic construction. It does not claim that a specially chosen factor with accidental extra endomorphisms cannot carry additional quadratic actions. Such special points do not provide dominance in a general Weil family: a generic member of the latter has endomorphism algebra K.

## SF-02 — The rational Hermitian space is split (proved, using the standard surface mapping-class theorem)

For a connected cyclic étale cover of a genus-(n+1) curve, the order-e primitive homology, for e>2, is a hyperbolic Hermitian space of rank 2n over Q(ζ_e), relative to complex conjugation. In the quadratic cases e=3,4,6 its determinant class is [(-1)^n]. In particular, all the sixfold sources of SF-01 have determinant class [-1].

**Proof.** A connected cover is specified topologically by a surjective homomorphism χ:H_1(X,Z)→Z/d. A primitive integral lift of χ exists: if the residues have gcd together with d equal to one, one can change one coordinate by a multiple of d so that its gcd with the remaining coordinates is one, by the Chinese remainder theorem. An integral primitive vector in a unimodular symplectic lattice extends to a symplectic basis. The surjectivity of the surface mapping-class representation onto Sp(2g,Z) (Farb–Margalit, *A Primer on Mapping Class Groups*, Theorem 6.4) therefore lets us place all the monodromy on the first handle.

Write X topologically as a one-holed torus glued to a genus-n surface with one boundary circle. The cover of the latter consists of d disjoint copies; the connected cover of the torus has genus one and d boundary circles. Gluing gives C. Inside the d copies choose the usual handle curves a_{j,k},b_{j,k}, where 1≤j≤n and k∈Z/d. Their intersection numbers are

    <a_{j,k},a_{l,r}>=<b_{j,k},b_{l,r}>=0,
    <a_{j,k},b_{l,r}>=δ_jl δ_kr.

The deck generator shifts k. These classes account for a nondegenerate rank-2nd direct summand of H_1(C,Q); its complement is the invariant rank-two homology of the torus. Thus the nontrivial rational isotypic part is obtained entirely from

    Q[G]^n ⊕ Q[G]^n,

whose two displayed summands are G-stable totally isotropic and paired perfectly. Applying the order-e central idempotent yields two Q(ζ_e)-subspaces of dimension n, totally isotropic for the Hermitian form associated with the symplectic pairing. (A G-stable symplectically isotropic subspace is Hermitian-isotropic because all of its field multiples remain in it.) The Hermitian pairing is nondegenerate, so it is hyperbolic. In bases for the two isotropic subspaces its matrix has block form [[0,A],[A*,0]], with determinant (-1)^n N(det A). This proves the determinant assertion. ∎

**Scope consequence.** The natural genus-four cyclic source has a nine-dimensional image in the split Q(i) and Q(sqrt(-3)) Weil moduli. It has **no image** in the other determinant components as a moduli map preserving the prescribed K-action and polarization form. It is not appropriate to call the empty image “rank zero.” All components for K=Q(sqrt(-2)), Q(sqrt(-7)), Q(sqrt(-11)), Q(sqrt(-19)), Q(sqrt(-43)), Q(sqrt(-67)), Q(sqrt(-163)) are absent from this construction; so are all nonsplit components for Q(i) and Q(sqrt(-3)). The list of nine class-number-one fields is the standard Heegner–Baker–Stark classification; an author-hosted exact list is William Stein, *Algebraic Number Theory*, subsection “Class Number 1,” https://wstein.org/books/ant/ant/node46.html, lines containing the nine fundamental discriminants. The field classification is used only to spell out the seven names; SF-01 applies without it.

Explicit absent examples are Hermitian diagonal forms diag(1,1,1,-1,-1,-3) for Q(i), of determinant -3, and diag(1,1,1,-1,-1,-2) for Q(sqrt(-3)), of determinant -2. The positive factors 3 and 2 are not norms respectively, because they are inert primes and valuations of norms there are even. Their signatures are (3,3), so these are actual nonsplit Weil moduli types. This is a counterexample to universal cyclic-source dominance, not to the Hodge conjecture.

## SF-CW — Exact rank certificate for the cubic source (published theorem rechecked)

Published input: Schoen, *Addendum to: Hodge classes on self-products of a variety with an automorphism*, Compositio Math. 114 (1998), **Lemma 13**, equations **(13.1), (13.2)**, pp. **334–335**. The codifferential is multiplication

    H^0(C,ω_C)_χ ⊗ H^0(C,ω_C)_χ^-1 → H^0(C,ω_C²)^(C_3).

Schoen's explicit cover has group (Z/3)^3 over P¹, with inertia e_1,e_2,e_3,-e_1-e_2-e_3; the étale subgroup is generated by e_1+e_2. Characters are triples modulo 3. The two three-dimensional eigenspaces split into the following one-dimensional characters:

    χ=1: (0,1,1), (1,0,1), (2,2,1);
    χ=2: (1,1,0), (1,1,1), (1,1,2).

Their nine pairwise sums are

    (1,2,1) (1,2,2) (1,2,0)
    (2,1,1) (2,1,2) (2,1,0)
    (0,0,1) (0,0,2) (0,0,0).

All are distinct. Multiplication of two nonzero holomorphic differentials on a smooth integral curve is nonzero. Thus the nine products are linearly independent, and the rank is **9**. Both source and target have dimension nine. The Chevalley–Weil multiplicities and all nine products are verified by `sixfold_certificates.py`; this computation supplements the cited published proof and is not claimed as a new dominance theorem.

## SF-KO — Exact rank certificate for the quartic source (published theorem rechecked)

Published input: Koike, *Algebraicity of some Weil Hodge Classes*, Canadian Math. Bull. **47(4) (2004), 566–572**, **Theorem 2.1** and **Proposition 3.1**; codifferential **(1)** on p.568, defining eigenvectors **(2)** on p.568, relations **(6),(7)** on p.571, coefficient substitution **(8)** and monomial basis **(9)**, pp.571–572. Corollary 2.1 states the resulting algebraicity. Koike's printed discriminant notation δ=1 should not be silently identified with the unsigned determinant modulo norms; SF-02 establishes the convention used in this run, determinant [-1].

The source is a general invariant complete-intersection curve in (P¹)^4. The codifferential is

    H^0(X,ω_X⊗L) ⊗ H^0(X,ω_X⊗L³) → H^0(X,ω_X²),

with dimensions 3·3→9. In Koike's normalized product coordinates, three target coordinates give an identity block. The remaining six give a polynomial matrix M in nine parameters A_i,B_i,C_i. At formal A=B=C=0 it is

    M0 = [[1,0,0,0,0,0],
          [0,1,0,0,-2,0],
          [0,0,1,0,0,0],
          [0,0,0,1,0,0],
          [0,0,0,0,-1,0],
          [0,0,0,0,0,-1]],

with determinant 1. This is a witness that the determinant polynomial is nonzero; the zero parameter point is **not asserted smooth**. The nonempty rank-open set meets the nonempty smooth/free-action open set of Proposition 3.1 in the irreducible coefficient parameter space. The differential rank there is exactly **9**.

As a second finite check, at

    A=(1,2,3), B=(2,3,5), C=(3,5,7)

the six-product matrix has determinant **-389639**, while the first six rows of the seven quadratic b-product relations have determinant **227264**. All sixteen displayed polynomial identities (6),(7) have been expanded and verified over Q(i). The selected coefficient point is again a polynomial rank witness, not a certified smooth curve. No analytic numerical rank is used.

## SF-03 — A corrected effective Gaussian sixfold detector bound (proved)

Let C→X be a connected étale cyclic-four cover of a genus-four curve, σ its deck generator, Y=C/<σ²>, and

    B = Prym(C/Y),       Θ|_B = 2Ξ,

where Ξ is the integral principal Prym polarization. Put

    P = ker(Nm(C/X))^0.

Then dim C's Jacobian is 13, dim P=9, and dim B=6. The polarization type on P is (1,1,1,1,1,1,4,4,4), so χ(Θ|_P)=64. There is an effective integral threefold Z_B⊂B with nonzero Weil projection and

    deg_Ξ Z_B ≤ 121,993,819,950,101,299,200.

The same bound holds on every fibre of the connected principal Gaussian Prym component dominated by this family.

**Proof.** Cite the étale r=0 construction of Schoen 1988, Theorem 2.0, pp.12–13 and Lemma 2.6, and its primitive Künneth identification in §3, pp.24–25. For h=6, its supplier cycles on C^6 are supported over the canonical linear system |K_X|⊂Sym^6 X. At least one irreducible effective supplier has nonzero pairing with the pulled-back Weil plane. Here is the precise support and nonvanishing argument needed for the degree bound.

Write a:C^6→J(C) for the sum Abel map and q=1−σ²:J(C)→B. The map (q∘a)^* identifies the two Weil lines with the two alternating top exterior powers of the primitive ±i eigenspaces in H^1(C)^{⊗6}, up to nonzero constants. This is the primitive summand U in Schoen's theorem. Its pairing is nondegenerate: the cup-product pairing on H^1(C) pairs the ±i eigenspaces perfectly, and the pairing on their top exterior powers is its nonzero determinant. Since Schoen's supplier classes span U, one supplier pairs nontrivially with (q∘a)^*W. Decomposing that supplier into irreducible components shows that one effective integral component has nonzero pairing. Its Abel image Z has dimension three, as does q(Z); otherwise the corresponding pushforward class would vanish. The reduced image q(Z) remains a detector because the pushforward is a nonzero positive integral multiple of its class.

The class of the norm of a supplier divisor is K_X. Thus Z lies in W_6(C)∩T0, where T0 is one connected component of the appropriate norm fibre, hence a translate of **P**, not of B. Conversely, any point of W_6(C)∩T0 has an effective divisor representative whose norm lies in |K_X|. The map Sym^6 C→Sym^6 X is finite; its inverse image of |K_X| has dimension at most three. Consequently W_6(C)∩T0 has dimension at most three, and Z is a three-dimensional irreducible component. This justifies applying the component Bézout inequality to Z.

The asserted type of Θ|_P is the standard étale cyclic Prym type, as stated in Lange–Ortega, *Prym varieties of cyclic coverings*, §4, paragraph defining the type D (arXiv0805.1020 p.6), citing Birkenhake–Lange, Corollary12.1.4 and Lemma12.3.1. Equivalently, p^*J(X) has induced type (1,4,4,4), because the degree-four isogeny p^*:J(X)→p^*J(X) pulls its polarization back to 4Θ_X and has cyclic kernel. Complementarity in the principally polarized J(C) gives the stated nine-dimensional type. The double étale Prym B has induced type (2^6), hence Θ|_B=2Ξ with Ξ integral principal.

Embed J(C) by 3Θ. Poincaré's formula and the polarization degree give

    deg_(3Θ) W6 = 3^6 ·13!/7! = 900,694,080,
    deg_(3Θ) T0 = 3^9 ·9!·64 = 457,124,290,560.

The component Bézout inequality (Fulton, *Intersection Theory*, Example8.4.6, as used in GHOSTS R12) gives

    deg_Θ Z ≤ [900,694,080 ·457,124,290,560]/3^3.

For the projection, σ preserves Θ and has Rosati adjoint σ^-1. Hence

    q†q = (1−σ²)^2 = 2(1−σ²) ≤ 4·Id,

where the difference is positive semidefinite on the analytic tangent space. Therefore q^*(Θ|_B)≤4Θ in the nef order, and q^*Ξ≤2Θ. Applying the projection formula to the effective threefold Z gives

    deg_Ξ q_*Z ≤ 2^3 deg_Θ Z.

Removing the positive generic-degree multiplicity can only reduce degree and preserves nonvanishing of the Weil projection. The product is exactly

    (8/27) ·900,694,080 ·457,124,290,560
      = 121,993,819,950,101,299,200.

Every operation before choosing a component is an effective finite inverse image, proper pushforward or effective component selection; no rational cycle is counted as integral. Koike's rank-nine dominance supplies a Zariski-dense set of fibres of the nine-dimensional Weil component. Closedness of the bounded detector locus, supplied Theorem D/Lemma Dom, extends this same integer bound to every fibre. ∎

**Correction to the naive analogue of GHOSTS R12.** In the quartic case, the supplier norm fibre has dimension 3n; its polarization Euler characteristic is 4^n. The primitive Prym has dimension 2n and Euler characteristic 2^(2n)=4^n, the same number. This coincidence does **not** justify replacing the norm fibre's factorial (3n)! and power 3^(3n) by those of the smaller primitive Prym. The safe proof above preserves the correct dimension.

## SF-04 — Transfer to an arbitrary fixed split polarization (proved)

Fix a connected Weil sixfold family (A_s,L_s,ι) whose rational Hermitian space is isometric to the source rational polarized Hermitian space in SF-03, or to the Eisenstein source in GHOSTS R20. Let F:V_source→V_target be one rational K-linear isometry of the alternating polarization forms. Choose symplectic/integral lattice bases, and let m≥1 clear every denominator of the matrix of F, so mFΛ_source⊂Λ_target. Then the detector bound on the target family is

    δ_W(A_s,L_s) ≤ m^6 D_source

for all s; D_source is D_G,6 or D_E,6 respectively.

**Proof.** The K-linear isometry identifies the period domains and sends each admissible source complex structure to a target one. After passing to the finite-index lattice stabilizer subgroup, hence to a finite cover of the relevant level moduli, mF induces a family of K-equivariant isogenies f:B→A. By definition of F,

    f^*L = m² L_source

in the Néron–Severi group. A source detector Y of dimension three satisfies

    deg_L(f_*Y) = ∫_Y f^*c1(L)^3 = m^6 deg_(L_source)Y.

The correspondence f_* is a nonzero isomorphism on the rational Weil plane, and it respects the decomposition defined by K. Thus f(Y), with reduced integral structure, is a detector and has degree no larger than f_*Y. Dominance and the closedness input then give the same bound on the target component. Existence of F for signature (3,3) and determinant [-1] follows from rational Hermitian classification, cited exactly as Schoen1998 §7, p.332; the construction of the family isogeny is §6, p.332. One may enumerate rational K-matrices and test F*H_target F=H_source until an isometry is found; classification ensures termination. All quantities used in the bound are then exact integers. ∎

This does not claim that the isogeny degree itself controls c_t on a varying Hecke orbit. F and m are fixed once for a fixed polarized family. Varying the target lattice would vary m and would return to the obstruction of Theorem E.

## From the degree bound to division

Use supplied Theorem W, with n=3, the chosen integral endomorphism a, denominator δ of t, and T=-∫t²>0. Substituting D_G,6 or m^6D_source yields an explicit integral division bound after taking ceilings. A simple deliberately loose integer form, with s=ceil(sqrt(T)), is

    c_t ≤ δ Nm(a)^6 (|R|^4 + 4s κ |R|^3) D^4,

where R and κ are the exact integers defined in Theorem W. This keeps every numerator integral. The root agent has a stronger proposed quadratic extraction and may replace this bound after its independent check. The existence and degree statements SF-01–SF-04 do not depend on that improvement.

## Translation into the programme

- **Condition A:** SF-03 and SF-04 give effective integral detector families dominating the split Gaussian/Eisenstein sixfold moduli, hence bounded c_t by the supplied detector reduction. Their location in the project's archive language is cote16 scan050, corrected SIGN_NEXT SN-C03/C04. They settle the relevant split-family instance of the open sixfold row in HODGE_DIVISION_ATTACK §4 item2.
- **Condition I:** positivity is used only to extract/divide the two-dimensional Weil plane after the supplier exists (cote16 scan049 and cote44 Theorem4). It supplies no detector in an absent determinant component.
- **Correspondences and motives:** the primitive projector q and the rational K-isotypic projector are algebraic endomorphism correspondences. The new degree statement concerns an effective cycle in the primitive summand of h(C) and h(B); its rational Betti realization has nonzero component in Λ_K^6 H¹(B). Clearing a fixed resultant denominator is the Cayley–Hamilton inverse mechanism of cote16 scans048–049.
- **Schemes and ℓ-adic realizations:** the maps and finite-type cycle parameter spaces spread over a finitely generated integral Z-algebra after inverting the cover degree and polarization/level denominators. The dense-family argument is a statement about proper cycle parameter spaces, not about pointwise finite-field algebraicity. The Hodge classes correspond to weight-six classes in H⁶ with Tate twist(3); no L-value nonvanishing estimate is used to supply these cycles.
- **K-theory and λ-rings:** the classes of the effective detecting subvarieties define coherent K₀ classes; their Chern characters recover the codimension-three cycle classes in the topological filtration. This is an interpretation after cycle construction, not a semiregularity assertion.
- **Missing components and ghosts:** SF-01/SF-02 close the proposed cyclic approach for the other fields/determinants. They leave bounded division there undecided. A hypothetical counterexample is a ghost only under the supplied 032-dependent background GHOSTS B03, with that dependence retained.

No new exact EGA/SGA/FGA locator is asserted in this note: the parent paper should reuse its already checked cycle-space, spread and base-change locators rather than invent a formal citation for these interpretations.

## Remaining gates and attempted approaches

- The demand “every h_K=1 field and every determinant by the genus-four cyclic source” is refuted by SF-01/SF-02. The broader bound on the missing sixfold families remains open here.
- Searched modern literature: located unrefereed 2026 claims for Q(i) determinant[-3] and Q(sqrt(-3)) determinant[-2] involving reflection groups. They are **not used** as theorems and are not substitutes for the missing source.
- A direct nodal rational-curve multiplication calculation is available from the imprimitive agent and may give an alternate exact rank certificate for the order-six variant. It is unnecessary for the published cubic/quartic dominance theorems. Schoen1988 p.26 explicitly treats order6 as equivalent to order3 at the level of the cyclotomic construction.
- General fixed rational determinant cannot be changed by rescaling the polarization on a rank-six K-space: scaling by c multiplies determinant by c^6=N(c^3). Adding a compensating Weil surface changes dimension to eight; it cannot turn this sixfold dominance result into an all-determinant sixfold result. This blocks the naive re-use of Schoen's fourfold compensation Proposition10.

## SF-05 — The two principal Gaussian lattice components and a uniform factor eight (proved)

Assume the maximal Gaussian order Z[i] acts integrally and the principal polarization is compatible with conjugation. A rank-2n Hermitian lattice of signature (n,n) underlying such a principally polarized Weil variety is isometric to precisely one of

    U^n,   U=[[0,1],[1,0]],       or       I_(n,n)=diag(1^n,-1^n).

The first is even (all vector norms are even integers), the second odd. The cyclic-four étale double-Prym construction has lattice U^n. There is a fixed K-equivariant isogeny from the U^n family to the I_(n,n) family satisfying f^*θ_odd=2θ_even. Consequently the Gaussian sixfold detector bound valid for either maximal-order principal component is

    D_G,6,all-principal = 8 D_G,6
      = 975,950,559,600,810,393,600.

**Proof of the classification.** In an O_K-basis the principal alternating polarization corresponds to an integral unimodular Hermitian matrix H. Indeed, for K=Q(i), H(x,y)=E(x,iy)+iE(x,y), and det_Z E=(det_K H)^2. Its determinant is (-1)^n by signature. Rational Hermitian classification (Schoen1998 §7) says that the rational space is split. Choose a rational isotropic vector, clear denominators, and divide by its O_K-content to obtain a primitive isotropic vector e in the lattice. Since H is unimodular, H(e,L)=O_K, so choose f with H(e,f)=1. Their Gram matrix is [[0,1],[1,k]] with k∈Z, and its determinant is -1, so it splits off integrally. Replacing f by f-ce changes k by 2Re(c). If k is even this block is U; if k is odd it becomes [[0,1],[1,1]], which in the basis f,e-f is diag(1,-1). The orthogonal complement is again balanced unimodular and rationally split. Induction gives a sum of U and I_(1,1) blocks.

An even lattice has no odd block. If an odd block occurs, every remaining U block can be converted to odd blocks using the integral identity <1>⊕U≅<1,1,-1>: for a,e,f with Gram diag(1,U), the vectors a+e,a-f,a+e-f have Gram diag(1,1,-1) and form a unimodular basis. Keeping the negative line of the existing I_(1,1) block yields I_(2,2). Repeating proves the classification. Parity distinguishes the two cases.

**Proof of the source lattice assertion.** Use the topological model in SF-02. On each unaffected base handle the integral primitive sublattice has basis

    a_0-a_2, a_1-a_3, b_0-b_2, b_1-b_3.

The restriction of the Jacobian symplectic form is twice the standard symplectic form. Its half is the principal Prym form Ξ. For the K-basis a=a_0-a_2, b=b_0-b_2, σ acts as i and the Hermitian matrix is [[0,i],[-i,0]]. A unit basis change makes it U. The invariant torus contributes no primitive homology. Thus the lattice is U^n.

**Proof of the fixed isogeny and bound.** For one hyperbolic pair put

    M=[[1,1],[1,-1]],       M* diag(1,-1) M=2U.

This is integral over Z[i] and invertible over K. Direct sums give a K-linear rational similitude identifying the two period domains and inducing, after a finite level cover, an isogeny f with f^*θ_odd=2θ_even. Its degree is 2^(2n). A dimension-n effective cycle's degree grows by 2^n, by the projection formula; passing to its reduced image can only reduce that degree. Nonzero Weil projection is preserved under the K-equivariant isogeny. For n=3 this gives the factor eight and the displayed exact integer. ∎

For a merely rational K-action, or a nonmaximal integral order, a principal polarization alone does not justify applying this two-lattice statement. The fixed-family isometry cost of SF-04 must then be retained.

## SF-04a — Explicit Gaussian split-polarization bound (proved)

For a split Gaussian Weil sixfold with integral maximal order and polarization Euler characteristic Δ=∫θ6/6!, the matrix-dependent cost in SF-04 can be bounded uniformly:

    δ_W ≤ (2Δ)^6 D_G,6.

For an integral order of conductor f, the safe bound is(2f^12Δ)^6D_G,6. Proof: choose a saturated maximal isotropic Gaussian submodule and extend its basis. The Hermitian matrix becomesH=[[0,B],[B*,C]], withb=detB andNorm(b)=Δ. PutC'=(B*)^-1CB^-1=(adjB)*C(adjB)/Δ andT=[[I,−C'/2],[0,B^-1]]. ThenT*HT=U³ andT^-1=[[I,(B*)^-1C/2],[0,B]]. Both matrices have denominator dividing2Δ. Hence(2Δ)T induces the required isogeny with polarization pullback(2Δ)²Ξ. For the nonmaximal order enlargeΛ toΛ'=O_iΛ⊂(1/f)Λ, indexk≤f12; useθ'=f²θ, whoseEuler characteristic isf12Δ/k. The map[f]:A'→A pullsθback toθ', so pushforward costs no further degree. The principal parity estimateSF-05 is sharper when applicable.

## SF-06 and SF-07 — Small sixfold projectors and quadratic division constants (proved)

Full proofs are in sixfold_section.tex; exact computations ran in sixfold_division_certificates.py.

Gaussian: P=(1−[i]*)(150−[2+i]*−[2−i]*)=768eW onH6, each signed part≤400D, d=−∫y²≤16384D². WithA=[2+i]*, theGramshape is[[1,−117],[-117,15625]], determinant1936, dual norms5500sqrt(d) and44sqrt(d). Thus

    c_t ≤ δ D² max(31719424,563200000 ceil(sqrt(T))).

Eisenstein: P=(1+[ω]*+[ω²]*)(27−[2+ω]*)=162eW, each signed part≤81D, d≤729D². WithA=[3+ω]*, theGramshape is[[1,−143],[-143,117649]], determinant97200, dual norms61740sqrt(3d) and180sqrt(3d). Thus

    c_t ≤ δ D² max(70858800,270050760 ceil(sqrt(3T))).

In both statementsδt isintegral andT=−∫t²>0; the statedO_Kendomorphisms must actintegrally. These supersede the olderquartic substitution paragraph above. TheEisenstein sourceD_E,6 usesΘ|Ptype(1³,3³), not a principalpolarization. No unnoticed principalquotient is used.
