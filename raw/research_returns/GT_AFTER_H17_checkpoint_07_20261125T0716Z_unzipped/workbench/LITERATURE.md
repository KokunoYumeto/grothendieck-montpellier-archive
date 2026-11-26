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
