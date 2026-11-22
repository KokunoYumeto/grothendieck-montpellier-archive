# Independent full proof and source audit: C.3aw

**Result: PASS.** We read the entire typed proof in `agents/real_weil/C3_positive_characteristic_low_injectivity_draft.tex` and independently checked its geometric construction, finite-field choice rule, Chow quotient, and both restriction kernels. This audit does not claim an independent rerun of the author's finite certificate.

## Scope

For every prime p, r at least 2, and r+1 at most N at most 2r-1, the construction gives a specified normal excellent strictly henselian local ring with an algebraically closed coefficient field transcendental over the algebraic closure of the finite field. Its regular puncture and regular principal divisor puncture have a non-torsion ordinary algebraically trivial class in the kernel of restriction. The same class is a principal Gysin image and dies on the open complement. No rational nonvanishing over the algebraic closure of a finite field is asserted.

## Checks of the complete proof

1. The parameter m=N-r-1 lies between zero and r-2, exactly the interval needed for a positive-dimensional complete-intersection base. The Calabi–Yau and generic-point nonsupport input is precisely C.3at, which we independently audited in full, including the separate source- and target-support slope arguments.
2. Serre vanishing applied to the square of the ideal of the two distinct rational points supplies surjective first jets. Stacks Lemmas 33.47.1 and 33.47.3 apply to the complement of the two points and, successively, to its smooth sections. Independent jets at the marked points supply smoothness there. The smooth complete intersection has dimension at least one. Its Koszul resolution in projective space gives geometrically connectedness; smoothness and connectedness imply integrality.
3. The enumeration of coefficient tuples from finite constant extensions is valid even though the basis has coefficients in the function field. A polynomial with coefficients in an extension field that vanishes at every tuple from an infinite subfield is zero, by induction on the number of variables. Thus constant tuples are Zariski dense over the function field, and one meets the nonempty good open. The prescribed enumeration and Jacobian tests terminate without introducing another transcendental parameter.
4. The incidence divisor is smooth off the base by its projective-bundle description and is smooth on the base because the differentials of its defining sections are independent. The m=0 case is correctly included: the incidence divisor is the base itself. The fibre cycle P^m times ([P]-[a]) has codimension r-1 on that divisor, and its proper pushforward is exactly the pullback of the fixed zero-cycle, with multiplicity one.
5. The ordinary equivalence uses a smooth proper connected curve through the marked points, followed by proper pushforward and flat pullback on the product with that same curve. It is therefore an actual fixed-product family and does not rely on formal or varying families.
6. The projective-bundle quotient is exactly CH^r(T) divided by (ell H)^(m+1) CH^(r-m-1)(T). This follows by eliminating h with h=-ell H; the sole projective relation becomes (-ell H)^(m+1). That denominator lies in H CH^(r-1), so the previous nonsupport theorem proves infinite order in the integral quotient. This argument also checks the m=0 endpoint.
7. Hypersurface projective normality, the Veronese multiplication, and the Segre multiplication give degree-one generation of the full section ring. Its normality follows from the divisor-valuation description of the full section ring on a normal variety. The punctured cone is the punctured line bundle, and the principal divisor puncture is the corresponding bundle over the smooth incidence divisor. No unnecessary normality claim for the closed-point quotient is used.
8. The flat pullbacks and proper pushforwards commute before taking parameter fibres. C.3e's all-characteristic integral strict-cone injection therefore preserves the exhibited infinite-order ordinary class. Dimensions agree: the local dimension is m+r+1=N.
9. The divisor is principal, so its normal line is trivial. The exact integral Gysin definition kills each cycle supported on it, equivalently i^*i_* is multiplication by the first Chern class of the normal line. Thus the exhibited Gysin class restricts to zero on the divisor. Localization independently kills it on the open complement. Neither conclusion requires rational coefficients, although rational coefficients detect its nonzero infinite-order source class.

## Primary statements freshly opened and read

- Stacks Project, Lemma 30.17.1, Tag 0B5U, the coherent Serre-vanishing criterion: https://stacks.math.columbia.edu/tag/0B5U (opened ref `turn644823555view0`).
- Stacks Project, Section 33.47, Tag 0FD4, especially Lemmas 33.47.1 and 33.47.3 and their proofs: https://stacks.math.columbia.edu/tag/0FD4 (opened ref `turn644823555view1`).
- Stacks Project, Lemma 31.15.2, Tag 0B3P, the Cartier normal line: https://stacks.math.columbia.edu/tag/0B3P (opened ref `turn644823555view2`).
- Stacks Project, Definition 42.29.1, Tag 02T8, the Gysin rule for cycles contained in the divisor: https://stacks.math.columbia.edu/tag/02T8 (opened ref `turn644823555view3`).
- Stacks Project, Remark 42.29.6, Tag 0B6Z, its integral zero formula when the line restricts trivially: https://stacks.math.columbia.edu/tag/0B6Z (opened ref `turn644823555view4`).

The C.3at crystalline/Witt sources and proof were fully independently audited in our separate C.3at review; this audit reuses that certified antecedent and does not claim a new reread of all of its sources. No mathematical correction remains. The positive-characteristic range N at least 2r remains outside this theorem.

Actual completed audit receipt: 2026-11-19T11:25:12.660118+00:00
