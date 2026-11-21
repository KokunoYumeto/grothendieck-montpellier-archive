# Clearing the proper-pair denominators of the actual cubic system

Author: `/root/tripod_integral`, GPT-6 Astra Pro. 21 November2026.

This is a supplementary algebraic lemma for `cubic_uppertriangular_bridge.md`. It does not prove Triple-NV or a cohomology-localization theorem.

## Statement and proof

Use that note's notation, and let

\[
A=\mathcal O[[T_1,T_2]],\quad z_1=1+T_1,\quad z_2=1+T_2,
\quad z_3=\alpha/(z_1z_2),\quad K=\operatorname{Frac}(A[1/p]).
\]

The substitution is integral and continuous for the maximal-ideal topologies because alpha lies in 1+m_O. Let q be an integral polynomial annihilating the even torsion module, and put

\[
d_{12}=q(z_1z_2),\qquad d_{23}=q(z_2z_3)=q(\alpha/z_1).
\]

Both belong to A and are nonzero: their arguments are nonconstant, and substitution into either corresponding one-variable power-series ring is injective. They need not be units in A, but they are units in K.

Replace the three linear functions by

\[
\widetilde f_1=d_{12}f_1,\qquad
\widetilde f_2=f_2,\qquad
\widetilde f_3=d_{23}f_3.
\]

Uniqueness of the equivariant pair extensions then gives

\[
\widetilde b_{12}(y)=d_{12}b_{12}(y)=n_{12}(q(D)y),\qquad
\widetilde b_{23}(y)=d_{23}b_{23}(y)=n_{23}(q(D)y).
\]

Consequently

\[
\widetilde\psi=d_{12}d_{23}\psi.
\]

This also follows directly from the literal commutator formula. It is a compatible diagonal rescaling of the strictly upper triangular matrix coordinates: its factors on the first, second and third positions are d12,1,d23, and its factor on the central coordinate is d12*d23. In particular all Lie identities and Gamma/Delta equivariance are preserved. On the root field K, the cubic extension is zero before this operation if and only if it is zero after it.

There are no proper-pair denominators left in the rescaled pair maps. The input modules have actual compact lattices, and the rational rank-one coordinate changes have one bounded p-denominator. The completed bilinear maps are bounded on the tensor products of those lattices. The finite torsion bases add only finitely many bounds. Thus a common power p^N, applied to each first coordinate, makes the first coordinates and the rescaled second coordinates integral: the latter acquire p^(2N). The central functional acquires p^(3N). Increasing N if necessary absorbs the finitely many denominators in the class-three exponential and BCH polynomials as well.

It follows that the specified partial matrix system, and the tested central relation after this scaling, can be represented over the compact complete Noetherian coefficient ring A. The continuous maps into A use its maximal-ideal topology. This construction is performed before any claim about commuting cohomology with K. The nonzero factors removed in K are explicit, so none changes the generic nonvanishing test.

## Exact relationship to the checked Bockstein source

LLSWW Definitions3.3.1–3.3.2 and Theorem4.1.2 fix homomorphisms to unipotent groups over a coefficient ring and take their outside first-diagonal coordinates in H1(G,R), with trivial R action. In our arithmetic group H semidirect Gamma, the three coordinates have distinct universal Gamma characters gamma->z_i, and their Delta characters are also prescribed. They are naturally entries of a **twisted Borel cocycle**, not all untwisted homomorphisms on that larger group.

The general definitions already cover this situation: LLSWW Definitions3.1.3,3.2.1 and3.2.2 allow a separate compatible G-action on every matrix-entry module. The specialization to at most one nontrivial first-diagonal module is imposed only after Definition3.2.2. Thus no new notion of a Massey defining system is needed. One can repeat the explicit matrix/cochain proof with the three rank-one coefficient characters, but the published specialized Bockstein theorem should not be invoked verbatim. Alternatively one may use an external-Gamma Hochschild–Serre comparison, with its topological hypotheses supplied. Restricting to H alone does not resolve the issue: H is free, and the obstruction of interest measures compatibility with Gamma.

For a group realization, use exp of the specified Lie map modulo the center. In particular the (1,3) group coordinate is the Lie (1,3) coordinate plus one half the product of the first two coordinates; the (2,4) coordinate has the analogous correction. The finite p-power scaling above handles these denominators at every odd p. The central cochain must be formed from these actual group coordinates, rather than silently treating Lie coordinates as group cochains.

No arithmetic image-support statement follows from this compact realization. Its purpose is to remove a topology and denominator ambiguity from the comparison that an arithmetic theorem would need to detect.
