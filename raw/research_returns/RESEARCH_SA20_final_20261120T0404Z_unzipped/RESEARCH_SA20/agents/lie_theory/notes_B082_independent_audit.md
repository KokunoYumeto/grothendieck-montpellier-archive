# Independent audit of B.082

Agent /root/lie_theory; actual clock 2026-11-19 18:17:33 UTC.
Read the complete draft at agents/tensor_and_finite/notes/pending_B082.tex.

## Outcome

PASS. The criterion is valid without a flatness assumption. The audit is of the written proof, including the direct chain calculations, not merely of the expected spectral-sequence pattern.

## Checked details

1. In the matrix-epimorphism converse, a finite presentation of c tensor 1 minus 1 tensor c gives the displayed matrix relations. Removing row and column zero leaves both Y'M' and M'Z' over R and gives Y'M'Z' = m00 minus c. The final block construction therefore produces c. Repeated element labels may be taken in a finite free presentation; the case c = 1 is already immediate.

2. Since E is a quotient of (C/R)[X], epicness gives C tensor E = 0, hence F tensor E = E tensor F = E tensor E = 0. No use of tensor injectivity occurs here.

3. The functorial free resolutions are well defined: a module map acts on the free module on its underlying set, preserves the augmentation kernel, and continues recursively. A generator of each kernel is a finite relation. The fixed construction does not require a basis of any kernel.

4. The transgression signs agree with the total differential. For degree q the lift satisfies dw = (-1)^(q+1) h0 z and the obstruction is (-1)^(q+1) h1 w. Changing a cycle representative by dv changes w by (-1)^(q+1) h0 v and leaves h1 w unchanged. Changing a lift by a cycle changes the class by the image of b_(q+1). This proves the claimed canonical maps for the fixed resolution and their linearity.

5. The two-column complex L has homology A in degree zero and zero elsewhere because F to E is surjective with kernel A. Its degree-minus-one term is free, so the surjection onto that term splits. Removing this contractible summand leaves a nonnegative projective resolution. Tensor products of the contractible summands are contractible without any flatness assumption.

6. The sign (-1)^(p1 b) in the map from L tensor L to the three-column total complex is correct for all four differential types. The first vertical differential is unchanged; the second vertical sign becomes (-1)^a; the first horizontal sign becomes (-1)^(a+b); the second becomes (-1)^(a+b-p1), which is exactly the minus sign on Q tensor P to Q tensor Q. This verifies the chain isomorphism directly.

7. The edge map is the map induced by the inclusion A into F in each factor. Thus it is the actual polynomial coefficient tensor map theta2, rather than an unrelated isomorphism of its source.

8. The degree-zero cycle equations yield image(theta2) = kernel(delta0). Any pure column-two vertical degree-one cycle is a total degree-minus-one cycle, and H_-1 = 0 supplies its preimage. The signs then give delta0[x0] = [y], proving surjectivity and coker(theta2) = T1.

9. Killing a zero-edge column-zero component gives the canonical map from ker(theta2) onto K1. Killing its K1 class leaves a pure column-two vertical degree-two cycle. Such a cycle is a boundary exactly when it is, modulo a vertical boundary, h1 w with dz = 0 and dw = h0 z. These are precisely the delta1 relations, together with the image of b2 from changing w by a cycle. Consequently the kernel is exactly K2 and the claimed short exact sequence follows.

10. The final coefficient arrays are the binomial expansion of F(X+Y) and the diagonal expansion of F(XY). The image and kernel calculations therefore give both existence and uniqueness. The construction is independent of any prior computation of a tensor power of Omega. It is an infinite arithmetic criterion for arbitrary rings, not a claim of a terminating algorithm.

No mathematical correction requested. The special examples are separate consistency checks and were not needed for this proof audit.
