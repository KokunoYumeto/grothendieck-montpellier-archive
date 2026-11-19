# Parts B and E: working report, 2026-11-19 11:48 UTC

## State at first checkpoint

Both mathematical chapters have full drafts: `part_B.tex` has B.001–B.012, and `part_E.tex` has E.001–E.014. Exact programs and actual outputs are in `code/` and `logs/`. A final independent proof/source audit is ongoing; this is not a claim that the parent package is complete.

| Task | Current result | Remaining gate before agent sign-off |
|---|---|---|
| B.1 / L6 | Literal equivalence refuted by a three-element semigroup over F2; corrected reconstruction, rigidity, continuous duals, and Deligne derivation written | Final convention audit and parent review of counit hypothesis |
| B.1 source comparison | Takeuchi, Hai, Deligne, Schauenburg1998 and2003 primary texts opened; exact locators in B.012 | Verify any typesetting/citation-key errors |
| B.2(a) | Exact added biring/plethory data; finite64-element analyser satisfying1–3 with no compatible plethory; faithful-constants sufficient criterion | Final audit |
| B.2(b) | Divided-power nonunital analyser acts on PD ideals; all composition coefficients proved integral; literal3a impossible without unit terms | Final audit |
| B.2(c) | Counterexample F2⊂F4 to arbitrary-extension freeness; exact injectivity/image criterion; fraction-field+free-module theorem proved | The criterion is necessary and sufficient, but a structural classification of all inclusions is not claimed; parent must preserve this scope |
| B.2(d) | Exact coefficient null-polynomial criterion, full domain case, general Vandermonde sufficient condition | Final audit |
| E.1 | Every listed construction has a theorem/proof; three perspectives, torsors, bihexagons, affine triality, geometric realizations, finite counterexamples | Official119 scans156–160 pending root fetch; both doubtful normalizer readings proved regardless |
| L7 | Refuted by exact identification with Cameron2015 §§2–6, especiallypp8–9 | Root must open cited source before using its web citation |
| E.2 | Exact marked-disc word types and both isotypique/isotopique readings; full partial-involution criterion; all-genus map dictionary | Final audit; scan152/003,004 opened visually |

## Important corrections, with manuscript/transcription locators

* **155/002**, transcription `MPL_121_049-073+153+155_transcription.tex` scan002 beginning aroundline1396: data(i),(ii) omit multiplicativity of the anchor/counit. B.002 verifies every stated unital hypothesis and shows no tensor unit exists. It is not merely a nonunital counterexample.
* **155/004 / R7**: failure of the diagonal functor on arbitrary L⊗kL modules does not establish failure on A⊗kL modules. Under rigidity and End(1)=k the restricted functor is exact and faithful even for inseparable L/k (B.004).
* **155/006–010**: Hom_A(M,U) identifies canonically with the L-dual, but identifying End_A(U) with A-op using the k-dual requires a nonzero Frobenius functional L→k. Inseparable trace may vanish. Antipode existence alone must be accompanied by A-linearity of evaluation and coevaluation (B.005).
* **153/004**, scan beginningaroundline1163: the former domain/fraction-field assumptions are crossed out in the scan. Freeness does not suffice after replacement by an arbitrary ring inclusion. F2⊂F4 is a finite-field counterexample (B.008). The fraction-field version is true (B.009).
* **153/006**, scan beginningaroundline1235: existential finite decomposition identities are not chosen coherent co-operations. The64-element quotient F2[T]/((T²−T)^3) satisfies all three axioms and has no compatible plethory (B.011).
* **153/010**: the divided-power example is naturally nonunital and acts on PD ideals; its coaddition lives in the augmented tensor target. Literal optional3a with both factors in a nonunital zero-constant analyser fails at G''=0 (B.006).
* **119/156–157**: rotation orientation of a square differs from sign orientation of its four vertices. The twist must use the side dual Q∨; ordinary vertex twist has no equivariant map, while the side-dual twist has exactly two (E.006).
* **119/156**: index10 in Aut(S6), not order10. Normalizer in G gives D8; normalizer in Aut(G) gives SD16, order16 (E.008). Both manuscript readings are treated, pending scan image.
* **119/156 / R12**: uniqueness is true for graphs containing translations and normalized by the direction-pairing stabilizer. There are nine graphs if normalization is omitted (E.008).
* **119/159**, transcription `MPL_119_144-161+119_276-281_transcription.tex` scan159 aroundline846: A requires distinct blocks. Conditionc alone does not force9 blocks; the explicit18-block counterexample satisfies it. Conditionsa+c do suffice (E.007).
* **119/160**: all monomial3×3 matrices over F3 form a48-element group. Determinant1 or quotient by±I gives S4 (E.002).
* **152/003**, transcription `MPL_152+120_transcription.tex` line183ff: “isotopique” visually supported. Exact combinatorial objects include a cancellation matching, root and boundary marks, and no unmatched gap inside a matched interval. If “isotypique” is intended, pass to isomorphism types as specified in E.010. Raw homeomorphism groupoids are not discrete type sets.
* **152/003**: displayed reduced order is n−2m for m>0 chords but n−1 when K is empty. It is not uniformly ordinary reduced word length.
* **152/004**, line283: literal one-edge contraction leaves an obstructing fixed point; delete both edges. With fixed points, the repaired criterion requires both noncrossing and no enclosed fixed point (E.011). Scanned wording confirms “l'une” remains.
* **152/010–013**, lines424–479: use σ=τα, not σ=τ; inverse convention is allowed consistently. One-edge tree distinguishes the formulas (E.012).

## Exact checks

`check_B_finite.py`: all eight elements of the F2 semigroup algebra; all512 associativity triples; all64 augmentation pairs; all64 coproduct multiplicativity pairs; both counit identities; all three tensor-unit candidates. Also16 tensors in the F2⊂F4 witness subspace; divided-power coefficients; and all262144 triples in the64-element analyser for associativity and decomposition identities. All assertions pass.

`check_E_finite.py`: all518400 multiplication pairs for the outer action; all36 point-total pairs and120 bijections each; twelve hemiicosahedra and all72 root descriptions; all8640 orientation actions; all90 edge and120 face perspectives; all16 square stabilizer elements and all24 proposed twists; all3×1440 graph isomorphisms; all432 affine maps and1296 conjugations; all54 lifts of double transpositions; all54 cross-class pairs in the18-block counterexample; exact small-projective-group computations; all pairings through14 positions and all involutions through10 positions. All assertions pass. The independent graph enumeration is deterministic and logs the three explicit conjugators.

## Sources opened and browser handles for root

* Deligne1990: https://www.math.columbia.edu/~dejong/tannakian/Deligne-Categories-tannakiennes.pdf ; IAS mirror https://publications.ias.edu/sites/default/files/60_categoriestanna.pdf ; browserref turn859131385view3. Theorem1.12, §§5.18–5.21,6.1–6.8,6.14–6.15; all relevant portions read locally.
* Takeuchi1977: https://www.jstage.jst.go.jp/article/jmath1948/29/3/29_3_459/_pdf ; download and local text opened. Definition4.5 pp474–475 expressly requires both coproduct and anchor algebra maps.
* Hai2008: https://arxiv.org/pdf/math/0206113 ; refs turn468435281view0, turn165180661view2/3/4. Author TeX https://arxiv.org/src/math/0206113 downloaded and relevant sections read.
* Schauenburg1998: https://schauenburg.perso.math.cnrs.fr/papers/bnrsthb.ps ; authorhomepage turn587942895view0, link75, unsupported browserpostscript refturn591045249view0; successful exec download, ps2pdf, text read. Theorem5.1 and Remark5.3, preprintpp15–17. Old LMU link404; publisher deliveredHTML, so not used.
* Schauenburg2003: https://arxiv.org/pdf/math/0204180 ; refturn165180661view1. §§2–3, Theorems5.1/5.5/6.1 read.
* Borger–Wieland: https://maths-people.anu.edu.au/~borger/papers/_all/PlethysticAlgebra.pdf ; refturn468435281view1; Definitions1.1/1.3/1.8.
* Elliott2010: https://www.numdam.org/item/10.5802/acirm.34.pdf ; refturn468435281view2; whole6-page paper read, including Problem16.
* Cameron2015: https://cameroncounts.wordpress.com/wp-content/uploads/2015/01/m12.pdf ; refs turn472750346view0,turn966145136search30. §§2–6 pp2–9; exact AGL identification§6 pp8–9.
* HMSV2008: https://math.stanford.edu/~vakil/files/sixjan2308.pdf ; refturn472750346view3; §§1.1–1.4 pp1–3, especiallyicosahedra§1.3.
* DeVos: https://www.sfu.ca/~mdevos/notes/comb_struct/blocks.pdf ; refturn472750346view1; pp6–8.
* Esquisse: https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseFr.pdf ; refs turn781910400view0,turn587942895view3; §3 printedpp14–17, §4 printedpp20–23.

All downloaded primary sources remain in this agent's `sources/` for inspection. They are not deliverable claims of ownership and should be excluded from the user's research checkpoint archive if appropriate.

## Original119 scan audit, 2026-11-19 11:58 UTC

Opened images of scan pages156,157,159,160,161 from the parent's `source_external/119_selected.pdf` (printed foliation155,156,158,159,160). The boxed formula on157 clearly reads Q*=epsilon wedge Q-dual: the dual marker is present in the manuscript. Thus E.006 repairs the transcription, not that boxed manuscript formula. Page156's earlier formula without the dual is superseded on157. Page159's A really lacks the distinctness condition. Page156's cramped normalizer subscript remains uncertain after enlarged inspection; E.008 covers both G and Aut(G) exactly. Source-opening gate closed; only that palaeographic ambiguity remains.

## A.6 added, 2026-11-19 12:20 UTC

`part_A6.tex` contains A6.001--009. The six recollement functors, actual and derived sheaf gluing, the full finite-poset corner reconstruction and inverse, the precise morphism correction, the surface peripheral-groupoid classification, and the general information bounds are written with proofs. `check_A6_finite.py` and its actual output verify the finite two-dimensional polygonal counterexample.

The reconstruction uses a conical control atlas with radial trivializations, exactly the explicit hypothesis of ALMP2012 Definition1(v), and compatible collars in the resolution datum. It does not silently invoke smooth ODE flows in an arbitrary real closed field. Its finite coordinate construction is valid for definable data as specified. The common-base labels for disconnected faces must be retained: an interval resolves both a marked circle and an interval if that grouping is forgotten. ALMP Remark2.4 itself records this issue.

Important new correction on121/039: arbitrary triples with G on the whole resolved X do not equal ordinary sheaves on the pushout with the proposed restrictions. For X=[0,infinity), Y=boundary X={0}, the nonzero triple (0, boundary skyscraper,0) has zero restrictions to both strata. The corrected open--closed functor is i^{-1}j_*, and p_* of a single link level computes it under radial constancy. A6.001 retains the valid abstract comma-category formulas.

Dimension2 groupoids: the peripheral functor Pi1(boundary M)->Pi1(M) recovers each compact surface's genus, orientation and boundary count. Aggregate attaching functors lose cyclic corner incidence. Two explicit null hexagonal words have identical such functors but link-component marked-point counts (3,1,1,1) and (2,2,1,1), so their stratified spaces differ. The full finite corner flags would distinguish them. In general ordinary groupoids retain exactly the1-type of each piece; aspherical coherent gluing diagrams recover full homotopy only by homotopy colimit, not ordinary groupoid colimit. The manuscript's undefined “special” and “admissible” terminology remains an interpretative limitation, recorded separately.

New primary sources opened, for root to reopen before web citations:

* ALMP2012 published PDF https://www.numdam.org/item/10.24033/asens.2165.pdf ; browserref turn550457255view0. Definition1(v)249--250; Definition3 p252; Propositions2.3 and2.5 pp253--257; Remark2.4 p254; Definition4 p258. All relevant passages and proofs read locally.
* Debord--Lescure--Rochon2015 published PDF https://numdam.org/item/10.5802/aif.2974.pdf ; browserrefs turn720499982view2,turn476656695view1. Definitions1.1/1.3, Lemma1.4 pp1804--1808, including full lemma proof; blowdown/resolution pp1809--1811.
* Albin2016 survey https://arxiv.org/pdf/1603.04106 ; browserrefs turn764380328view0,turn720499982view4. Section6.1--6.4, Theorem6.3 p48. Used to locate the two primary papers, not as a substitute for them.
* Stacks Project https://stacks.math.columbia.edu/tag/009Z and https://stacks.math.columbia.edu/tag/00AD ; refs turn720499982view1 and turn720499982view0. Opened ordinary restriction, closed extension and stalk assertions.
* Gallier--Xu author book https://www.cis.upenn.edu/~jean/surfclassif-root.pdf ; refs turn982324837view0,turn505601269view0. Author revision2025-01-08, Theorem6.2 p97 and polygon presentations pp101--103 read. One typo2q+p−1 onp102 was corrected from the displayed presentation; its later H1 formula is correct.

## B.2(c) strengthened, 2026-11-19 12:32 UTC

B.013 gives the complete finite-base classification: for every nonzero finite ring R and arbitrary unital overring S, the polynomial tensor map is injective iff S=R. B.014 gives the complete field-base classification and reduces torsion-free extensions of infinite domains to overrings in the fraction field. B.015 is a general finite-difference obstruction. B.016 constructs a one-dimensional Noetherian local domain R=F_q+t(t-1)T for every finite field, with g=((X^q-X)/m)^q-(X^q-X)/m in Int(R) but g(XY) outside the tensor image. All hypotheses, including locality, fraction field, Noetherianity and dimension, are proved. The q=2 example is credited to the newly opened May2026 primary preprint; the proof here generalizes it and removes dependence on its asserted general biring equivalence.

Actual verification: check_B_domains.py and logs/check_B_domains.txt contain84 exact rational-valuation checks for q=2,3,4,5,7,8,9 and n=1..12, plus all722 polynomial elements of degree<=4 in the relevant R for q=2,3,5. All passed. These checks supplement the universal proof; they do not replace it.

New source: Jiang et al., arXiv2605.25259v2, Theorem3.4 pp7--8, https://arxiv.org/pdf/2605.25259 , browserref turn793649937view0; full proof read locally. Its introduction's stronger equivalence is not used. Official Elliott arXiv1505.06493 notice, https://arxiv.org/abs/1505.06493 , browserref turn754749564view0, says withdrawn on2025-06-10 for critical errors; no theorem from that withdrawn paper is used. The2010 question is no longer described as current universal-existence status.

The remaining stronger structural-classification gate is explicit in unchecked_B.tex. The exact necessary/sufficient tensor criterion is proved, together with full finite-ring/field cases and a strong infinite-domain counterexample, but no invariant classification of all infinite nonfield domains is asserted.

## Compact two-dimensional reconstruction strengthened

A6.010 gives a complete positive classification for compact finite PL resolution systems of dimension<=2: peripheral surface groupoids plus the full cyclic corner flags/common-base labels and finite-covering monodromy with endpoint maps. The proof constructs the resolved-diagram homeomorphisms, including a boundary-extension proof and the orientable common-sign condition recovered from the peripheral kernel. This states exactly what must be retained beyond the aggregate diagram refuted by A6.008. Noncompact and higher-dimensional limitations remain those explicitly proved in A6.009.

## B.2(c) gate reduced again

B.017 proves a complete structural classification of bases with universal extension property: every unital inclusion R⊂S has the unique co-operations iff every maximal residue field of R is infinite. The proof uses local Vandermonde inversion and an explicit square-zero extension over any finite residue field. It includes rings with zero divisors and arbitrary, possibly nonflat extensions. The finite F2 square-zero example was exhaustively checked.

B.018 extends the freeness repair: for every infinite domain R and every R-torsion-free coefficient extension S, free Ω gives all multivariable tensor isomorphisms and the plethory. Thus the residual stronger structural gate is now restricted to infinite nonfield bases with finite residue fields outside these free-module cases. The exact tensor criterion for a specified arbitrary inclusion remains B.009.

## B.2(c) normal bases and projectivity

B.019 gives a finite dual-basis criterion, satisfied by every projective Ω, and proves all tensor powers directly. B.020 constructs the integer-valued module over every infinite Noetherian normal domain with any torsion-free coefficient extension as a direct sum of invertible fractional ideals times monic polynomials. This proves the unique plethory in that whole class and removes every Noetherian normal domain from the residual classification gate. The proof includes the DVR digit interpolation, finiteness of small finite residue fields in a Noetherian ring, Chinese remainder construction, and all intersection/localization steps.

Primary algebra inputs opened: Stacks tag031T Lemma10.157.6, https://stacks.math.columbia.edu/tag/031T (turn704987244view0); tag00PD Lemma10.119.7, https://stacks.math.columbia.edu/tag/00PD (turn704987244view1); tag00NX Lemma10.78.2, https://stacks.math.columbia.edu/tag/00NX (turn704987244view2). Proofs read. No unproved classification from the withdrawn Elliott paper is used.

## B.2(c): the nonnormal cusp gate removed, 2026-11-19

B.021 proves infinite-rank Milnor patching directly with an elementary block factorization and a patched complement. B.022 proves that Int(R) is projective for every R=F_q+t^mF_q[[t]]. B.023 extends this to R=k+t^m l[[t]] for arbitrary finite field extensions k⊂l. The proof is complete: mixed-digit Newton interpolation makes B=Int(R,l[[t]]) free; B/tB is an l-algebra with every element satisfying z^|l|=z; finite product decomposition gives exact q-Frobenius descent; the t-nilpotent matrix inverse gives the gluing isomorphism; B.021 proves projectivity. B.019 then gives all tensor isomorphisms and the plethory.

This refutes the two conjectured nonflat cases F2[[t²,t³]] and F2+tF4[[t]] recorded on page2 of Elliott's opened arXiv1109.3921 paper. The original q=2 cusp proposal and the infinite block patching were independently attacked by root and checked. Root also checked B.017--020, including the subtle coefficient-overring point in B.019. The finite-field extension descent in B.023 has been sent for root review.

Exact validation is attached as check_B_patching.py and logs/check_B_patching.txt:2800 denominator identities,116512 value lower bounds, all1638 invertible2x2 matrices over F2[t]/t^m for m=1,2,3 with lifted inverses checked in the untruncated polynomial ring, finite-field descent through F16, and all2048 cusp inputs modulo t^12. All assertions pass.

Source documenting the conjectures: https://arxiv.org/pdf/1109.3921 , ref turn704987244view3, introduction p2; official nonwithdrawn abstract https://arxiv.org/abs/1109.3921 , ref turn435584162view0. The downloaded PDF has an internal March8,2021 date despite arXiv's2011 v1 metadata; both are recorded in references.bib.


## B.2(c): complete finite-normalization classification in dimension one, 2026-11-19 13:34 UTC

B.024 proves projectivity for every unital R inside a finite-residue DVR V which contains a nonzero V-ideal. The proof works with arbitrary conductor gaps, finite residue extensions, mixed characteristic, and without completeness: greedy Newton polynomials make Int(R,V) free; iterates of (X^Q-X)/pi give every congruence-class indicator; high Q-powers lift them to every finite quotient; the resulting function modules split freely under refinement; explicit infinite Milnor patching proves projectivity. Root independently audited B.023--025 at13:24 UTC, including all these steps and the multiple-difference negative argument.

B.025 gives the local branch criterion for fraction-field coefficients. The negative proof explicitly constructs principal maximal ideals of the semilocal normalization by Chinese remaindering, hence an exact conductor generator. Multiplying the polynomial indicator by that generator puts every value in R. The higher-variable obstruction rules out binary multiplicative existence by finite iteration. B.026 classifies all coefficient extensions in the one-branch local class.

B.027 proves polynomial localization, including a uniform denominator for all values; no polynomial L-regularity assumption is imported. B.028 globalizes the branch criterion. B.030 gives the finite-extension obstruction with cofinite conductor. B.031 handles every coefficient overring at a multibranch local point: finite proper extensions fail injectivity; for an element b of negative branch valuation, Bezout puts the branch inverse in T[b], and multiplication by the conductor puts the existing obstruction in R[b]. B.032 consequently gives a complete criterion for every one-dimensional Noetherian domain with finite normalization and every torsion-free coefficient extension S. At each finite-residue maximal m, S_rat localized at m must be R_m, or K with a single normalization branch. No condition is needed at infinite-residue maximal ideals.

The actual new verification log is logs/check_B_conductor.txt:33,117 exact modular indicator evaluations for p=2,3; all1,024 splitting vectors over Z/4; six explicit conductor-exponent2 obstruction calculations; all16 elements and256 products in the finite tensor-algebra witness. All passed. B/E/A6 TeX inline and display delimiters are balanced. The P-Gamma-L and A-Gamma-L text-font glyph errors are fixed.

The Jiang2026 author source https://arxiv.org/src/2605.25259 was downloaded and opened locally at sources/jiang2026_source/main.tex, especially lines637--760, together with its complete section and reference searches. Section3.4 is the explicit F2 two-branch example; it does not contain B.024's one-branch projectivity or B.025's general branch criterion. Browser requests to that source and its abstract returned DisabledError (turn886152418view0/1), so these are not claimed as successfully opened browser pages; the successful local source fetch is documented. The original PDF ref turn793649937view0 remains the opened browser locator. No novelty or priority assertion is made.


## B.2(c): higher dimensions, nonfinite normalization and valuation domains

B.033 proves localization in all Noetherian dimensions by total-degree induction on s^dF(X)-F(sX). B.034 identifies the coefficient ring R^sharp with the punctured-spectrum intersection and proves its equality with R exactly when depth is at least two. B.035 handles every higher-dimensional finite-normalization local case, including normalization branches of unequal dimensions, and B.036 gives the complete global finite-normalization criterion. B.037 gives the explicit two-dimensional domain F2+(x,y)^2 F2[x,y]_(x,y) and its split tensor kernel. Root independently audited B.033--037 at13:50 UTC. The exact B.037 program checked512 tensor elements and262144 products, and262144 coefficient/input pairs; all passed.

After checkpoint04, B.038--041 were incorporated following root's independent audit at14:09 UTC. B.038 detects a tensor kernel by the R-balanced functional beta(F,G)=D(F'(0))G'(0) modulo a valuation overring, under the precise bounded-derivation hypothesis. B.039 completely specifies a characteristic-two Akizuki example using factorial exponents and proves its transcendence, Noetherianity, dimension, normalization and nonfiniteness. B.040 extends the tensor counterexample to all finite-residue Akizuki--Reid families, including mixed characteristic. B.041 proves the positive case of every infinite valuation domain of arbitrary rank and every torsion-free extension. No general nonfinite-normalization or non-Noetherian classification is asserted.

New primary source: Miles Reid, Akizuki's counterexample, https://arxiv.org/pdf/alg-geom/9503017, browserref turn631366328view0; root independently opened as turn680646715view0. The two theorems are onp2, with hypothesesp1 and proofspp2--4. Author LaTeX source https://arxiv.org/src/alg-geom/9503017 was opened locally in sources/reid_akizuki.tex, lines49--212. The sentence after Eq12 claiming that all f_i have coefficients in A when expanded in z is problematic for the displayed generators, and Eq12 has shifted summation bounds. Our direct derivation proof of nonfiniteness avoids both lines. The characteristic-two specialization also supplies independent ring-structure checks.

For B.034--036, opened primary Stacks sources are https://stacks.math.columbia.edu/tag/00L9 (turn392757328view0, Lemmas10.63.5/9), tag00LW (turn392757328view1, Lemma10.72.5), tag00LE (turn392757328view2), tag00DS (turn947256071view0, prime avoidance), tag00OG (turn947256071view1, Lemma10.112.4), and tag00GH (turn947256071view2, integral extensions). All cited proofs were read.

## 2026-11-19 14:26 UTC: Krull and infinite-residue cusp extensions

B.042 is proved for every infinite Krull domain, without a Noetherian assumption, and every torsion-free coefficient extension. B.043 completely classifies R=F_q+t^a l[[t]] for every infinite field l/F_q: only rational coefficient ring L=R works; fraction-field coefficients have an explicit tensor kernel. Both received independent root targeted proof audits. These classes are removed from the residual non-Noetherian gate. The source inventory requested by root is being written separately, with unread works and unsuccessful attempts explicitly distinguished.

## Requested-source inventory, 2026-11-19 14:28 UTC

`requested_sources.tsv` inventories every requested B/E/A6 source, with actual attempts, exact opened locators, browser refs and reading limits. `references.bib` now includes every requested work, even unread Roby1965, Walsh--Lehman1972 and King1985. Verona was read only in official primary previews (pp2--3 and37--38), Stanley only in author chapter extracts, MacPherson--Vilonen only pp403--405. No unopened theorem supplies a proof. Saavedra and Roby1963 were successfully downloaded despite browser size limits. The original Deligne--Milne Theorem2.11 is p130, and Tall--Wraith Definition3.1 pp626--627 explicitly requires biring compatibility.

## 2026-11-19 14:37 UTC: full one-dimensional fraction-field classification

B.044 proves completion commutes with integer-valued polynomials in every number of variables, using finite degreewise evaluation tests. B.045 constructs a nonzero tensor kernel whenever the generic algebra of the completion has a nilpotent, including mixed characteristic. B.046 therefore completes the fraction-field-coefficient classification for all one-dimensional Noetherian domains, without finite normalization: each finite-residue local completion must be a domain, equivalently its normalization must be finite and local. All three were independently audited by root at14:36UTC. Arbitrary intermediate coefficient overrings in the nonfinite-normalization class remain outside this theorem; work on that gate continues.
