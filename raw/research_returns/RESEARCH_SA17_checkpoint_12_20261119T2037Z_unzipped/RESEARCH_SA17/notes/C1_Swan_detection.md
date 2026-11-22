# C.1: Swan induction, genuine reductions, and the necessary-condition failure

Recorded 2026-11-19T16:28:49Z by RESEARCH_SA17_FINISH/descent_groups. This note answers the requested induction/detection branch. It does not claim an all-rings classification.

## Exact source scope

The original Dress paper, *Contributions to the theory of induced representations*, LNM342 (1973), pp183–240, was downloaded from the University of Rochester archive and read at printed pp209–212 (PDF pp220–223). Proposition5.2 is on printed p210; its application on pp210–211 defines X(G,A), for **every commutative ring A**, using finitely generated A-projective AG-modules and exact sequences. This is exactly the manuscript's category. It gives integral hyperelementary induction and rational cyclic induction; p-local hyperelementary induction follows from the localized statement of Proposition5.2. The p211 calculation gives |G|² times the unit in the cyclic induction ideal. Printed p212 gives the compatible-restriction description, retaining conjugation and subgroup embeddings.

Primary URL: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/SLN342.pdf . Local original: sources/Dress1973_LNM342.pdf; extracted text: sources/Dress1973_LNM342.txt; the original p210 image was inspected as sources/Dress1973_p210.png. The web fetch rejected the 19.3MB file for size; direct download succeeded. The original Swan1960 journal PDF was not obtained, so no claim of directly inspecting its Corollary4.2 is made.

Cross-checks in original research papers: Bartels–Lück, arXiv:math/0404486v2, Lemma4.1(a),(c),(e), printed pp19–20, states the integral, p-local, and rational families separately. Hambleton–Taylor–Williams, ANT3 (2009), Theorem3.10 p523 and Example3.12 pp523–524, gives the scalar p-local formula for a hyper-p-closed family. Its use here is optional; the ordinary Swan action already proves detection.

## C:Swan_subgroup_detection — exact, but only a sufficient vanishing gate

For any commutative k and finite G put B=k tensor Q and D_k(G)=ker(R_k(G)→R_B(G)). The kernel is a Mackey functor and a module over the integral Swan Green functor. Indeed, restriction preserves finite k-projectivity; induction is a finite direct sum on underlying k-modules; tensor with a Z-free lattice preserves finite k-projectivity. Every exact sequence of Z-free lattices splits over Z, so tensoring with any k-module remains exact. Every admissible sequence in the k-category splits over k, so arbitrary base change is exact. The usual tensor-induction identity gives Frobenius reciprocity. These observations require neither flatness over Z nor noetherianity of k.

Choose Swan elements u_H with 1=Σ Ind_H^G u_H over the hyperelementary family. For x∈D_k(G),

    x = Σ Ind_H^G (u_H · Res_H^G x).

Consequently D_k(G)→∏_H D_k(H) is injective. After tensoring the groups with Z_(ell), ell-hyperelementary H suffice. After tensoring with Q, cyclic H suffice. The integral cyclic restriction kernel is annihilated by |G|², by applying the analogous cyclic formula for |G|² times the unit. These localizations are localizations of **abelian groups**, not replacement of the coefficient ring k by k_(ell). No such coefficient-localization injectivity has been established.

For a cyclic group C_m with m invertible in k, a finite k-projective k[C_m]-module is projective over k[C_m]: average a k-linear splitting over the group. Conversely group-ring projectivity implies k-projectivity. Therefore

    R_k(C_m)=K0(k[z]/(z^m−1)),

and its generic comparison is an ordinary K0 comparison for this commutative finite étale k-algebra. This is the intrinsic portion of the cyclic reduction. When m is not invertible, this replacement of the lattice category by group-ring projectives is invalid.

For completeness, a strictly henselian local k of residue characteristic ell splits every cyclic group C_m of order prime to ell. If H=C_m⋊P is ell-hyperelementary, the character idempotents of k[C_m] decompose the category as a product, over P-orbits of characters chi, of the exact categories R_k(P_chi). The equivalence sends a representation to its chi-eigensummand; its inverse tensors with chi and induces from C_m⋊P_chi. This commutes with k→B. Thus D_k(H) is a direct sum of the corresponding p-group kernels. This is a **sufficient** reduction to p-group vanishing, not a claim that ordinary restriction to P alone detects every character summand. No descent of K0-injectivity along a finite étale splitting cover is assumed.

## C:Swan_subgroup_boundary — why subgroup injectivity is not a necessary C.1 criterion

The positive case k=Z already disproves the proposed necessary condition that every cyclic or hyperelementary generic comparison be injective. The manuscript's C:DVR includes the integral symmetric-group theorem, theta_Z an isomorphism. Yet for G=C_p, Köck, *The Grothendieck–Riemann–Roch theorem for group scheme actions*, Ann.Sci.ENS31 (1998), Example6.9(d), printed pp443–445, identifies

    ker(R_Z(C_p)→R_Q(C_p)) ≅ Pic(Z[zeta_p]).

The source's exact category is locally free equivariant modules, identified on Spec Z with precisely Z-free integral representations; see its Definition2.1 and Example6.9 proof. The map sends an invertible Z[zeta_p]-ideal I to [I]−[Z[zeta_p]], with C_p acting by multiplication by zeta_p. Primary original opened at https://numdam.org/item/10.1016/s0012-9593(98)80140-7.pdf . This is a kernel in the lattice Grothendieck group, not merely in the projective group-ring class group.

Here is an explicit nonzero case, without relying on a table of cyclotomic class numbers. Let F=Q(sqrt(−23)), omega=(1+sqrt(−23))/2, and I=(2,omega) in O_F=Z[omega]. The norm of a+b omega is a²+ab+6b². There is no element of norm2: for b≠0 this form is (a+b/2)²+23b²/4>2, and for b=0 it is a square. Thus I, which has ideal norm2, is not principal. The two primes above2 are I and J=(2,omega−1). The element omega−2 has norm8, belongs to I, and is a unit modulo J. Hence (omega−2)=I³, and [I] has order3.

The quadratic Gauss sum g=Σ_{a mod23}(a/23) zeta_23^a satisfies g²=−23, so F is the quadratic subfield of L=Q(zeta_23), and [L:F]=11. If I O_L were principal, taking ideal norms would make I^11 principal; this contradicts the order3 of [I]. Therefore Pic(Z[zeta_23]) is nonzero. Köck's identification yields a nonzero element of D_Z(C_23), although D_Z(S_n)=0 for every n.

Since induction commutes with generic comparison, every induced image of this class in D_Z(S_n) is zero. The failure is not a flaw in Swan detection: that theorem detects a symmetric-group class from its compatible restrictions; it does not assert that every subgroup kernel class extends to, or has nonzero induction in, a symmetric group. A necessary-and-sufficient subgroup formulation must retain the compatibility/induction data, which would again be a representation-theoretic reformulation rather than the requested intrinsic ring classification.

## Consequence for the remaining research

The Swan route is useful for upper bounds and sufficient criteria and separates rational cyclic obstructions from integral torsion. It does not produce the requested intrinsic all-rings criterion. Ordinary and derived arithmetic-fibre data have already been shown insufficient in C:derived_fibre_twins; the present argument independently excludes the overstrong criterion that all cyclic or hyperelementary generic comparisons must be injective. The arbitrary mixed-characteristic singular-ring gate remains open.

No novelty claim is made: the induction and cyclotomic calculation are established results. The application to the precise manuscript category and the identification of the false necessary condition were checked in this run.
