# Independent audit of the strict local Picard counterexample C.3i

Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent /root/frobenius. Date: 19 November 2026.

We read research/agents/real_weil/C3_picard.tex and independently opened Kollár (2016), *Maps between local Picard groups*, full primary published PDF https://content.algebraicgeometry.nl/2016-4/2016-4-022.pdf. We checked Definition 3.3, pp. 467–468; §3.5, p. 469; and Example 4.2, particularly equations (4.2.3)–(4.2.4), p. 470.

## Actual Picard groups, not tangent spaces

The primary §3.5 explicitly identifies the rational points of the local Picard scheme over an algebraically closed field with the étale-local Picard group. For a henselian local ring, this is its actual punctured-spectrum Picard group. Example 4.2 gives the characteristic-zero exact sequence with the additive vector group \(\bigoplus_{a>0}H^1(V,M^a)\), not only its tangent space. The fragment therefore has the required algebraization input for actual line bundles. It does not improperly substitute completion for strict henselization.

## Geometry and cohomology

For \(m=N-2\ge2\), the kernel of the surjection \(\mathcal O_C^{m+1}\to K_C\) has rank \(m\), so its projective bundle of lines is smooth of dimension \(m\). The three coordinate sections of the plane quartic span \(H^0(C,K_C)\). The map
\[
H^1(W,\mathcal O_W)\longrightarrow H^1(W,L)
\]
is therefore exactly the injective contraction with image
\(\langle x_0,x_1,x_2\rangle\).
Künneth and Serre duality give \(H^1(W,L)=\mathbf C^{m+1}\), vanishing of \(H^1(W,L^a)\) for \(a\ge2\), and vanishing of all the \(H^2(W,L^a)\) used in the hyperplane exact sequence. Thus the target positive-degree vector group is \(\mathbf C^{m-2}\), and the restriction map is the indicated quotient with kernel \(\mathbf C^3\). At \(m=2\) the target vector group is zero, which is consistent.

The projective-bundle Picard formula applies because the fibres have dimension \(m-1\ge1\). It identifies \(\operatorname{Pic}(W)\to\operatorname{Pic}(H)\) as an isomorphism carrying \(L\) to \(L_H\). In the diagram of Kollár's exact sequences, the right vertical arrow is therefore an isomorphism and the left arrow is surjective with kernel \(\mathbf G_a^3\). The snake lemma gives precisely the asserted kernel and surjectivity on the middle groups. This conclusion does not actually require choosing splittings, although the projection splittings are compatible here.

## Normalization and henselization

The injection \(B/(f)\hookrightarrow B_H\) follows degree by degree from the hyperplane sequence. Its cokernel vanishes in all sufficiently large degrees, so it is finite-dimensional over \(\mathbf C\), and \(B_H\) is finite over \(B/(f)\). The map is an isomorphism on the puncture, and the full section ring is normal. Every positive-degree element above the vertex is nilpotent modulo the original positive-degree ideal, by finite graded integrality; hence there is exactly one point above the vertex, with residue field \(\mathbf C\). Finite algebras over a henselian base decompose into the henselizations at their points over the closed point. Here there is one point, so the normalization and henselization comparison used in the proof is valid. Quotient by \(f\) commutes with henselization as stated.

One explanatory clarification was sent to the owning agent. The normalized hyperplane section ring \(B_H\) need not be generated in degree one: in this example its additional sections occur in degree two. Consequently \(\operatorname{Tot}(L_H^{-1})\to\operatorname{Spec}B_H\) should be described as the proper normalized cone contraction, rather than necessarily the blow-up of the maximal ideal. It is obtained by factoring the proper contraction over the original hyperplane cone through its finite normalization. It is an isomorphism away from the zero section and has the same formal neighbourhood and normal line bundle used in Kollár's calculation. The fragment did not explicitly assert degree-one generation for \(B_H\); this clarification does not change the result.

The depth check is also correct. Normality gives depth at least two, and nonzero \(H^1(W,\mathcal O_W)\) gives nonzero degree-zero local cohomology in degree two, so the depth is exactly two. Quotient by the nonzerodivisor \(f\) lowers it to one. The example therefore does not meet the depth hypothesis of the cited local Lefschetz theorem.

## Scope of the conclusion

Every nonzero element of \((\mathbf C,+)^3\) is nontorsion, so the full Picard restriction fails to be injective after rational coefficients or removal of finite groups. The source and target punctures are regular, hence their \(\mathrm{CH}^1\) groups agree with their Picard groups.

Definition 3.3 permits an étale neighbourhood of the product with a parameter scheme that varies with that parameter. Ordinary algebraic equivalence of cycles on a fixed punctured scheme does not automatically allow this variation. Thus the fragment correctly distinguishes the identity component of the local Picard scheme from \(\mathrm{CH}^1_{\mathrm{alg}}\), and does not claim to refute the latter's restriction map without a further argument.
