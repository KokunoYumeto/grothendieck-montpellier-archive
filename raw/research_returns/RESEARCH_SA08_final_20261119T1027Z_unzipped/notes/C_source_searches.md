# Sources and searches for Part C / B.6

Date: 2026-11-19. Run: /root/topos. We make no novelty or priority claim.

Queries actually run included:

- `site.stacks.math.columbia.edu simplicial divided powers flat modules acyclic`
- `cosimplicial abelian group flasque exterior square acyclic de Rham Grothendieck`
- `Dold Puppe flat resolutions divided powers homotopy exact complexes`
- `flat chain complexes filtered colimit finitely generated projective contractible complexes exact flat cycles theorem`
- `site.stacks.math.columbia.edu divided powers simplicial flat quasi isomorphism`
- `SGA 4 flasque presheaf universally acyclic slice category simplicial`
- `SGA 4 Tome 2 expose V 4.1 faisceaux flasques pdf`
- `Christensen Holm direct limit closure perfect complexes arxiv`
- `SGA4 tome2 pdf V 4.1 flasques`
- `SGA 4 théorie topos cohomologie étale exposé V pdf Milne`

Opened and used:

1. Christensen--Holm, author-hosted PDF (20 May2013 preprint), Theorem7.3, PDF pages13--14. Full arXiv v2 LaTeX source fetched from https://arxiv.org/src/1301.0731v2; it is a gzip-compressed single LaTeX source rather than a tar archive. Saved as `sources/C_christensen_holm_source.tex` and relevant theorem/proof read at lines1349--1400. The source theorem supplies filtered contractible approximation; application to Gamma and Lambda and the nonnegative truncation are supplied in C05.
2. Stacks Project Section14.24, Theorem14.24.3, https://stacks.math.columbia.edu/tag/019D . The exact equivalence is used; the Ext computation in C02 is supplied in full.
3. SGA4 ExposéV Definition4.1, French re-edition https://www.normalesup.org/~forgogozo/SGA4/tomes/SGA4.pdf , printed p289/PDFp297. It defines flasque using every object, correcting the supplied study's terminology. The English text at grothendiecksga.com was also opened to locate the statement, then the French mathematical edition was opened and checked.
4. Stacks Project Remark21.39.11, https://stacks.math.columbia.edu/tag/08QD , for the Eilenberg--Zilber tensor comparison.

No located primary source was found containing the specific elementary half-algebra obstruction B601 or the particular strict-equalizer counterexample C07. These are proved directly; this search record does not establish novelty.

Failed retrievals: https://fabrice.orgogozo.perso.math.cnrs.fr/SGA4/details/index.html timed out through the web tool; the normalesup mirror succeeded. https://arxiv.org/html/1301.0731v2 returned DisabledError; the arXiv source fetch succeeded. One guessed exposed-PDF path under the mirror was inaccessible; directory and full-volume routes succeeded. No mathematical claim depends on the failed paths.

## Additional source checks, 2026-11-19

- Searches: `Steenrod 1947 Products of cocycles and extensions of mappings cup i pdf`; `cohomology theories commutative differential graded algebra Cartan uniqueness divided powers simplicial integral`; `Berger Fresse combinatorial operad actions on cochains pdf 2004 Barratt Eccles cup i`; `Monoidal Functors Acyclic Models Chain Operads arxiv Guillen Navarro Pascual Roig`.
- Opened Berger--Fresse, arXiv math/0109158v2 full source. Theorem 2.1.1 and Section 2.2 supply the exact action and cup-i identification, without relying on an unlocated theorem in May.
- Opened Porter--Suciu, arXiv2105.10753v2 full source, Definition3.1 and Section4.3 as a corroborating cup-one source.
- Opened Guillen--Navarro--Pascual--Roig, arXivmath/0506624v2 full source and published PDF, Sections8--9 as an integral uniqueness approach. Scope is a localized monoidal associative theory category. It does not itself prove strict PD uniqueness in the manuscript category.
- Source-download script: code/C_fetch_more_sources.py. All three downloads succeeded in 7.4--7.8seconds concurrently; exact byte counts and URLs in logs/C_more_sources_fetch.tsv.
- Cartan exact article, sources/cartan1976.pdf, OCRed by code/C_read_cartan.py into sources/C_cartan1976_ocr.txt. All12 article pages rendered at2000px and OCRed in17.639seconds. Visual checks of printedpp266,267,271 confirm the morphism convention, dimensional hypothesis of Theorem2, cycle-flatness hypothesis of Theorem3, and the weight/binomial conclusion.

## Original manuscript images and renewed integral search, 2026-11-19 06:47 UTC

- Range-fetched original https://grothendieck.umontpellier.fr/136.pdf using code/C_fetch_manuscript.py. The uniqueness excerpt contains scans100,117,119,121 (2,621,440 newly transferred bytes,93.254s,one503retry); the half-algebra excerpt scans348,350,352 (1,572,864bytes,57.845s). Exact range receipts and logs are C_cote136_uniqueness.json and C_cote136_half_algebra.json under logs.
- Visually read uniqueness scans100,117,119,121, including projectif correction, lambda(0), eventual simplicial homology condition, and separate a)/b) claims. Viewed all three half-algebra scans; their faintness prevents promoting every doubtful word to a confirmed reading. The typed theorem statements isolate every hypothesis actually used.
- Renewed searches: `"divided power" "acyclic models" algebra`; `"cohomological theories" Cartan uniqueness divided powers integral`; `"commutative differential graded" "divided powers" "model structure"`. Results suggest DG divided powers, shuffle algebra model structures, and Tate acyclic closures, but none has yet supplied an applicable strict integral comparison theorem.

- Finite-prime theorem literature search before stating C17: `"arithmetic square" "divided power"`; `"cohomological theories" "localization" Cartan`; `"de Rham" "admissible" "uniqueness" integral simplicial`. No directly applicable strict-PD generalized-theory uniqueness theorem was located. C16--C17 are proved in full here; no priority is claimed. The arithmetic exact sequence and simplicial path calculations are derived explicitly, not imported from an unverified model-category theorem.

## Nonlinear closures and the global partial model, 2026-11-19 08:10--08:25 UTC

- Routine searches `"acyclic" "divided power" "Cartan" construction`, `"divided power" "acyclic closure" functorial`, and `"commutative cochain" "divided powers" resolution` were verified by stronger primary-source searches for Cartan constructions and divided powers.
- Opened Cartan, *Constructions multiplicatives*, Seminaire1954/55 expose4, https://www.numdam.org/item/SHC_1954-1955__7_1_A4_0.pdf, especially Section2 Theorem4 (printed4-03--4-04); and *Puissances divisees*, expose7, https://www.numdam.org/item/SHC_1954-1955__7_1_A7_0.pdf, especially Section1 Theorem1 and Sections2,4. These are homological bar constructions; no positive-cochain strict comparison theorem was imported.
- Opened Richter, arXiv0811.4704v1, https://arxiv.org/html/0811.4704v1, Introduction and Sections2,7--8 scope. Its transferred nonstandard monoidal product and chain-complex divided powers do not provide the missing nonnegative cochain replacement automatically.
- Opened Stacks tag0GZ3, https://stacks.math.columbia.edu/tag/0GZ3, Lemma23.12.1 and proof. The page explicitly uses homological Tate resolutions; it assumes a Noetherian ring and a finitely generated ideal. Those hypotheses and grading differ from the present S=Gamma_Z(T) and positive-cochain problem. No application is asserted.
- C18 is proved directly in sections/C_repairs.tex, with independent root and B audits. C21 is proved in notes/C_global_partial_model.md and is undergoing independent audit. Neither auxiliary construction is presented as a complete integral C3 comparison.

## Signed shuffle and relative bar property, 2026-11-19 08:45--08:54 UTC

- Searched `"shuffle algebra" "divided power" "Lyndon"`, `"graded shuffle" "divided powers" free`, and `"bar construction" "divided power algebra" "free" Cartan`, then stronger primary-source searches for signed/super Lyndon freeness.
- Opened Melancon--Reutenauer1989, primary author PDF at the URL in C_references.bib, Section4 printed589--590. The exact unsigned triangularity and integral PD corollary were read. C24 derives the signed version, including odd Lyndon squares, rather than treating it as an assertion of that source.
- Opened Nuiten, *Formal moduli problems and derived Lie algebras*, https://www.math.univ-toulouse.fr/~jnuiten/Writing/DerivedLie.pdf, printedp11, proof of Proposition4.6: equations4.8--4.9 and the following paragraph recall unsigned shuffle PD freeness and mention the integral Lyndon proof. Its global setting is a field of characteristic p; no integral strict-PD comparison is imported.
- Source fetch is preserved as code/C_fetch_shuffle_source.py and logs/C_shuffle_source_fetch.json when complete. The signed exact certificate is code/C_signed_shuffle_checks.py, with full output logs/C_signed_shuffle_checks.json. C24 has independent root and D audits and is integrated in sections/C_bar_relative.tex.

## 2026-11-19 09:18--09:20 UTC: cotangent-amplitude and tangent-category search

Queries: "divided power cotangent complex truncated divided polynomial algebra homology";
"Gamma algebra Andre Quillen homology truncated divided power algebra cotangent complex";
"divided power cotangent truncated"; "Quillen cohomology divided power special derivations".
Used both available search engines; then opened primary arXiv HTMLs.

Opened Dokas--Frankland--Ikonicoff, arXiv:2403.18049v2, full HTML
https://arxiv.org/html/2403.18049v2 (web turn224704702view0), contents and
sections on Beck modules/derivations. It constructs Quillen cohomology
for divided-power algebras over an operad over a field. It does not state
the strict integral positive-cochain common-source theorem. Root has
independently opened v3 and is responsible for its bibliography entry.

Opened Ikonicoff, arXiv:2508.16302v1, full HTML
https://arxiv.org/html/2508.16302v1 (web turn224704702view1), Sections1.3--1.5
and6.3 (lines182--214 and614--616 in web extraction). Beck modules carry
an additional p-semilinear operation, and the special/inner derivation
case has additional restrictions. The paper explicitly describes a
future relation to crystalline de Rham theory rather than providing the
strict comparison required here. No theorem from it is imported.

Found Brantner--Taelman, "Deformations and lifts of Calabi--Yau varieties
in characteristic p", arXiv:2407.09256v3, with indexed Proposition4.39
on the first PD cotangent homotopy group I/I^[2]. Attempt to open its
primary v3 HTML failed with DisabledError. The indexed first-homology
formula was therefore not used as a checked theorem and supplies no
higher-amplitude bound. A complete primary read would be required before
any use.
