# Literature and source-access record

All searches below were made on 25 November2026. Published claims are used at their stated scope. None of the retrieved external sources is included in this workbench. Exact downloaded-source byte hashes are in records/EXTERNAL_SOURCE_HASHES.json; source pages are listed below. The attached sources have separate provenance in CROSSWALK.tsv and the topic audit notes.

## Search channels and findings

- arXiv and journal searches for Grothendieck–Teichmuller abelianization, invariant quadratic characters, Kummer cocycles, and the gentle pentagon found the classical Lochak–Schneps questions, Ihara's cocycles, Furusho's arithmetic/geometric comparison, and Marin's rigidity characters. No verified resolution of the full profinite abelianization problem was found.
- Author-page searches opened Schneps's Inventiones2000 text, her 2006 automorphism paper, Ihara's bibliography, Furusho's Math.Res.Lett.2003 paper, and Marin's Burau-rigidity exposition. Ihara's bibliography identifies the beta/gamma papers as LMS256(1999),144–179, and J.reineangew.Math.527(2000),1–11.
- Queries for Ihara beta/gamma unitarity, parity, multiplication, and rho_mn found Furusho2003 §2.2,p100 and §2.3,p101; Lemma3.2,p104 explicitly uses the extra Anderson multiplication relations to derive cocycle additivity. This prevents silently treating multiplicativity as a defining GT relation.
- Recent arXiv searches and direct retrieval opened Willwacher, arXiv2610.15592v4, 28October2026, pp1–2 and §3. Theorem1.1 plus Brown's free odd-generator injection proves the rational Deligne–Drinfeld statement used here. The characteristic-two theorem is a different statement. OpenAI's primary math repository was opened; a challenge file containing a placeholder is not counted as a formal proof.
- Forward literature search opened Markarian, arXiv2611.01745v2, 18November2026, Theorem4.8, §5 and AppendixC. It gives a geometric interpretation and restricted tangent reconstruction in the pro2 setting. Its warnings about leading survival for a larger solution set reinforce the distinction between an infinitesimal equation and full realization.
- Hexagon searches found indexed H17 material. Direct page retrieval was unavailable through the search interface; the attached version2 text and its explicit check records are the source used. The monoid note is likewise used from its attached text at TheoremsA andE. No contrary claim about their review status is made.
- ECCC searches for Grothendieck–Teichmuller and Teichmuller returned no relevant result; an unrelated computational report was discarded. This is a search result, not a claim that no relevant work exists anywhere.
- The mathematics-workbenches FORMAT.md and requested workbench URL failed through the search interface. An ordinary public raw-file download subsequently succeeded for FORMAT.md, and its complete text was read. Exact format adaptation is recorded in records/FORMAT_STATUS.md.

## Primary sources and exact uses

| Source | Locator used | Role |
| --- | --- | --- |
| Furusho, Geometric and arithmetic subgroups, MRL10(2003),97–108 | §2.2,p100; §2.3,p101; Theorem3.1; Lemma3.2,p104 | Integral cocycles, beta factorization, scope of additional multiplication relations |
| Nakamura–Schneps, Invent.Math.141(2000),503–560 | Definition5.1, Proposition5.3, closing paragraph of§5; Theorems1.3,1.4,11.2 | Frame normalization and tower actions |
| Schneps, Math.Nachr.279(2006),656–671 | §1 and p670 | Kummer cocycles and normalized relation |
| Marin, Characters through rigidity of the Burau representation | §§4–6 | Comparison with known rigidity and Soule characters |
| Schmidt–Wingberg, arXiv:math/9809211 | Theorem1,p1 | Solvable inverse Galois realization |
| Willwacher, arXiv2610.15592v4 | Equations1–7, Theorem1.1,pp1–2; §3 | Rational grt generation and recent context |
| Markarian, arXiv2611.01745v2 | Theorem4.8,§5,AppendixC | Restricted tangent interpretation, not full profinite comparison |
| Milne, Class Field Theory v4.03 | ChapterV,Theorem3.27,p165 | Conductor–discriminant formula |
| LMFDB256.1.c.a | Properties, q-expansion, Artin representation link | Classical quartic Kummer example, conductor256 |
| Boggi, arXiv2011.15075v6 | Theorem3.12,Corollary3.15,Remark3.11; Proposition6.9,Lemma6.16 | Inertia-preservation claim and separate proof issues |
| Lochak2025 author version | Definition5.4,Proposition–Definition5.6,Definition5.8,Theorem5.10,pp50–62 | Compatible pairs and procongruence identification |

Additional searches and exact source observations remain in research/towers/LITERATURE.md and research/graded/README.md. A failed retrieval is not treated as verification. No priority claim is made for results proved here.

## Distribution correction and additional primary checks

- Enriquez, Quasi-reflection algebras and cyclotomic associators, Selecta Math.13 (2007),391–463, arXiv math/0408035v2, Section8 Theorem8.1 equation(50), author pp30–32, and Remark8.6 p32. Full profinite GT satisfies all Kn, and rho_ab=rho_a+rho_b integrally. This corrects the earlier tentative treatment of multiplicative defects as open candidates. The source PDF and derived text are outside the deliverable; its hash is recorded.
- Moree–Stevenhagen, Computing higher rank primitive root densities, Acta Arith.163 (2014),15–32, arXiv1203.4313v2, Section2 Theorem2.5, author pp4–6. The rational-radical Galois image and its quadratic entanglement are classical. The paper supplies the precise GT normalization application.
- Herfort–Ribes, Torsion elements and centralizers in free products of profinite groups, J. reine angew. Math.358 (1985),155–161. TheoremB p155 and TheoremB-prime Section4 p159 apply to every nonidentity factor element, not just torsion. Opened the original paper text; used for the parabolic centralizer.
- Furusho2003 Theorem3.1 p102, Lemma3.2 and Theorem3.4 p104: exact dyadic Anderson consequences. The proof of the individual frame signs also uses Section2.3 p101 and H17 Lemma15, with a separate statement-only reproof.
- Anderson, The hyperadelic gamma function, Invent. Math.95 (1989),63–131, Corollary8.6.3. The exact beta form was directly inspected in Furusho Remark2.4 p101. The original full Anderson article was not accessible beyond its subscription preview; no direct full-paper check is claimed.
- Current primary searches for the odd Anderson determinant and for maximal abelian CM-field intersections were made. No searched secondary summary is used as a proof source. The CM image comparison is still under reconstruction and not yet cited as a theorem of this paper.

## 25 November 2026, 05:00 Europe/Berlin — cubic and CM comparison searches

- Searched general terms for cubic Magnus coefficients, two-adic divisibility, Ihara/Soulé characters, and Kummer normalization across arXiv, journals, author pages, ECCC and Hexagon. No verified source was found for the exact joint radical/cubic normalization proved here; this is not a priority claim. Several search hits concern only rational or pro-unipotent characters and are not substituted for an integral theorem.
- Opened Marin, *Characters of the Grothendieck–Teichmüller group through rigidity of the Burau representation*, Ann. Fac. Sci. Toulouse17 (2008),765–780, §6.3 p780. It gives arithmetic expansions and extends the degree-three and degree-five Soulé characters through rigidity. The paper credits this classical construction but defines m3 directly and proves its integral normalization without asserting an unchecked scalar conversion to a Soulé convention.
- Opened Milne, *Modular Functions and Modular Forms*, version1.10, Remark12.12 and Proposition12.13 p119 and Theorem12.27 p124. These give the precise abelian CM torsion and ray-class reciprocity input.
- Opened Papikian, *Rigid analytic geometry and abelian varieties*, 13June2004, §2, Theorem2.2 and pp3–4. The complete nonarchimedean-field and Galois-compatible Tate uniformization supports the signed integral comparison, including prime2. The torsion filtration is derived explicitly in the paper.
- Downloaded primary PDFs for these three sources and Moree–Stevenhagen into temporary research storage; only their citation, URL, SHA-256 and used pages are included in the workbench.
- The earlier statement that the CM image was still under reconstruction is superseded: the complete signed comparison and arithmetic quotient are now proved and separately targeted-checked. Combining CM with radicals is still a separate joint-image gate.

## 25 November2026 — integral weight five and radical–CM entanglement

- Repeated primary searches for integral two-adic Soulé/Magnus weight-five images and their Kummer normalizations. Marin2008 §6.3 p780 remains the verified classical extension reference; no searched result was used as an exact integral saturation theorem. The precise image32Z2 is proved by finite integral coefficients and an arithmetic witness in this paper.
- Searched for the Gaussian eighth-root extension, ray conductors and CM torsion. No snippet or secondary account was used to set its conductor. The proposed conductor exponent8 is derived directly from Eisenstein quadratic integral bases and Milne Class Field Theory V Theorem3.27 p165; CM containment uses Milne Modular Functions and Modular Forms Theorem12.27 p124.
- Searched for the exact overlap of all rational radicals with the two CM maximal abelian fields; the proof here uses the classical radical affine group from Moree–Stevenhagen §2 Theorem2.5 and an explicit simultaneous derived-subgroup calculation. No claim of priority is made.
- Reopened Enriquez2007 §8, Theorem8.1 equation(50), pp30–32 and Remark8.6. Its full distribution equation is delta_N(f)=y^(c_N(f))f. It gives Kummer additivity. It is not silently identified with Anderson gamma multiplication. Furusho2003 §2.3, Definition2.3 and Remark2.4 explicitly distinguish Anderson A_n from these defining relations; the latter beta form is the precise candidate tested here.
- A search located Goto–Ishii, arXiv2610.21052, CM Elliptic Analogue of Coleman–Ihara Formula, October2026. Only its abstract has been read so far; no theorem from it is used and no unsupported comparison of scope is made.

## Additional search before the fourth checkpoint

2026-11-25: searched primary arXiv, Numdam and author-page sources for integral Soulé/Magnus weight-seven divisibility and Ihara beta/CM eighth-root comparisons. The directly relevant results returned Marin, Characters of the Grothendieck–Teichmüller group through rigidity of the Burau representation, §6.3 p780 (already read), and Furusho, Three subgroups, §2.3 Definition2.3 and Remark2.4 (already read). Marin provides the degree-three/five arithmetic character comparison; Furusho distinguishes the arithmetic Anderson relations from their proposed full-GT extension. Neither locator supplies the exact normalized weight-seven64/128 interval or proves the outstanding tame tests. No priority claim is made. Other search matches were not used as mathematical inputs.

## 25 November 2026, 05:21 UTC — finite harmonic and cubic comparison

Opened Tsunogai and Nakamura, *Harmonic equations in the Grothendieck--Teichmuller group*, RIMS Kokyuroku1267(2002),197–208, Theorem2, printedpp199–200, <https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1267-18.pdf>. The formulas GF0 and HF1 are explicitly for the Galois image. At multiplier one and rho2=rho3=0 they identify the inverse harmonic and cubic frames with f(u,s) and f(u²,r); their scope is not enlarged to GT.

Searched finite SL2 modulo8/quaternion/binary tetrahedral quotients and GT harmonic/equianharmonic relations using both search systems, including arXiv, Hexagon and ECCC terms. No source for the precise192-to24 map used here was located; no priority conclusion is drawn. Citation-forward results identify Nakamura--Tsunogai partII, Contemporary Mathematics416(2006),197–211, and Nakamura--Tsunogai--Yasuda partIII, Journal of the Institute of Mathematics of Jussieu9(2010),431–448. The journal abstract of partIII concerns a Galois matrix specialization through a one-parameter quartic family; full text is assigned for further investigation, and no theorem from it is used at this point.

## 25 November 2026 — weight-eight commutator layer

Searched profinite GT integral weight-eight commutators, Soulé characters and two-adic images. The primary source returned was again Marin2008, Section6.3,p780, which extends the weight-three and weight-five arithmetic characters through Burau rigidity. The primitive degree-eight bracket is consistent with the classical rational odd-weight Lie generators and their bracket, but the precise integral image on D7 used here is proved directly. No source claiming that exact normalized image was located, and no priority claim is made.

## 2026-11-25 05:36 UTC — eleventh multiplication and finite-cover comparison

Queries: Grothendieck Teichmuller Kummer Anderson multiplication formula homology determinant cyclic cover; site:hexagonmath.org Grothendieck Teichmuller Anderson; then the stronger-engine queries "Grothendieck" "Anderson" "Kummer" Enriquez relation and "Grothendieck" "multiplication formula" homology determinant. Results again locate the Nakamura–Tsunogai–Yasuda part III author-uploaded paper and the already cited H17/monoid notes. A Journal of Algebra 2018 paper on Galois action on relative Fermat homology was located as a lead; it was not used to assert a full-GT comparison. Several broad-query hits concerned unrelated knot or analytic determinant formulas and were not used. The precise sources used remain Enriquez, Theorem8.1 and Remark8.6, and Furusho2003, p.102; the two explicit local-system and linear-sign arguments are proved in full in the paper. No priority claim is made.

## 2026-11-25 05:43 UTC — classical Bolza identification

Primary-source comparison identifies the genus-two cover with the classical Bolza curve. Opened Katz–Katz–Schein–Vishne, Bolza quaternion order and asymptotics of systoles along congruence subgroups, Experimental Mathematics25(2016),399–415, DOI10.1080/10586458.2015.1073642, author PDF https://u.math.biu.ac.il/~scheinm/text61.pdf . Corollaries13.3–13.4 and the displayed matrices immediately before Corollary13.4, author pp24–25, give the identical generating pair after conjugation by T. Also opened Koziarz–Rito–Roulleau, The Bolza curve and some orbifold ball quotient surfaces, https://www.math.u-bordeaux.fr/~vkoziarz/Bolza.pdf , section4 equation(4.1), author p7, for the model y²=x⁵−x and classical automorphism group. Their attribution to Bolza1887 is reported, not an assertion that the original nineteenth-century paper was inspected. The paper now gives explicit credit and states only its specific mod8/frame calculation. Download hashes are recorded separately; no source copies enter the workbench.

## 2026-11-25 05:58 UTC — exact nonabelian dyadic source check

Reopened Furusho2003 at the author URL already recorded. Read section3 equations(1)–(4), p102, and the entire printed statements and proofs of Lemmas4.1–4.2, pp105–106. The first is equivalent to IV, and the second follows from I,II,IV; both are full profinite word identities, not Galois-only or derivative statements. The new normalized harmonic-frame identity is derived from these exact identities, K2 and the pure-frame uniqueness argument. No inference that the remaining cubic defect vanishes is made. The source hash is unchanged from the earlier download.

## 2026-11-25T06:38:05.648216+00:00 — Integral beta boundary measures

Searched general beta/gamma, Soulé, Kummer-congruence and universal-Jacobi-series terms through journal and author pages, arXiv and Hexagon. Opened Furusho2003 Theorem3.1 p102: normalized dyadic duplication is an identity in the completed group algebra, not merely selected character values. Opened Nakamura, Arithmetic and Combinatorics in Galois fundamental groups, RIMS Kôkyûroku2120(2019), pp188–198, §§0.1–0.2: arithmetic Soulé expansion, Coleman space and the Vandiver gap. Followed his references to Ichimura–Kaneko, J.NumberTheory31(1989), pp312–334: §1.2 p314 explicitly assumes an odd prime; Theorem1p315 characterizes the arithmetic image under Vandiver. This is relevant context, but does not directly state the present dyadic full-GT coordinate bound. Opened Ihara–Kaneko–Yukinari author scan, introduction and §1; detailed coefficient-theorem scope remains to be read. Hexagon2611.00939v2 search metadata concerns the pro-p outer Galois action under Vandiver; opening failed, so its mathematical statement has not been used. Three downloaded source hashes are in EXTERNAL_SOURCE_HASHES.json; source files remain outside workbench. No priority claim is made.


## 2026-11-25T06:58:45.476318+00:00: cubic special homomorphisms and all-odd normalization

Opened Schneps, *Automorphisms of curves and their role in Grothendieck--Teichmuller theory*, Math.Nachr.279(2006),656-671, author-hosted journal PDF <https://webusers.imj-prg.fr/~leila.schneps/automorphisms.pdf>. Read Definition1.2 p658, Theorem3.1 p665, and Theorem3.4 with the full NT2 strand-forgetting calculation, equations3.10-3.11 p667. Its scope is the subgroupGS defined by special-homomorphism compatibility, not allGT. The cubic proof in the present paper uses full-topology centralizers, HMM rigidity and exactK3 to extend the normalized comparison tofullGT; the normalized identity implies precisely the inverse of3.10. The earlier Galois-only HF1 scope of Nakamura--Tsunogai remains distinguished. Source SHA256: c77dad73a1c20ba751e5c884f98483f47d6a716b04032538a76586b3e22f6742.

Stronger-engine queries: Grothendieck Schneps NT2 profinite; arXiv Grothendieck special homomorphisms cyclic; Hexagon harmonic Grothendieck; ECCC Grothendieck Teichmuller. Located the Schneps primary journal paper and author preprint, the H17 and monoid notes already used as background, and general braid-action references. No relevant ECCC result or separate full-GT cubic comparison was found in these results; no exhaustive coverage or priority conclusion is asserted. The broad Hexagon result on Grothendieck inequalities is unrelated and unused.

The earlier all-odd beta search covered the author sources of Ihara--Kaneko--Yukinari, Ichimura--Kaneko and Nakamura, as recorded above. Additional arXiv/ECCC/Hexagon dyadic-beta queries returned no further relevant theorem; several broad hits concerned Grothendieck inequalities or fusion rings and were excluded. Ichimura--Kaneko's Theorem1 uses an odd prime and its Vandiver hypothesis, not the exact dyadic statement proved here.

Completed the cubic topology source audit: HMM author31-32, BZ TheoremA andSection6.1, Asada RIMS1179 introduction theorem, BH Theorem1p424 andp433 plus2017erratum, Gardiner--Hu uniquenesspp14-15 andexistencep22, and Kerckhoff's cusp extensionpp255-256. All downloaded files remain outside the workbench; hashes and the exact read scopes are recorded.


## 2026-11-25T07:14:58.567773+00:00: mixed degree-eleven coordinate follow-up

Searches: arXiv domain, “Grothendieck Teichmuller Ihara bracket integral degree eleven Soulé characters 2-adic”; Hexagon domain, “Grothendieck Teichmuller beta function Ihara bracket eleventh weight”; ECCC domain, “Grothendieck Teichmuller Ihara bracket”. The indexed results returned Furusho’s stable derivation/MZV paper (arXiv:math/0011261), the already cited Hexagon background notes2611.00940v2 and2611.01024, and unrelated ECCC Grothendieck-inequality results. They did not supply a result on the stated integral mixed coordinate. This is a narrow search result, not evidence of absence or a priority claim. The arithmetic witness and explicit bracket identity are proved directly in the paper. Stronger primary-source follow-up remains scheduled.


## 2026-11-25T07:32:41.934891+00:00: stronger primary-source follow-up

Stronger-engine searches for fullGT special homomorphisms, NT2, Ihara beta integral characters and degree-eleven brackets again located Schneps2006 on the journal and author sites; no separate fullGT NT2 theorem appeared in those results. Followed its special-locus reference to Schneps, Special loci in moduli spaces of curves, MSRI41 (2003),217–275, authorPDF https://webusers.imj-prg.fr/~leila.schneps/MSRI.pdf . Read Section4.3 Theorems4.3.1–4.3.2 and Section4.5: cyclic genus-zero normalizers surject onto the quotient pure mapping class group, whereas the genus-one unbranched-cover example has a proper liftable subgroup. No generic finite-cover compatibility is inferred. The author preprint numeral “index2” for <tau1,tau2²> was not used; the modular index requires separate checking. The journal scan text extraction was corrupt, so the readable author text is used with its own page locators.

Opened Hoshi–Mochizuki–Tsujimura, J.Math.Sci.Univ.Tokyo32(2025),1–125, TheoremC(ii) p5 and introductionpp2–6. It characterizes the Galois subgroup through additional arithmetic-Belyi/algebraic-ampleness conditions; it does not supply a calculation of the relative abelian quotient. It is included as directly relevant anabelian context. Downloaded source hashes are recorded.

Re-read Willwacher arXiv2610.15592v4, pp1–4, especially Theorem1.1 and its integral defining-system basechange in Section1.1. The rational upper bound in degree11 is2, and may replace the large necessary-system calculation after checking the leading-map hypotheses. Characteristic-two Theorem1.3 has different odd generators and is not silently identified with their rational names. Its recursive { [x,y], - } formula is being investigated as a possible arithmetic integral mechanism, not yet asserted.

### 2026-11-25T07:37:17.846513+00:00: exact algebraic-ampleness scope

Read Hoshi–Mochizuki–Tsujimura Definition5.12 in full, pp87–90. AA requires ArBC, the additional conditions(i)–(iii), and the configuration-space compatibility(iv). The context paragraph cites these hypotheses explicitly; it does not infer that full GT satisfies them.

## Main-gate literature refresh, 2026-11-25T07:57:57.272713+00:00

Queries on profinite GT abelianization, integral Deligne-Ihara generation, and arithmetic mixed monodromy led to primary BCL arXiv2004.08860v3 (Theorems1.2,1.3 and2.1, pp2-4), Hirose arXiv2610.23719v1 (pp1-3, Theorem4 and Section1.2 p2), and Sharifi math/0104116v2 (author pp1-2). BCL extends generalized-Jacobian representations to a finite-index automorphism subgroup; it does not compute the full normalized GT image used here. Hirose proves a Z_(2) Hoffman-basis result and gives an alternative rational Deligne-Drinfeld argument; no integral arithmetic pro-two generation is inferred. Sharifi explicitly assumes odd regular primes in the relevant theorem, so it cannot supply a dyadic generation step. Marin Sections3.2-4.3 pp771-775 were reread. Furusho2010 printed p554 was read in full to check the completion/associator bridge. These bounded searches do not establish priority or absence of other work. Downloaded source bytes remain outside the workbench; exact hashes are recorded.

## Uniform dyadic image source check — 2026-11-25T08:22:38.778114+00:00

Root read all10pages of Willwacher2610.15592v4, including characteristic-two freeness Theorem1.3p2, the extended Ihara bracket Proposition4.1pp6–8, proof§4.3p9 and integral-lattice discussion§4.4p10. These are exact primary inputs for the emerging uniform arithmetic-generator argument; the rational upper bound alone is not used to infer integral saturation. Queries for pro-two GT/Galois image and integral arithmetic Willwacher results were run with the stronger search engine and recency365days. No matching fullprofinite conclusion was verified; this is a bounded literature search, not a novelty guarantee. The Hexagon2611.00939 page couldnot be opened byweb; its identifier mustnot be confused witharXiv2611.00939, anunrelatedCS paper. No theoremfromthatinaccessibletext isused. KMT2017§7 relates Ihara power series, Jacobi sums and Soule cocycles ontheGaloisside; it isneighboringcontext, not afullGTimage theorem.

## 2026-11-25T08:36:21.258140+00:00 — Uniform dyadic arithmetic-image comparison

Repeated strong searches for pro-two GT/Galois image, arithmetic realization of Willwacher generators, and Hexagon pro-two GT. They led back to Willwacher, OpenAI and Markarian; no search absence is used as evidence of priority. Directly reread Markarian Theorem4.8 and Section5, printed pp9–10: strict restricted tangent reconstruction and initial terms of solutions, not an asserted equality with the arithmetic image. The new proof cites Willwacher Theorem1.3 p2 and Section4.3 p9 for the free characteristic-two generators and supplies its own integral arithmetic construction. KMT2017 primary PDF hash is recorded; its Jacobi-sum/Ihara formulas are context, not a full-GT surjectivity input.

## 2026-11-25T08:44:02.238195+00:00 — Hain–Matsumoto and finite beta characters

Directly opened official Hain–Matsumoto2003 PDF and read Section8.5 printed p151. It states actual tangential pro-l automorphism-action unramifiedness outside Nl, not merely outer unramifiedness. Setting N=1,l=2 is the precise input for odd-prime inertia axes in the arithmetic pro-two kernel. PDF SHA256 b35079dd08fb5ebe6878fb49b05b137113e51f2ce26c88368e7e0ffcfec58f1a recorded. Rechecked Furusho2003 Remark2.4 p101 full Anderson beta formula, not only its derivative, for the new harmonic/cubic arithmetic residue calculations. No full Anderson formula on GT is inferred.

## 2026-11-25T09:21:19.224005+00:00 — full dyadic image and arithmetic free product

Strong primary searches for pro-two Grothendieck–Teichmuller/Galois freeness and Galois extensions unramified outside2 found Neumann, On maximal p-extensions, class numbers and unit signatures, Asterisque41-42(1977)239-246, Theorem3.7 printedp244. Opened the Numdam publisher archive and read the exact theorem: for the rational base field its group is C2 free-pro-two-product Z2. This is an earlier arithmetic group presentation, not a claim about all full profinite GT. The current proof determines the specific dyadic action image from uniform arithmetic leading lattices and a direct relation argument. No priority claim is made.

Downloaded and directly read OpenAI, The Deligne–Drinfeld conjecture,23September2026, introductionpp1-3 and Theorem1.1 printedp2. The theorem is the rational free odd-generator Lie algebra and its weight completion; it is contextual credit, with the explicit characteristic-two input taken from Willwacher. Primary PDF SHA5ae63f326803a634e7c6dc5684ce7062ea0ac6940a88a75c7052875382dbc762. Reopened Markarian Definition1.9, Theorem4.8 and Section5: restricted reconstruction on initial terms of solutions, not an arithmetic surjectivity statement. All source copies/extractions remain outside the workbench.

## 2026-11-25T09:30:58.866205+00:00 — local CM inertia alternative

Lubin–Tate1965, Formal complex multiplication in local fields, Annals81(1965)380-387, p380 conditions(1) and reciprocity(2): tower worker checked the indexed primary scan; root read the complete resulting local proof. URL https://math.bu.edu/people/jsweinst/AWS/Files/LubinTateFormalCMinLocalFields.pdf. Full PDF download and root direct-open timed out, so no local-file SHA or full-article reading is asserted. This source supports the alternative seven-inertia witness, not the independent pure-primary proof of the strict gate.


## 2026-11-25T09:53:00.114167+00:00 — exact odd CM image and quadratic Galois target

The complete primary Lubin–Tate1965 scan was retrieved from https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/lubin-tate.pdf . Root and tower read pp383–384, the formal-group criterion and Theorem2(b,d,e) with its Eisenstein proof. SHA b1d5502619d8f182861bef3b5f66b351a2274ed35afa445416a26aed8dae04f0; historical failed downloads remain recorded.

For the exact odd CM image, the allowed full integral cubic comparison and arithmetic CM image were rechecked. Local inertia uses Milne MF110 Theorem12.27 p124 and Hain–Matsumoto Section8.5 p151. The independent construction obtains the joint image, not only separate projections.

Strong searches for invariant square classes in cyclotomic-radical extensions, dihedral Redei extensions, Hexagon quadratic GT characters and ECCC Galois characters were followed by arXiv/journal/author-site searches for Stevenhagen Redei reciprocity. The classical5,29 norm example was located; it is not claimed as a new field construction. Opened Stevenhagen arXiv1806.06250v3 and the Cambridge publication listing (Math.Proc.Cambridge Philos.Soc.172(2022)627–654). The direct primary proof of the exact K2 target will use class field theory and continuous group cohomology. Root reopened Milne CFT4.03 and read II Remark1.35 p72, IV Theorem3.14 p137, VII Theorem7.1 pp219–220 and Theorem8.1/reciprocity diagram pp221–223, and VIII Theorem4.2 p241. No search absence or priority claim is inferred.

## 2026-11-25T10:07:43.730268+00:00 — arithmetic target cohomology and classical dihedral fields

Root read Hochschild–Serre1953, ChapterIII Theorem2 pp129–130 and Section6 Theorems3–4 pp132–133 with proofs, including the extension-class cup differential. Continuous adaptation is Milne CFT II Remark1.35 p72 and Section4 pp87–88. Root opened Stevenhagen, Redei reciprocity, governing fields, and negative Pell, arXiv1806.06250v3, Lemma5.1 and Corollary5.2 with proof and Remark5.4, authorpp9–10; these explicitly give the classical norm/dihedral construction and central embedding problem. The paper now cites this directly for the5,29 witness. No novelty or absence inference is made. Primary source PDFs and extracts remain only outside the workbench; exact hashes are in EXTERNAL_SOURCE_HASHES.json.

### 2026-11-25T10:13:07.868995+00:00 — odd-prime target exact locators

Root checked Milne CFT printedp81 PropositionII3.4 with proof, printedpp49–50 TheoremI4.16 with proof, in the original primary PDF (PDF pages90 and58–59; nine-page frontmatter offset). Earlier root checks coverII1.35p72, IV3.14p137 andVIII4.2p241. The independent odd-target source audit additionally checksII1.22p67, II4.2pp87–88, I1.1p20 andLubin–Tate1965p380formula2. No source extraction entersworkbench. The exact two-place coefficients are proved directly by comparing trivial/cyclotomic connecting cocycles and were independently sign-checked by root with the tame relator.

## 2026-11-25T10:44:07.051612+00:00 — finite cyclic covers, beta values and quadratic central extensions

Strong-search queries, run after10:23UTC: (1) Grothendieck Teichmuller quadratic characters Jacobi sums Redei cup product; (2) Ihara Anderson beta function quadratic character symplectic normalizer cyclotomic cup product; (3) site:arxiv.org GT quadratic Jacobi Fermat; (4) site:hexagonmath.org GT quadratic; (5) Grothendieck Teichmuller quadratic Jacobi; (6) Ihara Redei beta; (7) site:eccc.weizmann.ac.il Grothendieck Teichmuller; (8) symplectic normalizer cup product cyclotomic. Results included Otsubo2016, Nakamura2021slides, Hirano-Morishita2019 and the existing Hexagon notes. No matching fullGT family theorem was verified; search absence is not used as priority evidence. The Hirano-Morishita publisher open returned500, so no theorem from that inaccessible page is used.

Root directly opened Otsubo, Homology of the Fermat Tower and Universal Measures for Jacobi Sums, Canad.Math.Bull.59(2016)624–640, doi10.4153/CMB-2016-012-0. Read introductionpp624–625 andSection7p637eq7.1–7.2 with the comparison argument. This credits classical arithmetic Fermat homology and its equality withAnderson beta onGQab. The currentfinite symplectic normalizer construction proves the central extension onthefullperipheral action. PublisherPDF SHAe0cd1343e29105644090c7577c214a7e72f945269b54c271df655aab6ef83f57; onlycitationmetadata entersworkbench.

## 2026-11-25T11:03:14.621094+00:00 — dyadic unit norms and quadratic lifting context

Root directly read Milne CFT II Proposition1.22 and Corollary1.23 on printedp67, and III Propositions1.1–1.2 on printedpp97–98, including the unit norm and principal-unit trace arguments. These provide exact primary locators for the unramified unit calculations; the full cyclic-cover proof gives the remaining formulas directly.

Strong searches around10:52UTC: Grothendieck quadratic characters surjective; Ihara Hilbert symbol beta; symplectic normalizer unramified2-adic; site:hexagonmath.org characters Grothendieck. Results included previously known Hexagon material, Nakamura2021slides and Hiroo Miki, Jacobi sums and the Hilbert symbol for a power of two, J.Math.Soc.Japan48(1996)367ff. Root opened the J-STAGE primary PDF and read only its introduction onp367. It concerns arithmetic Jacobi sums and conductors; no full-GT lifting theorem is inferred. A subsequent find timed out; no unread theorem is attributed. No search-absence or priority claim is made.

## 2026-11-25T11:16:41.031750+00:00 — companion characters and primary formulas

Strong search queries: Ihara Kummer cocycle quadratic character beta function Jacobi sums duplication; Grothendieck Teichmuller Kummer character symplectic homology quadratic; Fermat curve Jacobi sums quadratic residue reciprocal Grothendieck Teichmuller; site:hexagonmath.org Kummer beta quadratic characters. Results included the already cited Marin2008 rigidity paper, Nakamura–Schneps, a curve-automorphism paper and arithmetic Jacobi-sum sources. Only the primary formulas already read are used in the new proof; no search-absence or priority inference is made. Root reread Furusho2003 printedp102 directly from the primary PDF extraction, including B{x,x}=x^(-2Psi2)B{-1,x} and Theorem3.1. Root also directly read Milne CFT printedp248, including the explicit dyadic Hilbert-symbol formula.

## 2026-11-25T11:33:14.755840+00:00 — genus-two CM normalization and reciprocity refresh

Root searched the stronger web system for: `Grothendieck Teichmuller genus two complex multiplication Jacobian y^5 x(1-x) Galois image`; `site:arxiv.org cyclotomic Jacobian complex multiplication local reciprocity y2 x5 2-adic image`; `site:hexagonmath.org Grothendieck Teichmuller arithmetic quotient genus two`; and `site:eccc.weizmann.ac.il Grothendieck Teichmuller complex multiplication`. Returned primary listings include Teichmuller curves/Galois actions, Yelton generic hyperelliptic 2-adic images, and the already cited Hexagon monoid theorem; they were not used as proof inputs. A secondary listing for a CM Honda-system example was also unused. No absence or priority claim follows. The mathematical input is Milne CM2020, official author PDF, directly read at Example1.19 p14, Proposition1.26 p17, Corollary6.11 p51, Section9 p76 and Theorem9.10 p78; faithfulness was checked at p52. The exact local inertia formula follows here by auxiliary-coefficient removal from that adelic theorem, not from a guessed finite-character correction.

The character worker also records six focused Anderson/beta reciprocity queries in relative_kernel_reciprocity/RESEARCH_STATUS.md; both search systems returned the already inspected Furusho2003 and unused older subgroup listings. The elementary common-cover limitation needs no new external theorem. No newly verified source in those searches settled the full-GT cross-coefficient sign.

## 2026-11-25T11:44:34.290302+00:00 — simultaneous cyclotomic CM normalization

The general cyclotomic extension uses the same directly read Milne CM2020 Example1.19, Proposition1.26, Corollary6.11 and Theorem9.10, plus Milne CFT II1.22/1.23 and III1.1/1.2 for field Hilbert90 and unit norms. Product-algebra descent, exact polynomial criterion, torsion and cross-prime witness separation are proved here; no class-number formula or priority claim is used. Earlier broad cyclotomic/CM/GT searches are recorded above.


## 2026-11-25 — post-checkpoint13 primary-source review and recovery

The root primary readings used Agoh2012 Eq1.2 p1 (odd prime conductor), Dummit2020 Proposition1(1)-(2)p207, Anglès–Nuccio2010 definitionp201 andLemma5.1p214, Otsubo2016 Theorem8.1/Remark8.3/Corollary8.4 pp638–639, Zarhin MPIM18-31 Theorem3.2 printedp13 andExample3.7 printedp16, Milne CFT4.03 II1.35p72 andII4.2p87 withfollowingcontextp88, Furusho2003 Theorem3.1p102, andLochak–Schneps1997 section1pp571–572. Root opened the cited sources and checked these inputs before mathematical acceptance. Exact recovery URLs, hashes, byte counts and printed/PDF page mappings are in records/recovery_external_sources_20261125.json. The recovery worker visually inspected all14 cited pages. Source PDFs and extracted source text are excluded from the workbench.

The Jacobi conventions are not interchangeable: Otsubo's residue exponent is(Nv-1)/p, while Anglès–Nuccio uses(1-NP)/p. Both sums have a leading minus sign. The roots used for the Frobenius computation are labelled to match these conventions. Furusho Theorem3.1 requires I,II,IV,K2; the recovered paper's uses explicitly provideIV fromH17 andK2 fromEnriquez. S1–S3 continue to be cited rather than reproved.

The topicality search at13:37–13:40 found no resolution of the full profinite GT/Galois abelianization question. The2026 finite-dihedral quotient paper gives those specified finite images; it does not settle the global relative kernel. No priority claim is made for the classical CM determinant interpretation.

## 2026-11-25 — omitted-prime cohomology and complete CM products

Searched the web in general terms for Grothendieck–Teichmuller arithmetic quotients, abelianization, Jacobi sums, Kummer units, inertia and continuous cohomology; separately searched arXiv, Hexagon and ECCC, then followed Lochak–Schneps citations through author and journal pages. ECCC returned no relevant exact match in this search; that is not an absence or priority claim. Opened Lochak–Schneps, Inventiones 127 (1997), pp.571–600, at https://webusers.imj-prg.fr/~pierre.lochak/textes/inventiones.pdf; its introduction interprets GT equations by noncommutative cohomology and proves the Galois inclusion and complex-conjugation centralizer result. Opened Enriquez, arXiv:math/0408035v2, at https://arxiv.org/abs/math/0408035; its distribution theorem is the already cited input GTK=GT and does not by itself identify every cyclotomic real-unit Kummer relation on full GT. Opened Milne, Class Field Theory v4.03, https://www.jmilne.org/math/CourseNotes/CFT.pdf; the exact continuous-cohomology locators remain II Remark1.35(b), p.72, and Proposition4.2, p.87, already inspected in the source recovery. Current journal/author search results include Collas on torsion action and Schneps/Scheiderer publication lists; no new theorem is imported from a search snippet. Hexagon returned the already cited relation-IV and monoid notes, not an identified prior statement of the present exact CM-image product or omitted-prime quotient theorem. No priority claim is made. Source PDFs stay outside the workbench; their hashes and pages used are in the existing source registry.

## 2026-11-25T16:27:03.403716+00:00 — acyclotomic twist and circular-unit scope

Opened both author and publisher versions of Lochak–Schneps2015, reading Theorem2.1, block definitions(9)–(12), Lemma3.1 and the displayed conjugator calculations. Visually checked authorp4 and publishedpp126–127. The first argument in the first conjugator of F23(z) in(10) must be z by the block definition; the publication fragment makes this emendation explicit. Formula(26) and the following x14 cancellation have opposite conjugator requirements; their exact displays and the still-open off-diagonal convention audit are preserved in the research packet. The determinant calculation is insensitive to this inversion. No claim that the intended theorem is false is imported.

Dummit2020 p206 and Proposition2, pp209–210, were reread in full at their used scopes. Circular-unit finite index/rank and the conductor163 signature defect are unconditional; the asserted full real class number4 is conditional in that source and is not used. Furusho2003 §2.3,p101 explicitly recalls Ihara’s full adelic beta factorization, including rational-torsion evaluations; the new finite cyclic gamma argument uses precisely this scope. Source PDFs remain outside the workbench, with URLs and exact hashes recorded.

## 2026-11-25T16:45:59.018855+00:00 — exact convention and background checks

Lochak–Schneps2015, definitions9–12, Lemma3.1, and sphere equations14,16,18 were read in full again. A direct two-pentagon derivation under Inn(g)(h)=ghg^-1 gives the conjugating proword f(x23,x12), reversing the arguments in printed equation8. The publication states this convention and gives the whole derivation; it does not rely on the inconsistent action display26. The finite matrix identity detects the same scalar coordinate and kills multiplier-one commutators.

For the independent CM-frame reconstruction, root read Campagna–Pengo arXiv2006.00883v3 pp13–16, Theorems4.6 and4.7, including their exact maximal-order/invertible-ideal scope. The Weber theorem includes the extra-unit casesj=0,1728. All other quoted CM source hypotheses were matched to the specified Legendre fibers.

For the independent peripheral lift, root re-read only the permitted S3 surface criterion, Hexagon2611.01024v1 TheoremE(a), pp2–3, verifying its application to three-boundary genuszero and one-boundary genusone surfaces. No proof of S3 was undertaken. The remaining character-theory inputs are finite-group semisimplicity and Schur lemma; the finite central multiplier is explicitly constructed in the new proof.

## 2026-11-25T16:54:18.291570+00:00 — nonabelian quotient literature

Searched for full profinite GT solvable quotients, A4 and SL2(F3) quotients, and representations extending Galois actions. Read the primary arXiv v3 statements of Bleher–Chinburg–Lubotzky Theorems1.1–1.3 (2004.08860) and Bortnovskyi–Dolgushev–Holikov–Pashkovskyi Theorem5.3, Corollary5.4, Theorem5.7 and Proposition5.8 (2405.11725, revised6August2026). The first result concerns finite-index extensions of specified generalized-Jacobian representations; the second gives arithmetic surjectivity for the two-power dihedral finite quotient family and its infinite index-two affine subgroup. General dihedral arithmetic surjectivity remains Conjecture5.1 in that paper. The present search produces no comparison that evaluates our relative central obstruction. These results are credited in the paper, with no novelty or global nonexistence claim inferred from the search. Third-party files remain outside the workbench.

## 2026-11-25T17:04:24.132688+00:00 — finite quotients and possible central lifts

Searches: profinite GT solvable quotients of derived length three and SL2(F3); quaternion and binary tetrahedral quotients; finite-group GT constructions of Guillot; metaplectic GT constructions; cyclotomic degree163 beta/gamma and class numbers. The retrieved primary leads are Guillot arXiv1407.3112 and1604.04415, his author bibliography, and Kitchloo–Morava arXiv1212.6905. No theorem from a search snippet is used. The proposed inference from a calculation of GT(F) for one finite groupF to every possible homomorphism GT→SL2(F3) has no established factorization step. Existing dihedral arithmetic surjectivity and generalized-Jacobian representations concern their specified quotient maps. The obstruction remains open. The source-reading record will distinguish any exact scope actually inspected.

Primary follow-up: Guillot1407.3112v3 pp1–3 explicitly identifies his inverse limit with Drinfeld’s gentle GT0, not full pentagon GT. Guillot1604.04415v1 Theorem1.1 and Proposition3.2/Corollary3.3 pp1–3 prove finite-field characteristic-two rigidity. The degree163 detector here lives over O/4 and its principal scalar is identically1 after reduction modulo2, so the cited rigidity does not evaluate that detector. Kitchloo–Morava1212.6905v3 Corollary3.7/Theorem3.11 pp10–11 and Appendix4 pp13–14 concern a characteristic-zero proalgebraic and graded-abelian construction; no profinite F2 vanishing theorem is inferred. All downloaded hashes and exact pages are registered, and all third-party files stay outside the workbench.

2026-11-25T17:12:25.335572+00:00: Follow-up searches for GT and SL2(Z/4), finite local rings and quaternion quotients returned no primary GT theorem eliminating the integral deformation. A representation-theory paper on SL_n over rings of length two is a separate possible input, not yet used. Grothendieck manuscript and generic moduli/symplectic results in search output were not imported.

## 2026-11-25T17:25:49.443956+00:00 — scope check on a recent profinite-space claim

Read the primary abstract and HTML introduction and Theorem3.1 of Noemie C. Combe, arXiv:2503.13006v2 (2July2025), https://arxiv.org/html/2503.13006v2 . The theorem identifies underlying profinite spaces with Cantor space. The introduction explicitly leaves surjectivity of the fixed natural Galois embedding open. It supplies no group-homomorphism extension or evaluation of the present relative central classes. No theorem from this preprint is used in either paper, and no main question status changes.

## 2026-11-25T17:28:38.167087+00:00 — elliptic sections and a specified completed surface operad

Searched primary-source literature for profinite elliptic GT sections and degree-three isogeny compatibility. Enriquez, Elliptic associators, arXiv:1003.1012v3, Proposition2.20 explicitly extends its section to the full profinite setting; Proposition8.3/Theorem8.4 give the arithmetic elliptic action. Those statements alone do not identify the exact action through the degree-three modular degeneracy correspondence. The required equality d3(f(a,b))=f(a,b) remains unproved.

Read Basualdo Bonatto–Robertson, arXiv:2606.01466v2 (8October2026), Corollary4.4, Definition4.8/Theorem4.9 and Corollary6.13/Proposition6.14 directly in the primary PDF. It constructs a particular completed surface modular operad, its action by the Nakamura–Schneps subgroup, and determination by the genus-at-most-one truncation. With the stipulated H17 background this action is a full-GT action. The precise current source is credited in the paper; it does not identify the absent historical E230 construction or recognize arbitrary connected-complement multicurves. Its homotopy-one-type tower scope is not conflated with a full higher-genus etale K(pi,1) theorem. No question status changes and no smaller main relative gate results. The institutional PDF endpoint failed with403; the primary arXiv PDF was read successfully.

## 2026-11-25T17:34:46.788696+00:00 — connected-complement and braid searches

Queries: profinite Dehn twists braid relation intersection one Boggi nonseparating; procongruence connected complement automorphisms; profinite braid relation curves. Primary leads include Boggi–Funar’s author PDF https://www-fourier.univ-grenoble-alpes.fr/~funar/bf_final.pdf and the published procongruence curve-complex article DOI10.1112/topo.12306, together with classical discrete Dehn-twist braid statements. No newly read theorem with the missing profinite unit-power converse was imported. The already recorded closed-pair result and punctured-annulus limitation remain the accepted scope.

## 2026-11-25T17:44:15.895353+00:00 — transfer proof standard inputs

Root read Lazard 1954, Chapter II 4.2–4.6, pp175–180, including the small-class correspondence and preservation of subgroups, ideals and homomorphisms. Root also read Cohen–Falk–Randell, Section4, p223, and Cohen–Pakianathan–Vershinin–Wu, p149: the ordinary pure braid Lie presentation is integral. The pro-p completion passage is supplied in the independent proof using almost-direct free-group combing and Hall coordinates. This verifies prerequisites for the full gentle transfer; no new research movement.
