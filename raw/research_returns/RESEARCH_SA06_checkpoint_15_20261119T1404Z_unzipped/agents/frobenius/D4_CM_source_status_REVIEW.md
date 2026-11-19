# D.4g: exact CM Hodge input and the boundary of our independent audit

## Finding

The current D.4g explicitly assumes **Theorem I of Pol van Hoften and Jack Sempliner, _The Hodge conjecture for CM abelian varieties_, Hexagon preprint 2610.00259v2**. It does not cite Grabowski. A search of the current arithmetic fragments, bibliography, root sections, and notes found no occurrence of that name. This corrects the attribution of the input without making any claim about other papers.

Theorem I, author-PDF p. 1, asserts the rational Hodge conjecture in every codimension for every complex abelian variety admitting complex multiplication. The definition immediately preceding it is surjectivity of the rational algebraic-cycle map onto rational Hodge classes. The source is a 25-page preprint. Its Hexagon history records the initial version on 15 October 2026 and version 2 on 18 October 2026; the record identifies no DOI or journal publication. Van Hoften's own page lists it under expository work. We have no source establishing completed peer review. The appropriate wording is therefore a theorem **claimed in this explicitly identified preprint and taken as an input**, with the downstream statement conditional on its validity.

## Exact dependency chain used in D.4g

1. The preprint's Theorem I supplies the hypothesis of Milne (2002), Theorem 3.3, printed pp. 607–608, in the published-layout arXiv v3. That theorem gives numerical equals prime-to-characteristic etale homological equivalence on all abelian varieties over an algebraically closed field, and the Hodge standard conjecture for their etale cohomology.
2. Milne (2002), Corollary 3.4, printed p. 608, supplies the unique geometric polarization of the corresponding category of abelian motives. Theorem 2.1 supplies the geometric positivity used earlier in that paper. These exact primary statements were freshly reopened.
3. D.4g then uses its explicitly assumed exact faithful specialization tensor functors and the common relative forms on degree-one generators. Restriction to summands, reflection of nondegeneracy, positivity of the numerical trace form, and uniqueness of the compatible positive classes prove the common-polarization statement. This tensor argument was independently checked in our earlier D4_refinements_independent_REVIEW.md.

The related finite-field Tate consequence uses Milne (1999), Theorem 7.1, author-PDF p. 25, and the interpretation of (0.1) on author pp. 2–3. That source was also freshly reopened. The journal pagination of this article is 45–76, as confirmed in Milne (2002)'s reference list; the arithmetic bibliography currently says 47–81 and should be corrected by its owner. This is a bibliographic correction, not a change to the theorem used.

The 2026 preprint itself refers to a differently numbered Milne Theorem 4.6. We do not silently transfer that locator to the published-layout 2002 source: the exact locators used by D.4g are Theorem 3.3 and Corollary 3.4 in that version.

## What was and was not independently verified

The statement, version, hypotheses, and formal applicability of the cited 2026 theorem were checked. The arithmetic agent opened the full preprint and checked the elementary surface-to-cycle reduction and the structure of its proof chain. Our independent D.4g audit checked the published Milne implications and the new common-generator polarization argument. **We have not independently verified the full analytic heart of the 2026 proof or re-proved all imported analytic results.** Opening a complete PDF, or checking a dependency chain, is not such a verification.

The relevant new analytic claim is Theorem 4.0.2, author p. 12: four specified degree-one Hodge structures admit maps into the first cohomology of a Picard modular surface with a nonzero fourfold cup product. Its proof uses the theta-lifting description and spanning result in Theorem 3.1.11 and Proposition 4.1.8, which draw on Liu (2021) and Bergeron, Millson, and Moeglin (2016). The final period argument is in Section 4.2. In particular, Lemma 4.2.7, pp. 17–19, proves nonvanishing of a diagonal theta-period functional from its archimedean value at zero; Lemma 4.2.9, pp. 20–21, supplies that nonzero archimedean value using the doubling map, Kudla–Millson forms, and approximation; Lemma 4.2.10, pp. 21–22, gives the final finite character expansion. A complete independent audit would have to check those arguments and the exact hypotheses, normalizations, and convergence statements in their analytic sources.

Section 1.3, p. 4, explains the relationship with the prior OpenAI preprint [Ope26]. The authors describe their own argument as a variant, and explicitly do not claim a detailed verification of [Ope26]. Thus our cited input is their stated Theorem I and their written proof, not an independent certification of [Ope26]. Section 1.4 and the Hexagon provenance statement disclose extensive model assistance. That disclosure establishes provenance; it does not by itself establish a mathematical error. We found no specific flaw in this source-status audit and make no claim that the theorem is false.

## Recommended status language

Retain D.4g as **proved conditional on the CM Hodge theorem claimed by van Hoften–Sempliner (2026, Theorem I)**. Describe the independent work as verification of the cited theorem's precise scope, the established Milne implications, and the tensor argument. Do not label the 2026 analytic proof independently verified, peer reviewed, or unconditionally certified by this project.

## Primary sources freshly opened

- van Hoften, P., & Sempliner, J. (2026). _The Hodge conjecture for CM abelian varieties_ (Hexagon preprint 2610.00259v2). Full author PDF, 25 pages: https://polvanhoften2.github.io/Pol%20van%20Hoften%20and%20Jack%20Sempliner%20-%20The%20Hodge%20conjecture%20for%20CM%20abelian%20varieties.pdf ; retrieval turn212171446view0. Local PDF and transcription: research/agents/real_weil/sources/vanhoften_sempliner2026.pdf and .txt.
- Hexagon version/status/provenance record: https://hexagonmath.org/2610.00259v2 ; retrieval turn755003707view0. Author's listing: https://polvanhoften2.github.io/ ; turn755003707view1.
- Milne, J. S. (2002). Polarizations and Grothendieck's standard conjectures. _Annals of Mathematics, 155_(2), 599–610. Published-layout arXiv v3: https://arxiv.org/pdf/math/0103175 ; retrieval turn324735366view1, precise theorem finds turn212171446view1–2.
- Milne, J. S. (1999). Lefschetz motives and the Tate conjecture. _Compositio Mathematica, 117_(1), 45–76. Author version: https://www.jmilne.org/math/articles/1999bP.pdf ; retrieval turn324735366view2 and theorem find turn212171446view3.

No shared fragment or bibliography was edited.
