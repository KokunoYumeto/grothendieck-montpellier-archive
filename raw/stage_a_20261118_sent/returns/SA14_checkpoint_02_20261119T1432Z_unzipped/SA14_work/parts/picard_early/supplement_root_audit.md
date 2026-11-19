# Supplemental checks requested by the root consolidator

Checked19November2026 after completing the two assigned Pro packages. These are reports to the root owner; no root files were edited. The fixed part counts remain142 claims and95 items. Root owns the additional Codex claim IDs.

## 1. Correspondence separatedness: bounded search, not a claimed resolution

**Root C-SA14-674.** I read `sources/SA14_texts/codex/A57-02_transcription.tex` physical lines1–32, scans20–23. The letter assumes the usual properness, flatness and direct-image-of-the-structure-sheaf conditions for both factors. It states that Picard representability for one factor suffices and explicitly broadens this to pre-ét representability: a quotient of a locally finite-type scheme by an étale relation. Its dimension argument is only sketched. The projective case and the attempted Chow/fundamental-group approaches must remain distinct from that sketch.

Modern Picard representability meets the **object-existence** part: Stacks Proposition99.11.8, tag0D2C, gives an algebraic space for a proper flat finitely presented morphism with universal O-base change. Its local finite-presentation property is discussed separately in the referenced Lemma108.9.3. However, this does not by itself constitute a checked proof of the letter’s generic-constant-to-special-constant step for maps into a possibly nonseparated Picard algebraic space. The general correspondence conclusion must not be justified by writing “Artin” alone.

The targeted searches used English and French forms of `Corr Picard separated Murre`, `functeur des correspondances séparé`, `Murre correspondences separated Picard functor`, `functor Corr separatedness algebraic`, `Picard rigidity algebraic spaces proper flat`, `A note on divisorial correspondences arxiv`, and the exact variants `Raynaud III4.3`, `III.4.3`, `III, Proposition4.3`. These found the modern primary paper by Bertolin–Galluzzi, arXiv1902.07448v2,8January2020, opened in full. Its Theorem1.1 concerns extensions of abelian schemes by tori with universal H⁰=O. Its proof, pp2–3, cites **Raynaud, LNM119, III Proposition4.3** for separatedness. Its introductory summary of Murre’s Theorem4 omits the qualification that the root’s direct reading found; it therefore cannot substitute for the original theorem.

The Raynaud book and chapter metadata were opened at:

- <https://link.springer.com/book/10.1007/BFb0059504>
- <https://link.springer.com/chapter/10.1007/BFb0059509>

The latter is “Applications au foncteur de Picard et aux correspondances divisorielles,” printedpp37–55, copyright1970. Only subscription metadata/preview was available; a direct primary-PDF request was unsuccessful. No exact statement of III.4.3 was read. A further search of exact reference forms did not locate a primary full-text replacement. Laurent–Schröer’s Lemma3.2 was also opened, but it concerns the numerical Picard sheaf under its stated flatness hypothesis and does not give the unrestricted Corr statement.

**Recommendation:** retain C with the precise missing dependency. The search establishes modern Picard algebraic-space representability and strong special-case correspondence results; it does not establish that the entire general separatedness question is still mathematically open in2026. The remaining task is to read RaynaudIII.4.3 or give a complete algebraic-space rigidity proof with all the letter’s hypotheses. Raw search/open records are `outputs/web_58.json` through`web_70.json`; the relevant primary paper is <https://arxiv.org/pdf/1902.07448>.

## 2. The scan64 conormal question has an exact published answer

**Root C-SA14-686.** Read `K57-03_transcription.tex` lines395–430, especially414–422. This is a general group-scheme question over a characteristic-zero base, not merely the nearby Pic⁰ smoothness question.

The primary editor PDF <https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExp6B.pdf> was opened and Proposition1.6 read: for S of characteristic zero and G locally of finite presentation along the identity section e, G is smooth along e if and only if its conormal module ω_G/S is locally free. The local finite-presentation hypothesis is explicit. Flatness is not an additional assumption; it is included in the smoothness conclusion. The proof uses Ω¹_G/S=π*ω_G/S and EGAIV₄16.12.2,17.12.5. Cartier’s field theorem is a separate Corollary1.6.1.

Locator: PDFp6, current printedp202, original marginp327; text extraction lines244–268. The title is “Généralités sur les schémas en groupes,” byJ.-E.Bertin. The opened file notes that this exposé did not correspond to an oral seminar talk, so a seminar date should not be invented for the precise proposition. `outputs/web_60.json` and`web_61.json` preserve the reading.

## 3. Definite formulation issue in C-SA14-612

The current first sentence omits a separation or closed-embedding condition: finite étale subgroup schemes in an arbitrary unramified group over a connected base need not be determined by a single fibre when the ambient group is nonseparated.

The actual finite-étale lemma at scan45, physical lines282–284 of `K57-02_transcription.tex`, deliberately deletes “pré” from the historical S-schéma wording while deleting “fermés” for the two finite étale subschemes. Historical separatedness makes those finite-over-S maps closed in the ambient X. The proof at46 then uses closedness in taking closures. The modern consolidation should preserve that separation explicitly, or state the alternative that both embeddings are closed.

Here is the elementary obstruction if both conditions are removed. Glue two copies of a trait S=SpecQ[[t]] along their common generic open, obtaining an étale S-scheme D with a doubled closed point. Its two sections are finite étale overS, agree on the generic fibre and are distinct. D can be made an étale S-group by giving its special fibre the law Z/2 and identifying the two generic sections; chartwise multiplication adds the labels modulo2, and the laws agree on the generic overlap. In G=(Z/2)_S×_S D, take the graph of the zero map and the graph of the map sending each label to the correspondingly labelled section ofD. These are finite étale subgroup schemes, agree generically, and differ on the closed fibre. Their embeddings are not closed; that is exactly the missing alternative.

This is a counterexample to the broadened modern wording, not an accusation that the original historical “schéma” lemma was false. Adding ambient separatedness restores the intended finite-intersection argument. No uncertain ink character has been changed.

## 4. C-SA14-639: correct special case, missing general source statement

The modern statement with universal f_*O_X=O_S is mathematically correct. A section gives the normalization L⊗f*(g*L)⁻¹. The inverse is necessary. The cohomological boundary vanishes for a section because pullback along the section retracts pullback onH²(G_m); the rigidified descent description is consistent. The Brauer–Severi example at scan179 is an explicit source example, not merely a modern analogy.

There is nevertheless a coverage issue. Scans138–140 start with a factorization X→Σ→S, where Σ→S is finite and O_Σ≅φ_*O_X. Their exact sequence uses **Pic(Σ)**, and their section is a section of X→Σ. This need not have f_*O_X=O_S. The normalization uses φ* and g:Σ→X. It should be a separate claim or an explicit additional clause. Simply listing scans138–140 under the later S-based special case loses the finite-Stein-factor assertion.

The later scans173–179 also distinguish the raw absolute Picard presheaf, its Zariski-local version, and its fpqc sheafification. That hierarchy should remain visible: the page’s descent statements require exactly the section and universal-H⁰ assumptions it records. The direct reads covered K57-08 lines125–148,170–194 and K57-10 lines164–335.

### Finite Stein factor refinement proposed for rootC687

No additional flatness of Σ/S is needed for this particular rigidification and sheaf-identification argument. Assume Σ→S is finite, φ:X→Σ has a section g, and O_Σ→φ_*O_X remains an isomorphism after every S-base change. Then

\[
Q(T)=\operatorname{Pic}(X_T)/\varphi_T^*\operatorname{Pic}(\Sigma_T)
\]

identifies with isomorphism classes of g_T-rigidified line bundles. A representative L is replaced by L⊗φ_T^*(g_T^*L)⁻¹. Its restriction along g_T has a canonical trivialization. Conversely, two trivializations of the same line bundle differ by a unit on Σ_T, and universal H⁰ identifies that unit with a unique global unit on X_T. Consequently the rigidified object has no nontrivial automorphism, and isomorphisms between equal rigidified classes are unique. Effective fpqc descent of line bundles and of their trivializations therefore proves that Q is already an fpqc sheaf. This uses universal H⁰, not a finite-flatness assertion.

The comparison with the usual relative Picard sheaf uses the finiteness of Σ/S at a different step. Every line bundle M on a finite T-scheme Σ_T becomes trivial over Σ_{T_i} for a Zariski cover {T_i} of T. Locally at t∈T, the corresponding algebra is finite over the local ring O_{T,t}, hence semilocal; an invertible module over a semilocal ring is free of rank one. Its generator extends to a neighbourhood. After shrinking, its induced surjection from the finite algebra splits because M is projective, and the finite complementary module vanishes after another shrinking. Thus the generator gives an isomorphism. No flatness of the finite algebra over the base was used.

The natural surjection of presheaves Pic(X_T)/Pic(T)→Q(T) has kernel coming from Pic(Σ_T)/Pic(T), which the preceding argument makes Zariski-locally zero. Sheafification therefore identifies the usual fppf relative Picard functor with Q. Properness and flatness of X/S are appropriate to the surrounding Picard-representability discussion, but are not needed for this descent comparison once its finite-factor, section and universal-H⁰ hypotheses are supplied. The historical Pic′/Pic* distinction should still be stated before explaining this modern identification.

## 5. Independent audit of root_proofs§§4–6

The finite-type argument in§4 is valid in its stated noetherian separated/open setting. A quasi-compact open containing the entire generic fibre is finite type and its generic properness spreads after shrinking. Because the ambient target is separated overS, this proper open is closed inX. Its complement has open image and no generic point, hence is empty over the integral base. Closed-base restriction preserves the relevant ordinary openness by the displayed image equality, so noetherian induction supplies the local quasi-compactness. This does not justify dropping separation or openness, and the file does not claim that.

The conic bidegrees, concurrent-triple-line flatness and H¹ discrepancy, corrected Riemann–Roch threshold, normalization inverse, marked-projective-frame argument, and Cartier-divisor long exact sequence in§5 are consistent under their written assumptions. C-SA14-639 has the source-scope omission explained above, rather than a false modern normalization formula.

In§6, C-SA14-640 correctly assumes a **finite étale** divisor. The prose currently says only “finite reduced” over an arbitrary field; those are not equivalent over an imperfect field. Change the prose to finite étale (or geometrically reduced finite) to match the claim and its semiabelian Jacobian model. Its comparison with the invertible-n torsion of the generalized Jacobian, and the retained cyclotomic twist, are consistent under that corrected hypothesis. The normalization/δ/branch formulas inC-SA14-642 and the stable-graph arithmetic are also consistent. The relative transgression remains appropriately qualified rather than claimed from the field-level theorem.

## 6. SGA3 XI title verified

The existing R_SGA3XI title is correct. The opened primary <https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo11.pdf> has the header “Critères de représentabilité. Applications aux sous-groupes de type multiplicatif des schémas en groupes affines,” byA.Grothendieck. No title correction is needed. See`outputs/web_71.json`.

## Audit scope

The complete `research/root_proofs.md` and the mathematical statement/fate fields for rootC601–686 were read. The truncated combined claim display was followed by a separate complete read ofC629–657. I reread the original loci forC612,C639 and the general group question at64. Findings above are the definite issues identified; they are not a certification of every cited external theorem in the root register. Root retains authority to edit and merge its records.
