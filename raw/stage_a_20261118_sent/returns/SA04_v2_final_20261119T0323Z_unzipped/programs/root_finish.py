"""Manually authored final additions to the root research stream.

This program serializes judgments already made by direct reading. It performs no
text classification, automatic verdict assignment, or literature inference.
"""
import root_build as b
from pathlib import Path
import json

def claim(n): return next(x for x in b.claims if x['id']==f'C-SA04-{n}')
def item(n): return next(x for x in b.items if x['id']==f'SA04-{n}')

claim(686)['fate']='R-Q35: the opened CSG Articles and books catalogue explicitly identifies the Illusie-to-Grothendieck letter dated 24 February 1968 in cote 100. Both supplied transcriptions place the letter on scan 30. This verifies the letter’s identity, not the eventual outcome of its proposed appendix and Künneth work.'
for x in [claim(686),item(660)]:
 x['scans']=[30]
 x['lines']=['pro/MPL_8_079-081+9+4+100_transcription.tex:2029–2048','codex/K100-03_transcription.tex:40–59']
claim(686)['fate_date']='Letter dated 24 February 1968; date of its eventual archival publication is not established here.'
claim(641)['fate_date']='Katz publication 1972; Katz1982 received 19 September 1981; PSW preprint 12 November 2018, publication 2021; Lam–Litt public announcement verified at IAS on 13 October 2025, arXiv first submission 12 January 2026. The announcement does not establish first manuscript circulation.'
claim(641)['fate']+=' A fresh current-state search also opened Litt’s Problem 2, last edited 8 May 2026: even the specified general Gauss–Manin direct-summand case is presented as open. This is corroborating author testimony, not a proof that no solution exists.'
claim(641)['present_status']='As of 19 November 2026: the general conjecture remains open in the primary literature checked on that date. The named special cases and nonabelian isomonodromy results have narrower hypotheses.'
claim(641)['refs']+=['RLamLittAnnouncement2025','RLittProblem2026']
item(602)['his_words']='courbes de genre un; fibres elliptiques, multiplicatives ou additives'
claim(620)['statement']='Let v:E→E″ be the source quotient, let Δ act on E⊗Ω¹, and let D:E″→F be the induced operator satisfying D∘v=Δ∘d_E. The two locally defined Manin-section evaluations then satisfy ν(Δ)=μ(D), with the source’s affine-connection sign convention.'
claim(620)['present_status']='As of 19 November 2026: the equality ν(Δ)=μ(D) for D∘v=Δ∘d_E is proved by the local-jet naturality argument and independently checked. This is the marked equality on scan159, not the converse factorization claim on scan160.'
for x in b.claims:
 x['his_statement']=x['his_statement'].replace('J. Wanderley','Marcus Wanderley')
claim(638).update({'statement':'An étale trivialization of a stratified bundle gives compatible locally horizontal transition matrices, and conversely such a cocycle gives the associated stratified bundle by descent. The source’s proposed relative representation equivalence requires additional hypotheses and is recorded separately as C-SA04-698.','class':'C','fate':'R-Q14: the descent construction is standard and checked directly. The exact broad relative equivalence on scan191 is not established by that construction; opened dosSantos2007 Proposition13 treats a regular scheme over an algebraically closed point base, and the relative pro-étale comparison requires the qualifications in C-SA04-698.','present_status':'As of19November2026: the associated-object construction is valid; essential surjectivity under the source’s broad relative hypotheses is not proved here. The quasi-coherent zero-p-curvature/local-triviality issue is separately tested in C-SA04-700/701.','refs':['BDosSantos2007Supplement'],'confidence':'high'})
claim(644).update({'his_statement':'se remonte à A_s^(p) via Verschiebung; est-il vrai qu’alors ω est d’ordre fini?','statement':'The proposed implication is false: over an integral finite-type scheme S dominating SpecZ, a section of an abelian scheme need not be torsion even if its reduction at every closed point has a residue-field-rational Verschiebung lift.','status_on_pages':'false as stated','computation':'Refinement C-SA04-702 gives the complete counterexample S=SpecZ[1/30], E:y²=x³−2x, P=(2,2). Discriminant512 is a unit. Rational2-torsion and Hasse imply p does not divide#E(Fp) for everyp≥7, so V is bijective on rational points. Good reductions at3 and5 bound rational torsion by2, whileP is not2-torsion. Exact point counts and doubling are saved in b_supplement_computations.py/output.','fate':'R-Q16: Rössler2020 Theorem1.4 solves a fixed-characteristic infinite compatible divisibility problem modulo the constant trace, not this varying-prime one-step criterion. The literal manuscript question is answered negatively by C-SA04-702 in this audit, using opened Milne2021 Hasse/specialization and Chai–Oort Frobenius–Verschiebung identities. No historical novelty is claimed.','present_status':'As of19November2026: refuted under every retained base and rational-lift hypothesis. The full universal-vector-extension condition on scan197 and the p-curvature conjecture remain separate.','refs':['RRoessler2020','BMilne2021Supplement','BChaiOort2009Supplement'],'confidence':'high'})
for e in b.events:
    if e[0]=='SA04-602': e[4]='Textual comparison corrected after reading the explicit genus-one definition at K93-10:15–27: singular fibres are allowed; Proposition2.5 does not omit a discriminant inverse.'
claim(684).update({'class':'C','fate':'R-Q34: EGAIV3 Proposition15.6.3, printedp237, explicitly inherits the locally Noetherian hypothesis from15.6.1. Its DVR reduction is therefore not the stronger non-Noetherian argument proposed in the7April1967 letter. The published weaker theorem is verified; exact later incorporation of the proposed strengthening was not located. EGAIV4 19.1.5 does incorporate the separate basis argument, recorded as C-SA04-683.','present_status':'As of19November2026: the printed locally Noetherian proposition is established; the letter’s proposed removal of that hypothesis has not been matched to an exact later published statement in this search.','confidence':'high'})
claim(679).update({'statement':'For a reductive algebraic group over a field of characteristicp>0 and a fixed nonzero vector in a rational representation, a homogeneous invariant polynomial nonzero there exists, and it can be chosen in p-power degree. This gives the codimension-one symmetric-power complement in Mumford’s formulation.','fate':'R-Q33: Haboush1975 establishes geometric reductivity. The exact invariant-polynomial formulation is read in Sastry–Seshadri2011, introductionp415. Taking the coefficient of t^(d−p^r) in F(x+tv), where d=p^r m and p∤m, converts any separating invariant to p-power degree; thus the source’s p-power condition introduces no remaining gap.','computation':'root_computation_notes.md supplies the general coefficient argument; binom(p^r m,p^r)=m modp is nonzero. The result is attributed to Mumford’s preface and Haboush’s solution, not to a new Grothendieck conjecture.','refs':['RHaboush1975','RSastrySeshadri2011']})
claim(650)['fate']+=' The proof recorded here is in characteristicp. The page also discusses bases on whichp is locally nilpotent; that stronger base scope is not proved by the characteristicp formal-completion argument alone.'
claim(649)['statement']+=' In the source’s Pc0=Pci0 step, all global relative1-forms must be closed, the indicated two-form direct-image target must have the stated affine/corepresentability property, and Pic0 has the asserted abelian-scheme structure.'
claim(650)['statement']+=' The completion is along the entire zero-p-curvature locusPcip (B^(p) in the abelian setting), not just its identity section.'
claim(651)['lines']+=['codex/K93-05_transcription.tex:261–290','codex/K93-06_transcription.tex:7–36']
claim(651)['scans']=[206,207]+claim(651)['scans']
claim(672).update({'class':'A','fate':'R-Q21/30: exact original primary match now verified in SGA7I IX Corollary5.9 and Remark5.9.1, printedpp382–383. The remark attributes to Raynaud extension into every Néronian group and removes semistability and henselianity. The initial ell=p argument retains generic characteristiczero; Remark5.11p386 explicitly makes removal depend on Tate full faithfulness, supplied later by deJong1998. The broad target reduction cites an unpublished Néron-model construction input, not independently proved here.','present_status':'As of19November2026: the exact extension assertion reappears in Grothendieck’s published SGA7 exposition with Raynaud attribution; deJong supplies the expressly identified equal-characteristic input. The audit verifies this dependency and does not claim an independent proof of Raynaud’s unpublished construction.','confidence':'high'})
claim(673).update({'class':'A','fate':'R-Q21/30: the original SGA7I IX proof of5.9, printedpp383–385, reproduces the connected/étale reduction. Lemma5.9.2 has a pushout-representability hypothesis; the footnote invokes an unpublished Raynaud result for automatic representability. Remark5.11p386 identifies precisely the Tate dependence, later removed by deJong1998 with its1999 erratum.','confidence':'high'})
claim(672)['statement']='Over a trait S, for an S-Néronian group G and a p-divisible group H/S, every homomorphism Hη→Gη is claimed to extend uniquely to S. The initially bracketed semiabelian generic-fibre assumption is marked unnecessary on scan 48; scan 53 supplies the broader reduction. The historical proof retains its expressly identified Tate limitation, recorded in C-SA04-673.'
claim(672)['his_statement']='[ ] inutile; Je dis que φ_K se prolonge en φ:M→G'
claim(672)['scans']=[48,49,50,51,53]
claim(672)['lines']+=['pro/MPL_8_079-081+9+4+100_transcription.tex:2539–2545','codex/K100-04_transcription.tex:217–220','codex/K100-04_transcription.tex:375–393']
item(654)['scans']=[48,49,50,51,53]
item(654)['lines']=list(claim(672)['lines'])
item(654)['reconstruction']='The title and final attribution distinguish Raynaud’s theorem from Grothendieck’s handwritten generalization. The bracketed semiabelian assumption is explicitly marked unnecessary, and scan 53 treats an arbitrary Néronian target through its no-additive-subgroup property. This later scope is retained together with the historical Tate dependency.'
claim(673)['statement']+=' The same scan asserts a newly known restricted case when the target’s generic connected part is of multiplicative type, and calls the étale-target case easy; neither sentence supplies a proof of unrestricted equal-characteristic Tate full faithfulness.'
claim(673)['his_statement']='je sais maintenant prouver le théorème de Tate ... de type multiplicatif'
claim(673)['lines']+=['pro/MPL_8_079-081+9+4+100_transcription.tex:2501','codex/K100-04_transcription.tex:325–330']
claim(673)['refs']+=['RSGA7I']
claim(673)['present_status']='As of 19 November 2026: the connected/étale proof structure and its Tate dependency are matched to SGA7I IX5.9–5.11; de Jong’s later theorem supplies the general missing input. The restricted multiplicative-target assertion is recorded as a source assertion, not independently proved here.'
claim(676).update({'statement':'If an algebraic group G_K over the fraction field of a nontrivial discrete valuation ring has a Néron lft-model, it has no K-subgroup isomorphic to Ga. This is the reason given on scan 53 for applying the preceding image lemma to an arbitrary Néronian target, beyond the initial semiabelian case.','his_statement':'G_K n’a pas de ss-groupe isom. à G_a, puisque G_K admet un modèle de Néron','computation':'Independent proof in root_computation_notes.md: the Néron property extends every scaled additive-subgroup map. Its derivative would put a nonzero tangent vector in every power of the uniformizer times the finite free Lie lattice, an impossibility. This proves the no-Ga statement, not every representability step in the image lemma.','fate':'R-Q31 follow-up found the exact assertion in Bosch–Lütkebohmert–Raynaud1990, §10.1 Proposition8, printed pp293–294; statement and proof were opened. The source itself uses this stronger Néron-property rationale, so restricting it to semiabelian groups understates the retained page.','fate_date':'Standard consequence of the Néron property; exact checked textbook formulation published 1990. No first-discovery date is asserted.','present_status':'As of 19 November 2026: the no-Ga assertion for arbitrary Néronian generic fibres is established and independently reproved here. The broader schematic-image lemma remains separately qualified in C-SA04-675.','refs':['RSGA7I','RBLR1990'],'confidence':'high'})
item(655)['reconstruction']+=' The final application explicitly uses existence of a Néron model to rule out Ga, and removes the earlier semiabelian-target restriction.'
claim(670)['statement']+=' On scan 41(iv), Pro reads rationally projective whereas Codex reads algebraic and projective. The exact equivalence is conditional on resolving this witness difference; no reading is changed.'
claim(670)['lines']+=['codex/K100-04_transcription.tex:28–30','codex/K100-04_transcription.tex:98–104']
claim(671)['statement']+=' On scan 43(c), Pro joins the no-infinitesimal-automorphisms and sections conditions by AND, while Codex reads OR and descent-stable sections. Scan 45 also leaves projective versus quasi-finite cover unresolved. These alternatives prevent assigning one stronger unqualified theorem.'
claim(671)['lines']+=['codex/K100-04_transcription.tex:98–104','codex/K100-04_transcription.tex:153']
item(652)['reconstruction']+=' Pro/Codex also differ on rational projectivity versus projective algebraicity and on the conjunction/disjunction of the scan 43(c) conditions; the reading table preserves both.'
item(653)['reconstruction']+=' Scan 43(c) AND/OR and scan 45 projective/quasi-finite cover alternatives remain unresolved between the supplied witnesses.'
for c in b.claims:
    c['refs']=[{'CKatzOda1968':'KatzOda1968','CKatz1970':'Katz1970'}.get(x,x) for x in c['refs']]
for p in b.problems:
    p['refs']=[{'CKatzOda1968':'KatzOda1968','CKatz1970':'Katz1970'}.get(x,x) for x in p['refs']]

P=b.P
P(176,'The full-faithfulness face of the abelian/BT square',[655],
'A compatible abelian morphism onU and a BT morphism onS should come from one abelian morphism, with the boundary in characteristicp andU meeting each connected component.',
'Separate the locally Noetherian associated-point criterion for existing abelian schemes from any stronger arbitrary-open gluing claim.',
'Groth1966 Thm1.1p63 and Proposition1.2p64 give exact sufficient conditions at associated points. They are checked in the primary scan; the page’s more compressed hypotheses require the same tests.',
'The notes give a proposed reduction, not a later explanation of abandonment. The stronger formulation is not settled just by its resemblance to the1966 title.',
'Worth a short hypothesis-by-hypothesis comparison with Proposition1.2.',['RGroth1966'])
P(177,'Effectivity beyond a normal base',[656],
'The abelian/BT gluing functor should be essentially surjective under a finite geometrically unibranch cover and the stated étale-depth condition, or the alternative third-face condition.',
'For a normal locally Noetherian base, denseU and characteristicp boundary, an abelian scheme extends precisely when its BT group extends.',
'Krishnamoorthy–Pál2021 Cor6.12 proves the normal-base assertion; Groth1966 §4.9pp77–78 already asks that question. Neither statement supplies all the manuscript’s nonnormal alternatives.',
'No source records a personal reason for stopping. The finite-cover and depth conditions are actual additional scope, not interchangeable wording for normality.',
'Worth isolating the remaining nonnormal case before attempting a proof.',['RKP2021','RGroth1966'])
P(178,'The algebraicity locus of a specified BT homomorphism',[657],
'Represent the base changes on which a specified BT homomorphism is algebraic by a closed locus, open at its characteristicp points.',
'Use the exact associated-point algebraicity test of Proposition1.2; on a reduced base locally of finite type over a characteristiczero field, use the open-and-closed locus of §2.1.',
'Groth1966 Proposition1.2p64 and §2.1p67 are verified. The universal closed-subscheme assertion over the full source base class was not identified with either.',
'No account of why the broader representability claim was left in draft was found.',
'Worth a representability audit with the base hypotheses written explicitly.',['RGroth1966'])
P(179,'Effectivity of compatible local-ring families',[658,659],
'Compatible systems over all local rings are asserted to glue; the abelian-object version is then marked “Douteux, sans doute faux”.',
'Full faithfulness and object effectivity must be stated separately; an adequate coherence/descent datum on neighborhoods may be necessary.',
'R-Q22/24 searched local systems of abelian schemes and effective descent, and checked Rydh’s étale descent theorem. The latter is about étale morphisms, not this object-effectivity assertion.',
'The manuscript itself records doubt. No counterexample to its exact compatible-system formulation was found here.',
'Worth testing the literal quantifiers on a small nonnormal base.',['RRydh2010','RGroth1966'])
P(180,'A single neighborhood for all future comparisons',[660],
'ChooseV once so that every abelianB′ on every smaller neighborhoodV′ with an isomorphism overSpecO_S,t has that isomorphism on allV′.',
'Ordinary finite-presentation spreading only chooses a neighborhood afterB′ and its isomorphism; the source’s uniform statement is strictly stronger.',
'R-Q22/24 searched the uniform local-ring/abelian-scheme assertion and followed the1966 rigidity criteria. No exact uniform theorem or counterexample was identified.',
'The source leaves the statement open and supplies no subsequent explanation.',
'Worth a focused search for a varying-family counterexample before invoking spreading out.',['RGroth1966'])
P(181,'Proper descent to formally unramified targets',[661],
'A proper schematic epimorphism should descend maps to a formally unramified target when the two overlap pullbacks agree.',
'Retain all separation, quasi-compactness and schematic-density hypotheses in the target lemma; distinguish it from descent of objects.',
'Groth1966 Lemma1.2.1p65 proves the relevant nonramified essentially proper rigidity setup. Rydh2010 Theorem5.17 proves effective descent for quasi-compact étale morphisms along quasi-compact universally subtrusive maps, a different category.',
'The handwritten proof has reductions but no retrospective account of its scope.',
'Worth completing the exact target lemma before applying it to a moduli space.',['RGroth1966','RRydh2010'])
P(182,'Formal unramifiedness of BT Hom',[662],
'Verify the rigidity of the Hom functor for BT groups needed in the descent argument.',
'Use the standard infinitesimal rigidity theorem with a locally nilpotent divided-power thickening and the stated p-nilpotence conditions.',
'The checked Montréal/Illusie crystalline deformation literature supplies BT rigidity in its precise infinitesimal setting; Mazur–Messing I§2.6.7 gives the corresponding universal-extension rigidity. These are not arbitrary thickening statements.',
'This is an explicit verification left on the page; no reason for deferral is recorded.',
'A short reference-and-convention check is worthwhile, but it is not a new open theorem.',['GrothMontreal1974','RMazurMessing1974'])
P(183,'Effective descent of abelian objects along proper epimorphisms',[663],
'Descend an abelian scheme along the specified proper effective epimorphism, with complete-local reductions and a flatness alternative.',
'Keep proper morphism descent, proper object descent, and polarized algebraization as separate claims.',
'Groth1966 and Krishnamoorthy–Pál Cor6.12 supply morphism rigidity and normal-base extension, respectively. EGAIII1 5.4.5 supplies ample polarized algebraization. None alone proves the full object-descent quantifier on the page.',
'The manuscript indicates reductions; no documented historical explanation of the unfinished scope was found.',
'Worth mapping the missing effectivity step to one precise moduli problem.',['RGroth1966','RKP2021','REGAIII1'])
P(184,'Marked formal moduli and an algebraic equalizer',[664],
'Use a marked formal moduli object and formal functions to descend a map satisfying the overlap condition.',
'State representability, formal effectivity and any no-infinitesimal-automorphisms assumptions before using the equalizer.',
'Artin1969 Theorems1.6–1.7, in the opened previewpp25–26, require their effectivity and formal-versality hypotheses; they do not make every marked formal object effective automatically.',
'The source lacks a complete representability proof; no reason for stopping is given.',
'Worth a finite checklist of the exact Artin hypotheses for this one object.',['RArtin1969'])
P(185,'Algebraization tested on normalized one-dimensional subschemes',[665],
'A formal abelian scheme should be algebraizable iff it becomes so after proper surjection, equivalently on the indicated normalized integral curves.',
'The full criterion requires the source’s polarization-locus and descent arguments; the known ample-line criterion is a weaker sufficient condition.',
'EGAIII1 5.4.5 proves polarized algebraization; Krishnamoorthy–Pál2021 Cor7.7 uses a polarized formal setting. R-Q26/27 did not locate an exact theorem with all the page’s equivalences.',
'The page develops a possible proof route; no later source gives a reason it was left there.',
'Worth first auditing the countable polarization-locus step, which controls the proposed criterion.',['REGAIII1','RKP2021'])
P(186,'Bounded-degree polarization loci',[666],
'Cover suitable tests by countably many finite unramified loci of bounded-degree polarizations and force one locus to dominate a component.',
'Keep the marking, degree bound, representability and finiteness hypotheses; Baire handles avoidance only after these loci exist.',
'The Baire lemma is proved in this audit. EGAIII1 5.4.5 treats an already supplied ample line bundle. No exact opened source was found for the entire unpolarized locus package as stated.',
'No source says why the polarization construction remained a draft.',
'Worth checking finiteness for one fixed degree and marking before taking the countable union.',['REGAIII1'])
P(187,'Gluing algebraizations across closed components',[667],
'An algebraization on each irreducible component of a reduced complete local base should glue.',
'One needs compatible algebraizations and effective gluing on the scheme-theoretic intersections, not only componentwise existence.',
'R-Q28 checked formal algebraization and closed-pushout leads; EGAIII1 5.4.1 supplies full faithfulness of proper completion but not arbitrary closed-component effectivity.',
'The manuscript omits the overlap/effectivity proof; no historical reason is stated.',
'Worth examining a two-component base with a nonreduced intersection.',['REGAIII1'])
P(188,'Smooth algebraization through a nilpotent base thickening',[668],
'For a proper smooth formal scheme, algebraization after reduction should imply algebraization before reduction.',
'Over a complete Noetherian local base, lift a proper smooth algebraization successively through the finite nilpotent filtration.',
'The H² obstruction/H¹ torsor/H⁰ automorphism proof is supplied here using proper coherent formal comparison. EGAIII1 5.4.6 asks a broader question without smoothness, and must not be cited as proving this version.',
'The source sketches the method; no personal reason for leaving details is recorded.',
'The recorded smooth lemma is now checked; only extensions outside its hypotheses merit a new task.',['REGAIII1'])
P(189,'Countable avoidance by one-dimensional formal sections',[669],
'A countable family of closed subsets containing every closed integral subscheme of dimension≤1 must cover each irreducible component by one member.',
'For a complete Noetherian local ring, reduce to a domain and use finite Cohen normalization plus a Baire section whose generic point avoids every proper member.',
'A full targeted proof is given in root_computation_notes.md, independently reviewed by streamB. R-Q27 searched the exact formal/abelian/Baire lemma without locating a precise earlier published match.',
'The source gives its Baire route but no completion reference.',
'The proof is completed for the recorded lemma; a follow-up should address only its use in the polarization argument.',[])
P(190,'Picard-zero hypotheses in generalized algebraization',[670],
'Extend the abelian argument to proper flat formal schemes under Pic0 hypotheses, corrected by smoothness or finite-flat-cover conditions in the margin.',
'Specify Pic0 representability, smoothness and the role of a polarization; distinguish projective algebraization after a cover from unpolarized algebraization.',
'EGAIII1 5.4.5 and the checked Artin1969 criteria provide conditional tools. They do not identify the whole package without its missing effectivity assumptions.',
'The margin itself strengthens the assumptions; no retrospective reason is supplied.',
'Worth a comparison table of the exact Pic0 hypotheses and each claimed implication.',['REGAIII1','RArtin1969'])
P(191,'Algebraization of pairs without infinitesimal automorphisms',[671],
'Descend or algebraize a proper flat pair(X,L) when its infinitesimal automorphisms vanish.',
'Vanishing automorphisms controls uniqueness, whereas existence still requires effectivity and any positivity used in polarized moduli.',
'Artin1969 Theorems1.6–1.7 and EGAIII1 5.4.5 have separate effectivity/ample hypotheses. The source does not explicitly assumeL ample on scan45.',
'The retained statement is incomplete; no reason for the missing hypothesis is documented.',
'Worth testing whether the intendedL was ample before pursuing the broad unpolarized form.',['RArtin1969','REGAIII1'])
P(192,'Equal-characteristic scope of the Néron/BT extension argument',[672,673],
'Extend a generic BT homomorphism into the indicated Néron group, using Tate’s theorem where generic characteristiczero is explicitly assumed.',
'Use deJong’s integrally closed Noetherian-base extension theorem for BT Hom, with the distinct original-paper erratum respected.',
'deJong ICM1998 §3 Theorem2p261 extends BT homomorphisms over an integrally closed Noetherian domain without a p-basis hypothesis; its Theorem1 about F-crystals has a different hypothesis. The full Néron-group target step is compared separately.',
'The manuscript itself flags the characteristic restriction; later literature removes specific BT restrictions, not every target ambiguity.',
'Worth tracing the exact transition from BT image to the semiabelian Néron target.',['RdeJongICM1998'])
P(193,'Good reduction for a semiabelian generic fibre',[674],
'Formulate the desired good-reduction condition for a semiabelian generic fibre and its BT data.',
'Distinguish extension as an abelian scheme, extension as a semiabelian scheme, and existence of a Néron model.',
'deJong ICM1998 §3 Theorem3 records the abelian good-reduction and semistable BT comparison, referring to SGA7I IX5.10. It does not make the undefined semiabelian phrase on scan51 a single theorem.',
'The page explicitly leaves the meaning to be fixed.',
'Worth a short definitions task before a theorem search.',['RdeJongICM1998','RSGA7I'])
P(194,'The semiabelian image of a divisible group',[675,676],
'Factor a BT homomorphism through a semiabelian subgroup, using stabilization of p^νG in characteristicp and a separate characteristiczero argument.',
'Retain the commutative finite-type image and no-Ga assumptions and distinguish schematic image from the image on geometric points.',
'R-Q31 searched the exact image-factorization statement and the Néron extension references. Standard no-Ga facts for semiabelian varieties support the application, but no exact opened source was located for every relative variant on scans52–53.',
'The annotation is a proposed generalization of the attributed Raynaud theorem; no historical reason for stopping is given.',
'Worth checking one characteristic at a time with the image functor fixed.',['RdeJongICM1998','RSGA7I'])
P(195,'The proposed non-Noetherian openness correction',[683,684,685],
'Remove the Noetherian hypothesis using generalizations and finite presentation, and simplify the conormal proof by the regular-sequence basis argument.',
'Keep the two edits separate: the final conormal proof contains the basis argument; the published openness proposition still inherits local Noetherianity.',
'EGAIV4 19.1.5pp186–187 and EGAIV3 15.6.3p237 were read directly. Detached scan12 errata remain unattributed.',
'The letter asks for changes; no acceptance/rejection record for the stronger openness proposal was found.',
'Worth a precise later-edition/correspondence search for that one proposed strengthening.',['REGAIV3','REGAIV4'])
P(196,'Mumford’s geometric-reductivity conjecture',[679],
'The reused GIT preface asks geometric reductivity, including its p-power symmetric formulation.',
'This is Haboush’s theorem; the p-power refinement follows from the coefficient argument recorded here.',
'Haboush1975 is the solution; Sastry–Seshadri2011p415 gives a checked primary statement and alternative proof. The preface is dated27October1963, distinct from book publication1965.',
'This was Mumford’s published problem, not an undeveloped personal Grothendieck conjecture.',
'No new proof project is needed; its value here is correct attribution and chronology.',['RHaboush1975','RSastrySeshadri2011','RMumfordGIT'])
P(197,'Rational optimal destabilization',[680],
'The GIT discussion asks for rational instability data.',
'For perfectk, k-rational unstablev and a Galois-invariant length, use Kempf’s optimal parabolic and rational cocharacters; imperfect fields require extra hypotheses.',
'The original Kempf preprint, circulated by fall1976 and digitized2018, Theorems6–7pp7–9, and Bate–Martin–Röhrle–Tange2013 Remark4.10 and Remark5.10 were checked.',
'The supplied text predates the checked solution; its presence in this folder does not establish a separate Grothendieck formulation.',
'Worth only an exact field-hypothesis comparison if reused elsewhere.',['RKempf1978','RKempf1976','RBate2013'])
P(198,'The building-centre formulation in the preface',[681,695],
'A finite isometry group of a convex set in the flag building is said to have a fixed point.',
'For a convex subcomplex of the appropriate spherical building, retain the alternative that it is a subbuilding; otherwise the stabilizing automorphisms have a fixed point.',
'The literal sentence is refuted here byQ8 on the whole rank-one SL2(C) building. Ramos-Cuevas2013 Conjecture1.1/Theorem1.2 and corollaries supply the modern qualified result.',
'The preface supplies an informal claim; no source explains the omitted alternative.',
'The literal issue is settled by the counterexample; the useful task is editorial clarification.',['RRamosCuevas2013'])
P(199,'The surface-moduli hope in the GIT preface',[682],
'Develop stability and moduli for algebraic surfaces.',
'Choose a surface class, polarization, singularity convention and moduli functor before posing a modern theorem.',
'R-Q33 searched the preface and its invariant-theory successors. The retained broad hope has no uniquely matchable quantifiers, so no later surface-moduli theorem is assigned as its exact solution.',
'The preface presents a programme, not a stopped proof; no reason for abandonment is supplied.',
'Worth only after narrowing the moduli problem; it is too broad for one research run.',['RMumfordGIT'])
P(200,'Illusie’s proposed Riemann–Roch/Künneth appendix',[686],
'The24February1968 letter proposes editorial work on a Riemann–Roch appendix and Künneth material.',
'Identify the intended version and correspondence before attributing a mathematical theorem to the letter.',
'R-Q35 searched the date, author, appendix and Künneth wording; the supplied letter is primary evidence, and the opened CSG catalogue verifies its exact author/date/cote. The outcome of the proposed editorial work was not located.',
'The letter records planned work; no outcome or reason for a change of plan is present.',
'Worth a bounded bibliographic identification task, not a new theorem project.',['RIllusieLetter1968'])

next(x for x in b.problems if x['id']=='MP-SA04-168').update({'as_he_states':'Over integral finite-typeS dominatingSpecZ, if every closed reduction of an abelian section has a Verschiebung lift, must the section be torsion?','plausible_today':'The literal implication is false even for rational lifts at every closed point. Any surviving arithmetic criterion must retain stronger information, for example the connection/vector-extension data discarded by this projection.','state_of_art':'C-SA04-702 supplies a complete counterexample withS=SpecZ[1/30], E:y²=x³−2x andP=(2,2). Rössler2020 Theorem1.4 instead concerns infinite compatible divisibility in fixed characteristic modulo the constant trace.','why_open':'The manuscript asks the question without a proof. The audit’s counterexample resolves its literal formulation; the sources do not state why the author did not pursue it.','worth':'The literal question is settled negatively here; a new task should identify the extra data needed for the adjacent stronger arithmetic formulation.','refs':['RRoessler2020','BMilne2021Supplement','BChaiOort2009Supplement']})
next(x for x in b.problems if x['id']=='MP-SA04-192')['state_of_art']='The original SGA7I IX5.9/5.9.1pp382–383 gives the exact Néronian-target extension assertion with Raynaud attribution;5.11p386 states that removing the generic characteristiczero restriction follows from unrestricted Tate full faithfulness. deJong ICM1998 §3Theorem2p261 and the1998 article, with1999erratum, supply that input. The unpublished general Néron construction/representability dependencies are identified, not independently reproved.'
next(x for x in b.problems if x['id']=='MP-SA04-192')['refs']=['RSGA7I','RdeJongICM1998']
b.events.append(['C-SA04-644',b.DAY,b.WHO,"refuted, with the refined statement's id",'Refined statement C-SA04-702: independently checked exact source hypotheses and the complete residue-field-rational counterexample; see parts/b/root_supplement_proofs.md.'])

# Reading alarms: all remain undecided on ink; no diplomatic source is edited.
R=b.R
for row in [
(93,8,'codex/K93-10_transcription.tex:208','−F(r,t)−sF_y(r,t)','−F_x(r,t)−sF_y(r,t)','Coefficient substitution and degree give the derivative; see C-SA04-601.'),
(93,17,'codex/K93-11_transcription.tex:ordinary normal form','a2x in the ordinary characteristic2 normal form','a2x²','The previously defined normal form and the coefficient transformation require the quadratic term; C-SA04-723.'),
(93,14,'codex/K93-10_transcription.tex:Proposition6.1 proof','reference(6.2)','check reference to the preceding normal-form equation','The referenced normalization occurs earlier; an equation-number error is possible.'),
(93,5,'codex/K93-10_transcription.tex:duality paragraph','cohomological degree in Rp!','check R^−1 versus R^1 and the duality shift convention','Genus-one duality fixes a shift only after the author’s convention is identified; C-SA04-725.'),
(93,32,'codex/K93-12_transcription.tex:8','norm of θ(y)=Σα_i t_i(y)','norm of θ(y)−Σα_i t_i(y)','The next inequality applies the bounded operator to the difference; equality inside the norm is syntactically and mathematically inconsistent.'),
(93,36,'codex/K93-12_transcription.tex:113;122–125','coefficient3 in the intermediate exponential-Schwarzian expression','coefficient1, as in the final expression','Exact symbolic differentiation gives G(expf)=G(f)+(f′)². The final line already corrects it; C-SA04-609.'),
(93,137,'codex/K93-01_transcription.tex:149','H0(T)=0 followed by dimension3','check Ω-versus-T or the genus qualification','OnP1, h0(T)=3; the following dimension is incompatible with the displayed vanishing.'),
(93,146,'codex/K93-01_transcription.tex:468','Z1=ker(d2)','Z1=ker(d1), if d1 denotes the differential out of degree1','Degree bookkeeping in the displayed de Rham complex.'),
(93,146,'codex/K93-01_transcription.tex:482','O as acting module','E','The construction is anE-torsor, and its translations take values inE.'),
(93,150,'codex/K93-01_transcription.tex:624','unfinished quotient after the infinitesimal neighborhood symbol','retrieve the omitted quotient from the scan','The order of the principal-parts neighborhood is needed to type the descent map; no specific missing text is supplied.'),
(93,151,'codex/K93-02_transcription.tex:23','stratification onE in the torsor conclusion','stratification onP','E already carries the fixed linear stratification; the new construction acts on its affine torsorP.'),
(93,153,'codex/K93-02_transcription.tex:69','d_E applied to the affine section','d_P','The affine section is not a section of the linear bundle; compare the consistent signs at lines55/63.'),
(93,160,'codex/K93-02_transcription.tex:final factorization','domain ofΔ′ appearsΩ1','Ω2 in this factorization','The intervening differential is d:Ω1→Ω2, so the next operator must start in degree2.'),
(93,163,'codex/K93-02_transcription.tex:Gauss–Manin spectral sequence','d1 target indexedp−1','p+1','The filtration differential and the next displayed equations increase the first degree.'),
(93,165,'codex/K93-03_transcription.tex:base differential expression','Ω_X/S in the base connection term','Ω_S/T','The Gauss–Manin connection is a connection onS overT, so its base one-forms come fromS/T.'),
(93,170,'codex/K93-03_transcription.tex:Cartier canonical map','a natural map to closed formsZ','a natural map to cohomologyH=Z/B','In characteristic2, (x+y)d(x+y)−x dx−y dy=d(xy)≠0. C-SA04-625 is refuted as a literal functorialZ-valued claim; ink could instead sayH.'),
(93,171,'codex/K93-03_transcription.tex:Cartier splitting','canonical splittingZ=B⊕H','splitting relative to the chosenp-basis','The monomial representatives depend on thep-basis; the cohomology isomorphism is canonical.'),
(93,172,'codex/K93-03_transcription.tex:Cartier axioms','C(dω)=0 forω∈Z','all appropriate formsω','Withω already closed, dω=0 and the axiom says nothing; the uniqueness argument needs exact forms from the preceding degree.'),
(93,175,'codex/K93-03_transcription.tex:p-curvature tensor target','ordinary tensor powerΩ^{⊗p}','Frobenius pullbackF*Ω','p-linearity does not makev↦v^{⊗p} additive in rank>1; compare source scan215 and streamB’s independent check.'),
(93,183,'codex/K93-04_transcription.tex:170','f dg+g df=d(fg)=0','C(d(fg))=0','An exact differential need not be zero; Cartier annihilates it, which suffices for the pairing.'),
(93,183,'codex/K93-04_transcription.tex:176–177','nonzero wheni+j=p−1','i+j=p','The exponenti+j−1 must bep−1; both the drawn matrix and direct computation agree.'),
(93,184,'codex/K93-04_transcription.tex:determinant paragraph','determinant+1','retain the sign from the chosen basis/normalization','Forp=5 the displayed antidiagonal pairing has determinant−1; C-SA04-633/634 distinguish determinant and Pfaffian.'),
(93,184,'codex/K93-04_transcription.tex:imperfect-field conic paragraph','every imperfect characteristic2 field admits a pointless smooth conic','an additional field hypothesis, or a particular imperfect field','A separably closed imperfect field has a rational point on every smooth conic; C-SA04-635/636. Mathematics does not identify a specific missing word.'),
(93,198,'codex/K93-05_transcription.tex:106','lifts via Verschiebung','a k(s)-rational lift, if the intended condition is nonvacuous','As an fppf lifting condition any isogeny is surjective; even the rational-lift interpretation has the counterexample in streamB’s supplement.'),
(93,204,'codex/K93-05_transcription.tex:245','multiplicity of the root1 equals rationalp-torsion dimension','dimension ofker(F−1), with semisimplicity if replacing it by multiplicity','The saved genus-two example overF2 has multiplicity2 but rational2-torsion dimension1; C-SA04-647/648.'),
(93,212,'codex/K93-06_transcription.tex:182–185','kernel labelledPcip','Pcin','The target records the reduced p-curvature, so nilpotent p-curvature is in the kernel; streamB supplies a square-zero-base counterexample.'),
(100,3,'pro/MPL_8_079-081+9+4+100_transcription.tex:1352','comparison written as a morphism without an explicit isomorphism mark','check the intended isomorphism between the two BT restrictions','The fibre-product category of gluing data requires an isomorphism, not an arbitrary comparison map.'),
(100,9,'pro/MPL_8_079-081+9+4+100_transcription.tex:1450','base symbols in the comparison diagram','check the common base before identifying the BT restrictions','The descent comparison is only typed after both terms are pulled to the same base; no replacement is asserted on ink.'),
(100,34,'pro/MPL_8_079-081+9+4+100_transcription.tex:2144;codex/K100-03_transcription.tex:162','every finite isometry group of a convex building set has a fixed point','an additional condition or the subbuilding alternative','Q8 on the whole rank-one building is a counterexample. This may be an imprecise printed formulation, not a transcription error; C-SA04-681/695.')
]: R(*row)

# Links whose source endpoints were read. Project leads remain in the agents’
# separate kind="our projects" rows; these rows assert no unseen project result.
def L(kind,a,z,what,evidence,ids=''): b.links.append([kind,a,z,what,evidence,ids])
L('folder','cote93 scans179–181, C-SA04-630/631','cote93 scans206–213, C-SA04-649/650','Cartier/Frobenius duality feeds the Picard-with-connection construction','Both source passages were read; the second requires the proper smooth/Picard representability hypotheses.','SA04-623;SA04-634')
L('folder','cote93 scans194–198, C-SA04-641/643/644','cote93 scans206–217, C-SA04-649/651','Universal vector extensions link arithmetic flat-line questions with Picard connections','The actual common object is the vector extension of the dual abelian scheme; the torsion question after projection is weaker.','SA04-629;SA04-630;SA04-631;SA04-634;SA04-635')
L('folder','cote100 scans3–5/21, C-SA04-655/657','cote100 scans48–53, C-SA04-672/675','Abelian/BT extension and the attributed Raynaud Néron theorem','Both manuscript and typescript endpoints were checked; no chronology of their physical juxtaposition is inferred.','SA04-639;SA04-641;SA04-654;SA04-655')
L('published work','cote100 scans4/21, C-SA04-657','Groth1966 Proposition1.2p64;§2.1p67','Algebraicity of a BT homomorphism','Opened primarypp63–67; Proposition1.2 is an associated-point criterion and§2.1 has reduced characteristiczero finite-type hypotheses.','SA04-641')
L('published work','cote100 scans3/7–15, C-SA04-656','Groth1966 §4.9pp77–78','The normal-base extension question is explicitly published as a question','Primary§4.9 read directly; later normal-base answer is RKP2021 Cor6.12, not proof of all nonnormal variants.','SA04-640')
L('published work','cote100 scans31–39, C-SA04-665/668','EGAIII1 5.4.1,5.4.5–6pp154–159','Formal algebraization, ample criterion and reduced-base question','The primary text distinguishes full faithfulness, ample algebraization and an open general question.','SA04-647;SA04-650')
L('published work','cote100 scans40/42/44/46, C-SA04-683','EGAIV4 19.1.5pp186–187','Conormal basis proof','The final published proof contains the regular-sequence basis argument suggested in the letter.','SA04-659')
L('published work','cote100 scans40/42/44/46, C-SA04-684','EGAIV3 15.6.3p237','Proposed removal of Noetherianity','The published theorem still inherits locally Noetherianity; this is a verified difference, not an accepted-correction claim.','SA04-659')
L('published work','cote93 scans142–153, C-SA04-613/615','EGAIV4 16.7.1–7pp36–38','Principal parts and differential operators','Exact published definitions and universal property checked; the broader Ω-flat stratification claim remains separately qualified.','SA04-612;SA04-614')
L('folder','cote93 scan159, C-SA04-620','cote93 scans222–233, C-SA04-402–418; Pro lines31–315','The horizontal-lift/Picard–Fuchs comparison belongs to the same Gauss–Manin construction','Both streams read their source passages; streamC verified the second endpoint as cote93, not the distinct cote161-5. The scan159 identity was independently proved by streamC and root. This is an audit link, not an explicit manuscript cross-reference.','SA04-617;SA04-408;SA04-419;SA04-420;SA04-423;SA04-424')

for n in [601,603,604,609,624,628,632,647,678,690,720,723,724]:
 b.events.append([f'C-SA04-{n}',b.DAY,b.WHO,'computation or formal certificate','Exact saved program/output checked. Scope and distinction between finite tests and universal proof are in root_computation_notes.md.'])
for n in [611,613,614,616,620,624,628,634,636,648,668,669,678,679,695]:
 b.events.append([f'C-SA04-{n}',b.DAY,b.WHO,'targeted proof check','Written proof with hypotheses is in root_computation_notes.md; independent reviews and finite certificates are separately attributed.'])
for n,refined in [(625,624),(633,634),(635,636),(647,648),(681,695)]:
 b.events.append([f'C-SA04-{n}',b.DAY,b.WHO,'refuted, with the refined statement\'s id',f'Literal statement refuted with every hypothesis checked in root_computation_notes.md; corrected/refined record C-SA04-{refined}. No ink decision is made.'])

# Final clerical source-locator consistency. This reads page markers only and
# never assigns a verdict, mathematical status, or literature assessment.
for x in [item(628),claim(639),claim(640)]:
 x['lines']=list(x['lines'])+['codex/K93-05_transcription.tex:3–9']
import re
source_cache={}
for x in b.items+b.claims:
 actual=[]
 for locator in x['lines']:
  m=re.fullmatch(r'([^:]+):(\d+)(?:[–-](\d+))?',locator)
  if not m:continue
  file,a,z=m[1],int(m[2]),int(m[3] or m[2])
  if file not in source_cache:
   lines=(b.ROOT/'source/SA04_texts'/file).read_text().splitlines()
   marks=[];cote=None;scan=None
   for number,line in enumerate(lines,1):
    mc=re.search(r'\\cotefile\{([^}]+)\}',line)
    ms=re.search(r'\\scanpage\{(\d+)\}',line)
    if mc:cote=mc[1]
    if ms:scan=int(ms[1])
    marks.append((cote,scan))
   source_cache[file]=marks
  for cote,scan in source_cache[file][a-1:z]:
   if cote==x['cote'] and scan is not None:actual.append(scan)
 if actual:x['scans']=sorted(set(actual))
for p in b.problems:
 for occurrence in p['occurrences']:
  if 'claim' in occurrence:
   c=next(x for x in b.claims if x['id']==occurrence['claim'])
   for field in ['cote','scans','lines']:occurrence[field]=c[field]
next(x for x in b.problems if x['id']=='MP-SA04-194').update({'state_of_art':'The no-Ga consequence for every Néronian generic fibre is precisely BLR1990 §10.1 Proposition8 pp293–294 and is independently proved here. SGA7I IX5.9.1 gives the broad target theorem. The image-factorization and unpublished construction/representability inputs remain separate; their complete relative variants are not all independently reproved.','refs':['RBLR1990','RSGA7I','RdeJongICM1998']})
import csv
for patch in csv.DictReader((b.ROOT/'SA04_work/parts/b/root_reading_locator_patch.tsv').open(),delimiter='\t'):
 rows=[x for x in b.readings if x[0]==patch['cote'] and x[1]==patch['scan'] and x[2]==patch['old_line']]
 assert len(rows)==1,patch
 rows[0][2]=patch['new_line']
b.events.append(['C-SA04-676',b.DAY,b.WHO,'independent re-proof','Lie-lattice proof from the Néron mapping property written in root_computation_notes.md, with every DVR and tangent-space hypothesis explicit. The opened BLR10.1/8 statement and proof are a separate exact literature match.'])
b.events.append(['C-SA04-641',b.DAY,b.WHO,'used and rechecked in this run','Fresh current-state queries and opened IAS announcement/Litt problem page distinguish October2025 public announcement from January2026 arXiv posting, and retain the general conjecture’s open status with precise special-case boundaries.'])

if __name__=='__main__': b.save()
