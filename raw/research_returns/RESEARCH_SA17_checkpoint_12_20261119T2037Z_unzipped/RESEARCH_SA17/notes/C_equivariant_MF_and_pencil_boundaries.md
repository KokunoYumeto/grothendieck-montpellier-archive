# Equivariant MF transfer and the zero-curvature pencil

AI-produced research note, GPT-6 Astra Pro (OpenAI), RESEARCH_SA17 / c1_mixed_s3, 2026-11-19. Uncompiled research. No main coefficient-family gate is claimed closed. None of the proposed pencil-category identifications below is used as a theorem about Swan classes.

## An equivariant extension of the elementary MF construction

Let S0 be regular noetherian local, g a nonzero nonunit, R=S0/(g), and G a finite group. For an R[G]-module X that is MCM over R, choose a surjection F0 -> X with F0 finite free over S0[G]. Its kernel F1 is finite free over S0, because X has projective dimension one over S0. It retains a strict G-action. The inclusion Phi:F1 -> F0 has a unique G-equivariant partner Psi:F0 -> F1 satisfying Phi*Psi=Psi*Phi=g. The underlying S0-ranks of F0 and F1 agree.

On (F0 mod g) direct sum (F1 mod g), let a second, commuting C2 act by

    T = [[I,Phi],[Psi,-I]].

Subtract the direct sum of F0 mod g with external trivial action and F1 mod g with external sign action. This gives a class Delta_g^G(X) in the kernel of the Swan map for G times C2 after inverting two.

The same conjugacy P=I+D*sigma/2 as in C:MF-Swan-transfer is G-equivariant, and proves this generic assertion. Presentation independence can be checked without averaging over G: two free S0[G] covers admit their direct-sum common cover. Projection of its kernel onto either free cover splits S0[G]-linearly. The resulting presentation is equivalent to the old one plus an identity presentation; its contribution is the external regular C2 tensor that free cover, and the subtraction cancels it. A horseshoe presentation for an exact sequence of MCM R[G]-modules has endpoint subcomplex and quotient. The source modules F1 need only form an underlying S0-split exact sequence, which is sufficient: after reducing modulo g, the block involutions preserve the endpoint free submodules and have the expected free quotient. The baseline classes add by the same admissible sequences. Thus the construction is additive.

Forgetting the extra C2 sends this class to zero: both its positive and negative terms have the same underlying G-representation F0 direct sum F1. It is therefore not, by itself, a transfer to the original G Swan group.

If chi:G -> C2 is a character, restriction along its graph gives a map to the Swan group of G. The new G-action on the matrix-factorization sum is rho(g)*T^(chi(g)), where chi(g) is written as 0 or 1. The baseline is F0 mod g plus chi tensor F1 mod g.

This graph-restricted map vanishes on every X that is already R-free. Indeed let K=im(Phi mod g). The two exact sequences

    0 -> K -> F0 mod g -> X -> 0,
    0 -> X -> F1 mod g -> K -> 0

are admissible, because X is free and consequently K is free. The second occurrence of X is im(Psi mod g). The invariant submodule K direct sum X in the MF sum has graph action K direct sum (chi tensor X), and its quotient has action X direct sum (chi tensor K). Its class equals F0 mod g plus chi tensor F1 mod g. Thus the construction factors through the cokernel of the R-free-to-MCM map; it is not a retraction on the kernel of that map.

These elementary arguments are a research extension of the audited nonequivariant MF lemma. They have not undergone a second independent audit or been promoted.

## A valid unit-curvature calculation

Assume A is a complete dyadic DVR, 2=v*pi^e with e>=2. For any unit c in A, the polynomial

    f(w)=w^2+2w-c*pi^3

is irreducible over Frac(A). If a root had integral valuation r, for r<=1 the term w^2 would have unique minimum valuation, and for r>=2 the constant term would have unique minimum valuation. Both are impossible. Its roots have valuation 3/2.

The local curve C=A[[w]]/(f) is a one-dimensional noetherian domain. Prime filtration generates G0(C) by [C] and its residue class [kappa]. Since C/(pi) has length two and C/(w) has length three, multiplication by pi and by w gives 2[kappa]=3[kappa]=0. Hence G0(C)=Z[C], and the ordinary singularity Grothendieck group G0(C)/Z[C] is zero.

This is a calculation of an ordinary curve Grothendieck group. It does not prove zero of a Swan class or of the Grothendieck group of a category with a specified cohomological support.

## Residual zero curvature is a separate case

Curvature that is zero modulo pi need not be literally zero. The already recorded node family in notes/C_ramified_nodes_research.md, for e=2 and xy=pi^3*u, is

    a=1+pi^2*b,
    h=b*(v+b),
    T=[[a,x],[-pi*h*y/u,-a]].

It is an actual involution. A lift has curvature a unit multiple of pi*h relative to the node equation. When h is a unit, the corresponding quadratic pencil has constant term of valuation four, not three; in all cases it has the exact factorization

    w^2+2w-pi^4*h
      = (w-pi^2*b)*(w+pi^2*(v+b)).

Thus the unit-curvature irreducible-cusp argument does not include this residual-zero family. The factorization is an exact polynomial identity after 2=v*pi^2; it is not a finite detector claim. The previous unsuccessful higher-page parity construction for this family and its explicit additivity counterexample are already preserved by the other agent in code/C_finish_ramified_higherpage_failure.py and its log. They are not rerun or reinterpreted here.

## The precise category issue for the pencil proposal

The R-free C2 category, modulo induced regular representations, is the relevant relative stable category. It should not be replaced by the whole ordinary MCM category: C:odd-node-MCM-comparison-boundary shows that this replacement kills the entire generic Swan kernel on every odd node.

Burke and Walker, Matrix factorizations in higher codimension, arXiv:1205.2552, Theorem 1 and Theorem 2.10 / Appendix A.4, explicitly treat regular ambient rings without an equicharacteristic restriction. Their relative singularity category consists of bounded coherent complexes perfect over the indicated ambient ring, modulo perfect complexes over the quotient. Sections 8.1-8.2 identify and realize cohomological supports. The original PDF was independently opened at https://arxiv.org/pdf/1205.2552 (tool refs turn311337125view2, turn744760135view0, turn744760135view1, turn744760135view2, turn744760135view3).

One still needs to identify the R-free relative category and its exact Grothendieck relations with the proposed pencil-support category. Moreover a full triangulated subcategory need not inject on K0 into its ambient category. Consequently vanishing of an ordinary pencil fiber's singularity K0 does not by itself establish vanishing in the primary-support category. The residual-zero component and this support-to-K0 passage are both unresolved in the present argument.
