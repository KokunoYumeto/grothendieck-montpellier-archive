# Middle-package search audit

Date: 2026-11-19 UTC. Research identity: GPT-6 Astra Pro; effort not exposed by runtime; SA08/middle.

This is the search record for all 101 middle-package claims. `search_coverage.tsv` gives one row per claim, its exact manuscript locator, actual search batches, the resulting fate, source hypotheses and computational evidence. `search_results_index.json` indexes all 51 saved result payloads and their hashes. The human-authored judgments are in `claims.json`; this program only joins already written records.

## Search scope and limits

The search covered published SGA7 IX and its backward references; Numdam for Cartan-related and Dold–Puppe/Roby/Sullivan sources; the author sites of de Jong, Mandell, Cartier, Horel and Li–Mondal; arXiv for integral, rational, binomial and p-adic homotopy models; publisher originals for BMT, Cenkl, Cenkl–Porter, Garvín and the monoidal acyclic-model theorem; MathOverflow; zbMATH-indexed results and a directly attempted record; and Grothendieck publication bibliographies. The final theorem comparisons use opened primary works, except the explicitly marked original-source access gaps.

The zbMATH record attempt returned 403. Coleman’s original PDF also returned 403 through the browser retrieval and an independent urllib attempt; a publisher first-page excerpt is bibliographic evidence only. The original Stoia1975 note, Dwyer1979 and Cartier1957 note were not obtained by this agent. Stoia’s title/month were followed back through the opened Bănică–Stoia1979 bibliography; Dwyer’s precise range is reported from the opened later primary exposition by Scheerer–Tanré1991; the elementary Cartier-coordinate calculation has its own proof. Miller’s original is delegated to root and is not relabelled as opened by this agent. These gaps limit source attribution, not the existence of a searched fate.

For batches 1–38 the saved files contain full original returned tool output but not a separate top-level input object. Their purpose labels below therefore describe the actual recorded research themes and source-opening trail; they are not invented verbatim search strings. Batches39–51 retain the literal tool inputs as well. Search-result titles are discovery leads until a primary source is opened and its hypotheses checked. Newly surfaced self-labelled AI-generated exposition and an unofficial SGA retyping were not used as theorem evidence.

## Principal comparison decisions

1. Cartan’s original §7 explicitly reports the Grothendieck lecture of 12 December1975 and publishes weighted PD comparisons and binomial products. This is an exact development by another author, not a theorem asserting an ordinary unweighted integral commutative cochain equivalence.
2. Garvín et al., Theorem4.2 p176, has strict p<q. Cenkl–Porter1982 Proposition1 has the same strict range and adds higher multiplicative homotopies; Cenkl–Porter1984 uses Q_q obtained by inverting primes≤q. These statements cannot replace the inclusive good-truncation comparison of the manuscript without a convention check.
3. Mandell2002 and Guillén Santos–Navarro–Pascual–Roig2008 establish strong uniqueness results in precisely specified enhanced or monoidal categories. Their exact axioms have not been verified for the manuscript’s weighted τ-infinity PD category. Li–Mondal’s algebraic de Rham endomorphism theorem has smooth-algebra inputs, so its semidirect monoid does not calculate the manuscript’s groups.
4. BMT2016 Proposition3.5 p270 is derived Γ/Λ/Sym décalage for finite projective modules; it does not make naive termwise powers of complexes equivalent. The Γ²/Sym² calculation in this dossier is explicit and distinguishes them from the correct exterior model.
5. The SGA donor matches are dated seminar1967–1969/publication1972, despite their physical reuse in a 1975–1976 folder. De Jong1998 removes a characteristic-p full-faithfulness obstacle; its1999 erratum changes the semistable definition. Published SGA9.7 and14.1.12 still retain the integrality and sign questions on which this search did not establish a precise modern answer.
6. Horel, Ekedahl, Toën, Mandell and Bachmann–Burklund require different algebraic structures and space hypotheses. None is silently identified with the manuscript coefficient/coPD construction; ordinary cohomology alone is never substituted for the enhanced model.

## Saved search and opening batches


### MID-S01

Purpose: SGA IX donor claims, mixed extensions and monodromy; title/section searches and bibliography leads.

Evidence file: `research/middle_search_01.json`. SHA-256: `ce97d68050181f3b812c485faa8dd351b718ccd6b5616befaad566a4ef193e76`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://iut-theory.org/divers/SGA7I.pdf
- https://grothendiecksga.com/read/sga7/fr/9-9.html
- https://grothendiecksga.com/read/sga7/en/9-9.html
- https://grothendiecksga.com/read/sga7/fr/
- https://web.math.princeton.edu/~gyujino/abschZ.pdf
- https://grothendiecksga.com/read/sga7/en/9-sommaire.html
- https://link.springer.com/book/10.1007/BFb0068688
- https://math.stanford.edu/~conrad/mordellsem/Notes/L10.pdf
- https://grothendiecksga.com/read/sga7/fr/9-sommaire.html
- https://grothendiecksga.com/read/sga7/fr/9-0.html
- https://www.sci.kanagawa-u.ac.jp/math-phys/yozeki/pdf/HKF200528.pdf
- https://books.google.com/books/about/Groupes_de_Monodromie_en_G%C3%A9om%C3%A9trie_Alg.html?id=beFUAAAAYAAJ
- https://www.ams.org/books/mmono/245/mmono245-endmatter.pdf
- https://stacks.math.columbia.edu/bibliography/SGA7-I
- https://math.nyu.edu/~tschinke/books/finite-fields/submitted/oort.pdf
- https://grothendiecksga.com/read/sga7/fr/7-0.html
- https://books.google.com/books/about/Groupes_de_Monodromie_en_G%C3%A9om%C3%A9trie_Alg.html?id=ekMmzwEACAAJ
- https://www.mathnet.ru/links/aa282e4637f8625defe4cefd7c7a274b/im_9481_refs_eng.htm
- https://grothendiecksga.com/read/sga7/en/9-10.html
- https://csg.igrothendieck.org/published-works/
- https://doi.org/10.1007/s00029-021-00669-8
- https://fr.wikipedia.org/wiki/S%C3%A9minaire_de_g%C3%A9om%C3%A9trie_alg%C3%A9brique_du_Bois_Marie
- https://www.researchgate.net/publication/46712651_Abelian_varieties_over_finite_fields
- https://www.scribd.com/document/785040358/978-88-7642-515-8
- https://www.scribd.com/document/873227060/AGRoots-final
- https://mathoverflow.net/questions/191643/the-generic-fiber-pullback-for-p-divisible-groups-in-characteristic-p
- https://www.scribd.com/document/953256402/05-oort
- https://portal.mardi4nfdi.de/wiki/Item%3AQ1273298
- https://www.academia.edu/101303573/Did_earlier_thoughts_inspire_Grothendieck
- https://www.academia.edu/88106988/Crystalline_Dieudonn%C3%A9_theory_over_excellent_schemes
- https://www.math.columbia.edu/~chaoli/docs/AbelianVarieties.html
- https://www.academia.edu/129561839/Crystalline_Dieudonn%C3%A9_theory_over_excellent_schemes
- https://doczz.net/doc/8013079/moduli-of-abelian-varieties-and-p-divisible-groups
- https://en.wikipedia.org/wiki/S%C3%A9minaire_de_G%C3%A9om%C3%A9trie_Alg%C3%A9brique_du_Bois_Marie
- https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.70146
- https://numdam.org/articles/10.5802/afst.1667/
- https://www.researchgate.net/publication/265332163_A_Rigid_Analytic_Gross-Zagier_Formula_and_Arithmetic_Applications
- https://www.academia.edu/77369442/A_Rigid_Analytic_Gross_Zagier_Formula_and_Arithmetic_Applications
- https://arxiv.org/abs/2609.11106
- https://www.degruyterbrill.com/document/doi/10.1515/crelle-2023-0031/html
- https://arxiv.org/abs/2611.17685


### MID-S02

Purpose: Equal-characteristic Tate full faithfulness, de Jong and bibliographic databases including zbMATH leads.

Evidence file: `research/middle_search_02.json`. SHA-256: `74988e5ad17d748830c98ca1f9196499531723e1f208bed28a12013ad02a14fd`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://www.math.columbia.edu/~dejong/
- https://portal.mardi4nfdi.de/wiki/Item%3AQ1273298
- https://doi.org/10.1007/s002220050266
- https://www2.math.upenn.edu/~chai/papers_pdf/fam_ord_av.pdf
- https://www2.math.upenn.edu/~chai/papers_pdf/survey02.pdf
- https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n3-p02-p.pdf


### MID-S03

Purpose: Graded divided powers, free algebra and Koszul hypotheses in Stacks; standard PD conventions.

Evidence file: `research/middle_web_003.json`. SHA-256: `f9c4fcad8ac2a306bd51756e0f376571fd40038e10945799f1a85bf0e9f8cec8`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://www.math.columbia.edu/~dejong/
- https://www.math.columbia.edu/~dejong/
- https://stacks.math.columbia.edu/tag/09PF
- https://stacks.math.columbia.edu/tag/09PF
- https://stacks.math.columbia.edu/tag/062D
- https://stacks.math.columbia.edu/tag/062D
- https://stacks.math.columbia.edu/tag/0656
- https://stacks.math.columbia.edu/tag/0656


### MID-S04

Purpose: Dold–Puppe derived nonadditive functors; Stoia Gorenstein title and Numdam discovery.

Evidence file: `research/middle_web_004.json`. SHA-256: `8260e6db214825c96ae5a1343889baacdac3038c0ad4afd86dd35e0fcfe1f68e`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://stacks.math.columbia.edu/tag/0C02
- https://stacks.math.columbia.edu/tag/0E19
- https://stacks.math.columbia.edu/tag/0C04
- https://stacks.math.columbia.edu/tag/0C09
- https://stacks.math.columbia.edu/tag/0C12
- https://stacks.math.columbia.edu/download/duality.pdf
- https://www.numdam.org/about/
- https://articles.math.cas.cz/10.21136/MB.2025.0110-24
- https://ncatlab.org/nlab/show/divided%2Bpower%2Balgebra
- https://stacks.math.columbia.edu/tag/07HZ
- https://openmaths.org/courses/cotangent-complexes-and-deformations-in-ringed-topoi/providers.html
- https://link.springer.com/article/10.1007/s00209-025-03681-2
- https://www.scribd.com/document/817534721/Derived-functors-of-the-divided-power-functors


### MID-S05

Purpose: Stoia/Gorenstein backward bibliography search and Numdam source checks.

Evidence file: `research/middle_web_005.json`. SHA-256: `a9529991a4cb2c773efe4936ec832cda8566bbc124a57bda3fa7844eaf5e343e`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://arxiv.org/abs/1312.5676
- https://arxiv.gg/abs/1312.5676
- https://portal.mardi4nfdi.de/wiki/Item%3AQ1273298
- https://www.math.univ-paris13.fr/~breen/
- https://pith.science/paper/1312.5676
- https://pith.science/paper/E3RMW4KG
- https://citeseerx.ist.psu.edu/document?doi=712b9e8ea8a54531ba502d03ef3fa06600d9cb79&repid=rep1&type=pdf
- https://arxiv.gg/author/Antoine%20Touz%C3%A9
- https://www.math.ens.psl.eu/~charles/these.pdf
- https://dokumen.pub/collected-works-of-john-tate-1951-1975-part-1-0821890921-9780821890929.html
- https://www.researchgate.net/publication/259367935_Derived_functors_of_the_divided_power_functors
- https://scirate.com/search?q=au%3ATouze_A+in%3Amath
- https://scirate.com/search?q=au%3AMikhailov_R+in%3Amath
- https://scirate.com/search?q=au%3ABreen_L+in%3Amath
- https://citeseerx.ist.psu.edu/document?doi=a26c9d9a52f9c8875c0fb7c2d5e5a86c44f183a8&repid=rep1&type=pdf
- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/82C52B04B1E877FB5E093A106B538DF4/S0010437X09004242a.pdf/tate_modules_of_universal_pdivisible_groups.pdf
- https://msp.org/gt/2016/20-1/gt-v20-n1-p04-p.pdf
- https://pureportal.spbu.ru/en/publications/derived-functors-of-the-divided-power-functors%28e7fb8e08-46a4-481b-b519-1a14c004f2d8%29.html
- https://msp.org/gt/2016/20-1/gt-v20-n1-p04-s.pdf
- https://scispace.com/papers/derived-functors-of-the-divided-power-functors-31nw1sa49c
- https://link.springer.com/article/10.1007/s00029-021-00669-8
- https://pureportal.spbu.ru/ru/publications/derived-functors-of-the-divided-power-functors%28e7fb8e08-46a4-481b-b519-1a14c004f2d8%29.html
- https://cv.hal.science/antoine-touze
- https://doi.org/10.1007/s00029-021-00669-8
- https://www.researchgate.net/publication/45887837_Stratifications_of_Newton_polygon_strata_and_Traverso%27s_conjectures_for_p-divisible_groups
- https://www.math.columbia.edu/~dejong/
- https://stacks.math.columbia.edu/tag/0C09
- https://stacks.math.columbia.edu/tag/0C09
- https://stacks.math.columbia.edu/tag/07HZ
- https://stacks.math.columbia.edu/tag/07HZ


### MID-S06

Purpose: Breen–Mikhailov–Touzé original derived-power paper and de Jong author bibliography.

Evidence file: `research/middle_web_006.json`. SHA-256: `a8e59ece2bc36f7adf81ab3d50f7cc5b3ebad4125ec13e14a6114dec59e18e45`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://www.math.columbia.edu/~dejong/
- https://www.math.columbia.edu/~dejong/
- https://msp.org/gt/2016/20-1/gt-v20-n1-p04-p.pdf
- https://msp.org/gt/2016/20-1/gt-v20-n1-p04-p.pdf
- https://arxiv.org/abs/1312.5676
- https://arxiv.org/abs/1312.5676
- https://doi.org/10.48550/arXiv.1312.5676†doi.org】


### MID-S07

Purpose: Original published SGA7 I access and donor section comparison.

Evidence file: `research/middle_web_007.json`. SHA-256: `b4aaa52ab90199df796ecdd0aae352aa4d9a1466d65ecd57b1485348d79f5844`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://www.math.columbia.edu/~dejong/papers/TATE.dvi:
- https://www.math.columbia.edu/~dejong/papers/ErratumTate.dvi:
- https://msp.org/gt/2016/20-1/gt-v20-n1-p04-p.pdf


### MID-S08

Purpose: Grothendieck/Cartan generalized de Rham comparison, uniqueness and weighted hypotheses.

Evidence file: `research/middle_web_008.json`. SHA-256: `22b3bbad53d9ae2248551c9a5ac768dfe5eecbfe4aee06ada22623db92ca151d`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://doi.org/10.1007/BF02684807
- https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/deRham.pdf
- http://www.numdam.org/item?id=PMIHES_1966__29__95_0
- http://www
- http://www.numdam.org/legal.php
- https://repo-archives.ihes.fr/FONDS_IHES/F_Communication/F3_Rapports_Scientifiques_Annuels/F3_1_1958_1968/F3_1_3_1967/F3_1_3_1/F3_1_3_1_2/F3_1_3_1_2.pdf
- https://csg.igrothendieck.org/published-works/
- https://csg.igrothendieck.org/unpublished-works/
- https://dokumen.pub/enriques-surfaces-i.html
- https://comptes-rendus.academie-sciences.fr/mathematique/articles/10.5802/crmath.764/
- https://shizhang.li/papers/Comparing_pris_and_crys.pdf
- https://openmaths.org/courses/cotangent-complexes-and-deformations-in-ringed-topoi/the-derived-de-rham-complex.html
- https://webusers.imj-prg.fr/~max.karoubi/KL.livre/Bibliographie.Index.pdf
- https://www.numdam.org/issues/AST_1987__149__1_0/
- https://numdam.org/issues/SB_1964-1966__9_/
- https://fr.scribd.com/document/720518649/GrothendieckTohokuPaperTohoku-Mathematical-Journal-Vol-9-Issue-2-Jan-1957-Pg-s-119-221


### MID-S09

Purpose: Cartier, the four differential complexes, Euler contraction and simplex integration.

Evidence file: `research/middle_web_009.json`. SHA-256: `3bde710bc3b41c15e272078ace1e4fcc595d7d4505c41b16184a0ac7b5984988`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://grothendiecksga.com/read/sga7/en/9-9.html
- https://ems.press/content/serial-article-files/46411
- https://smf.emath.fr/system/files/filepdf/smf_ast_424.pdf
- https://escholarship.org/uc/item/1rv1t97k
- https://math.mit.edu/research/highschool/primes/materials/2022/Devalapurkar-Misterka.pdf
- https://people.math.harvard.edu/~lurie/papers/Crystalline.pdf
- https://guests.mpim-bonn.mpg.de/ferdinand/q-Witt.pdf
- https://kskedlaya.org/prismatic/sec_derived-deRham.html
- https://www.math.columbia.edu/~chaoli/doc/BhattEilenberg.html
- https://doi.org/10.4213/sm10214e
- https://openmaths.org/courses/cotangent-complexes-and-deformations-in-ringed-topoi/derived-de-rham-complexes-in-characteristic-p.html
- https://hub.valency.io/works/W_anctf5w6
- https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/syntomic-complexes-and-padic-etale-tate-twists/5CEB0663B118E5CB3C2F16BD9C17CFB0
- https://www.mathnet.ru/php/archive.phtml?jrnid=sm&option_lang=eng&paperid=10214&wshow=paper
- https://www.scribd.com/document/774815319/Crystalline-cohomology-of-algebraic-stacks-and-Hyodo-Kato-cohomology-Olsson
- https://kskedlaya.org/prismatic/sec_hodge-tate-crystalline.html
- https://www.researchgate.net/publication/369924551_Generalized_n-series_and_de_Rham_complexes
- https://www.researchgate.net/publication/381274852_Intersection_de_Rham_complexes_in_positive_characteristic
- https://paperzz.com/doc/7404361/homological-methods-in-non-commutative-geometry
- https://abel.math.harvard.edu/~elkies/M223.24/index.html
- https://noncommutativegeometry.blogspot.com/2008/
- https://www.academia.edu/164973135/The_3x_1_Problem_Algebraic_Reduction_of_Macro_cycles_via_Local_Polynomials_and_Diophantine_Balance
- https://springerlink.fh-diploma.de/article/10.1007/s10208-020-09464-x
- https://doi.org/10.1017/prm.2025.7
- https://msp.org/gt/2016/20-1/gt-v20-n1-p04-p.pdf
- https://stacks.math.columbia.edu/tag/00HT
- https://stacks.math.columbia.edu/tag/00HT


### MID-S10

Purpose: de Jong publication/author source, full faithfulness and reduction criteria.

Evidence file: `research/middle_web_010.json`. SHA-256: `ea1c7260cdd81ee317857c4de80c9292713379efa4d277a5908a2394aecf75cf`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://link.springer.com/article/10.1007/s002220050266
- https://link.springer.com/article/10.1007/s002220050266
- https://doi.org/10.1007/s002220050266
- https://link.springer.com/content/pdf/10.1007/s002220050266.pdf
- https://link.springer.com/article/10.1007/s002220050266;
- https://www.math.columbia.edu/~dejong/papers/TATE.pdf


### MID-S11

Purpose: Potential-semista­ble monodromy integrality/sign questions; Coleman and Stoia leads.

Evidence file: `research/middle_web_011.json`. SHA-256: `dc4c9db59ab8d46e4bb6663c687e3a4a7c1bf4a1eca63d1a1495a66c386e7d80`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://grothendiecksga.com/read/sga7/en/9-10.html
- https://www.intlpress.com/site/pub/files/_fulltext/journals/ajm/2000/0004/0002/AJM-2000-0004-0002-a002.pdf
- https://link.springer.com/article/10.1007/s00208-021-02319-y
- https://link.springer.com/book/10.1007/978-3-319-27371-6
- https://books.google.com/books/about/Degeneration_of_Abelian_Varieties.html?hl=en&id=NkuxvgEACAAJ&output=html_text
- https://imar.ro/~increst/1979/31_1979.pdf
- https://www.sciencedirect.com/science/article/abs/pii/S0021869321005330
- https://books.google.com/books/about/Degeneration_of_Abelian_Varieties.html?id=qJr6CAAAQBAJ


### MID-S12

Purpose: Stoia original-note search, exact title and 1979 follow-back bibliography.

Evidence file: `research/middle_web_012.json`. SHA-256: `01cb2743c5ac72c3bd8e6e8eab739f9ef35fdb8c7222c4b3e26ac884cb7f33e7`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://imar.ro/~increst/1979/31_1979.pdf
- https://imar.ro/~increst/1979/31_1979.pdf
- https://www.intlpress.com/site/pub/files/_fulltext/journals/ajm/2000/0004/0002/AJM-2000-0004-0002-a002.pdf
- https://www.intlpress.com/site/pub/files/_fulltext/journals/ajm/2000/0004/0002/AJM-2000-0004-0002-a002.pdf:


### MID-S13

Purpose: Bănică–Stoia, Stacks Gorenstein openness, de Jong and monodromy publication matches.

Evidence file: `research/middle_web_013.json`. SHA-256: `609facebdfa6e7b301e4628fcd46c428a22ed4260279c75055a0eac806b51eba`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://www.intlpress.com/site/pub/files/_fulltext/journals/ajm/2000/0004/0002/AJM-2000-0004-0002-a002.pdf
- https://www.ams.org/notices/199905/urbana-prog.pdf
- https://citeseerx.ist.psu.edu/document?doi=58b9eddcd29b0e86bd8b95607830c28eaa4a1ed3&repid=rep1&type=pdf
- http://math.berkeley.edu/˜coleman/
- https://archive.numdam.org/item/AST_2010__331__179_0/
- https://archive.numdam.org/articles/10.5802/aif.1599/?source=MSMF_1980_2_4__1_0
- https://portal.mardi4nfdi.de/wiki/Item%3AQ1273298
- https://doi.org/10.1007/s002220050266
- https://www.jmilne.org/math/Books/ADTnot.pdf
- https://imar.ro/~increst/1979/31_1979.pdf


### MID-S14

Purpose: Completed PD categories, representability, localization and unresolved uniqueness/fraction formulations.

Evidence file: `research/middle_web_014.json`. SHA-256: `01f39e11c2b24e268cde93e38db1135578a82a92779c2ad5fd31ed782cb9344c`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://www.math.u-bordeaux.fr/~obrinon/enseignement/cl/cris.pdf
- https://gtbac.telecom-paristech.fr/slides/13xxxxplut.pdf
- https://webusers.imj-prg.fr/~antoine.chambert-loir/exposes/cdf-20250602.pdf
- https://www.scribd.com/document/870880816/PMIHES-1975-45-5-0
- https://doi.org/10.1007/BF02684807
- https://pure.mpg.de/rest/items/item_3239036_2/component/file_3450875/content
- https://openmaths.org/courses/cotangent-complexes-and-deformations-in-ringed-topoi/cohomology-of-flat-formal-categories-with-divided-powers.html
- https://mathoverflow.net/questions/1151/sheaf-cohomology-and-injective-resolutions/1210


### MID-S15

Purpose: Cartier/author bibliographies and integration normalization; direct calculations are separately logged.

Evidence file: `research/middle_web_015.json`. SHA-256: `9a6a11777e80ae12d5415646bda977e8c2c4bc555d1f118cf44366a77df0e1d9`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://www.ihes.fr/~/cartier/REFERENCES/publications.html
- https://mathshistory.st-andrews.ac.uk/Biographies/Cartier/
- https://www.numdam.org/item/10.24033/bsmf.1503.pdf
- https://numdam.org/book-part/SB_1956-1958__4__379_0/
- https://doi.org/10.1090/noti3140
- https://archive.numdam.org/item/SB_1998-1999__41__245_0/
- https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/hodge-ams.pdf
- https://ems.press/content/serial-article-files/32957
- https://archive.numdam.org/item/MSMF_2000_2_81__1_0/?source=AIF_1997__47_1_69_0
- https://www.williamstein.org/people/berthelo/publis/Intro._theo._D-mod._arith.pdf
- https://www.imo.universite-paris-saclay.fr/~david.harari/articles/revisobs.pdf
- https://numdam.org/item/SB_1956-1958__4__379_0.pdf
- https://archive.numdam.org/articles/10.24033/asens.1175/?source=SB_1961-1962__7__297_0
- https://www.numdam.org/book-part/SB_1998-1999__41__245_0/
- https://www.numdam.org/item/?id=BSMF_1958__86__177_0
- https://archive.numdam.org/book-part/SB_1986-1987__29__67_0/
- https://www.numdam.org/book-part/AST_2002__279__1_0/
- https://archive.numdam.org/item/SB_1986-1987__29__67_0/
- https://en.wikipedia.org/wiki/Cartier_isomorphism
- https://link.springer.com/article/10.1007/s00039-022-00597-5
- https://www.sciencedirect.com/science/article/abs/pii/S0747717121000420
- https://www.academia.edu/144935565/Facult%C3%A9_des_Sciences_de_Luminy
- https://www.academia.edu/103776692/The_Casas_Alvero_conjecture_for_infinitely_many_degrees
- https://github.com/royvanrijn/jacobian-research/blob/main/extended-geometry/POSITIVE_CHARACTERISTIC_DEFORMATION_LANDSCAPE.md
- https://www.researchgate.net/publication/260039387_Faster_Algorithms_for_Multivariate_Interpolation_With_Multiplicities_and_Simultaneous_Polynomial_Approximations
- https://ashvin-swaminathan.github.io/home/research.html
- https://doczz.net/doc/8846342/applications-of-polynomials-over-finite-fields
- https://www.academia.edu/86748153/Joints_formed_by_lines_and_a_k_plane_and_a_discrete_estimate_of_Kakeya_type
- https://www.academia.edu/164973135/The_3x_1_Problem_Algebraic_Reduction_of_Macro_cycles_via_Local_Polynomials_and_Diophantine_Balance
- https://dlmf.nist.gov/5.14
- https://dlmf.nist.gov/5.14
- http://dlmf.nist.gov/5.14】
- http://dlmf.nist.gov/5.14.E1】
- http://dlmf.nist.gov/5.14.E2】
- http://dlmf.nist.gov/5.14.E3】
- http://dlmf.nist.gov/5.14.E4】
- https://numdam.org/item/PMIHES_1977__47__269_0/
- https://numdam.org/item/PMIHES_1977__47__269_0/
- https://numdam.org/articles/10.1007/BF02684341/}
- https://numdam.org/articles/10.1007/BF02684341/


### MID-S16

Purpose: Sullivan minimal models and Cartier publication bibliography.

Evidence file: `research/middle_web_016.json`. SHA-256: `ea27d54c8a6767a44e3a57a87fec88de5ae19a6b0363a1834f418eec0c580713`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://numdam.org/item/PMIHES_1977__47__269_0.pdf
- https://numdam.org/item/PMIHES_1977__47__269_0.pdf
- http://www.numdam.org/item?id=PMIHES_1977__47__269_0
- http://www.numdam.org/conditions
- http://www.numdam.org/INFINITESIMAL
- https://www.ihes.fr/~/cartier/REFERENCES/publications.html
- https://www.ihes.fr/~/cartier/REFERENCES/publications.html
- https://zbmath.org/?q=an%3A0929.14029
- https://zbmath.org/?q=an%3A0929.14029:
- https://mathoverflow.net/questions/191643/the-generic-fiber-pullback-for-p-divisible-groups-in-characteristic-p
- https://mathoverflow.net/questions/191643/the-generic-fiber-pullback-for-p-divisible-groups-in-characteristic-p


### MID-S17

Purpose: BMT exact derived-power/Koszul discussion and Cartier comparison scope.

Evidence file: `research/middle_web_017.json`. SHA-256: `7aa0e1cd43b494a4e2eb5fe218e87c591ac7b13fec7988609c6a5006537db584`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://www.intlpress.com/site/pub/files/_fulltext/journals/ajm/2000/0004/0002/AJM-2000-0004-0002-a002.pdf
- https://mathoverflow.net/questions/481078/weil-pairing-for-an-abelian-variety-uniformized-as-torus-modulo-lattice-over-a-n?r=31
- https://archive.numdam.org/item/AST_2010__331__179_0/
- https://www.math.columbia.edu/~chaoli/doc/BhattEilenberg.html
- https://openmaths.org/courses/AG-CA/tor-and-flat-modules.html
- https://ncatlab.org/nlab/show/Lazard%27s%2Bcriterion
- https://www.sciencedirect.com/science/article/pii/S0022314X04002537/pdf
- https://www.research.unipd.it/handle/11577/153322?mode=complete
- https://dx.doi.org/10.1215/S0012-7094-99-09708-9
- https://ftp.math.utah.edu/pub/tex/bib/toc/lnm1980.html
- https://staging1.eurekamag.com/research/075/482/


### MID-S18

Purpose: Lazard theorem in Stacks058G, with flat-module reduction hypotheses.

Evidence file: `research/middle_web_018.json`. SHA-256: `ef1e6731b5a12616229f2a0d8b6592aa8b457ed3a9fa854251a2d231c68e1bd9`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://www.math.columbia.edu/~chaoli/docs/MumfordCurves.html
- http://www.math.psu.edu/papikian/Research/RAU.pdf
- https://toc.library.ethz.ch/objects/pdf03/e01_978-1-4704-1021-6_01.pdf
- https://doi.org/10.1090/CONM/605
- https://doi.org/10.1090/conm/605
- https://sites.google.com/view/mpapikian/research
- https://www.intlpress.com/site/pub/files/_fulltext/journals/ajm/2000/0004/0002/AJM-2000-0004-0002-a002.pdf
- https://grothendiecksga.com/read/sga7/en/9-10.html
- https://www.sciencedirect.com/science/article/pii/S0022314X04002537/pdf
- https://www.scribd.com/document/853648950/Tropical-and-Non-Archimedean-Geometry
- https://stacks.math.columbia.edu/tag/058G
- https://stacks.math.columbia.edu/tag/058G


### MID-S19

Purpose: Sullivan Theorems8.1 and10.1; monodromy exposition lead used only within checked scope.

Evidence file: `research/middle_web_019.json`. SHA-256: `d133c998823f6d1f45af057259ef586ea15f5979ef1c87c2eb1bcd46f8f8382f`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://www.math.psu.edu/papikian/Research/RAU.pdf
- https://numdam.org/item/PMIHES_1977__47__269_0.pdf
- https://numdam.org/item/PMIHES_1977__47__269_0.pdf


### MID-S20

Purpose: Sullivan rational/nonnilpotent distinction and exact theorem passages; follow-back references.

Evidence file: `research/middle_web_020.json`. SHA-256: `4c1cd299effc2d731a1a544968a1e0d1e5d0d240fd85d03fd0b6b3e09cadd814`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://sites.google.com/view/mpapikian/research
- https://sites.google.com/view/mpapikian/research
- https://numdam.org/item/PMIHES_1977__47__269_0.pdf
- https://numdam.org/item/PMIHES_1977__47__269_0.pdf


### MID-S21

Purpose: Cenkl1989 original, §5 hypotheses and obstruction to a natural commutative cochain model.

Evidence file: `research/middle_web_021.json`. SHA-256: `e01b496194e3a946c8dc1864a0887a64c4ddfe76f388428f4e0290235c48afae`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://msp.org/pjm/1989/140-1/pjm-v140-n1-p02-p.pdf
- https://msp.org/pjm/1989/140-1/pjm-v140-n1-p02-p.pdf
- https://drive.google.com/file/d/1rjRd-ufg5HfHvtHZ_euBJVyoEwJVpkrj/view?usp=drive_link


### MID-S22

Purpose: Horel, Ekedahl and Toën exact enhanced-model statements and their hypotheses.

Evidence file: `research/middle_web_022.json`. SHA-256: `5021074da4da3d42d07d811b5c6a65f4b100e9b5e5f967d2687b5ca5fefc078e`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://geoffroy.horel.org/binomial.pdf
- https://geoffroy.horel.org/binomial.pdf
- https://arxiv.org/pdf/math/0107004
- https://arxiv.org/pdf/math/0107004
- https://epiga.episciences.org/6060/pdf
- https://epiga.episciences.org/6060/pdf
- http://creativecommons.org/licenses/by-sa/4.0/


### MID-S23

Purpose: Dwyer tame homotopy, Cenkl–Porter cubical forms and exact coefficient-system queries.

Evidence file: `research/middle_web_023.json`. SHA-256: `0aad7245e0fe161125eb039ccc5ba392c02475d0d91e3f12a1be753194bdf676`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://archive.numdam.org/item/AST_1990__45__1_0/?source=AST_1984__113-114__96_0
- https://infoscience.epfl.ch/record/295971/files/EPFL_TH9066.pdf
- https://www.researchgate.net/publication/408302647_On_the_l-adic_homotopy_type_of_configuration_spaces
- https://mat.uab.es/pubmat/fitxers/download/FileType%3Apdf/FolderName%3Av35%282%29/FileName%3A35291_05.pdf
- https://www.numdam.org/item/AST_1990__45__1_0.pdf
- https://msp.org/pjm/1984/112-1/pjm-v112-n1-p03-s.pdf
- https://www.researchgate.net/publication/38341994_De_Rham_theorem_with_cubical_forms
- https://link.springer.com/book/10.1007/BFb0068706
- https://scispace.com/journals/topology-13mwfv7x/1979
- https://studyres.com/doc/530541/homotopy-theories-and-model-categories
- https://arxiv.org/pdf/math/0107004
- https://arxiv.org/pdf/math/0107004
- https://epiga.episciences.org/6060/pdf
- https://epiga.episciences.org/6060/pdf


### MID-S24

Purpose: Dwyer DOI access failure; Cenkl–Porter access; Toën/Ekedahl exact bounds.

Evidence file: `research/middle_web_024.json`. SHA-256: `e117f5fe9a771f3e6293907f6bfadd78da6b33ec2a387cff9b4460da8156dab6`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://doi.org/10.1016/0040-9383(79)90023-5
- https://doi.org/10.1016/0040-9383%2879%2990023-5
- https://msp.org/pjm/1984/112-1/pjm-v112-n1-p04-p.pdf
- https://epiga.episciences.org/6060/pdf
- https://epiga.episciences.org/6060/pdf
- https://arxiv.org/pdf/math/0107004
- https://arxiv.org/pdf/math/0107004


### MID-S25

Purpose: Scheerer–Tanré primary exposition found by backward references; original Dwyer sought.

Evidence file: `research/middle_web_025.json`. SHA-256: `7bb72bd93e1db359c49ed46394afed3cd11f2eb280e02be99ddd5763f9caf10c`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://msp.org/pjm/1984/112-1/pjm-v112-n1-p05-s.pdf
- https://mat.uab.es/pubmat/fitxers/download/FileType%3Apdf/FolderName%3Av35%282%29/FileName%3A35291_05.pdf
- https://math.nd.edu/people/faculty/william-dwyer/
- https://pepite-depot.univ-lille.fr/LIBRE/Th_Num/1990/55376-1990-3.pdf
- https://ncatlab.org/nlab/files/DwyerSpalinski_HomotopyTheories.pdf
- https://archive.numdam.org/item/AST_1990__45__1_0/?source=AST_1984__113-114__96_0
- https://numdam.org/item/AST_1990__45__1_0/
- https://geodesic.mathdoc.fr/book-part/AST_1990__191__15_0/
- https://msp.org/index/ail.php?jpath=pjm&l=C
- https://www.researchgate.net/publication/46583113_The_homotopy_theory_of_function_spaces_a_survey
- https://www.numdam.org/item/AST_1984__113-114__173_0/
- https://www.academia.edu/76864978/The_homotopy_theory_of_function_spaces_a_survey
- https://geodesic.mathdoc.fr/item/AST_1990__45__1_0/
- https://geodesic.mathdoc.fr/item/AST_1984__113-114__173_0/
- https://studyres.com/doc/530541/homotopy-theories-and-model-categories
- https://research.com/u/william-g-dwyer
- https://en.wikipedia.org/wiki/William_Gerard_Dwyer
- https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/lusternikschnirelmann-category-and-algebraic-rlocal-homotopy-theory/A4D55A7AA0FC8AB41618FDABAB992BF9
- https://academic.oup.com/jtopol/article-abstract/8/2/377/993487
- http://personal.us.es/fmuro
- https://pro.univ-lille.fr/daniel-tanre/publications
- https://ncatlab.org/nlab/show/William%2BDwyer
- https://www.researchgate.net/publication/225146117_The_tame_homotopy_groups_of_a_suspension
- https://www.rankless.org/authors/w-g-dwyer
- https://ncatlab.org/nlab/show/William%20Dwyer
- https://www.researchgate.net/profile/W-Dwyer
- https://www.math.univ-toulouse.fr/~dcisinsk/publications.html
- https://www.haoqingwu.com/research
- https://cisinski.app.uni-regensburg.de/publikationen.html
- https://doi.org/10.1112/jtopol/jtu029
- https://msp.org/index/ai.php?jpath=pjm
- https://de.wikipedia.org/wiki/William_G._Dwyer
- https://en.wikipedia.org/wiki/Julie_Bergner
- https://pt.wikipedia.org/wiki/William_Gerard_Dwyer
- https://en.wikipedia.org/wiki/Homotopy_category
- https://en.wikipedia.org/wiki/Homotopy_theory
- https://www.sciencedirect.com/science/article/pii/0040938379900235
- https://www.sciencedirect.com/science/article/pii/0040938379900235:


### MID-S26

Purpose: Garvín and Richter–Sagave searches; Scheerer–Tanré and Mandell cochain multiplications.

Evidence file: `research/middle_web_026.json`. SHA-256: `2652c9c2cc152c5be3408ef6d8ec8a213b719d9bdabef6e80cde7cd8341edfcc`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4076D51EAAD865E63F13B718B6026074/S0010437X20007319a.pdf/strictly_commutative_model_for_the_cochain_algebra_of_a_space.pdf
- https://doi.org/10.1112/S0010437X20007319
- https://www.cambridge.org/core/journals/compositio-mathematica/article/strictly-commutative-model-for-the-cochain-algebra-of-a-space/4076D51EAAD865E63F13B718B6026074
- https://www.math.uni-hamburg.de/home/richter/mfo-einftyoperadsichains.pdf
- https://www.cambridge.org/core/journals/compositio-mathematica/volume/D8DB9036FE962708A6F7B6E527C7720E?pageNum=4
- https://www.researchgate.net/publication/265549276_An_extension_of_Miller%27s_version_of_the_de_Rham_Theorem_with_any_coefficients
- https://www.cambridge.org/core/search?filters%5Bkeywords%5D=55P62
- https://www.math.ru.nl/~sagave/
- https://www.cambridge.org/core/journals/compositio-mathematica/listing?pageNum=28
- https://www.cambridge.org/core/browse-subjects/mathematics/msc-classifications/msc-2010-category-theory-homological-algebra/18xxx?pageNum=7
- https://www.cambridge.org/core/search?filters%5BclassificationCodesByType%5D=MSC%3B18D50%3BOperads
- https://www.cambridge.org/core/search?filters%5Bkeywords%5D=16E45
- https://www.cambridge.org/core/search?filters%5Bkeywords%5D=16e45
- https://www.cambridge.org/core/browse-subjects/mathematics/msc-classifications/msc-2010-associative-rings-and-algebras/16exx?pageNum=3
- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4076D51EAAD865E63F13B718B6026074/S0010437X20007319a.pdf/div-class-title-a-strictly-commutative-model-for-the-cochain-algebra-of-a-space-div.pdf
- https://portal.mardi4nfdi.de/wiki/A_strictly_commutative_model_for_the_cochain_algebra_of_a_space
- https://www.impan.pl/en/publishing-house/banach-center-publications/all/45
- https://www.mpim-bonn.mpg.de/de/node/7992
- https://www.impan.pl/pl/wydawnictwa/banach-center-publications/all/45
- https://www.math-conf.uni-osnabrueck.de/wp-content/uploads/2018/08/Sagave_abstract.pdf
- https://arxiv.org/abs/1801.01060
- https://www.math.uni-hamburg.de/home/richter/comonoidsichains.pdf
- https://mat.uab.es/pubmat/fitxers/download/FileType%3Apdf/FolderName%3Av35%282%29/FileName%3A35291_05.pdf
- https://mat.uab.es/pubmat/fitxers/download/FileType:pdf/FolderName:v35(2)/FileName:35291_05.pdf
- https://mat.uab.es/pubmat/fitxers/download/FileType:pdf/FolderName:v35(2)/FileName:35291_05.pdf;
- https://mat.uab.es/pubmat/fitxers/download/FileType:pdf/FolderName:v35(2)/FileName:35291_05.pdf
- https://msp.org/index/ail.php?jpath=pjm&l=C
- https://msp.org/index/ail.php?jpath=pjm&l=C
- https://webhomes.maths.ed.ac.uk/~v1ranick/papers/mandell.pdf
- https://webhomes.maths.ed.ac.uk/~v1ranick/papers/mandell.pdf


### MID-S27

Purpose: Mandell2002 exact Main/Uniqueness statements; Richter–Sagave and Cenkl–Porter source discovery.

Evidence file: `research/middle_web_027.json`. SHA-256: `706fcd2995a578f4f7f9f6a16abdca75e8ee4e3eca8938b3c712bb947271f712`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://webhomes.maths.ed.ac.uk/~v1ranick/papers/mandell.pdf
- https://webhomes.maths.ed.ac.uk/~v1ranick/papers/mandell.pdf
- https://mat.uab.es/pubmat/fitxers/download/FileType%3Apdf/FolderName%3Av35%282%29/FileName%3A35291_05.pdf
- https://mat.uab.es/pubmat/fitxers/download/FileType:pdf/FolderName:v35(2)/FileName:35291_05.pdf
- https://mat.uab.es/pubmat/fitxers/download/FileType:pdf/FolderName:v35(2)/FileName:35291_05.pdf
- https://mat.uab.es/pubmat/fitxers/download/FileType:pdf/FolderName:v35(2)/FileName:35291_05.pdf;
- https://www.impan.pl/en/publishing-house/banach-center-publications/all/45
- https://www.impan.pl/en/publishing-house/banach-center-publications/all/45
- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4076D51EAAD865E63F13B718B6026074/S0010437X20007319a.pdf/strictly_commutative_model_for_the_cochain_algebra_of_a_space.pdf
- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4076D51EAAD865E63F13B718B6026074/S0010437X20007319a.pdf/strictly_commutative_model_for_the_cochain_algebra_of_a_space.pdf
- https://doi.org/10.1112/S0010437X20007319
- http://creativecommons.org/licenses/by/4.0/


### MID-S28

Purpose: Mandell2002 uniqueness and Richter–Sagave diagram-category theorem boundaries.

Evidence file: `research/middle_web_028.json`. SHA-256: `9518f4f5f205027e34aa425a611fabc7fa4f0db17855f1de62429ba0e4908d90`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://webhomes.maths.ed.ac.uk/~v1ranick/papers/mandell.pdf
- https://webhomes.maths.ed.ac.uk/~v1ranick/papers/mandell.pdf
- https://www.impan.pl/en/publishing-house/banach-center-publications/all/45
- https://www.impan.pl/en/publishing-house/banach-center-publications/all/45
- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4076D51EAAD865E63F13B718B6026074/S0010437X20007319a.pdf/strictly_commutative_model_for_the_cochain_algebra_of_a_space.pdf
- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/4076D51EAAD865E63F13B718B6026074/S0010437X20007319a.pdf/strictly_commutative_model_for_the_cochain_algebra_of_a_space.pdf
- https://doi.org/10.1112/S0010437X20007319
- https://msp.org/index/ail.php?jpath=pjm&l=C
- https://msp.org/index/ail.php?jpath=pjm&l=C


### MID-S29

Purpose: Publisher click/access attempts, including an irrelevant result and inaccessible Garvín route; neither used as a proof.

Evidence file: `research/middle_web_029.json`. SHA-256: `f5118a78acfffb036ddca00ca4ac484b3903dc334b7f3162b75578635cd385c6`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://doi.org/10.4064/-45-1-169-176
- https://dx.doi.org/10.2140/pjm.1978.76.17:


### MID-S30

Purpose: Cenkl–Porter1982 original discovered; Garvín strict-range source search.

Evidence file: `research/middle_web_030.json`. SHA-256: `28820a121ddd61aeea674806985a25aec85a85acf1f7be636953db8bfdf96f2a`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://www.researchgate.net/publication/260939167_An_extension_of_Miller_scaling_to_scale_sorptivity_by_contact_angle
- https://mat.uab.cat/~pubmat/fitxers/download/FileType%3Apdf/FolderName%3Av26%283%29/FileName%3A26382_01.pdf
- https://www.researchgate.net/publication/39091988_Cup-i_product_and_higher_homotopies_in_the_de_Rham_complex
- https://www.academia.edu/144971493/Cup_i_product_and_higher_homotopies_in_the_de_Rham_complex
- https://doi.org/10.5565/PUBLMAT_26382_01
- https://documat.unirioja.es/ejemplar/509799
- https://neu.academia.edu/RichardPorter
- https://independent.academia.edu/RichardPorter40/Papers
- https://www.numdam.org/issue/AST_1990__45__1_0.pdf
- https://msp.org/pjm/1984/112-1/p04.xhtml
- https://msp.org/pjm/1984/112-1/p04.xhtml:
- https://www.impan.pl/shop/bc45/bc45117.pdf


### MID-S31

Purpose: Mandell2001 author PDF, Cenkl–Porter1982/1984 originals, Bachmann–Burklund2026 source discovery.

Evidence file: `research/middle_web_031.json`. SHA-256: `94fd843c2b10c17028c0ef793bb56de616401e1f080b294de6d7e6fd8f30324a`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://mmandell.pages.iu.edu/papers/einffinal.pdf
- https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/mandell-alg.pdf
- https://www.math.univ-paris13.fr/~ausoni/miscnotes/p-adic-htpy-type.pdf
- https://www.sciencedirect.com/science/article/pii/S0040938399000531
- https://www.sciencedirect.com/science/article/pii/S0166864101001912
- https://ncatlab.org/nlab/show/p-adic%2Bhomotopy%2Btheory
- https://mmandell.pages.iu.edu/papers/
- https://www.researchgate.net/publication/223160487_E_algebras_and_p-adic_homotopy_theory
- https://www.researchgate.net/publication/353047516_Prismatic_cohomology_and_p-adic_homotopy_theory
- https://www.sciencedirect.com/science/article/pii/S0022404900000542
- https://link.springer.com/article/10.1007/s00029-026-01141-1
- https://sites.google.com/view/mandellstheorem/home
- https://www.researchgate.net/publication/403043940_mathbb_E_infty_-coalgebras_and_p-adic_homotopy_theory
- https://www.researchgate.net/publication/369477318_On_the_deformation_theory_of_mathbbE_infty-coalgebras
- https://portal.mardi4nfdi.de/wiki/Item%3AQ1591430
- https://arxiv.org/abs/2402.15850
- https://arxiv.org/abs/math/0311016
- https://arxiv.org/abs/2012.08941
- https://www.youtube.com/watch?v=jMq162v8xDs
- https://arxiv.org/abs/math/9907115
- http://www.hopf.math.purdue.edu
- https://en.wikipedia.org/wiki/Highly_structured_ring_spectrum
- https://www.scribd.com/document/954982395/Toms-G-2014-on-Metioning-the-Unmentionable-Feminism
- https://en.wikipedia.org/wiki/Algebraic_number_theory
- https://www.academia.edu/1462053/Miller_s_environmental_uncertainty_scale_An_extension_to_the_Arab_world_International
- https://en.wikipedia.org/wiki/P-adic_analysis
- https://mat.uab.cat/~pubmat/fitxers/download/FileType%3Apdf/FolderName%3Av26%283%29/FileName%3A26382_01.pdf
- https://mat.uab.cat/~pubmat/fitxers/download/FileType:pdf/FolderName:v26(3)/FileName:26382_01.pdf
- https://mat.uab.cat/~pubmat/fitxers/download/FileType:pdf/FolderName:v26(3)/FileName:26382_01.pdf;
- https://mat.uab.cat/~pubmat/fitxers/download/FileType:pdf/FolderName:v26(3)/FileName:26382_01.pdf
- https://msp.org/pjm/1984/112-1/pjm-v112-n1-p04-s.pdf
- https://msp.org/pjm/1984/112-1/pjm-v112-n1-p04-s.pdf


### MID-S32

Purpose: Mandell2001 and Bachmann–Burklund arXiv/published versions; Cenkl–Porter1984 §4.

Evidence file: `research/middle_web_032.json`. SHA-256: `7f5bd102f94bd60a6644876f80b3ec19e6a2cf6ab35a9c699df886e5112e9e19`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://mmandell.pages.iu.edu/papers/einffinal.pdf
- https://mmandell.pages.iu.edu/papers/einffinal.pdf
- https://arxiv.org/pdf/2402.15850
- https://arxiv.org/pdf/2402.15850
- https://msp.org/pjm/1984/112-1/pjm-v112-n1-p04-s.pdf
- https://msp.org/pjm/1984/112-1/pjm-v112-n1-p04-s.pdf


### MID-S33

Purpose: Mandell coefficient distinctions, Cenkl–Porter theorems and Bachmann–Burklund publication metadata.

Evidence file: `research/middle_web_033.json`. SHA-256: `01f446e67ed4d77e81df6aaa22be97d67179644c73360e66342207ec55f7e4cc`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://arxiv.org/abs/2402.15850
- https://arxiv.org/abs/2402.15850
- https://link.springer.com/article/10.1007/s00029-026-01141-1
- https://link.springer.com/article/10.1007/s00029-026-01141-1
- https://mmandell.pages.iu.edu/papers/einffinal.pdf
- https://mmandell.pages.iu.edu/papers/einffinal.pdf
- https://msp.org/pjm/1984/112-1/pjm-v112-n1-p04-s.pdf
- https://arxiv.org/pdf/2402.15850


### MID-S34

Purpose: Mandell AppendixA; visual Cenkl–Porter §4 statements; Bachmann–Burklund dates.

Evidence file: `research/middle_web_034.json`. SHA-256: `50af8e400cd523660f4c9e2d4d4bcacb41423972bbb1b044fbe1d56006e93ded`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://mmandell.pages.iu.edu/papers/einffinal.pdf
- https://msp.org/pjm/1984/112-1/pjm-v112-n1-p04-s.pdf
- https://link.springer.com/article/10.1007/s00029-026-01141-1


### MID-S35

Purpose: Published Bachmann–Burklund Theorems1.2/8.1 and1.3/8.2; Mandell AppendixA.

Evidence file: `research/middle_web_035.json`. SHA-256: `fb33b20ee77b623b93cee2ad01173a3dd9877dbe34919dfb33b8fe9f25bfc863`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://link.springer.com/article/10.1007/s00029-026-01141-1
- https://mmandell.pages.iu.edu/papers/einffinal.pdf
- https://link.springer.com/content/pdf/10.1007/s00029-026-01141-1.pdf
- http://creativecommons.org/licenses/by/4.0/†creativecommons.org】
- https://doi.org/10.1007/s00029-026-01141-1


### MID-S36

Purpose: SGA9.7 and Grothendieck uniqueness follow-up; Sullivan full-source follow-back. Unofficial SGA retyping and AI-generated exposition excluded as theorem evidence.

Evidence file: `research/middle_web_036.json`. SHA-256: `15c542a9057fca4507236e622c95e81a8c262edbdacd0bca6415c91eb59187d9`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://grothendiecksga.com/read/sga7/fr/9-9.html
- https://smf.emath.fr/publications/realisation-ell-adique-de-laccouplement-de-monodromie-dapres-grothendieck
- https://www.numdam.org/issue/AST_1991__196-197__1_0.pdf
- https://grothendiecksga.com/read/sga7/fr/9-sommaire.html
- https://grothendiecksga.com/read/sga7/fr/9-10.html
- https://www.numdam.org/item/AST_1991__196-197__1_0.pdf
- https://numdam.org/item/AST_1991__196-197__1_0.pdf
- https://geotoppos.org/divers/SGA7I.pdf
- https://grothendiecksga.com/read/sga7/fr/
- https://grothendiecksga.com/read/sga7/en/9-sommaire.html
- https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf
- https://grothendiecksga.com/read/sga7/fr/9-12.html
- https://grothendiecksga.com/read/sga7/fr/7-0.html
- https://zenodo.org/records/22985823
- https://www.math.mcgill.ca/darmon/pub/Articles/Research/16.Rigid-analytic%20/pub16.pdf
- https://grothendiecksga.com/read/sga7/fr/9-11.html
- https://books.google.com/books/about/Groupes_de_Monodromie_en_G%C3%A9om%C3%A9trie_Alg.html?id=beFUAAAAYAAJ
- https://grothendiecksga.com/read/sga7/fr/1-5.html
- https://fr.wikipedia.org/wiki/S%C3%A9minaire_de_g%C3%A9om%C3%A9trie_alg%C3%A9brique_du_Bois_Marie
- https://openmaths.org/courses/GL-DMOD/the-de-rham-functor.html
- https://www.researchgate.net/publication/369924551_Generalized_n-series_and_de_Rham_complexes
- https://www.sciencedirect.com/science/article/abs/pii/S0001870822005084
- https://numdam.org/item/PMIHES_1977__47__269_0.pdf
- https://numdam.org/item/PMIHES_1977__47__269_0.pdf


### MID-S37

Purpose: Sullivan exact theorem search; unsuccessful guessed Numdam endpoint retained as an access failure.

Evidence file: `research/middle_web_037.json`. SHA-256: `0c8b25f7a4b9100c8b61a08d98113a8797b243a5e88f4aa0bbecb37b6f7a2a39`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://www.numdam.org/item/AST_1991__196-197__27_0/
- https://numdam.org/item/PMIHES_1977__47__269_0.pdf
- https://numdam.org/item/PMIHES_1977__47__269_0.pdf


### MID-S38

Purpose: Sullivan §§5/8 direct source reading of construction, nilpotent comparison and incomplete nonnilpotent claim.

Evidence file: `research/middle_web_038.json`. SHA-256: `a5c0248c104ee220f3a7414a14962c0e7ac749a233c34748b263785fca31ff5f`.

Literal top-level search strings were not separately retained at the time. Full original returned payload, including embedded open/find Source commands, URLs and result titles, is retained. This purpose is a later human-authored index, not a reconstructed verbatim query.


Retrieved/opened URLs (presence here is not endorsement):

- https://numdam.org/item/PMIHES_1977__47__269_0.pdf
- https://numdam.org/item/PMIHES_1977__47__269_0.pdf


### MID-S39

Purpose: Explicit final searches: de Jong erratum, Coleman pairing, Stoia title, MathOverflow divided powers.

Evidence file: `research/middle_web_039.json`. SHA-256: `fde10c2373885ace5a000d509a896ce287f8aeee86bb105119b47c97e6bdf6b7`.

Literal tool input retained.


Literal input:

```json
{
  "system1_search_query": [
    {
      "q": "\"Homomorphisms of Barsotti-Tate groups and crystals in positive characteristic\" erratum 1999"
    },
    {
      "q": "\"The monodromy pairing\" Coleman 2000 315"
    },
    {
      "q": "\"Stoia\" \"Points de Gorenstein\" 1975"
    },
    {
      "q": "site:mathoverflow.net Grothendieck \"de Rham\" \"divided powers\""
    }
  ],
  "response_length": "long"
}
```


Retrieved/opened URLs (presence here is not endorsement):

- https://portal.mardi4nfdi.de/wiki/Item%3AQ1273298
- https://www.jmilne.org/math/xnotes/Tate.pdf
- https://intlpress.com/site/pub/files/_fulltext/journals/ajm/2000/0004/0002/AJM-2000-0004-0002-a002.pdf
- https://imar.ro/~increst/1979/31_1979.pdf
- https://mathoverflow.net/questions/251143/grothendiecks-motivation-of-crystalline-cohomology
- https://mathoverflow.net/questions/230874/have-grothendiecks-notes-in-montpellier-already-been-investigated/237267
- https://www.cambridge.org/core/books/abs/padic-differential-equations/references/6E71998A1978BC1E554F913AC279B305
- https://portal.mardi4nfdi.de/wiki/Crystalline_Dieudonn%C3%A9_theory_over_excellent_schemes
- http://www.numdam.org/item?id=BSMF_1999__127_2_333_0
- https://eudml.org/doc/87809
- http://smf4.emath.fr/Publications/Bulletin/127/html/smf_bull_127_333-348.html
- https://abelprize.no/sites/default/files/2021-09/The%20Abel%20Prize%202008-2012_Full_.pdf


### MID-S40

Purpose: Open Coleman (403), Bănică–Stoia original, zbMATH record (403), MathOverflow crystalline question.

Evidence file: `research/middle_web_040.json`. SHA-256: `334e1be2b1c93e7e90b6a631e21b5f0c08013c99b013dd2ad935b89cd1517dde`.

Literal tool input retained.


Literal input:

```json
{
  "open": [
    {
      "ref_id": "https://intlpress.com/site/pub/files/_fulltext/journals/ajm/2000/0004/0002/AJM-2000-0004-0002-a002.pdf"
    },
    {
      "ref_id": "https://imar.ro/~increst/1979/31_1979.pdf"
    },
    {
      "ref_id": "https://zbmath.org/?q=an%3A0929.14029"
    },
    {
      "ref_id": "https://mathoverflow.net/questions/251143/grothendiecks-motivation-of-crystalline-cohomology"
    }
  ],
  "response_length": "long"
}
```


Retrieved/opened URLs (presence here is not endorsement):

- https://intlpress.com/site/pub/files/_fulltext/journals/ajm/2000/0004/0002/AJM-2000-0004-0002-a002.pdf
- https://intlpress.com/site/pub/files/_fulltext/journals/ajm/2000/0004/0002/AJM-2000-0004-0002-a002.pdf:
- https://imar.ro/~increst/1979/31_1979.pdf
- https://imar.ro/~increst/1979/31_1979.pdf
- https://zbmath.org/?q=an%3A0929.14029
- https://zbmath.org/?q=an%3A0929.14029:
- https://mathoverflow.net/questions/251143/grothendiecks-motivation-of-crystalline-cohomology
- https://mathoverflow.net/questions/251143/grothendiecks-motivation-of-crystalline-cohomology


### MID-S41

Purpose: Explicit uniqueness/Hasse/endomorphism searches; Li–Mondal surfaced as a distinct algebraic de Rham theory.

Evidence file: `research/middle_web_041.json`. SHA-256: `f01921919119a0cb54dd48fe7c3d50af5907812d770325bc007eaf179fd3943c`.

Literal tool input retained.


Literal input:

```json
{
  "system1_search_query": [
    {
      "q": "site:mathoverflow.net \"de Rham\" \"Cartan\" \"Miller\""
    },
    {
      "q": "site:zbmath.org \"Théories cohomologiques\" Cartan"
    },
    {
      "q": "\"Hasse derivatives\" \"invariants\" \"additive group\""
    },
    {
      "q": "\"divided power\" \"automorphisms\" \"de Rham\""
    }
  ],
  "response_length": "long"
}
```


Retrieved/opened URLs (presence here is not endorsement):

- https://mathoverflow.net/questions/91385/where-can-i-find-a-proof-of-the-de-rham-weil-theorem
- https://mathoverflow.net/questions/91385/where-can-i-find-a-proof-of-the-de-rham-weil-theorem/91424
- https://mathoverflow.net/questions/tagged/sheaf-cohomology?page=7&tab=Active
- https://mathoverflow.net/questions/tagged/at.algebraic-topology?page=170&tab=newest
- https://www.arietiform.com/application/nph-tsq.cgi/su/20/https/www.alphaxiv.org/abs/2608.20066
- https://www.researchgate.net/publication/320464646_Elementary_components_of_Hilbert_schemes_of_points
- https://pure.tue.nl/ws/portalfiles/portal/102837613/200710440.pdf
- https://www.math.canterbury.ac.nz/~f.voloch/Pdfs/comp2.pdf
- https://guests.mpim-bonn.mpg.de/ferdinand/q-deRham.pdf
- https://borowiecki.dev/pdf/2611.13877
- https://msp.org/gt/2024/28-2/gt-v28-n2-p07-s.pdf


### MID-S42

Purpose: Hasse–Schmidt, DLMF and author-bibliography searches; no exact PD-localization theorem inferred.

Evidence file: `research/middle_web_042.json`. SHA-256: `8f4aa32660098da7ef5d4b6ba5f0f3331f029385aef7bb576ec116d18443f63a`.

Literal tool input retained.


Literal input:

```json
{
  "open": [
    {
      "ref_id": "https://msp.org/gt/2024/28-2/gt-v28-n2-p07-s.pdf"
    }
  ],
  "system2_search_query": [
    {
      "q": "Hasse Schmidt derivation additive group action invariants polynomial translation site:arxiv.org"
    },
    {
      "q": "Dirichlet integral simplex monomial beta integral site:dlmf.nist.gov"
    },
    {
      "q": "\"Théories cohomologiques\" Cartan zbMATH"
    },
    {
      "q": "\"Grothendieck\" \"De Rham\" \"unicité\" \"Cartan\""
    }
  ],
  "response_length": "long"
}
```


Retrieved/opened URLs (presence here is not endorsement):

- https://wstein.org/sga/aiello/AIELLO%20-%20Grothendieck%27s%20Bibliography.pdf
- https://dlmf.nist.gov/5.14
- http://dlmf.nist.gov/5.14
- https://books.google.com/books?id=NheFSfGEEz8C
- https://webusers.imj-prg.fr/~max.karoubi/KL.livre/Bibliographie.Index.pdf
- https://numdam.org/item/AST_1990__45__1_0.pdf
- https://arxiv.org/abs/1110.6108
- https://portal.mardi4nfdi.de/wiki/Resolutions_via_homological_perturbation
- https://archive.numdam.org/item/AST_1987__149__1_0/
- https://dlmf.nist.gov/14.12
- https://dlmf.nist.gov/draft1/5.12
- https://www.numdam.org/item/AST_1987__149__1_0/
- https://www.numdam.org/issues/AST_1987__149__1_0/
- https://portail.polytechnique.edu/editions/sites/editions/files/content/pages/documents/2024-12/table-des-matieres_154.pdf
- https://dlmf.nist.gov/5.12
- https://etudier.uqam.ca/cours?p=1913&sigle=MAT9330
- https://arxiv.org/abs/1212.5788
- https://d-nb.info/1068402180/04
- https://numdam.org/item/SB_1964-1966__9__287_0/
- https://dlmf.nist.gov/18.10
- https://webusers.imj-prg.fr/~max.karoubi/Publications/47.pdf
- https://dlmf.nist.gov/25.19
- https://arxiv.org/abs/1001.3293
- https://www.numdam.org/item/AST_1990__45__1_0/
- https://geodesic.mathdoc.fr/item/AST_1990__45__1_0/
- https://arxiv.org/abs/1810.08075
- https://dlmf.nist.gov/5.13
- https://dlmf.nist.gov/18.17
- https://csg.igrothendieck.org/published-works/
- https://dlmf.nist.gov/15.6
- https://dlmf.nist.gov/8.17
- https://ouci.dntb.gov.ua/en/works/98ZkA8Y4/
- https://www.academia.edu/89969208/La_g%C3%A9om%C3%A9trie_alg%C3%A9brique_Recherches_historiques_coll_Sciences_dans_lhistoire_
- https://bibliotheque.imo.universite-paris-saclay.fr/bibliotheques-numeriques/publications/publis-avant-1995/?critere=titre
- https://dlmf.nist.gov/19.16
- https://dlmf.nist.gov/5.18
- https://fr.scribd.com/document/952233931/66
- https://ftp.math.utah.edu/pub/tex/bib/toc/lnm1970.html
- https://www.academia.edu/74546881/Travaux_de_Gabber_sur_luniformisation_locale_et_la_cohomologie_etale_des_schemas_quasi_excellents_Seminaire_a_lEcole_polytechnique_2006_2008
- https://fr.wikipedia.org/wiki/Liste_des_th%C3%A8ses_math%C3%A9matiques_soutenues_en_fran%C3%A7ais_de_1811_%C3%A0_1960
- https://opac.lib.u-toyama.ac.jp/opc/xc/search/%2A?date_df_gap=%2B10YEAR&filter%5B0%5D=type%3Amanifestation&filter%5B1%5D=locations_fc%3A%22Central+Library+-+Stacks+2F%22&filter%5B2%5D=place_fc%3A%22Central+Library%22&filter%5B3%5D=contentType_fc%3A%22Book%22&filter%5B4%5D=subject_fc%3A%22%E6%95%B0%E5%AD%A6%22&filter%5B5%5D=date_df%3A%5B1900-01-01T00%3A00%3A00Z+TO+1999-12-31T23%3A59%3A59Z%5D&ql=1&remove_facet=1&rows=100
- https://opac.lib.u-toyama.ac.jp/opc/xc/search/%2A?filter%5B0%5D=type%3Amanifestation&filter%5B1%5D=locations_fc%3A%22Central+Library+-+Stacks+2F%22&filter%5B2%5D=place_fc%3A%22Central+Library%22&filter%5B3%5D=contentType_fc%3A%22Book%22&filter%5B4%5D=subject_fc%3A%22%E6%95%B0%E5%AD%A6%22&ql=1&remove_facet=1&rows=100
- https://opac.lib.u-toyama.ac.jp/opc/xc/search/%2A?filter%5B0%5D=type%3Amanifestation&filter%5B1%5D=locations_fc%3A%22Central+Library+-+Stacks+2F%22&filter%5B2%5D=place_fc%3A%22Central+Library%22&filter%5B4%5D=subject_fc%3A%22%E6%95%B0%E5%AD%A6%22&ql=1&remove_facet=1&rows=100
- https://www.imj-prg.fr/gestion/evenement/affEvenement/74
- https://ftp.math.utah.edu/pub/tex/bib/toc/lnm1990.html
- https://opac.lib.u-toyama.ac.jp/opc/xc/search/%2A?filter%5B0%5D=type%3Amanifestation&filter%5B1%5D=locations_fc%3A%22Central+Library+-+Stacks+2F%22&filter%5B2%5D=place_fc%3A%22Central+Library%22&filter%5B3%5D=contentType_fc%3A%22Book%22&filter%5B4%5D=subject_fc%3A%22%E6%95%B0%E5%AD%A6%22&filter%5B5%5D=place_fc%3A%22Central+Lib-stuck%22&ql=1&remove_facet=1&rows=100
- https://opac.lib.u-toyama.ac.jp/opc/en/xc/search/%2A?date_df_gap=%2B10YEAR&filter%5B0%5D=type%3Amanifestation&filter%5B1%5D=place_fc%3A%22Central+Library%22&filter%5B2%5D=contentType_fc%3A%22Book%22&filter%5B3%5D=locations_fc%3A%22Central+Library+-+Stacks+2F%22&filter%5B4%5D=date_df%3A%5B1900-01-01T00%3A00%3A00Z+TO+1999-12-31T23%3A59%3A59Z%5D&filter%5B6%5D=place_fc%3A%22Central+Lib-stuck%22&filter%5B7%5D=subject_fc%3A%22%E6%95%B0%E5%AD%A6%22&ql=1&remove_facet=1&rows=100
- https://opac.lib.u-toyama.ac.jp/opc/xc/search/%2A?filter%5B0%5D=type%3Amanifestation&filter%5B1%5D=place_fc%3A%22Central+Library%22&filter%5B2%5D=contentType_fc%3A%22Book%22&filter%5B3%5D=locations_fc%3A%22Research+room%22&filter%5B4%5D=subject_fc%3A%22%E6%95%B0%E5%AD%A6%22&filter%5B5%5D=locations_fc%3A%22Central+Library+-+Stacks+2F%22&ql=1&remove_facet=1&rows=100
- https://fr.wikipedia.org/wiki/Chronologie_de_l%27alg%C3%A8bre
- https://msp.org/gt/2024/28-2/gt-v28-n2-p07-s.pdf
- https://msp.org/gt/2024/28-2/gt-v28-n2-p07-s.pdf


### MID-S43

Purpose: Hoffmann–Kowalski, Hazewinkel, DLMF and Grothendieck published-works bibliography opened.

Evidence file: `research/middle_web_043.json`. SHA-256: `9ac6e29b73c01c790aae78454536cf082e7480e188aaeda9f43ffef7113ca65c`.

Literal tool input retained.


Literal input:

```json
{
  "open": [
    {
      "ref_id": "https://arxiv.org/pdf/1212.5788"
    },
    {
      "ref_id": "https://arxiv.org/pdf/1110.6108"
    },
    {
      "ref_id": "https://dlmf.nist.gov/5.14"
    },
    {
      "ref_id": "https://csg.igrothendieck.org/published-works/"
    }
  ],
  "system2_search_query": [
    {
      "q": "\"On endomorphisms of the de Rham cohomology functor\" theorem"
    }
  ],
  "response_length": "long"
}
```


Retrieved/opened URLs (presence here is not endorsement):

- https://msp.org/gt/2024/28-2/gt-v28-n2-p07-p.pdf
- https://msp.org/gt/2024/28-2/gt-v28-n2-p07-s.pdf
- https://www.math.purdue.edu/~mondalsh/papers/Endomorphisms_of_the_de_Rham_cohomology_functor.pdf
- https://arxiv.org/abs/2109.04303
- https://portal.mardi4nfdi.de/wiki/On_endomorphisms_of_the_de_Rham_cohomology_functor
- https://www.researchgate.net/scientific-contributions/Piotr-Achinger-2025828547
- https://www.researchgate.net/publication/379064181_On_endomorphisms_of_the_de_Rham_cohomology_functor
- https://pith.science/paper/1810.11853
- https://www.researchgate.net/publication/354493517_On_endomorphisms_of_the_de_Rham_cohomology_functor
- https://shizhang.li/papers.html
- https://www.researchgate.net/publication/369504069_Some_refinements_of_the_Deligne-Illusie_theorem
- https://antieau.github.io/2021/12/31/yir.html
- https://scispace.com/papers/on-endomorphisms-of-the-de-rham-cohomology-functor-1kl25oq8jg
- https://www.sciencedirect.com/science/article/abs/pii/S0001870822005084
- https://pith.science/paper/2005.04746
- https://portal.mardi4nfdi.de/wiki/Reconstruction_of_the_stacky_approach_to_de_Rham_cohomology
- https://arxiv.org/pdf/1212.5788
- https://arxiv.org/pdf/1212.5788
- https://arxiv.org/pdf/1110.6108
- https://arxiv.org/pdf/1110.6108
- https://dlmf.nist.gov/5.14
- https://dlmf.nist.gov/5.14
- http://dlmf.nist.gov/5.14】
- http://dlmf.nist.gov/5.14.E1】
- http://dlmf.nist.gov/5.14.E2】
- https://csg.igrothendieck.org/published-works/
- https://csg.igrothendieck.org/published-works/


### MID-S44

Purpose: Higher-derivation definitions/constants; Li–Mondal publisher access; bibliography checks.

Evidence file: `research/middle_web_044.json`. SHA-256: `d15a655febb2ad49e1987778ce1e7979b8829be340a9f94829dc8abee9593d2b`.

Literal tool input retained.


Literal input:

```json
{
  "open": [
    {
      "ref_id": "https://msp.org/gt/2024/28-2/gt-v28-n2-p07-p.pdf"
    }
  ],
  "find": [
    {
      "ref_id": "turn572673458view0",
      "pattern": "Definition 2.1"
    },
    {
      "ref_id": "turn572673458view0",
      "pattern": "[19]"
    },
    {
      "ref_id": "turn572673458view0",
      "pattern": "constants"
    },
    {
      "ref_id": "turn572673458view3",
      "pattern": "Puissances"
    }
  ],
  "response_length": "long"
}
```


Retrieved/opened URLs (presence here is not endorsement):

- https://msp.org/gt/2024/28-2/gt-v28-n2-p07-p.pdf
- https://msp.org/gt/2024/28-2/gt-v28-n2-p07-p.pdf
- https://arxiv.org/pdf/1212.5788
- http://mat.msgsu.edu.tr/~dpierce/Mathematics/Derivations/Revisited/
- https://csg.igrothendieck.org/published-works/


### MID-S45

Purpose: Li–Mondal author original; Hoffmann–Kowalski translation formula and arXiv chronology.

Evidence file: `research/middle_web_045.json`. SHA-256: `5e5dc147f2cc3bff551185c353e0b6cd5b2dec97dffbf21fc857e251e489de9f`.

Literal tool input retained.


Literal input:

```json
{
  "open": [
    {
      "ref_id": "https://www.math.purdue.edu/~mondalsh/papers/Endomorphisms_of_the_de_Rham_cohomology_functor.pdf"
    },
    {
      "ref_id": "turn572673458view0",
      "lineno": 410
    },
    {
      "ref_id": "turn572673458view0",
      "lineno": 1649
    },
    {
      "ref_id": "https://arxiv.org/abs/1212.5788"
    }
  ],
  "response_length": "long"
}
```


Retrieved/opened URLs (presence here is not endorsement):

- https://www.math.purdue.edu/~mondalsh/papers/Endomorphisms_of_the_de_Rham_cohomology_functor.pdf
- https://www.math.purdue.edu/~mondalsh/papers/Endomorphisms_of_the_de_Rham_cohomology_functor.pdf
- https://arxiv.org/pdf/1212.5788
- http://arxiv.org/abs/1404.7475
- http://www.math.uni.wroc.pl/~pkowa/mojeprace/integnote.pdf
- http://mat.msgsu.edu.tr/~dpierce/Mathematics/Derivations/Revisited/
- http://home.mathematik.uni-freiburg.de/ziegler/preprints/canonical-p-bases.pdf
- http://www.math.uni.wroc.pl/~pkowa/
- https://arxiv.org/abs/1212.5788
- https://arxiv.org/abs/1212.5788
- https://doi.org/10.48550/arXiv.1212.5788†doi.org】
- https://doi.org/10.1016/j.jpaa.2014.05.024†doi.org】


### MID-S46

Purpose: Li–Mondal Theorem1.1 precisely read and excluded as a solution of the different simplicial PD category.

Evidence file: `research/middle_web_046.json`. SHA-256: `692314d5a104a2bf33356b8684cbfb447d27e56b726bd6cbb178c79227e3ae17`.

Literal tool input retained.


Literal input:

```json
{
  "open": [
    {
      "ref_id": "https://www.math.purdue.edu/~mondalsh/papers/Endomorphisms_of_the_de_Rham_cohomology_functor.pdf",
      "lineno": 64
    }
  ],
  "find": [
    {
      "ref_id": "https://www.math.purdue.edu/~mondalsh/papers/Endomorphisms_of_the_de_Rham_cohomology_functor.pdf",
      "pattern": "Theorem 1.1."
    }
  ],
  "response_length": "long"
}
```


Retrieved/opened URLs (presence here is not endorsement):

- https://www.math.purdue.edu/~mondalsh/papers/Endomorphisms_of_the_de_Rham_cohomology_functor.pdf
- https://www.math.purdue.edu/~mondalsh/papers/Endomorphisms_of_the_de_Rham_cohomology_functor.pdf


### MID-S47

Purpose: Exact final search strings for quasi-flasque, uniqueness, simplicial PD endomorphisms and fraction calculus; unrelated algebraic de Rham and AI-generated pages excluded.

Evidence file: `research/middle_web_047.json`. SHA-256: `020c659fa2f02403359f063b65516d69261c1211cc001c4a14e5a81bb25d0969`.

Literal tool input retained.


Literal input:

```json
{
  "system1_search_query": [
    {
      "q": "\"Grothendieck\" \"de Rham\" \"quasi-flasque\""
    },
    {
      "q": "\"Grothendieck\" \"théories de de Rham\" \"unicité\""
    },
    {
      "q": "\"divided power\" \"de Rham\" \"endomorphisms\" simplicial"
    },
    {
      "q": "\"Cartan\" \"de Rham\" \"calculus of fractions\""
    }
  ],
  "response_length": "long"
}
```


Retrieved/opened URLs (presence here is not endorsement):

- https://comptes-rendus.academie-sciences.fr/mathematique/articles/10.5802/crmath.764/
- https://www.numdam.org/item/PMIHES_1966__29__95_0/
- https://www.numdam.org/articles/10.1007/BF02684807/}
- https://www.numdam.org/articles/10.1007/BF02684807/
- https://books.google.com/books/about/On_the_De_Rham_Cohomology_of_Schemes.html?id=plrvAAAAMAAJ
- https://www.academia.edu/29211781/From_Sheaf_Cohomology_to_the_Algebraic_de_Rham_Theorem
- https://csg.igrothendieck.org/wp-content/uploads/2024/10/U10.2.pdf
- https://openmaths.org/courses/cotangent-complexes-and-deformations-in-ringed-topoi/the-de-rham-complex-of-a-formal-category-with-divided-powers.html
- https://www.math.uni-bielefeld.de/~hzou/papers/btt/
- https://openmaths.org/courses/cotangent-complexes-and-deformations-in-ringed-topoi/the-derived-de-rham-complex.html
- https://openmaths.org/courses/cotangent-complexes-and-deformations-in-ringed-topoi/providers.html
- https://www.researchgate.net/publication/368716787_Non-decomposability_of_the_de_Rham_complex_and_non-semisimplicity_of_the_Sen_operator
- https://djvu.online/file/glFr1NcBvwDx7
- https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/monoidal-functors-acyclic-models-and-chain-operads/0EFBB005091A8F0D687806A1407D5927
- https://arxiv.org/abs/2109.04303


### MID-S48

Purpose: Guillén Santos–Navarro–Pascual–Roig monoidal acyclic-models original and source discovery.

Evidence file: `research/middle_web_048.json`. SHA-256: `8a88da058c99a84282ed1b01f761cdca88d7df138175fb30b3bd43995d6ce4e3`.

Literal tool input retained.


Literal input:

```json
{
  "open": [
    {
      "ref_id": "https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/monoidal-functors-acyclic-models-and-chain-operads/0EFBB005091A8F0D687806A1407D5927"
    }
  ],
  "system2_search_query": [
    {
      "q": "\"Monoidal Functors, Acyclic Models and Chain Operads\" pdf"
    }
  ],
  "response_length": "long"
}
```


Retrieved/opened URLs (presence here is not endorsement):

- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0EFBB005091A8F0D687806A1407D5927/S0008414X00018940a.pdf/div-class-title-monoidal-functors-acyclic-models-and-chain-operads-div.pdf
- https://diposit.ub.edu/dspace/bitstream/2445/34464/1/531385.pdf
- https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/monoidal-functors-acyclic-models-and-chain-operads/0EFBB005091A8F0D687806A1407D5927
- https://doi.org/10.4153/CJM-2008-017-7
- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0EFBB005091A8F0D687806A1407D5927/S0008414X00018940a.pdf/monoidal_functors_acyclic_models_and_chain_operads.pdf
- https://www.academia.edu/89942788/Monoidal_Functors_Acyclic_Models_and_Chain_Operads
- https://diposit.ub.edu/items/1e0b4cb5-dbeb-40f3-99b4-701d28665a8b/full
- https://diposit.ub.edu/items/1e0b4cb5-dbeb-40f3-99b4-701d28665a8b
- https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/issue/55B5D32420AAC856C6051CECE88435CA
- https://diposit.ub.edu/server/api/core/bitstreams/b3e682b4-8e17-400e-82d6-315e218467bc/content
- https://www.cambridge.org/core/search?eventCode=SE-AU&filters%5BauthorTerms%5D=F.+Guill%C3%A9n+Santos
- https://zendy.io/pdf-viewer/10.4153/cjm-2009-017-5
- https://www.cambridge.org/core/search?filters%5Bkeywords%5D=cohomology+theories
- https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/most-cited?pageNum=157
- https://www.cambridge.org/core/search?filters%5Bkeywords%5D=55N10
- https://www.researchgate.net/publication/33421484_Monoidal_Functors_Acyclic_Models_and_Chain_Operads
- https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/most-cited?pageNum=158
- https://arxiv.org/abs/math/0506624
- https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/monoidal-functors-acyclic-models-and-chain-operads/0EFBB005091A8F0D687806A1407D5927


### MID-S49

Purpose: Original publisher PDF and arXiv chronology for monoidal acyclic models.

Evidence file: `research/middle_web_049.json`. SHA-256: `cac8a11e3103dcf1f3b6514751b665a03cde7aaaef0e359c30bd02947c961962`.

Literal tool input retained.


Literal input:

```json
{
  "open": [
    {
      "ref_id": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0EFBB005091A8F0D687806A1407D5927/S0008414X00018940a.pdf/monoidal_functors_acyclic_models_and_chain_operads.pdf"
    },
    {
      "ref_id": "https://arxiv.org/abs/math/0506624"
    }
  ],
  "response_length": "long"
}
```


Retrieved/opened URLs (presence here is not endorsement):

- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0EFBB005091A8F0D687806A1407D5927/S0008414X00018940a.pdf/monoidal_functors_acyclic_models_and_chain_operads.pdf
- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0EFBB005091A8F0D687806A1407D5927/S0008414X00018940a.pdf/monoidal_functors_acyclic_models_and_chain_operads.pdf
- https://doi.org/10.4153/CJM-2008-017-7
- https://arxiv.org/abs/math/0506624
- https://arxiv.org/abs/math/0506624
- https://doi.org/10.48550/arXiv.math/0506624†doi.org】


### MID-S50

Purpose: Theorems4.10,8.1,9.2 and Corollary9.3, with exact hypotheses, in monoidal acyclic models.

Evidence file: `research/middle_web_050.json`. SHA-256: `114d925afdb77689a11541e6dfb9fe792197034ba04f3042436b8f5efd7f50e2`.

Literal tool input retained.


Literal input:

```json
{
  "find": [
    {
      "ref_id": "turn912054172view0",
      "pattern": "Theorem 9.2"
    },
    {
      "ref_id": "turn912054172view0",
      "pattern": "Theorem 8.2"
    },
    {
      "ref_id": "turn912054172view0",
      "pattern": "9 Cohomology"
    },
    {
      "ref_id": "turn912054172view0",
      "pattern": "Theorem 4.10"
    }
  ],
  "response_length": "long"
}
```


Retrieved/opened URLs (presence here is not endorsement):

- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0EFBB005091A8F0D687806A1407D5927/S0008414X00018940a.pdf/monoidal_functors_acyclic_models_and_chain_operads.pdf
- https://doi.org/10.4153/CJM-2008-017-7


### MID-S51

Purpose: Monoidal acyclic-models p373 visually checked; Theorem4.10 proof and9.2 proof read. OCR >0 corrected to ≥0 only for this published source, not manuscript ink.

Evidence file: `research/middle_web_051.json`. SHA-256: `92f86099dc9f3d44abeaf39c23b5f8d17a31ef0a7dbe6a00fc934aada5ef4e46`.

Literal tool input retained.


Literal input:

```json
{
  "open": [
    {
      "ref_id": "turn912054172view0",
      "lineno": 1429
    },
    {
      "ref_id": "turn912054172view0",
      "lineno": 568
    }
  ],
  "screenshot": [
    {
      "ref_id": "turn912054172view0",
      "pageno": 25
    }
  ],
  "response_length": "long"
}
```


Retrieved/opened URLs (presence here is not endorsement):

- https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0EFBB005091A8F0D687806A1407D5927/S0008414X00018940a.pdf/monoidal_functors_acyclic_models_and_chain_operads.pdf
- https://doi.org/10.4153/CJM-2008-017-7


## Shared primary-source work

`ROOT-Cartan-full`: original journal scan at `work/reference_pdfs/invent35.pdf`; printed pp264,266–271, particularly §7. `ROOT-SGA-full`: original SGA7I PDF and per-page text/images in `work/reference_pdfs/sga7-1/`; exact donor locators are in `reference_audit.json` and `links.tsv`. `ROOT-Roby` and `ROOT-DoldPuppe`: original Numdam works opened by root, with the bounded source findings shared in the agent record. Shared access is identified as such in CHECK_EVENTS; it is not a claim that this agent independently reproved the source.

## Follow-back paths

Cartan’s1976 proof note → Miller preprint → Miller1978 → Cenkl–Porter1982/1984 and Garvín1998. Cartan’s comparison axioms → Mandell2002 and Guillén Santos et al.2008. SGA Tate proviso → de Jong’s author bibliography → original1998 DVI → original1999 erratum. Stoia donor attribution → same-title1975 note in Bănică–Stoia1979 bibliography → Stacks scheme openness theorem, kept distinct from the1979 analytic theorem. Dold–Puppe normalization → BMT derived-power décalage, with explicit finite-projective hypotheses. Dwyer title/DOI access attempts → Scheerer–Tanré1991 original, whose exact restatement is used under its own citation.

No source search or negative result in this file is used to assert that a manuscript question is new or still open in November2026. Classes C/D are accompanied by the exact comparison or search boundary in each claim.
