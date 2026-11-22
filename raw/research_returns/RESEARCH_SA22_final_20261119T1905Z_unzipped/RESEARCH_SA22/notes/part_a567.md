# Part A.5–A.7: proof record, source audit, and exact limits

AI-produced by GPT-6 Astra (OpenAI), agent part_a567, in this run of 19 November 2026. No priority or novelty claim is made. The complete proofs are in the three LaTeX fragments, included by sections/part_a567.tex. Every numbered statement is indexed in checks/part_a567_results.csv, with its dependencies and manuscript pages. This file records the arguments and their limits, rather than claiming that the whole assignment is finished.

## Current status and scope

**A.5 and A.7 have complete proofs.** A.6 has complete corrected presentation calculations, literal counterexamples to 048 NB and 049(b), and a framed-logarithmic reconstruction theorem answering a precise interpretation of 049(a). That theorem is submitted to the parent for an independent check, especially the vertex normalizer and normal-frame compatibility. Its hypotheses and the reason for them are explicit. It is not a theorem about ordinary étale fundamental groups.

**049(c) now has a constructive answer with explicit limits.** A tangential log compactification is a smooth proper SNC pair together with its strata, normal-torus diagrams and tangential fibre functors. Temkin2018 Theorem1.1.15 proves existence in every dimension for smooth separated finite-type characteristic-zero varieties. Hoshi2006/2009 Corollary3.9 and log purity PropositionA.10 give a finite-cover-category specialization theorem over k[[t]], compatible with the log base and with the section fixed by a normal frame. A full proof also shows that log-canonically ample smooth SNC compactifications are determined by their interior; on any stated Isom-anabelian class this reconstructs the pair from arithmetic pi1. The earlier boundary-blowup counterexample explains why arbitrary models cannot be reconstructed without such a criterion. Universal existence of an *ample* smooth log compactification, or anabelianity of every stratum, is not proved or asserted. Those are stronger requirements than the sheet specifies; they must not be folded into the proved definition, existence and specialization statements.

The initial live notes, which predate the A.6 proof and original-image checks, are preserved as part_a567_initial_notes.md. They are superseded by this file.

## Exact supplied-input locations

The transcription root is inputs/RESEARCH_SA22_transcriptions/transcriptions/.

| File | Lines | Content used |
|---|---:|---|
| MPL_67_002-052_transcription.tex | 1046–1065 | 048: stable curve with normal propagator, outer arithmetic actions, marginal three-class NB |
| same | 1066–1081 | 049(a),(b),(c), including finitely generated field over Q in (b) and the compactification question |
| same | 1082–1101 | 050: pants/Lego/involution expectations and matrix presentations |
| same | 1102 onward, especially 1807–1886 | 051: handwritten upside-down group diagrams, partly erased modulo4 quotient, projective-line quotient and Birman sequence |
| MPL_67_053-101_transcription.tex | 1017–1068 | 084: octahedral construction |
| same | 1069–1101 | 085: faces and normalizer |
| same | 1102–1156 | 086: characteristic≠2 proposition and six-point formulation |
| same | 1157–1247 | 087–088: quotient/torsor construction |
| same | 1248–1277 | 089: groupoid theorem |
| same | 1278–1353 | 091: integral involution category and rank-one corollary |
| same | 1354–1467 | 092: intermediate integral algebra |
| same | 1468–1582 | 093–095: real lattice parameter and automorphism framework |
| same | 1583–1722 | 096: exceptional automorphism groups |
| same | 1723–1769 | 097: classification and tentative logarithmic j |
| same | 1770–1819 | 098: hexagonal ratio |
| same | 1820–1864 | 099: explicit period lattices |
| same | 1865–1935 | 100: count and struck unit-surjectivity proviso |
| same | 1936–end | 101: topology, torsors, H1, and struck “sans” |

The earlier study's global CORRECTIONS.tsv lines29–32 concern faces, characteristic5, and theorem089; lines33–38 concern the rank-one corollary, unit proviso, j, topology and dating. The parallel reading CORRECTIONS.tsv has the same relevant entries at lines15–24. These were read and each mathematical correction used here was independently proved. In particular the proposed connectedness repair at global line33 is **insufficient**, as the new domain counterexample shows.

## Original images checked

The parent downloaded the official cote67 PDF to sources/cote67.pdf. Physical PDF page numbers agree with the transcription scan numbers. The displayed PDF footer is one less; the manuscript archive pencil foliation is two greater in the inspected sheets. Thus use the scan number, not a guessed pencil page, to retrieve the image.

Rendered pages and high-resolution crops are under notes/original_scans_a567/. The images actually inspected are 048, 049, 051, 086, 089, 091, 100 and 101 (including crops). Sheet051's manuscript must be rotated180 degrees relative to its printed background.

- 048 explicitly says three conjugacy classes of homomorphisms from Zhat(1), with the “empty” class when there are no punctures. The literal wording is confirmed; a three-kind simple-loop interpretation remains an interpretation, not a claimed decipherment.
- 049 confirms the distinction between (a) extension of the conjecture, (b) invariant procyclic subgroups, and (c) a proposed general definition plus specialization.
- 051 clearly has +! in its first formula; the second superscript plausibly has a prime instead. We do not declare an author contradiction by forcing both to mean the pure group. The lower formula explicitly suggests a quotient of SL2(Z/4), supporting the consistent binary-dihedral reconstruction.
- 086 really excludes only characteristic2; the characteristic5 correction is necessary. The doubtful word transcribed as “réelle” does not enter the proof.
- 089 confirms that the groupoid theorem assumes characteristic unequal to2; the characteristic5 issue belongs to the unpaired six-point proposition, not this theorem.
- 091 has a general2-regular commutative base and a rank2 projective module, without a Dedekind hypothesis. Thus the stronger domain counterexample applies to the actual statement.
- 100 visibly strikes the unit-surjectivity proviso; the complete residue-unit orbit calculation shows when it is necessary.
- 101 visibly strikes “sans”; the fixed-point-free torsor quotient is a Klein bottle without boundary, as independently proved.

## A.5: proof and characteristic audit

Put V={z,−z,1/z,−1/z} over an algebraically closed field of characteristic unequal to2. Every Klein four subgroup of PGL2 is conjugate to this one: diagonalize one involution; a commuting distinct involution exchanges its two fixed points and can be scaled to inversion. Its centralizer is V. Its normalizer maps into Aut(V)=S3, and explicit transformations realize the required permutations, giving order24. Its action on the four antipodal face pairs is faithful and gives S4. The three double transpositions of an abstract S4-subgroup form its characteristic normal Klein group, proving the reverse correspondence even in characteristic5.

The six fixed points are S={0,∞,±1,±i}. Delete an antipodal pair: the remaining quartet is harmonic. Delete a nonantipodal pair: the crossratio is ±i up to the anharmonic orbit. Such a quartet is harmonic precisely when ±i equals one of −1,2,1/2. Squaring shows the only odd exceptional characteristic is5. Hence outside2,5 the unpaired set intrinsically recovers the antipodal pairing and V, and its full projective stabilizer is the normalizer24. In characteristic5 the set is P1(F5). Any projective automorphism preserving it is defined overF5, because its values at0,1,∞ are rational; consequently its stabilizer is PGL2(F5), order120. The S4 normalizers form an index5 family, giving five distinct Klein groups with the same six fixed points. Keeping the antipodal pairing repairs the six-point formulation in every characteristic unequal to2.

An individual face has C3 stabilizer. A face together with its antipode has S3 stabilizer, a complement to V. This proves the earlier wording correction.

For089, the Klein quotient has the explicit invariant (z²+1)²/(4z²), with branch values0,1,∞. For any four-set I, its three pair partitions J(I) determine V(I); the quotient line with its three branch points is canonical. A four-point embedding gives an unramified quotient fibre over a point ζ outside the branch triple. Conversely use the V-torsor Isom_V(P,I), where P is the corresponding standard fibre, and contract the standard octahedral line by this torsor. Evaluation gives the embedded four-set. The two constructions are inverse on objects and morphisms, including their automorphism groups. Nothing here uses the failed characteristic5 unpaired-six-set statement.

For L7 the family object is [U/S4], U=P1 minus0,1,∞, over Z[1/2,i]. The action factors through S3, so the generic kernel V4 remains as stack inertia. The coarse invariant is J=(λ²−λ+1)³/[λ²(λ−1)²]. The proof checks the invariant ring integrally and treats characteristic3 rather than dividing by6. The coarse space is A1_J; it is not equivalent to the stack as a groupoid. The field-level089 theorem is not silently promoted to a family equivalence without descent; the torsor construction supplies descent.

## A.6: framed-log reconstruction proof chain

**Typing.** A propagator is a nonzero tensor q_e in the product of the two tangent lines at each node. In local coordinates it is c_e∂x⊗∂y. Use the standard log smoothing xy=c_e t with the log-base generator t fixed, or equivalently the normal-torus tangential point with coordinates c_e. The corresponding geometric admissible group is the profinite smooth surface group with its G_K outer action. Ordinary étale pi1(Y minus markings) omits this data: the labelled two-component nodal0,4 curve with q=1 and q=2 gives a counterexample. Each component has identity automorphism because0,1,∞ are fixed. Its ordinary geometric group is Fhat2; the admissible group is Fhat3.

Hoshi–Matsumoto–Nakayama (2026), Proposition1, constructs the tangential map using a pro-Kummer log chart. Proposition2 and Remark1 identify changes by units equal to1 along the stratum, and show dependence only on the normal cotangent basis. This is an exact source for the first-order dependence used here. Rescaling t by a changes the coefficients by1/a and changes the arithmetic section by κ(a); forgetting that section weakens the data. The theorem is conditional on the fixed-frame interpretation, not on an unframed isomorphism category.

**Kummer separation.** For K finitely generated overQ, the kernel of K×→H1(G_K,Zhat(1)) is the intersection of all power subgroups. A normal projective model over the constant number fieldF shows any infinitely divisible element has all divisorial valuations zero, hence lies inF×. Its roots inK are algebraic overF and therefore lie inF; all finite-prime valuations vanish, so the element is infinitely divisible in the finitely generated unit group. It is1. Each l-adic cyclotomic image is open, so the invariants of Z_l(1), and then Zhat(1), vanish.

**Graph recovery.** Mochizuki2007 Corollary2.7(ii) applies once l-graphical fullness is established. On every characteristic finite admissible cover, the component quotient Mvert/Medge is the sum of Tate modules of normalization Jacobians. Descend its finite data to a finite field extension ofK and spread over an integral finite-type scheme over Z[1/l] with abelian-scheme Jacobians. A closed point has finite residue field. Weil's theorem (MilneAV II1.1(b)) gives absolute Frobenius eigenvalues q^(1/2). Any Q-cyclotomic constituent satisfying ψ^b=χ^a therefore has associated weight2a/b=1. Thus every associated weight lies strictly between0 and2, on every cover. The cited theorem recovers vertices, edges, cusps and incidence from the arithmetic action.

**Twist kernel and tensors.** Hoshi–Mochizuki2012 Theorem4.8(iv) and Proposition4.10(ii), summarized as TheoremB, identify the kernel of the restrictions to the graph and component anabelioids with the product of one Zhat(1) per node. This includes loops and selfnodes. Lemma5.4(i),(ii) and Theorem5.7 identify normal-deformation Kummer inertia with those Dehn twists. For tangential points c,c', compatible roots r_m^m=c'/c yield the transport cocycle γ(r_m)/r_m. A different transport changes this by a coboundary; coordinate changes cancel in c'/c. Higher units equal to1 do not change the first-order tangential functor by the2026 result.

**Full faithfulness.** Recover the graph, pass to finiteL/K splitting branches, and take normalizers of vertex groups to obtain the arithmetic groups of smooth hyperbolic normalization components. Mochizuki1999 TheoremA=16.5 reconstructs each component, since L is sub-p-adic. Extend to compact normalizations, glue the matched punctures, and descend by uniqueness. Pulling back the target tensor, the remaining compatible outer isomorphism is a twist. Its compatibility says the Kummer classes of every tensor ratio are coboundaries, so separation makes all ratios1. The remaining ambiguity is a G_L-invariant twist, which vanishes. This gives the stated bijection of isomorphisms. The parent is independently reviewing these steps; no review is claimed before it is received.

**049(b) and NB048.** For a rational cusp its inertia I≅Zhat(1) has invariant conjugacy class and cyclotomic action. Every subgroup mI does too. Their abelianized images mZhat e1 distinguish them, so there are infinitely many rather than finitely many marked points/nodes. The corrected positive result is full graphical recovery, not an unproved criterion for arbitrary maximal invariant procyclic subgroups. Likewise, powers of a primitive geometric generator yield infinitely many conjugacy classes of injective maps Zhat(1)→Δ. The three geometric kinds of simple loops are peripheral, separating and nonseparating. Separating mapping-class orbits require the genus and puncture counts of both sides (and subsets when labelled), not merely the word “separating.”

## A.6: 049(c), existence, specialization and canonical recovery

**Obstruction and definition.** For U=(P1 minus0,1,∞)², P1×P1 has six boundary components; blow up the crossing(0,0) to get seven. The open U and its arithmetic pi1 are identical. Therefore no bare-group rule can recover every chosen SNC compactification. This does not refute a definition. Our definition retains a proper smooth SNC pair (X,D), its strata S_J and the product over S_J of the nonzero normal-line bundles for the branches through that stratum. Normal-torus points give tangential fibre functors through compatible Kummer roots, independent of higher units with residue1. This is a concrete category with stated extra data, not an unsupported uniqueness claim.

**Existence, no dimension bound.** Temkin2018 Theorem1.1.15 applies to S=Spec(k), Y=Y0=U and empty initial boundary. It produces a regular proper compactification with strict normal-crossings complement. Over characteristic zero the base is perfect, so regular finite-type is smooth. This gives an object for every smooth separated finite-type characteristic-zero variety, without a quasi-projectivity restriction. No positivity is imported into this theorem.

**Arithmetic specialization, no dimension bound.** Let R=k[[t]], F=k((t)), Slog the divisorial trait, and Xlog proper log-regular over it, with generic interior U geometrically connected over F. Hoshi's July2006 RIMS1558 preprint Corollary3.9 (printed pp31–32, later published2009) identifies finite Kummer-etale covers of Xlog with those of the strict special log fibre X0log. Its PropositionA.10 (pp57–58) identifies the former with tame covers of U; all residue characteristics are zero, so all finite etale covers are tame. Applying the same facts to the base gives a compatible isomorphism pi1ket(X0log)≅pi1et(U) over pi1ket(slog)≅G_F. The chart t fixes a splitting G_k→Zhat(1)⋊G_k. Pull back along it: the kernel is pi1et(U over Fbar) by the ordinary arithmetic exact sequence of U. This is a full finite-cover theorem, not an invalid inference from cohomological base change. If t′=at, its root-fixing section differs by inverse κ(a) relative to t; units1+tR have unique roots of residue1, so only first-order framing matters. Ordinary pi1(X0) is not substituted for the log group.

**Geometric specialization.** Nakayama–Ogus2010 Theorem5.1 (published p2226) gives a topological fibre bundle for proper separated exact relatively smooth log-analytic maps with fine base and relatively coherent source. Its Kato–Nakayama fibre over a limiting boundary angle transports to the nearby smooth fibre; path transport gives outer pi1 isomorphisms. The angle/log structure is retained. We do not deduce full nonabelian comparison from Illusie's cohomological theorems.

**Canonical recovery.** For a smooth proper SNC pair, form Rlog(U)=⊕H0(X,ω_X(D)^m). AKMW2002 Theorem0.3.1(6) factors birational maps isomorphic on U into smooth-centre blowups/downs outside U, with centres normal crossing with the boundary, over arbitrary characteristic-zero fields. In a blowup of codimension c centre contained in r boundary branches, K_X1+D1=f*(K_X+D)+(c−r)E, with c≥r. For q≥0, f_*O(qE)=O because a function regular away from the codimension≥2 centre extends by normality; projection formula proves equality of all graded pieces under rational-form identification. Hence Rlog is intrinsic and functorial. If ω_X(D) is ample, X=Proj Rlog(U); an interior isomorphism extends uniquely, preserving D. Thus an Isom-anabelian theorem for U yields one for these pairs. Strata and normal-torus/fibre-functor diagrams are then recovered as functorial geometry of the pair. No assertion is made that bare pi1 selects an arbitrary individual normal vector.

**Concrete anabelian inputs.** Published Hoshi2014 Corollary3.18 gives the Isom theorem for hyperbolic orbi-polycurves over sub-p-adic fields if either dimension is at most4; ordinary polycurves are included. Carlson2026 preprint TheoremA=3.11 removes the dimension bound for ordinary hyperbolic polycurves. Its exact theorem and final proof were opened. We explicitly retain its preprint status (submitted27April2026, current HTML manuscript dated24August2026). The canonical-compactification theorem is conditional on an explicitly stated Isom-anabelian class and does not depend on adopting this recent preprint.

**Exact remaining limits.** The literal sheet asks for a definition and specialization; the three numbered results supply these, with existence. A stronger requirement that *every* smooth anabelian variety have a smooth compactification with ample log canonical bundle has not been proved here. Neither arbitrary compactification uniqueness nor anabelianity of all strata follows. The blowup example distinguishes these stronger assertions from the results actually established. Parent cross-review of the new theorems was requested at approximately12:02UTC.

## A.6: presentations, with category corrections

The central quotient of the SL2 presentation is C2*C3. Its central element z=σ²=ρ³ has order at most2 and maps to−I, proving the presented group is exactlySL2(Z). The three explicit reflection matrices reduce the GL2 presentation to SL2⋊C2, with the involution invertingσ andρ. The exact program checks every displayed matrix relation; the completeness proof is algebraic.

The pure four-punctured sphere group is Γ(2)/±I≅F2. The full group is V4⋊PSL2(Z), from the double cover of the sphere by a torus. The subgroup fixing one puncture is PSL2(Z). The affine action on F2² gives the exactS4/S3 diagram. The possible prime reading of the second superscript on051 is therefore mathematically coherent.

For the erased lift, the displayed order4 normal subgroup W of SL2(Z/4) avoids−I and complements the center in the reduction-mod2 kernel. Its inverse image inSL2(Z) is F2. The quotient has order12, with relations R6=1, S2=R3, SRS^−1=R^−1: it is the binary dihedral groupDic3. All256 matrices mod4 were scanned;48 have determinant1, W is normal, and all12 normal forms are distinct. This is a consistent reconstruction, not a claim that erased ink has been read.

The projective-line calculation on051 is also checked: primitive integral pairs modulo sign identify SL2(Z)/B_infinity with P1(Z) and P1(Q), and reduction to P1(F2) is surjective. This is an equality of point sets, not an isomorphism with the projective-line scheme. Nearby peripheral relations require opposite boundary orientations on the two pants.

The Birman sequence requires the added puncture to be fixed and the base surface to have negative Euler characteristic. The closed torus and twice-punctured sphere show why the left injection fails in low complexity. Boundary circles fixed pointwise and punctures require different conventions.

Bakalov–Kirillov Theorems4.24/5.1 give a connected simply connected complex of marked pants/Lego moves. Its path groupoid has trivial vertex automorphism groups: it must **not** be identified directly with the mapping class group. Their Remark4.3 warns of this distinction. The corrected derivation retains the mapping-class action, takes the action groupoid and keeps stabilizers. Pairs (g,path M→gM) recover g uniquely; simple connectivity supplies the relation completeness. Stukow3.1 proves that three orientation-reversing involutions generate the closed extended genus≥1 group. Finite presentability plus Tietze transformations gives a finite presentation on those generators, but Stukow is not falsely credited with an explicit complete relation list. No numerical three-generator claim is made for arbitrary puncture/boundary conventions.

## A.7: complete proof record

For a2-torsion-free module with involution, its eigenspaces P,Q satisfy2M⊂P⊕Q⊂M. The image m=2M/(2P⊕2Q) in(P/2P)⊕(Q/2Q) intersects either axis trivially. Conversely take the half-lattice of(p/2,q/2) whose residues belong tom; the sign involution has eigenspaces exactlyP,Q. Maps extend uniquely. This proves the full categorical equivalence without finite generation.

The rank-one corollary fails even over the domain R=Z[x,y,z]/(x²+yz−1), with σ=[[x,y],[z,−x]]. In the polynomial ring, (σ−1)(σ+1)=fI. Cancellation of f proves ker(σ−1)=im(σ+1), and hence P≅coker(σ−1). At m=(2,x−1,y,z), its residue fibre has dimension2 while its generic rank is1. It is not invertible. Over a Dedekind domain finite torsion-free eigenspaces are projective; over a connected base with2 invertible they are images of complementary idempotents. These are sufficient corrected hypotheses.

Over aPID with residue fieldκ=R/2R, the gluing module is zero or the graph of a nonzero scalar between two lines. Unit changes divide out by im(R×), giving one split class and κ×/im(R×) nonsplit classes. For Z the total is2. For Z[(1+√−11)/2], the norm m²+mn+3n² and rounding give Euclidean bound15/16, so it is aPID. Its units are±1, its residue field isF4 and the unit image is trivial, giving three nonsplit classes and four total.

Complex uniformization (MilneEC III3.10 and3.3) reduces real elliptic curves to conjugation-stable lattices. Applying the integral involution theorem overZ gives either Zu⊕Zv or the index2 enlargement by(u+v)/2. Normalizeu=1 andv=i√a. This gives the two real families E_a and E'_a, a>0. Real isomorphisms are real scalars, preserving the type and squared-length ratio, proving uniqueness. Real automorphisms are±1.

On a fixed complex lattice its linear automorphism group has order2,4,or6. If j is real, an anti-linear lattice isomorphism exists, has modulus1 and squares to1. The resulting dihedral reflection set has exactly two conjugacy classes. Replacingσ by−σ gives a↔1/a except in the square case, where the pair is E_1,E'_1. The hexagonal pair is E'_3,E'_(1/3). The quadratic form matrix[[1,1/2],[1/2,1]] gives ratio3, not√3. The reciprocity j(a)=j(1/a), and j at the square point1728, refute the logarithm guess.

Fixed-point equations give two circles forE_a and one forE'_a. The exact sequence0→Λ→C→E(C)→0 and averaging give H1(R,E)=Λ^σ/(1+σ)Λ. It isZ/2 in the split case and0 in the nonsplit case. The nontrivial split cocycle is z↦bar(z)+1/2; its fixed-point equation has impossible real part. Its quotient is a closed nonorientable Euler-characteristic0 surface, hence a Klein bottle. Standard reflection quotients are the annulus and Möbius band. MilneEC IV7.8 classifies torsors byH1, and IV7.19 makes every genus-one curve a torsor under its Jacobian. Thus the list is exhaustive and restores “sans bord” on101.

Alling1981's opened preface and0.10 state the three species and positive real parameters, matching this conclusion. The full1971 Alling–Greenleaf book was not opened; no unseen formulas are attributed to it.

## Source access, locators and search evidence

All bibliography entries in sources/part_a567.bib state the exact open status and locator. Local full PDFs/text include Mochizuki1996/1999/2006/2007, Hoshi–Mochizuki2011, Farb–Margalit, Bakalov–Kirillov and Stukow. The2012 twist paper, Milne books/notes and2026 tangential note were opened in full through the web PDF interface. Nakamura1990's header alone was retrieved and Ihara–Nakamura1997's author bibliographic entry alone was verified; their mathematical texts were not opened despite several routes and they are not proof inputs.

Useful primary-source web references, for the parent to reopen before final-chat citation:

- Hoshi–Mochizuki2012: turn648876089view0; exactTheorem5.7 turn691529854view0 andLemma5.4 turn691529854view1.
- Mochizuki1999: turn229799813view2 and earlier exactTheoremA turn384763552view1.
- Mochizuki2007: turn506144128view2.
- Hoshi–Matsumoto–Nakayama2026: turn813725709view0, https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1995.pdf.
- Mochizuki2020 comments: turn229799813view0, https://www.kurims.kyoto-u.ac.jp/~motizuki/Semi-graphs%20of%20Anabelioids%20(comments).pdf.
- Hoshi author bibliography, publication metadata: turn788355284view1.
- MilneEC exact torsor statements: turn331150099view3.
- MilneAV Weil theorem: turn691529854view2.
- Farb–Margalit Birman: turn331150099view0; sphere group: turn693367753view2.
- Stukow full paper: turn515922793view2.
- Alling preview: turn506144128view3.

At11:48UTC the primary web search queries were “Grothendieck ‘Chirurgie des surfaces conformes’ étude publication”, “Grothendieck ‘cote67’ ‘cote68’ étude”, and “Grothendieck ‘Courbes elliptiques réelles’ octaèdre”. Results included the official Montpellier inventory (turn194846871search0) and unrelated works; no dedicated published study was identified by these searches. This does not prove none exists and supports no priority claim. The parent conducts the broader literature search.

## Computation and independent checks

The exact program code/part_a567_checks.py and its output cover24 odd primes3..97,120 triple images each, the characteristic2 collapse, matrix relations, all256 modulo4 matrix candidates, the universal-domain involution, the residue-unit count, and the hexagonal form. Final output says all assertions passed, with elapsed0.236781seconds for the recorded run. The initial wrong reflection selection and a separate unsimplified SymPy equality failure are retained in the initial/second scripts and their outputs; no mathematical claim relied on those failed checks.

Independent targeted checks sent to the parent: its A.1 Koebe bound |q|≤16 on the labelled nodal0,4 normalization is coordinate-consistent and refutes an unrestricted q=17 target. Its Schwarzian cap second-jet coefficient b=(a0+a1−a∞)/(2a0) is algebraically consistent. These are targeted checks, not a claim to have independently reproved every part of the parent argument.

The clock tool, not filesystem modification-time display, is authoritative for global review timing. This consolidation was saved near the parent's first checkpoint; dates of earlier source readings are recorded, but precise times are not fabricated.


## Sources opened during the 049(c) expansion

- Hoshi2006 RIMS1558, https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1558.pdf: exact Corollary3.9 turn504298884view0; exact PropositionA.10 turn504298884view1. Published2009 metadata recorded, preprint numbering stated explicitly.
- Nakayama–Ogus2010 published PDF, https://msp.org/gt/2010/14-4/gt-v14-n4-p09-p.pdf: exact Theorem5.1 turn739999003view1.
- AKMW primary arXiv PDF, https://arxiv.org/pdf/math/9904135: exact Theorem0.3.1(6) turn504298884view2.
- Temkin author PDF, https://math.huji.ac.il/~temkin/papers/Embedded_Desingularization.pdf: exact compactification Theorem1.1.15 turn528015954view0; published2018 bibliographic metadata verified. This single theorem supplies existence directly.
- Hoshi2014 published PDF, https://www.ms.u-tokyo.ac.jp/journal/pdf/jms210201.pdf: exact Corollary3.18 turn528015954view1.
- Carlson2026 preprint HTML, https://arxiv.org/html/2604.24898v1: TheoremA turn307735358view0, Theorem3.11 turn845257903view2, final proof turn504298884view3.
- Illusie2002 overview and Talpo2026 log-homotopy-exact-sequence preprint were also opened during approach testing. Illusie's cohomology comparison alone is insufficient for the nonabelian assertion; Talpo's newer homotopy exact theorem is unnecessary once Hoshi's finite-cover equivalence is applied. Neither is used as a proof input in the final specialization theorem.

The accent-macro brace pass requested for unicode-math was completed in A5–A7 at11:59UTC (26 replacements in A6 and10 in A7); this was a typesetting edit only.


## Final source audit and cross-review, 19 November 2026 after 12:17 UTC

### A6(a) hypotheses and normal-torus globalization

The precise distinction in Mochizuki2007 Definition2.3 is now corrected:
Q-cyclotomic means a positive power equals an integral power of chi
on an open subgroup; quasi-cyclotomic means equality with chi on an
open subgroup. The associated-weight argument uses Q-cyclotomic.

Mochizuki2007 Proposition1.2(ii) makes each vertex group
commensurably terminal, hence self-normalizing in the geometric group.
After splitting the graph over L, the arithmetic normalizer surjects
onto G_L and has that geometric vertex group as kernel. Its induced
outer action is the actual action on the punctured normalization.
Centre-freeness identifies the extension with the pullback
Aut(Delta_v) x_Out(Delta_v) G_L. Mochizuki1999 TheoremA explicitly
includes the full profinite arithmetic assertion, so it is not being
extrapolated from its geometrically pro-p clause.

The full2012 paper was converted to local text and re-read at
Definition4.4, Proposition4.5, Theorem4.8(iv),(v), Proposition4.10(ii),
Lemma5.4 and Theorem5.7. The twist kernel statements allow arbitrary
semi-graphs, including loops. The geometric monodromy theorem is used
over Kbar[[t]], with separably closed residue field of characteristic0,
so all primes are allowed. Galois equivariance follows from the
functorial synchronization and its node-wise uniqueness.

The normal-torus functor is now explicitly globalized. On T_J the
tautological normal vectors v_j give units a_j=dx_j(v_j). Local charts
x_j/a_j agree because changing x_j to u_j*x_j changes a_j to
(u_j restricted to S_J)*a_j. Thus the pullback logarithmic structure
has a global N^J chart, and its pro-Kummer roots define the desired
finite-cover functor. The overlap rule also gives Galois descent when
branches are permuted. Composition for nested strata is the canonical
homotopy of Hoshi--Matsumoto--Nakayama2026 Proposition3.
Their Proposition2 and Remark1 give exactly the first-order chart
dependence. Fresh opened ref: turn131690314view0.

The parent reports independently reading HoshiRIMS1558 Cor3.9 and
PropA.10, Temkin1.1.15, and the log-ring weak-factorization derivation,
and agreeing with their stated applications. Earlier paragraphs and
events recording a requested review are historical, not current gates.

### Historical L6 sources recovered

The original1990 and1997 texts retain their honest not-opened status.
Three further primary sources were opened:

- Nakamura1994 full published PDF:
  https://www.ms.u-tokyo.ac.jp/journal/pdf/jms010103.pdf .
  Section2.1, Theorem(2.1.1), Lemmas(2.1.2),(2.1.4), pp93--97.
  Fresh refs turn807807931view2 and turn393176829view0.
  It gives an exact cyclotomic-normalizer test for membership in the
  union of cusp inertia groups of a smooth affine hyperbolic curve
  over a number field. The new numbered proposition
  A6-cyclotomic-detection states the full-profinite specialization and
  derives it using the all-cover mod-l detection lemma and Weil weights.
  It is not silently applied to the limiting action of a singular log curve.
- Nakamura--Tamagawa--Mochizuki2001, the authors' own survey, Section2.4,
  author-PDF pp7--8, fresh ref turn484472058view1. It attributes the
  genus-zero arithmetic reconstruction over fields finitely generated
  over Q to Nakamura1990 and explains inertia plus Kummer cross-ratios.
  This is an opened retrospective account, not an opened1990 proof.
- Ihara--Nakamura1995, RIMS Kokyuroku925,129--133:
  https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/0925-16.pdf .
  Fresh ref turn484472058view0. Sections1.2--1.4 reproduce the English
  deformation-paper introduction, with exact Theorem2-prime and
  Theorems3A--3B. The additional tangential structure and node ordering
  are essential to its formal coordinates and Galois-groupoid comparison.
  This supports L6's historical connection without importing an
  unavailable proof or confusing Oda's constant-field assertion with
  complete stable-log reconstruction.

### Independent analytic re-proof requested by the parent

I read part_a2b_secondary.tex, part_a2_limits.tex and part_a1_range.tex
in full, independently of their author's review, and found no
substantive gap in the stated unbordered/fixed-compactification claims.
The checks were as follows.

1. In the seam coordinate zeta=x+iy, log|w|=-y/lambda. Its variation
   gives h=c-V_y and seam normal velocity V. Differentiating continuity
   of the first spatial derivatives, with second derivatives1 on the
   core and0 on the cylinder, gives h_y(flat)-h_y(core)=V.
   The Green identities have the stated signs; their sum is
   pi*sum(dot s_i dot F_i)=E_h+E_V. Using V_b and h_a in the two
   boundary identities proves the full bilinear symmetry, not merely
   positivity of a quadratic form. Zero energy forces h=0 on the
   nonempty core and then c_i=0 by bounded harmonic uniqueness.
2. Collars extend the inverse cap map to radius exp(a_i/lambda_i);
   rescaling its source disc gives the precise stated bound on its
   first coefficient. This is uniform in all other boundary lengths.
   The cusp decay gives zero truncated Green boundary terms.
3. The area comparison projects cylinder excursions nonexpansively
   onto the core, so every peripheral test circle has length at least
   L_i. Cauchy--Schwarz and the relation
   w_i=(r_i(E_i)/r_i(s))*zeta_i+O(zeta_i^2) give the signs and
   constant2g-2+n in the renormalized-area deficit.
4. Zero-weight faces are valid: choose Solynin's B to be the positive
   marked points, A the remaining marked points, all other systems
   empty, and only peripheral circle homotopy classes. I independently
   opened his Theorem2.1/(2.27), printedp32, and the definitions on
   p21. The strict uniqueness clause is explicit. Poles at A have
   order at most1 and may disappear upon collision with a zero.
   The sole edit to the author's A2b file clarifies this last phrase.
   Source refs turn142272209view0, turn465666776view0/1:
   https://www.mathnet.ru/php/getFT.phtml?jrnid=aa&option_lang=eng&paperid=1040&what=fullt .
5. On a boundary ray p>=0, the derivative upper bounds imply
   S(s0+tp)>=S(s0+t(p+epsilon*1))-t*epsilon*sum b_i.
   The support supremum proves K(p+epsilon*1)->K(p), including when
   the b_i or their sum are negative. This closes the recession step.
6. An unbounded sublevel sequence gives a normalized nonnegative
   direction p; convex segment comparison contradicts the positive
   recession slope. The closed convex extension is bounded below by
   an affine support. Along b+t*1, lower semicontinuity and convexity
   give convergence to its finite boundary value, while the uniform
   collar bound makes the inward derivative tend to minus infinity.
   Thus the minimizer is interior. The positive Hessian supplies the
   real-analytic inverse and the support inequalities describe exactly
   the logarithmic radius image.
7. In the cap-limit argument, zero-weight summands are removed using
   their upper bounds, not an unjustified lower bound. Positive
   coefficients and all other upper bounds then give a lower bound for
   each positive-weight radius. Normal families give nonconstant
   disjoint kernel limits. Strebel uniqueness identifies them, and an
   additional positive-radius zero-weight disc would be an open subset
   of the critical graph, impossible.
8. The graph Hessian sum A_v^T Hess(S_v) A_v counts both branches of
   a loop and is positive definite because every nonzero edge vector
   has a nonzero incidence image. The same coercivity and collar
   proof applies. The actual seam phases supply the full S1 variables;
   fully marked real twists require the explicitly stated quotient.
   Common length1 gives intrinsic shadow circles. Radial contraction
   to this circle bundle stays in the log-convex image, is equivariant,
   and is a common deformation retraction of the image and the full
   nonzero-tensor bundle. Thus the orbifold pi1 claim is justified.

For analytic dependence I independently inspected Mondello's actual
source sources/mondello/Triang-submitted.tex, lines3535--3541
(thm:grafting), which states a real-analytic diffeomorphism on every
finite topological stratum. Its setup explicitly permits cusp ends
(lines3494--3508; reduction at4074--4088). Smooth complex seam charts
and the normalized Beltrami parameter theorem supply the needed
parameter smoothness; the metric's C1,1 regularity is not mistaken
for C2 smoothness across the interface.

### R4/R5 final completeness audit

Re-read the exact supplied transcriptions for084--089 and091--101.
No interpreted-condition gate remains for A5/A7. The ambiguous erased
word on086 does not affect the algebraically closed projective-line
statement, and the091 corollary is independently disproved under the
weaker visible hypotheses, so no decipherment is used to rescue it.
The091 category proposition has now been broadened to arbitrary
possibly noncommutative rings and left modules, exactly as its opening
line states; central localization at2 makes the existing proof valid.
The rank-one corollary is kept over the explicitly specified
commutative rings. The100 count now also displays all three nonsplit
matrices [[1,c],[0,-1]], c=1,omega,1+omega. The topology proof uses
chi(quotient)=(chi(torus)+chi(fixed circles))/2=0 and the boundary
count, so the annulus/Mobius classification is explicit.

L7's stack and coarse descriptions descend to Z[1/2]; i is only used
for the chosen octahedral matrix model. Generic V4 inertia, bad-prime3
invariant-ring issues, and the unrelated characteristic5 six-set
exception remain separated. No characteristic2 theorem is asserted.


## Independent review of later A1 additions

Read part_a1_plumbing.tex, part_a1_bordered.tex, part_a1_algebraicity.tex,
and part_a1_cut_choice.tex in full. No substantive gap was found in their
stated hypotheses. The exact Hinich witness was independently checked
by quotient differentiation with Fraction arithmetic, without reusing
the parent's SymPy or residue method: lambda(9/11)=323680/323761,
lambda-prime=0, lambda-double-prime=271040/371353867. Script and output:
code/part_a567_plumbing_review.py and .out.

The global-coordinate issue has a direct domain proof. Retain the first
piece |z|<9/(10|t|), so u=(11t/9)z has |u|<11/10. Its image is
phi(D_(11/10)); phi is injective there because the second possibility
for equal images is u+v=3. The second retained piece is the sphere
minus phi(closed D_((11/10)|t|)). Their common image is exactly the
annulus phi({(11/10)|t|<|u|<11/10}), which is the plumbing overlap
since x=tz/(9/10). Hence the images cover the sphere and identify
exactly the required overlap, proving global bijectivity. All marked
points remain distinct for every 0<|t|<1. Hinich's actual arXivv2
was opened independently, https://arxiv.org/pdf/math/0606240 ,
ref turn185981208view0. Its equations5--9 match the rational constants.
Its p4 paragraph does reverse the inside/outside cap assignments;
the explicit two-sphere construction avoids relying on that wording.
The parent was sent the complete domain argument and the exact output.

The retained-germ welding/plumbing identity and the annular metric
formula were re-derived. Extending cap coordinates across analytic
seams supplies the annular identification uv=c; changing x=au,y=bv
gives t=abc and exactly the same tensor. The complete annulus core
length is2*pi^2/(-log|t|), with the stated cusp limit. I did not claim
a second independent reading of all Kra/Wolpert locators.

For the bordered obstruction, the existing two external cap second
jets b0=b1=1/2 are invariant under centred-disc rotation. After
forgetting the node cap, a cusp has a_infinity=1/2. The two equations
force a0'=a1'=1/2, contradicting positive external boundary lengths,
even though these new lengths were allowed to vary. The repaired
edge-plus-leg potential correctly uses each leg once and each edge
branch twice. Its Hessian and closed-orthant minimization are the same
valid argument already independently checked above. Full external
disc shape recovery is precisely equality with the uniquely recovered
canonical cap embeddings; no false external-only admissibility is
smuggled into the criterion.

For cut-choice, the given H has no critical point on S1, and h is
injective there. Compactness upgrades this to a globally injective
sufficiently small annulus, as communicated to the parent. Thus the
analytic welding exists, but its nonconstant angular derivative
prevents a pointed-disc antiisomorphism. Geodesic representatives
restore the explicitly required toric compatibility.

For algebraicity, the pure four-pointed group is P Gamma(2); the
unoriented primitive cut-line stabilizer is exactly the cyclic
parabolic generated by T^2. The quotient H/<tau->tau+2> is the
punctured unit disc. A finite-type smooth algebraic curve with its
noncompact topology and pi1=Z would have2g+r=2, r>0, hence be C*.
The universal covers H and C differ, so the stated natural complex
cut-component cannot be such an algebraic curve. This does not
assert that every possible unrelated complex structure on its
underlying real surface is nonalgebraic, and does not infer
nonholomorphicity from real analyticity.


## Follow-up source access audit

The additional exact-DOI and institutional searches, INSPIRE records, failed original access, and actually opened Matsumoto2019/Earle-Sipe1991 originals are recorded in notes/part_a567_retrieval_followup.md. The original joint Earle-Marden2012 and Marden1987 theorem texts remain unavailable; the new direct Earle-Sipe plumbing equations are not relabelled as those missing sources.


## Explicit collar strengthening

At the parent's request, the rigorous all-large-n family was strengthened to fixed parameters n=10000 and epsilon=10^-14. The full independent supersolution proof is in sections/part_a567_collar_explicit.tex, label A2-collar-explicit. It uses the exact local mode exp(-ny)(n-tan(y)), a fixed quintic C2 cutoff between heights1/100 and1/50, H=2000-sum(eta*tan(y)), and U=epsilon*(2H+w/2). Every global residual, normal-derivative and graph-curvature bound is explicit. The certificate code/part_a567_collar_explicit.py and .out checks the symbolic identities and rational inequalities, not a numerical PDE solution. The old all-large-n result has not been weakened or edited. McMullen1994 Theorem2.18 and its proof were opened in full, refs turn538000997view0 and turn292953626view1. The parent has independently checked the full new proof and found no gap; a second independent check is in progress with the C researcher.


## Retained input IDs and two explicit qualifications

The exact supplied IDs are retained in checks/part_a567_input_id_map.csv and in21 new events under those same IDs. The safe-to-rerun mapping script is code/part_a567_legacy_ids.py. L6/L7/L9 each have their own result and event row. Date claims and unused palaeographic readings were not automatically marked checked.

For the input 67/087 six-point V-set claim: V preserves each two-point fixed set because it is abelian. A nonidentity element fixes its own pair pointwise. On either other pair it has no fixed point, since the three fixed sets are disjoint, so it interchanges that pair. Conversely, given three pairs and a bijection between those pairs and the three nonidentity elements of V, define each element to fix its own pair and swap the other two. The product of two distinct such permutations is the third. This verifies the action, its faithfulness and the claimed reconstruction directly. It is the antipodal-pair combinatorics used in A5-normalizer and A5-groupoid.

The exact input ID SA22-8 (67/089, Theorem) correctly asserts the groupoid equivalence, but its exceptional inertia counts8 and12 require characteristic unequal to3. In characteristic3 the harmonic and equianharmonic values all equal lambda=-1. All six anharmonic maps fix it, so its full inertia is S4 of order24. This qualification is now proved explicitly after A5-moduli; the finite enumeration code/part_a567_char3_inertia.py and its output verifies24 projective transformations of P1(F3), and all six values. This does not alter the all-characteristic groupoid theorem.

For SA22-9 (67/093-101, the complete picture), the claimed real j-images are checked by the sign of the discriminant of y^2=x^3+Ax+B and its number of real roots. A=-3 with B^2 below or above4, and A=3 with arbitrary B, realize all values of the stated intervals. The proof is now written at the end of A7, rather than importing the earlier memory-based claim. The input rank-one-eigenspace corollary is already refuted even over an integral domain, so the earlier connectedness repair is explicitly superseded.

The fixed-parameter collar proposition A2-collar-explicit was independently checked by both the parent and the C researcher. The latter explicitly verified the exact ODE, curvature from Christoffels, every constant and sign, collar embedding, C2 comparison-function regularity, and the final bound, and reported no error. Its own independent event is recorded in the C researcher's audit file.

## Final exact-input correction audit and excluded characteristic 2

The 54-row `checks/part_a567_corrections.tsv` gives the five requested columns. Paths are workspace-relative to the actual extracted attachments under `inputs/`; the original prompt is under `upload/`. Line numbers are those of the attached input files, never those of our new TeX. All paths and line endpoints were checked. Rows distinguish a new correction from an independent verification, an interpreted positive replacement, or retained ink uncertainty. In particular event66 needs inertia24 in characteristic3; event68/CORRECTIONS33/PROMPT80 have an insufficient connectedness repair. The real j-range row is expressly an independent verification.

The active A5 fragment now explicitly treats characteristic2 as excluded: i=1, the six-set has three points, the displayed standard group has two elements. Faithful translations by F4 instead form V4 but have common unique fixed point infinity, so the geometric fixed-pair construction itself fails. The general proof is in the paragraph; `code/part_a567_char2_edge.py` and `.out` supply the new finite certificate (all16 products, all5 rational projective points), as requested for finite examples. This is a new edge-case check, not a repetition of the existing odd-prime or characteristic3 computations.

## Original Crelle sources recovered and mathematically read, 13:45 UTC

This supersedes every earlier not-opened or inaccessible status for Nakamura1990 and Ihara–Nakamura1997 in this chronological record. Both full original articles were downloaded through links explicitly advertised by the official GDZ IIIF manifests, without any access challenge.

- Nakamura1990: `https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0411/LOG_0014.pdf`, 1,450,241 bytes, local `sources/part_a567_nakamura1990_original.pdf`. Theorem(1.1) p205, Definition(3.3) p209, Theorem(3.4)/Corollary(3.5) p210, and Theorems(5.10)/(6.1) p215 were read. Critical p210 and p215 were visually checked. Theorem5.10 requires rational puncture sets of cardinality at least three over a field finitely generated over Q, and realizes the induced puncture bijection by a projective transformation. Theorem6.1 descends to arbitrary smooth hyperbolic genus-zero curves. These statements are not quoted as a full Isom-bijection theorem. The1990 cyclic criterion requires geometric self-normalization, open arithmetic-normalizer image and cyclotomic action; the stronger element criterion in our proof remains the opened1994 theorem.
- Ihara–Nakamura1997: `https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0487/LOG_0009.pdf`, 3,390,605 bytes, local `sources/part_a567_ihara_nakamura1997_original.pdf`. Sections2.1–2.4 define the smooth-component P1_01infinity diagrams, tangential structure and node numbering; equation(5_mu), p131, is TTprime=q_i(mu). Theorems1/1prime pp132–133 construct the proper formal deformation and its algebraization. These diagrams exclude selfnodes. Theorems2/2prime are actually in Section3.6 p146, though the introduction says3.5. They compare Galois kernels/actions using the chosen tangential groupoids and the one-parameter diagonal. Theorems3A–3B and Corollary4.2.2 p148 give the constant-field inclusion and pro-l equality for n>=1; that same page reports Takao's removal of n>=1. We do not convert that report into a proof supplied by this article. Critical pp131–133,146,148 were visually checked.

OCR utility `code/part_a567_ocr_sources.py` processed12 and27 original mathematical pages respectively, yielding28,616 and60,472 characters in41.446637 seconds. It is document access, not a mathematical test; formula glyphs were checked on original scans. Saved manifests and scans make the opened status reproducible. The active A6 historical comparison, bibliography and L6 result/event rows have been updated. The theorem proving fully faithful framed-log reconstruction still rests on its stronger explicitly opened modern inputs.
