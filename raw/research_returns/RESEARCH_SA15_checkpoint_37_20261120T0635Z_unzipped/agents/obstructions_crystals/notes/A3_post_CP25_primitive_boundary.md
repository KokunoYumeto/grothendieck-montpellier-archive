# Primitive boundary investigation after CP25 preparation

Recorded UTC: 2026-11-19T21:27:30.627759+00:00

The promoted residual-pencil bridge is an exact reformulation only. The actual missing assertion remains nonzero restricted cup common radical (equivalently a variation image of dimension at least two) at a suitable sharp source. The following are research calculations, not promoted results.

## Actual crossed syzygy and an AP connecting map

For V=E0, E1=VP, P^2=O and sections s0,s1, the actual determinant direction kernel is K tensor P. The map End^0(V) -> K tensor P given by X -> (X s0,X s1) is well typed and lies in the crossed kernel because the first derivative of a two-by-two determinant under X is tr(X) times that determinant.

On a chart s0=(1,0),s1=(h,w)e, a trace-zero matrix [[a,b],[c,a]] maps to the three free kernel coordinates (a,c,h a+w b). Thus it is injective and its cokernel is a line on D=(w), even when D is nonreduced. Globally, the rank-one map O_D direct-sum P_D -> V_D has image R0 and kernel P R0^{-1}. The residual cokernel is Hom(P R0^{-1},R0)=A P, where A=R0^2. This suggests the exact sequence

0 -> End^0(V) -> K tensor P -> i_*(A P) -> 0.

It provides a new description of the actual Delta annihilator but does not prove its dimension. In particular, even if primitive local index zero makes V simple, an extra section of A P may have nonzero image in H1(End^0 V); it need not lift to an extra global endomorphism. Monodromy independently flagged exactly this obstruction. No simplicity-to-pencil-exclusion inference is made.

On an integral D with h0(A)=2, one can at least infer h0(R0)=h0(R0 P)=1: two independent sections of either half-degree line would give three independent symmetric products in A. The product of the two unique sections supplies one section of A P. No upper bound h0(A P)=1 has been established.

## Possible homogeneous structure of the acyclic rank-two bundle

In characteristic two the representation identity End^0(V)/O = F_abs^* V tensor det(V)^{-1} is exact. For V=nu_*J and the alpha2 torsor nu:C->T, nu^*nu_*J has a two-step filtration with both quotients J. Absolute Frobenius of T factors through nu via the semilinear complementary map, and the pullback of J along that map should identify with Nm_nu J=det(V). This suggests that g=(End^0V/O)P is an extension of P by P. This factorization and its extension class must be checked globally before use.

Even an explicit extension description of g would not by itself establish nonvanishing: the residual symmetric-square boundary depends on the relative position of the three-dimensional residual-pencil product space and the image of H0(Sym^2 g^dual), as well as the subsequent actual Delta restriction. Acyclicity of g does not dispose of the cohomology of Sym^2 g.

## Excluded shortcuts

The same-weight Koszul complex twisted by L has middle O^2 direct-sum End(V)P; the actual crossed determinant complex is twisted by LP and instead has P^2 direct-sum End(V). The acyclicity of End(V)P therefore cannot be transferred to the actual direction complex.

Scaling either section gives square-weight changes in the relevant matrix coordinates in characteristic two. Such group-orbit dimensions do not prove a lower bound for the differential.

No new generic-rank theorem, extra pencil exclusion, uniform h0(KP) bound, or claimed review movement results from these calculations.

## Typed complementary-map calculation, post-CP26 setup

Recorded 2026-11-19T22:06:01.319500+00:00. The complete isolated proof is post_CP26_unipotent_bundle_candidate.tex. The actual complementary map is nu^c:T→C^(2), with nu^c nu=F_C and nu^(2)nu^c=F_T; its kernel is mu2. Pullback of the transition derivative kappa=b/(a+bz) after Frobenius twist is gamma=b²/(a²+b²h). Its cohomological pullback is an isomorphism because the dual kernel is etale. The local-local polarization block therefore makes gamma nonzero exactly when the actual local index is zero; a positive actual local index makes the extension split. Even exponents can change which case applies. This candidate remains unaudited and supplies no restricted-cup nonvanishing.

The local17-identity checker passed at22:05:41 UTC in0.0684365240012994 seconds. Its symmetric-square splitting identity is conditional on gamma² being a coboundary; it does not prove that global assertion. Initial executed code is retained with its output; one comment was subsequently narrowed to the symmetric-square calculation actually present.
