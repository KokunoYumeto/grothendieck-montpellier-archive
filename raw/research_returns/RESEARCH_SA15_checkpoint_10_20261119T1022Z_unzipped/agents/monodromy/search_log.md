# Part A.3--A.5 search log

2026-11-19: searches on Hasse-Witt monodromy, plane curves, p-rank, ordinary hypersurface sections; located Koblitz (1975), SGA 7 XXI, Illusie (1990), Stienstra--van der Put--van der Marel (1991), Tian (2009).


## Retained searches and source inspections, 03:00–05:49 UTC

The early search wording was not fully retained; theorem-specific inspections are recorded in CHECK_EVENTS.tsv and the opened/not-opened notes in references.bib. The following later queries are retained exactly:

- `generic p-rank curves ample linear system smooth surface Hasse Witt nonreduced Picard ordinary hypersurface sections`.
- `Koblitz revised conjecture generic invertibility Hasse Witt smooth variety hypersurface sections counterexample`.
- `hypersurface sections arbitrary variety point counts all residues modulo p monodromy Hasse Witt Koblitz Katz`.
- `generic hypersurface sections Hasse Witt monodromy all traces finite field residue characteristic p`.
- `Frobenius splitting Hom F_* O_X omega_X 1-p duality smooth trace proposition`.
- `site.stacks.math.columbia.edu Frobenius dualizing sheaf Cartier trace`.

Primary works inspected and actually used:

- Koblitz1975, complete paper: I§5 Theorem1 p139 (rendered), Theorem2 p141, I§6 Theorem3 p142; II§3 pp149–151 is a revised conjecture, not an exact arbitrary-X rank result.
- Achter–Pries arXiv0707.2110v2 Proposition4.8 p16: monodromy over p-rank strata of curve moduli. Plane pullback requires a separate argument; quartics use the canonical-model PGL3 torsor.
- Katz SGA7II XXII Proposition2.0 and Corollary3.2 pp410–411; https://web.math.princeton.edu/~nmk/old/congzeta.pdf. Lang comparison and proper coherent trace formula, including nodal curves.
- Katz–Sarnak1999 Theorem9.7.13 p290, hypotheses9.7.1–9.7.9; https://web.math.princeton.edu/~nmk/RMFEM.pdf. Constant-field cosets tracked explicitly.
- Kantor–Seress2001 Theorem3.6 printedp22/PDFp25; https://pages.uoregon.edu/kantor/PAPERS/ksfinal.pdf. Downloaded and rendered; image retained in outputs. Used only for odd-characteristic transvection classification under the exact irreducibility/full-transvection hypotheses.
- Christ–He–Tyomkin2023 corrected publisherPDF MainTheorem p2, Proposition2.7 p8, Corollary5.3 p27; DOI10.1007/s10240-022-00135-x. Used in the independent plane theta/contact proof, superseded for group computation by elementary projective-space quadric swaps.
- Churikov–Vasil’ev–Zvezdina arXiv2202.09705v3 Lemma3.3 p6, and Basheer–Moori Table1 p3. Hering original publisher endpoint unavailable; not claimed directly inspected. These group classifications occur only in the earlier independent plane argument.
- Kothari arXiv2304.07628v2 Theorem3.3 p6, Proposition3.4 pp6–7, Corollary3.7 p9; published JTNB38(2)341–353 (2026), DOI10.5802/jtnb.1364. Quotient smoothness and finite-group-scheme construction; no assertion that the complete-intersection torsor is smooth.
- Edixhoven–van der Geer–Moonen, Abelian Varieties, Chapter5 Propositions5.19,5.20,5.22, Definition5.23; https://van-der-geer.nl/~gerard/AV.pdf. Frobenius/Verschiebung duality, degree and p-rank.
- Cotner–Zavyalov2024 publisherPDF Definition2.2.1/Theorem2.2.3 p1854: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8556201EDB51D7F2F76F5950A800CD64/S0010437X24007231a.pdf/lefschetz_theorems_in_flat_cohomology_and_applications.pdf. Independently audited root’s A1 all-degree CI/W2 ranges.
- Entin arXiv1805.05454v3 Proposition3.1 pp7–8 and Theorem2 p3; https://arxiv.org/pdf/1805.05454. Joint symmetric monodromy from two-point irreducibility and isolated simple collisions. Published IMRN2021(14)10409–10441, DOI10.1093/imrn/rnz120.
- Stacks Lemma41.20.5 Tag0BTN and Lemma58.8.2 Tag09ZS, full proofs: https://stacks.math.columbia.edu/tag/0BTN and https://stacks.math.columbia.edu/tag/09ZS. Finite part of a quasi-finite etale map over a henselian pair and equivalence of finite-etale covers. Root independently reopened both.
- Stacks Remark48.20.12 Tag0AX4 and Section49.5 Tag0FKW, finite duality used for normalization/conductor calculations.
- Brion–Kumar2005 author-hosted full book, Lemma1.3.6 p26, Proposition1.3.7 p27, Theorem1.3.8 p28; https://www-fourier.univ-grenoble-alpes.fr/~mbrion/fbook.pdf. Cartier trace, finite-Frobenius duality and evaluation at1; root independently opened.
- Sannai–Tanaka arXiv1411.5294v5, Lemma4.5 p11, proof inspected; https://arxiv.org/pdf/1411.5294. Ordinary abelian F_*O decomposition. Publisher page opened and metadata confirmed: Math.Ann.366,1067–1087(2016), DOI10.1007/s00208-015-1352-3.

Additional opened source, not used as an input to a proved result: Grammatica, arXiv2510.03001v1, full36-page PDF at https://borowiecki.dev/pdf/2510.03001, Theorems1.2/3.16,1.3/3.18,1.4/3.29 and §3.3 Theorems3.21/3.24. Formal smoothness and crystalline/etale torsion; referred to root as a possible A6 lead, with no inferred theorem beyond the inspected statement.

### 2026-11-19 06:28 UTC: exact matrix algorithms and next structural gate

Opened original Stacks tags037P (Lemma10.47.8),037Q (Lemma10.47.13),030W (Lemma10.44.2),030X (Lemma10.44.3) for finite constants, geometric irreducibility and separability. Parent independently opened all four. Queried Chai p-adic monodromy author PDF (403, not read). Opened Banerjee–Salter arXiv2512.04018v1 full PDF: TheoremA printedp1 is complex, simply-connected surface, 6-jet-ample times very ample; it does not apply to characteristic p product abelian surfaces. Its local implantation idea suggested a separate plane-bubble construction, currently unproved. Queried irreducible groups generated by transvections characteristic2 and Kantor/McLaughlin. Reobtained exact Kantor–Seress Theorem3.6 printedp22 from primary author PDF indexed text, and retained prior locally rendered original page. Classification in dimension>=3 consists of SL, Sp, and at fieldF2 orthogonal/symmetric groups. All alternatives to SL in the F2 case preserve a nondegenerate alternating form. No classification assertion has yet been applied to the ordinary-product full group.

### 2026-11-19 06:47 UTC: full product groups

Opened original Stacks0BMB Lemma58.21.4 (purity) in full; reread original0BTN and09ZS for the strict-henselian finite Lang subgroup. Reused visually opened Kantor–Seress original printedp22 Theorem3.6; primary web fetch fails because57MB, indexed exact theorem and local original both available. Full theorem product_full_groups.tex and exact code product_char2_group_certificates.py independently audited/rerun by parent. No additional classification theorem is assumed: socle/Clifford multiplicity, imprimitive wreath exclusion, form uniqueness, and translation fullness are proved in the text, H1 uses the earlier elementary transvection proof.

### 2026-11-19 07:13 UTC: uniform product reduction

No additional unopened theorem was introduced. Primitive-prime group criterion uses the already opened Kantor–SeressThm3.6; the degree3 prime is independently certified by trial division. Jet separation, nodal discriminant and joint tangency incidence are proved directly. Uniform ordinary-product invariant calculation uses finite Cartier duality already opened in Brion–Kumar and ordinary elliptic Frobenius splitting already opened in Sannai–TanakaLemma4.5; stability and scalar endomorphisms of odd-degree rank-two pushforwards are proved by adjunction and degrees. Root audited entire file; reduction_descent independently audited uniform transvection propagation.

### 2026-11-19 07:52 UTC: irreducible Hasse gate

Queried Hasse-Witt monodromy hypersurface abelian surface; p-rank linear system abelian surface monodromy; symmetric Cartier Hasse determinant irreducibility; symmetric determinantal reducible decomposable; Hasse invariant linear system irreducible surface. No directly applicable opened theorem was found. Indexed Kerner material on determinantal decomposition may be relevant, but has not been used. The conditional reduction is proved from the previously opened classification and elementary sheaf/group arguments, independently audited by root. A possible global symmetrization route was rejected by exact one-factor linear-system calculations (cartier_symmetrizer_probe.py).

2026-11-19 07:58–08:02 UTC: searched nonordinary linear-system irreducibility, p-rank g-1 moduli irreducibility, Cartier bilinear-pairing Hasse determinant irreducibility on abelian surfaces, and characteristic-two commutative nonassociative multiplication determinants. Search results did not provide an applicable primary theorem; no result used. Do not extrapolate moduli-stratum irreducibility to this restricted family.

2026-11-19 08:32–08:41 UTC: searched Chai ordinary Hecke-orbit density / elliptic prime-to-p isogeny orbit and geometric irreducibility of fibres. Opened Oort2009 original report §3a p1 (elliptic density), Stacks0553/0559 Lem37.27.5 full statement/proof, and original Chai1995 full indexed author-PDF text via search+find+open, Theorem2 printedp477. Direct ChaiPDF open returned403; successful full indexed refs turn359103300view3, turn111590792view0. These new sources apply only to the separately marked isogeny candidate.

## 2026-11-19 09:53:06 UTC — renewed A4 literature search

Queries (system2): Hasse Witt monodromy linear systems curves abelian surfaces supersingular; p-rank strata curves on abelian surfaces monodromy; irreducibility Hasse invariant linear system abelian surface. Verification queries (system1): Newton strata realization for hypersurfaces2026 (recency30); monodromy linear system p-rank abelian; Hasse irreducible abelian surface linear. No retrieved theorem determining our fixed-linear-system images. The Achter–Pries moduli-stratum theorem is not transferred to a fixed surface family.

Opened primary publisher full text: Batubara, Garzella, Huang, Mellberg, Newton strata realization for hypersurfaces via explicit p-adic cohomology, Research in Number Theory12,110 (published16November2026), https://link.springer.com/article/10.1007/s40993-026-00802-6 ; source refs turn640040335view0/turn640040335search0. Read abstract and introduction through§1.5. It concerns computational zeta functions and explicit Newton-polygon examples, principally7<=p<50, not a fixed-linear-system Hasse-Witt monodromy theorem. Not used as a proof input.

## 2026-11-19 10:02:00 UTC — theta symmetrizer primary inputs

Opened author source https://www.math.ru.nl/personal/bmoonen/BookAV/ThetaGr.pdf (turn642022372view0), read Theorem8.28/description8.29 via turn120635906view0/view1 and full local AV text; requested rendered pages122–123 via turn217075943view0/view1. Read8.20,8.24pp119,121 and9.17pp133–134 in retained full AV source. Opened Laszlo–Pauly author paper https://math.univ-cotedazur.fr/u/pauly/actionfrob.pdf (turn642022372view1),§2pp2–3, especially relative Frobenius andTheorem2.5; not used instead of the explicit level3 construction. Opened Oda original publisherPDF from root ref turn230619289view0, obtained turn414897521view0, read§1pp43–45/Theorem1.2(i)p45. Added Oda1971 bib entry and exact AV opened-locator notes.

## 2026-11-19 10:08--10:12 UTC: ordinary ppav surface extension
- Queries: `site.math.upenn.edu chai density_hecke_orbit "Theorem 2" ordinary`; `site.math.upenn.edu chai density_hecke_orbit "smooth" "irreducible"`.
- Reopened original Chai1995 indexed full text, https://www2.math.upenn.edu/~chai/papers_pdf/density_hecke_orbit.pdf, refs turn836764717view0--3. Read Theorem2 printedp477 (lines1575ff), introduction's orbit definition and all-algebraically-closed-field scope (printedpp439--440). New use is g2 fixed3-power polarized Hecke density, not only prior g1 use.
- Opened BrianConrad author exposition https://math.stanford.edu/~conrad/papers/cmchina.pdf, refs turn969414238view0--1. Read Definitions7.3.8/7.3.10 and exact Theorem7.3.11 printedpp75--76: smooth geometrically irreducible fine full-level-n ppav moduli and universal family in arbitrary characteristic prime to n. Original MumfordGIT/FaltingsChai proof not newly read; citation explicitly records opened exposition rather than original proof.
- Full candidate ordinary_ppav_surface_full_groups.tex written with exact fixed quotient, all d>=2 Hasse irreducibility/common-kernel result, moduli-open/odd isogeny naturalGL8block, eventual full groups and arithmetic S3-character action. Parent passed firsthalf; fullfile root/OC/RD audits requested. Visible status remains Candidate until explicit full pass.
