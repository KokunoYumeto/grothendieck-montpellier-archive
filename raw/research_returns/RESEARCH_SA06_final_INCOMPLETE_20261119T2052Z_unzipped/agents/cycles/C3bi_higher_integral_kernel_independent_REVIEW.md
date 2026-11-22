# Independent audit of C.3bi

Completed 2026-11-19 14:34:54 UTC by `/root/cycles` (GPT-6 Astra Pro, RESEARCH_SA06). This is an independent agent proof and source check, not an independent-model verification.

**Verdict: PASS** for the complete current text `../real_weil/C3_higher_integral_kernel_draft.tex`, including the explicit finite-field incidence pair and the actual fifth-power vanishing. The result is an integral ordinary codimension-two restriction kernel of exact order five in local dimension five. No rational conclusion or uniform extension is certified here.

## 1. Geometry and the divisor cup

I rederived the rank-two map on the smooth Fermat cubic surface in characteristic five. Along the specified line, the normal map is `(3s^2,3t^2)`. The connecting functional on binary quadratics kills `s^2,t^2` and is nonzero on `st`; the twisted Euler and normal sequences identify the desired cup with this functional on the product of the two restricted linear sections. The cohomology used to make the final boundary an isomorphism follows from the negative ample degrees and the displayed Euler characteristic. This is an integral characteristic-five calculation, without a hidden factorial.

For the explicit pair over F125, I checked the two independent rows at every point of the quartic, the kernel parametrization, the restricted equation `A0 sigma^3+B0 theta^3`, the twelve simple zeros of each coefficient, and their disjointness. The exclusions `lambda^12 notin {1,3,4}` cover exactly the exceptional cases in those branch calculations. The derivative in the fibre direction handles the complement of the branch divisors, while the nonzero derivative on the curve handles each branch point. Thus the complete intersection is smooth and the incidence hypersurface is its smooth blow-up. The rank-three coefficient minor and rank-two restricted cup are both correct.

The contracted neighbourhood has the asserted unique exceptional fibre, regular resolution and puncture, and the principal equation is exactly `tau ell`. The target strict transform is the split line neighbourhood of the smooth incidence divisor. The pullback of the cubic line is an actual line bundle on the source resolution.

## 2. Actual ordinary line classes

I checked all cohomological vanishings in the product P1 times cubic surface times quartic. The extension class has image `U=ell H^1(O_V)` of dimension three. The ordinary quartic, the Verschiebung lift and the Hom--Ext calculation imply that the finite kernel maps into this vector group with linear span U. A nonzero cup on U therefore detects at least one actual finite-kernel point.

The Poincare bundle is pulled to a proper connected curve in the domain of Verschiebung. Its first obstruction vanishes, and the difference from the prescribed extension map is a constant map to a vector group, removed by normalizing at zero. All higher product obstruction groups vanish. The already audited formal existence, finite-data Popescu descent, henselian lift with prescribed first jet, and punctured Picard comparison give an actual fixed-product ordinary family. I reread the revised endpoint paragraph: it proves actual target triviality and actual fifth-power triviality, not merely first-jet statements.

## 3. Relative-to-absolute K-theory

The curve localization sequence really implies divisibility of K1(C): its two relevant subquotients are quotients of direct sums of `k*` and a copy of `k*`. The projective and blow-up formulas then give `K1(V)=K1(C)^18`. Geisser--Hesselholt's bounded p-primary theorem applies on every affine in a finite cover, and the finite Mayer--Vietoris argument gives a bounded exponent for global relative K0. Thus the boundary from the five-divisible K1(V) is zero, and relative K0 injects into absolute K0. This essential step is present and valid.

For the nonsplit first neighbourhood, local smooth splittings and the rank-one dual-number calculation identify relative K2 with `L tensor Omega^1`. Two choices of splitting differ by a symbol with both entries infinitesimal, which is zero when 2 is invertible; hence the identification is canonical globally. The chosen sign is explicitly tracked. Perfectness of the characteristic-five field removes the absolute field differentials here.

The relative descent sequence has a finite cohomological filtration, because its underlying space is four-dimensional. At the relevant `(2,-2)` term the sole possible incoming differential comes from global relative units; every such unit is actual, so that differential vanishes. The product of the two actual line classes is permanent and has the stated nonzero cup as its associated-graded term. The tensor-product pairing is the required relative module pairing. I checked that no unsupported general relative Adams operation is invoked: only absolute Adams operations on actual line bundles, followed by their unique relative lifts, are used.

## 4. Chow localization and Adams separation

If the punctured Chow class vanished, the regular-pair localization sequence would express it as an exceptional pushforward from Pic(V). Its refined restriction gives `L gamma=0`. The P1 coefficient computation proves injectivity of this multiplication integrally, including any torsion in Pic0(C), since the final integer coefficient is killed only by a strictly positive ample degree. Therefore the Chow class would vanish already on the resolution.

The absolute coniveau filtration then puts the K-class in F3. On the five-dimensional regular scheme, the polynomial `(T-8)(T-16)(T-32)` annihilates F3 by its successive graded Adams eigenvalues. Its value at four is -1344, congruent to one modulo five. Pullback to the first neighbourhood contradicts the nonzero relative associated-graded class. The class is therefore nonzero and, by the actual Picard endpoint argument, has exact order five. Intersecting the actual family with the fixed cubic divisor proves ordinary algebraic triviality.

## 5. Primary sources freshly checked

- Iwasa--Kai, published Cambridge PDF: Proposition 3.4, printed pp.1957--1958; Definition 3.9 and Lemma 3.10 with proof, p.1960; Theorem 4.2, pp.1961--1962. I checked that the argument uses their absolute coniveau statements. The affine-neighbourhood hypothesis in their relative Chow-with-modulus theorem is not silently discarded.
  <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/42DCFAFEE9CAE2011E983ABFADA02766/S1474748020000055a.pdf/isomorphisms-up-to-bounded-torsion-between-relative-dollark0dollar-groups-and-chow-groups-with-modulus.pdf>
- Khan, author version dated 1 February 2020, Corollary 3.6, p.12, and Corollary 4.4, p.16: spectrum-level projective-bundle and regular-blow-up decompositions.
  <https://www.preschema.com/papers/kblow.pdf>
- Geisser--Hesselholt, Theorem A, published p.29: bounded p-primary relative K-groups for every integer degree under a nilpotent extension with p nilpotent.
  <https://math.mit.edu/~larsh/papers/025/bounded.pdf>
- Van der Kallen, original p.A1204, unnumbered theorem and its 1/2 corollary, visually read from the local rendered primary scan. The rest of the original proof was previously audited in the project; no fresh complete reread of A1205--A1207 is claimed here.
  <https://webspace.science.uu.nl/~kalle101/K2nd1971.pdf>
- Weibel, Chapter III, Exercise 5.14, pp.46--47, for the Dennis--Stein normalization and both-infinitesimal kernel.
  <https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf>
- Thomason--Trobaugh, Theorem 8.1 and proof, p.367; Theorem 10.3 and proof, pp.383--386; Section 3.15, pp.318--319. I freshly read the finite-dimensional hypotheses, strong descent, preservation of fibres, and the tensor pairings. Taking the fibre of the two descent equivalences gives the relative sequence used here.
  <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Thomason-Trobaugh.pdf>

The already certified C.3bf/bg actual Picard-family construction and their Illusie/Brion/Elkik inputs were reused with the newly verified product cohomology. This audit does not claim to have freshly reopened every earlier source.

## 6. Finite certificate inspection

I read the complete program `../frobenius/code/check_cubic_incidence_geometry.py` and every entry of `../frobenius/output/C3bi_cubic_incidence_geometry.json`. All sixteen exact checks agree with the independent geometric proof above. The recorded author run began at 14:26:08.725769 UTC and took 0.19333759199798806 seconds. I did not rerun that program. Its scope is finite identities supporting the all-geometric-point proof, not a machine proof of the higher Chow theorem.

The local primary scan render retained for this audit is `output/C3bi_vdk_p1.png`, with its actual render metadata in `output/C3bi_vdk_p1_render.json` (1.722185189006268 seconds). No calculation runtime has been recycled as a new run.

## 7. Separate follow-up

The parent has requested a possible direct H1(K2)-divisibility argument to remove the Adams restrictions. That is a new, unproved follow-up and is not needed for this PASS. In particular, the K1(V) decomposition used above does not by itself establish a decomposition of H1(V,K2).
