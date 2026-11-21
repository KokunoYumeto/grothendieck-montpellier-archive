# Finite presentations, Frobenius matrices, and the proposed Sinnott bound

Date: 2026-11-21. Author/reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

Throughout this note p is the characteristic of the finite base field, and ℓ is the distinct prime defining the geometric tower. This reverses the names of the two primes in Sinnott's paper.

## Outcome

A finite presentation of the relevant full étale fundamental group is known. It does **not** supply the proposed finite Laurent-polynomial Frobenius matrix. The presentation is profinite, the familiar finite surface-word presentation concerns the prime-to-p quotient, and the available arithmetic Fox constructions have completed coefficients. The directly relevant skew-abelian tower theorem of Asvin G. controls valuations at ℓ, not at p.

There is a useful conditional route: a *fixed nonzero rational function* describing the actual primitive Frobenius determinants would give an eventual uniform p-adic determinant bound by an elementary reduction argument below. The geometric construction of that function, and the treatment of the growing Frobenius character orbit, remain missing. No general rational-factor or bounded-exponent witness has been supplied by this probe.

## 1. Which fundamental group and which finite presentation?

The prime-to-p geometric group of a proper genus-g curve has the familiar surface presentation with 2g generators and the single finite word given by the product of g commutators. This does not compute the characteristic-p étale cohomology of the ℓ-power covers. An open subgroup U of a pro-prime-to-p group has

\[
 H^1_{\mathrm{cont}}(U,\mathbf F_p)
 =\operatorname{Hom}_{\mathrm{cont}}(U,\mathbf F_p)=0:
\]

every continuous homomorphism factors through a finite quotient of order prime to p. The actual full étale group of a cover can have positive-dimensional H¹ with F_p coefficients, dual to the geometric étale p-torsion of its Jacobian. Thus the surface presentation cannot be silently substituted for the full group in this calculation. This is about omitted characteristic-p étale information; a proper étale p-cover is not being called ramified.

The full group is nevertheless finitely presented **as a profinite group**. Esnault–Shusterman–Srinivas, *Finite presentation of the tame fundamental group*, Selecta Math. 28 (2022), article37, Theorem1.1, includes every smooth projective variety. Their definition on p.2 permits finitely many normal generators of the relation kernel inside a free profinite group. It does not say those generators lie in its discrete free subgroup. They distinguish the surface-word presentation on p.4. Shusterman's *Balanced presentations for fundamental groups of curves over finite fields*, MRL29(4)(2022),1251–1259, Theorem1.1 and Corollary1.2, give the arithmetic balanced presentation and coherence; its proof estimates cohomological dimensions, without producing finite discrete relator words or Frobenius words.

Even if the geometric relators were finite words, adjoining arithmetic Frobenius introduces expressions of the form

\[
             F x_i F^{-1}=\varphi(x_i).
\]

Finite topological generation of the group places \(\varphi(x_i)\) in a free/profinite quotient; it does not put it in the discrete word subgroup or give a uniform finite support bound on its Fox derivatives. That additional assertion is precisely what the proposed shortcut needs.

## 2. What the arithmetic Fox literature actually provides

Kodani–Morishita–Terashima, *Arithmetic topology in Ihara theory*, PRIMS53(4)(2017),629–688, §§4.1–4.3, defines continuous pro-ℓ Fox derivatives in \(\mathbf Z_\ell[[F_r]]\). Its Magnus matrix is a crossed cocycle; after abelianization the Gassner matrix has coefficients in \(\mathbf Z_\ell[[u_1,\ldots,u_r]]\). Proposition4.3.4 explicitly expresses the entries as infinite sums of ℓ-adic Milnor coefficients. The setup is a number-field Galois action on a punctured projective line's pro-ℓ group. It is evidence for the completed-coefficient distinction, not a theorem identifying the characteristic-p Tate module of our proper-curve tower with that matrix.

The finite matrix size is therefore not the same statement as finite Laurent support. No theorem making these actual Frobenius entries rational functions was found in the inspected sources.

## 3. A directly matching geometric tower theorem, with a different valuation

Asvin G., *On the variation of Frobenius eigenvalues in a skew-abelian Iwasawa tower*, Algebra & Number Theory17(12)(2023),2151–2179, DOI10.2140/ant.2023.17.2151, treats geometric towers over a fixed finite field. Definition8, CaseB, pulls back multiplication by ℓ^n on an abelian variety; it requires geometric connectedness. Frobenius acts on the deck group through a matrix Q. Lemma17 describes a finite free module over an ℓ-adic power-series Iwasawa ring with semilinear Frobenius.

There are two exact restrictions on using this for the present task:

1. Section3.1, equation(6), obtains the return operator by multiplying the matrix evaluations around the **whole** Frobenius orbit. The orbit length grows with n. It is not a fixed expression \(\det(1-M(\zeta_{\ell^n}))\).
2. Theorems19,23,26 give **ℓ-adic** congruences. In the first paragraph of §3.3, p.2169, a power series is truncated to a polynomial at a degree depending on n because \(\zeta_{\ell^n}-1\) has positive ℓ-adic valuation. At the prime p≠ℓ, a nontrivial ℓ-power root has the same nontrivial order after reduction, so \(\zeta_{\ell^n}-1\) is a p-adic unit. That truncation argument does not transfer.

The paper does not supply a fixed Laurent matrix at the different coefficient prime p. Its full prime-to-characteristic cohomology has constant character multiplicities; the rank of the characteristic-p étale stable part is a further issue. No cross-prime exponent bound is deduced here from ℓ-adic convergence.

## 4. Completed coefficients alone allow arbitrary primitive valuations

The following elementary calculation makes the missing hypothesis explicit. It is an abstract algebra statement, **not** a realization by the Jacobians of a curve tower.

Set

\[
 R=\varprojlim_n\mathbf Z_p[C_{\ell^n}],
\]

with the usual quotient maps, and write γ_n for a generator at level n. For a≥0 define a compatible idempotent e_a by its component at level n:

\[
 e_a^{(n)}=
 \begin{cases}
 1,&n\le a,\\[2mm]
 \displaystyle\ell^{-(n-a)}
   \sum_{j=0}^{\ell^{n-a}-1}\gamma_n^{j\ell^a},&n>a.
 \end{cases}
\]

The denominator is a p-adic unit. The quotient from level n+1 to n sends this average to the preceding average, so e_a belongs to R. On a character of exact order ℓ^b, its value is 1 if b≤a and 0 otherwise. Character decomposition after a finite unramified coefficient extension proves that these are idempotents, with e_a e_c=e_min(a,c).

Put ε_0=e_0 and ε_a=e_a−e_(a−1) for a≥1. These are orthogonal conductor idempotents. At level n, ε_a vanishes for a>n and the sum from a=0 to n is 1. Consequently **any** sequence of nonnegative integers b_a defines

\[
                  B=\sum_{a\ge0}p^{b_a}\varepsilon_a\in R.
\]

There is no convergence problem: the sum is finite at each quotient level. For every character χ of exact order ℓ^a,

\[
                        \chi(B)=p^{b_a}.
\]

Choose b_a≥1. Multiplication by F=1−B is an automorphism of the free rank-one R-module R, because each conductor component 1−p^{b_a} is a p-adic unit. On the conductor-a summand, the cokernel of 1−F has exact exponent p^{b_a}. The integers b_a can grow arbitrarily quickly. Thus a rank-one finite matrix over the completed algebra, even an invertible one, does not imply a primitive-exponent bound.

The same point survives nonconstant-deck semilinearity. Let u∈Z_ℓ^× act on R by γ↦γ^u. It preserves every ε_a. Define the semilinear automorphism F=(1−B)u. After extending the coefficient ring to split C_(ℓ^n), the characters of conductor ℓ^a fall into u-orbits of length

\[
                       d_a=\operatorname{ord}_{\ell^a}(u).
\]

On each such orbit F is the cyclic permutation matrix multiplied by c_a=1−p^{b_a}. The relations in the cokernel of 1−F successively eliminate all but one basis vector; the remaining relation is multiplication by 1−c_a^{d_a}. Therefore that orbit cokernel is the coefficient ring modulo this element. If b_a≥2, the binomial lifting-of-exponent calculation (valid also for p=2) gives

\[
               v_p(1-(1-p^{b_a})^{d_a})=b_a+v_p(d_a).
\]

For completeness, when m is prime to p the first term of \((1+x)^m-1\) has valuation v_p(x) and every later term has larger valuation. Raising successively to the pth power increases the valuation by one when v_p(x)≥2: the linear term has valuation v_p(x)+1, the middle terms have larger valuation, and the last term has valuation p·v_p(x)>v_p(x)+1. Splitting d_a into its p-power and prime-to-p parts proves the displayed equality. Finite unramified scalar extension preserves elementary-divisor exponents. In particular, these semilinear cokernels again have unbounded or arbitrarily prescribed large exponents. No Weil-weight, polarization, or geometric-realization condition is asserted for this example.

## 5. What an actual fixed rational determinant would prove

Let K/Q_p be finite, with residue field F_(p^s), uniformizer ϖ, and normalized valuation v_ϖ. Let f(X)∈K(X) be nonzero. Write

\[
 f(X)=\varpi^\mu G(X)/H(X),
\]

where G,H are integral Laurent polynomials, each with at least one unit coefficient. Multiplying each by a monomial, suppose their reductions have degrees at most D. If

\[
                   \operatorname{ord}_{\ell^a}(p^s)>D,
\]

then every primitive ℓ^a-th root ζ satisfies

\[
                         v_\varpi(f(\zeta))=\mu.
\]

Indeed adjoining these roots is unramified at p, and the reduction of ζ has exact order ℓ^a. Its minimal polynomial over F_(p^s) has degree ord_(ℓ^a)(p^s), so it cannot be a root of either nonzero reduced polynomial of degree ≤D. Both G(ζ) and H(ζ) are units. Finally ord_(ℓ^a)(p^s) tends to infinity: if it stayed bounded, infinitely many ℓ^a would divide one of the finitely many nonzero integers p^(sj)−1 with j in that bounded range. This proves eventual constancy of the valuation.

In particular, for a fixed integral Laurent matrix M(X) of fixed size, with nonzero f(X)=det(1−M(X)), its high-conductor cokernels have uniformly bounded p-primary exponent: the sum of their nonnegative elementary-divisor valuations is the bounded valuation of f(ζ). With an actual identification of these cokernels with the primitive rational p-primary groups, that would eventually meet A47's increasing degree threshold in genus two and characteristic two. This paragraph is a **conditional implication**. No such identification or fixed determinant has been constructed for the nonconstant-deck tower.

In that tower, replacing M(ζ) by the product of matrices over a growing Frobenius orbit produces a sequence f_a, not the single f above. The lemma cannot be applied to f_a without a uniform bound on its reduction degree or another theorem controlling those orbit products.

## 6. Exact Sinnott hypothesis and the remaining geometric task

Sinnott, *On a theorem of L. Washington*, Astérisque147–148(1987),209–224, §1.16, calls a measure rational when its Fourier transform agrees with one fixed rational function at all but finitely many prime-power roots. His Theorem3.2, pp.214–218, assumes such a measure, supported on the unit group; infinitely many vanishing Γ-transform values force R(Z)+R(Z^−1)=0. The number-field application then verifies a specific rational-function identity for Dirichlet L-values. It is not a theorem for arbitrary completed matrices or arbitrary geometric Artin factors. Section1.8's Fourier inversion explicitly allows arbitrary functions on the roots for unrestricted measures.

Two extra cautions matter. The Γ-transform is not automatically the determinant of a growing semilinear orbit product. Also, obtaining nonvanishing from the theorem requires the relevant inversion-sum to be nonzero. In coefficient characteristic two, a symmetric R automatically has R(Z)+R(Z^−1)=0, so rationality by itself would still not give that contrapositive. This is a conditional scope warning, not a claim that a geometric measure R has been constructed or must be symmetric.

A possible geometric formulation would use the Poincaré family of degree-zero line bundles and the Frobenius maps between its coherent-cohomology fibres, rather than the prime-to-p surface presentation. This points to functions or sections on the Jacobian evaluated at torsion classes. It does not identify those evaluations with a fixed rational function on G_m, nor control their full return products or integral p-adic lifts. No general theorem accomplishing these identifications was located in this bounded search. Specialized CM elliptic-function analogues of Sinnott were seen in the search, but not verified as hypotheses applicable to an arbitrary genus-two Jacobian.

The exact remaining task is therefore to prove a geometric rationality or orbit-product valuation theorem for the **actual** primitive p-primary Frobenius cokernel, with its nonconstant deck action and prescribed pointing. Finite profinite presentation, finite matrix size, and tower-prime convergence do not establish it. No main witness-supply gate has been closed here.

## Retained primary sources and reading scope

All PDFs and extracted text are retained under `fox_probe_sources/` in this directory.

- `ess2021.pdf`: https://page.mi.fu-berlin.de/esnault/preprints/helene/141_ess.pdf ; refs `turn460302903view0`, `turn349318753view1`. Read pp.2–4 definitions, Theorem1.1, and surface-presentation distinction. No complete proof of the general-dimensional theorem was rechecked.
- `shusterman2018.pdf`: https://arxiv.org/pdf/1811.04192 ; ref `turn973123487view1`. Read the complete six-page preprint, including the proof of Theorem1.1 and Corollary1.2; the external cohomological theorems cited there were not reproved.
- `kmt2017.pdf`: https://arxiv.org/pdf/1608.07926 ; refs `turn460302903view2`, `turn651466722view4`. Read the number-field setup, §4.1, the Magnus-cocycle definition, and §4.3 including the full displayed proof of Proposition4.3.4. No whole-paper reading claimed.
- `asvin2023.pdf`: https://msp.org/ant/2023/17-12/ant-v17-n12-p03-p.pdf ; ref `turn877236471view0`. Read Definition8/Remark9, Lemma17 with proof, the §3 setup, Lemma21 with proof, §3.1 including equation(6), Theorems23/26 and their stated scopes, and the first truncation paragraph of §3.3. No complete check of the long congruence proofs claimed.
- `sinnott1987.pdf`: https://www.numdam.org/item/AST_1987__147-148__209_0.pdf ; refs `turn460302903view1`, `turn349318753view0`. Read §1.8–1.16 and the entire displayed proof of Theorem3.2 including Lemma3.6. The proof's external/already-stated independence inputs were not independently reproved.

The elementary completed-algebra construction and fixed-rational-function lemma above were checked in full. No finite curve, actual infinite tower, or Frobenius presentation was computed in this probe. No new finding number or novelty claim is assigned.
