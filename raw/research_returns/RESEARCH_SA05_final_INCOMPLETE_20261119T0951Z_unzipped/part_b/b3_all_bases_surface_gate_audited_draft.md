# Pending post-checkpoint proof: all finite-type abelian-scheme finiteness has the surface-Tate gate

Written 2026-11-19 during the CP04 freeze. This file is outside the frozen deliverable tree. It is a proof draft for independent audit, not a claim that surface Tate has been proved.

## Statement

Fix p != ell. The following universal statements are equivalent:

1. Divisor Tate for every smooth projective surface over every finite extension of F_p.
2. For every finite-type F_p-scheme S, including nonreduced, singular and nonseparated S, and every abelian scheme A/S, H^1_et(S,A)[ell^infinity] is finite.
3. The same assertion restricted to Jacobians of smooth projective geometrically connected curve families with a section over nonempty opens of P^1 over finite extensions of F_p.

The existing all-base Kummer chain identifies statement 2 with the corresponding geometric invariant finiteness in the manuscript. The existing regular relative-curve theorem and root's surface-gate theorem prove 2=>3=>1. The new work is 1=>2 and, in particular, rational proper-cover descent of sections.

## Lemma: rational sections satisfy proper-cover descent

Let S be a noetherian F_p-scheme, q:T->S proper surjective, and A/S an abelian scheme. Then

0 -> A(S) tensor Q -> A(T) tensor Q -> A(T x_S T) tensor Q

is exact. Tensoring these Q-vector spaces with Q_ell gives the same exact equalizer sequence. No clearing of arbitrary Q_ell denominators is claimed.

First take S reduced. For an actual section b:T->A satisfying b pr1=b pr2 as maps T x_S T->A, let Z be its scheme-theoretic image in A and write j:Z->A, g:Z->S. Stacks Lemma29.42.10 says Z->S is proper and T->Z surjective. For every algebraically closed geometric point s, any two geometric points of T_s form a point of (T x_S T)_s, so their b-images coincide. Proper surjectivity T->Z persists after base change, hence Z_s has exactly one geometric point. Thus g is proper, quasi-finite and radicial, and surjective; it is a finite universal homeomorphism. Exact sources: Stacks Lemma37.44.1 for proper plus finite fibres=>finite, Lemma29.10.2 for radicial, and Kelly Proposition3/Corollary20 for Frobenius factorization.

There is an r and h:S->Z such that h g=F_Z^r and g h=F_S^r. For reduced S this also follows immediately from Stacks Lemma29.47.9: locally O_S embeds in g_*O_Z, every element has a p-power in O_S, and finitely many algebra generators on finitely many affine opens give a uniform r; the local maps b->b^(p^r) glue.

Define A^(p^r)=A x_(S,F_S^r) S. The pair (j h,id_S) is a section c:S->A^(p^r). Pulling it to T gives F^r_(A/S) b. If V^r:A^(p^r)->A is the iterated Verschiebung, then a=V^r c satisfies q^*a=[p^r]b. This establishes descent after multiplying by p^r.

For an element in the rational equalizer, first multiply by an integer to represent it by an actual section b; its actual Čech difference is torsion because its rational difference vanishes. Multiply again by its finite order. The preceding construction then descends a p-power multiple, proving rational surjectivity onto the equalizer. Injection follows because a separated target has a closed equality locus, and a surjective pullback of two sections over reduced S can coincide only when the sections coincide.

For general noetherian S, reduction S_red->S changes sections only by p-primary kernel and cokernel, as proved in the existing all-base section lemma through a finite nilpotent filtration and the additive Lie sheaves. Alternatively, Kelly Corollary20 directly gives the Frobenius factorization for the finite universal homeomorphism because the kernel is a bounded nilpotent ideal. Thus the rational equalizer statement holds without reducedness. For an ordinary finite Zariski cover, rational section descent follows directly from the sheaf property and exactness of tensor Q; the finite products involved cause no problem.

## Step 1: surface Tate gives invariant Kummer surjectivity on smooth separated bases

Let T/k be smooth separated finite type and A/T abelian. Root's Kahn/Morrow reduction gives divisor Tate for the total dual abelian scheme B=A^vee, which is itself smooth separated finite type over k. Write pi:B->T. Multiplication [m] has eigenvalue m^q on R^q pi_*Q_ell. Therefore the Leray spectral sequence degenerates in total degree2 by the distinct eigenvalues 1,m,m^2, and its eigenvalue-m summand is

e1 H^2(B_bar,Q_ell(1)) = H^1(T_bar,R^1 pi_*Q_ell(1)) = H^1(T_bar,V_ell A).

The earlier B3 proof identifies the eigenvalue-m algebraic divisor subspace with the geometric Kummer image N_T=A(T_bar) tensor Q_ell. Concretely the Poincare line bundle gives each section of A its normalized degree-zero line bundle on B; the zero section splits the Brauer obstruction to relative Picard sections. The relative NS part has eigenvalue m^2 and the base Picard part eigenvalue1, so the eigenvalue-m divisor subspace is precisely the Kummer image. Divisor Tate on B thus gives

kappa_T: N_T^Gamma -> H^1(T_bar,V_ell A)^Gamma

surjective, and it is injective by the previously proved rational Kummer/completion lemma.

## Step 2: descend invariant Kummer surjectivity to a separated singular base

Let S/k be reduced separated finite type. Choose a proper surjection q:T->S with T smooth separated finite type: use the finitely many reduced irreducible components, compactification/Chow lemma, and de Jong alterations, then restrict above S. The cover and all its data descend to a finite extension of k if necessary; alternatively keep the smooth components over their finite constant fields. The surface-Tate premise is quantified over these finite extensions.

Put T_a=T x_S ... x_S T (a+1 factors) and F=V_ell A. Proper Čech descent gives

E1^(a,b)=H^b(T_(a,bar),F) => H^(a+b)(S_bar,F).

The exact primary source is Stacks Lemmas85.36.3--85.36.6. Apply at finite ell-power coefficients, then pass to continuous cohomology; finite-coefficient cohomology is finite, so the inverse systems have the needed Mittag--Leffler property. The total-degree1 truncation involves only finitely many terms per degree. After tensor Q_ell, the usual five-term sequence identifies the kernel of

H^1(S_bar,F) -> H^1(T_bar,F)

with E2^(1,0). Each H^0(T_(a,bar),F) is pure of weight -1: after a finite constant extension evaluation on each geometric connected component injects into a fibre of V_ell A at a closed point, and those fibres have weight -1. Hence E2^(1,0), a subquotient of H^0(T_(1,bar),F), has no Gamma invariants. No general weight theorem for singular H^1 is needed.

Take c in H^1(S_bar,F)^Gamma. By Step1, q^*c=kappa_T(b) for a unique b in N_T^Gamma. The two pullbacks of c to T_1 agree; Kummer injectivity on the possibly singular T_1, already established in the all-base completion lemma, therefore gives pr1^*b=pr2^*b in A(T_(1,bar)) tensor Q_ell. The rational proper-cover equalizer above descends b to a in N_S. Its uniqueness makes a Gamma invariant. Then c-kappa_S(a) is an invariant vector in the weight-minus1 kernel E2^(1,0), so it is zero. This proves invariant Kummer surjectivity on every reduced separated S.

## Step 3: nonreduced and nonseparated bases

Nilpotent thickening does not alter F or its etale cohomology, and alters section groups only by p-primary groups. Thus it does not alter the rational Kummer comparison.

For a general finite-type S, choose a finite affine open cover. Each open and every finite intersection is separated, so Step2 applies to its components. The ordinary Zariski Čech-to-cohomology spectral sequence again has a degree-one pullback kernel which is a subquotient of H^0 on intersections, hence pure weight -1. A pulled-back invariant Kummer section descends by rational Zariski section descent. The same subtraction argument proves the global invariant Kummer comparison. It does not require a nonseparated compactification or a proper surjection from a separated scheme onto S.

Finally use the previously proved all-base Kummer equivalence chain (including finite cotype) to convert invariant Kummer surjectivity to finiteness of H^1(S,A)[ell^infinity]. This completes 1=>2.

## Opened primary sources and independent audit status

- Kelly, Universal homeomorphisms of and not of finite presentation, July4,2018: Proposition3 p2; Lemma18 pp8--9; Corollaries19--20 p9, full proofs opened by B and D. https://www.ms.u-tokyo.ac.jp/~kelly/pdfs/uh%20non-fp.pdf . B refs turn122340076view1, turn651953450view2/3.
- Stacks Lemma29.47.9, tag0CNF, full proof: https://stacks.math.columbia.edu/tag/0CNF , B ref turn220504476view0.
- Stacks Lemma29.42.10, proper graph image: https://stacks.math.columbia.edu/tag/01W0 , B ref turn651953450view1.
- Stacks Lemma37.44.1, proper finite fibres=>finite: https://stacks.math.columbia.edu/tag/0F2P , B ref turn220504476view2.
- Stacks Lemmas85.36.3--85.36.6, proper Čech/hypercover cohomological descent: https://stacks.math.columbia.edu/tag/0DHI , B refs turn122340076view0, turn651953450view0.
- Root independently checked the graph/Frobenius/Verschiebung mechanism and the invariant Kummer descent outline. D independently checked Kelly and the section construction. The complete note subsequently passed the independent D and root audits before the first formal review.

## Scope

This is an exact reduction of the universal prime-to-characteristic abelian-scheme finiteness assertion to divisor Tate for surfaces. It does not prove surface Tate or the resulting universal finiteness. The characteristic-primary counterexample remains valid and entirely separate. It does not on its own establish the relative-curve Brauer quotient theorem on every singular base: there the Picard-degree obstruction needs its own treatment.


## Final root audit

Root read the complete late proof in part_b/b3_all_bases_surface_gate_audited_draft.md. Independently opened and read Kelly Lemma18 and Corollaries19–20; Stacks29.47.9, 29.42.10,37.44.1 and85.36.3–6. Checked the schematic graph, relative Frobenius twist and Verschiebung; rational equalizer then flat Q-to-Qell extension; eigenvalue-m divisor/Kummer identification on the total dual abelian scheme; weight−1 Cech kernel; nilpotent and finite-open descent. The equivalence with surface Tate passes for every finite-type base. The arbitrary relative-curve Brauer quotient remains a separate unresolved scope.

Audited at 2026-11-19T05:49:43+00:00.
