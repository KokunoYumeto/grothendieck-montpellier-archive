"""Serialize links checked by reading both supplied/primary passages.
Context-project rows preserve the earlier note's citation only; absent target
manuscripts or result registers are explicitly not corroborated.
"""
from pathlib import Path
import json,csv
R=Path('/workspace/scratch/a77a578fa7d4/SA12_work/reviews/31');C={int(x['id'].split('-')[-1]):x for x in json.loads((R/'claims.json').read_text())};I=json.loads((R/'items.json').read_text());B={x['key']:x for x in json.loads((R/'reference_verification.json').read_text())};L=[]
def fromclaims(ns):return '; '.join(C[n]['id']+' /31 scans'+','.join(map(str,C[n]['scans']))+' /'+C[n]['lines'] for n in ns)
def notes(ns):return ';'.join(sorted({s for n in ns for i in I if i['id'] in C[n]['items'] for s in i['sources']}))
def p(ns,key,loc,what):L.append(dict(kind='published work',**{'from':fromclaims(ns),'to':key+' '+loc+' / '+B[key]['url']},what=what,evidence='Supplied text and named primary passage both read; '+what,note_ids=notes(ns)))
p([408],'SGA3IX','5.1','Central rigidity; the published theorem only assumes centrality on the fiber, weaker than the draft.')
p([409],'SGA3IX','5.2–5.3','Triviality near a fiber and clopen triviality locus; separatedness belongs to ambient G.')
p([410],'SGA3IX','5.1bis','The globally cancelled subgroup version survives in print; cancellation does not refute it.')
p([411,412],'SGA3X','5.1–5.8','Character anti-equivalence and representing Hom/Isom/Aut schemes.')
p([413,416],'SGA3X','5.11–5.11bis,editorial footnotes43–44','Isotriviality criteria and the editor’s explicit converse verification request.')
p([414,415,417],'SGA3X','5.12–5.16,footnote45','Quasi-compact closed parts, finite fibers and geometrically unibranch bases.')
p([488],'SGA3IX','2.3–2.5','Quotient by a multiplicative-type subgroup and the relevant representability scope.')
p([498,499],'SGA3IX','3.1–3.4','Hochschild cohomology vanishing and square-zero conjugacy.')
p([503,505],'SGA3IX','4.6–4.10','Published strengthening drops retrocompactness from the density statement;4.10 completes the selected m-power torsion family.')
p([421],'SGA2','XIII1.1','Old cofini means finite Hom, and quotient stability is explicitly denied; not Hartshorne’s all-Ext condition.')
p([435,436,437],'SGA2','XII5.10–5.11','Formal full faithfulness and coherent algebraization under degrees0,1 coherence; local freeness is not automatic.')
p([438],'SGA2','XII5.11','Nonproper Picard expectation, rather than a universal representability theorem.')
p([438],'Murre1964','1.2.1 and II15','Seven-axiom criterion; the published Picard application explicitly assumes properness.')
p([439],'EGAIII2','Erratum24 to0III13.7.7','Published correction adds a finiteness hypothesis not contained in the draft’s deletion instructions.')
p([440],'SGA2','IX2.1','Three adjacent graded degrees control coherence and uniform Mittag–Leffler.')
p([441,442],'SGA2','XII2.4 and formal-comparison statements','Depth≥1/≥2 gives faithful/fully faithful completion; endpoint signs remain ink questions.')
p([403,426,472],'SGA4III','IX3;X2.1;X5.1','Artin–Schreier, Kummer and field dimension: the prime restriction is essential.')
p([422,424,427,428,429,430,473,486,487],'SGA4III','X2.1–2.5;X6.2','Real exceptions, local lower bounds, henselian dimension-one equality and finite-type arithmetic upper bounds.')
p([425],'SGA4III','XVI4.1','Complex comparison with constructible-torsion or properness alternatives; real free-involution descent is a stated reconstruction.')
p([431,432,433,434,477,478],'SGA4V','4.3,5.9 and Čech-comparison sections','Cartan/Čech framework; the source’s finite-degree implication graph and boundary are kept distinct.')
p([443,444],'Armstrong1965','Theorem3, reproduced in1966 thesis','Later orbit-space π1 theorem matches stabilizer quotient; no date is inferred for the undated draft.')
p([447],'Serre1953Classes','III theorem1, printed271','Homology-to-homotopy passage for the stated Serre class; source argument stops before this result is applied.')
p([448,452],'Broue2007','6.8;group-algebra example printed55;referencesHi1,Hi2','Relative trace criterion has a standard proof; its use does not justify stable-corestriction bijectivity.')
p([450],'Serre1953Arithmetic','§1','Dimension shifting in both directions for Tate cohomology.')
p([406,465],'MilneCFT','II1.11;II4.2–4.4','Shapiro and filtered continuous cohomology.')
p([451,455,460],'MilneCFT','I1.1;III1.1–1.5','Trace/norm calculations for unramified local fields; finite residue-field scope matters.')
p([459],'MilneCFT','Idèle/ray-class discussion, printed172–173','Archimedean factors are taken modulo principal/global-unit contributions.')
p([402,463,466],'MilneAG2017','11.3;14.54;16.13,16.15,16.20','Finite connected–étale splitting, perfect-field decomposition and exponent-p vector groups; imperfect-field scope separated.')
p([480,481],'SGA4III','IX2.9,5.5','Constructible dévissage and generic coefficient reductions.')
p([482,483,484],'SGA4III','X4.1–4.4','Support-dimension criterion, with p+q total degree; the undefined φ variant is not supplied by the theorem.')
p([485],'ILO2014','XVIII-B4.1.2, combined with SGA4X2.4','Strict-local fraction-field equality is established even without excellence.')
p([489,490,493,494,495,496,500],'ILO2014','XV1.1.1,1.2.1–1.2.2;XVIII-B3.2.5,5.1.4','Quasi-excellent affine Lefschetz and nonexcellent counterexamples delimit the word good.')
p([491,492,495,497,504],'SGA4III','XIV3.1–3.6,4.3–4.5;X6','Artin’s simultaneous induction and arithmetic applications; an announcement does not settle every earlier variant.')
p([428,501,502],'GabberOrgogozo2008','1.2;§2.1;6.1','Exact mixed-characteristic theorem uses Kato p-dimension and nonempty affine opens inside SpecA[1/p].')
p([506,507,508],'SGA4III','XIV3.3;XVI3;XVIII3.2.5–3.2.6','Gysin and purity shifts, top-degree class and weak Lefschetz.')
p([509,510,511,512],'SGA4III','XV2.1–2.6,3.1–3.4','Completed local étale-extension and smooth local1-asphericity proofs.')
p([511,518],'SGA1','X3.1–3.3,3.6','Purity and the tame Abhyankar lemma; regularity is retained.')
p([513,515,516],'SGA4III','XVI1.1–1.6,3.7–3.8;XVIII3.2.5','Smooth base change, relative purity and duality; the draft’s omitted ambient setup is not filled silently.')
p([514],'HaineHolzschuhWolf2024','0.1;1.9;2.30','Modern nonabelian smooth base change for specified truncated torsion sheaves of spaces.')
p([518],'Achinger2017','Example1.2;corollary2.3','Wild base-change failure and a precise constant-Swan curve-family theorem.')
p([519,520,521,522],'HeinzerRotthausWiegand2020','§2.11–2.18','Classical Krull valuation and intersection structure; the typescript’s missing middle remains documentary.')
p([522],'Chang2021','§2 and proof of theorem4.1','Complete integral closure plus ACC on divisorial ideals, with backward references.')
def f(a,b,what,evidence):L.append(dict(kind='folder',**{'from':a,'to':b},what=what,evidence=evidence,note_ids=''))
f('31 scan7 /MPL_31_002-051_transcription.tex:143–154','31 scan9 /MPL_31_002-051_transcription.tex:205–223','Cancelled surjectivity route is replaced by prime-to-p transfer and μp dévissage.','Both passages read; retained deletion and later proof route distinguish withdrawal from abandonment.')
f('31 scans18,16,14,12 /MPL_31_002-051_transcription.tex:504–546;432–476;363–400;280–322','31 scans4,6,8 /MPL_31_002-051_transcription.tex:38–70;106–134;173–203','Reused multiplicative-type texts follow mathematical order rather than physical scan order.','Headings, theorem numbers and hypotheses compared; global strikes are preserved.')
f('31 scans11,13,15 /MPL_31_002-051_transcription.tex:240–279;323–362;401–431','31 scan17 /MPL_31_002-051_transcription.tex:477–503','Pushout module construction culminates in the nonfinite quotient.','Relations, regularity and transition maps compared directly.')
f('31 scan27 /MPL_31_002-051_transcription.tex:811–865','31 scans29,31 /MPL_31_002-051_transcription.tex:918–972;1018–1079','Čech refinement spectral sequence and corrected implication graph.','The later p=0 and explicit arrows constrain, but do not replace, uncertain earlier text.')
f('31 scan28 /MPL_31_002-051_transcription.tex:896–905','31 scans28,30 /MPL_31_002-051_transcription.tex:882–917;973–1017','The EGA erratum is an input to the graded/formal comparison.','Both displayed hypotheses and the cited erratum were read.')
f('31 scans35–39 /MPL_31_002-051_transcription.tex:1111–1300','31 scan43 /MPL_31_002-051_transcription.tex:1351–1414','Transfer in simplicial homology and transfer in Tate cohomology are parallel constructions, with different domains.','Consolidator’s comparison; no source claim that the two complexes are identified.')
f('31 scans47–51 /MPL_31_002-051_transcription.tex:1499–1626','31 scan52 /K31-01_transcription.tex:2–27','Field-cohomological-dimension discussion continues into the curve-function-field case.','Both coefficient conventions and the use of Tsen/Artin–Schreier compared.')
f('31 scans56–59 /K31-01_transcription.tex:73–174','31 scan60 /K31-01_transcription.tex:175–219','Closed-restriction counterexamples are followed by an acyclicity-on-all-opens criterion.','Nonflasqueness is not used as a substitute for nonacyclicity.')
f('31 scans65–68 /K31-01_transcription.tex:294–472','31 scans70–81 /K31-02_transcription.tex:2–446','Support dimension and local fraction-field questions feed the simultaneous affine induction.','Definitions, shifts and good-ring qualifications compared in the complete texts.')
f('31 scan86 /K31-02_transcription.tex:593–616','31 scans88,90 /K31-03_transcription.tex:9–65','Density argument continues on reused sheets with torsion-subgroup applications.','The cutoff and continuation were checked, including the incomplete final m condition.')
f('31 scans91–97 /K31-03_transcription.tex:66–278','31 scans98,99,101 /K31-03_transcription.tex:279–345;384–407','Local cover/asphericity lemmas lead to base change, purity and the wild-complement programme.','All leaves read; source assumptions and later questions separated.')
f('31 scan102 /K31-03_transcription.tex:408–436','31 scan100 /K31-03_transcription.tex:348–383','The Krull theorem proof begins and ends on physically reversed reused sheets.','Valuation notation and theorem statements match; absent intermediate proof not invented.')
# Every earlier context target is recorded, with original entry ids rather than
# conflating N-labels after N071b with NOTES_INDEX row numbers.
D=json.loads((R/'outputs/context_register_extract.json').read_text())
meaning={
'MPL_33_002-049 §2':'Earlier S19/étale-cohomology comparison plan, not a theorem establishing a topology comparison.',
'MPL_131 §2':'Earlier representability/multiplicative-type lead; exact group-scheme claims here are checked in SGA3.',
'MPL_131 RN001':'Construction/descent lead at131/002,017; no proof of the present rigidity or residual-H1 claims supplied.',
'MPL_60_036-070 §2':'Earlier norm/averaging lead; neither a common coefficient object nor equality of norm maps is supplied.',
'MPL_11_043-058+56 N045':'Norm-two and compact-to-ordinary pairing lead at56/020; the proposed map to this Tate module remains unspecified.',
'LM7_PUSH C.6':'The earlier return labels a class-two residue classification Proved; that status is quoted as a lead, not adopted or extended here.',
'MPL_131 10':'First-pass descent/representability placement, without the full result or proof.',
'MPL_33_002-049 §93':'Documentary title/pagination comparison lead only.',
'MPL_33_147-181+34_002-017 8.3':'Independent-pagination comparison lead; not evidence for a count on these leaves.',
'Hua, findings register, 31-local-ring-cd-lower-bound':'Earlier reference-not-found candidate at31/023; this run independently matches the clean scope to SGA4X2.4. The unprovided register is not verified.',
'MPL_33_147-181+34_002-017 D21':'Analytic-duality/cohomological-descent lead at33/166; no common complex with the present Čech complex supplied.',
'MPL_106+107 §136':'BISITE/RESIDUE bookkeeping lead; no chain map to the present complex supplied.',
'MPL_14_002-044 §107':'Earlier effectivity question; not a supplied solution of formal vector-bundle or Picard existence.',
'MPL_33_147-181+34_002-017 11':'Bibliographic-method lead, not a new mathematical identification.',
'MPL_11_043-058+56 §117':'Bibliographic-method lead, not evidence deciding the EGA erratum ink.',
'WG2 §2.1 #2':'Unchecked graded-endomorphism/projector plan. The present associated-graded direct-image module is not identified with that algebra.',
'WG H9':'Unchecked cycle-pairing/Lefschetz hunch; no map from cycles to these endomorphisms is supplied.',
'LM7 E.23':'Earlier return calls the Fermat-tower/class-two section problem Open; arithmetic/profinite marking is not identified with this abstract stabilizer quotient.',
'MPL_142_001-093 §316':'Fundamental-group methodological lead with no supplied earlier scan endpoint.',
'INTAKE LM7_CONTINUED §?':'Intake-only E.37/continuity reading; no referee verdict or common Tate correction module supplied.',
'MPL_60_002-035 §2':'Local-symbol/norm lead, not a theorem supporting the unqualified norm-unit converse.',
'MPL_91_099-143 §68':'Adic/thickening lead at91/124,126,128; no precise completion–Tate theorem supplied.'}
project=[]
for key,d in D.items():
 ids=[f'MPL_31_002-051#{n}' for n in d['entries']]
 its=[i for i in I if set(i['sources'])&set(ids)]
 row=dict(kind='our projects',**{'from':'; '.join(i['id']+' /31 scans'+','.join(map(str,i['scans']))+' /'+i['lines'] for i in its),'to':key+' / '+d['metadata']},what=meaning[key],evidence='Both ends of the supplied note-to-context citation were inspected in the Pro notes. Target register/manuscript was not supplied or independently checked; this is strictly an earlier-run lead, not a corroborated result or established endpoint.',note_ids=';'.join(ids))
 L.append(row);project.append(row)
fields=['kind','from','to','what','evidence','note_ids']
for filename,rows in [('links.tsv',L),('our_project_leads.tsv',project)]:
 with (R/filename).open('w',newline='') as f:
  w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'links':len(L),'published':sum(x['kind']=='published work' for x in L),'internal_folder':sum(x['kind']=='folder' for x in L),'context_leads':len(project)}))
