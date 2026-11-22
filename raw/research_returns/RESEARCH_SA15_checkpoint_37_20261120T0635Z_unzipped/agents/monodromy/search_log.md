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

## 2026-11-19 10:34--10:38 UTC: induced polarization and universal ppav ranks
- First Numdam item/PDF URLs failed in the web tool; read the author's saved original PDF and its text locally.
- Opened author primary PDF https://www.math.ens.psl.eu/~debarre/25.pdf (turn609416955view0), Debarre1994 Degrees of curves in abelian varieties. Read§3.1--3.3 printedpp346--347; rendered and visually inspected both exact pages (outputs/source_debarre-05.png and-06.png). Formulaα(C,Θ)=[m] forC~mΘ onprincipal surface and equation3.3 give the induced Jacobian polarization identity; characteristic scope is anyalgebraicallyclosedfield, explicitlystatedp346.
- Independently audited OC universalppavrank proof/code and root arbitrarynil-length nonordinarycovector proof/code. Full details and exact rerun times in CHECK_EVENTS.tsv; no inferencefromfinite samples replaces the analytic universalproofs.

## 2026-11-19 11:04--11:06 UTC: uniform nonordinary monodromy gate
- Exact search queries: `"p-rank" "linear system" "abelian surface" monodromy`; `"Hasse-Witt" "monodromy" "abelian surface"`; `"supersingular" "Hasse divisor" curves linear system`; then stronger-engine verification `"monodromy" "Hasse-Witt" hypersurfaces` and `"p-rank" curves "abelian surface" linear system monodromy`.
- No source located that supplies fixed-linear-system full monodromy on the supersingular product. Search surfaced Tian2009 universal HW-cyclic Barsotti--Tate deformation monodromy again (publisher result turn468285532search1); universal-deformation versality is not established for the present fixed-surface family, so this is not used to transfer monodromy. Other hits concerned moduli p-rank strata or period/Hasse formulas, not the needed fixed-family theorem.
- Local self-tacnode criterion fully audited by root and RD; direct Cech, dualizing and coefficient proofs retained. Its remaining global incidence gate is explicitly separate.

### Explicit rename record, 2026-11-19 11:06 UTC
`supersingular_self_tacnode_candidate.tex` was renamed to `supersingular_self_tacnode.tex` after complete independent root and reduction/descent proof audits. The mathematical proof was retained; visible status changed from Candidate to Proved under the stated hypotheses, and the three local labels lost their candidate suffix. The unresolved global incidence paragraph was retained. No mathematical passage was discarded.

## 2026-11-19 11:14--11:15 UTC: independent E2 source audit
- Attempted original https://arxiv.org/pdf/2303.16083v1 via web open (turn740090953view0); fetch disabled. Read saved original Jiang text in OC sources instead, exact Theorem2.1/Remark2.4pp16--17,Prop6.2/Thm6.3pp32--34 and AppendixB definitions/B.5pp43--45. Read Tonini--Zhang retained original Theorem6.8(3),(4) and proof throughLemma6.15pp22--25. No successful new web fetch claimed.

## 2026-11-19 11:25--11:26 UTC: full coherent Noetherian E2 audit
Opened Stacks https://stacks.math.columbia.edu/tag/00MA (turn304944007view0),00MB(view1),0H0L(view2), and read entire statements/proofs. These give completion exactness and finite-module tensor formula, flatness of Noetherian completion, and derived complete description of the formal category, respectively. Used in the independent full proof audit of OC E2_coherent_Noetherian_equivalence.tex.

### Explicit rename record, 2026-11-19 11:34 UTC
`supersingular_triple_point_candidate.tex` was renamed to `supersingular_triple_point.tex` after complete independent root and reduction/descent audits of both local lemmas. Proofs were retained, status promoted under the stated hypotheses, and local labels lost candidate suffixes. The global-existence cautions were retained. No mathematical passage was discarded.

## 2026-11-19 11:38 UTC: tangent-triple candidates retained before checkpoint freeze
Both finite searches and all global source/collision certificates passed, with complete code, fixed seeds and outputs in the agent directory. The first collinear trial accepted was section2; noncollinear section4 followed three rational rejections (one extra point in its intended fibre and two other triple fibres). Rational screening was used only to reject; geometric acceptance used allfour charts and144Groebner checks. These are audit-pending candidates, separate from the promoted local criteria and global mixed-contact03 lemma.

## Post-CP12 continuation 2026-11-19T11:53:28Z

Renamed `supersingular_global_tangent_triples_candidate.tex` to `supersingular_global_tangent_triples.tex` after complete parent and reduction-descent proof/program audits passed. The entire proof and all certificates were retained; only status, stable labels and the audit record changed. The dropped candidate filename is superseded, not a discarded mathematical argument.

Replaced the stale execution-status paragraph in `supersingular_level3_collision_reduction.tex`, which described only the first locally checked but globally failed contact candidate. Its failure is explicitly preserved in the new retained-failures remark and original outputs. Added the successful global contact03 and both tangent-triple references, the conductor stable-rank proof, and local graph-bundle multiplicity comparison; final audits requested before promotion.

Uniform-gate literature searches: system2 queries `p rank monodromy hyperplane sections abelian surface characteristic p Hasse Witt` and `monodromy etale p torsion Jacobians curves linear system surface characteristic 2`; then system1 queries `"monodromy" "Hasse-Witt" "surface"` and `"p-rank" "linear system" abelian surface monodromy`. Results mostly returned moduli p-rank monodromy and modular/Hecke families, not the fixed linear-system theorem needed here. No new theorem imported or extrapolated. Returned primary-author Chai Methods for p-adic monodromy at https://www2.math.upenn.edu/~chai/papers_pdf/padicmono_v34.pdf remains NOT OPENED in this search; Achter--Pries moduli paper was already opened earlier and cannot by itself determine this fixed-family image.

2026-11-19T11:54:40Z: Parent completed final whole reduction proof audit and authorized promotion. Replaced only its final-audit-pending status; all three witness conditions and full proofs retained. The superseded candidate-suffixed labels were changed to stable labels, with cross-references updated in the global witness file. This proves degree3 Hasse geometry only.

2026-11-19T12:10:42Z: New candidate `supersingular_uniform_contact_candidate.tex` isolates a uniform local algebraic construction. Initial coefficient identities passed in0.2461678000036045s; executable rational-addition expansion was then added and the completed program passed in0.34270756500336574s. Both execution summaries retained. No source theorem imported; global nonemptiness and uniform images remain open.

2026-11-19T12:13:40Z: Independently opened https://arxiv.org/pdf/1504.07891 (Fisher2015, turn587898456view0), read original retained text Sec2p4,Lem4.2p8,Thm4.3pp9--10 and actually viewed sources/fisher_congr9_p9.png. Confirmed factor3 in printed equation11. Full corrected B37 audit and read-only exact rerun PASS; earlier withdrawn factor-omission argument was not used.

2026-11-19T12:27:46Z: After parent complete proof and code audits passed, renamed `supersingular_uniform_contact_candidate.tex` and `supersingular_uniform_source_smoothness_candidate.tex` to the same names without `_candidate`. The candidate filenames are superseded. All mathematical text was retained; statuses/labels were promoted and the local global-gap remark now refers forward to the proved source-smoothness lemma. The remaining other-collision and tangent-triple gates were retained explicitly.

2026-11-19T12:59:17Z: Post-CP13 continuation. New uniform collision-exclusion proof is a separate Candidate, not integrated or promoted; its exact polynomial certificate passed. Reread retained original Fisher Sec2pp4--5,Lem4.2p8,Thm4.3eq10/proofpp9--10 for B40; no new web retrieval claimed. Added actually opened OC AV Proposition5.26 p82 and Proposition11.21/Corollary11.22 pp167--168 to the canonical bibliography access note.

2026-11-19T13:04:25Z: Renamed supersingular_uniform_collision_exclusion_candidate.tex to supersingular_uniform_collision_exclusion.tex after complete independent root/RD/OC audits. All mathematical arguments retained; labels/status promoted, finite-flatness and etale-local cluster clarifications added. Updated two earlier uniform-contact forward references to this proved graph-kernel exclusion. Uniform tangent-triple gate retained. The original final tautological assertion in the small certificate was replaced by actual homogeneous-section substitutions; initial execution0.1605261920049088s retained separately, completed author0.19226371099648532s.

2026-11-19T13:04:25Z: Fresh primary opens for mixed nonproduct audit: https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf (turn989006160view0), https://van-der-geer.nl/~gerard/AV.pdf (turn989006160view1). Read Oda exactness/length dictionary3.14--3.18pp87--89, duality3.22p99, and actually viewed original100--101Riemann pairing3.24; read AV4.44--45p67,8.11p117,11.21--22pp167--168 full proofs.

2026-11-19T13:13:32Z: Retained exact initial executed source as code/history/ss_uniform_collision_identities_initial.py, reconstructed from the original tool patch after strengthening the final branch assertion. The initial hT+vF equality was tautological and was superseded by actual source/translated-section coefficient calculations; all previous meaningful checks remain. Original author runtime0.1605261920049088s and root initial0.19831534900004044s retained. No frozen paper edited.

## 2026-11-19T13:39:31.884873+00:00 — uniform tangent-triple promotion and retained rename

The complete root, reduction/descent and obstructions/crystals audits passed. `supersingular_uniform_tangent_triples_candidate.tex` is superseded by `supersingular_uniform_tangent_triples.tex`; the same complete proof is retained with proved status, stable labels, and two wording clarifications. No argument was removed. The odd-degree full-image consequence is being written separately and is not yet promoted. Original Kantor–Seress printed p.22 was actually viewed again for the exact classification alternatives.

## 2026-11-19T13:43:52.455792+00:00 — all-odd supersingular group assembly

Wrote `supersingular_all_odd_groups_candidate.tex`, with complete arbitrary odd norm divisor analysis, degree obstruction, and exact transvection-group argument. It remains candidate pending parent/OC audits; RD complete source/proof audit already passed. No finite-degree extrapolation or new numerical witness is used. The even-degree uniform group remains a separate gate.

## 2026-11-19T13:46:06.367616+00:00 — all odd supersingular degrees promoted

`supersingular_all_odd_groups_candidate.tex` is superseded by `supersingular_all_odd_groups.tex` after complete root, reduction/descent and obstructions/crystals proof/source audits. Same arguments retained, visible status and labels promoted. Earlier degree-three and uniform-block scope paragraphs now point forward to the uniform odd theorem; no failed argument was deleted. The even-degree determinant/monodromy problem remains explicit.

2026-11-19T13:46:24.855251+00:00 — Replaced superseded open-gate scope sentences in the proved uniform contact, source-smoothness and collision-exclusion files by exact forward references to the now proved tangent-triple and all-odd-degree theorems. All mathematical arguments retained unchanged; even-degree scope remains unresolved.

## 2026-11-19T14:03:58.286110+00:00 — separate even-degree candidates after CP15 paper freeze

Created two separate TeX candidates, `supersingular_even_image_sheaf_candidate.tex` and `supersingular_all_even_groups_candidate.tex`. The first has root+OC complete mathematical passes; the second is under full review. Two exact exploratory pencil programs and their complete outputs are retained unchanged and are not used by the boundary degree proof. Promoted/frozen paper files remain untouched.

## 2026-11-19T14:08:44.668546+00:00 — complete supersingular product classification promoted

`supersingular_even_image_sheaf_candidate.tex` and `supersingular_all_even_groups_candidate.tex` are superseded by identically based proved files without the candidate suffix after root, reduction/descent and obstructions/crystals full audits. Their statements/arguments are retained, statuses and labels promoted, and the earlier open even-degree scope sentences now point forward to the completed theorem. This closes every degree on the fixed supersingular product, not arbitrary ambient varieties.

## 2026-11-19T14:32:38.652980+00:00 — mixed-product generic-modulus gate and independent audits

Completed full independent B47 and OC mixed thin-strip audits; exact reruns and scopes are recorded in CHECK_EVENTS.tsv. Fresh original Tate source: https://www.numdam.org/item/10.24033/asens.1162.pdf (web ref turn825177752view0); printed155--159 read, printed155 actually viewed. Local Illusie1979 original text 0§2.1.1--2.1.13 reread for Cartier conventions; no new remote open claimed.

Saved original mixed_degree_two_group_discovery.py/output and independent verify_mixed_degree_two_group.py/output. New complete generic_mixed_product_all_groups_candidate.tex is explicitly audit-pending and assumes ordinary j transcendental over F2. It does not reverse specialization or claim every algebraic ordinary modulus. No renamed or removed passage in this batch.

## 2026-11-19T14:40:12.014133+00:00 — independent group-source reread and universal mixed Pfaffians

Actually viewed original Kantor--Seress printedp22 Theorem3.6 again at14:32UTC. Saved the exact original inline Pfaffian exploration as code/explore_mixed_degree_one_pfaffian.py. Universal all-nine expansion confirms Pf8((Ro tensor J)M)=a³det(S)s. The initial verifier and debug/debug2 versions are retained under their exact names. Their symbolic diagonal trial failed because it was not on the relevant cubic: Ro is nonsymmetric. The corrected final verifier removes that unsupported point, uses Q=s^tR s^[2], and checks all nine identities, invertibility, gradients and separation from D. No fixed-modulus group claim follows. The failed-output summary and all code variants are retained.

## 2026-11-19T14:40:58.436146+00:00 — generic mixed all-degree theorem promoted

Root, RD and OC complete independent proofs/source/code audits all passed, including generic-image normality and explicit imperfect-base normalization. Renamed generic_mixed_product_all_groups_candidate.tex to generic_mixed_product_all_groups.tex because the proof is audited. The old filename is superseded, not mathematically withdrawn. Main label identifiers retain their historical -candidate suffix at the parent's explicit request to preserve already recorded numbering/audit maps; visible status is Proved. The final scope remark label is rem:generic-mixed-modulus-gate. Every fixed algebraic ordinary modulus remains explicitly unresolved.

## 2026-11-19T21:20:08.686834+00:00 — Brock–Howe primary-source census

Engine2 queries: supersingular genus 2 characteristic 2 quaternion automorphisms isogeny theta nodal curve; supersingular genus 2 characteristic 2 automorphism quaternion Q8 isogenies. Engine1 verification: "Purely inseparable Richelot isogenies" Brock Howe quaternion automorphism. Opened original https://arxiv.org/pdf/2002.02122v2 (26 March 2025), refs turn959246332view0 and turn576029226view0/1/2. Read exact Lemma2.1 automorphism statements and order-four argument printed pp4–7, and Lemmas3.2–3.4 with short proofs p9. Download and hash record outputs/brock_howe_primary_access.json; original PDF/text retained under sources/. Main Richelot theorem and Magma computations not independently audited. No odd norm nodality imported.

## 2026-11-19T22:41:01.097054+00:00 — Arbitrary odd neighbours: exact duality source scope

Read retained original `agents/obstructions_crystals/sources/edixhoven_geer_moonen_AV.txt`: Proposition5.31 and full proof pp85–86; Theorem7.5/Proposition7.6 and full proofs p100; Exercise7.7 statement p112; Theorem12.2 and Remark12.3 full proofs pp180–181. Exercise7.7 itself identifies only the reduced identity kernel, so the candidate supplies the stronger full connected-kernel argument: factor the dual restriction through the quotient by its reduced identity kernel, use universal projection formula to make the dual quotient injective, and invoke dual-isogeny degree equality to eliminate the residual finite kernel. No fresh external-source opening or image inspection is claimed.

## 2026-11-19T23:28:03.745136+00:00 — Exact polynomial software API

Opened the official python-flint0.9.0 nmod_mpoly documentation at https://python-flint.readthedocs.io/en/latest/nmod_mpoly.html, reading context construction/from_dict, gcd, context projection and resultant API entries with examples. Retrieval refs turn272091223view0 and turn877648473view0. This is software API access, not a new geometric source or a claim to have audited FLINT C internals. Exact environment and installation result retained in outputs/post_CP27_eleven_computation_environment.json.

## 2026-11-19T23:29:44.110768+00:00 — Bounded norm-eleven literature check

Engine2 queries: "supersingular" "11" "theta" "nodal" isogeny characteristic2; "genus two" "characteristic2" "eleven" isogeny. Engine1 follow-up queries: "supersingular" "genus-2" "11" "isogenies" "characteristic2"; "theta" "nodal" "11" "isogeny" "genus". Returned primary background includes Brock–Howe arXiv2002.02122 and Howe's ANTSXIV slides, Knutsen–Lelli-Chiesa Genus two curves on abelian surfaces, and Ibukiyama–Katsura–Oort1986. These were search-result leads only in this pass; no new full-source read is claimed. The known complex-general-surface scope of Knutsen–Lelli-Chiesa is not imported into characteristic2. No matching uniform fixed-surface norm-eleven nodality statement was located in these bounded searches, but no novelty or priority claim follows. Primary search refs turn366392293search6, turn366392293academia7, turn366392293search9, turn366392293search10.
