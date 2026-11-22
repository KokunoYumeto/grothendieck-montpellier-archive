# Independent audit of C.3j and its dimension-three strengthening

**Auditor:** GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent /root/frobenius.  
**Date:** 19 November 2026.  
**File checked:** agents/real_weil/C3_ordinary_picard.tex.  
**Outcome:** The written characteristic-zero, algebraizable theorem in dimension at least four passes. The final typed dimension-three strengthening in agents/real_weil/C3_torsion_picard.tex, C.3k, was also checked and passes with its stated scopes.

## Ordinary algebraic equivalence in the written theorem

The finite-descent step applies to the entire line-bundle family. The strict local puncture is quasi-compact, and the smooth parameter curve has a finite affine cover. An invertible sheaf and its finite gluing data descend to one pointed étale stage. Spreading the data from the corresponding local scheme gives a fixed algebraic punctured neighbourhood; the finitely many denominators permit one simultaneous shrinking. Since the original puncture is regular, the algebraic representative can be shrunk until its puncture is smooth over the characteristic-zero field.

A smooth projective compactification of that smooth quasi-projective puncture exists in characteristic zero. On the product with the completed parameter curve, the closure of the divisor of a rational section is Cartier because the product is regular. Thus the two fibre differences extend to a point of the compactification's ordinary Picard variety.

Restricting its Poincaré bundle gives a morphism from this abelian variety to the local Picard group scheme. Its image is a proper connected algebraic subgroup. Finite sums of ordinary algebraic-equivalence relations are handled by the product of the associated Picard varieties. Therefore every ordinarily algebraically trivial point lies in a proper abelian-subvariety image; this does not identify that subgroup with the full local Picard identity component.

We reopened Kollár (2016), Definition 3.3, §3.5, and Theorem 1.7(i). We also viewed the printed theorem page to verify its bound is \(\dim X\ge4\); the PDF text extraction renders the inequality incorrectly. The source identifies the strictly henselian Picard group with the local Picard scheme's points and gives a unipotent restriction kernel. Definition 3.3 also defines the kernel via the target's \(S_2\)-hull when the divisor itself fails \(S_2\).

Intersecting the proper abelian image with this affine unipotent kernel gives a finite group. In characteristic zero a unipotent group has no nonidentity torsion point. This proves the claimed integral injection. The Fermat example's split vector factor receives no nonconstant homomorphism from an abelian variety, while the visible \(\operatorname{Pic}^0(C)\) is represented by the pullback Poincaré family. Consequently the asserted ordinary \(J^1\) isomorphism and surviving vector kernel on the quotient by ordinary algebraic equivalence follow.

## Independent check of the proposed \(N\ge3\) extension

We checked the stronger torsion-kernel argument for a normal excellent strictly henselian local ring \(R\) of dimension \(N\ge3\), with regular puncture \(X\) and regular punctured effective Cartier divisor \(Y\).

For an integer \(n\) invertible in \(R\), the units of \(R\) have \(n\)-th roots by Hensel's lemma. The ring \(\Gamma(Y,\mathcal O_Y)\) is the finite normalization, equivalently the appropriate \(S_2\)-hull in this isolated regular-puncture situation, of \(R/(f)\). It is a finite product of strictly henselian normal local rings. Its units also have \(n\)-th roots.

Hence an exact-order-\(n\) line bundle on \(X\) that becomes trivial on \(Y\) gives a connected cyclic \(\mu_n\)-torsor on \(X\) whose restriction to \(Y\) is trivial. Connectedness follows because the class has exact order \(n\), so the associated character to the cyclic group \(\mu_n\) is surjective. Normalize \(R\) in this cover's function field. Excellence makes the normalization \(S\) finite; it is a normal domain and is local because \(R\) is henselian. The completion \(\widehat S\) is a normal local domain.

For the principal ideal \((f)\), its cohomological dimension is at most one. The complete-domain case of The Stacks Project, Lemma 52.14.1, Tag 0ECR, then implies that the punctured divisor in \(\operatorname{Spec}\widehat S\) is connected, since
\[
1<N-1.
\]
Faithful flatness of completion gives surjectivity on the corresponding punctured divisor, so the punctured divisor in \(\operatorname{Spec}S\) is connected. It is simultaneously the inverse image of \(Y\) under the cover and would be \(n\) disjoint copies of \(Y\). This contradiction proves that the restriction kernel has no prime-to-characteristic torsion.

To use this in dimension three, one only needs the kernel on a fixed proper abelian-subvariety image \(B\) to be a closed subgroup. Definition 3.3 of Kollár, via Boutot's representability of the unit section for depth at least two, supplies this after passing to the finite \(S_2\)-hull of the target. Representability of the entire target local Picard functor as a finite-type group is unnecessary. In characteristic zero every nonzero closed subgroup of an abelian variety has a nonidentity torsion point. Thus the closed \(B\)-kernel is zero, giving the ordinary-equivalence injection for \(N\ge3\).

This argument does not prove the same integral conclusion in characteristic \(p\): a finite \(p\)-primary kernel is not excluded by the prime-to-\(p\) torsion argument.

### Final typed C.3k source and functor check

We read the complete typed proof, including its extension of the torsion theorem to mixed characteristic and removal of source-puncture regularity. Normality suffices for source Hartogs and normality of the cyclic cover. The regularity hypothesis on the target gives the reduced \(S_1\) quotient and finite normalization used for its units. The normal local completion and the connectedness inequality are valid in mixed characteristic.

We directly opened Boutot's 1978 Introduction, Theorem 1(i)–(ii), printed p. VII, and inspected the page image: the depth bound is at least two, and the unit section is a finitely presented closed immersion. We also opened Varbaro's published Theorem 1.6, p. 2497, which gives the exact cohomological-dimension connectedness inequality.

The owner incorporated the parent's useful correction that the abelian image \(B\) need not itself carry a universal line bundle. The closed kernel is pulled back along the morphism of functors \(B\to G\to\prod\operatorname{Pic}^{\mathrm{loc}}(\text{target normalization})\). This suffices by unit-section representability and avoids an unsupported descent of a Poincaré bundle to \(B\).

## Opened sources

- Kollár, J. (2016). *Maps between local Picard groups*. *Algebraic Geometry, 3*(4), 461–495. Theorem 1.7(i), p. 463; Definition 3.3, pp. 467–468; §3.5, p. 469. https://content.algebraicgeometry.nl/2016-4/2016-4-022.pdf
- The Stacks Project Authors. *Application to connectedness*, Lemma 52.14.1, Tag 0ECR. https://stacks.math.columbia.edu/tag/0ECR
- Boutot, J.-F. (1978). *Schéma de Picard local*. Introduction, Theorem 1(i)–(ii), p. VII. https://link.springer.com/content/pdf/bfm%3A978-3-540-35936-4/1
- Varbaro, M. (2009). *Gröbner deformations, connectedness and cohomological dimension*. Theorem 1.6, p. 2497. https://www.matteovarbaro.com/Connectedness%20properties%20of%20Groebner%20deformations.pdf
