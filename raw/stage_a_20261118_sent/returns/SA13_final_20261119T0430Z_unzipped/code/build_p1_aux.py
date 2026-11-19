"""Serialize manually reviewed problems, reading alarms, links and source audit for p1."""
from pathlib import Path
import json,csv
ROOT=Path(__file__).resolve().parents[2]; O=ROOT/'deliverable/shards/p1'
items=json.loads((O/'items.json').read_text()); claims=json.loads((O/'claims.json').read_text())
def tsv(name,fields,rows):
 with (O/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
problems=[]
def P(n,title,cs,his,today,art,why,worth,refs):
 occ=[]
 for c in cs:occ.extend(claims[c-1]['lines'])
 problems.append(dict(id=f'MP-SA13-{n:02}',title=title,occurrences=occ,as_he_states=his,plausible_today=today,state_of_art=art,why_open=why,worth=worth,refs=refs,claims=[f'C-SA13-{c:03}' for c in cs]))
P(1,'Derived pullback without flatness',[5,8],
 'Whether Lf* and its tensor/Hom identities still work when f is not flat; scan106 retracts the naive injective argument.',
 'Derived inverse image exists for morphisms of ringed topoi and is composition-compatible and monoidal. Use K-flat/K-injective or the appropriate bounded resolutions.',
 'Stacks21.18 (tag06YV) supplies this formulation. The elementary f_* injective-preservation proof needs exact f*.',
 'The pages themselves identify the flaw. No historical cause beyond that correction is documented.',
 'Useful as a short commentary task explaining the correction, not as an unsolved theorem.', ['Stacks06YV'])
P(2,'Finite relative cohomological dimension over a noetherian base',[9],
 '“C’est peut-être vrai dès que Y est noethérien”: remove the finite-type-over-a-field restriction.',
 'For finite-type f over a finite-dimensional noetherian base and an invertible prime ell, relative ell-cohomological dimension is finite. The unrestricted noetherian/coefficient version must be kept separate.',
 'Gabber–Illusie XVIII_A Cor1.4 proves the stated finite-dimensional prime-to-characteristic case; Stacks59.96.2 covers finite-type schemes over a field.',
 'The manuscript leaves a hope; the checked sources do not state why this exact broad wording was dropped.',
 'A bounded hypothesis comparison is worthwhile; the search does not justify advertising a new general theorem.', ['GabberIllusie2014','Stacks0F10'])
P(3,'Projection coherence and resolution independence',[12,13],
 '“Il faut vérifier” functoriality and compatibilities of the constructed projection and Künneth maps.',
 'For compactifiable morphisms and torsion coefficient sheaves in the stated bounded ranges, the canonical projection and external-product isomorphisms are natural and compatible with the six operations.',
 'SGA4XVII5.2.9 and5.4.3 are exact statement matches;5.4.3.2 and5.4.3.5 leave auxiliary compatibility checks to the reader. This run does not claim a full re-proof of those diagrams.',
 'The draft explicitly isolates coherence as the remaining task; Illusie later records how substantial compatibility work affected the trace formula.',
 'Worth a focused reconstruction of one named diagram, with the original models and signs fixed.', ['SGA4XVII','IllusieChronology2026'])
P(4,'Ordinary Künneth without properness',[16,17],
 'He expects ordinary Künneth when n is prime to the characteristic, even if neither factor is proper.',
 'For finite-type schemes over a separably closed field and invertible n, the derived Z/n Künneth formula holds.',
 'Stacks59.97.9 proves exactly this. The unrestricted p-primary version is false, with the Artin–Schreier xy counterexample in C-SA13-017.',
 'The page distinguishes the obstacle from the proper case; it gives no later abandonment history. The conditional Verdier priority remark remains historical evidence only.',
 'The mathematical question is settled; a concise historical comparison would improve the companion.', ['Stacks0F1P','Stacks0F14','Stacks0A3J'])
P(5,'Curve Lefschetz formula with nonconstant coefficients',[19,21],
 'Prove the curve case with nonconstant coefficients and correct local terms, as a route to rationality.',
 'Use constructible prime-to-characteristic ell-adic coefficients and the exact local terms of a cohomological correspondence; stalk traces need extra hypotheses.',
 'Bourbaki279 §§5–6 announces the reduction; SGA5III,III B,XII contain the completed formulations. Illusie distinguishes the independent curve route from the later general compatibility proof.',
 'Illusie documents missing compatibility arguments and the1974–1975 work; this does not prove a personal motive or a date for these sheets.',
 'A precise page-to-publication concordance is valuable, but re-solving the established trace theorem is unnecessary.', ['GrothendieckBourbaki279','SGA5','SGA5III','IllusieChronology2026'])
P(6,'Passage from finite-level traces to ell-adic coefficients',[20,30],
 'Compatibility in n, projective limits, and extraction of the ell-adic trace needed for functions L.',
 'Compatible perfect finite-level systems admit compatible traces; the full adic six-operation theory requires its finiteness and derived-limit hypotheses.',
 'SGA5V–VI andXIV=XV provide the published setting. The independently checked certificate covers finite-projective Z_ell models and their reductions, not all derived limits.',
 'SGA5 introduction explicitly notes that its V–VI do not build a full derived category of ell-adic sheaves. No reason for this sheet’s unfinished paragraph is stated.',
 'Worth isolating the exact adic hypothesis in a commentary task, avoiding a claim that the elementary calculation solves the whole formalism.', ['SGA5','IllusieChronology2026'])
P(7,'Definition and independence of perfect-complex trace',[24,25,26,27,28,29],
 'Show the alternating trace descends through resolutions and has the expected additivity, duality and tensor properties.',
 'A perfect object has a canonical categorical trace. Strictly compatible cone diagrams have additive trace; arbitrary endomorphisms of abstract triangles need not.',
 'Stacks64.10.2 and21.48 give the positive statements;110.65 gives the counterexample. The sheet132→134 supplies the later resolution argument itself.',
 'The same-text development resolves much of the initial question. Illusie reports Ferrand’s1968 counterexample to the stronger abstract assertion.',
 'Worth making the distinction explicit because the earlier notes blurred the two additivity claims.', ['Stacks03TI','Stacks0FPP','Stacks087J','IllusieChronology2026'])
P(8,'Global Tor dimension after compact-support cohomology',[31,34,35],
 'The question begun at136 is developed into the uniform Tor bounds and Rf! estimate at138–142.',
 'For compactifiable finite-type f with fibers of dimension≤d and the draft’s uniform Tor interval [N,M], the homological interval becomes [N−2d,M]; constructibility and noetherian coefficient hypotheses supply perfectness over a point.',
 'SGA4XVII5.2.10,5.3.6–8 give the corresponding finiteness statements. The sign conversion and uniformity requirement are independently checked.',
 'This is largely an open step answered later in the same supplied text, not evidence of a surviving conjecture.',
 'Useful for one worked example and a warning about nonuniform stalk bounds; no new general research claim follows.', ['SGA4XVII','Stacks0656'])
P(9,'Construction of the local trace pairing',[36,37,38,39],
 'The correspondence pairing is started on144, partly deleted, and rebuilt on146 using duality and Koszul signs; boundedness is struck in one passage.',
 'Dualizable/perfect coefficient objects admit evaluation-defined local pairings with H⁰ in the correct place. Finite Tor amplitude alone is insufficient; an unbounded model must not be traced term by term.',
 'SGA5III/III B supply the published framework. Lu–Zheng2022 Th2.16 and2.21 give a relative dualizability criterion and a proper-pushforward pairing formula under explicit noetherian, torsion, finite-Tor and local-acyclicity hypotheses.',
 'The visible cancellation is a revision, not evidence of rejection of local trace. Illusie’s chronology records later compatibility work; the scan is needed for the deleted word.',
 'High-value companion work: reconstruct the single typed pairing with the two shifts and evaluation map fixed.', ['SGA5III','SGA5','LuZheng2022','Stacks0FPP'])
P(10,'Broader ordinary projection formula',[11],
 'The paragraph about locally constant finite-type cohomology and a qcqs relaxation is left with an unfinished “où”.',
 'Perfect target complexes satisfy projection on arbitrary ringed topoi. For constant noetherian coefficient rings and finite relative cd, bounded-above finite-free resolutions permit the stated way-out extension; qcqs alone is not a replacement for all colimit hypotheses.',
 'Stacks21.50.1 and SGA4XVII5.2.11–12 are the checked positive formulations. The exact maximal range of the unfinished sentence was not identified.',
 'The text is unfinished; the sources opened do not explain why it was left so.',
 'Worth a small hypothesis audit, with no claim that the familiar perfect case is open.', ['Stacks0944','SGA4XVII'])
(O/'problems.json').write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')

readings=[]
def R(s,line,reading,alternative,evidence,weight='high',confidence='medium'):
 page=next(x for x in json.loads((ROOT/'work/pages.json').read_text()) if x['file']=='pro/MPL_33_098-146_transcription.tex' and int(x['scan'])==s)
 readings.append(dict(cote=33,scan=s,line=f"pro/MPL_33_098-146_transcription.tex:{page['start']}–{page['end']} (scan range; passage identified by quotation)",reading=reading,alternative=alternative,evidence=evidence+' No ink decision; transcription unchanged.',weight=weight,confidence=confidence))
R(98,'global5–25','placements of ! and * in D exchange identities','Check each exponent against the actual functor domain','D exchanges proper/ordinary pushforward and pullback/exceptional pullback only in correctly typed formulas')
R(102,'global73–96','f′ versus f*; plain connector','f* where pullback of a module is meant','The tensor and adjunction expressions require a functor, not a second unspecified morphism')
R(104,'global119–141','D− versus D0−; unqualified Γ','Confirm boundedness category and finite-cd qualification','Finite cohomological dimension is used to preserve an upper bound')
R(106,'global143–177','injective-preservation proof and marginal ne marche que si','Retain the visible flatness restriction and scope of cancellation','The unrestricted underived injective argument fails when f* is not exact')
R(112,'global251–294','tensor factors written on different spaces without visible f*','Check omitted pullbacks and the unfinished hypothesis after où','Projection morphism must live in one ringed topos')
R(114,'global300–335','Y′/X′ and Y/X in compactification diagram','Compare diagram objects and arrows with114→116','Functor domains fix the mathematical alternative but not the ink')
R(116,'global340–383','g′* versus f′* in external product','Check the two projections separately','The two pulled-back complexes originate on different factors')
R(118,'global388–421','même pour H¹','Confirm exponent1 rather than2','Artin–Schreier xy gives a real degree-one failure; it supports plausibility, not a reading decision')
R(128,'global650–671','A_X versus Λ_X and clipped ell-adic sentence','Check whether one coefficient sheaf or a change of coefficients is intended','Trace compatibility depends on specifying the finite-level system')
R(132,'global746–786','Tr_* and overwritten trace decoration','Check which trace is on complexes and which on cohomology','Perfect complexes can have nonprojective cohomology')
R(134,'global807–843','L→L∨∨ and unadorned M','Check duals, direction and complex grading','Evaluation is an isomorphism for perfect first input; changing its factor changes the formula')
R(136,'global902–932','Hom(M,L) / Hom(L,M) and <u,v>=H⁰(A)','Check factors and membership sign ∈H⁰(A)','A scalar lies in H⁰(A); it cannot equal the whole group')
R(138,'global981–1030','overwritten M/N′ interval endpoints','Check each endpoint in the fixed uniform Tor interval','Existence of individual finite stalk bounds does not give a uniform bound')
R(140,'global1062–1093','[N] versus [N,M] and ∃','Confirm interval and quantifiers','The truncation assertion needs a fixed lower bound')
R(142,'global1111–1132','+2d / hom and ordinary tensor on right','Check homological sign and derived decoration','Homological[N−2d,M] corresponds to cohomological[−M,−N+2d]')
R(144,'global1181–1229','Hom_D identified with a complex / Hom⁰','Check H⁰ on the derived global Hom','A morphism set is H⁰ of derived Hom, not the entire complex')
R(144,'global1181–1229','finite Tor dimension alone in trace construction','Look for pseudo-coherence/constructibility hypothesis in continuation','An infinite free module is flat but not dualizable')
R(146,'global1251–1297','struck et borné','Determine the exact scope of deletion','An unbounded representative of a perfect object has intrinsic trace, but its infinite termwise sum need not exist')
R(146,'global1251–1297','RHom dual factor and arrow direction','Check source/target and which factor is dualized','Evaluation requires K∨ tensor K and its Koszul symmetry')
R(105,'typed ramification Lemma2.2','indices of completion/diagonal maps','Check primes and hats against101–109','The algebra changes under completion; symbols cannot be interchanged')
R(109,'typed Lemmas2.4–2.6','multiplicity and ramification factors','Check ambient-dimensional multiplicity convention in missing §1','Usual own-dimensional multiplicities give counterexamples for lower-dimensional summands')
R(111,'typed theorem2.7 proof','rank/residue degree factors','Check missing brackets and which field degree multiplies length','The tower degree and Euler factors must agree')
R(121,'typed proposition3.10','gothic g/J and η/N','Check the ideal symbols before interpreting the truncated statement','The proposition stops before a complete conclusion; no unique invariant can be reconstructed')
R(125,'typed Lemma6','pi-rational','birational','The morphism of normal projective models is used as a birational comparison','medium')
R(127,'typed Lemma5','uppercase S exponent','lowercase s','The length polynomial is indexed by the integer s','medium')
R(129,'typed Lemma4','every valuation ring','nontrivial valuation ring dominating the local domain','The fraction field itself is a trivial valuation ring, not a DVR')
R(131,'Weierstrass induction','γ versus h in correction term','Check the symbol against the previous homogeneous coefficient','The induction identity depends on one consistently chosen correction')
R(133,'Weierstrass direction argument','projective plane','projective line in the two-variable argument','Binary forms have directions in P¹; the stated finite-field count uses that space','medium')
R(135,'coefficient-field/power-series paragraph','same characteristic so coefficient field; R=k[[x]]','Check for a standing completeness hypothesis or hat on R','C-SA13-065/066 give counterexamples to the isolated implications')
R(135,'divisor corollary','tangential to z','non-tangential to z','The proof uses the latter; z=t=x₂ refutes the literal implication')
R(137,'completion argument','ybar=mbar^q','Check principal ideal or membership notation','An element cannot be identified with a whole ideal power without notation')
R(139,'quadratic transform','M_V versus M_v','Check capitalization of the valuation/local ring','The center condition depends on which maximal ideal is meant','medium')
R(143,'global1147 / Lemma7','x₁b and F/f','x₁^q b and one consistent polynomial variable','Homogenization in degreeq requires exponentq')
R(143,'Lemma8','r^m versus r^u and m/n','Check quotient order and lifted exponent','The verified construction needs gcd(u,n)=1 with n dividing m')
R(145,'typed étale criterion','flat fp plus separable residue extension','Check for equality of maximal ideals or reduced fiber hypothesis','Q[epsilon]/epsilon² is a fully checked counterexample to the literal statement')
tsv('readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],readings)

links=[]
def L(kind,fr,to,what,evidence,ids):links.append(dict(kind=kind,**{'from':fr,'to':to},what=what,evidence=evidence,note_ids=';'.join(ids)))
L('folder','33:144–146','33:148–160','Continuation of local trace construction','Both supplied Pro transcriptions read; source foliation and local-pairing notation continue. No claim that every deleted expression persists.', ['MPL_33_098-146#36','MPL_33_098-146#39'])
L('folder','33:145','33:147,163','Reused typed topos exposition','Both supplied packages read; later sheet explicitly names Roos. Exact author/title remains a source-identification question.', ['MPL_33_098-146#57'])
L('published work','33:112–116','SGA4XVII §5.2.9; §5.4.3','Compact projection and Künneth','Primary chapter opened; statements and bounded torsion hypotheses compared. Auxiliary compatibility proofs not independently supplied.', ['MPL_33_098-146#13','MPL_33_098-146#15'])
L('published work','33:130–136','SGA5VIII pp351–371; Stacks15.76.2;64.10.2','Perfect complexes and their traces','SGA5 title/contents and modern exact criteria opened; do not confuse VIII with XIV=XV.', ['MPL_33_098-146#28','MPL_33_098-146#29'])
L('published work','33:122–128','Bourbaki279 §§5–6; SGA5III,III B,XII,XIV=XV','Curve trace route and rationality','Bourbaki full text and SGA5 introduction opened. Talk December1964 versus collected publication1966 distinguished.', ['MPL_33_098-146#22','MPL_33_098-146#25'])
L('published work','33:123','EGAIV4 §21.15; Stacks31.19.2','Relative effective Cartier divisor comparison','EGA metadata opened; exact modern theorem and explicit EGA cross-reference checked. Missing §10.1 prevents identifying the whole quotient-sheaf definition.', ['MPL_33_098-146#49'])
L('published work','33:145','EGAIV4 §17; Stacks41.14.1','Étale criteria and open immersion','Modern exact theorem opened; the literal residue-only criterion is false and remains an ink alarm.', ['MPL_33_098-146#56'])
L('our projects','MPL_33_098-146#1–2,43,59–70','LM7 E.23; LM4 D.12/F.7; LM7_PUSH C.6; WG H9; WG2 §2.1 #2; S19; S6','Earlier-run context and bibliographical leads','Only the SA13 side is supplied and checked. Underlying runs/context packets unavailable; explicitly unverified comparison leads, with no imported result or status change.', ['MPL_33_098-146#1','MPL_33_098-146#2','MPL_33_098-146#43','MPL_33_098-146#59','MPL_33_098-146#60','MPL_33_098-146#67','MPL_33_098-146#68','MPL_33_098-146#69','MPL_33_098-146#70'])
tsv('links.tsv',['kind','from','to','what','evidence','note_ids'],links)

refs=[]
def B(key,title,url,year,author,scope,verified=True,**extra):
 refs.append(dict(key=key,title=title,url=url,year=year,author=author,note='verified' if verified else 'unverified',annote=scope,urldate='2026-11-19',**extra))
B('SGA4XVII','Cohomologie à supports propres, SGA4 ExposéXVII','https://www.normalesup.org/~forgogozo/SGA4/17/17.pdf','1973','Deligne, Pierre','Full primary chapter, §§4.1–4.2,5.2.8–12,5.3.6–8,5.4.3 read. Modern author-hosted transcription; draft1968–1969 based on1964 lectures.',pages='250--480',booktitle='Théorie des topos et cohomologie étale des schémas, tome3')
B('SGA5','Cohomologie l-adique et fonctions L (SGA5)','https://link.springer.com/book/10.1007/BFb0096802','1977','Grothendieck, Alexander and collaborators','Publisher metadata and primary front matter including contents and1977 introduction opened; not all chapters read.',doi='10.1007/BFb0096802',series='Lecture Notes in Mathematics',volume='589',editor='Illusie, Luc')
B('SGA5I','Complexes dualisants','https://link.springer.com/chapter/10.1007/BFb0096803','1977','Grothendieck, Alexander','Chapter metadata and primary introduction checked; full chapter not obtained. ExposéI, redacted byLucIllusie.',doi='10.1007/BFb0096803',pages='1--72',booktitle='SGA5')
B('SGA5III','Formule de Lefschetz','https://link.springer.com/chapter/10.1007/BFb0096804','1977','Grothendieck, Alexander','Publisher chapter record opened; full theorem text not obtained here. Primary introduction and Illusie chronology checked; redacted byLucIllusie.',doi='10.1007/BFb0096804',pages='73--137',booktitle='SGA5')
B('SGA5VIII','Groupes de classes des catégories abéliennes et triangulées. Complexes parfaits','https://link.springer.com/chapter/10.1007/BFb0096809','1977','Grothendieck, Alexander','Metadata opened; ExposéVIII verified from original contents, redacted byI.Bucur. Exact criterion checked separately in Stacks.',doi='10.1007/BFb0096809',pages='351--371',booktitle='SGA5')
B('IllusieChronology2026','Chronology and posterity of SGA5','https://www.imo.universite-paris-saclay.fr/~luc.illusie/Chronology-SGA5-1.pdf','2026','Illusie, Luc','Author PDF and author bibliography opened. Dates of lectures, counterexample and compatibility work checked; publication volume364 pp479–494.',doi='10.5802/crmath.841',journal='Comptes Rendus Mathématique',volume='364',pages='479--494')
B('IllusieErrSGA5III','Erratum: SGA5 III','https://www.imo.universite-paris-saclay.fr/~luc.illusie/ErrSGA5III.pdf','2026','Illusie, Luc','One-page author errata opened; p98 andp124 corrections checked. Year is access year, not a claimed original issue date.')
B('GrothendieckBourbaki279','Formule de Lefschetz et rationalité des fonctions L','https://www.numdam.org/item/SB_1964-1966__9__41_0/','1966','Grothendieck, Alexander','Full original opened. Header dates talk toDecember1964; §§5–6. Collected publication1966; laterDixExposés1968 is distinct.',series='Séminaire Bourbaki',number='279',pages='41--55',zbl='0199.24802')
B('GabberIllusie2014','Cohomological dimension: first results','https://www.numdam.org/item/AST_2014__363-364__455_0.pdf','2014','Illusie, Luc','Full ExposéXVIII_A read, especiallyCor1.4. Email date2007-08-15 is documented, not claimed first circulation.',journal='Astérisque',volume='363--364',pages='455--459')
B('LuZheng2022','Categorical traces and a relative Lefschetz–Verdier formula','https://arxiv.org/abs/2005.08522','2022','Lu, Weizhe and Zheng, Weizhe','arXiv record and full Cambridge article opened; Th2.16,2.21 andRemark2.21 checked. First arXiv2020-05-18.',doi='10.1017/fms.2022.2',eprint='2005.08522',archivePrefix='arXiv',journal='Forum of Mathematics, Sigma',volume='10',pages='e10')
B('EGAIV4','Éléments de géométrie algébrique IV, quatrième partie','https://www.numdam.org/articles/10.1007/BF02732123/','1967','Grothendieck, Alexander and Dieudonné, Jean','Numdam metadata opened. Large originalPDF failed tool size limit; §§17 and21.15 compared through exact Stacks cross-references, not claimed full EGA proof review.',doi='10.1007/BF02732123',journal='Publications Mathématiques de l’IHÉS',volume='32',pages='5--361',zbl='0153.22301')
B('AuslanderRim1963','Ramification index and multiplicity','https://doi.org/10.1215/ijm/1255645095','1963','Auslander, Maurice and Rim, Dock Sang','Candidate source only. DOI retrieval failed; ProjectEuclid challenge blocked full article. ContemporaryWilliamson bibliography supports identity, not exact manuscript collation.',False,journal='Illinois Journal of Mathematics',volume='7',number='4',pages='566--581',doi='10.1215/ijm/1255645095')
B('Abhyankar1960II','Tame coverings and fundamental groups of algebraic varieties. II. Branch curves with higher singularities','https://doi.org/10.2307/2372882','1960','Abhyankar, Shreeram Shankar','Candidate source only. DOI/IASbibliography inaccessible; exact lemmas and standing hypotheses not collated.',False,journal='American Journal of Mathematics',volume='82',number='1',pages='120--178',doi='10.2307/2372882')
B('Williamson1963','Crossed products and hereditary orders','https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5017A9C59943910CE1ECED5E80CB8A14/S0027763000011211a.pdf/crossed_products_and_hereditary_orders.pdf','1963','Williamson, Susan','Full original opened, introduction and bibliography used only for backward reference toAuslander–Rim; not a source for missing typed definitions.',doi='10.1017/S0027763000011211',journal='Nagoya Mathematical Journal',volume='23',pages='103--120')
tags={
'06YV':'§21.18 Derived pullback; composition and tensor compatibility', '0944':'Lemma21.50.1 projection with perfect target',
'0F10':'Lemma59.96.2 relative cohomological dimension over a field', '0F14':'Lemma59.97.2 Künneth with one proper factor',
'0F1P':'Lemma59.97.9 Künneth with invertible coefficients', '0656':'§15.76, Lemma2 perfect iff pseudo-coherent and finite Tor amplitude',
'03TI':'Proposition64.10.2 trace invariance', '087J':'§110.65 nonadditivity for arbitrary triangle endomorphisms',
'0FPP':'§21.48 duals, particularlyLemma4', '08G8':'§21.47 perfect complexes on ringed sites',
'0A3J':'§59.63 Artin–Schreier sequence', '09IG':'Lemma10.120.18 one-dimensional normalization',
'02M9':'Lemma10.78.7 semilocal finite-projective freeness', '032A':'Theorem10.160.8 Cohen structure',
'0C0S':'Lemma10.160.10 complete regular local power-series form', '03PC':'Lemma59.26.2 étale criterion',
'0AZU':'§43.15 algebraic multiplicities, ambient dimension and associativity', '00MC':'Lemma10.97.3 faithful flatness of completion',
'02GH':'§29.37, Lemmas8 and15 étale morphisms', '025G':'Theorem41.14.1 étale universally injective iff open immersion',
'056P':'§31.19 relative effective Cartier divisors andEGAIV21.15 comparison'}
for tag,scope in tags.items():B('Stacks'+tag,'The Stacks Project, tag '+tag,'https://stacks.math.columbia.edu/tag/'+tag,'2026','The Stacks Project Authors','Opened exact primary project statement and its relevant hypotheses: '+scope+'. Access year; no first-publication priority claim.')
with (O/'references.bib').open('w') as f:
 for r in refs:
  f.write('@misc{'+r['key']+',\n')
  for k,v in r.items():
   if k!='key':f.write('  '+k+' = {'+str(v).replace('\n',' ')+'},\n')
  f.write('}\n\n')
(O/'reference_audit.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')

queries=[
('P1-S01','"SGA 5" dualité "Lefschetz" Illusie chronology; site:arxiv.org "Categorical traces and a relative Lefschetz-Verdier formula"','SGA5I;LuZheng2022;IllusieChronology2026','Chapter family and exact modernrelative theorem distinguished.'),
('P1-S02','site:stacks.math.columbia.edu "Derived pullback" ringed topoi','SGA4XVII;Stacks06YV;Stacks0FPP','Exact bounded/unbounded formalism checked; not all foundational proofs repeated.'),
('P1-S03','Gabber Illusie dimension cohomologique relative noetherien XVIII_A','GabberIllusie2014;Stacks0F10','Finite-dimensional and invertible-prime hypotheses retained; broad merelynoetherian case not declared settled.'),
('P1-S04','site:mathoverflow.net trace additivity distinguished triangle Ferrand; perfect complex finite Tor amplitude pseudo coherent trace','Stacks0656;Stacks03TI;Stacks087J;SGA5VIII;IllusieChronology2026','MO-targeted search supplied no exact useful hit; primary Stacks counterexample and historical chronology opened.'),
('P1-S05','"SGA 4" "5.2.9" "5.4.3"','SGA4XVII;Stacks0944','Primary §§5.2.8–12,5.3.6–8,5.4.3 matched; two published compatibility verifications remain admitted.'),
('P1-S06','site:stacks.math.columbia.edu Kunneth separably closed proper invertible','Stacks0F14;Stacks0F1P;Stacks0A3J','Both positive formulas and characteristic-p obstruction checked.'),
('P1-S07','Grothendieck Bourbaki 279 rationalité fonctions L 1964','GrothendieckBourbaki279;SGA5;IllusieChronology2026','Primary talk header and final publication dates separated. SGA5contentscorrectVIIIversusXIV=XV.'),
('P1-S08','"Theorem 4.6.6" "operator" "homotopy"; "homogeneous parts" "symbol" "4.6.6"','No collatable source','Exact-number/phrase and operator-source searches returned no identified primary match; classF, not evidence of a new theorem.'),
('P1-S09','"Auslander" "Rim" "Ramification index and multiplicity"; site:zbmath.org "Ramification index and multiplicity"','AuslanderRim1963;Williamson1963','Backward references inWilliamson andCliff–Weiss1986 checked. DOI/ProjectEuclid failed; zbMATHaccess403/no usable directrecord. Missing§1prevents exact invariant identification.'),
('P1-S10','"EGA" "21.15" "relative effective Cartier"','Stacks056P;EGAIV4','Exact effective modern version; full relative rational-function sheaf needs missing source§10.1.'),
('P1-S11','"Abhyankar" "Tame coverings" "Lemma 6"','Abhyankar1960II','Title,author bibliography andbackward references searched. DOI/IASblocked; valuation-versusdivisor definition not recovered.'),
('P1-S12','"Abhyankar" "Weierstrass" "quadratic transform"; regular local coefficient field complete power series normalization semilocal','Stacks032A;Stacks0C0S;Stacks09IG;Stacks02M9;Stacks00MC;Stacks0AZU;Abhyankar1960II','Classical positive hypotheses checked inprimaryproject; two isolated missing-completeness implications refuted. Sourceauthorshipunidentified.'),
('P1-S13','site:stacks.math.columbia.edu etale universally injective open immersion','Stacks025G;Stacks03PC;Stacks02GH;EGAIV4','Exact modern criterion; explicitdual-numbercounterexample toresidueonly version.'),
('P1-S14','"Roos" "topos" "axiomatic" Grothendieck','p2sourceaudit;SGA4','Suppliednextpackage namesRoos at33:163. ModernpresheafRoostheorem not substituted for unidentifiedfragment.')]
rows=[]
for sid,q,refsused,result in queries:
 rows.append(dict(search_id=sid,date='2026-11-19',claims=';'.join(c['id'] for c in claims if sid in c['search_ids']),queries=q,sources_opened_or_attempted=refsused,result=result))
tsv('search_log.tsv',['search_id','date','claims','queries','sources_opened_or_attempted','result'],rows)

events=[];who='GPT-6 Astra Pro; configured effort not exposed; SA13 part2/p1'
def E(s,t,o):events.append(dict(statement_id=s,date='2026-11-19',who=who,type=t,outcome=o))
for i in items:E(i['id'],'carried as background without fault found','Text concordance review: '+i['check_reason']+' This item-level event does not assert an independent proof.')
independent={2,6,8,10,14,17,18,20,24,25,26,27,28,29,30,31,32,39,45,48,51,55,62,64,65,66,68,69,70,71,74}
refuted={26:'C-SA13-025',37:'C-SA13-022',39:'C-SA13-024',65:'C-SA13-067',66:'C-SA13-067',68:'C-SA13-068',74:'C-SA13-074'}
for c in claims:
 n=int(c['id'].split('-')[-1])
 if 'proof' in c['computation']:E(c['id'],'independent re-proof' if n in independent else 'targeted proof check','Scope and dependencies recorded in '+c['computation']['proof']+'. This label applies only to the explicitly reconstructed substatement.')
 else:E(c['id'],'used and rechecked in this run','Page statement compared with searched literature scope: '+c['fate']+' No independent full proof claimed.')
 if n in refuted:E(c['id'],"refuted, with the refined statement's id",'Refined statement '+refuted[n]+'. Counterexample/scope inproofaudit; uncertaininkandmissingstandinghypothesesremainundecided.')
for n in [10,14,17,20,24,25,26,27,30,31,32,39,62,69,71,74]:E(f'C-SA13-{n:03}','computation or formal certificate','Exact finite checks incode/p1_compute.py andoutputs/p1_computations.json; universalproofscope inproofs.md.')
for r in refs:E(r['key'],'used and rechecked in this run' if r['note']=='verified' else 'carried as background without fault found',r['annote'])
tsv('check_events.tsv',['statement_id','date','who','type','outcome'],events)
(O/'review.md').write_text('''# P1 review scope\n\nAll70 indexed entries, all1,297 lines of the Pro transcription, and the substantive doubts register were read. No scans or second-pass files were supplied. Sixty-one items cover the70 entries;76 distinct claims are recorded, including individually separated typed lemmas. Ten genuine open steps are distinguished from historical publication questions.\n\nThe appended proof audit and exact computations establish selected reconstructed statements; they do not certify the whole six-operation formalism, unknown typed sources, or every published proof. Missing definitions in the ramification sheets yield classF, not a declaration that the mathematics is open. CandidateAuslander–Rim andAbhyankar references remainunverified. The operator-sourceidentitysearchalsoremainsunresolved.\n\nCross-package trace andtopos continuations havebeenchecked onboth suppliedsidesbytheassignedreviewers. Earlier-run project comparisonsareseparatedandnotverifiedagainstunavailableexternalruns.\n''')
print(f'p1 auxiliary: {len(problems)} problems, {len(readings)} reading alarms, {len(links)} links, {len(refs)} references, {len(events)} check events')
