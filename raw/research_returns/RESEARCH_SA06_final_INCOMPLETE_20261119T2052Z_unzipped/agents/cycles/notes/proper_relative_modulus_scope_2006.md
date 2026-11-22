# Proper relative families and the modulus comparisons: exact read scope

**Research status:** no new theorem on the UK.7 quotient. This is a primary-source scope check and a refinement of the location of the remaining gap.

Credit: GPT-6 Astra Pro (OpenAI), ChatGPT Pro mode, RESEARCH_SA06, `/root/cycles_continuation`; effort setting not separately exposed.

The sufficient assertion under investigation is: for a smooth projective surface S and its divisor D, every class in T(S)_Q is the image of an endpoint difference of an actual class in K0(S×P,D×P)_Q for a fixed smooth connected proper curve P. The RC countermodel excludes the corresponding assertion for all curve Pic0 classes. VP.1 proves the surface assertion when S=A×B and D is a union of vertical fibres. Neither decides a general boundary or a crossed product boundary.

## Published comparisons read in full at the indicated locations

Binda, F., & Krishna, A. (2018). Zero cycles with modulus and zero cycles on singular varieties. *Compositio Mathematica,154*,120–187. https://doi.org/10.1112/S0010437X17007503 . Retained published PDF SHA256 `1835e56ebf7c67b4fd6da6272a0e54724e7d9be31243d4287dfd76dd309339c3`. During the checkpoint23 freeze I read all of §12.2, including Theorem12.4 and its full displayed proof, and all of §13 through the full proof of Theorem13.4, printed pp.177–181. This includes Lemma13.1, Proposition13.2 and Lemma13.3 with their complete displayed proofs. Proposition12.3 is a cited affine Milnor statement, not a newly reconstructed proof. Earlier double-decomposition, Levine and birelative foundations are explicitly external dependencies in these arguments; no full new audit of those papers is claimed.

Krishna, A. (2015). On 0-cycles with modulus. *Algebra & Number Theory,9*(10),2397–2415. https://doi.org/10.2140/ant.2015.9.2397 . Retained published PDF SHA256 `b151f9416aa40455f6b1822de72d6e965dcfad6915070cc7c2a33b3b1dcf0871`. Read the complete relative/support spectral-sequence setup and Lemma2.1 with its full displayed proof, pp.2401–2402. The unit f congruent to one along D lifts to relative K1 by pullback of the coordinate class on (G_m,{1}), so the displayed differential vanishes. The dimension-two truncation is essential to that exact sequence. No fresh full proof audit of the paper's remaining theorems is claimed.

## The two comparisons must be distinguished

For positive-characteristic rational K-theory, the double-to-relative K comparison on S×P follows already from the previously audited Geisser–Hesselholt closed-union excision and Thomason–Trobaugh Zariski descent. The double of S×P along D×P is the product of the double with P. Its actual homotopy pullback square identifies the relative fibre from one branch with K(S×P,D×P)_Q. This argument is not limited to surface dimension and is natural in the fixed parameter and its endpoints.

The remaining gap is the **cycle comparison in codimension two on the threefold S×P**, with enough functoriality to control proper endpoint differences. Binda–Krishna Theorem13.4 identifies top zero-cycles on a surface with a filtration-two relative K0 group. Applying that theorem to S×P would change dimension to three and would ask instead for a non-top one-cycle statement. Its proof does not give that statement. In particular, Lemma13.3 uses H² of the boundary curve equal to zero; D×P is a surface.

If D is ample, any actual proper curve in (S minus D)×P projects constantly to the affine S minus D. This does not prove that all relative K0 families have constant endpoints: it would first require a surjective cycle-class comparison with precisely those admissible representatives in the non-top degree. Such a comparison is not supplied by the displayed surface theorems. No rigidity or vanishing conclusion follows from this observation alone.

## Further primary lead, read as statements only

Krishna and Pelaez, *Motivic spectral sequence for relative homotopy K-theory*, arXiv:1801.00922v2 (12March2019), https://arxiv.org/pdf/1801.00922 , was opened in full. I read its introduction and Theorems1.4–1.6, author pp.1–4, as statements, not their complete proofs. It supplies relative KH motivic spectral sequences with rational degeneration and identifies projective relative motivic cohomology with compact-support cohomology of the complement. Its comparison with Chow groups with modulus is asserted as an isomorphism only in the affine top-degree range with the displayed regularity hypotheses. It therefore does not fill the needed projective non-top proper-family comparison. No K=KH identification on arbitrary singular pairs or motive-level endpoint-generation theorem is imported from this introductory read.

Searches also returned derived logarithmic Albanese and Suslin-homology results. Universal regular quotients and affine/smooth parameter classes are not equated with the actual smooth-proper endpoint subgroup here. No absence or priority claim is made.

Saved after thaw: 2026-11-19T20:06:59.815054+00:00

## Follow-up: proper parameter parts in Kohrita

After thaw I read Kohrita's 2017 author v2, arXiv:1512.02320, the complete Section3.4 (Definitions3.17 and3.19 through the end of Theorem3.25's displayed proof), authorpp27–32. It expressly defines the subgroup generated using smooth proper parameters. Theorem3.25 identifies its universal regular representative with the maximal abelian subvariety of the usual semi-abelian representative only for (m,n)=(2,1), under resolution of singularities. This is a relative-Picard result; it does not identify the desired (4,2) subgroup or show that the surface Albanese kernel is in it. Universal representatives remain distinct from the full subgroup.

I also read v3 (10April2024), Section2.1 and Definitions2.3–2.5, Axiom2.6 and Lemmas2.8–2.9 with their printed arguments. This version develops the general parameter-class formalism and explicitly notes a gap in an earlier multiplicative-morphism argument that it repairs. The curve reduction permits smooth curves generally; it does not change them to proper curves for an arbitrary relative motive. No v2 theorem is imported without its stated hypotheses, and no proper-family exactness conclusion is inferred.

Primary source: Kohrita, T. (2017; revised2024). *The algebraic part of motivic cohomology*, arXiv:1512.02320v2/v3. Exact local versions are sources/kohrita2017_algebraic_part_v2.pdf and sources/kohrita2024_algebraic_part_v3.pdf. The displayed arguments were read; their complete external foundational references were not newly re-audited.

Follow-up saved: 2026-11-19T20:16:27.645638+00:00
