#!/usr/bin/env python3
"""Individually authored cote2 problem, reading and link indexes."""
import json,csv
from pathlib import Path
P=Path(__file__).resolve().parent
I={int(x['id'].split('-')[-1]):x for x in json.loads((P/'items.json').read_text())}
problems=[]
def p(n,title,items,as_he,plausible,art,refs,why,worth):
    problems.append(dict(id=f'MP-SA23-root-{n:02}',title=title,occurrences=[{'item':I[i]['id'],'cote':'2','scans':I[i]['scans'],'lines':I[i]['lines']}for i in items],as_he_states=as_he,plausible_today=plausible,state_of_art='As of19November2026: '+art,why_open=why,worth=worth,refs=refs))
p(1,'The question mark in the preliminary curve diagram',[4],
 'The branch L=D∩N→N on scan4 has a question mark; the text also proposes verifying its numerical identity on point sheaves and O_X.',
 'For a smooth proper geometrically connected curve, the numerical Riemann–Roch reduction is valid; no unique strongest modern meaning can be assigned to the diagram mark without fixing the preliminary groups.',
 'Borel–Serre1958 §7 and Stacks0AYQ establish the precise numerical statement. They do not identify the marked arrow in this unfinished presentation.',
 ['BorelSerre1958','Stacks0AYQ'],'No reason or subsequent resolution of the diagram mark is stated.','Worth source reconstruction, not a new Riemann–Roch research problem: first determine what the question mark qualifies.')
p(2,'Bimodule-valued polarization',[76],
 'Are all preceding identities still valid for an A-bimodule-valued form satisfying the unprovided conditions(1)–(4)?',
 'Identities(9)–(13) survive with left/right actions kept distinct. The scalar form of(14) requires compatible central actions of i; without them it fails under the conventional bimodule sesquilinearity axioms.',
 'Ram2011 supplies explicit modern axioms. The present-run example A=C, twisted right action andPhi(x,y)=xy gives0 versus4 in(14). Missing manuscript axioms prevent an unconditional historical verdict.',
 ['Ram2011'],'The margin has only a question mark; the referenced axioms are off the supplied leaf.','Worth a short source-collation run: retrieve the preceding typed definitions before deciding whether the question already assumes centrality.')
p(3,'Completing exterior operations from symmetric tensors',[21,24],
 'The text promises to derive the exterior operations later from the equivariant tensor-power formalism, while revising the admissible Young-subgroup modules.',
 'For an exact category of finite locally free O-modules, exterior powers induce lambda operations onK0 via the exact-sequence filtration; a symmetric-power representation model must preserve that filtration and descent integrally.',
 'Atiyah1966 §§1–3 establishes the complex topological tensor-power setting. Serre1977 §7.1 explains orbit induction. These do not by themselves settle every integral ringed-topos convention of this draft; the local basis argument is verified here.',
 ['Atiyah1966','Serre1977'],'A proof is promised; the supplied pages stop before the complete descent argument. No historical explanation for that stopping point is given.','Worth a bounded reconstruction of the exact-category assumptions and descent step; avoid presenting the complex representation specialization as the whole answer.')
p(4,'Is the universal Chern comparison always injective?',[32,33],
 'Est-ce que phi_K est tjrs bijectif ??? followed on the same sheet byNon andK=Z[L]/(L−1)^n with one geometric generator.',
 'It is not always injective for a selected geometric family. Forn≥3, C^n(K,{L})=Z/(n−1)!; addingnL−1 imposesξ^n=0.',
 'Answered on scan22 itself. The exactn=3 ring and the all-n leading coefficient are recomputed. SGA6 V6.13–14 and Mackall2020 Prop2.1/Th4.1 are related universal constructions with explicitly different input conditions.',
 ['SGA6V','Mackall2020'],'The author answers it immediately; no longer-open question should be attributed to him.','Worth developing only the dependence on the chosen family, because the universal injectivity question itself is closed.')
p(5,'The cancelled direct proposition',[40],
 'Proposition(à prouver directement) begins an equivalence but is deleted and ends with an empty(ii).',
 'No unique formulation is recoverable; the nearby factorial comparison does not determine the missing condition.',
 'SGA6 V§6 was checked for nearby statements, but none can be substituted as the absent second condition on textual grounds.',
 ['SGA6V'],'Explicitly withdrawn; the reason and missing condition are not supplied.','Not worth mathematical development before scan collation and recovery of the missing condition.')
p(6,'Redundancy of the determinant condition',[37],
 'c1(E)=c1(det E), conséquence des autres?? under the full augmented lambda-map definition and geometric rank bounds.',
 'Yes: inCh(A), λ^n[n,1+a1+...+an]=[1,1+a1]. The conclusion can fail for the abbreviated ring-only presentation.',
 'Grothendieck’s1957 report§3 Prop1.2, reprintedSGA6 p30, and SGA6 V6.6.1 give the exact identity. The universal splitting proof is included inproofs.md R8.',
 ['GrothendieckRRR1957','SGA6V'],'Left as a question on the page; no reason is recorded.','Useful for a precise commentary, but mathematically settled under the full definition.')
p(7,'Generation of the gamma filtration',[38],
 'À voir ... si les E_s engendrent??? asks whether the chosen geometric generators suffice to generate the gamma filtration.',
 'For a special augmented lambda ring ring-generated by the indicated geometric elements, weighted monomials inγ^i(E_s−ε_s) generate its canonical gamma filtration.',
 'SGA6 V’s free-lambda framework supports the exact integral free-ring/quotient proof written here inR8. This conclusion says nothing about replacing a chosen-family universal property by an all-geometric-family one.',
 ['SGA6V'],'It is a marginal proof obligation; the text supplies no explanation for leaving it.','Worth writing up as a short integral lemma for the commentary; no open existence question remains in this formulation.')
p(8,'A supported Chow substitute from a filtration',[50],
 'On essaiera de définir a supported intersection theory via a filtration on the lambda pseudo-ring; scan38 ends with??.',
 'Specify a noetherian scheme, a family of closed supports, supported exterior operations and a gamma convention, then ask for a comparison with a precisely defined supported cycle theory. Several inequivalent choices are possible.',
 'SGA6 Exposé0§2, BFM1975 I§6/II§1–3, Fulton–Gillet1983 p288 and Stacks0FET give established ordinary or localized rational theories. They do not identify the exact integral supported object suggested here.',
 ['SGA6','BFM1975','FultonGillet1983','Stacks0FET'],'Only the programme is written. The support quotient and nonunital operation conventions are not specified; this is an observed gap, not an attributed historical motive.','Worth a focused definition-and-comparison task, beginning with one regular affine pair and separating integral from rational targets.')
p(9,'Cohomological or homological Chern classes?',[51],
 'A one-line extension proposal ends in??; the adjective itself is doubtful betweencohomologiques andhomologiques.',
 'A bivariant theory can accommodate both variances, but it cannot determine which one-line question is written.',
 'Alonso–Jeremías–Sancho2023 Th6.1 constructs bivariant relative-perfectK0; BFM1975 gives a covariant rational character. Neither is an exact solution to an unidentifiable sentence.',
 ['AlonsoEtAl2023','BFM1975'],'The wording and intended target are unresolved in the supplied transcription.','Scan review has priority; no standalone mathematical project should be cut from the undecided adjective.')
p(10,'Inverse images without conditions',[52],
 'images inverses sans conditions(?) in the relative-perfect/support programme.',
 'Absolute perfect complexes have arbitrary derived pullback. Relative perfection survives a Tor-independent classical square; unconditional classical base change fails.',
 'Alonso–Jeremías–Sancho2023 Prop3.11 is the exact positive result. The dual-number fibre-product counterexample is proved here by its periodic free resolution.',
 ['AlonsoEtAl2023'],'The page does not specify whether it means absolute or relative perfection, nor derived versus classical fibre products.','Worth a concise functoriality chart; the major mathematical alternatives are already settled.')
p(11,'Proper covariance with no extra Tor condition',[53],
 'propriété sur supports(sans plus), with tentative K_? andA_? notation, asks for a covariant character compatible with proper direct image.',
 'For properf:X→Y over a noetherianS, Rf_* sendsS-perfect complexes toS-perfect complexes without requiringf itself to have finite Tor dimension. A compatible target character still needs a specified theory.',
 'Alonso–Jeremías–Sancho2023 Prop3.5 andTh6.1 prove the relative-perfect pushforward and bivariant operations. Fulton–Gillet1983 proves rational coherent Riemann–Roch over a field.',
 ['AlonsoEtAl2023','FultonGillet1983'],'The page states a programme with provisional notation; it gives no reason for the lack of a completed target construction.','Worth integrating into a commentary, while keeping the establishedK-theory statement separate from the unspecified supported integral target.')
p(12,'The unfinished canonical element',[54],
 'The character should involve un élément canonique explicitable, without a completed definition.',
 'For a finite-Tor-dimension map,[O_X] is the relativeK-theory orientation. A general singular Todd homology class need not equal an ordinary cohomology class capped with[X].',
 'Alonso–Jeremías–Sancho2023 §6.9/Prop6.10 gives the orientation; BFM1975 §0.2 andIV§6 gives the obstruction to the broader cohomological interpretation.',
 ['AlonsoEtAl2023','BFM1975'],'No identification or reason for abandonment is stated.','Worth only after resolving which proposed theory the element belongs to; the modern orientation is a comparison, not a recovered definition.')
p(13,'Localized Riemann–Roch with supports',[58],
 'The expressionch(i_!x)Todd(X′/S) is placed in the supported programme, ending with uncertain target/filtration notation.',
 'For a separated finite-type scheme over a field embedded in a smooth ambient scheme, a localized Chern character of a bounded locally free resolution times the ambient Todd class gives its rational Riemann–Roch class.',
 'Fulton–Gillet1983 p288 property(3) matches this formula; BFM1975 I§6 supplies the earlier construction, and Stacks0FET gives a supported bivariant character. This is not an integral theorem for every unspecified baseS.',
 ['FultonGillet1983','BFM1975','Stacks0FET'],'The transcript records a proposed extension, without a full definition of its target.','Worth a precise comparison section; the rational embedded formula is established, while the remaining task is to specify the manuscript’s stronger scope.')
p(14,'The cancelled splitting-dependent character',[8],
 'An unfinished homological-character homomorphism on scan8 is crossed out after the preceding discussion of a nonnatural splitting.',
 'Keep the live Cartan/structure-sheaf map and the dependence ofδ on chosen lifts; no unique canonical character follows from that choice.',
 'Quillen1973 §5 explains coherent dévissage, while the later supported character uses different intrinsic constructions. Neither identifies the cancelled incomplete map.',
 ['Quillen1973','BFM1975'],'Cancelled on the page. Nonnaturality may explain it, but the source does not say so.','Not a current conjecture; worthwhile only as an editorial account of the abandoned construction.')
p(15,'The abandoned effective-divisor example',[14,15],
 'The hypersurface setup on scan14 is cancelled and replaced by the elliptic point difference.',
 'Use the live rank-zero2-torsion line-bundle class; a nonzero effective divisor on a proper curve cannot itself have torsion class.',
 'The integral Chern-ring identities inGrothendieck’s1957 report verify the replacement. Its smallerE×P2 variant is an earlier-run implication, not the author’s example.',
 ['GrothendieckRRR1957','GrothendieckChern1958'],'The replacement is visible; its motive is not explained.','Useful for correcting attribution in the commentary, not for a new open-problem list.')
# Final manual provenance audit: a withdrawn asserted example is not itself
# an authorial question. Keep the commentary task without inflating Stage 3.
editorial_tasks=[]
for problem in problems:
    problem['problem_origin']='authorial question or explicit unfinished programme'
    if problem['id']=='MP-SA23-root-14':
        problem['problem_origin']='withdrawn unfinished authorial construction; not a currently open conjecture'
    if problem['id']=='MP-SA23-root-15':
        problem['original_id']=problem['id']
        problem['id']='ED-SA23-root-15'
        problem['problem_origin']='present-run editorial comparison of a withdrawn asserted example'
        problem['source_cue']='No question or deferred-proof cue in the cancelled hypersurface example, lines470–489; its explicit replacement follows at491–499.'
        problem['reclassification_reason']='The page asserts and then replaces an example. This is retained in the claim map and as an editorial attribution task, outside the authorial problem count.'
        editorial_tasks.append(problem)
problems=[p for p in problems if p not in editorial_tasks]
(P/'editorial_tasks.json').write_text(json.dumps(editorial_tasks,ensure_ascii=False,indent=2)+'\n')
(P/'problem_origin_audit.json').write_text(json.dumps({'date':'2026-11-19','reviewer':'SA23-20261119/root','scope':'All15 original cote2 problem records individually reviewed against the already read manuscript; scan14 and the cancelled character on scans7–8 reread in the final audit.','kept':[{'id':p['id'],'origin':p['problem_origin'],'source_cue':p['as_he_states'],'occurrences':p['occurrences']}for p in problems],'reclassified':[{'original_id':p['original_id'],'id':p['id'],'source_cue':p['source_cue'],'reason':p['reclassification_reason']}for p in editorial_tasks]},ensure_ascii=False,indent=2)+'\n')
(P/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')

readings=[]
def r(scan,line,reading,alt,evidence,weight='high',confidence='high mathematical alarm; ink undecided'):
    readings.append(dict(cote='2',scan=str(scan),line='texts/pro/MPL_2_transcription.tex:'+line,reading=reading,alternative=alt,evidence=evidence,weight=weight,confidence=confidence))
r(3,'39–45;79–80','Phi_N called a quotient, then used inPhi/Phi_N','A relation subgroup, or a different scope for the wordQuotient','The objects have incompatible types in the two displayed uses.')
r(3,'16–25','D annihilates the reduced subgroup with product unspecified','Derived alternating-Tor product in the finalK-theory comparison','O_p⊗O_p=O_p but the alternatingTor class is0; the preliminary product cannot be supplied silently.')
r(4,'94–115','Question mark onL=D∩N→N','No unique replacement; identify what the mark qualifies','The numericalRR reduction does not determine the marked group arrow.','medium','low formulation confidence; ink undecided')
r(12,'388–400','PiecewiseQ_i formula omits eta^r','Coefficient extraction convention, or an explicit eta^r factor','The following total-class expression and degree counting containeta^r.')
r(14,'487–499','Vanishing of allC^i(x) gives vanishing after pushforward','Rank-zero hypothesis or an explicitly augmentedChern convention','x=O_X contradicts the positive-Chern-only reading.')
r('10/12/14','334;399;487–499','Ctilde(y)=0 beside total classes beginning1','Additive zero(0,1) in the augmentedChern ring','Grothendieck1958 §4,2° andSGA6 reportp28 confirm the convention; no need to replace0 by1.')
r(16,'540–557','u^*u_*F≃F^(G′/G)','Underlying-module isomorphism, or Mackey conjugate summands equivariantly','C3⊂S3 withχ nontrivial givesχ⊕χ^−1, notχ⊕χ.')
r(16,'554–558','Finite free subcategories stable under the preceding functors','Finite-index qualifier for restriction along a subgroup','k[Z] restricted to1 is infinite dimensional.')
r(19,'636–644','Deleted local freeness condition versus inserted trivialYoung modules','Preserve the revised modules; determine whether locality survives the deletion','Tensor-basis orbit decomposition works locally; a rank-one trivial module is not free over a nontrivialYoung group algebra.')
r('21/22','726–729;743–770','(−1)^i in proposition, (−1)^(i−1) in proof','The latter sign is mathematically consistent','Degree1 and the universal finite difference verify the proof sign. The earlier exponent is not struck out.')
r(25,'861–865','A^(n+2)=0','All homogeneous degrees≥n+2 vanish, if a truncation is intended','A single missing homogeneous component does not kill products in higher degrees; the exact coefficient proof uses a full cutoff.')
r(25,'869–884','gamma^m(x) after deletion of−epsilon(x)','gamma^m(x−epsilon(x)) as a candidate repair','For a lineL, gamma²(L)=L; evaluatingL=1 kills every proposed shifted ideal generator but not the left side.')
r(29,'974–981','Short relation list presented after full lambda-map definition','Non-exhaustive list, or additional exterior-operation compatibility relations','The rank-two/dual-number countermodel violateslambda²;SGA6 V6.14 explicitly includes those relations.')
r(30,'1005–1019','A identified additively, decorationA! uncertain','Keep the modified multiplication a⋆b=−(i+j−1)!ab/((i−1)!(j−1)!)','The manuscript’s additive caveat agrees with the printed1957 report andSGA6 V6.5.3.')
r(33,'1030–1055','D_parf(i_n), withrelatively in the initial definition','Retain relative perfection; do not normalize to intrinsicPerf(Z_n)','k overk[t]/t^n isA-perfect but intrinsically nonperfect for n≥2.')
r(34,'1061–1085','Surjective radicial fragment with preceding hypothesis absent','Integral+surjective+radicial in the complete theorem','SGA4 VIII1.1 p367 explicitly suppliesintegral;D(t)⊔V(t)→A1 refutes dropping it.')
r(35,'1111','Rational equivalence with supports unspecified','Distinguish equivalences inside the support from image in ordinaryChow','CH0({0})=Z but its image inCH0(A1) is0.','high','high ambiguity; not an asserted ink error')
r(35,'1115','cohomologiques|homologiques','Both remain candidates','The two variances require different targets and neither is selected by the later bivariant comparison.')
r('36/39','1121–1127;1224–1228','u_i^*(R^nf_i*F_i), u_i:X→X_i','Use theY-projection, calledv_i onscan39','The sheaf is onY_i. The originalSGA4 VII5.11 p364 has the same printed typing defect, so this may be a source-level error.')
r('36/39','1117–1132;1221–1231','Large deletion strokes interpreted as cancellation','Possibly editorial rulings; inspect the strokes','The doubts register explicitly questions their function; exact published statements still exist.','medium','low ink confidence')
r(37,'1141','images inverses sans conditions(?)','Absolute derived pullback, or Tor-independent relative classical base change','The dual-number counterexample separates the two interpretations; no unconditional relative claim follows.')
r(38,'1189–1201','Deleted inverse arrows with survivingv′/w′ equations','Reconstruct each arrow’s endpoints before reading the equations','Nilpotent dévissage is an isomorphism, but the different forget-support map kills the point class inA1.')
r(38,'1204–1218','ch(i_!x)Todd(X′/S) with support target unclear','Localizedch before forgetting support, if the modernRR comparison is intended','Ordinary ambientch may lose support information;Fulton–Gillet1983 property(3) uses localizedch.')
r(41,'1263–1271','Division by(−1)^q C_Y^q(T_Y/X)','A universal polynomial quotient before evaluation; also check the normal-bundle source label','The evaluated topChern class can be zero and need not be invertible.')
r(41,'1276–1282','E^(i) is a vector bundle whose fibre isH^i','Additional base-change/constancy hypotheses, or a coherent derived direct-image interpretation','The Poincaré line bundle overE×Pic0(E) has jumpingh0,h1.')
r(43,'1333–1363','phi_X(f_!xi)','Candidatephi_Y(f_!xi)','f_!xi lies onY; scan41 has the compatibleY formula.')
r(44,'1374–1376','f_*O_X described as a sheaf onX','CandidateonY','Direct image has targetY; the adjacent rank/degree calculation usesY.')
r(45,'1422–1428','C²(O_C) with genus of the normalization','CandidateC²(ν_*O_Ctilde), or add the normalization-defect term','For a rational nodal plane cubic the displayed value is8 butc2(O_C)=9; exact sequence restores+[Q].')
r(11,'359–382','First adjoint targetE|E*','CandidateE*','The next tensor map requiresT^p(E*) before evaluation into(T^pE)*.')
r(13,'435–465','m|n lines andn|m columns','U of shapen×m forF^m→E^n','ThenU^t R U^J has the required shapem×m.')
r(15,'508–537','All scalar polarization formulas extended to anA-bimodule','Check whether the absent axioms impose compatible central scalar actions','Twisting the rightC-action gives0 versus4 in formula(14), while formulas through(13) keep ordered actions.')
r(24,'844–848','p_iota^(n_A) orp_iota^n A','Candidate principal idealp_iota^n A','The valuations and integrality proof use powers of a prime element timesA; the cross-reference is off-leaf.','medium','medium mathematical; ink undecided')
with(P/'readings.tsv').open('w')as f:
    w=csv.DictWriter(f,fieldnames=['cote','scan','line','reading','alternative','evidence','weight','confidence'],delimiter='\t');w.writeheader();w.writerows(readings)

links=[]
def l(kind,frm,to,what,evidence,notes):links.append({'kind':kind,'from':frm,'to':to,'what':what,'evidence':evidence,'note_ids':';'.join(f'MPL_2#{n}'for n in notes)})
l('folder','cote2/scan10 lines281–351','cote2/scan14 lines491–499','Constant-section left inverse verifies nonzero elliptic torsion pushforward.','Both endpoints read; the latter uses the first calculation.',[10,15])
l('folder','cote2/scans21–22 lines660–789','cote2/scans28–30 lines908–1021','Two treatments of the same chosen-familyChern construction, comparison and altered geometric family.','Both units read; explicitL andnL−1 examples identify the shared object.',[25,28,32,33,37,38])
l('folder','cote2/scan33 lines1030–1056','cote2/scans35–38 lines1088–1218','Relative-perfect/support definitions feed the nonunital and covariant-character programme.','Both endpoints read;relative is retained and finite-stage tests do not replace the colimit quantifier.',[42,43,45,50,52,53,58])
l('folder','cote2/scan44 lines1392–1416','cote2/scan45 lines1422–1428','The curve-to-surface computation specializes to a normalization pushforward, exposing the structure-sheaf defect.','Both formulas read and recomputed;C-SA23-root-070/071/071R.',[70,71,72])
l('published work','cote2/scans10–12,21–30','GrothendieckRRR1957 §3,SGA6 printedpp28–32;SGA6V6.5–6.14 printedpp349–359','AugmentedChern operations, factorial leading terms, modified product and completedlambda compatibility.','Original publication scans inspected. Different universal families are not identified.',[11,17,25,27,28,29,30,31,34,37])
l('published work','cote2/scan34 lines1061–1085','SGA4VIII1.1–1.2 printedpp367–368','Exact reused theorem/proof fragment; the complete theorem supplies integrality.','Original source inspected onboth pages;C-SA23-root-047.',[46,47,81])
l('published work','cote2/scans36,39 lines1117–1132;1221–1231','SGA4VII5.11–5.13 printedpp363–364','Exact continuity corollaries; the printed5.11 also has theu_i type mismatch.','Original source inspected; group-scheme versus étale-sheaf warning agrees.',[47,59,60,61,81])
l('published work','cote2/scans33,37','AlonsoEtAl2023 Prop3.5,Prop3.11,Cor4.2,Th6.1,§6.9','Precise relative perfection, proper covariance, Tor-independent base change and orientations.','All cited statements opened and hypotheses compared; canonical-element identification remains a hypothesis.',[42,52,53,54])
l('published work','cote2/scan38 lines1204–1218','FultonGillet1983 p288,Riemann–Roch Theorem(3);BFM1975 I§6','LocalizedChern character times ambientTodd class.','Exact formula read in both works; base-field and rational coefficients stated.',[58])
l('published work','cote2/scans41–44','BorelSerre1958 §7 p113 and§17 Prop16 pp135–136','RationalGRR and fibre tangent/Todd calculations.','Opened full primary paper and inspected exact theorem; curve/surface consequences recomputed.',[63,65,66,67,68,69,70])
l('published work','cote2/scan16 lines540–557','Serre1977 §7.3 Prop22 pp58–59','Mackey decomposition distinguishes conjugate summands from identicalH-modules.','PrimaryPDF downloaded; statement and proof read.',[19])
l('published work','cote2/scans17–19','Atiyah1966 §§1–3;Serre1977 §7.1–7.2','Induction products, tensor powers, projection formula and orbit modules.','Exact primary sections read; complex topological scope not generalized by citation alone.',[21,22,23,24])
l('published work','cote2/scan5','PedriniWeibel1994 AppendixA p404','Rank andPicard description in dimension≤1.','Original appendix inspected, including its noetherian context and reference back toTT.',[5])
l('published work','cote2/scans22,28–30','Mackall2020 Prop2.1 andTh4.1','Comparable factorial maps, with a different all-bundle universal property.','Both definitions and theorem read; comparison is an explicit distinction, not an identity or influence claim.',[25,28,32,33,41])
for key,nums,scans,meaning in [
 ('2-chern-ring-gamma-comparison',[1,25,26,28,37,38,41], '21,22,28,29,30','Chosen-family andlambda-compatibility qualifications'),
 ('2-chern-ring-not-injective-pn',[1,32,33,84],'22','Question answered on the page and changed family'),
 ('2-trivial-total-chern-class',[1,10,11,14,15,16,17,18],'10,12,14','Live elliptic example replaces the cancelled hypersurface setup')]:
    l('our projects','cote2/scans'+scans,'Hua findings register /notes/RESULTS_STATE.md /'+key,meaning,'Lead reported by the supplied notes. The cited register itself is not attached, so its endpoint cannot be independently verified; no project result is imported.',nums)
l('our projects','MPL_2 notes opening lines7–9','LM4/LM7 referee list in earlier context','The notes expressly say this is unrelated to cote2.','Only the report of the earlier context search is present; noLM4/LM7 endpoint or mathematical link is asserted.',[1])
l('our projects','MPL_2#92','records/research_chern_curves.md;research_lambda.md;research_supports.md;research_leads.md','Earlier-run calculation appendices named as evidence.','Unavailable attachments, checked against ZIP inventory. All computations used in this dossier are rerun; this is an unavailable lead, not a verified mathematical link.',[92])
with(P/'links.tsv').open('w')as f:
    w=csv.DictWriter(f,fieldnames=['kind','from','to','what','evidence','note_ids'],delimiter='\t');w.writeheader();w.writerows(links)
events=[]
for x in problems:events.append([x['id'],'2026-11-19','GPT-6 Astra Pro; effort not independently exposed; SA23-20261119/root','used and rechecked in this run','Authorial wording checked against the transcript; opened-reference scope matched. '+x['state_of_art']])
for x in editorial_tasks:events.append([x['id'],'2026-11-19','GPT-6 Astra Pro; effort not independently exposed; SA23-20261119/root','used and rechecked in this run','Problem-origin audit: '+x['reclassification_reason']])
with(P/'problem_check_events.tsv').open('w')as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(events)
print(json.dumps({'problems':len(problems),'editorial_tasks':len(editorial_tasks),'reading_alarms':len(readings),'links':len(links)},ensure_ascii=False))
