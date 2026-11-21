# Independent whole-proof review: THETA3-C33

**Reviewer:** GPT-6 Astra Pro, agent `/root/definite_bridge`; reasoning effort inherited/not exposed. **Date:** 21 November 2026. **Result:** PASS at the exact labelled horizontal scope.

I read the entire final `paper_C33.tex`, including the characteristic-zero Artinian deformation argument and the revised boundary-only Chow conclusion.

## Primary sources actually read

- Lan, corrected author revision of *Arithmetic compactifications of PEL-type Shimura varieties*: Section 4.1 (printed p207), the full statement of Theorem 4.4.16, Construction 4.5.4.27 and the complete proof of Lemma 4.5.4.28 (pp299–300), and Corollary 4.5.5.5 with its complete proof (p303). The last page was also inspected visually in `Lan_C31_Cor4555_330.png`. Its statement treats arbitrary generic homomorphisms, not only polarized isomorphisms.
- Lan, corrected *Toroidal compactifications of PEL-type Kuga families*: Theorem 1.8 (p7) and Theorem 1.41 through clause (5) (pp16–17), identifying the actual formal universal family with the Mumford family.
- Complete Stacks statements and proofs at tags 0AH2, 0C21, 0C22, 032Y, 04HH and 0ALI. These justify the completion/normalization and local labelled-immersion steps at the stated noetherian excellent scope.

## Mathematical reconstruction

1. The good source has degeneration datum `[0 -> B]`. A map to `[Y -> G^natural]` has no nonzero source-lattice component. Its extension obstruction is exactly the pullback torus-extension class, namely `h^dual c`. Splitting is unique because an abelian scheme has no nontrivial group homomorphism to a torus. The dual period equation gives that same condition.
2. Fully faithful degeneration and polarization compatibility identify the actual generic norm with the abelian-part product. The three columns therefore give norms `a*bar(a)+2`, `a*bar(a)+1` and `2`, without a hidden boundary-isogeny multiplier.
3. For characteristic-zero local Artinian deformation rings, `e=f t^{-1} f^dagger` is a self-adjoint quasi-endomorphism idempotent. Clearing denominators splits the target up to isogeny into the fixed source image and its complementary PEL factor. The torsion kernel, action, isotropy and level structures are finite etale and lift uniquely. Thus the labelled deformation functor is the smooth complementary PEL functor; rigidity is used only for the local closed immersion. This addresses nilpotents in the actual scheme structure.
4. The graph is smooth and independent of the toroidal coordinates, so its ideal is saturated by both p and the q parameters. Its normal completed local rings construct the generic homomorphism by Lan. Conversely the horizontal closure is reduced, remains reduced on completion, and has finite normalization. Every normalized component has the prescribed abelian-part label by rigidity and must satisfy `h^dual c=0`. This proves equality of the actual horizontal closed formal subschemes.
5. Each q parameter is a nonzero divisor on the closure, so refined pullback to the boundary gives exactly the labelled graph. The proper contraction is then on the boundary abelian parameter scheme B^3. No projection from the whole toroidal chart is assumed proper.

The claim remains confined to the specified good-prime labelled horizontal closures. It does not calculate vertical derived intersection multiplicities or produce an interior map from the original compact ball to the larger PEL model.
