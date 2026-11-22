# Part H: the higher Ext vanishing, and corrections to SA19 H4

## H.1 — Proved (derivation from opened classical results)

Let k be an algebraically closed field of characteristic p>0. Let C be a smooth projective connected curve with function field K. For each nonzero effective divisor m on C let J_m be the **connected, degree-zero** generalized Jacobian, considered in Serre's abelian category P of commutative pro-quasi-algebraic k-groups. Write J_infinity=lim_m J_m. Then J_infinity has projective dimension at most one in P. Consequently

    Ext^i_P(J_infinity,G)=0  (i≥2)

for every commutative proalgebraic group G, in particular every algebraic group viewed through its quasi-algebraic perfection. The assertion includes p=2 and p=3. No identification with Ext in a category of all étale sheaves is assumed.

### Proof

For a modulus m=Σ_x n_x[x] with nonempty finite support S_m, set

    R_m=∏_{x∈S_m}(O_{C,x}/m_x^{n_x})^×,
    L_m=R_m/G_m,

where G_m is the diagonal subgroup of constant units. The usual generalized-Jacobian exact sequence is

    0→L_m→J_m→J→0,

where J=Pic^0(C). This is an exact sequence of commutative algebraic k-groups and hence of P. The statement, including its algebraic-group structure, is Serre, *Groupes algébriques et corps de classes*, Chapter I, §1, Theorem 3, p.12 in the opened French extract (proof referred there to Chapter V, §3). A short sheaf explanation is that a point of J_m is a degree-zero line bundle rigidified along m; forgetting the rigidification maps to J, and rigidifications of the trivial bundle form R_m modulo scalar automorphisms.

The transition maps are induced by forgetting some rigidification, and the diagrams of these exact sequences commute. Inverse limits are exact in P (Serre 1960, §2.5, Proposition 10, p.19). Therefore

    0→L→J_infinity→J→0,  L=lim_m L_m.

Choose a k-point x_0 of C. Moduli containing x_0 form a cofinal system. For every such modulus, residue at x_0 gives a retraction R_m→G_m of the diagonal inclusion. Consequently, compatibly in m,

    L ≅ (∏_{x≠x_0} G_m) × ∏_{x∈C(k)} U_x,

where U_x is the proalgebraic principal-unit group 1+m_x O_hat_{C,x}. To verify the limit formula, each finite set of points and every finite jet level occurs in a modulus, and the transition maps are exactly jet truncations and coordinate projections. A local parameter t_x identifies U_x with the multiplicative power-series group 1+t_x k[[t_x]]. This choice affects the displayed isomorphism but not the Ext vanishing.

The additive big-Witt functor is naturally isomorphic to 1+tR[[t]] for any k-algebra R, and over a Z_(p)-algebra it decomposes into a product of p-typical Witt groups. The exact opened references are Hesselholt, *Lecture notes on the big de Rham–Witt complex*, Propositions 1.14 and 1.10, pp.11 and 8. These are functorial isomorphisms of proalgebraic groups and give

    U_x ≅ ∏_{r≥1, p∤r} W,

where W=lim_n W_n is the infinite p-typical Witt group, **not** its universal cover.

Serre 1960 proves pd_P(G_m)=1 (§7.5, pp.50–51; also summarized in §10.1, Theorem 1, p.62), pd_P(W)=1 (§8.6, Corollary 3, p.58), and pd_P(J)≤1 (§9.2, Proposition 4, p.61). For an arbitrary product T=∏_i T_i of copies of G_m or W and a quasi-algebraic target B, we write T as the inverse limit of its finite subproducts. Serre's §3.4, Proposition 7, p.27 applies to this inverse system in P and this target B, and yields

    Ext^2_P(T,B)=colim_{F finite} Ext^2_P(∏_{i∈F}T_i,B)=0.

Here the target hypothesis is essential and has been explicitly checked. Finite products are finite direct sums in the abelian category, so their Ext groups are direct sums of the corresponding zero groups. In particular this vanishing holds for each elementary target B, including every finite group Z/ell. Serre's §3.4, Proposition 9, p.27, with k=1 in his notation, then implies pd_P(T)≤1. Applying this to the displayed product L gives pd_P(L)≤1.

Finally, for any target G in P, the long exact sequence in the first variable of Ext for 0→L→J_infinity→J→0 contains

    Ext^2_P(J,G)→Ext^2_P(J_infinity,G)→Ext^2_P(L,G).

The outside groups vanish. The identical argument in every degree i≥2 proves the asserted vanishing; equivalently J_infinity has projective dimension at most one. This proves the precise higher-Ext question posed in Part H, without appealing to an unverified category comparison. ∎

## H.2 — Proved: the target G_a was never the remaining obstruction

For every P in Serre's category and every connected quasi-algebraic target B,

    Ext^i_P(P,B)=0  (i≥2).

Indeed, for an elementary source, the only possibly nonzero Ext² case is (G_a,Z/p); Serre §8.6, Corollary 5, p.58 gives Ext²(G_a,B)=0 for connected B, while finite sources, tori and abelian varieties have projective dimension ≤1 by the locators just given and §4.4, Corollary 2 to Proposition 5. Every quasi-algebraic source has a finite composition series with elementary quotients (Serre §1.3, Corollary to Proposition 7; §3.2, Definition 1). Long exact sequences prove Ext²=0 for such a source. Proposition 7 of §3.4 passes to arbitrary proalgebraic sources. Degrees ≥3 vanish by §10.1, Theorem 1. In particular Ext²(P,G_a)=0 for **all** P. The reading's reduction of Part H to a difficult G_a target is incorrect.

## H.3 — Refuted: the unaugmented degree-zero comparison

The precise French transcription on 43:80 reads

> « Passant à la limite inductive sur les ouverts denses de X, on trouve ainsi, si K=k(X) »

followed by the box Ext^*(J_{K/k},G)≃H^*(K,G). Earlier on the same page J'_X/k is explicitly an **extension of Z** by the connected group. Thus this is not the connected J_infinity defined in Part H's wording.

For the connected J_infinity and G=Z/ell (ell any prime), every morphism J_infinity→G is zero: it factors through a connected J_m, which has no nonzero finite étale quotient. But H^0(K,Z/ell)=Z/ell. Hence the purported comparison already fails in degree zero for the unaugmented connected pro-Jacobian.

The correction is to retain the augmented degree torsor/group object, in a category that contains Z. The constant infinite discrete group Z is not an object of Serre's P. The higher-Ext vanishing above is valid in P and does not by itself identify the different augmented perfect-site problem. We have not silently equated these categories.

## H.4 — Proved counterexample to transferring the Zariski concentration claim to étale cohomology

Let k be an algebraically closed field of characteristic p>0, A=k[[s,t]], m=(s,t), and E=H^2_m(A). Then

    E=⊕_{i,j≥1} k s^(−i)t^(−j).

Only finite sums occur: the Čech model A_st/(A_s+A_t) gives precisely the finite negative-negative rectangle. Frobenius is F(a s^(−i)t^(−j))=a^p s^(−pi)t^(−pj). The element e=s^(−1)t^(−1) is not in (F−1)E. To prove this, suppose F(h)−h=e. Partition exponent pairs into orbits under simultaneous multiplication by p. On the orbit of (1,1), h has finite support. If its last nonzero coefficient occurs at (p^r,p^r), F(h) has a nonzero coefficient at (p^(r+1),p^(r+1)), which −h cannot cancel. Thus h has no nonzero coefficient on this orbit; it therefore cannot produce e. This contradiction works for every p, including 2 and 3.

In fact the ordinary cohomology functor does not even descend, with its usual functorial action, to Serre's category P: Frobenius on G_a is an isomorphism in P but its action on E is not surjective (e is not in its image). A proalgebraic object Q representing this ordinary functor in P therefore cannot exist. Even if one only asks for a projective Q with the displayed value and the usual action of F−1, projectivity would make Hom_P(Q,−) exact on the Artin–Schreier exact sequence

    0→Z/p→G_a --(F−1)→ G_a→0,

forcing F−1 to be surjective on E, contrary to the calculation. This is a failure of the proposed category transfer, not a disproof of a separately formulated Zariski representability theorem.

For completeness, simply replacing E by its Frobenius direct limit does not remove this Artin–Schreier obstruction. In colim_F E each orbit is indexed by all integers rather than only the nonnegative integers, but every element still has finite support. On each orbit F−1 has a nonzero cokernel isomorphic to (k,+), by the same telescoping quotient below. Thus this particular attempted repair cannot establish projectivity either. This observation is conditional on using that direct-limit interpretation; no perfect-site comparison is asserted.

There is also an explicit corrected statement for étale cohomology with supports. Quasi-coherent étale cohomology agrees with ordinary coherent cohomology, so H^i_m(A,G_a)=0 for i≠2 and equals E for i=2. Artin–Schreier gives

    H^2_m(A,Z/p)=ker(F−1:E→E)=0,
    H^3_m(A,Z/p)=coker(F−1:E→E)≠0,

and all other degrees are zero. The same finite-support argument proves the kernel is zero. More explicitly, choose one vector v=(i,j) with i,j>0 and not both divisible by p from each orbit. Then

    H^3_m(A,Z/p) ≅ ⊕_{v primitive} (k,+)

as F_p-vector spaces. On the v-orbit the quotient map sends a finite sum Σ_r a_r e_(p^r v) to Σ_r a_r^(p^(−r)); perfection of k makes this defined. It annihilates F−1, is surjective, and its kernel consists exactly of the telescoping relations F(ae_r)−ae_r. This computes the entire obstruction, not just one nonzero element.

The exact opened inputs for this étale calculation are Stacks, Theorem 59.22.4 (tag 03P2, quasi-coherent comparison), Section 59.63 (tag 0A3J, the Artin–Schreier exact sequence), and Lemma 51.2.1 (tag 0A6T, the Čech model and localization triangle): https://stacks.math.columbia.edu/tag/03P2 ; https://stacks.math.columbia.edu/tag/0A3J ; https://stacks.math.columbia.edu/tag/0A6T . The same orbit calculation proves the analogous degree-(d+1) nonvanishing in k[[t_1,...,t_d]] for every d≥1.

The readings explicitly label 43:70–74 as **Zariski** theory. For that topology Artin–Schreier is not an exact sequence of sheaves. Thus the Zariski concentration statement cannot be transported to the Serre category or to étale cohomology, and it does not prove the stated projectivity. The complete ring example also obstructs the corresponding essentially-finite-type version: the completion map from k[s,t]_(s,t) carries any hypothetical preimage to the impossible preimage just considered. The original Zariski representability claim is not refuted by this étale computation.

## Literature search and novelty discipline

Searched Serre's proalgebraic homological dimension, generalized-Jacobian unit kernels, and big-Witt decomposition, then opened the sources above. The argument H.1 is a derivation from those known results; no novelty is claimed. The proof does not use the unverified all-degree geometric class field comparison as an input.

## H.5 — Proved: the perfect étale site gives the same higher vanishing here

The comparison is a theorem, not a formal consequence of the full embedding. Let S be the site of perfect k-algebras with the étale topology, and view the quasi-algebraic groups as their associated sheaves of abelian groups on S. Suzuki, *Duality for local fields and sheaves on the category of fields*, Kyoto J. Math. 62 (2022), 789–864; opened author version arXiv:1310.4941v6 (27 January 2021), Proposition 3.8.1, p.47, gives

    Ext^n_Ab(S)(P,B) = Ext^n_PAlg/k(P,B)

for affine pro-quasi-algebraic P and quasi-algebraic affine B. Remark 3.8.4, pp.55–56, explicitly extends this statement to sources that are extensions of a perfected abelian variety by an affine proalgebraic group, and to arbitrary quasi-algebraic targets. Its auxiliary category P'Alg' has projective resolutions in Serre's full category staying inside P'Alg'. Enlarging the site to quasi-compact quasi-separated perfect schemes gives the same topos. Source: https://arxiv.org/pdf/1310.4941 .

The source J_infinity belongs to precisely that category by the exact sequence 0→L→J_infinity→J→0 proved in H.1. Consequently for every quasi-algebraic G and every n≥0,

    Ext^n_Ab(S)(J_infinity,G) = Ext^n_P(J_infinity,G).

H.1 therefore proves the requested vanishing for n≥2 also on the perfect étale site. This use of the comparison has its source and target hypotheses checked. It does not assert agreement for arbitrary pro-objects or arbitrary sheaf targets.

There is a material warning in the proof: PAlg/k→Ab(S) is only left exact (Suzuki p.53). Its derived comparison is built through the exact realization on the perfect pro-fppf site and the limit theorem of Lemma 3.8.2, pp.48–53. Merely asserting an exact fully faithful embedding into perfect étale sheaves would be wrong. The limit theorem treats inverse limits in the source and algebraic targets; it does not license an unqualified interchange in the second variable.

The augmentation problem in H.3 remains separate. For any actual exact sequence 0→J_infinity→J_aug→Z→0 in Ab(S), the same higher vanishing follows: Ext^n(Z,G)=H^n(S,G)=0 for n>0, since every étale cover of the terminal object Spec(k) splits when k is algebraically closed. Apply the long exact sequence in the first variable. This proves a conditional statement about the correctly augmented sheaf, not the unqualified geometric comparison with ordinary H^*(K,G). In particular a perfection of coefficients and of the geometric argument must be specified before comparing ordinary rational points in degree zero.

## H.4b — Refuted: projectivity of the ordinary two-dimensional local Jacobian

This counterexample can be stated in an actual representability category, independently of any imperfect transfer to Serre's category. Let A_0=k[s,t]_(s,t), x its closed point, with k algebraically closed of any characteristic p>0. In the abelian category Pro(AbSch_k) of pro-objects in commutative finite-type group schemes, let J_x be the local Jacobian prorepresenting

    Hom(J_x,G) = H^2_{x,fppf}(Spec(A_0),G).

Existence and this universal property are Toën, *Generalized local jacobians and commutative group stacks*, arXiv:2308.01670v3 (21 February 2026), Definition 3.5 and preceding construction, pp.17–18. Its application here is to a codimension-two point of the smooth surface A^2_k; no locally constant infinite component occurs. The local comparison proved inside Proposition 3.7, pp.20–22, gives Ext^i_naive(J_x,G)=H^{2+i}_{x,fppf}(A_0,G) for unipotent G. The relevant source is https://arxiv.org/pdf/2308.01670 .

For a direct nonsplitting proof, use the map f:J_x→G_a corresponding to e=s^(-1)t^(-1) in E_0=H^2_x(A_0,G_a). Form the pullback in Pro(AbSch_k)

    Q = J_x ×_{G_a,f,F−1} G_a.

Projection gives the exact sequence 0→Z/p→Q→J_x→0. A splitting would be equivalent to a homomorphism g:J_x→G_a with (F−1)g=f, hence to an element h∈E_0 with (F−1)h=e. The completion map to k[[s,t]] is functorial for Frobenius and sends this equation to the impossible equation proved in H.4. Thus the extension is nonsplit, and J_x is not projective. This gives the full counterexample, including the exact extension and its nonsplitting, for every p, including 2 and 3.

In fact E_0 identifies with the previously computed E: local cohomology commutes with flat completion, and E_0 is m-torsion, so tensoring it with the completion leaves it unchanged. Toën's Lemma 3.9, pp.21–22, gives Ext^1_naive(J_x,G_a)=0. The Artin–Schreier long exact sequence therefore computes

    Ext^1_naive(J_x,Z/p) = E_0/(F−1)E_0
                        = ⊕_{i,j>0, p∤gcd(i,j)} (k,+).

Thus the claim 'pro-unipotent and projective' in SA19-H4 is false in this ordinary group-scheme category. Being pro-unipotent does not imply projectivity. The earlier warning that the ordinary functor does not descend to Serre's perfection category is still valid and prevents conflating these two counterarguments.

## Exact scope of the modern geometric comparison

Toën's Theorem 0.3 (= Proposition 3.7), pp.3 and20, compares the full complex of local Jacobians J_*(X), not simply its connected degree-zero term, with fppf cohomology on a smooth scheme X. Its restrictions are affine G for cohomological degree i>0 and unipotent G for i>1. Section 3.2, p.19, explicitly distinguishes Yoneda Ext in pro-group schemes from Ext in all fppf sheaves: the realization is not fully faithful in higher degrees. Remark 3.10(2), p.22, attributes the absence of these restrictions in Grothendieck's formulation to his use of Zariski cohomology. These are precise comparison theorems, not a general identification of every Ext category.

Cais–Otabe, *Class field theory for function fields and finite abelian torsors*, arXiv:2507.02483v4 (16 October 2026), Theorem 1.3, p.3 (=Theorem 2.1), proves the fppf torsor/isogeny classification for every finite commutative k-group scheme, including nonreduced groups. Formula (1.8), p.2, is H^1_fppf(U,G)=colim_m Ext^1(J_m,G). The authors state on p.3 that Deligne's 1974 letter asserted this for all commutative G but that its two-variable effaceability sketch lacks details; their theorem proves the finite-group case. Source: https://arxiv.org/pdf/2507.02483 . This is stronger than étale class field theory but is not an all-degree, all-target comparison to be silently substituted into Part H.

## H.3b — Refuted: ordinary degree zero cannot agree naturally with perfect coefficients, even after augmentation

For any source P on the perfect étale site, a family of isomorphisms Hom(P,G^perf)=H^0(k(t),G) natural in ordinary commutative algebraic groups G is impossible. Indeed F:x↦x^p is an isomorphism of G_a^perf, so induces a bijection on Hom(P,G_a^perf). Its action on ordinary H^0(k(t),G_a)=k(t) is not surjective: a solution h^p=t would imply p v_0(h)=1 at the discrete valuation t=0. Naturality would identify a bijection with this non-surjective endomorphism. This contradiction applies to any augmented P as well as the connected pro-Jacobian. Augmentation repairs the missing degree map but does not repair this distinct coefficient/perfection mismatch. Higher Ext vanishing in the specified categories remains proved.
