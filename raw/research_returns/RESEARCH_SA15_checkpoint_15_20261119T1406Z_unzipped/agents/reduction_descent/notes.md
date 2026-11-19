# Parts B and C: active research notes

Owner: GPT-6 Astra (OpenAI), subagent /root/reduction_descent. Started 2026-11-19 03:52 Europe/Berlin. These notes are intermediate and contain explicitly separated proved claims and research gates.

## Confirmed directions

1. B.1 admits elementary explicit counterexamples; Kisin modules are unnecessary for existential refutation. At p=3, K=Q_3(zeta_3), E: y^2+y=x^3 has all nine 3-torsion points over K and additive potentially good reduction. Delta=-27, v_K(Delta)=6 prevents good reduction, and j=0. The division polynomial is 3x(x^3+1). This sharpens the e=6 proposed construction to e=2.
2. For every odd p, start with any good supersingular elliptic curve over an unramified p-adic field F with algebraically closed residue field. The p-division field is tame cyclic of order p^2-1, as follows directly from the height-two formal group Newton polygon. Fix the scalar -1 subgroup and twist: an additive curve with rational full p-torsion results over a field with e=(p^2-1)/2. Precise proof being written; no Kisin full-faithfulness is used.
3. C.1's claimed equivalence iff reduced is false even if the reduced theorem holds: over S=Spec(k[[t]][eps]/eps^2), U=D(t), characteristic p, Serre-Tate and the equal-characteristic p-divisible good-reduction criterion imply F is an equivalence. The nilradical is nonzero at T. Need cite/open de Jong 1998 Theorem 2.5 and Tate extension theorem.
4. C.3 has an affirmative proof using representability of Hom of BT groups by an affine inverse limit and a finite schematic image. Rigidity is needed only for noetherian nilpotent thickenings, not on every test ring. Important correction: unrestricted formal unramifiedness of Hom_BT over Z_p is false. Over Z_p plus the square-zero module Q_p/Z_p, compatible roots 1+1/p^n define a nonzero Q_p/Z_p -> mu_{p^infty} morphism reducing to zero. This does not invalidate C.3 because all finite images and derivation tests are noetherian.
5. Lead B' requires an additional hypothesis. A successive extension of potentially good p-divisible groups over a characteristic-zero field need not have a potentially semistable Tate representation. The representation [[1,log chi_p / p],[0,1]] over K containing mu_p has constant graded pieces, yet nonzero nilpotent Sen operator, hence is not Hodge-Tate and has no Fontaine WD representation. On potentially semistable objects the character agrees with the trace on the associated WD inertial representation, by exactness and comparison for the good graded pieces.

## Gates not resolved

- Sharp classification of all ramification e and semistability defects in B.2, and all higher levels and dimensions in B.3.
- Least uniform level in B.4 for arbitrary height.
- C.1 essential image in full generality; C.2 reduced nonexcellent bases.
- C.4 effectivity for reduced/nonreduced arbitrary locally noetherian bases. The proposed nodal twist by -1 is not a counterexample: such descent data are effective finite etale twists. Normal case follows from extension of homomorphisms of abelian schemes over normal bases, pending exact primary locator.

## Source record so far

- Read supplied c9_c100.md, sections 3 (cote9), 1-5 (cote100), and STUDY.md section3. R3(a) ordinary argument is mathematically sound with explicit mu_p assumption and a careful multiplicative connected part. R3(b)'s asserted unrestricted full-faithfulness G_K -> G_Kinfty is not accepted without checking its precise theorem.
- Opened Katz (1981), Serre-Tate local moduli, author's PDF https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf: Lemmas 1.1.1-1.1.3 and Theorem 1.2.1, pp.141-146. This verifies the nilpotent characteristic-p deformation equivalence and rigidity.
- Opened SGA7 IX §5 online transcription https://grothendiecksga.com/read/sga7/en/9-5.html, to be corroborated against original scans if obtainable; target Theorem5.10.
- Opened Vasiu-Zink (2012) arXiv0911.2474 abstract; full source not yet read, hence not used.
- Located de Jong (1998), Homomorphisms of Barsotti-Tate groups and crystals in positive characteristic, Invent.Math.134,301-333; author DVI identified but web tool does not parse DVI. Need materialize/convert or alternative PDF.
- Search 2609.06554 Ozeki-Yoshida appeared, but arXiv abstract fetch disabled; not used.

## Search queries (exact phrases)

- elliptic curve full p torsion additive reduction ramification index p
- abelian variety good reduction p torsion ordinary Serre Raynaud criterion
- "full" "p-torsion" "additive" "ramification"
- elliptic curve rational p-torsion semistable reduction ramification Lorenzini
- "semistable" "torsion" "p-1" "ramification" elliptic
- "semistable reduction" "p-torsion" "ramification index"
- "good reduction" "torsion" "Vasiu" "Bondarko"
- "p-divisible" "inertial type" "torsion" determined
- "p-divisible" "extends" "abelian" "equal characteristic" "good reduction"
- de Jong 1998 homomorphisms Barsotti Tate groups crystals function fields normal 134 theorem
- Serre Tate theorem nilpotent ideal p nilpotent arbitrary schemes theorem deformations
- Katz Serre Tate local moduli 1981 pdf theorem 1.2.1
- de Jong Homomorphisms Barsotti Tate groups crystals positive characteristic pdf 1998 2.5

## Verified source upgrades, 2026-11-19 03:18 UTC

- de Jong original TATE.dvi downloaded and converted correctly after fixing TEXMF font/prologue discovery; read Theorem1.1, Corollary1.2, section2 including2.5, and entire 1999erratum. Erratum changes Lemma2.1(iii)/Definition2.2 only, not2.5.
- Vasiu-Zink2012Boundedness read Theorem1,Corollaries1-4 andTheorem2; does not give least levels.
- Vasiu-Zink2010Purity supplied source read propositions labeled P7 and P9 and LemmaLe6; numbering to obtain from PDF. P7 states pdiv-extension implies abelian-extension over regular local mixed-characteristic rings. P9 uses geometrically unibranch projectivity, Raynaud ChapterXITheorem1.4.
- Krishnamoorthy-Pal2021RankTwo full publishedHTML opened. Corollary6.12 establishes normal locallynoetherian extension noexcellence; proof includes Mori-Nagata EGA0_IV23.2.6-8 and Krull schemes viaTheorem6.3. Need check all hypotheses of reductions.
- Berger2004Introduction authorPDF opened/read §II.1.2p9, exact non-Hodge-Tate upper-unipotent logcyclotomicexample.
