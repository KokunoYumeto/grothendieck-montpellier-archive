# Post-CP05 proof: unit cups uniformly at all primes different from p

Written during the CP05 freeze, outside frozen deliverables. This strengthens the fixed-prime result; it does not prove the surface Tate conjecture.

## Exact assertion

Fix a finite field k of characteristic p. Let D=(Q/Z)[p'] be the subgroup of elements of order prime to p. Assume divisor Tate for every smooth projective surface over finite extensions of k at a fixed prime ell0 different from p. For every smooth quasi-projective k-scheme T, the arithmetic cyclic-cup map

\[
c_T:\Gamma(T,\mathcal O_T^\times)\otimes D\longrightarrow\operatorname{Br}'(T)[p']
\]

has finite cokernel. Here Br' denotes the torsion part of H²_et(Gm), and the arithmetic character has the prescribed value on arithmetic Frobenius. This is a single finite group across all primes different from p.

The proof below reduces the assertion to Qin's Theorem 5.2, whose exact primary source is https://arxiv.org/pdf/2012.01681, version 2 dated December 2021, author pp.14–15. That theorem says that for a smooth geometrically connected variety U over a finite field, finiteness of Br(Ubar)^Gamma[ell0 infinity] at one ell0 implies finiteness of Br(Ubar)^Gamma[p']. Its proof uses Lemmas 3.2–3.4, Proposition 4.2–4.3, Theorem 4.4 and Lemma 5.1 in the same paper. The owner has opened those exact passages; Part D independently read the full internal chain and passed it. The cited external dependencies have now been checked in their current primary versions: Qin's 2024 published fibration paper, Proposition2.1 and Lemmas2.2–2.3, pp5–8, and Ertl–Keller–Qin, Comparison of different Tate conjectures, arXiv2012.01337v4 (August2025), Proposition2.6 and Theorem2.7 with their full proofs, pp14–16. These replace the stale locators Qin1Prop2.3 and Qin2Lemma3.4/Theorem3.5 used in the 2021 bibliography. The owner read the full current proofs. The divisor splitting and the weight-zero unit calculation agree with the separately proved Part B lemmas; the zeta pole formula makes the geometric finiteness condition independent of ell. The older v1 endpoints were attempted but not obtained.

## 1. One compactification

First let U be a geometrically connected dense open in a smooth projective geometrically connected Y/k. Let Gamma=Gal(kbar/k), and let B be the free abelian group on the finitely many geometric codimension-one components of Ybar minus Ubar. Boundary subsets of codimension at least two do not affect units or Picard groups on the regular Ybar. The standard divisor sequence is Gamma-equivariant:

\[
0\longrightarrow\bar k^\times\longrightarrow
\Gamma(\bar U,\mathcal O^\times)\longrightarrow B
\longrightarrow\operatorname{Pic}(\bar Y)
\longrightarrow\operatorname{Pic}(\bar U)\longrightarrow0.
\]

All groups are regarded as discrete continuous Gamma-modules; every element is defined over a finite constant extension. The image N of the unit divisor map is a finite free lattice with finite Frobenius action. Write E for the geometric unit group, so 0→kbar*→E→N→0.

### Arithmetic units generate the degree-two constants term

Since kbar* is torsion and Gamma has cohomological dimension one on discrete torsion modules, H²(Gamma,kbar*)=H³(Gamma,kbar*)=0. Thus

\[
H^2(\Gamma,E)\cong H^2(\Gamma,N).
\]

Also H¹(Gamma,kbar*)=0: Frobenius minus identity is the surjective power map x↦x^(q−1). Hence the arithmetic global-unit group maps onto N^Gamma.

Higher continuous cohomology of the rational module N⊗Q vanishes, by averaging on finite quotient groups. The exact sequence 0→N→N⊗Q→N⊗Q/Z→0 therefore gives

\[
H^2(\Gamma,N)\cong H^1(\Gamma,N\otimes Q/Z)
\cong (N\otimes Q/Z)_\Gamma
\cong N_\Gamma\otimes Q/Z.
\]

The middle equality is continuous cohomology of a procyclic group on a discrete torsion module. The map N^Gamma→N_Gamma has finite cokernel, since Frobenius acts through a finite group and averaging identifies invariants and coinvariants over Q. Tensoring with the divisible group Q/Z makes the map surjective. Its restriction to D remains surjective onto the prime-to-p subgroup.

The induced map from an invariant unit and the character class is precisely the degree-two Hochschild–Serre term of the cyclic algebra. This follows by comparing the Bockstein of 0→Z→Q→Q/Z→0 with the Kummer boundary for the unit, or by the usual cyclic cup construction. Consequently the image of H²(Gamma,E)[p'] in H²(U,Gm) is contained in C_U=im(c_U). There is no finite-error loss in this step.

### The degree-one Picard term is finite

Let L be the image of B in Pic(Ybar), and let A=Pic^0_(Y/k),red. The group A(kbar) is torsion: each point is rational over some finite field. The subgroup F=L∩A(kbar) is both finitely generated and torsion, hence finite. Put Q=NS(Ybar)/image(L); Q is finitely generated and its Gamma action has finite image. We have

\[
0\longrightarrow A(\bar k)/F\longrightarrow
\operatorname{Pic}(\bar U)\longrightarrow Q\longrightarrow0.
\]

Lang's vanishing H¹(Gamma,A(kbar))=0 can here be seen directly: arithmetic Frobenius minus identity is an isogeny, because its differential is minus identity, so it is surjective on geometric points. The procyclic cohomology formula applies because A(kbar) is torsion. Since H²(Gamma,F)=0, the sequence 0→F→A(kbar)→A(kbar)/F→0 implies H¹(Gamma,A(kbar)/F)=0.

Thus H¹(Gamma,Pic(Ubar)) injects into H¹(Gamma,Q). The latter is finite: the torsion of Q is finite, and after passing to a finite quotient acting on its free quotient, the remaining H¹ is finite-group cohomology of a finite-rank lattice. The kernel procyclic subgroup has no nonzero continuous homomorphism to a torsion-free discrete lattice. Therefore H¹(Gamma,Pic(Ubar)) is finite, uniformly across all primes.

### The Hochschild–Serre filtration

Use the multiplicative-sheaf Hochschild–Serre spectral sequence

\[
E_2^{a,b}=H^a(\Gamma,H^b(\bar U,G_m))
\Longrightarrow H^{a+b}(U,G_m).
\]

The kernel of restriction H²(U,Gm)→H²(Ubar,Gm)^Gamma has a two-step filtration whose associated groups are a quotient of H²(Gamma,E) and a subquotient of H¹(Gamma,Pic(Ubar)). Its first part is generated by arithmetic unit cups on prime-to-p torsion; its second part is finite. Since U is regular, its full H²(Gm) is torsion. Consequently

\[
\ker\bigl(\operatorname{Br}'(U)[p']\to
\operatorname{Br}'(\bar U)^\Gamma[p']\bigr)/C_U
\]

is finite. The inclusion C_U in that kernel is immediate because the arithmetic characters vanish over kbar. No degeneration of this spectral sequence is assumed, and no canonical splitting of its filtration is required.

## 2. The geometric prime-uniform input

The assumed surface Tate assertion at ell0 gives divisor Tate on every smooth variety by the already-audited Kahn–Morrow reduction. Together with the already-proved Galois splitting of the divisor subspace on smooth opens, geometric Kummer gives

\[
V_{\ell_0}\operatorname{Br}'(\bar U)^\Gamma=0.
\]

Finite cotype implies Br'(Ubar)^Gamma[ell0 infinity] is finite. No full Frobenius semisimplicity is added: the needed divisor splitting is already independently proved in Part B. Qin Theorem5.2 now makes Br'(Ubar)^Gamma[p'] finite. The preceding Hochschild–Serre kernel calculation therefore proves Br'(U)[p']/C_U finite.

An alternative verification of Qin's hypothesis, suggested and checked by Part D, uses the already-proved fixed-ell unit-cup lemma plus Qin Lemma5.1 for the identity alteration U→U: the arithmetic-to-geometric invariant map has bounded-exponent cokernel, hence finite ell-primary cokernel. Since arithmetic unit cups vanish geometrically, geometric invariants at ell0 are finite. The direct divisor-splitting argument above avoids needing this extra use of Lemma5.1 outside Qin's own proof.

## 3. Integral trace down an alteration

Now let T be smooth quasi-projective and geometrically connected. Choose a projective proper generically finite alteration g:U→T, degree d, with U open in a smooth projective Y. This is de Jong Theorem4.1/Remark4.2 applied to a projective compactification; the chosen source and target have ample line bundles.

For every n prime to p, Riou's finite-coefficient purity/Gysin construction gives

\[
g_*:H^2(U,\mu_n)\longrightarrow H^2(T,\mu_n),
\qquad g_*g^*=d.
\]

Exact primary source: https://www.numdam.org/item/AST_2014__363-364__301_0.pdf, Proposition2.5.13 and Remark2.5.14, Corollary3.1.2, Lemmas3.5.8–3.5.10, printed pp.323,333–335. The equality with multiplication by d is valid without assuming d invertible modulo n: the composite is a scalar endomorphism of the constant coefficient sheaf, and restriction to the dense finite-flat locus computes this scalar as d. The argument in the cited degree lemma does not require dividing by d. The finite-flat trace normalization is Proposition2.5.13, including inseparable generic degrees.

These maps descend to compatible corestrictions on Br'[n]. One way to check this without invoking an unstated integral Gm trace is as follows. A Pic(U)/n class restricts to zero on the generic field of U. The finite-coefficient Gysin trace commutes with restriction to the generic finite field extension, so its image has zero generic Brauer class on T. Regularity makes Br'(T)→Br'(k(T)) injective, by the opened Grothendieck Brauer II Proposition1.4/Corollary1.8. Thus its image in Br'(T)[n] is zero. The induced maps are independent of Kummer lifts and compatible as n varies.

The projection formula and the degree-one Kummer norm identity show

\[
\operatorname{cor}_g(\chi|_U,u)=(\chi,\operatorname{Nm}_{k(U)/k(T)}u).
\]

The field norm of a global unit on U is a unit on T: properness ensures that codimension-one valuations of T extend to centers on U, and the norm valuation is the weighted sum of the zero valuations of u. Equivalently use the finite normalization in k(U), with the proper birational map from U, and inspect height-one points. The Kummer trace identity is checked on the dense finite-flat locus and extends because H¹(T,μ_n)→H¹(dense open,μ_n) is injective on a normal scheme. Purely inseparable factors give the corresponding degree power and create no exception for n prime to p.

Thus both pullback and corestriction preserve the respective unit-cup subgroups. If B_T=Br'(T)[p']/C_T and B_U=Br'(U)[p']/C_U, there are maps B_T→B_U→B_T whose composite is multiplication by d. The group B_U is finite by the compactification case, so a single positive integer h annihilates B_T.

Finally C_T is divisible, being the image of units(T)⊗D. The exact sequence for multiplication by h therefore makes B_T[h] a quotient of Br'(T)[h]. The latter is finite by Kummer and finite-coefficient etale cohomology (replace h by its prime-to-p part if needed). Since B_T=B_T[h], B_T is finite. This proves the asserted uniform smooth-source lemma.

For a connected component not geometrically connected over k, use its finite field of constants k'. The character from k restricts to [k':k] times the character normalized over k'. Multiplication by that integer is surjective on D, so the two unit-cup images coincide. Thus finite constant fields and finite disjoint unions require no additional hypothesis.

## 4. Global consequence being supplied by Part D

Replace the coefficient ring Z_(ell) by Z[1/p] in the already-audited arbitrary-base descent, and replace Qell/Zell by D. Every finite-rank unit matrix has one finite Smith defect across all primes. The Gm cover-kernel lemma already holds over Z[1/p]. The smooth unit-cup cokernel is now one finite group. Thus uniform L,M,N give the same equation LMN a−c_S(v) in the finitely generated restriction kernel for every a in A_S=H²_et(S,Gm)[1/p].

The only change in the final algebra is that one must not assume a prime-uniform finite-cotype decomposition. Instead the unit-cup image is divisible, so the fixed-h torsion of the target quotient is a quotient of Br'(T)[h], which is finite by finite-coefficient cohomology. Hence A_S/C_S is finitely generated over Z[1/p], and its torsion Br'(S)[p']/C_S is finite. Proper smooth geometrically connected families preserve units by Stacks36.32.6; their entire prime-to-p relative Brauer cokernel is consequently finite. The regular-pencil converse retains the exact surface-Tate equivalence. This is stronger than separate finiteness of each primary component.

Part D's independent full abstract proof is in pending_post05_b3_prime_uniform_d.md. The primary CP05 deliverables remain unchanged during the freeze.

## Written-proof audit and checkpoint scope

Root and Part D independently read this entire proof note and passed it. Part D additionally opened Riou and read all the exact finite-coefficient trace passages, including the complete degree proof. The only wording correction was to replace an imprecise reference to lower-codimension boundary by codimension at least two. This note is a fully proved, audited extension awaiting numbered-TeX integration after CP05; it is not marked as an unproved proposed argument. The universal surface-Tate hypothesis remains unproved.

An alternative source path for the geometric uniformity is also available. Qin2024 Proposition2.1 proves the entire prime-to-p geometric invariant Brauer group is unchanged by a dense smooth open up to a finite cokernel, using the finite-order residue groups in Lemmas2.2–2.3. Thus the compactification case can instead use Qin2021 Theorem1.2 for the proper Y, followed by that Proposition2.1. The current proof deliberately retains the direct nonproper Theorem5.2, whose exact proof dependencies have now been checked. No general Frobenius semisimplicity conjecture is inserted.
