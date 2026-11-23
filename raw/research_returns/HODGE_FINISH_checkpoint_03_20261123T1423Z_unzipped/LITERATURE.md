# Literature and source audit

Audit date: 22 November 2026 (UTC).

The exact search queries and dates are in `workbench/records/search_log.tsv`. The opened primary sources, exact locators, publication status and byte hashes are in `workbench/records/source_audit.tsv`, with discussion in `source_audit.md`. No downloaded source or plain-text source extraction is included.

Main findings: Brünjes–Serpé is the arithmetic bounded-complexity predecessor. Cattani–Deligne–Kaplan's opening page already contains the Baire/degree/denominator/Chow mechanism. Recent Bhattacharjee–Bhattacharya preprints explicitly state qualitative finite-Hilbert-data criteria in Weil families. Markman's split-sixfold theorem is for every imaginary quadratic field; nine-field restrictions belong only to particular explicit estimates. The recent CM proofs are unrefereed and are optional context, not inputs to the main equivalence. The OpenAI split-eightfold manuscript was withdrawn and is not used.

Further targeted sources opened by the root: Deligne's revised 1982 notes, Proposition4.1/Corollary4.2 and Proposition6.1; Ballmann's Theorem5.42 and equation5.43 in the Oxford-hosted author text; Milne's Abelian Varieties, Remark7.3 and Theorem13.3; Rito–Roulleau–Sarti's Introduction and Theorem1; Beauville's A tale of two surfaces, §3; André1996, Theorems0.5,0.6.2 and Lemma6.3.2. These readings resolve the specific geometric or linear-algebra inputs, not complete source-proof certifications.

No claim of priority is made. A failed search is not evidence that a result is new.

## 23 November 2026: additional primary-source checks

The main author opened Galluzzi, *A geometric description of Hazama's exceptional classes*, Boll. UMI (8) 3-B (2000), 727–737, especially Propositions4.1–4.2 pp733–734; Noot, *On Mumford's families*, J.Pure Appl.Algebra157(2001),87–106, §1.1 and Proposition3.3; and Moonen–Zarhin, Math.Ann.315(1999),711–733, Theorem0.1(iii). Galluzzi's full primary PDF was available through the web reader but a local download returned503, so no local SHA is asserted. The original Hazama PDF could not be opened; it is not cited as directly checked in the paper.

The main author visually read van Geemen1996 printed pp617–623, including the general Gaussian period domain, section action, quadratic basis and theta multiplication formula (§3.5). The generic theta-null argument and full-minus-kernel identification are proved here, not attributed to van Geemen's fourfold cycle theorem. General-term searches of arXiv, journal records, author pages, ECCC and Hexagon found relevant theta literature but no opened source stating this complete eightfold assertion. No priority claim is made.

For the all-field sixfold bound, Perry arXiv2604.00511v2 Theorem1.2 and its §6.2 proof pp26–28 were opened in the primary PDF and the attached author TeX. Hotchkiss arXiv2212.10638v1 §4 Definitions4.5,4.16, Lemma4.6, Remark4.13 and Theorem4.17 were opened in the attached author TeX. Their root-gerbe conventions were checked against the exact identity T0^r=det(F)^−1. Both are treated as the identified unrefereed author versions.

Buchweitz–Flenner, *The global decomposition theorem for Hochschild (co-)homology...*, Adv.Math.217(2008),243–281, author arXivmath/0606730v1, Proposition6.2.1, Corollary6.3.2 and Theorem6.4.2, pp29–31, were opened. Mukai, Nagoya Math.J.81(1981),153–175, Theorem2.2 p156, formulas(3.1),(3.4), pp158–159, and Proposition3.11 p162 were read from the published PDF, with the displayed formula pages visually inspected.

Exact source files and SHA-256, kept outside the deliverable:

- semiregularity.tex: `f931625fd98f3cae035b927e9ecdd7aad90236b39d0c1bb5cffccca18fd0a13e`; 125879 bytes.
- Dec6_version.tex: `9da3903df70453b07fdbf3c0105beb3974c5adfcc3a59abf67c6c951e054b54f`; 131465 bytes.
- Mukai1981.pdf: `062dd13ffac9249fd248f0cca061ff5e41918e8087f688ae30cb7a4f1c86be1c`; 1903728 bytes.

## 2026-11-23: finite-cover and Hochschild follow-up

- Opened Cohen1976 classification §§2,5 and corrected1978 normalizer statement; locally read pp.388–389 and431–435. Opened Malle1999 Tables8.1–8.2 and omissions explanation, pp.674–676; exact Gaussian reflection fields checked. PDFs remain outside deliverables.
- Opened the full published-text copy of Guralnick–Saxl2003 Theorem7.1 and remarks, pp.548–549, https://www.academia.edu/95917548/Generation_of_finite_almost_simple_groups_by_conjugates ; verified its tensor convention and absence of a generation-by-bireflections premise. No immutable local PDF hash is asserted for the HTML copy.
- Opened rStation75v2,30October2026, https://rstation.ai/problems/hodge_conjecture/papers/75 . Its primitive reflection-free rank23 obstruction concerns period dimension>=15. The article credits this context; our fully proved rank25 statement uses dominance16 and treats the original complex representation, including imprimitivity. No priority claim.
- Opened Guralnick–Tiep arXiv1009.2535 Corollary1.6 as the related source used by paper75. The root proof uses GS7.1 directly. Publisher PDF hash and exact locators are in GS_GT_PRIMARY_LOCATORS.md.
- Opened Golyshev–Lunts–Orlov2001 author PDF, https://homepage.mi-ras.ru/~orlov/papers/GLO.pdf ; downloaded473301bytes, SHA2565f470c51b31324a2c0d5e1f2c2caf8cdf0f642f2d5fe3924a6d6c45441107949. Read full Proposition4.3.7 and proof, author pp.17–19, including Clifford intertwining. The PDF is not copied into deliverables.
- Reopened Perry2022 Proposition5.4 publisher page while auditing weak/strong comparisons. The article states only the exact strong criterion and the direct implication strong=>weak; no general Hochschild isomorphism is inferred without geometric hypotheses.
- Reopened the current Severn Hexagon2610.00387v2 record. Its31-page served text and the linked17-pageZenodo draft differ; primary version status is kept explicit. Quantitative integration remains pending, not silently completed by this lookup.

## 2026-11-23: Eisenstein transfer, degree25 endpoint and Mumford sources

The main author read the whole quantitative Eisenstein proof and the original Schoen1988 cyclic-cover construction, printed pp11--19, including the exceptional paired-exponent step. Milne1999, Lemma3.5, Proposition3.6 and Remark3.7, were read in full for the exterior invariant decomposition. The current31-page Severn2610.00387v2 text was opened at Lemma4.4, Proposition4.6, Theorem5.1, Lemmas8.2--8.4, Proposition8.5, Section9 and AppendixA. The specified dominant G34 family remains an unrefereed geometric premise; the degree bound is separately proved in the paper.

The degree25 finite-group endpoint was checked directly against Hiss--Malle2001, Theorem1 and generic Table2 p31, and the corrected2002 Table2 p102. The PSp4(7) degree25 row is retained; the 3D4(2) degree25 row is characteristic3 only. Guralnick--Saxl2003 Lemma3.1 pp527--529, Theorem4.3 p533 and the primitive reduction pp549--550 were opened in full published text. An independent statement-only worker used the same primary list and found no counterexample.

For the surface criterion, the main author opened Nikulin1980 Theorem1.12.4 pp122--123 and visually read Morrison1984 Theorem1.7 p109 and the surrounding lattice discussion pp110--111. BHPS arXiv2510.00093v2, Theorem1.2 and Section5, was read for its explicit Mumford families and prior K3/RM/KS proposal. This context is credited; no priority claim is made.

The next positive attempt required a more precise KS source audit. Bolognesi--Laterveer arXiv2310.11981v2, Section4 Theorem4.1, Conjecture4.2, Theorem4.4 and its proof, and Section6 Propositions6.2 and6.4 were read. The cited van Geemen--Izadi Math.Z.242(2002),279--301, Sections5.5--5.6, explicitly constructs a half-twist block. The proposed rank12 Mumford transfer needs compatible Clifford operations on a different spin block; that conversion remains undecided. This is a limitation of the present deduction, not an assertion that their theorem is false. Buskin arXiv1510.02852v3 Theorem1.1 p2 and the CM-endomorphism corollary p3 were opened. Artebani--Sarti arXiv0801.3101 Table2, Propositions3.1--3.2 and the period description, and Gross, Incoherent definite spaces, Section3 Theorem3.1 pp6--7, were opened for the provisional lattice construction.

A fresh prior-art search also opened Bhattacharjee--Bhattacharya, Hodge Classes on K3 Powers and Sixfolds, preprints.org/manuscript/202602.0462, version7 posted17November2026. Its introduction distinguishes the unresolved Mumford linkage from algebraicity statements on the separate K3/sixfold factors. No theorem from that manuscript is used as a premise here. rStation60v1 was located as related discussion of KS-map precision; its claims are not substituted for reading the primary sources.

New primary file hashes (files remain outside the deliverable):

- BHPS2510_v2.pdf: SHA256 `ba69358dee54974010a2eaa174fc59382d3baf3f5ca2036dc8328e83a6da8fcb`; 1885638 bytes; Theorem1.2 and Section5.
- Milne1999aP.pdf: SHA256 `28ae245e58748438b7070680cac83f8b2f695c43f1643b59cde21eb94077fe53`; 352495 bytes; Lemma3.5, Proposition3.6 and Remark3.7.
- Severn2610_current.pdf: SHA256 `ee285c82b0a0b864bd63696dc6d701e1fab2c44272afb8747f0beef5d8fcccb4`; 492267 bytes; Sections4,5,8,9 and AppendixA.
- Morrison1984.pdf: SHA256 `62a6345fe40bc0699f3bcd5acacb4190294bb398e71e4d4ac9f9722bbd561d7c`; 789356 bytes; Theorem1.7 and pp109--111.
- BolognesiLaterveer2310_v2.pdf: SHA256 `6cd9e2353abe6811428909b2071103c893de221ac43dd5f937510975d4aeda70`; 262752 bytes; Theorem4.4 and Propositions6.2,6.4.
- HissMalle2001.pdf: SHA256 `83b68deb2a468db04e34da07bef713c203a3e0b6e3e4f46bfcdd5bc10249fda2`; 238318 bytes; degree25 tables and classification conventions.
- HissMalle2002_corrigenda.pdf: SHA256 `0c0e7bbb1ee9857a5339a14f017ebad8d69e7e91d98682697816f9e65920fd7d`; 141242 bytes; degree25 tables and classification conventions.

## 2026-11-23, 02:26UTC: exact finite-group follow-up

Opened CTblLib1.3.11's official description and the full Section1.2-9 construction for the elementary-abelian extension of M11. Read the constructor implementation to ensure that recomputing CharacterTable(group) does not reuse the stored table. The actual44-point permutation group, radical and full table were then recomputed successfully. The degree99 survivor is excluded by its11-by9 block system and the stronger branch-index inequality; the full scan remains a finite database computation with explicit coverage limits.

### 2026-11-23 02:48–02:55 UTC: balanced-sixfold support criterion

Opened Abdulali, arXiv:1203.4857, Theorem13 (author p10): every type-IV signature must satisfy |p−q|=1. Opened the author survey https://myweb.ecu.edu/abdulalis/Vancouver.pdf, Theorems6.5–6.6 p7, §8.2 p10, AppendixB.5 p12. The corrected signature hypotheses do not include(1,1),(2,0),(0,2); the recorded Schoen sixfold result concerns the rank-two degree-six CM determinant structure, not our rank16 degree-three structure. Opened Landherr's original four-page paper https://webhomes.maths.ed.ac.uk/~v1ranick/papers/landherr.pdf, especially pp246–247 for classification by determinant and signatures, and Gross's §3 exposition https://people.math.harvard.edu/~gross/preprints/incoherent.pdf. These readings support the exact scope comparison and the hyperbolic determinant calculation; no generalized-Hodge input was inferred from ordinary HC. Primary documents remain outside the workbench. Local hashes will be recorded if downloaded; no hash is asserted for a web-only opening.

Downloaded source hashes (documents remain outside all returned ZIPs):

- Landherr1935.pdf: SHA-256 `ccfaea6449b2d70fd3093551694bc7062548e88bc330ec8ef476612fdb34050f`; 137725 bytes; used pp246–247. Addresses are recorded immediately above.
- Abdulali2012_typeIV.pdf: SHA-256 `79ae3b9a5a22aaed065c0d273f085f1d2822c317572bd46674a4aa9691d0f31f`; 187872 bytes; used author p10, Theorem13. Addresses are recorded immediately above.
- Abdulali_Vancouver.pdf: SHA-256 `1d0b54bbd2c955a43d9eeda438d8a2373adbce8cafe29ae839ee24523568df62`; 312183 bytes; used pp7,10,12. Addresses are recorded immediately above.

### 2026-11-23 03:02–03:04 UTC: elliptic surface and sixfold-link context

Opened Schütt–Shioda, Elliptic surfaces, arXiv:0907.0298v3, §4.5 Table1 p14; Theorems6.8 and6.12, pp26 and29; Corollary6.11 p27. These verify the fiber-type, canonical-bundle and irregularity assertions needed by the explicit quadratic-twist example. Download:919673bytes, SHA-256 `eeac47d53b52e96a1d2457a131dcce474332dd6b226e4dcd944575e995aa44b1`, https://arxiv.org/pdf/0907.0298 .

Reopened Bhattacharjee–Bhattacharya, Hodge Classes on K3 Powers and Sixfolds, served v7, https://www.preprints.org/manuscript/202602.0462 ; Theorem37 is a prior sixfold-link sufficient criterion involving the rank9 adjoint tensors in H1(X)⊗H1(X)⊗H2(Z_K). AppendixA23 gives the rank9 K3 realization. Exact overlap comparison and full relevant proof review continue; no priority claim is made for our Mumford routes. HTML downloaded12385507bytes outside the workbench, SHA-256 `cf05289e9380b6ac986455b3582af2c81a13a247ba43fa50dfb0bed76c8fee1f`. Its unrefereed theorems are context, not hidden premises.

## 2026-11-23 03:30 UTC — additional primary checks and precise antecedents

- Achter–Casalaina-Martin–Vial, On descending cohomology geometrically, author version 28 September 2015, Proposition1.3 and entire proof p8: opened directly. URL https://www.math.colostate.edu/~achter/math/dcg0915.pdf ; SHA256 9bf22c61910f7fbc6abe69385976ab1953577db5802aee7b3167931a442ac3c8. Used only for the curve description of geometric coniveau.
- Voight, Quaternion Algebras, current author PDF, Main Theorem5.4.4 and Lemma5.4.7, pp72-74, full statements and proofs read. URL https://jvoight.github.io/quat-book.pdf ; SHA256 a9316b834dbd500c52cd3a981c3205c9f4145b217042b213d23f696aee84b0f0.
- Milne, Class Field Theory4.03, II Proposition1.39(d), pp73-74, full statement and proof paragraph read. URL https://www.jmilne.org/math/CourseNotes/CFT.pdf ; SHA256 50d79af78250a9f1117ad9d337e0b231704a533fc707966ed1bfa52e13d498f5. Used for restriction/corestriction cup projection.
- Mumford, Abelian Varieties, primary scanned spreads visually read: Appell–Humbert cocycle and additivity pp20-21; RR/vanishing p150; index p155 and Hermitian signature corollary p162. Primary scan https://djvu.online/file/2tC7xp3dbqGCh and university scan https://wstein.org/edu/Fall2003/252/references/mumford-abvar/Mumford-Abelian_Varieties.pdf . Individual scan hashes are recorded in the source table when assembled; no scan is returned.
- Bhattacharjee–Bhattacharya, Hodge Classes on K3 Powers and Sixfolds v7, 17 November2026, unrefereed. Root opened Theorems37-38, Proposition41 and TheoremA23; the balanced-sixfold criterion differs in its compact central signatures. Root then opened TheoremA6 and its complete rank proof, the exact prior general formula underlying rank104. TheoremA7 asserts a universal pure-character obstruction via unpolarized tori; its analytic deformation premise LemmaA2 is under separate primary-source audit and is not yet admitted as an unconditional result. URL https://www.preprints.org/manuscript/202602.0462/v7 ; fetched HTML SHA256 cf05289e9380b6ac986455b3582af2c81a13a247ba43fa50dfb0bed76c8fee1f. No priority claim is made.

## Analytic source audit, 23 November 2026

Voisin, A Counterexample to the Hodge Conjecture Extended to Kähler Varieties, IMRN2002: https://webusers.imj-prg.fr/~claire.voisin/Articlesweb/hodgeimrn.pdf . Main author opened the full Appendix Proposition A.3 and Corollaries A.4–A.5, printed pp1072–1074, including the induction and Ext vanishing argument. SHA256 bea2795aa609b2a6c396c88c93a6903ee9965b92d1ecad91f36812adec562115.

Bando–Siu, Stable sheaves and Einstein–Hermitian metrics, printed p40, Theorem3 and Corollary3: https://people.math.harvard.edu/~siu/bando_joint_paper/bando2.jpg . Main author visually opened this primary page. Image SHA256 029d19c14dc375ba0b1a82b846495fc1b43323952bb7a7ed2c62c510374aaded. No source scan is redistributed.

Bhattacharjee–Bhattacharya v7, Lemma A2 and Theorem A7, were read with their complete displayed proofs. Lemma A2 asserts a global bounded holomorphic-vector-bundle resolution on every nearby torus; this stronger assertion has a point-sheaf counterexample. Whether A7 can instead be established through deformation of analytic perfect objects is being audited; A7 is not used as an established input.

GAP4.14.0 primary implementation lib/ctblsymm.gi, CharValueSymmetric lines305–378, read in full. Its rim-hook recursion and integer hook degree case are the character routine used in the symmetric scalar calculation. SHA256 42f81b7166af971a2e291fb9951949aa5093f9a5cb4b4ab67e24a4199f020210. No third-party source code is redistributed.

## Foundational source reopening, 23 November 2026

Main author read EGA IV2.4.6 (full statement and short proof), IV11.1.1 (full statement), and SGA6 XIII6.9–6.11 (full statements and displayed proofs) from the attached LaTeX editions. File hashes: 
- ega4-2.source_aligned_r1.tex: c4ce68a7af02029a8f969a25e7b58cb1b0c9055c98bfefeb9c0c0dfb6570f06d
- ega4-11.tex: f568653ec94fd22e9dac716b55de20389ac2b4166219d627cf541ac8f64d12f2
- main.tex: 4bbfb49c6bbb2c1d7c69fc4883a8031fe79b888cbb6523a50016512136917adc

Scanlon, Automatic uniformity: https://math.berkeley.edu/~scanlon/papers/autouni.pdf . Definition2.2 and Theorem4.2 with its proof read, author pp2,7. SHA256 73b9edc8d15bb7f87dd3e9304381999adf09917427afbe65ee3b327c80e35a38. Chai–Oort, Annals176(2012),589–635: https://annals.math.princeton.edu/wp-content/uploads/annals-v176-n1-p11-p.pdf . Definitions5.3–5.4 p607, Remark5.8 and proof p610, Lemma6.3 and full proof pp621–622 read. SHA256 6b30ee956259f924fe74c4811dfe15682040d16a4d3b467a5cf2420c8536b4fe.

Schoen2007 full-text retrieval repeated with title, title plus pdf, DOI, author home page, publisher PDF and epdf. Publisher PDF returned403; epdf unavailable. The Duke publication record and author home page were opened, but the complete original Lemma10.4 remains unavailable. The published form explicitly stated by vanGeemen2022§6.2 is the inspected geometry input; citation wording will distinguish this from direct inspection of Schoen2007.

## 2026-11-23 UTC — final foundational-source audit

Reopened the attached SGA4½ Cycle2.3.1–2.3.8, including the trace construction, Definition2.3.2, Lemma2.3.7, Theorem2.3.8 and its proof. Reopened the erratum to SGA4XVI Corollary2.2: coefficients must be locally constant. The paper uses constant coefficients and now says so. Reopened SGA4XI Theorem4.4, XVI Corollary2.2, XVIII Theorems2.9 and3.2.5. Exact numbered locators are authoritative; the Cycle transcription has no printed-page markers. No scans were fetched. Source hashes are in SOURCES.tsv.

## 2026-11-23 UTC — Gaussian diagonal-trace construction search

Queries: `"Weil" "semiregularity" "G(4,4,4)"`; `"Weil" "trace" "line bundles" semiregular eightfold`; `site:hexagonmath.org "Weil" "trace" semiregularity`; `site:eccc.weizmann.ac.il Hodge Weil algebraic cycles`. The second search engine returned Markman-related discussions, the previously inspected secant-object preprints and unrelated trace results; no identified source for the exact block-reflection incidence construction. This is not a priority claim. A first-engine cross-check used `"Weil" "semiregularity" "reflection" "trace"`, `site:arxiv.org "Weil" "line bundles" "extensions" semiregularity`, and `site:hexagonmath.org "Weil" "incidence"`. No search result is used as a theorem without opening its primary text. The construction is reported only at its verified diagonal-trace scope.

The cross-check identified Bhattacharjee–Bhattacharya, Secant Objects for Weil Classes on Abelian Varieties, Preprints.org202611.0672v1(6November2026). Root opened and read complete §3.1 Lemmas2–3, Proposition2 and Theorem10/proof. The generic-torus/coherent vanishing is now credited explicitly in the paper. Theorem10 repeats the global bounded-vector-bundle passage already under audit; it does not repair the relative analytic perfect-object gap. Downloaded HTML SHA256c3ca70a1618ea67c7f372b6f545187905093355412440b083fe6660eb2f3c3ec. No priority claim; no source copy in deliverable.


## Finishing continuation, 23 November 2026

This checkpoint retains the inherited mathematical record, with the current changes below. Historical descriptions of checks in the preceding entries refer to their original sessions, not to fresh checks in this continuation.

Fresh primary sources and exact source hashes are being accumulated in the Q23, Q24 and Q32 review records. Voisin, Markman, Cohen, Malle, the public Severn certificate deposit, and the original statements surrounding Schoen surfaces have been opened. Full original Schoen 2007 proof text is not yet available; its Theorem 1.1 on page585 has been checked from the publisher preview. No unread proof is represented as read.


## Finishing source audit completed before checkpoint 02

Date:23November2026. The new source records are under workbench/checks, with inspected versions, locators and hashes. The following are new searches/inspections of this continuation, distinct from the inherited log above.

- The Voisin exposé, Markman ICM account and detailed secant preprint, published Cohen classification/correction and Malle field tables were opened. The OpenAI eightfold withdrawal notice was opened and its6October2026sign-error status is stated. The uniformity theorem does not use recent unrefereed CM algebraicity theorems.
- The Schoen2007full-PDF search tried publisher PDF/epdf, DOI/title searches, author pages and alternate indexed copies. The original Theorem1.1(i)–(iii), printedp585, was visible in the publisher preview. The complete proof and Lemma10.4 were not obtained. The degree36 argument instead has a complete independent exterior-algebra/principal-quotient calculation and uses the exact published ambient statement of vanGeemen2022§6.2; no unread Schoen proof is claimed to have been read.
- Q12searches and primary checks covered Buchweitz–Flenner, Căldăraru–Willerton, Pridham, Wei, Chan–Suen, Goldman–Millson and the two Bhattacharjee–Bhattacharya preprints. The exact strong dimension criterion agrees with the known evaluation/trace framework. The remaining distinction is a relative convergent analytic deformation theorem for arbitrary perfect objects; fixed-manifold cohesive Kuranishi theory and algebraic derived obstruction statements do not alone state that relative analytic theorem. The detailed comparison and precise scopes are in the Q12report.
- Q23primary and forward-citation checks covered vanGeemen–Izadi, Laterveer, Bolognesi–Laterveer, Floccari, Buskin, Varesco, Artebani–Sarti, Gross and Voight. The strong published canonical statement is acknowledged; the formal-support obstruction is not represented as its refutation. The existence lemma uses the order-three component's actual coinvariant lattice and exact model-period locus.
- The finite-cover independent proof reopened Cohen and Malle, Guralnick–Saxl's published article, Hiss–Malle and its correction. The strengthened scalar-standard argument uses elementary branching and compact Shapiro; the rank25primitive step retains the exact published classification dependencies. The complete independent and targeted reports are separate.
- The public Gaussian certificate deposit was recovered by DOI/hash. All112irreducible characters and subgroup maps were rebuilt from the actual matrix group, then combined with a rigorous interval period replay and a checked geometric dictionary. No third-party source body or certificate archive is returned.

The continuing comparison makes no priority claim. Searches of arXiv, journals, author pages, ECCC and Hexagon are recorded by the individual reports and earlier dated query log; no claim of exhaustive coverage is made.
