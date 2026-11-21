# Independent targeted reading: cote 134-8, manuscript footers 47, 48, 53

Run `/root/source_and_masullo`; GPT-6 Astra Pro; effort not exposed. Primary local source: `research/root_sources/Grothendieck_134-8.pdf`, downloaded by parent from the Montpellier archive. This note gives mathematical transcription/paraphrase of selected assertions, not a proof or a complete diplomatic edition. It distinguishes manuscript footers from physical PDF positions.

The source's catalog title is *Pursuing stacks (À la poursuite des champs). First episode: The Modelizing Story (Histoire de Modèles), Chapitre VII: Linearization of homotopy types*, cote 134-8, 86 archive pages. The supplied page images include the archive cover, so physical PDF positions exceed the footer number by one.

## Footer 47: conditions (a)–(d)

The image is `1348_pre-48.png`; enlarged selected crop is `1348_47_ad_crop.png`.

The displayed setup has a symmetric associative tensor product with unit denoted `Z_M`. A functor

\[
\kappa:\mathrm{Ab}_k\longrightarrow\mathcal M,\qquad U\longmapsto U\otimes_k Z_{\mathcal M}
\]

is stated to be compatible with tensor products. The notation `Z`/`Z_M` is retained from the page; replacing the base unit by k would be an interpretive normalization, not a literal transcription.

(a) The arrow under the limit symbol points **left**: κ is required to commute with inverse limits. The text then states that κ admits a **left adjoint**

\[
\varphi=H_0^{\mathcal M}:\mathcal M\longrightarrow\mathrm{Ab}_k.
\]

The parenthetic **right adjoint of κ** is separately described as the immediate functor `X -> Hom_M(Z_M,X)`. These two adjoint statements must not be interchanged.

(b) The category M has enough projectives. The left derived functor is denoted `Lφ = LH_*^M`; the page states the adjunction

\[
L\varphi:\mathrm D^-(\mathcal M)\rightleftarrows\mathrm D^-(\mathrm{Ab}_k):L\kappa=R\kappa.
\]

The upper arrow points toward the right and the lower κ arrow toward the left. A right-margin comment explains that φ sends projectives to projectives because its right adjoint κ preserves epimorphisms. The surrounding setup treats κ as exact; this cannot be inferred merely from the presence of the tensor notation without its setup.

(c) The displayed augmentation/counit is

\[
L\varphi(Z_{\mathcal M})=L\varphi\kappa(Z)\longrightarrow Z,
\]

and it is required to be an isomorphism. The arrow is **from** the derived value **to** the ground-unit object. This is called global acyclicity.

(d) There is a monomorphism `α: Z_M -> J` with two displayed requirements, for every x in M:

\[
Z_{\mathcal M}\otimes x\longrightarrow J\otimes x
\quad\text{is a monomorphism},\qquad
LH_*^{\mathcal M}(J\otimes_k x)=0.
\]

An annotation mentions flatness of `J/Z_M` as a sufficient interpretation of the tensor-monomorphism condition; the exact crossed-out wording in that annotation has not been certified here.

## Footer 48: proposed theorem

The image is `1348_-1.png`; enlarged upper crop is `1348_48_thm_crop.png`.

The theorem heading has an explicit **question mark**. Under conditions (a)–(d), with W_M the weak equivalences relative to Z_M/φ_M, the displayed claim is

\[
W_{\mathcal M}^{-1}\mathcal M\longrightarrow \mathrm D_{\bullet}(\mathrm{Ab}_k)
\quad\text{is an equivalence of categories}.
\]

The subscript on D is a handwritten dot/bullet in this image. It should not silently be replaced by the whole unbounded derived category. The corollary draws a chain-complex functor Λ from M toward `Ch_*(Ab_k)`, its purported right adjoint in the reverse direction, and the composite `Lφ=LH_*^M` to the corresponding derived target. This note does not certify the full corollary's remaining handwritten hypotheses.

## Footer 53: adjunction notation and marginal bubble

The image is `1348_-6.png`; crops `1348_53_margin_crop.png` and `1348_53_margin_rotated2.png` aid inspection. The upper diagram shows a forward λ_! from M to chain complexes and a reverse λ^*. The text explicitly refers to an adjoint pair. The marginal circled note alongside the lemmas reliably ends with `λ_!, λ^*`; its preceding handwritten words are **not sufficiently legible in this review to certify an exact transcription or a full new question**. No theorem or proof status is inferred from those unread words.

The root agent is independently treating Lemmas 1–3. This targeted reading supplies arrow directions and points of uncertainty; it does not claim those lemmas have been proved here.

## Completed follow-up: the counit criterion

On 2026-11-21, the high-resolution images of handwritten pp. 52–53 were inspected again. The clear all-counits quasi-isomorphism condition, localization equivalence, adjoint directions, and right-adjoint epimorphism-preservation clause support the precise modern statement F-SM-17 in `source_cote1348_counit.tex`. The overwritten variants (ii′) and (ii″) remain uncertified as diplomatic transcriptions.

F-SM-17 is now fully proved: for an exact adjunction into nonnegative complexes, all counits are quasi-isomorphisms if and only if they are so on projective objects of the complex category; these conditions are also equivalent to the explicitly compatible localized adjunction being an equivalence. The projective test uses a resolution inside the abelian category of complexes and finite-diagonal totalizations. It assumes no preservation of infinite coproducts by the right adjoint. The complete proof was reread by its drafter, then independently read throughout by the parent, who reported no gap. These are separately logged whole-proof readings, not formal kernel checks or independent re-proofs.

The six companion modern results BR-13401–06 in `root_linear_archive.tex` were independently read in full by this agent and passed, including the finite-injective-dimension argument over fields and the integers, the locally projective ringoid construction, and the degree-zero counterexample. That proof check does not authenticate the absent intake proofs or every crossed-out manuscript formulation.
