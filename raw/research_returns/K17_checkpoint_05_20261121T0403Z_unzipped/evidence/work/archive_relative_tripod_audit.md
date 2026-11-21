# Independent audit: relative cusp normalizer and Chern extension

Researcher: `/root/tripod_integral`, GPT-6 Astra Pro, 21 November 2026. Effort not exposed. This records a whole-proof audit of `work/archive_relative_section.tex`, theorem **F149-RELATIVE**, and its cited local calculations. Verdict: **PASS under the explicit hypotheses in the current statement**. This is a mathematical review, not machine verification.

## 1. Scope and exact source checks

The theorem retains the injection of the geometric fundamental group in the homotopy sequence. It assumes a smooth connected finite-type base over a characteristic-zero field, a smooth proper relative curve, finite étale boundary, hyperbolic geometric fibres, and a global boundary section. These restrictions matter. In particular, SGA 1 XIII 4.1 initially uses a relative prime-set quotient; in the present characteristic-zero case the allowed set contains every prime and that quotient is the full group.

I read Deligne's relative construction in §15.19, printed p.239, and its relative tame formal-coordinate interpretation in §15.26, p.242. I also read the full proof of SGA 1 XIII Proposition 4.1, reedition pp.306–307, and Examples 4.4, p.309, including the smooth compactification with relative normal-crossings complement. The line bundle compactification by its zero and infinity sections meets that example.

Primary locators:

- Deligne, *Le groupe fondamental de la droite projective moins trois points* (1989), §§15.19, 15.26; https://publications.ias.edu/sites/default/files/61_LeGroupeFondamentalDroite.pdf . Retrievals `turn733446639view1`, `turn733446639view2`.
- SGA 1, Exposé XIII, 4.0–4.1 and 4.4; https://arxiv.org/pdf/math/0206203 . Retrievals `turn640479968view0`, `turn640479968view1`. The local Kummer inputs are XIII 5.2–5.6, already checked in the preceding local proof.
- Stix, *On cuspidal sections of algebraic fundamental groups*, author version dated 24 February 2012, Corollary 15 and Proposition 16, pp.7–8; https://www.math.uni-frankfurt.de/~stix/research/preprints/STIXcuspsec20120802homepage.pdf . Fresh retrievals `turn654832430view0`, `turn481421575view0`; Proposition 16 and its full proof were read. They give the required geometric self-normalizer; no section-conjecture hypothesis from later packet statements enters.

## 2. Group and formal-category comparison

The tangential functor produces a continuous map Φ from the punctured normal-line fundamental group to the curve fundamental group, over the base group G. On a geometric fibre it is exactly cusp inertia. SGA gives a right-exact sequence I → π1(N×) → G → 1. The composite of the first map with Φ is injective because geometric inertia injects and the retained homotopy hypothesis injects the geometric group. Thus the source sequence is short exact. This argument does not assume an independent vanishing theorem for a boundary map from π2 of the base.

The chosen boundary section makes the geometric conjugacy class of I stable under G. If e is a lift of a base element, a geometric correction a makes a⁻¹e normalize I. The normalizer therefore surjects onto G. Its geometric kernel is I by self-normalization. The image of Φ normalizes I because I is normal in its source. The resulting map of extensions is identity on kernel and quotient, hence injective and surjective; compactness and Hausdorffness give the topological isomorphism.

The formal-tube assertion concerns the category of covers tame along the removed section. Locally the tame Kummer description identifies that category with covers of the punctured tangent line. A coordinate change with the same linear term lifts uniquely through every prime-invertible root tower: the higher-order factor belongs to 1+tR[[t]], on which the nth-power map is bijective. The linear term gives exactly the normal-line transition. These local equivalences consequently descend to the relative punctured normal line, as specified by Deligne §15.26. No wild category or algebraization of arbitrary formal covers is being asserted.

## 3. Extension cocycle and the Kummer Chern class

I independently reconstructed the comparison rather than merely identifying two similarly named obstructions. Push the group extension out along I → I/nI = μn. Its obstruction can be viewed on the étale site as the gerbe of local fibre-standard μn root covers of N×, with descent isomorphisms. A local conormal frame supplies such a cover by adjoining an nth root of the corresponding fibre coordinate. The inertia character of this cover is the chosen standard quotient I → μn; therefore its descent gerbe is the pullback of the group-extension lifting gerbe along the étale classifying map to BG.

If local frames have transition units u_ab, choose roots v_ab with v_ab^n = u_ab after étale refinements. The root-cover identifications compose on a triple overlap with discrepancy v_ab v_bc v_ca. This is both the extension-gerbe descent cocycle and the boundary cocycle defining the Kummer class of the line bundle. Refinement/hypercover descent, rather than the cohomology of one fixed Zariski cover, is the relevant computation. This proves equality of the image of the group extension in étale H² and the finite Kummer Chern class. It requires no K(π,1) hypothesis.

Conormal versus normal coordinates dualize the line and reverse the class; changing the designated inertia orientation can also invert the character. The stated ± convention is therefore appropriate. A completely arbitrary rescaling of the standard inertia orientation would rescale the class by the corresponding unit, but the theorem fixes compatible tangential points and the standard root-coordinate inertia identification, so it is not making that broader claim.

## 4. Continuous comparison and splitting criterion

The extra K(π,1) hypothesis is used only to identify finite locally constant cohomology with group cohomology. For the full factorial inverse system, the earlier F149-KUM paragraph explicitly assumes that the torsion of Pic(S) has bounded exponent. Under that assumption the H¹ inverse system is Mittag–Leffler: at a fixed level, sufficiently deep transition kills its Picard-torsion part and leaves exactly the full unit quotient. The degree-two derived-limit term is zero. The compatible finite-level Chern equality therefore gives the stated continuous equality. For clarity the relative theorem may spell out this global bounded-exponent condition instead of referring to it, but the existing reference is mathematically adequate.

If Pic(S) is finitely generated and the extension splits, every finite pushout has zero class. The established finite étale comparison implies δ_n(L)=0 for every n, so L belongs to n Pic(S) for all n. The intersection of these subgroups is zero in a finitely generated abelian group, including its torsion part. Hence L is trivial. Conversely a conormal basis has a dual normal vector and gives a genuine section of N× → S, inducing a group splitting. This implication does not use K(π,1) or the continuous H² comparison.

Finally, changing the basis by an actual global unit changes its root-coordinate descent by that unit's Kummer cocycle. The acting geometric set is therefore the uncompleted unit torsor described earlier; the theorem does not infer intrinsic recognition of this subset from the abstract group extension.

## 5. Verdict and limitations

All parts of the current theorem pass: the full profinite normalizer comparison, the tame formal-tube comparison, the finite-level Chern-class image, the continuous comparison with its additional hypotheses, and the finite-generation splitting criterion. The exact homotopy-sequence injection, characteristic zero, tame category, and the distinction between geometric tangent bases and all abstract splitting classes must remain visible. No assertion about arbitrary mixed-characteristic fibrations or intrinsic recognition of geometric tangents is justified by this proof.
