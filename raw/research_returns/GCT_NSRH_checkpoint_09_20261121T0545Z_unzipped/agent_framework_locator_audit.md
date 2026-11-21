# Exact affine and perfect-complex locator audit

Auditor: /root/grothendieck_dictionary, GPT-6 Astra Pro; effort not exposed. Date: 21 November 2026 UTC.

## Corrections required by the reviewed Part III snapshot

EGA I (1960), Section9.5 is a scheme-theoretic-image locator. It must not be used as the affine module/sheaf equivalence in the F30/F36/F34-ray/F40 dictionary paragraphs. Its use for the affine scheme-image example F15 remains appropriate.

SGA6, Exposé V, Sections2–3 belongs to the lambda/gamma framework. It is not the definition of a perfect diagonal or the source of a modern smooth dg category criterion.

The reviewed snapshot was agent_grothendieck_dictionary_snapshot3.tex. Its scope hash was 0ae824fc1951fef43e3ea3bb4f6ba0ce379543ba16538bcedd6b4a03c6f5956b; the corresponding whole main text hash was2e694f7108523b4a3559443d4699c36b55968ac2d134b9cc39f1c190570cc95b. The entire Part III-through-end scope was read, including the table, later dictionary paragraphs, archive audit, remaining gaps, and bibliography. This is a scoped dictionary review, not a new full-paper proof check. The two locator corrections above were the substantive issues found in that snapshot.

## Verified modern exact formulations

- Stacks Lemma26.7.5, tag01IB: modules over R and quasi-coherent sheaves on Spec(R) are equivalent through tilde and global sections. Original formal source: https://stacks.math.columbia.edu/tag/01IB. Reopened refs turn125015554view0 and turn858390100view0.
- Stacks Definition15.76.1, tag0657: a ring complex is perfect when it is quasi-isomorphic to a bounded complex of finite projective modules. Current numbering is15.76.1. Source: https://stacks.math.columbia.edu/tag/0657. Reopened refs turn125015554view1 and turn858390100view1.
- Tabuada, Noncommutative Weil conjecture, inspected arXiv1808.00950v7, Section5.1, printed pages13–14: properness and perfect-diagonal smoothness for dg categories. This is the exact modern framework used for F40/F44 and is separate from the historical SGA definition.

The root agent is separately inspecting the original EGA affine theorems. This file does not assert their exact theorem numbers before that inspection is confirmed.

## Original SGA6 Definition4.7 and Example4.8 now inspected

The original facsimile was retrieved as small page images from the William Stein SGA mirror and visually inspected. This closes the original-source-access qualification specifically for Exposé I, Definition4.7 and Example4.8.

The table of contents, original pages 6c_1 and6c_2, identifies Exposé I by L. Illusie, “Généralités sur les Conditions de Finitude dans les Catégories Dérivées,” beginning on printed page78. Exposé V by P. Berthelot, “Généralités sur les lambda-Anneaux,” begins on printed page297. These are published SGA6 facsimiles, not Montpellier unpublished archive leaves.

Exact definition:

- **Exposé I, Definition4.7, printed pages121–122.** Perfect amplitude is defined locally by comparison with a strictly perfect complex supported in a bounded interval; perfection means local finite perfect amplitude.
- **Example4.8, printed page122.** For a ringed topos the relevant subcategory consists of direct summands of finite free modules. Under the locally free condition stated there, perfection means local isomorphism in the derived category to a bounded complex of finite free modules.
- **Notation4.9, page122**, and the complete statement of **Proposition4.10, page123**, were also inspected. The proposition identifies the associated local category with the perfect triangulated subcategory. Its entire general proof was not separately certified.

Original images:

https://wstein.org/sga/sga/6/6t_121.jpeg

https://wstein.org/sga/sga/6/6t_122.jpeg

https://wstein.org/sga/sga/6/6t_123.jpeg

Local checked files are primary_sources/SGA6_6t_121.jpeg, SGA6_6t_122.jpeg, and SGA6_6t_123.jpeg. Supporting original table-of-contents images are SGA6_6c_1.jpeg and SGA6_6c_2.jpeg. The image named SGA6_contents1.jpeg is actually the first introduction page, retrieved from6a3i_1.jpeg; its content was read as introduction, not mistaken for the table of contents. That page explicitly describes perfect complexes as a central notion developed in Exposés I–III.

The web-accessed original mirror index is https://wstein.org/sga/sga/6/index.html, ref turn652533079view1; its table-of-contents image route is recorded in the local source files. The exact mathematical definition above was read visually from the original pages.

This does not remove the separate access qualification for the original Exposé V Sections2–3 scans. Their lambda/gamma locator remains background corroborated by already inspected primary mathematical literature. No modern diagonal-smoothness assertion is attributed to Exposé V.

## Honest check-event scope

The affine and perfect-complex source statements above were checked as exact definitions/equivalences and applicable framework locators. The new F40/F44 diagonal resolutions are independently proved in their own notes and fragments. This audit does not claim that SGA6 contains those noncommutative constructions or their GCT comparisons.

## Original EGA I audit reported by the parent

The parent subsequently downloaded and read the original EGA I (1960), including the proof context, and visually checked printed pages86,87,90. The exact affine locators are Theorem1.3.7 p86, Corollary1.3.8 p87, and Theorem1.4.1 pp90--92. In that PDF the corresponding first pages are one-based85,86,89. The saved original is primary_sources/EGAI_1960.pdf, SHA256 78d209f1d58e53f679944f336eaca5ac73f68bd811b1fbe6e655e1d4270bbb2d. This paragraph records the parent's original-source inspection; it does not invent an additional independent visual inspection by this author. The original-source access qualification may now be removed from those affine locators. EGA I §9.5 remains the separate scheme-image reference.
