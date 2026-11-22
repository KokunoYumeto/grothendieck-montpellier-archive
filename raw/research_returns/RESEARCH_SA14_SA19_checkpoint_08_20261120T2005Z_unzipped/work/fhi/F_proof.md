# Part F: checked literature, corrected scope, and precise nonabelian obstruction

## F.1 — Known: the actual published theorems

The exact conjecture reproduced in Suzuki, *Finite generation of nilpotent quotients of fundamental groups of punctured spectra*, Journal of Algebra 633 (2023), 489–509, Conjecture 1.1, p.1, is SGA 2 XIII, Conjecture 3.1. It assumes a complete noetherian local ring with algebraically closed residue field, **all irreducible components of dimension at least two**, and connected punctured spectrum. Theorem 1.2, p.2, proves finite generation of the **maximal pro-nilpotent quotient**, in both equal and mixed characteristic. It includes the maximal pro-p and abelian quotients. Its introduction, pp.2–3, explicitly distinguishes this result from finite generation of the full group. Opened source: https://arxiv.org/pdf/2207.01563 (v4, 4 July 2023); publisher DOI https://doi.org/10.1016/j.jalgebra.2023.07.005 .

The original Grothendieck–Murre theorem was opened directly, rather than inferred from a later citation. In *The tame fundamental group of a formal neighbourhood of a divisor with normal crossings on a scheme*, LNM 208 (1971), §9.1 and Theorem 9.2, p.122, A is complete noetherian local of dimension two with algebraically closed residue field, E is closed, and S=Spec(A)\E is connected. The maximal prime-to-p quotient of π₁(S) is topologically finitely presented. The definition immediately below, pp.122–123, uses a free pro-prime-to-p group. The residue characteristic p=0 is allowed, in which case this is the whole group. Opened original preview containing the theorem and definition: https://page-one.springer.com/pdf/preview/10.1007/BFb0069617 ; chapter https://doi.org/10.1007/BFb0069617 . Thus characteristic zero is covered without assuming that an arbitrary complete local ring already comes with a complex-analytic link.

Carvajal-Rojas–Schwede–Tucker, *Fundamental groups of F-regular singularities via F-signature*, Ann. Sci. ENS 51 (2018), 993–1016, Theorem A=Theorem 5.1, printed p.994, proves that for a normal F-finite strongly F-regular strictly henselian local domain of characteristic p>0 and dimension at least two, π₁ of the punctured spectrum is finite, of order prime to p and at most 1/s(A). Opened original: https://www.numdam.org/item/10.24033/asens.2370.pdf . In the equal-characteristic setting of Part F, completeness and algebraically closed residue field imply strict henselianity. F-finiteness also follows: a Cohen presentation exhibits A as a quotient of k[[x₁,…,x_e]], whose Frobenius is finite because k is perfect. The extra hypothesis still needed to apply this theorem is strong F-regularity; it is not a theorem about all normal surface singularities.

**F.1b — Known: log terminal surfaces in every characteristic.** Carvajal-Rojas–Yasuda, *On the behavior of stringy motives under Galois quasi-étale covers*, Documenta Mathematica 30 (2025), no.3, 709–751, DOI 10.4171/DM/1012, Theorem B p.4 of the opened arXiv:2105.05214v4 (27 March 2025), equivalently Corollary 6.4 pp.29–30, proves that the full punctured étale fundamental group of a **two-dimensional complete log terminal local ring with algebraically closed residue field is finite**, in all equal and mixed characteristics. This includes residue characteristics 2 and 3. The theorem is not restricted to strongly F-regular rings and does not claim the finite order is prime to the residue characteristic. Section 6 setup p.28 specifies normality, Q-Gorenstein (torsion canonical class), and positive log discrepancies on a minimal resolution. Those extra singularity hypotheses are not consequences of the normality assumed in Part F. Opened original author PDF: https://arxiv.org/pdf/2105.05214 ; published metadata https://arxiv.org/abs/2105.05214 .

Searches through 20 November 2026 for a resolution for arbitrary normal complete surfaces located no such primary theorem. That negative search is not a proof that no theorem exists. The full positive-residue-characteristic surface case outside the log terminal and strongly F-regular cases remains undecided in this work.

## F.2 — Refuted: the dimension-free wording of the alleged consequence

The transcription 58:19 says that the finite-generation question is reduced to normal rings of dimension two, and then conjectures the result for complete local rings with algebraically closed residue field. The prompt's unqualified wording “every complete local ring” omits the dimension restriction of the published conjecture. Taken literally, that wording is false.

Let k be algebraically closed of characteristic p>0, A=k[[t]], and U=Spec(k((t))). Artin–Schreier theory gives

    H¹_et(U,Z/p)=k((t))/(F−1)k((t)).

The classes of t^(−n), over all positive integers n not divisible by p, are linearly independent over F_p. For a nonzero finite linear combination, let n be its largest pole order; this n is not divisible by p. If g has a pole of order m>0, then g^p−g has pole order pm, divisible by p. If g has no pole, neither does g^p−g. Therefore the combination cannot equal g^p−g. A profinite group generated by d elements has at most p^d continuous homomorphisms to Z/p, while the displayed H¹ has infinite dimension. Thus π₁(U) is not topologically finitely generated. This counterexample does not refute the dimension-two question in Part F; it corrects the omitted qualification in its stated consequence.

## F.3 — Proved: even a prosolvable inference from the known finiteness statements is invalid

There is a metabelian profinite group G such that:

1. its maximal pro-nilpotent quotient is the topologically cyclic group Z₃;
2. every open subgroup H has topologically finitely generated abelianization, hence H¹_cont(H,F_ℓ) is finite for every prime ℓ;
3. G is not topologically finitely generated.

**Construction.** For n≥1 let f_n be the multiplicative order of 2 modulo 3^n. The finite field L_n=F_(2^f_n) contains an element ζ_n of order 3^n. Put V_n=(L_n)^n with its additive group, V=∏_{n≥1}V_n, and Γ=Z₃. Let γ∈Γ act on V_n by the scalar ζ_n^(γ mod 3^n). This is a continuous action on V. Set G=V⋊Γ. The group is metabelian because V and Γ are abelian, and its finite quotients are solvable.

**Its nilpotent quotients.** The map v↦(ζ_n−1)v is invertible on each V_n. Consequently the single commutator operator with 1∈Γ maps V onto V, so [Γ,V]=V. In any finite nilpotent quotient Q, the image of V is a 2-group and the image of Γ is a 3-group. The Sylow subgroups of a finite nilpotent group commute, so the image of [Γ,V] is trivial. Thus every finite nilpotent quotient kills V and factors through Γ. Conversely every finite quotient of Γ is nilpotent. The maximal pro-nilpotent quotient is therefore Γ itself.

**Abelianizations of open subgroups.** Let H be open in G. The product topology implies that H contains ∏_{n>M}V_n and the subgroup 3^NΓ for some integers M,N. Put L=max(M,N) and T=∏_{n>L}V_n. On T the commutator operator with 3^N∈Γ is multiplication, in its n-th coordinate, by ζ_n^(3^N)−1. Each scalar is nonzero for n>L; the coordinatewise inverse is continuous in the product topology. Therefore every element of T is a commutator of two elements of H, and T⊆[H,H]. The quotient H/T is a closed subgroup of (∏_{n≤L}V_n)⋊Γ. Its kernel under projection to Γ is finite, and its image is a closed subgroup of the procyclic group Γ. Thus H/T is topologically finitely generated: choose finitely many generators of the finite kernel and a lift of a topological generator of the image. Its quotient H^ab is also topologically finitely generated. The asserted finite H¹ follows.

**Failure of finite generation.** Suppose d elements of G generate a dense subgroup. Project them to V_n⋊(Γ/3^nΓ). Let W_n⊂V_n be the L_n-linear span of their d vector coordinates. Every word in these generators lies in W_n⋊(Γ/3^nΓ), because the action is by scalars. If n>d, W_n is a proper subspace of V_n. Their projection cannot generate that finite quotient, a contradiction. Hence G is not topologically finitely generated. ∎

This is an abstract profinite counterexample to a proposed inference, not a realization as a surface local fundamental group. It strengthens the ∏A₅ example in the supplied reading by showing that passing from nilpotent to solvable groups does not remove the gap. A geometric argument must exclude unbounded multiplicities of nontrivial finite coefficient modules, or supply another condition that fails in this explicit group.

## F.4 — Approaches tried and exact gates

**Rank-one Artin–Schreier and Frobenius methods.** These explain finite H¹ with constant p-torsion coefficients and the maximal pro-p quotient. Theorem F.3 shows exactly why repeating this for each open subgroup is insufficient: its open subgroups satisfy the same qualitative condition. A quantitative uniform bound, or control of coefficients with nontrivial action, would be a new input. No such bound has been proved here for all normal complete surface singularities.

**Prosolvable dévissage.** Trying to build the full group from successive abelian kernels fails at the multiplicities of the nontrivial modules V_n in F.3. The failure is already metabelian. An argument that merely enumerates finite solvable quotients without a uniform generator bound cannot conclude finite generation.

**Resolution and exceptional curves.** Suzuki's negative-definite intersection argument controls Frobenius-fixed deformation cohomology and constant-coefficient wild characters. Extending it to arbitrary finite local systems would need a uniform estimate compatible with their ramification and with finite covers of the exceptional divisor. This is a precise unproved step, not an established reduction to a finite collection of curve groups.

**Global wild covers of curves or cones.** A family of wild covers on an affine curve does not automatically yield covers of the punctured complete local surface: regular Artin–Schreier functions on a henselian complete local ring are killed by Hensel's lemma when the residue field is algebraically closed. We have no constructed non-finitely-generated π₁ satisfying Part F's dimension-two assumptions.

**Smallest undecided scope recorded here.** A complete normal two-dimensional local domain in positive residue characteristic, outside the log terminal and strongly F-regular cases, with its full (possibly non-solvable) wild fundamental group. All claims about full finite generation in that scope remain undecided; the partial theorems and counterexamples above do not close it.

**Stringy motives and nonabelian wild covers.** Theorem 6.3 and Corollary 6.4 of Carvajal-Rojas–Yasuda, pp.29–30, use strict decrease of stringy motives under ramified quasi-étale Galois covers and a descending chain condition. This controls nonabelian wild covers in the log terminal class. The positive discrepancies and convergence are part of the construction. Extending this invariant and its descending chain condition to arbitrary non-log-terminal normal surfaces is a separate unproved gate, not a formal generalization of their theorem.

## F.3b — Proved: the missing uniform bound is detected by explicit twisted coefficients

For the group G in F.3, let M_n=L_n, with V acting trivially and Γ acting through the scalar ζ_n. Then

    H¹_cont(G,M_n) ≅ L_n^n,

so its F₂-dimension divided by dim_F₂(M_n) is n. For a profinite group generated by d elements, by contrast, every finite F_ℓ-module M satisfies dim H¹(G,M)≤d dim M: a crossed homomorphism is determined by its values on the generators, first on their words by the cocycle identity and then on their closure by continuity.

To compute the displayed H¹, every cocycle on Γ is a coboundary because ζ_n−1 is invertible. Subtract the coboundary with the same value at the topological generator 1∈Z₃; its restriction vanishes on all integers, hence on Γ. A cocycle on G normalized in this way is exactly a continuous Γ-equivariant additive homomorphism V→L_n. Such a map factors through finitely many factors of V. No factor L_m with m≠n contributes: if m<n, γ^(3^m)−1 is zero on L_m and invertible on L_n; if m>n, γ^(3^n)−1 is invertible on L_m and zero on L_n. On L_n^n, equivariance is L_n-linearity since F₂[ζ_n]=L_n. Thus the normalized cocycles form Hom_Ln(L_n^n,L_n)=L_n^n. A coboundary that vanishes on Γ arises from an element fixed by ζ_n, necessarily zero, so none of these normalized nonzero cocycles is a coboundary. This proves the full formula.

Therefore a proof of finite generation for the geometric group must supply information beyond finite constant-coefficient H¹ for each open subgroup. The explicit obstruction violates a necessary uniform bound for nontrivial finite coefficient modules. No sufficiency criterion for such a bound is assumed here.


## F4: quantitative prosolvable criterion

Full proof is in F_prosolvable_criterion.tex and appended to F.tex. If every finite simple coefficient module has normalized continuous H1 at most C, then a prosolvable profinite group is generated by at most ceil(C)+1 elements. The sharper bound uses the nonzero End_H(M) summand in H1(M semidirect H,M), reducing the number of bad generating lifts strictly below the number of all lifts. The required uniform geometric estimate is not proved.


## F5: uniform bound for abelian prime-to-p coefficient monodromy

F_tame_abelian_bound.tex, now merged into F.tex, proves a uniform linear rank bound on H1(U,M) for finite F_p local systems with abelian prime-to-p monodromy in equal characteristic p. A finite subgroup of abelian tame inertia is killed by the resolution intersection determinant; one fixed cover kills it. The resulting torsion line bundles on a fixed resolution admit a uniform Suzuki high-pole cutoff and a rank-linear low-pole bound. Root independently audited the entire proof against Suzuki §§2–3; BCE independently passed the geometric inertia/purity reduction. This excludes F3 as a geometric quotient in characteristic2 but does not settle nonabelian or wild coefficient monodromy, and does not close Part F.


## F6: nonabelian wild kernels over abelian tame quotients

The complete proof in F_pro_p_by_abelian.tex, merged into F.tex, combines F4/F5 with normal pro-p invariants and inflation-restriction. Root independently audited it. Every such quotient has a uniform generator bound; virtually abelian tame quotients also give finite generation. Full F remains open.


## F7/F7a/F7b

Full proofs in F_unramified_coefficients.tex and F.tex. Arbitrary extended finite coefficient systems have rank-uniform H1; relative pro-p kernels need no solvable quotient. Root independently passed mathematics and exact sources. Full F remains undecided.
