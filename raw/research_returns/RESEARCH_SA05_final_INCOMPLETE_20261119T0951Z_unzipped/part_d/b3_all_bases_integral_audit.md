# Independent audit: proper descent, arbitrary bases, and the integral torsor lattice

**Audit date:** 19 November 2026, after checkpoint 04. **Auditor:** Part D agent, independent of Part B's proof draft and root's separate proof check. This note records a theorem conditional on divisor Tate for surfaces; it does not assert that conjecture. It also isolates a remaining Brauer obstruction rather than silently replacing full cohomology by its torsion subgroup.

## 1. The new universal surface gate

I read the complete proof in `pending_b3_all_bases_surface_gate.md`. For fixed primes p ≠ ℓ, the following universal assertions are equivalent:

1. Divisor Tate holds for every smooth projective surface over every finite extension of F_p.
2. H¹_et(S,A)[ℓ∞] is finite for every finite-type F_p-scheme S and every abelian scheme A/S, with no reducedness, smoothness, or separatedness hypothesis on S.
3. The same finiteness assertion holds for the Jacobians of smooth curve families with a section over nonempty opens of P¹ over finite extensions of F_p.

The already audited surface-pencil argument proves (3) ⇒ (1), and (2) ⇒ (3) is immediate. The genuinely new step is descent of the invariant Kummer comparison from smooth separated bases to arbitrary bases. That step passes the following independent checks.

For a smooth separated base T, the surface-Tate hypothesis implies divisor Tate for the smooth total space B=A∨ by the exact Kahn/Morrow reduction already checked separately. Multiplication [m] on B has eigenvalues 1,m,m² on the total-degree-two Leray terms. Its eigenvalue-m summand is H¹(T̄,V_ℓA), and the same summand of divisor classes is exactly the Kummer image of A(T̄)⊗Q_ℓ. The zero section removes the relative Picard obstruction; the Poincaré bundle supplies the actual normalized divisor. Thus the invariant Kummer map is surjective on smooth T.

For a proper smooth alteration cover q:T→S, proper Čech descent identifies the kernel of H¹(S̄,V_ℓA)→H¹(T̄,V_ℓA) with E₂^{1,0}. It is a subquotient of H⁰((T×_S T)̄,V_ℓA). These section spaces have weight −1: after a finite constant-field extension, evaluation on a closed point of each geometric connected component injects them into the Tate module of an abelian variety over a finite field. The kernel therefore has no arithmetic Frobenius invariants. Kummer injectivity on the possibly singular double intersection forces the pulled-back section to satisfy the Čech equalizer condition. Proper rational section descent, proved below, gives a section on S; subtracting its Kummer class leaves an invariant vector in the weight −1 kernel and hence zero.

This uses only the H⁰ weight statement on the singular Čech terms, not a general weight theorem for their H¹. Finite-coefficient proper cohomological descent passes to continuous coefficients using the finiteness/Mittag–Leffler condition, and the total-degree-one argument has only finitely many terms in each relevant degree. Nilpotent thickenings change the section groups by p-primary groups and do not change the prime-to-p étale local system. A finite affine open cover and its ordinary Čech sequence then handle nonseparated bases. No proper separated cover of an arbitrary nonseparated base is presumed.

## 2. Exact proper descent after inverting p

Let q:T→S be proper surjective between noetherian F_p-schemes and let A/S be an abelian scheme. For an actual section b∈A(T) whose two pullbacks to T×_S T agree, let Z be its schematic image in A. The map T→A is proper because A/S is separated. Thus Z→S is proper, and every geometric fibre has exactly one underlying geometric point: any two geometric points of T_s form a point of the double fibre product and have the same b-image. Consequently Z→S is finite, surjective, and radicial, hence a finite universal homeomorphism.

Kelly's Proposition 3, or Corollary 20 in the possibly nonreduced case, gives r and h:S→Z such that, for g:Z→S,

    h g = F_Z^r,      g h = F_S^r.

The second formulation applies because the kernel of O_S→g_*O_Z is a bounded nilpotent ideal on a noetherian quasi-compact base. If j:Z→A is the image map, (jh,id_S) defines a section c of A^(p^r)=A×_{S,F_S^r}S. Its pullback to T is F^r_{A/S}b. Applying the iterated Verschiebung V^r gives a∈A(S) with

    q*a = [p^r]b.

Thus the equalizer is exact after inverting p when its difference is already zero after inverting p. The rational equalizer follows as well: first clear the rational denominator, then kill the finite-order actual Čech difference. Tensor the resulting Q-vector-space equalizer with Q_ℓ. There is no illegitimate attempt to clear arbitrary Q_ℓ coefficients by an integer.

For reduced S, injection follows from schematic density and separatedness. For general S, a finite nilpotent filtration has additive Lie-sheaf kernels, killed by p at each stage, so injection is restored after inverting p. The same filtration controls cokernels of the section map to S_red.

**Opened exact source:** Shane Kelly, *Universal homeomorphisms of and not of finite presentation*, 4 July 2018, Proposition 3 p. 2, Lemma 18 pp. 8–9, Corollaries 19–20 p. 9. I read the full Frobenius-factorization proof. URL: <https://www.ms.u-tokyo.ac.jp/~kelly/pdfs/uh%20non-fp.pdf>. Root, B, and D performed separate checks; this note records D's check only.

## 3. The stronger integral theorem

**Proposition.** Assume the surface-Tate assertion in §1. Then for every finite-type F_p-scheme S, every abelian scheme A/S, and every ℓ≠p, the localized group

    H¹_et(S,A) ⊗ Z_(ℓ)

is a finitely generated Z_(ℓ)-module.

Here Z_(ℓ) means integers localized away from ℓ. This assertion is stronger than finiteness of the ℓ-primary torsion: it also controls the torsion-free part at ℓ. It is useful on singular bases, where H¹(S,A) need not be torsion.

### 3.1 The proper-cover kernel embeds into a Čech lattice after inverting p

First suppose S is reduced and separated. Choose a proper surjection q:T→S with T smooth, a finite disjoint union of regular schemes, and write T_a=T×_S⋯×_S T with a+1 factors. Set

    K = ker[H¹(S,A) → H¹(T,A)].

An element of K is an A-torsor P that has a section b over T. The torsor may be a proper algebraic space; representability by a scheme is not assumed. The difference of the two pulled-back sections is an element z∈A(T_1), satisfying the ordinary Čech 1-cocycle identity. Changing b changes z by a coboundary. Contracted product adds the cocycles. This defines a homomorphism

    K → H¹(A(T_•)).

Its kernel is p-primary. Indeed, a zero Čech class allows b to be translated so that its two pullbacks agree exactly. Take the schematic image Z of T→P. The same fibre argument as in §2 makes Z→S proper and quasi-finite, hence finite. A finite algebraic space over a scheme is a scheme, so Kelly's theorem applies to Z→S without any unproved scheme-representability assertion for P itself.

The Frobenius factorization gives a section of P^(p^r). Relative Frobenius identifies this torsor with the pushout of P along F^r_{A/S}:A→A^(p^r). Pushing its section along V^r gives a section of the pushout of P by [p^r]. Therefore [p^r][P]=0 in H¹(S,A).

Since integer localization is exact, the resulting map is injective:

    K[1/p] ↪ H¹(A(T_•))[1/p]
             = H¹(A(T_•)[1/p]).

This uses an actual homomorphism of cocycle groups and ordinary exact localization. It does not presume comparison of étale and h-site H¹, or claim that a proper cover is itself an étale cover.

### 3.2 The Čech terms have finite rank over Z[1/p]

For every finite-type F_p-scheme U, A(U)[1/p] is a finitely generated Z[1/p]-module. If U is reduced, restriction to its finitely many generic points injects A(U) into a finite product of groups A(k(η)). Each is finitely generated by Lang–Néron, since its constant-field trace has only finitely many rational points over the finite constant field. For nonreduced U, a finite nilpotent filtration changes sections by groups killed by a power of p, so localization gives the reduced answer.

The Čech H¹ group is a subquotient of A(T_1)[1/p], and Z[1/p] is noetherian. It is therefore finitely generated. Its submodule K[1/p] is also finitely generated. Further localization gives finite generation of K⊗Z_(ℓ).

### 3.3 The regular-cover quotient is finite at ℓ

For regular integral noetherian W with function field K and abelian scheme G/W,

    H¹(W,G) → H¹(K,G_K)

is injective, and the target is torsion. The exact opened source is Stacks Project, Remark 110.74.2 and Lemma 110.74.3, tag 0AF8, <https://stacks.math.columbia.edu/tag/0AF8>. The dimension restriction in Lemma 110.74.1 is explicitly removed in Remark 110.74.2; I am not importing the surface-only lemma into arbitrary dimension.

For completeness, the remark's Picard argument extends a rational torsor section étale-locally. After trivializing the torsor, G is Pic⁰ of its dual G∨. A generic line bundle extends across regular G∨ by taking Cartier closure. Rigidify it along the zero section. Its associated homomorphism φ_L:G∨→G is zero on the generic fibre, hence zero everywhere by separatedness and generic density. Fibrewise φ_L=0 characterizes algebraically trivial line bundles, so the extended section lands in Pic⁰. Uniqueness glues the local extensions. The field torsion assertion follows by taking a point over a finite separable extension and applying the norm/symmetric-sum construction to its torsor class; the cited lemma explicitly allows group algebraic spaces.

Apply this to each regular component of T. The group H¹(T,A) is torsion. Its ℓ-primary subgroup is finite by §1 under surface Tate. Hence H¹(T,A)⊗Z_(ℓ) is finite. Localizing

    0 → K → H¹(S,A) → H¹(T,A)

now proves the proposition for reduced separated S.

### 3.4 Remaining bases

A nilpotent thickening induces a finite sequence of additive Lie-sheaf kernels on the relevant deformation complexes. Their cohomology is p-primary, so H¹(S,A)⊗Z_(ℓ) is unchanged. For nonseparated S, choose a finite affine open cover. The kernel of restriction in H¹ is the ordinary Čech H¹ of the section sheaf, by genuine open-cover torsor descent. Its localized terms are finitely generated by §3.2; the localized target is a finite direct sum of finitely generated modules by the separated case. This proves the full assertion.

## 4. Consequence for the relative Picard sheaf of a curve

Let f:X→S be a smooth proper family of geometrically connected curves and J its relative Jacobian. Étale-locally on S the degree map gives

    0 → J → Pic_{X/S} → Z → 0.

The kernel of H¹(S,J)→H¹(S,Pic_{X/S}) is the image of H⁰(S,Z), a finitely generated group because S has finitely many connected components. The group H¹(S,Z) is torsion-free: for each n, H⁰(S,Z)→H⁰(S,Z/n) is surjective, so its n-torsion vanishes by the long exact sequence. Thus the ℓ-primary torsion of H¹(S,Pic_{X/S}) is contained in the ℓ-primary torsion of a quotient of H¹(S,J) by a finitely generated subgroup. The proposition makes the corresponding Z_(ℓ)-localization finitely generated, whose torsion is finite. Therefore

    H¹(S,Pic_{X/S})[ℓ∞] is finite

under surface Tate, even when the degree obstruction has infinite order. This resolves the degree-obstruction step in the Leray argument. It does not resolve the different base-image issue below.

## 5. The remaining genus-one Brauer/base-image obstruction

Write Br′(Y)=H²_et(Y,G_m)_tors. The kernel in the Leray sequence is the image of the **full** H²(S,G_m), not automatically the image of Br′(S). Put

    D = im[Pic_{X/S}(S) → H²(S,G_m)].

A torsion class on X lying in that kernel may lift to a non-torsion a∈H²(S,G_m) with ℓ^n a∈D. The finite-generation argument for Pic_{X/S}(S)[1/p] does not itself bound this phenomenon: a finitely generated subgroup can have an infinitely ℓ-divisible saturation in a larger torsion-free group. The elementary example Z⊂Z[1/ℓ] already shows why finite generation of D alone is insufficient.

For genus 0 or genus at least 2, the relative canonical or anticanonical line bundle has nonzero degree, supplying a bounded-degree trace/obstruction mechanism. The unresolved genuinely new case is a genus-one torsor over a singular base whose period can be infinite. One needs either a bound on the ℓ-saturation of the degree-zero Picard obstruction in H²(S,G_m)/torsion or a different torsion-lifting argument. This note does not assert either.

It is false that full H²(S,G_m) is always torsion on finite-type finite-field schemes. The original Colliot-Thélène–Skorobogatov author draft dated 31 October 2019, §7.1 pp. 156–157, gives reducible examples from Picard gluing and spreads them to affine finite-field varieties. Its later published numbering differs. Esser's *Non-torsion Brauer groups in positive characteristic*, arXiv:2102.01799v3, Theorem 2.4 p. 4, proves torsion for normal surfaces over F̄_p, while the introduction records higher-dimensional counterexamples. These sources rule out a shortcut; they do not supply a counterexample to the remaining relative genus-one assertion.

## Source access and scope record

- Kelly 2018: full primary PDF and exact factorization proof opened; Proposition 3, Lemma 18, Corollaries 19–20.
- Stacks tag 0AF8: full primary page opened; Remark 110.74.2 and Lemma 110.74.3 read. This is the used regular-base source.
- Raynaud, *Faisceaux amples sur les schémas en groupes et les espaces homogènes*, chapter XIII, publisher metadata opened, but the chapter's full text was **not obtained**. No assertion that XIII.2.6 was read is made.
- Colliot-Thélène–Skorobogatov 2019 author draft: §7.1, Lemma 7.1.2 and the following explicit constructions, pp. 156–157, opened for the non-torsion scope warning.
- Esser 2022 arXiv version: introduction and Theorems 2.3–2.4 opened for the precise normal-surface limitation.

All prior independent audit events are preserved. The universal abelian-scheme surface gate was already counted in checkpoint 04's formal review. The integral lattice proposition and Picard-degree consequence are separately recorded advances; the final genus-one base-image obstruction remains open.


## Subsequent resolution at 06:20 UTC

The nonproper base-image or genus-one saturation gate isolated above is now resolved, conditional on the same surface-divisor Tate conjecture. The full proof is `b3_all_bases_brauer_units.tex`, independently audited in full by root and Part B. On every finite-type finite-field scheme S, full H²_et(S,G_m) tensor Z_(ell), modulo its actual divisible unit-cup subgroup, is finitely generated. The proof combines the finite-generation cover kernel already established here with a smooth quasi-projective unit-cup finite-cokernel theorem, an unconditional finite-kernel residue argument on arbitrary double intersections, and rational descent of unit lattices. It therefore controls non-torsion base classes becoming torsion in Leray quotients without any replacement of full H² by Br. For morphisms with equal global units, the relative ell-Brauer cokernel is directly finite. The universal curve-family assertion is consequently equivalent to surface Tate over all finite constant fields. The earlier warning remains a valid description of the limitation of the earlier proof alone; the added unit-cup argument supplies its missing step.
