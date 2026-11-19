"""Manually selected mathematical reading alarms and checked links; event ledger."""
from pathlib import Path
import csv,json,datetime
W=Path(__file__).resolve().parents[1]
def tsv(name,fields,rows):
    with (W/name).open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(fields);w.writerows(rows)
rr=[]
def r(c,s,l,a,b,e,w='high',conf='mathematical alarm high; ink undecided'):
    rr.append([c,s,l,a,b,e+' No scans or second-pass corrections were supplied.',w,conf])
r(8,79,'3–25','ℓ with superscriptG/C; f⁻¹ versusf*','Retain distinct sheaf inverse image and derived ringed-topos pullback.','The two functors have different tensor factors; Codex corroborates the distinction, not the ink.')
r(8,80,'47–64','Deleted flatness ofO_S overΛ','Do not restore the deleted condition.','Locally free end cohomology modules suffice for the Postnikov base-change argument.','medium')
r(8,81,'70–78','p² versusn² after n=p inserted','p² is consistent with the live prime-specific representation-lifting question.','Composite n and prime p are different lifting problems; insertion changes the quantifier.')
r(8,81,'79–83','pour toutM in H² injection','Locally constant π-moduleM, with the indicated universal-coverH¹ vanishing.','Cartan–Leray does not justify an arbitrary sheaf version.')
r(9,3,'151–159','p-operation and F/V on the reduced module','Check operator and Frobenius twist before identifying tangent p-power.','Covariant and contravariant conventions exchange F,V; duality diagram constrains the reading.')
r(9,3,'160–176','Pro:G sans tore; Codex:G* sans tore','Starred dual if intended as the connected-dual criterion.','μ_p∞ is connected but has an étale dual; it distinguishes the statements.')
r(9,3,'169–176','H^(2|1)(G,Ga)','Read the superscript on the scan; no degree selected here.','The surrounding Dieudonné realization does not uniquely fix the ambiguous cohomological model.','high','low textual confidence; ink undecided')
r(9,'5,7','196–242;303–335','W_n with F^(n+1),V^(n+1) truncations','Determine whetherW_n denotes lengthn orlengthn+1.','Exact small-ring pairing is perfect with targetZ/p^(n+1), degenerate with targetZ/p^n under the specified exponents.')
r(9,5,'220–223','CanceledF^iV^i↦0 and coefficientλ00','Keep canceled; normal-form coefficient includesp^i.','FV=p makes diagonal monomials contribute unless the target kills that power.')
r(9,5,'204–239','Finalφ(Fz)=φ(zF)= left unfinished','Compare with liveσ-twisted identity above.','In nontrivial Witt Frobenius the un-twisted equality can fail; coefficient calculations requireσ.')
r(9,7,'303–335','Finite bimodule isomorphism live inPro, canceled inCodex','Cancellation to be decided on the scan.','The witnesses disagree materially; standard duality cannot decide a strike-through.')
r(9,8,'336–365','u·V=π(u∘F)','Compare later precomposition byV_g, with the correct twist.','F=J3,V=0 makes the literal dual operators violateFV=0.')
r(9,8,'365–392','λ_g/λ_d and F_g/F_d,V_g','Retain side labels rather than combine coefficient actions.','The twoW-actions in the bimodule model differ by Frobenius; the page itself saysATTENTION.')
r(9,9,'393–425','Order of composition in canceled torsor lemma','Check f∘g versusg∘f and the missing final conclusion.','Type checking depends on composition order; the entire sheet is canceled.','medium')
r(9,11,'433','inégales caractéristiques with insertedin','Retain mixed-characteristic qualification.','The historical Tate theorem invoked is not an unqualified equal-characteristic result.')
r(9,12,'458–468','SuperscriptG versusG/I on representation group','Residual quotient acts on both inertia andW(k′).','Ordinary conjugation invariance would omit the semilinear coefficient action.')
r(9,13,'474–478','M(o) versusM(0)','Likely firstp-torsion level, but indexing must be read.','The argument usesμp andthe mod-p module; a shifted level would change the comparison.','medium')
r(9,'13,14','478–485','T_ℓ for anyℓ','ℓ≠p Tate inertia, or an appropriate finitep-adic comparison realization.','Good reduction need not make rawT_p inertia finite. The finite character cannot be that literal representation.')
r(9,14,'482','Trace=n=dimA','For the full realization rank is2dimA.','At the identity the trace must be the rank; the same sheet gives elliptic trace2.')
r(9,14,'484–485','G⊂Aut(A_s′); faux parTate margin','G may mean inertia after unramified closure; locate margin’s intended target.','Full residual Galois action is semilinear. Both witnesses leave the margin without a definite leader.')
r(9,18,'545–563','DiscreteGL_g overk','Constant finite groupGL_g(Fp).','Unit-F local systems have finiteFp fibers; algebraicGL_g,k has positive dimension.')
r(9,19,'589–604','A[p](k) over a perfect field','Geometric points with Galois descent or the associated étale sheaf.','OrdinaryE/F5:y²=x³−x has no nonzero rational5-torsion but a one-dimensional tangent space.')
r(9,20,'605–640','Canceledt_A*→t_A versuslivet_A→t_A*','Keep live direction and check the transpose convention.','The homomorphism attached to a line bundle isA→A*, while alternating duality can introduce a sign.')
r(9,'21,22','641–674','L/ω and determinant of tangent without dual','ω_A=det(t_A)^∨; section belongs toω_A^(p−1).','Taking determinant of t_A^(p)→t_A fixes the line exponent and dual.')
r(9,24,'737–740','Q_ℓ versusQ_p and leftward arrow','Check coefficient and arrow; normalized ordinary map isp-adic.','The preceding comparison usesℓ≠p, but this construction usesT_p(A)_et.')
r(9,25,'773–779','Δ(ψ)/δ(φ|ψ)','For comparison of normalized maps, denominator should trackthe same polarizationψ.','Otherwise the displayed multiplicative reduction does not follow.')
r(9,25,'789–793','u* versusRosatiu′; conjugation exponent−1','Distinguish Cartier dual map from Rosati involution.','The proof ofΔ(u*)=Δ(u) uses conjugacy in the positive symmetric case, not allu.')
r(9,26,'808','CanceledT_p(u)_et=T_p(u*)_et withoutdet','Missingdet is possible, but even determinants are unequal for arbitraryu.','Codex also has no determinant sign. Preserve cancellation and do not silently repair.')
r(9,27,'831','Q_p/Z_p; herm/hom; canceledZp[T]∩Q[T]=Z[T]','The polynomial is on the Rosati-self-adjoint subspace and rational coefficients suffice.','The integer-ring intersection is false; values on integral coordinates give rational coefficients by interpolation.')
r(9,27,'832–835','Δ versusδ on the square root; v versusw','The multiplicative determinantΔ(w²)=Δ(w)² proves the sign.','Using an undefined square-root functionδ would not be the same polynomial argument.')
r(9,28,'850–857','Kernel(p) decoration and parentheses','p-primary component, distinct from Frobenius twist.','The valuation argument compares orders of étale and multiplicativep-primary kernels.')
r(9,28,'866–880','u*⁻¹ versusu*; inserteddet','Retain inverse dual and bothdet signs.','The product equals1 forautomorphisms; individual determinants need not agree.')
r(9,29,'901–909','Final comparison lacksdet; biduality sign?','Keep it a determinant-line comparison; do not infer full module isomorphism.','For dimensiong>1 a rank-one determinant line cannot be a rank-g Tate module.')
r(4,2,'938–968','ss superscript/subscript;T_lib/H_lib;Tor/Tors','Superscript refers toV, subscript toF; read each degree separately.','Duality exchanges stable operators with a shifted torsion degree; ordinary semisimplification is a different functor.')
r(4,3,'969–997','p≠2 historical attribution; shifted torsion degree','Check the historical qualifier but preserveH^(i+1)[p] inUCT.','Modern smooth-proper crystalline base change includesp2; the exact sequence requires the next cohomological degree.')
r(4,'3,4','1000–1048','Live reference to canceled(8.2.1)','Keep reference as surviving after cancellation, not as a validated formula.','The canceled Gysin route cannot supply a missing premise of the amended argument.')
r(4,7,'1105–1119','Cokerw replaced byH^n_cris[p]_st; oldkerw end canceled','Use the inserted torsion term and final0.','The later dimension and bijectivity corrections are coordinated with this replacement.')
r(4,7,'1115–1119','n−1/n+1 and faintKatz/Faux margin in deletedw','Scan check only; no reconstructed claim from the faint margin.','Gysin degree shift matters, but the formula is canceled and the annotation is not recoverable.','medium','low textual confidence; ink undecided')
r(4,7,'1124','E^(n−1)(Y|X); geometricFrob versus inverse GaloisFrob','Vanishing cohomology belongs toY; retain inverse convention.','The variable section isY and its critical dimensionn−1; arithmetic and geometric eigenvalues invert.')
r(4,'7,8','1129–1145','Cancelednegativekerw corrections','Use onlydimH^n[p]_st−dimker v in the live identity.','Restoring the deleted terms contradicts the amended exact sequence.')
r(4,9,'1179–1183','Growthto∞ replaced by>0; absentsection7','Distinguish positivity from growth and record unavailable internal endpoint.','SGA7XXI1.4 proves positivity; it cannot identify the missing manuscriptsection7.')
r(4,9,'1191–1204','p-linear semisimple over imperfectk;constantkernel;degree superscript','Use relativeF*E≃E andcheckH^n versusH^(n−1).','An imperfect-base absolute semilinear inverse is not the unit-F structure. Kernelconstancy needsker v control.')
r(4,10,'1216–1230','surjective replaced byinjective,doncbijective; dual torsionn+1','Preserve corrected criterion and itsker v0 qualification.','φ is already surjective in the live exact sequence; the oldresp cases are canceled.')
r(4,11,'1254–1260','General equivalence ofφ-bijectivity with equality of free-rank inequality','Check whether a missing hypothesis kills preceding-degree stable torsion andker v.','Independent derivation gives defectb+c butdimkerφ=c−dimker v.')
r(4,11,'1262–1269','H¹(X)=0; truncatedZ/;H²[p] versusH²⊗k','InterpretH¹ ascrystalline here and distinguishp-torsion kernel fromtensor quotient.','The universal-coefficient argument producesH²[p], not allH²/p; Codex corroborates the group endingZ/p.')
r(4,11,'1271–1277','Canceledprojective-spaceproduct stable term','Keep canceled; positive-degreeTate classes havezeroF-stable reduction.','The proposed factor does not supply slope-zero classes.')
r(4,12,'1280–1312','Fullπ1 image,arithmetic/geometric;rankr≥2;conditionalpointcounts','Separate monodromy groups andretain finite-extension/every-open qualifiers.','Arithmetic cosets can restrict Frobenius classes even when an arithmetic image islarge.')
r(4,12,'1280–1296','n≥2 insertion and ambiguous parenthesisX=P^(r=1)','Retain the n=1 boundary exclusion.','ForP1, monodromy on the d-point quotient factorsS_d; p3,d3 gives at most6 elements, versus48 forGL2(F3). This does not refute n≥2.')
tsv('readings.tsv','cote scan line reading alternative evidence weight confidence'.split(),rr)

ls=[]
def l(kind,a,b,what,e,ns):ls.append([kind,a,b,what,e,ns])
l('folder','cote8:78,otherPropackage2755–2799; rootP78-I062 (root remaps)','cote8:79,3–25;P894-I001','Direct continuation ofco-Lie character formula','Both endpoints read;79 begins the additionalΛ-coefficient calculation.','MPL_8_079-081+9+4+100##1;##2')
l('folder','cote8:80,50–64','cote100:37,2192–2216','Earlier-run comparison ofdegree-two obstruction and completion','Both endpoints read. Different deformation problems; no canonical comparison proved. Cote100 endpoint outsideTOPIC.','MPL_8_079-081+9+4+100##5')
l('folder','cote9:19,564–604','cote4:6,1065–1088','Earlier-run comparison ofunit-F étale sheaves andstabledeRham augmentation','Both endpoints read; connection throughFrobenius descent anddualization, not literal equality ofallobjects.','MPL_8_079-081+9+4+100##57')
l('folder','cote9:23,689–713','cote100:3,1346–1392','Earlier-run comparison ofordinaryextension datum andreconstruction from(A_U,M,φ)','Both endpoints read; structural lead only. Cote100 excluded fromtheSA15claimscensus.','MPL_8_079-081+9+4+100##73')
l('folder','cote9:25,793','cote9:27,831–836','Intermediate sign doubt isresolved bypositive-Hermitian square-root proof','Direct continuationread; ends cqfd.','MPL_8_079-081+9+4+100##79;##85;##86')
l('folder','cote4:7,1105–1108','cote4:10–11,1216–1221;1250–1271','Amendedtorsionsequence changesφfailurefromsurjectivity toinjectivity','Both revisions read againstProandCodex.','MPL_8_079-081+9+4+100##120;##136;##137;##138')
l('published work','cote8:79–80,3–64','BerghRydh2019,AppendixB,PropositionB.4','Exactderivedco-Lie formula','The primaryPDFproofandbothmanuscriptpagesread; modernsourceisnotGrothendieckauthorship.','MPL_8_079-081+9+4+100##1;##3')
l('published work','cote9:3,128–176','Oda1969,Theorem3.19;Corollary5.11','DieudonnédualityanddeRham/Hodge realization','Exactpublishedobjectschecked; uncertainstarsandoperatorsremaininkquestions.','MPL_8_079-081+9+4+100##11;##12')
l('published work','cote9:23,697–713','Katz1981,Theorem2.1','Explicitordinaryformaldeformationextensionparameters','Matcheslocaldeformationquantifiers, notallglobalbases.','MPL_8_079-081+9+4+100##71')
l('published work','cote4:6,1065–1088','SGA7IIXXII,Theorem3.3,(3.3.4),p411','StabledeRhamaugmentation','Exactformula verified inKatzchapterofSGA7; do notattributeauthorshiptoGrothendieck.','MPL_8_079-081+9+4+100##115')
l('published work','cote4:9,1173–1183','SGA7IIXXI,Theorem1.4,pp374–376','Genericlarge-degreepositiveHasse–Wittvanishingrank','Exactall-Cohen–MacaulayX theoremread; absentmanuscriptsection7notidentified.','MPL_8_079-081+9+4+100##129')
l('published work','cote4:12,1295–1312','SGA7IIXXII,Corollary3.2,pp410–411','Tracecongruenceingredient','Publishedtraceformula suppliesoneingredient; monodromyconclusion remainsconditional.','MPL_8_079-081+9+4+100##146')
tsv('links.tsv',['kind','from','to','what','evidence','note_ids'],ls)

claims=json.loads((W/'claims.json').read_text());items=json.loads((W/'items.json').read_text());refs=json.loads((W/'reference_evidence.json').read_text())
who='GPT-6 Astra Pro; effort setting not exposed; SA15-20261119/cotes8_9_4'
events=[]
for x in items:
    events.append([x['id'],'2026-11-19',who,'used and rechecked in this run','Source-fidelity check of notes against the cited diplomatic passage and relevant Codex witness: '+x['check']+'. '+x['check_reason']+' This is not a claim of proving the mathematics.'])
computations={6,12,14,23,28,31,38,40,57,67,71,75,80,82}
independent={5,7,19,21,22,23,25,28,31,38,53,57,64,67,71,75,78,80,82}
targeted={1,2,3,4,8,9,10,15,27,29,30,32,33,35,37,39,40,41,43,45,49,50,54,55,56,58,60,63,69,70,72,76,79}
refuted={6:6,14:15,22:21,23:23,25:25,31:30,38:39,69:67,71:71,72:72,77:77}
for x in claims:
    n=int(x['id'][-3:])
    typ='independent re-proof' if n in independent else ('targeted proof check' if n in targeted else 'carried as background without fault found')
    outcome=('Scope/quantifier audit, with limitations: ' if typ=='carried as background without fault found' else 'Mathematical argument checked at the stated scope: ')+x['fate']
    events.append([x['id'],'2026-11-19',who,typ,outcome])
    if n in computations:events.append([x['id'],'2026-11-19',who,'computation or formal certificate',x['computation']+' Finite tests do not imply an untested general theorem.'])
    if n in refuted:events.append([x['id'],'2026-11-19',who,'refuted, with the refined statement\'s id','Literal/overbroad assertion refuted or its formal implication shown to need hypotheses; refined or qualified statement P894-C%03d. '%refuted[n]+x['statement']])
for x in refs:
    typ='carried as background without fault found' if x['read_status'].startswith('metadata') else 'used and rechecked in this run'
    events.append([x['key'],'2026-11-19',who,typ,x['read_status']+'; '+x['locator']+'. '+x['scope']+' No complete proof re-verification is implied.'])
tsv('check_events.tsv',['statement_id','date','who','type','outcome'],events)

# Complete reading ledger for commands made before the span-reader was installed.
with (W/'source_read_log.tsv').open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for path,a,b,note in [
      ('sources/SA15_texts/pro/MPL_8_079-081+9+4+100_transcription.tex',1,335,'Initial readingbeforeutility; reread mathematicalendpointsspanswhilecheckingclaims.'),
      ('sources/SA15_notes/pro/MPL_8_079-081+9+4+100_doubts.md',260,399,'Fullmanualread; reread19Novemberduringfinalreadingsaudit.'),
      ('sources/SA15_texts/pro/MPL_8_079-081+9+4+100_transcription.tex',1089,1280,'Numberedreread corrected cote4itemlocators.'),
      ('sources/SA15_texts/pro/MPL_8_079-081+9+4+100_transcription.tex',714,892,'Numberedreread ofRosatisign,lattice,variance.'),
      ('sources/SA15_texts/pro/MPL_8_079-081+9+4+100_transcription.tex',430,488,'Numberedreread added marginaltrace-integralityclaim.'),
      ('sources/SA15_texts/pro/MPL_8_079-081+9+4+100_transcription.tex',196,242,'Numberedreread added everycoefficientidentity.'),
    ]:w.writerow(['2026-11-19',path,a,b,'GPT-6 Astra Pro / cotes8_9_4',note])
    for name in ['K4-01','K8-01','K9-01','K9-02']:
      path='sources/SA15_notes/codex/'+name+'_notes.md'
      count=len((W.parents[1]/path).read_text().splitlines())
      w.writerow(['2026-11-19',path,1,count,'GPT-6 Astra Pro / cotes8_9_4','Fullyreadinitiallyandrereadfinalaudit;leads,noverdictrows.'])
print('Wrote',len(rr),'readings,',len(ls),'checkedlinks,',len(events),'checkevents; completedreadingledger.')
