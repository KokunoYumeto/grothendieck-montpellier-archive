"""Integrate checked findings after checkpoint04; this creates no checkpoint."""
from pathlib import Path
import csv, datetime

ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/'work'; PACKAGE=WORK/'package'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
paper=PACKAGE/'DELTA23.tex'
text=paper.read_text()
old='''quotient lead to a complete finite list of normalized conjugators,
of which thirty-six survive the checked first-subgroup test.
The corresponding raw product-fixed cover is also preserved.'''
new='''quotient lead to a complete finite list of normalized conjugators.
Uniqueness of the full first value and the literal raw pentagon
reduce that list from thirty-six conjugators to six, with three
mixed values each. Cubing and actual complex conjugation reduce
the existence question further to three explicit pairs.
Every retained pair nevertheless passes the complete finite
common-word and mixed-cycle tests; none is asserted to lift to GT.
The corresponding raw product-fixed cover is also preserved.'''
assert old in text
text=text.replace(old,new)
old='''coupled Hurwitz action leaves thirty-six necessary conjugators
after the checked tests. Their full free-word compatibility
and the raw cover constraints remain under investigation.'''
new='''coupled Hurwitz action, first-value uniqueness and raw pentagon
leave six conjugators and eighteen pairs. D23.C30--C31 reduce
actual mixed existence to the three pairs $(1,0),(19,0),(27,2)$.
Their realization or exclusion in full GT remains open.'''
assert old in text
text=text.replace(old,new)
anchor='\\input{proofs/hurwitz_raw_simultaneous_covariance.tex}'
extra='''
\\input{proofs/hurwitz_raw_solvable_quotient.tex}
\\input{proofs/hurwitz_raw_pentagon45.tex}
\\input{proofs/hurwitz_raw_survivor_covariance.tex}
\\input{proofs/hurwitz_mixed72_gentle_core.tex}
\\input{proofs/hurwitz_full_mixed_gentle_core.tex}
\\input{proofs/hurwitz_mixed45_cycle_link.tex}
\\input{proofs/hurwitz_full_commonword.tex}
\\input{proofs/pure_frame_abelian_constraints.tex}
\\input{proofs/hurwitz_mixed_source_intertwiners.tex}
\\input{proofs/hurwitz_candidate_power_normalization.tex}
\\input{proofs/hurwitz_complex_conjugation_normalization.tex}'''
assert anchor in text and extra not in text
text=text.replace(anchor,anchor+extra)
old='''complete finite list now has thirty-six necessary conjugators.
The full mixed commutator fibers have size $432$ each, and the
first-pair maximal solvable quotient has order $93312$.
The remaining common-word cycle and raw-cover constraints are
active work; no geometric coordinate-deletion compatibility is
assumed. All finite candidate arrays are retained with their
precise check status.'''
new='''complete finite list initially had thirty-six necessary conjugators.
D23.F36 fixes the full first value uniquely. D23.H8 then imposes
the complete third-pair derived membership, and D23.P26 imposes
the literal raw pentagon. These are actual necessary restrictions
and leave six conjugators with three mixed values each.
D23.C30--C31 use powers and actual complex conjugation to reduce
mixed existence to three pairs, not to a claim of their existence.

D23.H9/F38 proves that every one of the eighteen raw survivors
has a single ordinary commutator word realizing all five values
and every mixed orientation. D23.P27 also gives full raw braid
covariance. D23.H10 and P28 distinguish the necessary derived-pure
cubic frame from an arbitrary finite conjugator and show that
each of the three existential normal forms passes that test.
These finite statements do not impose the free gentle identities
or construct an actual full-GT lift.

The active next comparison is a five-puncture Hurwitz action
with four local classes $\\mathcal C$ and one inverse class,
including its order-five pure-frame coboundary. Its construction
and tests are retained as working calculations until separately
proved and checked. Other noncentral orbital comparisons remain
available. No geometric coordinate-deletion compatibility is
assumed, and all finite candidate arrays retain their check status.'''
assert old in text
text=text.replace(old,new)
anchor='\\item L. Alp\\"oge, \\emph{Remark}, supplied four-page PDF:'
assert anchor in text
text=text.replace(anchor,'''\\item P. Lochak and L. Schneps, \\emph{A cohomological interpretation
of the Grothendieck--Teichm\\"uller group}, Invent. Math. 127
(1997), 571--600: equation~(2), p.~572; Theorems~1--2,
p.~573; Proposition~4, p.~574.
\\url{https://webusers.imj-prg.fr/~pierre.lochak/textes/inventiones.pdf}.
'''+anchor)
paper.write_text(text)

qfile=PACKAGE/'QUESTIONS.tsv'
with qfile.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)
for row in rows:
    if row['id']=='Q2-main':
        row['findings_or_current_gate']='D23.H2 normalizes mixed actual GT to rho0,a3=1,a2=0. F36 gives unique fullF_V; H8 reduces36V to12Vx3R; P26 rawpentagon leaves6Vx3R. C30 cubing andC31 actual complex conjugation reduce existence to three pairs(1,0),(19,0),(27,2). Needexcludeallthree actualsource realizations or constructone. H9/F38,P27,P28 show statedfiniteword/covariance/frame tests stillpass.'
newrows=[
('Q2-first-value-unique','Prompt','item2 route','Is the full first Hurwitz value uniquely determined by each necessary conjugator?','proved','D23.F36: centralizer argument and centerless perfect residual forceF=F_V; no unenumerated first-value branch.'),
('Q2-pentagon45-base','Prompt','item2 route','Does complete third-pair membership shrink the necessary actual candidate list?','proved','D23.P25,H8: H=[D,F_VR]; all7776 fibers tested, leaving12V with3R each.'),
('Q2-raw-pentagon','Prompt','item2 route','Does the literal raw pentagon further exclude normalized candidates?','proved','D23.P26: unique rawpair lifts and exact completedB4 identity leave6Vx3R; rejectedpartners have nonconstant order2 fiberdefects.'),
('Q2-raw-full-covariance','Prompt','item2 route','Do all eighteen raw survivors admit simultaneous raw braid covariance?','proved at finite scope','D23.P27: each has exactly6 canonical linear lifts, differing byglobaldeck; noactualGT lift inferred.'),
('Q2-raw-solvable','Prompt','item2 route','What is the exact marked solvable quotient restored by raw block framings?','proved','D23.F37: literal unprojectivized Burau group331776; centralC3 liesinderived; allfivepairimages retainunique values.'),
('Q2-mixed-full-gentle','Prompt','item2 route','Do the full six mixed orientations and cycle tests exclude any of the eighteen survivors?','refuted at specified finite scope','D23.C27-C28: all18 pass fullcyclicderivedmembership, reflected consistency, and induced norm equations; nofreegentle lift.'),
('Q2-mixed45-cycle','Prompt','item2 route','How is the third pentagon-pair value related to the full mixed cycle?','proved','D23.C29: exact B4 identity relates45 to mixedyz for every commutatorword; all18 agree.'),
('Q2-five-full-commonword','Prompt','item2 route','Does one common commutator word realize all five values and full mixed orientations?','proved at finite scope','D23.H9/F38: all18 have a common ordinaryword with allfive unique rawlifts and literalpentagon; noactualgentle orfullGT realization.'),
('Q2-pure-frame-constraints','LM7_PUSH','E.65.1,E.65.11','What abelian constraints apply to the actual cubic and harmonic pure frames?','proved','D23.H10: A in closedFprime; betaab=(-rho,-rho),rho even. NormalizedC12² images require cubicderived and harmonic0or(6,6).'),
('Q2-finite-source-frames','Prompt','item2 route','Do finite source surjectivity and derived-pure frame conditions exclude the remaining normal forms?','refuted at specified finite scope','D23.P28: all18 sourceimages generated; eachof6V has a survivingpair with onecommon derivedpure intertwiner, including allthreeC31forms.'),
('Q2-power-normalization','Prompt','item2 route','Can actual-source powers reduce the existential candidate list?','proved','D23.C30: V_n=V^n,R_n=V^n(R^-1V)^-n; cubesof18pairs areexactlyfour involutivepairs, preservingmixedcharacters.'),
('Q2-conjugation-normalization','LochakSchneps1997','Theorem1,p573; newHurwitz calculation','Can actual complex conjugation reduce the four cube-normalized cases?','proved','D23.C31: eta-correctedinverseclass realization ofW; swaps(19,0)/(23,1), leaving threeexistentialforms(1,0),(19,0),(27,2).'),
]
existing={r['id'] for r in rows}
for values in newrows:
    assert values[0] not in existing
    rows.append(dict(zip(fields,values)))
with qfile.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(rows)

events=[
('D23.P26','targeted proof check','PASS: whole proof read; central completedB4 kernel and exponent12 injectivity independently checked. Fresh root raw45/base group orders and all36rawpentagons PASS; sixVxthreeR necessaryactual reduction.','agents/pentagon/hurwitz_raw_pentagon45.tex; records/root_hurwitz_raw_pentagon45_recheck.log'),
('D23.P27','targeted proof check','PASS: whole proof read and fresh full18pair replay; unique markedrawlifts, connected fourvertex potentials and literal8064A/B/C/deck equations checked.','agents/pentagon/hurwitz_raw_survivor_covariance.tex/.py'),
('D23.F37','targeted proof check','PASS: whole proof read; Schreier local-abelian action, complete markedmatrix graph and globalcentralderivedC3 argument checked. Fresh block construction and995328matrixedge replays PASS; separate pairmarkings replay recorded oncompletion.','agents/five_level_six/hurwitz_raw_solvable_quotient.tex; records/root_hurwitz_raw_block_recheck.log; records/root_hurwitz_raw_burau_recheck.log'),
('D23.C27','targeted proof check','PASS: whole proof read and fresh fullmixed72S3certificate rerun; eightacceptedresidues andallC26fiber projections checked.','agents/characters/proofs/hurwitz_mixed72_gentle_core.tex; agents/characters/code/hurwitz_mixed72_s3_core.py'),
('D23.C28','targeted proof check','PASS: whole proof read; reflectiongraphs, theta²=Adx, C12²abelianization, sixinducedblocks andmembership-to-commonword implication checked. Exactrecordedgroup/norm certificates inspected; this event doesnot claim a freshrootlargecore rebuild.','agents/characters/proofs/hurwitz_full_mixed_gentle_core.tex'),
('D23.C29','targeted proof check','PASS: whole proof read and fresh faithfulArtinfree4 identity/18value replay; centralinput factors cancel for everycommutatorword, notjustactualgentle words.','agents/characters/proofs/hurwitz_mixed45_cycle_link.tex; agents/characters/code/hurwitz_mixed45_cycle_link.py'),
('D23.H9/D23.F38','targeted proof check','PASS: both full proofs read; jointderivedmembership viaC12² andSLP exponentcorrection, exactfirstperfect adjustment, reflections, C29andunique fivepairrawlifts checked. F38 isparallelproof ofsamefinding. Freshrootstrongerjointreplay separatelyrecorded oncompletion.','notes/hurwitz_full_commonword.tex; agents/five_level_six/hurwitz_full_core_commonword.tex'),
('D23.H10','targeted proof check','PASS: whole proof reread after five independentreproof; integral det3 argument givesAab0, E65.11givesrhoeven and normalizedtwoharmonicclasses. Nofinite3torsion cancellation used.','notes/pure_frame_abelian_constraints.tex'),
('D23.P28','targeted proof check','PASS: whole proof read and fresh complete18intertwiner replay. Exact2952point identities implygeneration; sixderivedpure intertwiners includeallthreeexistentialforms. Other12notclaimedtofailallframes.','agents/pentagon/hurwitz_mixed_source_intertwiners.tex/.py'),
('D23.C30','independent re-proof','PASS: whole proof read, GTcomposition derived directly, U=R^-1V implementsfreeaction, givingR_n=V^nU^-n. Fresh18pair powerreplay producesfourcubes; actualcharacters preserved. Existentialnormalizationonly.','agents/characters/proofs/hurwitz_candidate_power_normalization.tex; agents/characters/code/hurwitz_candidate_power_closure.py'),
('D23.C31','targeted proof check','PASS: whole proof read and fresh eta/inverseclass/uniqueW/full18action replay. Targetpostcomposition commutesprecomposition, proving actualc-conjugacy realization; characterdecoders andthreeform reduction checked.','agents/characters/proofs/hurwitz_complex_conjugation_normalization.tex; agents/characters/code/hurwitz_complex_conjugation.py'),
('LochakSchneps1997.eq2.Theorem1','used and rechecked in this run','PASS: authorprimaryPDF opened andexacteq2p572/Theorem1p573 read. GTcomposition and actualcomplexconjugation c=(-1,1) supportC30-C31. Theorem2IIIprimep573 read foractiveorderfivepureframe route, notyet a newexclusion.','https://webusers.imj-prg.fr/~pierre.lochak/textes/inventiones.pdf; InventMath127(1997)571-600'),
]
with (WORK/'records/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for ident,typ,outcome,locator in events:
        writer.writerow([ident,now,'GPT-6 Astra Pro; inherited effort not exposed; run DELTA23; /root',typ,outcome,locator])

with (PACKAGE/'LEDGER.md').open('a') as f:
    f.write('''
## Working update after review 1: three actual-source normal forms

Recorded '''+now+'''. This is a working entry, not a scheduled formal review; the no-movement counter remains0 and the next review is02:59UTC.

The main necessary gate has become strictly smaller within the same Hurwitz representation. F36 proves uniqueness of the complete first value, closing the possible unenumerated perfect branch. H8 exhausts all36×216 mixed fibers and leaves12V with3R each. P26 then proves the literal raw pentagon is required in completedB4 and excludes every even partner, leaving6V with3R each. C30 replaces a hypothetical actual mixed element by its cube and reduces existence to four pairs. C31 uses actual complex conjugation to identify two of those. The resulting main gate is actual full-GT realization or exclusion of the three pairs(1,0),(19,0),(27,2), always in the normalizationrho0,a3=1,a2=0.

The finite ordinary-word gates have also been resolved at their precise scope. C28,C29,H9/F38 give one ordinary commutator word realizing every prescribed first/mixed orientation and allfive rawpentagonvalues for all18P26survivors. P27 gives rawcovariance. H10 establishes the actualderivedpure cubicframe constraint, and P28 shows that the three normalforms pass this and the harmonicfinitecoset constraint. None of these finitepasses gives an actualgentle orfullGT lift.

Originalquestions1,3,4,5 retain the states and gates of review1. The active main followup is the fullfive-puncture Nielsen orbit with classpatternfourC+ oneC− and the orderfivepureframe coboundary ofLochak-Schneps1997 Theorem2. This working route is not counted as a result before its proof and checks.
''')

with (PACKAGE/'IMPLICATIONS.md').open('a') as f:
    f.write('''
## Strict necessary reductions after checkpoint04

F36,H8,P26 now eliminate candidates inside the fixed actual-GT Hurwitz test, reducing36 necessary conjugators to6 and18 fullpairs. The rejected raw pentagons have nonconstant ordertwo fiber defects, so allowing a global deck scalar would not repair them. C30-C31 then give three existential normalforms by actual-source operations: cubing and conjugation by complex conjugation. This is a smaller main gate, while A.84 remains open.

C28,C29,H9/F38 resolve a different question: each surviving finitepair has one ordinary commutator word realizing allfivevalues and allmixedorientations. P28 also supplies the relevant finitepureframes for every existentialnormalform. Consequently these finiteword and frametests cannot finish the proof. The missing step is actualprofinite compatibility or a new necessary obstruction. The orderfiveframe in the larger sphericalNielsen action is being investigated separately. None of these statements changes the stated complexity or historical implications.
''')
print('Integrated three-form main gate, eleven proof inputs, twelve question rows and twelve root check events; no checkpoint created.')
