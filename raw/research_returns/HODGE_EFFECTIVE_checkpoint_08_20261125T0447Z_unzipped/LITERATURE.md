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

## Finishing source and construction checks, 23 November 2026, 14:00–15:00 UTC

### Parabolic duality: corrected source, not only a changed page number

The actual cup-product theorem is Dettweiler–Wewers, *Variation of parabolic cohomology and Poincaré duality*, Séminaires et Congrès13(2006),145–164, Theorem2.6 on p.158. The published article at https://www.emis.de/ft/47210 was opened and the theorem/proof checked; SHA-256 `68a9f46fd16753245511f3a67612eaeaf8ff5c135c8086029b7db9d702d4231a`. Its author version https://arxiv.org/pdf/math/0411119 has the corresponding Theorem2.5 on author p.12, SHA-256 `606d31016f927739e83e50eefb707c0f96b1d351acd845e3bbd21b15002e2ccf`. The distinct *Variation of local systems and parabolic cohomology*, math/0310139v2, Theorem2.5 is a braid-action statement; it remains appropriately cited for that different use in Paper B. The source repair and finite/analytic proof scopes are documented in `workbench/checks/q24/`.

### All-field sixfold regularity and B-field normalization

The fresh statement-only supplier attempt reconstructed the arithmetic and cyclic geometry but explicitly left the all-field regularity constant as a gate. The subsequent full proof-aware comparison checks the Fourier sheaf, Buchsbaum–Rim constant560, multiplication-isogeny vanishings, normalized rank64D seed, finite-band untwisting and effective third Chern cycle. Perry arXiv:2604.00511v2 Theorem1.2 and §6.2, author pp.26–28, remain the explicit unrefereed input. Hotchkiss arXiv:2212.10638v1, Definitions4.5/4.16, Lemma4.6, Remark4.13 and Theorem4.17, author pp.15–18, were opened for conventions: https://arxiv.org/pdf/2212.10638v1 ; SHA-256 `72f6f61c828d81e49894a93f377ff912e3587b6a97bfddaa62a413df1c009d75`. No source body is returned. The initial partial proof record is preserved; it is not retrospectively relabeled as a complete independent proof.

### Strengthened coordinate-sign obstruction: searches before reporting the extension

Second-engine queries were `"abelian varieties" "sign" "trace" "semiregularity"`, `"Weil classes" "permutation" "Specht"`, `site:hexagonmath.org "Weil" "trace"`, and `site:eccc.weizmann.ac.il "semiregularity"`. Results included the already inspected Bhattacharjee–Bhattacharya secant papers, related rStation finite/spin discussions, and ECCC08/099 on a different semiregularity topic. No result was identified with the exact coordinate-sign network theorem.

The stronger first-engine cross-check used `"Weil classes" "coordinate" "sign" "extension"`, `site:arxiv.org "semiregularity" "Weil" "bundles"`, and `site:hexagonmath.org "semiregularity" "sign"`, with a one-year recency filter. Primary results included Markman's ICM article/detailed preprint and the previously inspected secant/K3 preprints; van Geemen's spinor-map paper was related context. No priority or exhaustive-search claim is made. The mathematical extension is the explicit n>=2 four-label determinant and Specht propagation argument now proved in Paper B. An additional fresh statement-only worker independently found and proved the same four-coordinate mechanism.

### Additional fresh theorem comparisons

The Gaussian network was independently reconstructed, including a newly selected exact rational witness and a standard-library verifier of every one of the6272 equations. The cyclic and all-determinant bounds, conditional Eisenstein eightfold bound, sharp theta rank/full ideal, Mumford cubic bound, nonsquare surface criterion and genuine coniveau criterion received distinct initial and subsequent targeted reports. The reports identify prior theorems and their source versions; none makes a priority claim. The positive networks remain statements about diagonal trace equations, not completed eightfold deformations.

Artebani–Sarti's notation M_{n,k} was checked at the opening of §5, author p.14, with Theorem2.2 p.5, Table1 p.8 and Proposition4.7 p.12. M_{0,1} has one smooth genus-four fixed curve and no isolated fixed point. This definition is now stated at first use. Publisher-deposited metadata confirms *Mathematische Annalen*342(2008),903–921; the paper's existing page range was already correct. The metadata SHA-256 and source version are in the review record; the external metadata body is not needed in the deliverable.

### Current format1 source

The live format document, dated22November2026, was read at https://github.com/KokunoYumeto/mathematics-workbenches/blob/main/FORMAT.md . A direct HTTPS retrieval succeeded after the web reader's blob/raw openings failed. SHA-256 `b6cff6c746787fc706e3db621a372b83ab49b84e76b218776807154a7cd92832`. The official read-only checker at `tools/check_workbench.py` has SHA-256 `13042772b472b1a65f35fd8d8c349dc55a5e9cdabb5e6e5e4434aa1d4b6f0291`. Its exact formatting issues are being repaired; provisional WB numbers and the public commit/version seal remain explicitly for the depositor. Neither source file is copied into the workbench.

## Final stronger-criterion and maximal-lattice searches, 23 November 2026, 15:51–15:58 UTC

Searched general mathematical terms: “Gaussian hermitian lattices indefinite determinant3 maximal lattice class number one”; “Mumford fourfold quadratic Lie algebra K3 Hodge conjecture all powers”; Hexagon for Mumford/Clifford/quadratic/Hodge; ECCC for hermitian lattices and Mumford/Hodge. The searches found the existing Bhattacharjee–Bhattacharya and Floccari neighbouring literature and no ECCC result supporting these geometric claims. Search absence is not a priority claim. The new reduction is stated with its full proof and explicit input, without priority language.

Opened Kirschmer, Determinant groups of hermitian lattices over local fields, https://www.math.rwth-aachen.de/~Markus.Kirschmer/papers/det.pdf (SHA256965f1dc05710d44ee506a242842a9210c116a21dbff5ca7c30a3e76133da5226), Theorem4.3, Lemma4.6 and Remark4.8(2), for the separate proposed maximal Gaussian-lattice sharpening. Also inspected his Hermitian lattices manuscript, https://www.math.rwth-aachen.de/~Markus.Kirschmer/papers/herm.pdf (SHA256aef562cc9ea0cfcd7d82a6e325a3885c3527d367811eb39a8e8e7d544596e183), Corollaries3.3.19–3.3.20 and5.1.4. The local/global sharpening remains under a separate fresh statement-only attack at this dated entry. External source bodies are not included.

For the stronger Mumford result, the primary Varesco author version arXiv:2203.09778v3, Corollary2.3 pp6–7, was directly checked. It applies to any projective K3 with CM endomorphism field and has no Picard-number-sixteen restriction. The fresh proof records its exact source SHA and distinguishes it from the paper’s separate Picard16 main theorem.

A bibliographic warning in the fresh Q23 preprint-only phase was resolved by directly reading the publisher-formatted van Geemen–Izadi PDF, https://mathweb.ucsd.edu/~eizadi/papers/MathZ2002.pdf, SHA2566da8e0acaaf900ed80c895a4b8c229c70320adf845d7a6178b9334b3d2c8a732. The published locators are Theorem5.2 p294, Theorem5.4 p295, and §§5.5–5.6 pp296–298. These differ from the author preprint numbering. PaperB now supplies the published pages and the inspected URL. The frozen earlier caution is preserved as a historically accurate statement about the copies then read.

## 23 November 2026, final Gaussian lattice-source identity check

The independent local/global proof uses Landherr, *Äquivalenz Hermitescher Formen über einem beliebigen algebraischen Zahlkörper*, Abh. Math. Sem. Univ. Hamburg 11 (1935), pp.245–248, specifically pp.246–247; source URL `https://webhomes.maths.ed.ac.uk/~v1ranick/papers/landherr.pdf`, SHA-256 `ccfaea6449b2d70fd3093551694bc7062548e88bc330ec8ef476612fdb34050f`. It also uses the indefinite special-genus consequence in Kirschmer, *Determinant groups of hermitian lattices over local fields*, Arch. Math.113 (2019),337–347, Theorem4.3 and Remark4.8(2), author-version pp.7–9; URL `https://www.math.rwth-aachen.de/~Markus.Kirschmer/papers/det.pdf`, SHA-256 `965f1dc05710d44ee506a242842a9210c116a21dbff5ca7c30a3e76133da5226`. The finite determinant and Gaussian ideal-class corrections are proved in the paper. The earlier general-topic search entries remain the literature search record; no priority claim is made for the resulting volume factor.

The source-cap propagation uses proper bounded Chow spaces and the flat Weil projector; its statement-only proof and post-freeze source receipts identify the precise passages. `checks/gaussian_maximal_blind/POST_FREEZE_SOURCE_IDENTITIES.json` records separately downloaded source identities for Landherr, Kirschmer, Milne, Kollár and Voisin. An identity download is not recorded as a fresh full reading. External source bodies are excluded from the returned work.


# HODGE_EFFECTIVE searches and source checks

Date: 2026-11-25. No priority claim is made.


## cycle_degrees

# Literature and check provenance

Date: 25 November 2026 UTC. Worker: GPT-6 Astra Pro; inherited effort setting not exposed. The notes distinguish exact statement checks, proof checks, original deductions and unavailable sources. Read copies of other authors' PDFs and screenshots are not intended for the returned deliverable archive.

## Cycle degrees and geometry

* C. Schoen, *Hodge classes on self-products of a variety with an automorphism*, Compositio Math.65(1988),3--32. Full primary PDF obtained from https://www.numdam.org/item/CM_1988__65_1_3_0.pdf. The faithful-character construction was checked against the supplied corrected proof. The exponent m/2 repair and cyclic-supplier application are proved in the new material, not attributed unqualifiedly to the original argument.
* B. van Geemen, *Theta functions and cycles on some abelian fourfolds*, Math.Z.221(1996). Author PDF https://sites.unimi.it/vangeemen/ThetafctsCycles4folds_MathZ1996.pdf. Visually read the finite-base-locus argument p622, Proposition3.6 p623, Theorem3.7 pp624--625. The numerical degree48 residual-intersection deduction is the paper's calculation, not an explicit quoted theorem in this source.
* C. Schoen, *A family of surfaces constructed from genus2 curves*, Int.J.Math.18(2007),585--612. Theorem1.1(i)--(iii), p585, was read in the publisher preview. The full publisher PDF returned403 and the full original proof was not checked. Do not promote this to a whole-proof audit.
* B. van Geemen, *Weil classes and decomposable abelian fourfolds*, SIGMA18(2022),097. Journal PDF https://sigma-journal.com/2022/097/sigma22-097.pdf opened through web retrieval; local byte-fetch endpoint returned406. The actual deformation into a four-dimensional Weil family is described in the introduction; Section6.2 p14 gives the Eisenstein field and polarization type(1,1,3,3). The author version https://arxiv.org/pdf/2108.02087 was also obtained.
* C. Rito, X. Roulleau, A. Sarti, *Explicit Schoen surfaces*, author version https://arxiv.org/pdf/1609.02235. Introduction p1 and Theorem1 p3, including the Albanese embedding, Lagrangian form and four-dimensional deformation family, read in full. No claim to have re-proved Schoen's original deformation theory.
* M. Dettweiler, S. Wewers, *Variation of local systems and parabolic cohomology*, author version https://arxiv.org/pdf/math/0310139, Lemma2.2 p7 and Theorem2.5 p12. Checked the explicit cocycle and monodromy formulas used to identify the exact G34 calculation with geometric monodromy.
* M. Dettweiler, S. Wewers, *Variation of parabolic cohomology and Poincare duality*, Semin.Congr.13(2006),145--164, https://www.emis.de/ft/47210. Correct pairing locator is **Theorem2.6, pp158--160**, not Theorem2.5. The G34 dominance proof avoids needing an auxiliary-form/geometric-polarization identification.
* W. Schmid, *Variation of Hodge structure: the singularities of the period mapping*, Invent.Math.22(1973),211--319. Full PDF https://webhomes.maths.ed.ac.uk/~v1ranick/papers/schmid.pdf. Theorem(4.12) p233 and Theorem(6.16) p255 plus their setup read. These are external published inputs; their entire long proofs were not independently re-proved.
* J. S. Milne, *Lefschetz classes on abelian varieties*, Duke Math.J.96(1999),639--675. Author PDF https://www.jmilne.org/math/articles/1999aP.pdf, Lemma3.1 p14 and Theorem3.2 p15 read. Used for full Lefschetz-group invariants after Brauer contraction, with disconnected orthogonal factors retained.
* D. M. Davis, *Homotopy type and v1-periodic homotopy groups of p-compact groups*, Topology Appl.156(2008),300--321. Author PDF https://www.lehigh.edu/~dmd1/TOPOL3486.pdf, Theorem5.1 and proof pp312--313. Used for the six-dimensional Eisenstein G34 root realization. The ten reflections, group order, central scalar and geometric witness were reconstructed exactly in this work; the scalar identity (s1 s2 s3 s4 s7 s5)^14=omega I6 is separately verified.

## Effective Shimura constants

* S. Jaswal, supplied arXiv2611.00339v3 TeX, `source/outside/jaswal_2611.00339v3/main.tex`. Exact hypotheses and proof steps are logged in `research/discriminant_targeted.md`; Table1, Proposition3.3 and Corollary9.10 were checked for the later fixed-datum constants. These tasks had separate statement-only freezes before targeted comparison. Prior exposure to the earlier Jaswal source is explicitly disclosed in the later receipts.
* E. Ullmo, A. Yafaev, *Galois orbits and equidistribution of special subvarieties: towards the Andre--Oort conjecture*, author version https://www.ihes.fr/~/ullmo/publications/UllmoYafaevSept2013.pdf. Lemma2.4 p11, Lemma2.6 pp12--14, Lemma2.7 pp15--17, Lemma2.8 pp17--19, Proposition2.9 pp19--20 read and matched term by term. The common exponent is cleared by factorials; a mere numerical upper bound is not used as if it were divisible by every exponent.
* B. Edixhoven, A. Yafaev, *Subvarieties of Shimura varieties*, author PDF https://websites.math.leidenuniv.nl/edixhoven/public_html_rennes/publications/anoort.pdf. Proposition7.4.3 p23 was visually inspected because extracted text was defective. It asks for differences of weights in an integral character-lattice basis. The new HNF/Cramer bound meets this exact requirement, including the strict convention in the proof.

## Finite coefficient groups

* R. M. Guralnick, P. H. Tiep, *Decompositions of small tensor powers and Larsen's conjecture*, Represent.Theory9(2005),138--208, DOI10.1090/S1088-4165-05-00192-5. Theorem1.7 p142; proof pp194--195. Author PDF https://arxiv.org/pdf/math/0502080: Theorem1.7 p6; proof pp66--67. Full relevant theorem/proof read; publication text checked through an author upload at https://www.academia.edu/100276315/Decompositions_of_small_tensor_powers_and_Larsen_s_conjecture. The direct AMS PDF endpoint was unavailable. The d/8 bound requires M4=2.
* R. M. Guralnick, J. Saxl, *Generation of finite almost simple groups by conjugates*, J.Algebra268(2003),519--571, DOI10.1016/S0021-8693(03)00182-0. Exact original text read via https://www.academia.edu/164985288/Generation_of_finite_almost_simple_groups_by_conjugates. Theorem7.1 and Remark(3), pp548--549, have the threshold max(2,sqrt(d)/2). Lemma7.6 and Table1, pp553--554, supply alpha<=8 for every sporadic socle, including outer automorphisms. Relevant sections were read; the entire 53-page paper was not audited.
* R. M. Guralnick, P. H. Tiep, *A problem of Kollar and Larsen on finite linear groups and crepant resolutions*, JEMS14(2012),605--657, DOI10.4171/JEMS/313. Primary PDF https://arxiv.org/pdf/1009.2535. Theorems1.4,3.8 and its table,5.9 read with hypotheses. They do not apply merely because the average branch moving rank is small; the age<=1/generation hypotheses remain missing.
* H. Duyan, Z. Halasi, K. Podoski, *Random bases for coprime linear groups*, J.GroupTheory23(2020),133--157, DOI10.1515/jgth-2019-0043. Author PDF https://zhalasi.web.elte.hu/papers/16_CoprimeRandomBase.pdf. Definition2.3 p4, Lemma3.1 pp5--6 and Theorem4.1 p7 read. The latter is a complex-character theorem and gives sporadic ratio<0.54 and Lie-type ratio<=max(1/(sqrt(q)-1),9/q) for q>9. Its sporadic proof reports a character-table computation using floating evaluation; this work uses its published theorem without claiming to have recomputed those tables.
* D. Gluck, *Sharper character value estimates for groups of Lie type*, J.Algebra174(1995),229--266, DOI10.1006/jabr.1995.1127. Cited inside Duyan--Halasi--Podoski Theorem4.1. The DOI/publisher and several DeepBlue PDF endpoints returned403. **Original proof not read.** The new insertion directly cites the available primary Duyan--Halasi--Podoski theorem.
* D. O. Revin, A. V. Zavarnitsine, *Generation by conjugate elements of finite almost simple groups with a sporadic socle*, arXiv2402.03673v1, https://arxiv.org/pdf/2402.03673. Theorem3 p3 and surrounding reduction to prime order read; gives maximum alpha6. Published successor: *Conjugate generation of sporadic almost simple groups*, Siberian Electronic Math.Reports22(2025),552--562, DOI10.33048/semi.2025.22.037, https://math-semr.ru/en/content/22-1/0552. Publisher PDF opened; full revised proof not audited. Neither version is necessary for the insertion, which uses the sufficient GS maximum8.
* lelong_ridge, *Exact linear-programming obstructions to reflection-free cover sources of Weil classes*, rStation paper129 v2, 15November2026, https://rstation.ai/problems/hodge_conjecture/papers/129. Statements/method of Theorem5.1 and Proposition8.1 read; no independent full certificate audit. Specified scalar Specht/Weil blocks only, with conditional outer-unitary extensions; no universal classification claim.

## Withdrawn positive route

The repository notice at https://github.com/openai/math/blob/main/preprints/Algebraicity-of-Weil-classes-on-split-abelian-eightfolds-September-18-2026/README.md was read. It reports withdrawal on6October2026 after the reversed stabilization sign was found to be negative, leaving the required intersection cancellation nonzero. This is not a usable proof of the Gaussian eightfold case. The notice concerns that particular preprint; no unrelated CM-Hodge manuscript is described as withdrawn on this basis.

## Exact independence receipts

* Main discriminant statement-only proof: `research/discriminant_blind.md`, frozen2026-11-24 23:11:19.432294UTC, SHA256 `5d51d994213dfda60fded44b9d20f0bd86c188f1016f0bae2fc7c40cdcda20b7`.
* Coarse fixed-datum constants: `constant_bounds_blind.md`, frozen2026-11-25 00:00:02.854214UTC, SHA256 `811c3b0e5e79afe1c9cc32401cc0922ce0b4cace454ce540f16bda0bedbe646b`.
* Component field/fine level: `fine_level_blind.md`, frozen2026-11-25 00:04:03.495391UTC, SHA256 `274a212673ee17cc304193d6dc4e5195c50d33a50a31459d057cf1390db02522`.

These are same-model independent checks with explicit exposure boundaries. They must not be relabeled as an independent human review or as a check by a different model.


## effective_audit

# Literature and source checks for the effective criterion

Date: 2026-11-24 UTC (2026-11-25 Europe/Berlin after midnight).

These searches support attribution and comparison. They do not establish priority and no priority claim is made.

| Search or opened source | Result and use |
|---|---|
| Web search: `site.hexagonmath.org "2611.00339" Jaswal` | Located indexed metadata for Jaswal; the unversioned Hexagon landing failed in this tool, while the versioned page subsequently opened. |
| Opened https://hexagonmath.org/2611.00339v3 | Version 3 is dated 18 November 2026 in its version history. Declares predominantly AI-generated text and no parts with human understanding; provenance names Claude Fable 5.2 and GPT-6 Astra, separate AI checking, author reading and rerunning computations. |
| Search: `"Hodge generic" "F-irreducible" "Hecke" Jaswal` | Located the full statement of Theorem 6.7 and Lemma 6.8 at https://hexagonmath.org/pdf/2611.00339v3. Confirms the F-irreducible hypothesis, which permits the fixed-field application. |
| Search: `"Weyl" "special points" "effective" "André"` | Located Chai--Oort and Jaswal, and older Hecke-criterion literature. No separate paper with the precise detector specialization was identified. |
| Search: `site:eccc.weizmann.ac.il "André" "Oort"` | No relevant primary result identified in the returned search. |
| Search: `site:manvirjaswal.github.io "André"` | Located the author's index and effective André--Oort entry. Also located the author's Dirichlet-RH exposition after Alpöge; not used as a proof of the effective criterion. |
| Search/open: Chai--Oort, https://annals.math.princeton.edu/2012/176-1/p11 | Journal publication: Annals of Mathematics 176 (2012), 589--635, DOI 10.4007/annals.2012.176.1.11. |
| Opened and fetched author proof: https://webspace.science.uu.nl/~oort0109/IsogJac-AnnMath.pdf | Read Remark 5.8 and Lemma 6.3 with proof; author proof pp. 22--23 and 33--34. Exact hash in fetched_sources.json. The author proof is not a deliverable. |
| Opened https://arxiv.org/abs/2109.08788 | Pila--Shankar--Tsimerman with Esnault--Groechenig, v4 dated 17 December 2024; abstract explicitly states André--Oort in full generality. The attached source is used for precise theorem attribution. |
| Attempted primary PDFs https://arxiv.org/pdf/1209.0936v2, https://arxiv.org/pdf/1209.0934v2, https://arxiv.org/pdf/1209.0942v2 | Web tool returned DisabledError. These references were not thereby checked in full; their use in Jaswal is recorded as an external dependency. |
| Attempted direct fetch https://hexagonmath.org/pdf/2611.00339v3 | HTTP 403. The attached TeX source was read instead. The PDF search text independently confirms Theorem 6.7 and Lemma 6.8 numbering. |

## Precise external statements used

- Chai--Oort, Remark 5.8: a Weyl special point has full adjoint Weyl Mumford--Tate torus.
- Chai--Oort, Lemma 6.3: in Q-simple type A (also D and E in their stated range), a connected subgroup containing a Weyl torus is that torus or the entire group.
- Jaswal v3, Corollary 3.4 and Lemma 6.4: the Galois lower bound, in the latter case at every auxiliary level.
- Jaswal v3, Theorem 6.1: the uniform Hecke forcing step.
- Jaswal v3, Proposition 6.6: a splitting prime outside the exceptional torus-level primes.
- Jaswal v3, Theorem 6.7: the Hecke bound for Hodge-generic F-irreducible loci.
- Jaswal v3, Lemma 6.8: solution of the logarithmic inequality with the explicit function B.
- Jaswal v3, Theorem 8.1 and Remark 8.2: polynomial behavior at fixed field in the adjoint case, and the source of the exponential growth in the general recursion.
- Jaswal v3, Proposition 9.4(c): finite adjoint map and equality of Baily--Borel line bundles under pullback.
- Jaswal v3, Theorem 9.12 and proof of Theorem 1.1: general dimension recursion; not needed in the relative-Weyl application once the adjoint model is fixed.

The proof in effective_section.tex is an application of these inputs. It does not assert that this run has certified all of the external theorems or every one of their dependencies.

## Follow-up primary-source checks, 25 November 2026

- Ullmo–Yafaev, author PDF dated September 2013, https://www.ihes.fr/~/ullmo/publications/UllmoYafaevSept2013.pdf. Downloaded and hashed in `fetched_sources.json`. Read Lemmas 2.4–2.8 and Proposition 2.9, printed pp.11–20, for the uniform reciprocal exponents; independently checked by the cycle worker. In the point-chain second pass, read all of §2.2, Lemmas 2.11–2.18, Proposition 2.14, Theorem 2.19 and Remark 2.20, printed pp.21–32. This followed a successful author-PDF fetch and supersedes the earlier unsuccessful arXiv fetch for these portions; it does not amount to checking the whole UY paper.
- Edixhoven–Yafaev, author PDF, https://websites.math.leidenuniv.nl/edixhoven/public_html_rennes/publications/anoort.pdf. Downloaded and hashed. Proposition 7.4.3, PDF p.23, visually read after rendering because the text extraction was defective. The relevant coordinates bound **differences of weights**, with a strict inequality; the explicit coarse constant includes the necessary factor 2 and final +1. The rest of the local-torus/lattice theorem remains a named external input.
- Milne, *Introduction to Shimura Varieties*, revision 16 September 2017, https://www.jmilne.org/math/xnotes/svi.pdf. Opened through the web tool, not locally fetched. Theorem 5.17, printed p.59: components through the abelian quotient with simply connected derived group. §13, formula (64), printed p.119: canonical reciprocity on components. Siegel example, printed p.125: cyclotomic action on multiplier-level components. These statements support the concrete degree-two component field; the double-coset calculation itself is reproduced in the insertion.
- Milne, *Abelian Varieties*, updated 2 January 2022, https://www.jmilne.org/math/xnotes/AVs.pdf. Opened, not locally fetched. Remark 7.3, printed p.12, records the very ampleness of the cube of an ample line bundle (Mumford, §17, p.163). Used for the cube of the universal Poincare pullback of fibre class 2 Theta.
- The new detailed audit `jaswal_point_chain_second_pass.md` records exactly which source proofs were read, which elementary calculations were reconstructed, and which deep analytic, compactification, monodromy and Bruhat–Tits results remain granted.


## mumford_theta_orbits

# Literature search and exact opened locators

Date: 2026-11-24. Searches used two internet search indexes, with the stronger index for verification and primary-paper retrieval. No priority claim is made. Primary papers were opened through the search tool; their binary PDFs were not downloaded by this worker, so no invented binary SHA-256 is recorded. The returned final workbench should contain none of these papers or full-text extractions.

## Queries and outcomes

- `Madapusi Pera Tate conjecture K3 Kuga Satake correspondence algebraic reduction endomorphisms Theorem 2015`: located the author's research page and arXiv:1301.6326. Opened the paper; its precise scope is primitive divisor classes/special endomorphisms, not a full algebraic KS correspondence.
- `Bolognesi Laterveer Clifford Kuga Satake Mumford fourfold half twist`, followed by `"Bolognesi" "Laterveer" "Kuga" "4.4"`: located the original article and later discussions. Used the original arXiv paper, not the discussions, for every mathematical attribution.
- `Haan Rallis inner product formula U(1) U(3) Theorem 3.4 3/2`, then `Haan U(1) U(3) Rallis inner product formula refined Gross Prasad unitary groups`: located arXiv:1403.5061; opened Theorems 3.4 and 3.5 and the relevant normalization text.
- `Mumford fourfold ordinary reduction Frobenius rank maximal torus Noot`, then `"Abelian varieties with l-adic Galois representation of Mumford’s type" Noot pdf`: located Noot's author manuscript. Its proof of Proposition 4.1 supplies the cube-weight Frobenius relation analysis needed to justify the ordinary count.
- `Mumford fourfold ordinary Tate classes 132 8 32`: no primary source stating the exact 132/100/32 decomposition was identified. The combinatorial calculation is written out without a claim of novelty.
- `Kudla Millson unitary U(p q) special cycles codimension rq degree theta integral Siegel Weil`: located Bergeron–Millson–Mœglin's author manuscript, which gives codimension rq; the degree-at-a-CM-fibre question requires additional data.
- `site.arxiv.org Kudla Millson unitary special cycles codimension rq Shi`: found a 2026 injectivity preprint, arXiv:2611.21692. Its PDF could not be opened through the retrieval tool; no theorem from it is used.
- `Nouveaux théorèmes d’isogénie 1.8`: opened the authors' manuscript of Gaudron–Rémond and checked the exact statements used in the supplied CM orbit derivation.
- `Tate Endomorphisms of abelian varieties over finite fields 1966 pdf theorem 1`: opened the primary scan and corrected the locator from “Theorem 1” to “Main Theorem, p.134.”

## Primary sources read

1. Keerthi Madapusi Pera, *The Tate conjecture for K3 surfaces in odd characteristic*, arXiv:1301.6326v3; Invent. Math. 201 (2015), 625–668. https://arxiv.org/pdf/1301.6326. Opened Theorem 3, printed p.2; Theorem 4.17(1)–(4) and proof, printed pp.22–23. Retrieval references include `turn158063467view1`, `turn902593823view1`.

2. Michele Bolognesi and Robert Laterveer, *A 9-dimensional family of K3 surfaces with finite-dimensional motive*, arXiv:2310.11981v2; Rend. Circ. Mat. Palermo (2) 73 (2024), 2313–2331. https://arxiv.org/pdf/2310.11981. Opened Conjecture 4.2, Theorem 4.4 and its proof, printed pp.14–15; Proposition 6.2, p.16 and Proposition 6.4, p.17. Retrieval references `turn507652215view0`, `turn760519776view2`. The source asserts the specified KS embedding's algebraicity; this worker did not re-prove all cited dependencies.

3. Rutger Noot, *Abelian varieties with ℓ-adic Galois representation of Mumford's type*, J. Reine Angew. Math. 519 (2000), 155–169. https://irma.math.unistra.fr/~noot/publications/crelle.pdf. Author manuscript §1.2 and Lemma 1.3, pp.4–5; Proposition 4.1 proof, pp.12–14. Opened and used the exact relation-kernel calculation; an ordinary-only valuation proof is written separately. Retrieval references `turn308156296view0`, `turn623802417view0`, `turn750978353view0`.

4. Rutger Noot, *On Mumford's families of abelian varieties*, J. Pure Appl. Algebra 157 (2001), 87–106. https://www.math.unistra.fr/~noot/publications/jpaa.pdf. Opened introduction, maximal-torus argument near §3 and §4 on Newton polygons. This is context; the ordinary-count proof cites the preceding 2000 paper.

5. John Tate, *Endomorphisms of abelian varieties over finite fields*, Invent. Math. 2 (1966), 134–144. https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf. Main Theorem, p.134 and opening proof setup. The divisor consequence also uses the usual Rosati identification of the Néron–Severi space with symmetric homomorphisms. Retrieval `turn762350643view0`.

6. Jaeho Haan, *The Bessel period of U(3) and U(2) involving a non-tempered representation*, arXiv:1403.5061v7. https://arxiv.org/pdf/1403.5061. §3.3, Theorem 3.4, p.8; §3.4, Theorem 3.5, p.9; normalization at pp.6–8. Retrieval `turn480229330view1`. This is a norm formula, not an identified degree formula for the proposed detector.

7. Nicolas Bergeron, John Millson and Colette Mœglin, *The Hodge conjecture and arithmetic quotients of complex balls*, author manuscript. https://math.umd.edu/~millson/papers/BMM_Unitaire_Revision.pdf. Introduction, printed p.4, codimension rq of positive special cycles. Retrieval `turn215952039view2`. Only the standard geometric dimension statement is used; the manuscript opened has unresolved bibliography placeholders and is not used for a deeper theorem.

8. Éric Gaudron and Gaël Rémond, *Nouveaux théorèmes d'isogénie*, Mém. Soc. Math. France 176 (2023), authors' September 2022 manuscript. https://lmbp.uca.fr/~gaudron/art20.pdf. Notation 1.1–1.2 and definitions, pp.10–11; Theorem 1.5(2), p.13; Theorem 1.8, p.15; comparison with Proposition 13.7 in the proof summary p.111. Exact statements match the uses in the supplied orbit note. The full isogeny theorem was not re-proved. Retrieval references `turn750978353view1`, `turn750978353view2`, `turn480229330view2`.

## Coverage limitations

The algebraicity of the full KS correspondence on all reductions was not established. No detector degree was extracted from a Rallis norm. The Siegel orbit estimate is an explicit hypothesis in the transferred statement until its whole analytic input is admitted by the main audit. Searches found no reason to claim priority for the elementary orbit restriction or cube-weight enumeration.


## Primary worker searches

- General terms searched: effective Andre--Oort relative Weyl discriminant, least splitting prime under GRH, Hilbert polynomials bounded degree, CM splitting torus ordinary reduction, Gaussian split Weil eightfold Hodge conjecture, Kuga--Satake Mumford ordinary Tate classes; arXiv, authors' pages, journal pages, ECCC and Hexagon were included in the source searches. This is not an exhaustive literature census.
- Pila--Shankar--Tsimerman arXiv2109.08788v4: primary record opened; full Andre--Oort theorem1.1. No complete reproof claimed.
- Jaswal Hexagon2611.00339v3: source and primary record opened; AI/no-human-understanding status noted. Application chain and numerical inequalities checked, outside dependency chain not wholly checked.
- Alpoge https://alpo.ge/remark.pdf: announcement opened. Asserted Dirichlet GRH used conditionally; formal development not independently replayed.
- Hu Hexagon2610.00216v2: primary PDF opened, Corollary9.6 pp56--57; effective absolute least-prime constant not printed numerically.
- Bach--Sorenson Math.Comp65(1996), Theorem5.3 pp1731--1732: primary AMS search result gives coefficient2 for p<2(q log q)^2; later PDF open returned403.
- Haan arXiv1403.5061v7: primary PDF opened, Theorems3.4/3.5 pp8/9 distinguish3/2 and1/2, with different rank patterns.
- Brian Conrad, Shimura--Taniyama formula, https://math.stanford.edu/~conrad/vigregroup/vigre04/stformula.pdf: primary author notes opened, Theorem2.1 p3.
- Official OpenAI withdrawal README for Algebraicity of Weil classes on split abelian eightfolds opened. README dates withdrawal October6; repository history entry dates October7. Sign error prevents use as a theorem. URL: https://github.com/openai/math/blob/main/preprints/Algebraicity-of-Weil-classes-on-split-abelian-eightfolds-September-18-2026/README.md

Other authors' source bodies and downloaded PDFs are excluded from every returned ZIP. Hashes and exact locators are recorded where downloaded. Web-tool pages without downloaded bytes have URLs and access notes, not fabricated byte hashes.

# Additional primary-source checks, 2026-11-25

- Duyan--Halasi--Podoski, author PDF https://zhalasi.web.elte.hu/papers/16_CoprimeRandomBase.pdf: Lemma3.1 pp5--6 and Theorem4.1 p7 opened and read for normal quasisimple character ratios and the extraspecial case.
- Guralnick--Saxl, Generation of finite almost simple groups by conjugates: original publication text read through a mirror, Table1 p554, Lemmas3.1--3.4, Theorem4.4 and Lemma6.1. The publication PDF download returned403, so no PDF byte hash is claimed. Only the exact used statements and local proof passages were checked, not the whole paper.
- Hiss--Malle, Corrigenda: Low-dimensional representations of quasi-simple groups, LMS J.Comput.Math.5(2002),95--126: primary Cambridge corrected table pp102--103 read. Download SHA256 0c0e7bbb1ee9857a5339a14f017ebad8d69e7e91d98682697816f9e65920fd7d. Primary URL: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A3E3E934BEB019B905E1BBCA4A0F20D5/S1461157000000711a.pdf/corrigenda_lowdimensional_representations_of_quasisimple_groups.pdf
- Theta/Chow degree work is ongoing. No new explicit H(D) theorem has yet been accepted from this search; candidate formulas are labelled candidates in research notes.

## Theta degree and embedded deformation inputs

Mumford I Proposition3/Theorem2 pp295–298 and symmetric marking remarks pp318–320 were inspected in the primary PDF; Mumford II exact theorem statements pp83–84 were read in indexed primary text, not claimed as a full original-proof read. Freitag–Salvati Manni arXiv1606.04468 pp1–3 supplies the theta compactification normalization discussion; no high-genus image normality is asserted. Guerra–Pirola arXiv0807.2980v2 §5.2 supplies the Chow-form characterization, with an explicit regular-sequence/Macaulay derivation here. Koblitz Compositio31(1975), Lemma12(1) pp165–166 and IV.6 pp178–181, and Stacks Tag0E3S are the exact tangent/deformation locators used. The full-generality PST source remains cited as preprint: primary arXivv4 and authors' pages did not establish a journal publication. No priority claim is made.


## 2026-11-25 — primitive finite groups, theta rounding and source precision

Zalesski, J.London Math.Soc.74(2006),361–378, DOI10.1112/S0024610706023039: Lemma6.3 p375 gives exactly the primitive irreducible ordered-tensor-indecomposable dichotomy used in the rank34 assembly. The ordered convention appears after Lemma6.8 p376. Root read the primary author-upload text; a separate worker downloaded and visually inspected the journal PDF, SHA256 a659b08727023b88345cf09bf54eb74465408222303c279d408a53a660467823. Only Lemma6.3 is used, not Lemma6.4's scalar-kernel wording. Source URL and search audit are in cycle_degrees/zalesski_primary_pdf_addendum.md and INDUCED_COVER_GATE.md. General searches of arXiv, journals, author pages, ECCC and Hexagon found no exact preceding rank34/68 statement; no priority claim is made.

Cohen1976 Lemma2.7 pp389–390 and classifications(4.16)p412,(5.12)p435, together with Malle1999 Table8.2p675/G34p661, support the strengthened reflection argument. The independent tensor-power proof is elementary and uses no classification.

Tsimerman2018, Annals187 pp379–390, Theorem1.3 p380 (not the conjecture labelled1.1), was reopened and downloaded, SHA25643259ca3cfedfb574bf1fe2f80e1023cb736ea299a76588536fd816340722abc. Primary URL: https://annals.math.princeton.edu/wp-content/uploads/annals-v187-n2-p02-p.pdf . Madapusi Pera arXiv1301.6326v3 Theorem4.17 p22 explicitly assumes odd characteristic; B now says so.

Exploratory searches for a universal low-degree cycle exclusion on a simple abelian eightfold did not yield a usable theorem. Debarre's primary minimal-class and Fulton–Hansen/Barth–Lefschetz papers were inspected; geometric nondegeneracy alone was not promoted to an unproved degree bound such as1680. This attempt did not move the detector gate.

## 2026-11-25 — corrected representation degrees34–49

Primary HM2001 Theorem1p22, generic Table2p31 and characteristic conventionsp30 were read by root; SHA25683b68deb2a468db04e34da07bef713c203a3e0b6e3e4f46bfcdd5bc10249fda2. Corrected HM2002 Table2pp103–106 was visually inspected in all four pages; SHA2560c0e7bbb1ee9857a5339a14f017ebad8d69e7e91d98682697816f9e65920fd7d. Publisher PDF URL is in cycle_degrees/quasisimple34_47_audit.md. Root reopened Guralnick–Saxl2003 primary article text at https://www.academia.edu/164985288/Generation_of_finite_almost_simple_groups_by_conjugates and read Lemmas3.1–3.4, Theorems4.1–4.4, Theorem5.1, Lemma6.1 and Table1p554. All outer and small-field exceptions in the used ranges were included. Real-model FS+ is distinguished from merely real-valued characters. The new coefficient thresholds are deductions from those exact published inputs; no priority claim is made.

## 2026-11-25: arbitrary abelian supports and ordered factor2

General searches: abelian subvariety normal obstruction deformation Weil type unitary period domain semiregularity; finite group tensor representation two-dimensional factor Hurwitz period dimension reflection; explicit ECCC and Hexagon queries. Primary journals, arXiv and author sources were opened. The searches located no direct published version of the precise structural factor2 bound or the new support application; this is not an exhaustive novelty claim. Existing Bhattacharjee–Bhattacharya Secant Objects (Preprints.org202611.0672v1,6Nov2026) and Markman ICM2026 were reopened and are already discussed/cited in B with their exact scopes and analytic limitations.

Van Geemen, Fourfolds of Weil type and the spinor map, arXiv2205.00483v2, §§4.3–4.5, p7: root read the full primary page, confirming the full U(n,n)/(U(n)×U(n)) domain and conjugation action. PDF SHA2563d3dc2e16f6ac70925de0ea17db92f5952f8928e486f4d452f98032274cc5010; https://arxiv.org/pdf/2205.00483v2; DOI10.1016/j.exmath.2023.04.006. The normal-direction lemma is proved in the paper rather than attributed to this source. The factor2 result uses the earlier exact Cohen classification/unique-coordinate-system locators; it adds no quasisimple classification premise.

### 2026-11-25 03:41 UTC — fourfold secant antecedent and exact scope

General search for secant sheaves, fourfold semiregularity and rank one returned the primary rStation37v4 note by lelong_ridge and cm_symmetry_scout (24 October2026). TheoremsA--C in section1 and proofsA--B in sections3--4 give the ordinary Chern-character test; TheoremB_G in section1 states a free-translation equivariant form. We opened that primary page and downloaded its Markdown only into the excluded external_sources directory: URL https://rstation.ai/api/v1/papers/hodge_conjecture_37/versions/4/download ; SHA25678e8346daa9a74a5e0f140477d04e36a28e0e840a02617ee431d6b2a3a60718c ;72989 bytes. We credit these results and give our full proof for the precise determinant-normalized and arbitrary-product-action hypotheses. The earlier search-snippet exposure of our author is disclosed in its dated addendum; the independent statement-only checker had not seen that source. No priority claim.

The search also opened the New York Journal of Mathematics primary page for Caldararu--Willerton16(2010),61--98, and the local primary PDF's p83 and pp88--89. Markman's primary2502.03415v2 pp51--56 were checked at the scope of the individual records. The arXiv abstract fetch failed in the web connector, but the exact PDF is available and was read locally. Queries restricted to ECCC and Hexagon found no additional result used here; unrelated supersingular-Mumford material was not taken up. An author/seminar search confirmed the Markman lecture/preprint trail. The stronger restricted-obstruction claims of rStation37v4 are being compared separately and are not inputs to our strong-condition theorem.
# 25 November 2026, fourth-period additions

The complete source/version audit for the relative analytic and formal comparisons is `research/mumford_theta_orbits/analytic_formal_antecedent_search.md`, SHA256 f78f85fac891002c6c9ce2984156770b9710d6a4b488be5e8d0170bf6b73d710. Root read all136 lines. It records arXiv, journal, author, ECCC and Hexagon retrieval with explicit limits. Artin Theorem1.2, Block Theorem3.2.7(2) and Proposition4.1.2, CHL Theorem8.3, and ELO Definition5.2/Theorem8.1 have their exact roles and version locators. Wei's fixed-manifold result is credited; the varying-symbol proof supplies its own Sobolev/Green estimate. Holstein--Porta, Porta--Yu and van Garderen (2026) are nearby antecedents, with only the reported portions read. No absence or priority claim follows from the search.

The Gaussian78 assembly uses the corrected Hiss--Malle ordinary rows on printed pp106--110, Guralnick--Saxl's exact conjugate-generation bounds and the explicit Schur-cover presentation in Fayers--Morotti, Math.Z.309(2025),article27, section4.1, DOI10.1007/s00209-024-03646-x. Root visually read all five table pages and checked the named generation statements and Schur presentation; this does not reprove the imported classification. The further78--99 scan remains preliminary background. The primitive ordered100 argument has independently frozen spectral derivations and does not depend on that additional scan.

The current semiregularity proof is under review. Root has read Quillen's original superconnection statement, transgression calculation and proof in section2, printed p91, and Buchweitz--Flenner's connection-commutator construction. The precise full-trace definition and source page reconciliation are still being checked. No broad analytic perfect-object exclusion is claimed from this unfinished comparison.

