"""Serialize individually read and reasoned supplementary records; no verdict inference."""
import csv,json
from pathlib import Path

OUT=Path('/workspace/scratch/594d1dc856a9/SA04_work/parts/b')
DATE='2026-11-19'
WHO='GPT-6 Astra Pro; effort inherited, not separately exposed; run SA04/notes_93_b'
P4='codex/K93-04_transcription.tex'
P5='codex/K93-05_transcription.tex'
P6='codex/K93-06_transcription.tex'
claims=[]
def claim(n,items,scans,lines,words,statement,page,computation,cl,fate,present,refs,confidence='high',date=None):
    claims.append(dict(id=f'C-SA04-{n}',items=items,cote='93',scans=scans,lines=lines,his_statement=words,statement=statement,status_on_pages=page,computation=computation,**{'class':cl},fate=fate,fate_date=date or 'The manuscript layer is undated. Checked edition/publication dates do not date these sheets; no first-circulation date is inferred.',present_status='As of 19 November 2026: '+present,refs=refs,confidence=confidence))

claim(698,['SA04-627'],[191],[P4+':332–334'],'équivalence; marge ?',
 'For flat finitely presented X/S with geometrically connected fibers, a section (or the stated finite radicial substitute), and the tentative locally noetherian base condition, the author proposes a relative representation equivalence. In the broader version a strict pro-étale group Π/S and pro-Π_X torsor P have fiberwise quotient maps from the enlarged fundamental groups, and coherent continuous Π-representations should recover the coherent relatively étale-trivial stratified objects whose geometric fibers factor through Π_s.',
 'open on the pages',
 'Ordinary descent constructs the associated stratified object from a representation. The source does not prove that the fiberwise quotient condition implies essential surjectivity over an arbitrary base. The ordinary profinite group is not substituted for the explicitly enlarged group.',
 'C',
 'The opened dos Santos2007 §2.4 Proposition13 (author-version pp13–14) gives a point-base finite-monodromy comparison under regularity and algebraic closedness. Lara2019 Theorem3.1 (printed p7) gives a related homotopy theorem for flat proper finitely presented maps with reduced connected geometric fibers over a connected Nagata base, using near exactness. Searches for relative stratified coherent representations, enlarged/pro-étale fundamental groups, and relative homotopy sequences did not locate the exact arbitrary-base fiberwise equivalence printed here. These are related theorems, not an exact match.',
 'The construction direction and restricted finite-monodromy cases are established. The exact broad relative equivalence remains an identification/formulation gap in this audit; neither a proof nor a counterexample to its complete quantifiers has been established. Modern Noohi pro-étale groups must not automatically be identified with the historical enlarged pro-group.',
 ['BDosSantos2007Supplement','BLara2019Supplement'],'medium')

claim(699,['SA04-628'],[192],[P4+':337–339'],'L tensor n trivial comme module stratifié',
 'For a given stratified invertible sheaf L on finite-type geometrically unibranch X/k, the proposed criterion is étale-local triviality iff L^n is trivial as a stratified sheaf for some n>0 prime to char(k). The sufficiency direction is asserted without geometric unibranchness. Torsion of the underlying ordinary line bundle alone is only a necessary condition, not the stated iff.',
 'proof sketched',
 'The forward direction in the standard smooth connected algebraically closed-field setting uses finite image of a continuous rank-one representation of a profinite group; a finite subgroup of k* has prime-to-p order. For the reverse direction, the roots of a horizontal trivialization of L^n form an étale μ_n-torsor, and its tautological root is horizontal. Over nonclosed fields, retain relative descent/group-scheme data rather than replacing it by the full arithmetic étale group.',
 'C',
 'Stacks Lemma59.65.2 (tag0GIY) verifies finite Galois trivialization of finite-type locally constant module sheaves on irreducible geometrically unibranch schemes. dos Santos2007 Proposition13 supplies the regular algebraically closed positive-characteristic comparison and explicitly warns on p14 against the same formula over a nonclosed field. These open texts and the independent Kummer proof settle the usual setting and sufficiency; an exact primary proof including every singular/arbitrary-field convention of the manuscript was not located.',
 'The given-object criterion is established in the standard smooth algebraically closed setting, and the Kummer sufficiency proof works in the stated generality once the relative stratification convention is fixed. The audit does not promote the weaker claim about existence of some stratification on a torsion ordinary line bundle into this exact criterion.',
 ['BDosSantos2007Supplement','BStacks0GIYSupplement'],'high for the standard case; medium for the unrestricted source convention')

claim(700,['SA04-661'],[189],[P4+':306–320'],'E qu coh.; a), b), c), d)',
 'The equivalence of étale/Zariski local pullback-triviality with curvature and p-curvature zero is false for arbitrary quasi-coherent E if localization means neighborhoods in X over the fixed base S, as the definition of triviality suggests.',
 'asserted without proof',
 'For S=Spec F_p and X=A1, E=O_X/(x^p) with the induced d has zero curvature and p-curvature and descends through relative Frobenius from O_Xprime/(u). It is nonzero torsion at the origin and cannot become a pullback of a vector space under an étale neighborhood. This is a written proof, not a textual comparison.',
 'C',
 'Opened Katz1970 Theorem5.1, printed pp190–191, gives the precise quasi-coherent Cartier equivalence, which is weaker than local freeness. dos Santos2007 introduction independently emphasizes failure of local freeness for positive-characteristic integrable connections. The counterexample refutes the literal local-triviality implication, while the descent part survives as C-SA04-701.',
 'False under the stated ordinary fixed-base interpretation; keep a reading qualification because the site of pairs (X→S) is not defined here. No ink-level emendation is certified.',
 ['BKatz1970Supplement','BDosSantos2007Supplement'])

claim(701,['SA04-661'],[189],[P4+':310–320'],'équivalence de catégories',
 'Under the smooth characteristic-p (or the stated local p-basis) hypothesis, relative Frobenius pullback with its canonical connection is an equivalence from quasi-coherent sheaves on Xprime to quasi-coherent integrable connections with zero p-curvature. Matching coherent categories may also be used under the usual noetherian finite-presentation assumptions; one cannot mix coherent source with all quasi-coherent target.',
 'asserted without proof',
 'Katz gives the horizontal-sections inverse and a local Taylor projector. A finite locally free descended module has local bases; their Frobenius pullbacks are horizontal frames. Local freeness is preserved and reflected by faithfully flat Frobenius, so the locally trivial bundle version is valid. An infinite direct sum of trivial objects also witnesses the source-category size mismatch if line320 is read literally.',
 'B',
 'Exact modern formulation opened in Katz1970 Theorem5.1, printed pp190–191, with smoothness, characteristic-p base, and both categories quasi-coherent. The author attributes the result to Cartier. The printed coherent/quasi-coherent mismatch is a separate possible transcription or formulation error.',
 'Established Cartier descent. C-SA04-700 preserves the distinct false extension to local triviality for all quasi-coherent objects.',
 ['BKatz1970Supplement'])

claim(702,['SA04-631'],[197,198],[P5+':99–106'],'se remonte ... via Verschiebung; ordre fini ?',
 'The scan198 e) criterion is false even when every reduction has a lift rational over its residue field: an integral finite-type base dominating Spec Z and an abelian scheme section need not be torsion merely because all closed reductions lift through Verschiebung.',
 'open on the pages',
 'Complete proof in root_supplement_proofs.md: S=Spec Z[1/30], E:y²=x³−2x, P=(2,2), discriminant512. For every p≥7 the rational two-torsion makes Np even; Hasse gives 0<Np<2p; thus p does not divide Np. VF=[p] and bijectivity of F on Fp-points give a rational V-lift for every point. Exact counts at3 and5 are4 and10, so good-reduction injectivity bounds rational torsion by2; P has y≠0 and infinite order. Saved program b_supplement_computations.py and output verify the finite calculations.',
 'C',
 'Primary ingredients opened: Milne2021 II§5 Cor5.7 p66 (torsion specialization), IV§9 Thm9.4 p150 (Hasse); Chai–Oort2009 §10.24 p531 (VF=FV=p). Searches on Verschiebung-divisible reductions did not locate this exact manuscript formulation as a published theorem; the counterexample resolves the literal statement independently. This supplements/refines root C-SA04-644, not a second manuscript occurrence.',
 'Refuted with all visible retained hypotheses, including the stronger rational-lift reading and every closed point of the base. This is not a counterexample to the full p-curvature conjecture or to scan197 c), which retains universal-vector-extension data. No novelty claim is made.',
 ['BMilne2021Supplement','BChaiOort2009Supplement'])

claim(703,['SA04-628'],[193],[P5+':5–7'],'seule ... structure habituelle',
 'Assuming the finite-monodromy rank-one criterion and that every global unit is horizontal for the canonical relative stratification, an étale-trivial stratification on O_X is the standard one. Consequently, forgetting stratification identifies étale-trivial stratified line classes with prime-to-characteristic torsion in Pic(X) in this setting; the source names proper separable X/k as an example.',
 'proof sketched',
 'Choose n prime to p and a horizontal trivializing section σ of (O_X,T)^n. Write 1^n=λσ. The horizontal-unit hypothesis makes 1^n horizontal; the infinitesimal stratification ratio for1 is an nth root of unity equal to1 on the diagonal, hence1 is horizontal. Existence for any prime-to-p torsion ordinary line is supplied by its μ_n-torsor; uniqueness follows by tensoring two structures and applying the result on O_X.',
 'E',
 'This is an elementary Kummer consequence of the precisely stated C-SA04-699, independently reconstructed here. Searches on finite-monodromy rank-one stratifications and the opened dos Santos finite-monodromy comparison corroborate the setting; no separate historical first appearance is established.',
 'Valid with the horizontal-unit and preceding finite-monodromy hypotheses. Properness is not replaced by an assertion that every flat line bundle is finite monodromy.',
 ['BDosSantos2007Supplement'])

claim(704,['SA04-662'],[194,195],[P5+':14–35'],'voisinage ouvert ... p-courbure ... nulle',
 'For an integral finite-type S dominating Spec Z, smooth finite-type X/S, and a vector bundle with flat relative connection, finite-étale triviality on the generic fiber implies zero p-curvature on every positive-characteristic fiber over some open neighborhood of the generic point.',
 'proof sketched',
 'Spread the finite étale trivializing cover and its horizontal trivialization to a nonempty open of S. Shrink once to retain finite étale surjectivity and the finitely presented connection identities. In each residue characteristic, the trivial connection has zero p-curvature; faithful flat descent along the cover reflects its vanishing. This proves only the forward implication.',
 'E',
 'Katz1970 §5, notably Proposition5.2 and Theorem5.9, supplies the p-curvature functoriality used in the spreading/descent argument. The converse is the distinct arithmetic conjecture recorded by root C-SA04-641, whose modern status is handled there.',
 'Established necessary direction. It is not merged into the conjectural converse, because the manuscript states and treats them separately.',
 ['BKatz1970Supplement'])

claim(705,['SA04-663'],[208,209],[P6+':72–123'],'(Ω¹) tensor p; ω tensor p',
 'The p-curvature target in relative dimension greater than one is End(E)⊗F*Ω¹_(Xprime/S), not the literal full tensor power End(E)⊗(Ω¹)^(⊗p). For a line, the Cartier defect must use the additive Frobenius-power map rather than the generally nonadditive ordinary tensor-power expression.',
 'asserted without proof',
 'In characteristic2, (dx+dy)⊗(dx+dy)−dx⊗dx−dy⊗dy=dx⊗dy+dy⊗dx≠0. The four coefficients [0,1,1,0] are checked in the saved supplement program. Thus the claimed additivity cannot hold in the ordinary tensor square. On curves Ω¹ has rank1 and the appropriate identification holds.',
 'C',
 'Katz1970 Proposition5.2, printed pp191–192, proves additive p-linearity, which yields the Frobenius-pullback target by linear algebra. This locates the mathematical correction; whether the author intended Frobenius tensor notation or a symmetric Frobenius-power submodule remains a reading question.',
 'The ordinary-tensor reading is false in higher relative dimension. The intrinsic Frobenius-twisted version is established; the manuscript is not silently emended.',
 ['BKatz1970Supplement'])

claim(706,['SA04-664'],[212],[P6+':178–194'],'0→Pcip→Pci→V/Vformal (4.1)',
 'In equation(4.1), the kernel of p-curvature modulo its formal completion is the nilpotent-p-curvature locus Pcin, not the zero-p-curvature locus Pcip as printed.',
 'asserted without proof',
 'On A1 over F2[ε]/ε², the flat connection d+εx dx has p-curvature ε: (∂+εx)²=ε. It is nonzero but nilpotent. Therefore it lies in the displayed kernel and outside Pcip. The exact saved matrix check on basis1,x corroborates the full differential-operator proof in root_supplement_proofs.md. The following(4.2) correctly distinguishes the loci.',
 'C',
 'The counterexample is elementary and independent. Katz1970 §5 defines zero versus nilpotent p-curvature; the surrounding formal-completion statement is root C-SA04-650. This supplement records the displayed exact-sequence error, not a new claim of a crystal equivalence.',
 'Literal kernel label refuted. Replace it only as a mathematically motivated suggested reading; no manuscript image was inspected.',
 ['BKatz1970Supplement'])

claim(707,['SA04-665'],[210,211],[P6+':154–171'],'extension universelle ... annulé par V',
 'Over a perfect field of characteristic p, for an abelian variety B, the extension 0→α_B→B^(p)→B→0 given by Verschiebung is universal among commutative extensions of B by affine commutative groups H with V_H=0, with the usual finite-type/fppf conventions.',
 'asserted as known',
 'For any extension0→H→E→B→0, naturality makes V_E:E^(p)→E kill H^(p) when V_H=0. It descends to a lift u:B^(p)→E of V_B. Its restriction α_B→H gives the pushout presentation. Any two lifts differ by a map B^(p)→H, which is zero because an abelian variety has only constant maps to an affine group and a group map sends zero to zero. Thus the pushout map is unique.',
 'C',
 'The precise universal formulation was searched using Verschiebung, affine Vkilled extensions, Cartier duality and universal vector extensions. Opened Chai–Oort2009 §10.24 supplies natural Verschiebung for flat commutative groups; Fonseca–Matthes2022 §2.2 supplies the neighboring vector-extension universal property and cites Mazur–Messing I.1.10. No opened primary source with this exact Vkilled-affine universal formulation was located. The above independent proof establishes the stated perfect-field finite-type interpretation; historical attribution remains unassigned.',
 'Mathematically proved here for the explicitly stated commutative perfect-field category. The category and general-base extension require specification before promoting the source into a broader relative theorem.',
 ['BChaiOort2009Supplement','BFonsecaMatthes2022Supplement'],'high for the stated category; medium historical match')

claim(708,['SA04-665'],[211],[P6+':173'],'enveloppe vectorielle ... Lie(B*) dual',
 'Let A=B* and α_B=kerV_B. The universal vector extension of B is the pushout of its Verschiebung extension along the universal linear vector-group map α_B→V(Lie(A)^dual). The finite group whose vector envelope is used is α_B; its Cartier dual kerF_A has height one and supplies the Lie-space description.',
 'proof sketched',
 'For a finite group α with Cartier dual β, primitives in O(α)=O(β)* identify with Lie(β). Hence Hom(α,Ga)=Lie(β)=Lie(A) here; more generally maps to vector groups are represented by Lie(A)^dual with linear maps between vector groups. Apply the universal pushout in C-SA04-707 to H=Ga^r (whose Verschiebung is zero). This gives the standard vector-extension universal property. A literal antecedent referring the vector envelope to β instead of α would be wrong: Hom(μ_p,Ga)=0.',
 'C',
 'Opened Fonseca–Matthes2022 §2.2, pp2–3, verifies the usual universal vector extension and its Hom-to-Ext property, citing Mazur–Messing I.1.10. The α_B pushout derivation is independently supplied here, with the linearity convention explicit. The precise historical wording and antecedent are not certified from ink.',
 'The corrected, carefully typed pushout statement is proved. The phrase vector envelope must use α_B and linear morphisms of vector groups; it is not a universal property for all additive-polynomial morphisms of affine groups.',
 ['BFonsecaMatthes2022Supplement','BChaiOort2009Supplement'],'high mathematical reconstruction; medium source antecedent')

claim(709,['SA04-666'],[189],[P4+':306'],'pleinement fidèle ... du moins F de présentation finie',
 'For smooth surjective X→S with geometrically connected fibers in characteristic zero, the author asserts full faithfulness of pullback from quasi-coherent base modules to relative connections, tentatively restricting to finitely presented modules.',
 'asserted without proof',
 'Over an algebraically closed characteristic-zero field and connected smooth X, horizontal regular functions are constant, so horizontal maps between trivial bundles are constant matrices; this proves the finite-dimensional point-base case. The arbitrary-base and quasi-coherent quantifiers require a relative constants/descent argument, not just this field calculation.',
 'C',
 'Searches for relative horizontal constants, pullback full faithfulness and stratified fundamental groups led to the opened point-base dos Santos comparison and relative Lara homotopy theorem, neither of which is an exact proof of this characteristic-zero arbitrary-base quasi-coherent statement. It remains a precise bibliographic/proof-check gap in this audit, not a claim that the statement is new or false.',
 'Field case independently checked. A complete general-base proof with the source’s finiteness conventions was not obtained in this run; do not label the whole assertion verified from a textual reread.',
 ['BDosSantos2007Supplement','BLara2019Supplement'],'medium')

items=[]
def item(n,kind,scans,lines,words,statement,reconstruction,reason):
    items.append(dict(id=f'SA04-{n}',sources=[],kind=kind,cote='93',scans=scans,lines=lines,his_words=words,statement=statement,reconstruction=reconstruction,check='corrects',check_reason=reason))
item(661,'unproved claim',[189],[P4+':306–320'],'qu. coh.; cohérents','Local triviality and Cartier descent are equated for a quasi-coherent category.','Separate the torsion-module counterexample C700 from the valid descent theorem C701 and from the coherent/quasi-coherent category mismatch.','All lines read; this is an unindexed source-derived supplement, not a new NOTES_INDEX verdict row.')
item(662,'other',[194,195],[P5+':14–35'],'voisinage ouvert','Finite-étale generic triviality implies vanishing p-curvature after shrinking the arithmetic base.','Retain the necessary direction as C704 separately from root C641’s converse question.','The displayed necessary implication is materially distinct and was checked by a spreading/descent argument.')
item(663,'reading question',[208,209],[P6+':72–123'],'tensor p','The p-curvature target and Cartier defect use tensor-power notation.','C705 distinguishes Frobenius pullback from a full ordinary tensor power in relative dimension greater than one.','Literal tensor-square counterexample; no ink comparison or silent emendation.')
item(664,'reading question',[212],[P6+':178–194'],'Pcip; (4.1)','An exact-sequence kernel is labeled by the zero rather than nilpotent p-curvature locus.','C706 gives a nonreduced-base line-connection counterexample and the conditional corrected label Pcin.','Read against definitions and subsequent(4.2); independent calculation saved.')
item(665,'unproved claim',[210,211],[P6+':154–173'],'universelle; enveloppe vectorielle','Verschiebung is presented as a universal extension by groups killed by V, with a vector-envelope pushout.','C707/708 specify perfect field, commutative affine groups, and linear vector-group universal property.','This exact universality is distinct from root C649’s Picard/de Rham universal extension; the source calls it known but no exact primary locator was found.')
item(666,'unproved claim',[189],[P4+':306'],'pleinement fidèle','Pullback with canonical connection is asserted fully faithful over a characteristic-zero base.','C709 isolates the general-base coherent/full-faithfulness statement from the later monodromy classification.','The assertion was omitted by a thematic summary; finite-dimensional field case and remaining general-base proof gap are separated.')

problems=[]
def problem(n,title,item,scans,lines,as_he,now,art,worth,refs):
    problems.append(dict(id=f'MP-SA04-{n}',title=title,occurrences=[dict(item=item,scans=scans,lines=lines)],as_he_states=as_he,plausible_today=now,state_of_art=art,why_open='No documentary reason for nonpublication or later abandonment was established. The source status and the present mathematical scope are recorded separately; no psychological explanation is inferred.',worth=worth,refs=refs))
problem(201,'Relative enlarged-monodromy reconstruction','SA04-627',[191],[P4+':332–334'],'Representations of the given relative Π should be equivalent to fiberwise-subordinate stratified coherent objects.','Specify the exact covering site, strict pro-group, finite-presentation/flatness of coefficients, and effective descent requirements before asking whether the fiberwise criterion suffices.','C698: related point-base and proper reduced-fiber theorems are opened; no exact arbitrary-base equivalence found. Root MP164 may cross-reference or absorb this record rather than duplicate it.','High value as a formulation-and-comparison project; no unconditional new theorem proposed.',['BDosSantos2007Supplement','BLara2019Supplement'])
problem(202,'Given stratified line versus torsion ordinary line','SA04-628',[192,193],[P4+':337–341',P5+':5–7'],'A given stratified line is étale-trivial iff a prime-to-characteristic power is stratified-trivial; can finite type be relaxed to locally finite type?','Keep the given stratification in the statement, distinguish geometric unibranchness from smoothness, and separate field descent from arithmetic π1.','C699 and703 establish the usual finite-monodromy/Kummer setting and unit consequence; locally-finite-type and the full singular arbitrary-field convention were not checked.','Useful narrow reconstruction of the source’s margin question.',['BDosSantos2007Supplement','BStacks0GIYSupplement'])
problem(203,'The category in the local-triviality criterion','SA04-661',[189],[P4+':306–320'],'All four conditions, including local triviality, are equivalent for quasi-coherent E.','Use QC Cartier descent; restrict to finite locally free objects when requiring local horizontal frames, or define a different site of pairs explicitly.','C700 supplies a torsion counterexample; C701 is exactly matched by Katz Theorem5.1.','The literal fixed-base issue is closed by counterexample; archival inspection may clarify the intended site/category.',['BKatz1970Supplement'])
problem(204,'Verschiebung divisibility at every closed reduction','SA04-631',[197,198],[P5+':99–106'],'Does rational liftability of every closed reduction through V force a section to be torsion?','The stated criterion is false. Any replacement must retain connection/universal-vector-extension information or add a materially stronger arithmetic condition.','C702 refutes the rational-lift reading with E:y²=x³−2x over Spec Z[1/30] and P=(2,2). This refines root C644.','Do not advertise the printed question as still open. Studying a corrected stronger condition would be a new project, not the original claim.',['BMilne2021Supplement','BChaiOort2009Supplement'])
problem(205,'The p-curvature coefficient object','SA04-663',[208,209],[P6+':72–123'],'The tensor-power target should support the additive Cartier-defect map.','Use the Frobenius pullback of Ω¹, or explicitly identify a symmetric Frobenius-power subobject; ordinary tensor powers work here only in rank1.','C705 gives a characteristic-two surface counterexample to the literal reading and matches p-linearity in Katz Proposition5.2.','A precise editorial problem, not an unsolved p-curvature theorem.',['BKatz1970Supplement'])
problem(206,'Formal kernel and p-nilpotent-base interpretation','SA04-664',[211,212,213],[P6+':175–229'],'Nilpotent curvature should give the formal completion of the zero-p-curvature locus, also when p is nilpotent on S.','Separate characteristic-p scalar p-curvature from mixed or p-nilpotent-base quasi-nilpotence; specify the PD/crystalline construction before transferring formulas.','C706 refutes the printed(4.1) kernel; root C650’s completion statement is valid with characteristic-p/noetherian test conventions. No complete all-p-nilpotent-base definition is supplied on the page.','Worth a narrow reconstruction; do not extend the elementary characteristic-p proof across a missing definition.',['BKatz1970Supplement','BFonsecaMatthes2022Supplement'])
problem(207,'Verschiebung universality and the correct vector envelope','SA04-665',[210,211],[P6+':154–173'],'V_B is universal among affine Vkilled extensions, and its vector pushout is the universal vector extension.','Use commutative groups over a perfect field, the envelope of α_B rather than its Cartier dual, and linear maps of vector groups.','C707/708 contain independent proofs; exact historical theorem locator remains unassigned after targeted searches. Standard vector-extension property checked in Fonseca–Matthes§2.2.','Mathematical statement is settled in the stated category; high-value remaining work is exact provenance and relative generalization.',['BChaiOort2009Supplement','BFonsecaMatthes2022Supplement'])
problem(208,'Full faithfulness of horizontal pullback over a base','SA04-666',[189],[P4+':306'],'Smooth surjective geometrically connected fibers in characteristic zero should make pullback fully faithful, at least for finitely presented modules.','Formulate the relative-horizontal-constants result with exact base and module hypotheses.','C709 checks the finite-dimensional field case but leaves the broad relative proof/bibliographic match unverified.','A focused technical lemma worth checking; not evidence of a historically new claim.',['BDosSantos2007Supplement','BLara2019Supplement'])

readings=[
 ['93','189',P4+':308','localement sur (X→S)','Specify whether localization fixes S','C700 torsion counterexample applies to ordinary neighborhoods over fixed S; a non-Cartesian site would require a definition.','high','conditional mathematical constraint; ink undecided'],
 ['93','189',P4+':320','coherent source; quasi-coherent target','Both categories QC, or both coherent under finiteness assumptions','C701/Katz Theorem5.1; an infinite direct sum of trivial objects cannot come from a coherent source.','high','high literal category mismatch; ink undecided'],
 ['93','190',P4+':329','enlarged strict group, not necessarily profinite','Do not silently replace by ordinary profinite étale π1','The source explicitly retains nonnormal cases; finite-image inference requires its profinite/geounibranch hypotheses.','high','high textual'],
 ['93','191',P4+':332–334','equivalence marked ?','Construction and fibre criterion remain separate','C698 retains the source’s question mark and arbitrary-relative-base gap.','high','high textual'],
 ['93','192',P4+':339','L^n trivial as stratified','Underlying L^n merely trivial is weaker','C699 and the source’s explicit necessary-only clause.','high','high'],
 ['93','194',P5+':20','fundamental groups of components of E_K','Likely components of X_K','The local system lives on X_K; E_K is the bundle total object. This is a mathematical cue, not an ink certification.','medium','high intended mathematical object; ink undecided'],
 ['93','198',P5+':106','lifts through V over residue field','Do not weaken to fppf-local liftability','C702 refutes even rational lifts at every closed point, so the rational interpretation does not rescue the criterion.','high','high mathematical'],
 ['93','208–209',P6+':72–116','ordinary tensor p','Frobenius pullback, or stated symmetric Frobenius-power subobject','C705 nonadditivity on a surface rules out literal ordinary tensor powers; curve rank1 is different.','high','conditional on notation'],
 ['93','211',P6+':173','vector envelope of ce groupe fini','Envelope of α_B, not of D(α_B)','C708 primitive-element calculation; Hom(μ_p,Ga)=0 would contradict the alternate antecedent.','high','high mathematical; antecedent undecided'],
 ['93','211',P6+':175','connexions à courbure nilpotente within Pci','p-curvature/quasi-nilpotence needs a definition when p is only nilpotent','Pci already denotes flat connections; ordinary curvature would be zero throughout. Characteristic-p and p-nilpotent-base concepts must be separated.','high','high semantic; exact mixed-base meaning undecided'],
 ['93','212',P6+':182–185','Pcip in(4.1)','Pcin','C706 explicit ε p-curvature counterexample; following(4.2) distinguishes zero and nilpotent loci.','high','high mathematical; ink undecided'],
 ['93','213',P6+':229','completion along Pcip','Not completion only at identity','Zero p-curvature locus includes B^(p) in the universal-extension setting; root C650 should retain this whole locus.','high','high textual']
]

events=[]
for c in claims:
    if c['status_on_pages'] in ['asserted without proof','asserted as known']:
        c['status_on_pages']='stated without proof'
    if c['id'] in ['C-SA04-700','C-SA04-702','C-SA04-705','C-SA04-706']:
        c['status_on_pages']='false as stated'
    if c['confidence'] not in ['high','medium','low']:
        c['confidence']='medium'
    events.append([c['id'],DATE,WHO,'used and rechecked in this run','Textual only, not proof: all cited lines were read in context and the visible hypotheses, questions, deletions and category changes were retained.'])
for n in [699,700,702,703,704,705,706,707,708]:
    events.append([f'C-SA04-{n}',DATE,WHO,'independent re-proof','Written source-specific argument in root_supplement_proofs.md and/or this claim record; scope and interpretation limits stated explicitly. Counterexamples use the additional refuted event below. No novelty claim.'])
for n in [702,705,706]:
    events.append([f'C-SA04-{n}',DATE,WHO,'computation or formal certificate','Exact calculations in programs/b_supplement_computations.py; outputs/b_supplement_computations.json. Finite checks do not replace the general argument.'])
for n,scope in [(698,'dos Santos Proposition13 and Lara Theorem3.1: related restricted theorems only'),(699,'Stacks0GIY and dos Santos Proposition13: precise restricted comparison'),(701,'Katz Theorem5.1: exact QC Cartier equivalence'),(702,'Milne Cor5.7 and Theorem9.4; Chai–Oort10.24: counterexample ingredients'),(705,'Katz Proposition5.2: additive p-linearity'),(707,'Chai–Oort10.24; exact affine universality locator not found'),(708,'Fonseca–Matthes§2.2: standard vector-extension property')]:
    events.append([f'C-SA04-{n}',DATE,WHO,'used and rechecked in this run','Primary-text statement/hypothesis comparison only, not a re-proof of the cited theorem: '+scope+'. This event certifies only the stated opened passages, not all claims in the source or a first-circulation date.'])
for item_record in items:
    item_record['check']='agrees'
    events.append([item_record['id'],DATE,WHO,'used and rechecked in this run','Textual only, not proof: source-derived unindexed item compared with every cited passage. Mathematical corrections are separately recorded in claims/proof events.'])
for key,scope in [
    ('BDosSantos2007Supplement','author-version Proposition13 pp13–14 and nonclosed-field warning; metadata in author bibliography'),
    ('BKatz1970Supplement','Theorem5.1 and Proposition5.2, pp190–192; exact QC and p-linearity hypotheses'),
    ('BMilne2021Supplement','II§5 Cor5.7 p66 and IV§9 Thm9.4 p150; edition title page'),
    ('BChaiOort2009Supplement','§§10.23–10.24 pp530–531 and volume publication metadata'),
    ('BLara2019Supplement','v1 Theorem3.1 printedp7; arXiv5November2019 submission record'),
    ('BStacks0GIYSupplement','Lemma59.65.2 statement and finite-Galois-cover proof'),
    ('BFonsecaMatthes2022Supplement','v2 §2.2 pp2–3; no exact Vkilled-affine universality theorem')]:
    events.append([key,DATE,WHO,'used and rechecked in this run','Primary text opened and hypotheses compared; not a complete independent proof: '+scope+'.'])
for original,refined,scope in [
    ('C-SA04-700','C-SA04-701','QC local-triviality assertion under the fixed-base localization interpretation'),
    ('C-SA04-644','C-SA04-702','rational Verschiebung liftability at every closed reduction implies torsion'),
    ('C-SA04-705','C-SA04-705','literal ordinary-tensor target; refined intrinsic Frobenius target in the same record'),
    ('C-SA04-706','C-SA04-650','literal equation4.1 kernel; refined nilpotent formal-completion statement')]:
    events.append([original,DATE,WHO,'refuted','Refined statement '+refined+': '+scope+'. All hypotheses of the displayed counterexample are checked in root_supplement_proofs.md.'])

for name,data in [('root_supplement_claims.json',claims),('root_supplement_items.json',items),('root_supplement_problems.json',problems)]:
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def tsv(name,header,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(header);w.writerows(rows)
tsv('root_supplement_readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],readings)
tsv('root_supplement_events.tsv',['statement_id','date','who','type','outcome'],events)
assert len({x['id'] for x in claims})==12
assert len({x['id'] for x in items})==6
assert len({x['id'] for x in problems})==8
print(json.dumps({'claims':len(claims),'items':len(items),'problems':len(problems),'readings':len(readings),'events':len(events),'scope':'Serialization of manually reasoned records only; no automated scholarly verdicts.'},indent=2))
