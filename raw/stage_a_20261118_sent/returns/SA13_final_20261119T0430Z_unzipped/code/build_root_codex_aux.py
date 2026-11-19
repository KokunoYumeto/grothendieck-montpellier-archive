"""Manually authored auxiliary index for K34-09..12; serialization only."""
from pathlib import Path
import json,csv
R=Path(__file__).resolve().parents[2];O=R/'deliverable/shards/root_codex'
claims=json.loads((O/'claims.json').read_text());by={int(c['id'].split('-')[-1]):c for c in claims}
def tsv(name,fields,rows):
 with (O/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
items=[]
def I(n,cs,kind,words,statement,reconstruction):
 cc=[by[x] for x in cs];loc=[]
 for c in cc:
  for x in c['lines']:
   if x not in loc:loc.append(x)
 sources=sorted({x['file'].replace('_transcription.tex','') for x in loc})
 items.append(dict(id=f'SA13-{n}',sources=sources,kind=kind,cote=[34],scans=sorted({s for c in cc for s in c['scans']}),lines=loc,his_words=words,statement=statement,reconstruction=reconstruction,check='agrees',check_reason='Full Codex passage and the short lead note read. This is an unindexed Codex supplement; no Pro verdict row is added. Individual mathematical qualifications and refutations are in the linked claims.'))
 for c in cc:c['items'].append(f'SA13-{n}')
I(62,range(600,609),'self-flagged step','Donner démonstrations! Cette condition est peut-être inutile.',
 'Local Lefschetz/depth induction, the rewritten5.3, two geometric-depth lemmas, and the conjectural nonabelian/general-base extensions.',
 'Geometric depth follows SGA2 XIV5.3, not ordinary depth. The deleted dimension loss and standing purity assumptions are not repaired silently.')
I(63,range(609,614),'self-flagged step','À des signes et shifts près; Compatibilité b) laissée ...',
 'The punctured-local-space and nearby-cycle cone diagrams, their purity and inertia-cohomology computations, and the explicitly deferred compatibility.',
 'The modern RΦ convention is translated by one. Tate twists and signs are separated from scan readings.')
I(64,range(614,627),'unproved claim','Nous allons admettre pour l’instant le lemme-clef suivant.',
 'Prime-to-p fundamental-group monodromy: tame reduction, fixed paths, nodal curves, deformation parameters and the node-thickness product.',
 'The surviving theorem matches SGA7 I5; the fixed-square Bertini remark and imperfect-residue query remain separate historical questions.')
I(65,range(627,642),'self-flagged step','réf?; laisser tomber remarques6.7 et6.8.',
 'Analytic and algebraic envelopes of profinite groups, differentiated representation categories, connected algebraic envelopes and their comparison.',
 'The supplied counterexample to rational components concerns the general sentence, while actual image closures are dense by definition. Editorially dropped remarks are not treated as live conjectures.')
I(66,range(642,651),'unproved claim','En fait, on verra que ces dimensions sont toujours infinies.',
 'The arithmetic model pro-group, its distinction from ordinary π1, finite-presentation descent and the dimensions of its analytic and algebraic Lie objects.',
 'The analytic infinity parenthesis is refuted by Spec(Fbar_p), with the algebraic infinity assertion retained and proved separately.')
I(67,range(651,654),'conjecture','Une des conséquences des conjectures de Tate ... bijectif.',
 'The Tate-module endomorphism problem formulated using arithmetic model representations and their analytic/algebraic centralizers.',
 'The modern answer uses Tate–Zarhin–Mori–Faltings over finitely generated fields and normal-base extension, followed by descent. It does not use ordinary geometric π1 in place of the model pro-group.')
I(68,range(654,664),'self-flagged step','via conjectures standard; compatibilité à vérifier...',
 'Weights for normal-crossing divisors, compactifications and generic fibres; degeneration, motivic differentials and ell-independence expectations.',
 'Finite-field hypotheses are supplied for Frobenius weights. E2/E3 and Rj*/RΨ are kept distinct. The invariant/coinvariant purity sentence is refuted, not silently converted into weight–monodromy.')
I(69,range(664,671),'other','Theorem2.1; Proposition2.3; Proposition2.4.',
 'Printed English GIT sheets: numerical weights, one-parameter subgroup criteria, valuative/Iwahori argument and invariant affine charts.',
 'The reused source is identified with the GIT source family; no authorship by Grothendieck is inferred from the reverse-side manuscript. The missing nontrivial qualification needs the scan/standing definition.')
(O/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
(O/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')

problems=[]
def P(n,title,cs,as_he,plausible,art,why,worth,refs):
 occ=[]
 for k in cs:
  for x in by[k]['lines']:
   if x not in occ:occ.append(x)
 problems.append(dict(id=f'MP-SA13-{n:02}',title=title,occurrences=occ,as_he_states=as_he,plausible_today=plausible,state_of_art=art,why_open=why,worth=worth,refs=refs,claims=[by[k]['id'] for k in cs]))
P(190,'Geometric depth under localization',[603],
 'Supply the proof of5.3.3(i), profgeom(A_p)≥profgeom(A)−dim(A/p).',
 'Keep the invariant defined by a complete regular presentation and its minimal relation count; first establish the excellent/complete and lci cases before expanding quantifiers.',
 'SGA2 XIV5.3–5.6 defines the invariant and proves its étale comparison in characteristic zero; Illusie2003 §1–2 gives relative-depth results over fields and traits. No exact all-noetherian theorem matching this short lemma was located.',
 'The manuscript says to give proofs; no source explains why this lemma was not expanded on the sheet.',
 'Worth a focused proof-and-hypothesis task because it controls several later dimension bounds.', ['RC_SGA2','RC_Illusie2003'])
P(191,'Flat-map geometric depth and the residue hypothesis',[604],
 'Prove5.3.3(ii), and decide whether the formally smooth residue-field realization condition is unnecessary.',
 'Formulate the exact inequality for flat local noetherian maps using Cohen factorizations, retaining any separability/completion hypotheses actually needed.',
 'SGA2 XIV5.5 treats flat local maps with separable residue-field fibre; Illusie2003 supplies the finite-type relative setting. The unrestricted removal in this draft was not matched exactly.',
 'The writer explicitly doubts the extra condition and leaves both demonstrations for later.',
 'Worth one bounded commutative-algebra audit; the finite-type case alone must not be sold as the full answer.', ['RC_SGA2','RC_Illusie2003'])
P(192,'Nonabelian local Lefschetz specialization',[607],
 'Replace the lci hypothesis by geometric depth≥3 and obtain low-degree noncommutative specialization.',
 'Use prime-to-residue-characteristic ind-finite torsors and the precise depth and base assumptions of the local Lefschetz theorem.',
 'Raynaud1974 III1.2–1.3 gives the checked comparison; Orgogozo2003 §3–4 removes resolution assumptions for several generic prime-to-p results. The SGA2 XIV6.2 editorial note points to Raynaud; it is not a licence to erase all hypotheses in6.3.',
 'The sheet explicitly makes the extension conditional on SGA2 XIV6.3; its printed reference is misnumbered SGA1.',
 'Worth a precise theorem concordance, with no assumption that the broadest excellent-base reading remains open.', ['RC_MRaynaud1974','RC_Orgogozo2003','RC_SGA2'])
P(193,'Acyclicity from singular-locus dimension over a local base',[608],
 'For excellent flat local A→B, predict local(m−d−1)-acyclicity and a degree-one nonabelian analogue.',
 'Separate the trait lci theorem from the higher-dimensional-base formulation, specifying geometric singular loci after residue extensions and prime-to-p coefficients.',
 'SGA7 I4.5–4.8 and Illusie2003 establish the trait depth/lci range; Raynaud1974 and Orgogozo2003 give the cited nonabelian subcases. Full quantifier identity was not established.',
 'Resolution and local Lefschetz input are explicitly proposed, not supplied.',
 'Worth an exact-scope historical audit before posing any new research problem.', ['RC_SGA7I','RC_Illusie2003','RC_MRaynaud1974','RC_Orgogozo2003'])
P(194,'Signs and deferred compatibility in the local cone diagram',[609,610,611,612,613],
 'Extract and explain the diagram, settle the sign ofβ, and verify compatibility6.4(b).',
 'Choose one cone convention and construct the localization/nearby-cycle square as a coherent derived diagram, retaining Λ(−1)[−2] purity and the inertia Tate twist.',
 'The SGA7 formalism and Illusie2003 §3–4 supply the published variation/cross framework; the run checks the forced degrees but does not settle unread ink or claim to re-prove all coherent compatibilities.',
 'The source explicitly leaves part(b) to the redactor and marks the sign.',
 'High value for one short companion task: a single fully typed diagram can resolve several reading alarms.', ['RC_SGA7I','RC_Illusie2003','RC_Illusie2021'])
P(195,'Stable marked models and the residue-field question',[621,624],
 'Use a nontrivial model theorem to be proved later; ask whether the residue field must be perfect.',
 'Use stable marked reduction after a finite extension under the actual trait hypotheses, and distinguish the proof’s reduction of residue fields from the theorem’s statement.',
 'SGA7 I5.1.1,5.3.2 and5.4 give the checked published route, with the deformation input credited to RimVI/Schlessinger.',
 'The text explicitly defers an exposé and has an empty citation; no evidence of abandonment is supplied.',
 'Worth a bounded historical cross-reference task, since the principal tame-monodromy conclusion is already established.', ['RC_SGA7I'])
P(196,'A fixed square in Bertini with a prescribed section',[622],
 'The marginal suggestion is that the square should suffice in the hyperplane reduction.',
 'A correct sufficient-large-power theorem with prescribed section and boundary transversality; any uniform exponent2 needs its own hypotheses or counterexample.',
 'SGA7 I5.5 states the generic-section reduction; Orgogozo2003 Th4.10 gives a prime-to-p Lefschetz theorem. Neither verifies this exact exponent2 proposal.',
 'The source says to explain more and points to EGA V, which is not a published volume.',
 'Potentially useful as a small sharp-bound audit, after the line bundle and embedding assumptions are recovered from the scan.', ['RC_SGA7I','RC_Orgogozo2003'])
P(197,'Reference for compact analytic linearity',[636],
 'A margin asks for a reference to faithful linear representations of compact Qell-analytic groups.',
 'Every such compact group is linear over Qell, using local Ado integration and finite-index induction.',
 'Lazard1965 is the earlier theory; Casals-Ruiz–Zozaya2025 Th2.1 supplies a checked primary proof and degree bound for uniform groups plus induction.',
 'The question is bibliographical, not evidence that the author doubted or invented the theorem.',
 'Resolve in commentary with an exact citation; it does not warrant a new research project.', ['RC_Lazard1965','RC_CasalsZozaya2025'])
P(198,'Analytic and algebraic envelope comparison',[631,637,638],
 'The page asks when the analytic and algebraic objects agree and leaves an exceptional-case speculation.',
 'Separate equality of analytic Lie algebras, openness in a Zariski closure, full rational-point groups, and reconstruction with a fibre functor.',
 'Deligne–Milne2.8–2.11 proves the reconstruction; local Lie theory proves the openness criterion. The tentative unqualified progroup-isomorphism assertion is not identifiable as a settled theorem in that wording.',
 'The writer marks a question and then drops two subsequent remarks; no later source is used to infer a motive.',
 'Worth a concise counterexample table and notation audit, not an invented classification theorem.', ['RC_DeligneMilne1982','RC_Lazard1965'])
P(199,'The deferred infinite-dimension claim',[647,648],
 'The source promises that both analytic and algebraic dimensions are always infinite.',
 'Algebraic quotient dimensions are unbounded for the procyclic arithmetic example, but analytic Lie dimension can be1.',
 'The complete Spec(Fbar_p) counterexample and exponential-character proof are supplied in this run; their ingredients are p-adic Lie theory and neutral Tannakian reconstruction.',
 'The claim is deferred on195 and the continuation196 proves only the algebraic side; no textual retraction is present.',
 'Worth recording as a resolved correction and a pedagogical example, not pursuing as an open conjecture.', ['RC_DeligneMilne1982','RC_Lazard1965'])
P(200,'Arithmetic descent of geometric local systems and fixed quotients',[650,653],
 'The source expects the local systems and homomorphisms met in geometry to descend, and hopes to realize a useful fixed quotient at one model.',
 'A proper smooth finite-presentation family and finitely many algebraic maps/correspondences descend to some model; arbitrary lisse ell-adic systems need not.',
 'Stacks01ZM with finite/étale descent gives finite-presentation descent; centralizers at a fixed representation stabilize after the finite component issue is removed. No theorem quantifying over “everything met in practice” is inferred.',
 'This is a methodological hope in6.16–6.17, not an explicit arbitrary-local-system conjecture.',
 'Useful for explaining the manuscript’s arithmetic model category with one concrete family.', ['RC_StacksLimits','RC_StacksFundamental','RC_DeligneMilne1982'])
P(201,'Tate endomorphisms for the arithmetic model pro-group',[652],
 'End(A)⊗Qell should equal the commutant of the arithmetic pro-group for normal integral X.',
 'Keep the model category, ell invertibility and normal-base hypotheses; after descent the equality is the Tate homomorphism theorem.',
 'Gajda–Petersen2022/2023 Th2.3 states the all-finitely-generated-field theorem and Lemma3.4 the normal-base extension. Zarhin2010/2011 identifies the Tate1966, Zarhin1975–76, Faltings1983–84 and Mori1985 characteristic-specific history.',
 'The manuscript already knows Tate’s finite-field case. The sources establish the later cases; they do not explain this appendix’s editorial fate.',
 'Worth a historical completion note, not a surviving instance of the general Tate conjecture.', ['RC_GajdaPetersen2022','RC_Zarhin2011','RC_Tate1966','RC_Faltings1983'])
P(202,'Ell-independence of the normal-crossing weight complexes',[655,662],
 'Under the standard conjectures, dimensions and Frobenius polynomials of the specified weight pieces should be independent ofell.',
 'Identify the exact restriction/Gysin complex and rank statement; prove a selected case using a known realization or a verified standard-conjecture hypothesis.',
 'WeilII proves purity and weight degeneration. Van Dobben de Bruyn2020 Theorem1,p3 proves the exact equivalence over Fbar_p between homological-equivalence independence, ranks of algebraic correspondences and compact-support Betti independence for all separated finite-type schemes. His introduction pp2–3 treats this SNC/hypercover argument. The equivalent assertions remain conjectural; Wan–Zhang §1.1,p2 confirms the general open scope.',
 'The source explicitly writes the standard-conjecture condition and the unchecked d2 identification.',
 'High interest, but a short run should produce a precise reduction and known-case map rather than announce a solution of a standard conjecture.', ['RC_WeilII1980','RC_vanDobben2020','RC_WanZhang2025'])
P(203,'Duality and motivic identification of d2',[659,660,661,662],
 'The page tentatively compares the two complexes and leaves compatibility of the motivic d2 maps to check.',
 'With one indexing convention, show that restriction and Gysin maps give the claimed d2 and duality signs; terminal graded terms areE3.',
 'The normal-crossing Kummer calculation and Weil purity justify the page bound, while SGA7/Illusie provide the nearby-cycle framework. The exact handwritten compatibility still needs a typed coherent diagram.',
 'The verification is explicitly postponed; no claim of a failed proof is inferred.',
 'High value for one research run because it is a finite comparison of named maps and signs.', ['RC_SGA7I','RC_WeilII1980','RC_Illusie2021'])
P(204,'Purity of inertia invariants and coinvariants',[663],
 'The displayed conclusion suggests both are pure of the cohomological weight.',
 'Replace the false invariant/coinvariant assertion by the accurately formulated monodromy-weight filtration statement in an identified geometric class.',
 'The split Tate elliptic curve refutes the literal claim. Illusie2021 §6 reviews weight–monodromy; Ito–Zou’s author preprint dated2026-10-06 proves the hyper-Kähler case, not the general conjecture.',
 'The source makes the conclusion conditional on its preceding construction; the counterexample shows that the condition cannot justify this literal consequence.',
 'Worth a precise correction and example; do not promote the false sentence into a new open problem.', ['RC_Illusie2021','RC_ItoZou2026'])
P(205,'GIT reduction references marked with questions',[666,670],
 'Pencil questions surround the reductions to projective space/orbit closure and the circled1.14 citations.',
 'Collate the exact edition’s restriction-of-linearization and stability theorem, preserving the nontrivial1-PS condition and sign convention.',
 'Mumford’s GIT §1–2 is the checked source family; edition-specific numbering and the stronger later reductivity terminology must be distinguished.',
 'The annotations query a printed proof, not an original theorem of Grothendieck; no authored resolution is supplied.',
 'Worth a brief source collation with the scan; no new invariant-theory program follows.', ['RC_MumfordGIT'])
(O/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')

readings=[]
pages=[p for p in json.loads((R/'work/pages.json').read_text()) if p['file'] in [f'codex/K34-{i:02}_transcription.tex' for i in range(9,13)]]
def Q(scan,reading,alternative,evidence,weight='high',confidence='medium'):
 p=next(x for x in pages if int(x['scan'])==scan)
 readings.append(dict(cote=34,scan=scan,line=f"{p['file']}:{p['start']}–{p['end']} (scan range; quoted passage identifies location)",reading=reading,alternative=alternative,evidence=evidence+' No scan supplied; no reading changed.',weight=weight,confidence=confidence))
Q(149,'m versus m′ in5.1 conclusion','Check consistency of the induction bound','The hypotheses and local-cohomology comparison use m′ throughout')
Q(149,'prof ét_x(X(h) missing parenthesis','Confirm ring/space and h index','The bound is required for every finite-level neighborhood, not a single unspecified X')
Q(150,'local(m′±1)-acyclicity','Check sign and shifted Φ convention','Source Φ=usualRΦ[-1]; an off-by-one changes the specialization endpoint')
Q(151,'d ranges all generizations, earlier cancelled x′∈Z','Check scope of the cancellation','Using all generizations versus only the bad locus changes the numerical loss')
Q(151,'m′=profgeom*X0 with −d cancelled','Compare surviving proof on152','The proof still ends profgeom*−d=m′')
Q(151,'dim closure{x} versus closure{x′}','Check which point belongs in the rectified bound','The generic-fibre dimension formula tracks both points separately')
Q(152,'SGA1 XIV4.5','SGA2 XIV4.5','The named local Lefschetz theorem is in SGA2')
Q(152,'profgeom_x(X) in a special-fibre inequality','Check X versus X0','The subsequent flat-map step adds the base dimension1')
Q(152,'codimension ≥ or ≤ d−dimclosure{x}','Check inequality direction','The required lower depth bound uses an upper bound on codimension')
Q(153,'SGA1 XIV5.6','SGA2 XIV5.6','Geometric/étale depth comparison locator')
Q(153,'Donner démonstrations|démonstration','Confirm grammatical number only','The proof request is certain; its ending does not create a third conjecture','low')
Q(154,'Φ degree n+1','Retain source shift, compare usualRΦ degree n','K34:094,145 explicitly fixes the manuscript convention')
Q(154,'global upper bound n+d+1','Check pointwise support/depth hypothesis','A coarse support-dimension bound alone would give n+2d+1; perversity supplies the stronger bound')
Q(155,'codimension≥2 of nonsmooth locus','Identify codimension in total space or special fibre','The two interpretations differ by one in the flat trait case')
Q(155,'SGA1 XIV6.3','SGA2 XIV6.3','The named homotopical-depth conjecture is inSGA2')
Q(156,'m−d±1 local acyclicity','Check the sign against5.2 andΦshift','The threshold changes the nonabelian degree-one assertion')
Q(158,'RΓ(I,Λ)=Λ⊕Λ[-1]','Λ⊕Λ(−1)[−1], or explicitly chosen tame generator','Frobenius acts on the tame generator cyclotomically')
Q(158,'6.2.6 shifts and arrow direction','Check cone convention and source/target','Four-space reconstruction uses derived invariants, not an arbitrary rotation')
Q(159,'β and signe?','Fix sign only after inspecting the actual convention','The page itself marks this compatibility as unresolved')
Q(160,'compatibility b left to redacteur(s)','Keep as deferred, not proved by surrounding sketch','Part(a) andpart(b) have different page status')
Q(161,'H^{i−1}_I without twist','Coinvariants(−1) inH¹(I,−)','Tame inertia isZell(1); see the explicit two-term calculation')
Q(162,'top twist−n±1','Use−n for punctured dimn;−n−1 for punctured dimn+1','Purity supplies both dimension and twist')
Q(165,'connected X in arithmeticπ1sequence','Check geometric connectedness','Exactness ontoG_K requires the geometric condition')
Q(166,'Aut(π) as profinite without qualification','Check finite-generation/characteristic-quotient hypothesis','The proof used here needs a cofinal characteristic finite system')
Q(168,'Aut versusAutExt in the action','Match whether a rational base-point section is present','Only the outer action is canonical without a chosen section')
Q(172,'cancelled Nous admettrons','Retain its cancellation and replacement qui est','It must not be counted as a live admitted lemma','medium')
Q(177,'le carré doit suffire','Read as tentative fixed exponent, not sufficiently high power','Generic Bertini does not automatically prove the square bound')
Q(178,'connectedness inI′→I','Check geometric fibre connectedness','Connected base and total space alone do not justify surjectivity')
Q(179,'future exposéVII on Schlessinger','Compare published RimVI, retain draft forecast','Numbering of a planned exposé is not publication numbering','medium')
Q(180,'T_i^m in the Kummer quotient','T_i^m−t_i','The literal nilpotent algebra is not étale on the complement')
Q(181,'n_i=length quotient smoothing parameter','Check a_i and localDVR notation','Pullback exponent is its valuation, hence that length')
Q(183,'continuous homomorphism is continuous','Likely second word analytic','The literal sentence is tautological; the standard theorem is automatic analyticity')
Q(183,'G/(V∩V′)','π/(V∩V′)','V,V′ are kernels inπ, not subgroups of an unspecifiedG')
Q(185,'cannot recoverπ from tensorcategory','Check sense of recover and role of fibre functor','The next page givesπalg/(πalg)0=π')
Q(187,'rational component group implies dense rational points','Check for lifting hypothesis','Normalizer of norm-oneQ3(√3)torus refutes the literal general implication')
Q(188,'G_E algebraic versus open inGtilde_E','Distinguish full group equality from Lie algebra equality','Compact analytic images can be open proper subgroups of rational points')
Q(188,'laisser tomber6.7–6.8','Preserve editorial omission instruction','This does not by itself mean the mathematics is false','medium')
Q(190,'centre versus kernel; Borel lifting H²class','Recover exact groups and coefficient action','Overwritten centres do not determine a unique extension statement')
Q(191,'crossed diagram arrows','Check vertical Lie/an/alg placements','Each arrow has a typed source and target fixed by functoriality')
Q(193,'quasi-surjective versus quasi-isomorphism','Finite-index image is the source definition','Strictness uses surjective transitionLie maps')
Q(194,'limit fully faithful','Check category of finite-type models andqcqs hypothesis','This is about pro-schemes, not blanket descent of allℓ-adic local systems')
Q(195,'both dimensions always infinite','Check if analytic dimension was actually included','Spec(Fbar_p) givesanalyticLie dimension1 andalgebraicdimensionunbounded')
Q(196,'p>0 labels in both branches, first(p=0)','Positive characteristic forF_p, characteristiczero forZ[1/ℓ]','The two displayed base schemes fix the intended case split')
Q(196,'unique moduloisom terminalquestion mark','Inspect ink before calling it a manuscript doubt','The transcription itself marks the sign uncertain','medium')
Q(198,'6.15.1 versus6.16.1','Match local numbering of endomorphismmap','The map is well-typed regardless; numbering affects cross-reference only','low')
Q(199,'π1(X)=1 implies immediateLiecentralizeratone model','Check implicit passage to a finer model','Finite component quotients vanish only eventually')
Q(200,'SGA7II|III|IV appendice','Confirm Roman numeral','Heading is not a written date or a completeexposé identification','medium')
Q(201,'d_r=0 for everyr','Forr≥2 from the displayedE2page','The d1 restriction maps need not vanish')
Q(203,'last intersection summand twist(−1)','Twist−(q−1)','Exterior powers multiply the Tate twist')
Q(205,'Il faut croire|voir','Inspect whether tentative claim or editorial instruction','No secure newproblem follows from the doubt macroalone','medium')
Q(205,'dual spectral diagram q−1 and arrows','Check totaldegree reversal and E3terminalpage','Onlyd_r≥3 vanish in the Leray/localcohomology sequence')
Q(207,'gradedpieces E2','E3 aftertakingd2 unlessd2 separatelyzero','Weight calculation permitsd2')
Q(209,'invariants andcoinvariants pureweighti','Check intended gradedmonodromy statement','SplitTateellipticH1 givesweights0 and2')
Q(209,'H^(i−1) coinvariants without twist in the inertia sequence','H^(i−1)(X_Kbar)_I(−1)','H¹(I,Q_ell)=Q_ell(−1), already for the trivial representation; independent audit in shards/p2/weights_audit.md')
Q(209,'middle cohomology field in the inertia sequence','H^i(X_Knr), after strict henselization','The quotient by inertia is the maximal unramified extension. Geometric nearby cycles instead involve Kbar; arithmetic H^i(X_K) includes the residue Galois group')
Q(209,'coinvariants inHochschild–Serre no twist','Coinvariants(−1)','This is a Frobenius-equivariant, notjustvector-space identity')
Q(204,'stable μ>0 for all1-PS','For allnontrivial1-PS, unless1-PS definitionalreadyexcludestrivial','The trivialcocharacter hasμ=0')
Q(204,'circledTheorem1.14 andpencil1.19','Collate exactGITeditionbeforealteringnumber','The annotationquestions a printedreduction; a guessednewreference isnot ink')
Q(208,'r_i inequalities andμsign','Check minimumweight andminus sign','The valuationargument requiresμ=−minsurvivingweight')
tsv('readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],readings)

links=[]
def L(kind,fr,to,what,evidence,notes=''):links.append(dict(kind=kind,**{'from':fr,'to':to},what=what,evidence=evidence,note_ids=notes))
L('folder','34:094,145','34:149–162','Shift convention forvanishingcycles','BothCodexpassagesfullyread; short exactsequence fixesΦmanuscript=RΦusual[-1].')
L('folder','34:164–179','34:180–181','Prime-to-p monodromycontinuation','Same section3 andmanuscriptpages14→15→16; allsourcepagesread.')
L('folder','34:183–195','34:196–199','Lieappendixcontinuation','ManuscriptII.31–II.43 continuesII.44–II.47;6.15argumentcontinuesbutprovesonlyalgebraicinfinity.')
L('folder','34:201,203,205,207,209','34:202,204,206,208,210','Twointerleavedtexts','Oddfacesareweightmanuscript; evenfacesareprintedGITinargumentorder2.3,2.5,2.10,2.11,2.12,notphysicalorder.')
L('published work','34:149–156','SGA2XIV5.3–6.3;SGA7I4.5–4.11;Illusie2003 §§1–2','Depthandlci cycles','Exactdefinitionandprintedchar0hypothesischecked;Illusieprimaryintroexplicitlyextendsisolatedlciresulttoarbitrarytraitswithℓinvertible.')
L('published work','34:155–156','Raynaud1974III1.2–1.3;Orgogozo2003 §§3–4','NonabelianLefschetzsubcases','Bothfullprimarytextsopened; base/depth restrictionsretained.')
L('published work','34:165–181','SGA7I5.2–5.5,printedpp18–20','Tameprime-to-pmonodromy','Original1972pagesOCRreadandcompared;publishedsectionrecordslecture1968-11-19.')
L('published work','34:167,178','Orgogozo2003Cor4.5,Th4.10–4.11','Baseextension, Lefschetz andfinitepresentation','Exactprimarytheoremsopened; oldresolutionhypothesisremovedin2003.')
L('published work','34:185–188','Deligne–Milne1982Prop2.8,Th2.11,Prop2.20–2.21','Tensorreconstruction','Correctedauthor2012versionopened; fibre functorhypothesisexplicit. No claimthatthisexactdraftwaspublishedthere.')
L('published work','34:188','Lazard1965;Casals-Ruiz–Zozaya2025Th2.1','Compactanalyticlinearity','ModernprimaryproofanditsbackwardLazardreferencechecked;1965publicationmetadataopened.')
L('published work','34:198–199','Gajda–Petersen2022/2023Th2.3,Lemma3.4','TateEndandnormal-baseextension','Exactfield/basequantifiersopened; ownmodel-descentdeductionlabelled.')
L('published work','34:201–209','DeligneWeilII;Illusie2021 §6','Weightsandmonodromy','Weightseparationrecomputed; modernreviewdoesnotprovefalseinvariant/coinvariantpurity.')
L('published work','34:202,204,206,208,210','MumfordGIT §2','Reusedprintedsource','Sourcefamilyidentifiedandprimaryeditionopened; exacteditioncollationrecordedseparately, notauthorshipinference.')
tsv('links.tsv',['kind','from','to','what','evidence','note_ids'],links)

print(json.dumps({'items':len(items),'claims':len(claims),'problems':len(problems),'readings':len(readings),'links':len(links)}))
