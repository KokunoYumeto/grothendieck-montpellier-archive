# Independent audit of category I12, J9, and L5

Auditor: GPT-6 Astra (OpenAI), inherited effort, subagent algebra_letters.
Date: 2026-11-20; audit completed around 01:46 UTC.
This is a targeted proof/source check, not an independent discovery claim.
The category files were read but not edited by this auditor.

## I12: Kan extension, Ind extension, and accessibility

**Outcome: pass.** The complete written proof in sections/category_I.tex was checked.

For a small skeleton C=E_kappa, the canonical category C/X is kappa-filtered. Its colimit computes X. For any h:C→F with F admitting kappa-filtered colimits, the canonical extension exists. The displayed identification of Hom out of its value with natural transformations from the restricted representable is the usual universal property of that colimit; it does not require F to be a presheaf category. Since every c in C is kappa-presentable, the restricted representable sends a kappa-filtered colimit of X's to a pointwise colimit of presheaves. Maps from that presheaf colimit turn into a limit. Yoneda in F then proves preservation of the colimit. Terminal objects in C/c show that the restriction is h. The same universal property proves full faithfulness on natural transformations.

The common-rank paragraph added in the current file is needed and correct: one cannot merely choose an arbitrary cardinal above the original accessibility ranks and assume it is an accessibility rank. I11 supplies an actual common rank of the indicated form; the preservation rank can be dominated simultaneously. I8 then supplies a rank at which T preserves presentable objects.

The converse from a pointwise left Kan extension on an arbitrary small full C uses that every object of an accessible category is presentable at some sufficiently large regular rank. This follows from a small presentation and commutation of sufficiently filtered colimits of sets with that small limit of Hom sets. The small collection of objects of C has a common such bound. The same natural-transformation calculation proves accessibility. No presentability requirement on h(c) is needed for the final restriction equivalence.

## J9: exact source comparison

**Outcome: pass, as a comparison of known theorems with their stated scope.**

Sources opened or read directly in this audit:

1. A. Grothendieck, *Groupes de Barsotti-Tate et cristaux*, ICM Nice 1970, volume 1, pp.431–436, published1971. Original scan:
   https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/GroupesB-T.pdf .
   I directly viewed sources/category_Grothendieck_ICM1970_p5.png, printed p435.
   Remarks2–3 ask for reconstruction of the Galois representation from the filtered Dieudonne space, the converse reconstruction, and the essential image. The final paragraph explicitly broadens the programme to higher cohomology and more general complete bases. This validates J9's separation of the precise BT comparison from those broader questions.

2. J.-M. Fontaine, *Sur certains types de representations p-adiques du groupe de Galois d'un corps local; construction d'un anneau de Barsotti-Tate*, Annals of Mathematics115(1982),529–577:
   https://www.imo.universite-paris-saclay.fr/~fontaine/jmf.annals.1982.pdf .
   Introduction p529 permits arbitrary perfect residue field. Theorem5.2(iii–iv), printed p561, gives the crystalline/admissible equivalence and inverse; section6.2 identifies the BT comparison. These were opened independently through the web tool. The statement uses admissibility; the weakly admissible essential-image result is correctly assigned to the later theorem.

3. P. Colmez and J.-M. Fontaine, *Construction des representations p-adiques semi-stables*, author version:
   https://webusers.imj-prg.fr/~pierre.colmez/CF.pdf .
   Introduction p2 fixes perfect residue field and a finite totally ramified extension of the Witt fraction field. TheoremA is weak admissibility implies admissibility; section4.1/Theorem4.3 supplies the equivalence formulation. Introduction p3 explicitly attributes the origin of the theory to BT groups and Grothendieck's mysterious-functor questions, and reference[23] is the ICM article above. Thus J9's historical link is independently documented by the primary authors, rather than inferred merely from mathematical similarity.

4. M. Kisin, *Crystalline representations and F-crystals*, author DVI obtained through
   https://people.math.harvard.edu/~kisin/preprints.html
   and https://people.math.harvard.edu/~kisin/dvifiles/wam.dvi .
   I read the existing primary text sources/kisin_2006.txt, Introduction and section2.2, especially Corollary2.2.6. It states the weight0,1 crystalline representation realization as a rational Tate module for any p. The adjacent Lemma2.2.4 distinguishes integral full faithfulness for p>2 from bounded p2 cokernel; that does not invalidate the isogeny statement used here. The perfect-residue-field scope is stated in the Introduction.

The covariant/contravariant Dieudonne conventions require dualization; J9 explicitly retains this convention choice. The claim concerns actual BT objects and their crystalline realization, and does not equate that category with all Hodge–Tate representations. No additional claim about Newton slopes or arbitrary complete bases has been smuggled into the theorem.

Raw independent web retrievals are notes/algebra_web_31.json through algebra_web_33.json. The ICM screenshot request returned text only, so it was not counted as visual evidence; the existing original page PNG was subsequently viewed directly.

## L5: pro-algebra scope and arrow variance

**Outcome: pass after the explicit arrow-convention clarification now present.**

I read sections/category_L.tex, including L3 and L4, against the actual text of Beilinson–Drinfeld, *Chiral Algebras*, section1.4.14(ii), printed p41, and section1.4.15, pp42–44, in sources/category_BD_ch1.txt.
The primary author chapter is
https://math.uchicago.edu/~drinfeld/langlands/chiral/cha_ch1.pdf .

Section1.4.14(ii) defines a Lie coalgebroid by a square-zero odd derivation on Sym_A(P[-1]). The flat formal-groupoid theorem in1.4.15 requires flat conormal and symmetric associated graded. L3 supplies the latter in characteristic zero by polarization, and L4 supplies the inverse to the formal category via its shear map. The proof retains finite augmentation-ideal jets as a pro-algebra; it does not assert without proof that an ordinary inverse limit of sheaves has the prescribed quotients. This scope is coherent with the source's finite-order construction.

The text originally left the arrow convention implicit. A geometric formal-groupoid map G→H induces pullback B_H→B_G and a map of invariant de Rham complexes in that same pullback direction. I flagged this to the category agent. The current L5 now explicitly uses coordinate-proalgebra maps B→B' for its covariant equivalence, and says that geometric arrows give the contravariant form. That resolves the typing ambiguity.

The internal tensor-category use is legitimate. Modules in a ringed topos have the required flat resolutions; internally free modules provide enough flat objects. In the category of sheaves of rational vector spaces, the base tensor product is exact, and the relative A-module flatness is exactly the hypothesis retained for P. No finite projectivity assumption is introduced.

This audit does not attempt to re-prove the deep Beilinson–Drinfeld integration construction. It checks the theorem's exact hypotheses, the preceding elementary lemmas used to satisfy them, the arrow directions, and the stated pro-algebra scope.

