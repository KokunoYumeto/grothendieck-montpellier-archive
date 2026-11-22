# Part D supplementary search record

We record exact queries and the primary-source conclusions that affected the
research. Existing `fetch_sources.py`, `extract_sources.py`, their outputs,
and the additional/third acquisition JSON files document earlier retrievals.
Search snippets served only to locate primary texts; no theorem is justified
by an unopened snippet.

## Fixed-boundary finite generation, 20 November 2026, 01:51–01:57 UTC

Engine 2 queries:

- `"fundamental group" "finitely generated" "proper" "codimension two" characteristic`
- `"tame fundamental group" "non-projective" normal`
- `"fundamental group" "normal compactification" "finitely generated"`

Engine 1 verification queries:

- `"fundamental group" "proper" "normal" "codimension" "finitely generated"`
- `"tame" "fundamental group" "fixed compactification" finite generation`
- `"nonprojective" "fundamental group" characteristic p`

We opened Esnault–Srinivas, with Bost's appendix, *Simply connected varieties
in characteristic p > 0*, author's PDF
<https://page.mi.fu-berlin.de/esnault/preprints/helene/113-ES_B.pdf>.
The abstract explicitly requires a normal **projective** compactification;
Section 2 begins with that same assumption. Its generic hyperplane argument
in Lemma 2.2 and its following proof supports the geometric-generic-curve
method, but it does not remove the nonprojective residual gate. We therefore
do not cite this paper as solving that gate.

We reopened AHLS2026, source `arXiv-2-pit-schemes.tex`, comparison discussion
in §2.2 and Theorem2.6.1. Divisor tameness explicitly tests divisors on every
normal compactification. The normal-crossings fixed-boundary comparison is
Proposition2.2.3. This does not imply the general fixed singular compactification
claim. Suzuki2023, source Introduction, Conjecture1.1 and Theorem1.2, explicitly
retains the full punctured-spectrum finite-generation conjecture and proves
only its pro-nilpotent quotient. We make no claim that our global residual
question is equivalent to that local conjecture.

We also opened the Esnault–Kindler erratum, dated 29 September2016,
<https://page.mi.fu-berlin.de/esnault/preprints/helene/118b-EK.pdf>.
Its corrected statement of Theorem6.1 requires the test curve to be a complete
intersection of ample divisors. We do not invoke the uncorrected statement
for arbitrary curves. Our projective proof instead uses the generic Bertini
argument with the precise SGA1 X2.10–2.11 and XIII2.12,5.2 references.

Failed construction routes examined:

- A finite wild quotient of a proper regular variety cannot refute D2(ii):
  purity upstairs and finite effective descent prove finite generation.
- A projective modification does not preserve the fixed-divisor condition:
  exceptional divisors lying over a codimension-two omitted set are new
  places at which wild inertia has not been killed.
- Contracting the sole boundary of an affine-line fibration cannot produce
  a normal proper compactification with codimension-two complement if the
  original open has nonconstant global functions: normality and codimension
  two would force those functions to extend to the proper variety. This
  excludes a direct attempt to transport the infinitely generated group of
  the affine line into the desired geometry.

## Parent-requested graph audit, 20 November2026, around02:00 UTC

Engine2 queries:

- `"normalized graph" "abelian" "geometrically normal"`
- `"rational map" "abelian variety" "imperfect" normal`
- `"Albanese" "geometrically normal" graph normalization`

The AIF PDF <https://aif.centre-mersenne.org/item/10.5802/aif.3721.pdf>
returned403 on opening. We instead opened the authors' primary predecessor
<https://www.math.colostate.edu/~achter/math/algrep1119.pdf>,
*A functorial approach to regular homomorphisms*, TheoremA.3 and RemarkA.4,
printed p40, and TheoremA.18, printed p45. They give Albanese existence and
arbitrary base-change compatibility for proper geometrically reduced,
geometrically connected schemes. We passed this precise weaker hypothesis
to the PartB agent. It does not prove that a normalized graph is geometrically
normal, nor that such a graph lies in a class explicitly restricted to
geometrically normal models.


## 2026-11-20 02:19 UTC: exact arbitrary-base D10 closure
Opened primary SGA4 reedition directly:
- https://www.normalesup.org/~forgogozo/SGA4/09/09.pdf, IX Proposition2.11, originalp20 (re-editionPDFp12), exact arbitrary-scheme constructible specialization criterion. Proof explicitly obtains constructible isomorphism locus and neighborhood.
- https://www.normalesup.org/~forgogozo/SGA4/17/17.pdf, XVII Theorem5.2.6 originalp357: arbitrary proper-support base change. Cor5.2.8.1 originalp358: relative cohomological bound2d. Theorem5.3.6 originalp364: constructible cohomology for compactifiable fp morphism over arbitrary scheme; proof starts with affine reduction and noetherian approximation.
- https://www.normalesup.org/~forgogozo/SGA4/18/18.pdf, XVIII Theorem3.2.5 originalpp585–586 (re-editionPDFpp77–78): smooth compactifiable morphism over qcqs S; Rf! right adjoint f*(d)[2d]. No noetherian hypothesis.
Root proposed explicit R=V×kA (A eventually constant sequences) and boundary-finiteness condition; part D independently verified ring spectrum, localizations, all stalk computations, relative-duality signs/twists and complete criterion. C independently verified IX2.11 and XVIII3.2.5 plus the proof at02:20UTC.
Finite auxiliaries (not the infinite geometry itself) exhaustively checked by code/check_d10_nonconstructible.py in0.000967sec: rings of8..256elements, all idempotents and support localizations, F3[C2] orthogonal projectors, specialization stalk pattern.

## 2026-11-20 02:24--02:48 UTC: controlled Chow, explicit nonprojective surfaces, and Prop5

Opened and checked Raynaud, *Flat modules in algebraic geometry*, Compositio24(1),11--31 (1972), Chapter4 section4 Proposition5, printed p30:
https://www.numdam.org/item/CM_1972__24_1_11_0.pdf.
The entire prescribed quasiprojective open U is preserved by the blowup, whose centre is in X minus U. Part C independently checked the same primary statement. This supplies D:boundary-neighborhood.

Opened the primary author PDF of Schroer, *On non-projective normal surfaces*:
https://www.math.uni-duesseldorf.de/~schroeer/publications_pdf/on_non_proj.pdf.
The author publication list https://www.math.uni-duesseldorf.de/~schroeer/publications.html confirms the original journal publication Manuscripta Mathematica100(3),317--321 (1999); the later date in the author PDF is not used as its publication year. Sections2.2--2.5, author PDF pp3--4, give the mutation construction and the nonprojective two-centre examples. We compute their punctured fundamental groups ourselves, using SGA1 X Corollary1.7, pp264--265. Section3.1--3.2, author PDF p5, gives the Pic=0 contraction discussed as the next unresolved explicit test in notes.md.

Opened Lara--Srinivas--Stix (2024), primary journal PDF https://www.numdam.org/item/10.5802/crmath.518.pdf. Theorem2 requires properness of the scheme whose group is being studied; Proposition4 gives a finite-generation descent mechanism. Neither immediately treats our nonproper punctured open with uncontrolled exceptional boundary. We do not cite it as a solution.

Reopened the original Proposition5 context in inputs/RESEARCH_SA12_transcriptions/transcriptions/Codex_K29-02/K29-02_transcription.tex: scan191, axioms R1--R4; scans196--197, global bounded ranks, connected Galois objects, quotient system and the literally unwritten Prop5. These impose quasi-compactness of S, not of every Z_i or its quotient. The finite-realization version remains true, the natural unrestricted etale-stackified filtered union fails by D:prop5-counterexample, and D:prop5-completion proves the universal clopen-descent repair. C independently checked the source and both arguments.

All five primary PDFs requested by code/fetch_primary_updates.py downloaded successfully with HTTP200, and pdftotext exited0. Exact UTC, sizes and SHA256 values are in code/fetch_primary_updates_output.json; downloaded sources are SGA4_IX, SGA4_XVII, SGA4_XVIII, Raynaud1972 and Schroer1999. This locally preserves the opened source material. The initial attempt imported an unavailable requests module; the recorded successful implementation uses the standard-library urllib instead.

## 2026-11-20 02:50--02:56 UTC: finite local groups and fresh searches

Engine1 queries included `"fundamental group" "proper" "non-projective" "characteristic"`, `"fundamental group" "normal surfaces" "finitely generated"`, `"fundamental group" "proper" "smooth locus" "positive characteristic" "generated"`, and French/nonprojective variants. Engine2 added `"proper" "codimension two" "finite generation" fundamental` and `"wild inertia" "compactification" "finite generation"`. No general solution of the fixed-boundary residual gate was found. A recency-filtered engine1 search for local fundamental-group finite generation in2024--2026 again returned Suzuki's nilpotent-quotient theorem; this is not a proof of the full statement.

The strongly F-regular result found by those searches was opened in its primary source https://arxiv.org/pdf/1611.03884. Exact checks: Proposition3.2 pp3--4, Claim3.5 pp4--5, Corollary4.2 p6, both proofs pp7--8, and the explicit sentence on p2 removing quasiprojectivity. The source and PDF downloaded successfully to sources/BCGST2019/, with SHA256 metadata in fetch_log.json. The source file is tex/CoversOfFreg-Paper3.tex; its line142 expressly removes quasiprojectivity. The journal metadata is IMRN2019 no14 pp4325--4339, DOI10.1093/imrn/rnx253. The publisher webpage redirects to an inaccessible CDN, so all theorem checks use the opened primary arXiv source. Part C independently verified the same exact statements and our application to arbitrary codimension-two Y. This yields D:finite-local-groups, not merely an analogy.

For the B-agent's separate imperfect-field graph gate, opened Laurent--Schroer, *Para-abelian varieties and Albanese maps*, author PDF https://www.math.uni-duesseldorf.de/~schroeer/publications_pdf/ParaAlbanese_2.11.2023.pdf. Theorem10.2 and the introductory statement construct Albanese maps for proper algebraic spaces with H0(O)=k and appropriate families; no geometric-normal modification or graph theorem was found. Exact PDF searches for 'geometrically normal', 'graph', and 'modification' returned no matches. We reported this negative source check to B; no stronger assertion is inferred from the paper.

## 2026-11-20 02:58--03:00 UTC: all surfaces over Fbar_p

Engine2 query `"normal" "surface" "algebraic closure of a finite field" "projective"` led to Holschbach--Schmidt--Stix, *Etale contractible varieties in positive characteristic*, primary author PDF https://www.math.uni-frankfurt.de/~stix/research/preprints/HOLSCHBACH-SCHMIDT-STIX-contractible20131010.pdf. Opened Theorem13 and Remark14 pp6--7: they cite Artin1962 Cor2.11 for projectivity of every proper normal surface over Fbar_p. Their own theorem concerns etale 2-contractibility, not our full finite-generation assertion.

The original JSTOR English PDF https://www.jstor.org/stable/pdf/2372985.pdf redirected to an inaccessible summary. We instead opened the published Moishezon translation on MathNet, https://www.mathnet.ru/eng/mat359, full text https://www.mathnet.ru/php/getFT.phtml?jrnid=mat&option_lang=eng&paperid=359&what=fullt. Read Theorem2.9(B) on printed p12, its proof and Corollary2.11 on printed p13, and visually checked the p13 image. The corollary and proof exactly imply our surface field restriction. Bibliography explicitly records that this is the opened translation and that the original English was not opened.

### 2026-11-20 03:06--03:07 UTC
- Searched both engines for \"pseudo-proper\" with \"finitely generated\", \"etale fundamental\", and \"fundamental group\" \"finite type\". Primary hits Borne--Vistoli; Antei--Biswas--Emsalem--Tonini--Zhang; Tonini--Zhang establish gerbes or Tannakian descriptions, no located finite-generation implication. No such implication is claimed.
- Kollar arXiv2502.13800v1, PDF Section35 p11 and Section39 opened. Published metadata verified at Princeton author publication record: Pure Appl. Math. Q.22(2)(2026)647--673, DOI10.4310/PAMQ.250430140912. No geometric-normal graph theorem found.
- Artin1962 published translation success and hash now stored separately from the initial403 fetch attempt.

### 2026-11-20 03:10--03:20 UTC
- Searched exact phrases finite boundary/pronilpotent/proper fundamental group and punctured proper nilpotent fundamental groups. Found Suzuki2207.01563; reopened primary PDF v4 Theorem1.2 p2 and its local source labels0017/0018. No exact global finite-boundary corollary located.
- Opened Stacks04GG (finite henselian algebras),0BFK (normality ascent),0A3P (proper mod-p finiteness), with exact statements checked and source-download metadata attached.
- Opened Esnault2012 author PDF107-ecm120523.pdf, section3 p8 and reference18 to Kindler thesis. Thesis old author link times out; Kindler successor site inaccessible. These historical statements are not used to describe current theorem status.
- Searches on simple elliptic singularities and positive-characteristic local groups gave no full local finite-generation theorem; the analytic Heisenberg presentation was not transferred to positive characteristic.

### 2026-11-20 03:26--03:37 UTC: nonabelian constructibility and fixed tame smallness
- Opened Déglise's earlier author notes and ILO arXiv1207.3648v1, exposé XXI Theorem1.3 p389 and Lemma3.4(ii) pp394--395. The exact local TeX is sources/ILO2012/tex/exposes/finitude-non-abelienne.tex, labels21-groupes2 and21-devissage1. Both statements allow arbitrary finite G; C independently reopened them.
- Routine engine2 queries for the exact exposition title and 2014 metadata found the published chapter. Opened https://www.numdam.org/item/AST_2014__363-364__529_0.pdf and the Numdam chapter record. Theorem1.3 p529 strengthens the draft by dropping normality. Lemma3.2.1(ii) pp536--537 is the proper-composition lemma; section4.3 pp544--545 includes the critical codimension-two case. Page images529,536,537 checked, avoiding the OCR's incorrect strict greater-than symbol. Bibliography cites the published pp529--553 and distinguishes all draft locators.
- Opened Keith Conrad, Simplicity of A_n, https://kconrad.math.uconn.edu/blurbs/grouptheory/Ansimple.pdf, Theorem1.1 p1 and its proofs. This is the general group-theoretic input for the small alternating-product obstruction; finite computational certificates are reported separately.
- Opened Stacks0BRM (Lemma15.116.4, ramification-index form of Abhyankar),0EYG (Lemma58.31.5, regular-divisor form), and0EXT (the surrounding tame ramification section). Both exact proofs support the uniform Kummer construction.
- Opened William Stein's author-hosted Algebraic Number Theory: A Computational Approach, online version dated2012-09-24, section14.3 Theorem14.3.1 and proof: https://www.wstein.org/books/ant/ant/node95.html. The statement is for arbitrary fields with inequivalent valuations, so applies to boundary DVRs without an affine-neighborhood hypothesis.
- code/fetch_smallness_sources.py preserves the published PDF, Conrad PDF and the three Stacks pages, with HTTP200 and SHA256 metadata; the independent direct download of Stein's already-opened webpage returned403, which is recorded rather than concealed. Root independently opened the published theorem/lemma and both exact Stacks tags, and audited the actual proofs, before checkpoint05.
## 2026-11-20 03:39--04:03 UTC: residual finite generation and B cross-audit

- Queries combined `small fundamental group`, `proper`, `codimension two`, `nonprojective`, `finitely generated`, `pseudo-proper`, and `anti-affine`. No new primary theorem was found giving the required uniform generator bound. We did not use AI aggregation results.
- Opened Tanaka, https://arxiv.org/pdf/1502.01381, Lemma2.2(2) and proof, pp6--8; exact arbitrary field-extension normalization statement checked.
- Opened Kelly, https://www.ms.u-tokyo.ac.jp/~kelly/pdfs/uh%20non-fp.pdf, Corollaries19--20 and proof, p9; nilpotent-kernel condition checked.
- Reopened Milne, https://www.jmilne.org/math/Books/iAG2022.pdf, Section2i pp56--59, Theorem5.39 p108, Theorem8.27 pp154--155. Theorem5.34 p107 is a different assertion (monomorphism iff closed immersion).
- Reopened Kleiman, https://arxiv.org/pdf/math/0504020, Theorem5.4, Remark5.6 and Remark6.19. Geometrically normal proper Picard identity components are proper and the torsion component is finite type.
- Local source-retention script code/fetch_B_aux_sources.py completed successfully; exact SHA256 checksums and timings are in code/fetch_B_aux_sources_output.json.
- B.2r proof written as parts/D/B_aux_no_torus.tex for B to copy. Targeted actual-file B.2s audit passed, with its previously checked B.1g/B.2d and unreopened ACMV input explicitly distinguished.

## 2026-11-20 04:18--04:29 UTC: elliptic exceptional ramification

- Queried simple-elliptic finite covers, arbitrary-characteristic log-canonical surface classification, different exponent equality, and minimal resolutions. Opened Hara2015, https://www.ms.u-tokyo.ac.jp/journal/pdf/jms220106.pdf, Theorems1.1--1.2 pp194--195; the ordinary/F-pure distinction is not needed by the final proof.
- Opened Graf2021 primary publisher HTML, https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.12495. Its section7.8 cites Kollár's surface classification. We did not rely on that classification or import its main theorem's characteristic restriction.
- Opened Stacks0BUA and09E3 for inertia in imperfect residue fields; the final proof instead supplies a direct differential determinant calculation, avoiding any unverified perfect-residue hypothesis in a different theorem.
- Exact surface sources opened with proofs: https://stacks.math.columbia.edu/tag/0BGP (Theorem54.14.5), https://stacks.math.columbia.edu/tag/0C2M (Lemma54.16.8), and https://stacks.math.columbia.edu/tag/0C5R (Lemma54.17.1). These give arbitrary-characteristic resolution, contraction of rational(-1)-curves, and factorization by point blowups.
- Opened the publisher primary preview https://www.cambridge.org/core/books/abs/singularities-of-the-minimal-model-program/ancillary-results/746202C8C8DD774635E3DFA33D0C1FAB . Parsed lines480--484 explicitly restrict characteristic0 only after section10.1 and state Theorem10.1 negative definiteness for excellent surface morphisms. The complete theorem proof is not in the preview, and we do not claim to have opened it.
- Reopened local primary Schroer1999.txt, printedp5, section3.1: the divisor3B+2R0+2R1 constructs a projective contraction of exactly A union R2. B independently read this exact passage. Root and B audited the complete new proof fragment D_lc_elliptic.tex before integration.

## 2026-11-20 04:32--04:46 UTC: single-curve refinements and fierce ramification

- Reopened https://stacks.math.columbia.edu/tag/0BUA , Lemma58.13.5 and proof, for the absolute inertia exact sequence over any DVR. This supports the explicitly proved identity P_L=P_K intersection G_L in D:finite-exceptional-wild.
- Independently opened https://stacks.math.columbia.edu/tag/0C1D (Riemann--Hurwitz Lemma53.12.2), https://stacks.math.columbia.edu/tag/0CD0 (purely inseparable genus preservation Lemma53.13.5), and https://stacks.math.columbia.edu/tag/0CD2 (Frobenius/separable factorization Proposition53.13.7). These directly support C's weighted single-curve proof, copied after checkpoint06.
- Opened https://stacks.math.columbia.edu/tag/0C5P , Lemma54.16.11: a proper regular surface is projective. This supplies the global elliptic-boundary corollary.
- Searches combined proper/codimension-two/finitely-generated fundamental groups, nonprojective punctures, fierce surface ramification, and cone local fundamental groups. No general finite-generation theorem was located. We avoided AI-generated aggregation pages and did not transfer complex-analytic link presentations to positive characteristic.
- Opened Esnault--Kindler--Srinivas, https://page.mi.fu-berlin.de/esnault/preprints/helene/131_EKS.pdf (9pages), Theorem1 p2, Proposition2 pp3--5, Theorem8 p7. Publisher metadata at https://www.sciencedirect.com/science/article/pii/S002186931930167X confirms Journal of Algebra528(2019),250--259, DOI10.1016/j.jalgebra.2019.03.020. Its fierce-index bound fixes rank and a curve-wise Swan modulus; no uniform-all-rank claim is inferred.
- Opened https://stacks.math.columbia.edu/tag/0GS2 , Lemma58.9.2 and proof, for proper schemes over henselian pairs. Communicated the local-ring specialization tag0A48 to B for its prospective cusp argument. The cusp theorem itself is awaiting an actual-file audit.


### 2026-11-20 04:53 UTC — exact cusp and klt inputs
- Opened Stacks0A48, Lemma58.9.1, proper finite-etale comparison over a henselian local ring, full proof; also0GS2 Lemma58.9.2 for the henselian-pair variant. Exact source scope is used in D:cusp-tame.
- Opened primary published Carvajal-Rojas and Yasuda2025, Documenta Mathematica30,709–751, DOI10.4171/DM/1012, https://ems.press/content/serial-article-files/50862?nt=1 . Read Theorem5.3 at printedp739 (PDFpage30, parsedlines2145–2158), including all-characteristic remark; read Corollary6.4 at printedp741 (PDFpage32, parsedlines2284–2307), with its complete proof. Tool refs turn823895264view0, turn722612712view0. The mixed-boundary corollary uses local klt finiteness, not any unproved global quasi-projectivity.
- C's fierce-extension proof is direct algebra, not a literature-derived assertion. Read the actual source and full certificate, independently ran the copied D certificate; six q cases,1,029,677 assertions,0.5433858470059931s.

### 2026-11-20 05:03 UTC — all-lc and formal Picard source checks
- Read SGA1 reedition primary TeX, parts/D/sources/SGA1/smf_doc-math_3_01.tex lines25225–25415: XIII5.1,5.2,5.3, original pp428–430. The strictly local tame cover is dominated by a prime-to-residue-characteristic Kummer cover. Independently opened Stacks0EXT, full15.116.5–9, and exact0EXU/0EXV proofs (turn729835421view0/1).
- Independently opened exact Stacks0B5Y (ample iff positive degree on every reduced component, including nonreduced curves),0B5U (Serre vanishing),0C6R (first-order units/Picard sequence),02OC (formal functions),02KH (flat cohomology base change), reading full statements and proofs. Toolrefs turn834577093view0/1, turn762305454view0/1/2. These support the complete rational-tree class-group exponent proof.
- Opened Fujino authorhttps://www.math.kyoto-u.ac.jp/~fujino/logsurface27.pdf , version2012/4/2, fullLemma2.2 atpp6–7, parsedlines243–257; convention over C atp5, lines184–193. Refs turn919620361view1,turn432438884view0,turn799594003view0. logsurface25 first failed via web; versions24 and27 opened successfully. The characteristic-independent proof is supplied in our fragment and adds the explicit A² calculation; we do not erase the source's field convention.

### 2026-11-20 05:09--05:15 UTC: modern local/global finiteness
- Opened published Carvajal-Rojas--Stäbler (2023), Algebraic Geometry 10(6), 694--728, DOI10.14231/AG-2023-025, https://content.algebraicgeometry.nl/2023-6/2023-6-025.pdf. Downloaded full PDF and pdftotext under sources/CSK2023. Read Setup1.1 p694, TheoremA p695, Theorem3.7 and proof pp708--709, Theorem4.3/Cor4.5 pp713--714, and Cor4.7 p715. Full local group is finite prime-to-p, not merely its prime-to-p quotient; the tower theorem explicitly applies to normal integral excellent schemes and all cover degrees.
- Opened/downloaded Stibitz arXiv1707.08611, sources/Stibitz2017. Read Theorem1 pp1--2, all branch-stratification lemmas and Theorem2 pp4--6, and Section4 pp7--8. No quasi-projectivity hypothesis. The direct theorem states Z=Sing(X); our arbitrary-Y proof instead uses the independently published tower theorem and writes the relative cover argument in full.
- Opened Hoshi RIMS1558 (2006), https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1558.pdf, Proposition2.4 pp16--17 and PropositionA.10 pp57--58, including the latter proof. Confirms proper log product with connected log-regular second factor and the exact divisorial-generic-point tame category.
- Rechecked Suzuki arXiv2207.01563, latest verified v4 of July4,2023, published Journal of Algebra633 (2023),489--509, DOI10.1016/j.jalgebra.2023.07.005. Theorem1.2 remains only pronilpotent; targeted fresh searches found no full-generation theorem. This is a limit of the source search, not an assertion that no subsequent result exists.

### 2026-11-20 05:15--05:19 UTC: independent cone proof/source audit
- Read complete C/D_graded_cone_tameness.tex, including the final common-completed-boundary-DVR correction.
- Independently opened J.S.Milne, Basic Theory of Affine Group Schemes (2012), https://www.jmilne.org/math/CourseNotes/AGS.pdf, VI Theorem11.1 pp82--85, including the final arbitrary-Hopf directed-union argument at printedp85; no finite-type restriction is hidden.
- Independently opened Stacks0B3D (normal dimension<=2 implies CM),00R4 (miracle flatness),09XI (henselian-pair idempotent characterization); read published ILO XXI Theorem1.4 p529 in sources/Deglise2014_XXI.txt.
- Full actual-file audits received: root/B/D for both cone statements; root/B/C for D_Schroer_all_genera.tex. B explicitly did not reopen Hopf primary source and accepted root/C source checks; log preserves that scope.

### 2026-11-20 05:33 UTC: weighted extraction independent source audit
Opened and read https://stacks.math.columbia.edu/tag/0EGH (Veronese), /03GV (normalization and smooth base change), /02RS (42.18.1 norm formula), and /0BG4 (54.11.1 completed local rings and54.11.3 admissible blowup descent). Search tool refs turn414034168view0--3. These match the precise constructions in C's weighted extraction. The general regular-base-change tags0BFK/0H7S were C's independent reopenings, not separately reopened here.

### 2026-11-20 05:35--05:41 UTC: finite-group crown and cohomology primary sources
Opened the full published Lucchini--Marion--Tracey2020 PDF via Cambridge and Birmingham, especially Lemma2.5 pp10--11, Proposition2.4 p10, Proposition2.6 pp11--13, equations(2.1),(2.2) p12 and |Out(S)| boundp13. Web refs turn718725777view0, turn786864076view0, turn490100279view1, turn307849252view2. The PDF parser renders >= as >; the authors' own use s=2,d(L)=2 confirms the inclusive scope, and the downloaded arXiv text explicitly has >= at lines349/353. ArXiv PDF1807.05400 downloaded to sources/FiniteGroups/LMT2020_arxiv.pdf; it has earlier numbering Lemma3.1/Proposition3.2. Initial direct Birmingham download returned403 and the author Detomi--Lucchini PDF download returned503, although their sources were opened through search. Detomi--Lucchini Theorem12 p6 proves each crown finite using only finiteness of subgroups of fixed index, hence gives no uniform growth bound. Milne CFTv4.03 II1.11p62 andII4.2p87 were opened in full, refs turn307849252view0/1.

2026-11-20 05:53 UTC: independently opened and read Stacks0BMB Lemma58.21.4 (purity),0A48 Lemma58.9.1 (proper henselian finite-etale comparison),0EGH Lemma10.56.2 (Veronese generation), all full proofs, for B source-resolution/pro-two audit. URLs https://stacks.math.columbia.edu/tag/0BMB ; https://stacks.math.columbia.edu/tag/0A48 ; https://stacks.math.columbia.edu/tag/0EGH .

2026-11-20: independently read Hoshi2006 primary RIMS1558 text lines598-803 (Proposition2.1 and Theorem2.3, printedpp13-16) and2985-3050 (PropositionA.10,pp57-58); full opened PDF https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1558.pdf . Independently opened full primary Stacks0BXT,0B8Y,0EXY,0EYD,04DY for generic normalization, curve smoothness, arbitrary DVR tame pullback and universal-homeomorphism invariance.

2026-11-20 06:02 UTC: independently opened/read complete primary Stacks0BTX Lemma58.14.3 and056V Lemma33.25.7 for C generic-fibre audit. URLs https://stacks.math.columbia.edu/tag/0BTX ; https://stacks.math.columbia.edu/tag/056V . Earlier same-day exact normalization/tame base-change source checks reused without re-reading.

2026-11-20 05:55–06:04 UTC: searched primary local finite-generation and quantitative ramification literature. Reopened Suzuki2023 source introduction Conjecture1.1/Theorem1.2 and AHLS2026 scheme section: the former is pronilpotent only; the latter explicitly uses all centered valuations. Opened/downloaded Hu–Teyssier2502.11064v3 (31July2026), fullPDF372290bytes, exact introductionpp2–5;2502.11060v1,622727bytes, Definition7.3/Proposition7.4p32 andDefinition7.12/Theorem7.15p33; author-published Esnault–Srinivas2021 offprint326552bytes and its complete small erratum107595bytes. Source records are in sources/HuTeyssier2025_2026/source_record.json. Search hitv1 of2502.11064 was superseded by explicitly checkedv3 after the abstract page disclosed the finite-coefficient correction. No general crown bound follows from these statements.


### 2026-11-20 06:12–06:16 UTC — exact projective and logarithmic sources
- Opened and read full primary Stacks0BFP, Lemma33.17.3, including all four cases and proof; supports codimension-one isomorphism locus in C's projective-target fragment.
- Re-read local primary AHLS2026/arXiv-3-fg-pi1-log.tex: type-Vd inclusion lines24–27, Proposition3.1.8 lines86–101, Definition3.2.4 lines167–178, Theorem3.5.1 lines460–465 and full proof548–555, plus the intervening formal-gluing proof. The numbered locators were checked against the main source theorem-counter definitions.
- Re-read full Hoshi2006 PropositionA.10 and proof, author preprint pp57–58, local B text lines2985–3050. Its definition explicitly tests the original points with dimO_X,x=1.
- Earlier direct arXiv PDF open for2608.12601 returned DisabledError; the complete downloaded primary arXiv LaTeX source was used instead.


### 2026-11-20 06:18–06:22 UTC — projective-base and formal-cone primary audits
- Reopened/read full Stacks09EE Lemma15.114.5, including the April2026 correction and complete proof. Full wild order is e_p times inseparable residue degree; the action-trivial-mod-m² characterization requires separable residue and is not used here.
- Reopened/read09EB Lemma15.114.2 and full0BUA Lemma58.13.5, including finite-level wild surjectivity and the final inverse-limit argument.
- Reopened/read03GV Lemma37.19.2 and02VN Lemma35.23.31 in full for the smooth-normalization/fpqc descent step.
- Reopened/read09ZT Lemma30.28.2, including algebraization of the finite algebra multiplication/unit, and0BG4 Lemmas54.11.1–3, including actual completed local ring comparison. These support the independent actual-file audit of B's first three finite-cone statements.


### 2026-11-20 06:27–06:33 UTC — retractions, torsion and tower checks
- Read full primary Stacks04FF Lemma37.8.7, including proof, for unique compatible etale lifts giving a formal retraction.
- Read03PK Lemmas59.28.1/5 and0A3J Lemma59.63.2 with its full polynomial proof and the Artin-Schreier exact sequence, for torsion and coherent obstruction killing.
- Read0A22 Lemma33.43.4 and proof, with preceding33.43.3, for proper curve projectivity in the iterated-fibration theorem.
- Reran the16-assertion companion under D after reading its code; output preserved. Root's independently supplied run record was located at code/output/finite_cone_genus2_root_check.run.json.
