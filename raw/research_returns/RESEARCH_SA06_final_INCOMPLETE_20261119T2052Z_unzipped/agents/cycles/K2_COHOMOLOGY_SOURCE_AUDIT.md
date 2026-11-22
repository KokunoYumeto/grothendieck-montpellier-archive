# Direct Milnor cohomology bridge: source record

2026-11-19, checks completed by 14:44 UTC; retained before checkpoint16. The proof fragment `k2_cohomology_divisibility_draft.tex` is unregistered and separate from certified C.3bi.

## Opened original sources

**Rost (1996), Chow groups with coefficients.** Full author-hosted original PDF and author corrections opened and read. Exact inputs: §5, pp.355–357, defines the graded complexes and gives the localization sequence; Remark5.4,p357 compares degree-two Milnor/Quillen complexes; Corollary6.5,p360 identifies sheaf cohomology; Proposition8.6 and proof,p370 proves affine homotopy; Proposition4.1(3) and proof,p351 gives proper/flat base change; §12,p382 gives pullback and its explicit open-restriction compatibility, with Theorem12.1 and Proposition12.2,pp382–383. These suffice for the two generation surjections and the higher-degree induction. No full projective-bundle or blow-up cohomology theorem was assumed without proof.

- Primary: https://www.math.uni-bielefeld.de/~rost/data/10000028002.pdf
- Author corrections: https://www.math.uni-bielefeld.de/~rost/chowcoeff.html
- Local primary: `sources/Rost1996_chow_coefficients.pdf`
- Local corrections: `sources/Rost1996_author_corrections.html`
- Reproducible downloader: `code/fetch_k2_cohomology_sources.py`, stdout `.out`.
- Manifest: `output/k2_cohomology_source_fetch.json`, actual14:42:18.703636–14:42:33.530442UTC,14.82680718100164seconds. OriginalPDF543897bytes, SHA256 a87d65d2e5b1744e00e7001fe29110c04c27c6e5e5a1aabc1d7b291e772e851f.
- Bibliography: `k2_cohomology_references.bib`, key cyRost1996.

The author corrects an unused flatness remark on p377 and signs in14.3–14.4. Neither assertion is used in the generation/divisibility proof. If later arguments use the product section, the sign corrections must be retained explicitly.

**Kerz (2009), original 29-page author version dated29April2008.** Freshly reopened Theorem7.1,p21 and its proof throughp22; Theorem7.5,p22. The former supplies integral Gersten exactness on regular equicharacteristic schemes with sufficiently large residue fields, satisfied here because the fields contain the algebraically closed coefficient field. The latter supplies the integral Milnor Bloch formula. Definition2.1,p3 is the ordinary tensor/Steinberg sheaf definition. The comparison between the two smooth degree-two Gersten complexes uses only fieldK2,K1,K0; no comparison on an arbitrary nonreduced scheme is inferred.

- https://kerz.app.uni-regensburg.de/articles/milnork_inventiones.pdf
- Existing bibliography `absolute_picard_references.bib`, key cyKerz2009Milnor.

**Braunling (2013), published NYJM19,545–564.** Freshly reopened and read §1,pp548–549 and §3,pp557–558, especially the full ring-product diagram(22) onp558. The scope is smooth varieties over arbitrary fields; the plain Milnor sheaf agrees with the unramified sheaf over infinite fields. Diagram(22) identifies the full Chow-ring product with sheaf cup and symbol concatenation. Its scope is not restricted to the top numerical intersection specialization that follows it. This provides the actual line-product class compatibility in every characteristic. Regular strict-local constructions in this project reduce to their smooth finite stages for this compatibility; no Bloch formula for nonreduced E is required.

- https://nyjm.albany.edu/j/2013/19-28p.pdf
- Existing bibliography `absolute_picard_references.bib`, key cyBraunling2013; no duplicate entry created.

## Current proof status

The degree-two and higher Milnor divisibility arguments have received complete mathematical passes from parent, Frobenius, and real_weil (parent's initial exact source/proof pass was for degree two; the higher typed reread is separately recorded by parent). Frobenius's independent audit files are `../frobenius/K2_cohomology_divisibility_independent_REVIEW.md` and its CHECK_EVENTS.tsv. The all-degree relative differential/exponent lemma has a separate complete own review in `relative_milnor_all_characteristics_independent_REVIEW.md`. These auxiliary passes do not certify the combined geometric theorem, its exceptional Chow boundary, or a broader range of local restriction counterexamples.
