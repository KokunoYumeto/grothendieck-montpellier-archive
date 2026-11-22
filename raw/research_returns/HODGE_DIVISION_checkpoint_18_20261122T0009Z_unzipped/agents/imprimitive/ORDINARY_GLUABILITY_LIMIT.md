# An exact limitation of ordinary-gluability arguments at three cohomology degrees

**Status.** New author derivation by `/root/imprimitive`, GPT-6 Astra Pro, inherited effort not externally exposed, HODGE_DIVISION, 21 November 2026. The parent independently verified the complete argument. This is a counterexample to an inference about cohomology types, not a balanced RM example or a semiregular seed.

## Construction within the primitive RM divisor model

Take X=E_i^4 with its product principal polarization. Let the real-multiplication endomorphism be the symmetric integer matrix

    U=diag([[1,1],[1,-1]], [[1,1],[1,-1]]),  U²=2I.

Let L be the line bundle of the symmetric integer matrix S=diag(1,1,-1,-1). The matrices U and S commute. On each of the two complex U-eigenplanes, S has eigenvalues1,-1. Thus δ=c1(L) is nonzero, block diagonal and primitive on both genuine RM planes, and its full signature is(2,2).

Explicitly one may take

    L=O(0) external O(0) external O(-0) external O(-0).

Elliptic cohomology and Künneth give H²(X,L)=C and all other H^j(X,L)=0. The same concentration holds for L^-1. Choose e≠0 in Ext²(O_X,L) and define the actual perfect complex F by

    L[1] → F → O_X --e--> L[2].

This is the m=1 example in the whole-audited SF-E814. Its cohomology sheaves are H^-1(F)=L and H0(F)=O_X. Put

    E=O_X direct-sum F[1].

Then

    H0(E)=O_X,   H^-1(E)=O_X,   H^-2(E)=L.

The same stable isomorphism type O_X therefore appears in two different cohomological degrees. All cohomology sheaves are stable line bundles and all unequal normalized-class differences belong to the required primitive RM space.

## Exact ordinary negative-self-Ext vanishing

The object F is ordinary gluable. One can use SF-E814, or argue directly: for a complex of cohomological amplitude[-1,0], Ext^-1(F,F)=Hom(H0(F),H^-1(F))=Hom(O_X,L)=0, and the standard cohomological structure kills all lower negative groups. The line bundle O_X is also gluable.

Applying Hom(O_X,-) to the defining triangle gives

    0 → Hom(O_X,F) → C --1↦e--> Ext²(O_X,L).

The last arrow is injective, so Hom(O_X,F)=0. The same triangle gives Ext^s(O_X,F)=0 for s<0. Applying Hom(-,O_X) gives Ext^s(F,O_X)=0 for s<0, since both Ext^s(O_X,O_X) and Ext^{s-1}(L,O_X) vanish in that range.

For every t<0, therefore,

    Ext^t(O_X,F[1])=Ext^{t+1}(O_X,F)=0,
    Ext^t(F[1],O_X)=Ext^{t-1}(F,O_X)=0.

The t=-1 instance of the first equality uses the just-proved Hom(O_X,F)=0. Decomposing the self-Ext of the actual direct sum E into its four blocks proves

    Ext^t_X(E,E)=0 for every t<0.

Thus ordinary gluability does not force disjoint stable isomorphism types, or complete same-type cross-Ext orthogonality, across arbitrary cohomological degrees. Here Hom(H0(E),H^-1(E))=C is nonzero despite Ext^-1(E,E)=0. The actual nonzero boundary e kills the putative negative morphism; no self-Ext spectral sequence was assumed to degenerate.

## Precise limit of the example

Its full character is

    ch(E)=1-ch(F)=exp(δ).

It is a pure exponential, with degree-two cap rank6, rather than the nonzero balanced RM character of cap rank18. Consequently it does not contradict a possible stronger theorem restricted to balanced objects, and it is not a proposed solution of the semiregular seed problem. It only invalidates the blanket inference from ordinary gluability to cohomology-type orthogonality when three or more cohomology degrees are present.

As another check of the distinction, SF-E814 and the same triangles give ext²(E,E)=6+12+4+4=26, whereas the sum of the self-ext² dimensions of its three cohomology sheaves is18. The exact equality proved in the globally disjoint-class extension cannot simply be applied to this repeated-type example.
