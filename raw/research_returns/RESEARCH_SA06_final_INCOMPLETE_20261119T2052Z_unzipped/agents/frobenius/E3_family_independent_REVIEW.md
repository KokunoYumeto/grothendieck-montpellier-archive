# Independent audit of E.3m–n

**Auditor:** GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent /root/frobenius.  
**Date:** 19 November 2026.  
**Files checked:** agents/cycles/family_converse_reduction.tex and agents/cycles/family_countability.tex.  
**Outcome:** E.3m passes. E.3n passes after the moving-lemma notation was corrected; we also read the replacement Hilbert-scheme paragraph.

## E.3m: the exact Walker quotient

We checked the proof without assuming that its abstract quotient \(E\) carries a universal integral family. The original family on \(B\), its quotient by the connected kernel of the Walker map, and then its quotient by a finite subgroup are algebraic maps. Only the resulting injection \(E(\mathbb C)\to P\) initially remains an abstract homomorphism.

On enlarging the family from \(B\) to \(B\times A\), the map \(B\to E'\) remains algebraic. Its kernel contains the kernel of \(B\to E\) because both maps into \(P\) agree and \(E'(\mathbb C)\to P\) is injective. In characteristic zero these are reduced subgroup schemes, so the equality on complex points supplies the scheme-theoretic kernel containment needed for quotient descent. Hence \(E\to E'\) is algebraic. Its pointwise injectivity and equal dimensions make it an isomorphism. The enlargement argument therefore shows that a single image contains every abelian-family image.

The finite-family covering of the Walker Jacobian is also valid: each family has an abelian-subvariety image, finite sums remain abelian subvarieties, and strict enlargements increase dimension. Surjectivity of the Walker map together with the integral abelian parameterization of E.3g forces the terminal sum to be the whole Jacobian.

It follows that \(\ker(P\to J_W)\) is finite. It is a quotient of the divisible group \(\ker\psi_W\), so it is divisible and hence zero. We reopened Achter, Casalaina-Martin, and Vial (2022), Theorem 2.3, author manuscript p. 12, which is exactly the divisibility assertion required. No universality statement for arbitrary regular homomorphisms is substituted for this assertion.

The optional direct regularity argument also passes. If the integral map \(v:\operatorname{Alb}(T)(\mathbb C)\to E(\mathbb C)\) satisfies \(mv=f\) with \(f\) algebraic, then \(f\) kills the finite group scheme \(\operatorname{Alb}(T)[m]\). Thus \(f=g\circ[m]\) algebraically. The difference \(v-g\) has finite image and divisible source, so vanishes. Smooth projective compactification and closure of the cycle then handle quasi-projective parameter varieties; local constructions agree as morphisms because the target is separated.

## E.3n: countability with integral Albanese relations

### Correction identified and implemented

The original text asserted a map
\[
\mathrm{CH}_0(T^\circ)\longrightarrow\mathrm{CH}_0(T)
\]
for an open immersion. Such a pushforward is not defined in general. For example \(\mathrm{CH}_0(\mathbb A^1)=0\) while \(\mathrm{CH}_0(\mathbb P^1)=\mathbb Z\).

The needed statement is instead that every class in \(\mathrm{CH}_0(T)\) has a representative supported in \(T^\circ\), equivalently that \(Z_0(T^\circ)\to\mathrm{CH}_0(T)\) is surjective. The given curve-and-Riemann–Roch proof proves this integral representative statement. The cycles agent corrected the notation before this audit was closed.

### Parameter spaces

We checked that each operation uses finite discrete choices, indexed by countably many integers or Hilbert polynomials. Parameter varieties \(T\) can be embedded in projective spaces of varying dimensions; their smooth geometrically connected loci are obtained on finite-type strata. A marked point supplies a section.

The relative Albanese input was reopened in Javanpeykar and Mathur (2022), Theorem 2.2 and its following paragraph. It gives arbitrary-base-change compatibility for smooth proper characteristic-zero families, with the marked section turning the torsor into the pointed group scheme. Consequently the weighted Albanese-zero condition is an actual closed condition.

For correspondence cycles, the restriction to points of a common fibre-flat open is legitimate after the moving step. Vertical components act trivially because the zero-cycle can be represented away from their images. Relative Hilbert schemes parameterize the remaining flat families; fibre-flat loci are constructible, and finite stratification supplies cycle maps into fixed Chow schemes. These conditions retain integer multiplicities and do not replace the Albanese kernel by its saturation.

### Rational-equivalence witnesses

We read the revised argument using integral subschemes of \(\mathbb P^1\times X\), rather than a universal cycle over a Chow scheme. An integral subscheme dominating \(\mathbb P^1\) is flat over that regular curve. Its two fibre cycles differ by a rational equivalence. Conversely, closing the graph of a rational function produces precisely such a witness, with integral multiplicities. The Stacks Project, Lemma 43.9.1, Tag 0AZI, was opened and gives this exact equivalence, including the norm for generically finite projection to the cycle's support.

All finite signed sums of witnesses are parameterized by products of Hilbert schemes; endpoint equality is imposed in a fixed Chow scheme. Chevalley's theorem then gives countably many constructible image sets. We also reopened Schoen (1993), Lemma 4.4 and its proof, pp. 311–313, and checked its Hilbert–Chow witness construction. The additional relative Albanese-zero condition is supplied by this new proof, not attributed to Schoen.

### Uniform exponent and conclusion

The countably constructible sets for all positive exponents cover a nonempty open of the abelian variety if every family value is torsion. Baire gives a dense constructible member and thus a nonempty Zariski open \(V\) on which one fixed exponent kills the map. The kernel is a subgroup and \(V-V=A(\mathbb C)\), since any two translates of a nonempty open meet in an irreducible variety. Hence the same exponent kills the whole homomorphism. Divisibility of \(A(\mathbb C)\) then makes that homomorphism zero.

No uniform exponent is assumed in advance. The proof is integral and specific to the stated complex setting. Its final combination with E.3c and E.3m is an equivalence of remaining gates, not a proof that those gates always hold.

## Opened primary sources

- Achter, J. D., Casalaina-Martin, S., & Vial, C. (2022). *The Walker Abel–Jacobi map descends*. Theorem 2.3, author p. 12. https://www.math.uni-bielefeld.de/~vial/WalkerAJmap.pdf
- Javanpeykar, A., & Mathur, S. (2022). *Smooth hypersurfaces in abelian varieties over arithmetic rings*. Theorem 2.2 and following paragraph. https://doi.org/10.1017/fms.2022.87
- Schoen, C. (1993). *On Hodge structures and non-representability of Chow groups*. Lemma 4.4, pp. 311–313. https://www.numdam.org/item/CM_1993__88_3_285_0.pdf
- The Stacks Project Authors. *Rational equivalence*, Lemma 43.9.1, Tag 0AZI. https://stacks.math.columbia.edu/tag/0AZI
