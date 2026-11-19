# Part A.5--A.7 working research notes

AI-produced by GPT-6 Astra (OpenAI); independent research/check run 2026-11-19. No priority claim. This file records live state, not a claim that the overall assignment is complete.

## Scope and source reading

Read the supplied transcriptions for cote67/048--051 and084--101, especially `MPL_67_002-052_transcription.tex` lines1046--1105,1807--1886, and `MPL_67_053-101_transcription.tex` lines1017--1277,1278--1353,1468--1582,1723--end. Checked relevant rows of the study corrections and HUNCHES. The images are not yet obtained: uncertain readings are being kept explicit.

Opened primary sources: Mochizuki2006 Semi-graphs of Anabelioids (PDF), Mochizuki2007 Combinatorial Version (PDF), Hoshi--Mochizuki2011 (revised author PDF), Alling1981 preview (preface and0.10 only), Milne2021 EC2 (web PDF), Bakalov--Kirillov2000 (arXiv PDF), Stukow2004 (Numdam PDF), Conrad SL2(Z) AppendixC. Bibliographic/source-access evidence will be consolidated in `sources/part_a567.bib`.

## Decisive findings already proved

1. **A.5 proposition:** over algebraically closed k of char≠2, V≅C2² has normalizerS4 of order24. The bijection V↔S4-subgroups holds also in char5. RecoveringV from its six fixed points fails exactly char5: for S=P1(F5), its projective stabilizer has120 elements and there arefiveV with thisS. General proof: deleting an antipodal pair leaves a harmonic quartet; deleting a nonantipodal pair leaves crossratio±i, harmonic only ifchar5 (char2 excluded). Hence the antipodal pairing, andV, are recovered in every other characteristic. Exact program tests24 odd primes<100 with120 projective triple candidates each; output attached.
2. **A.5 theorem/L7:** correct groupoid is quotientstack[U/S4], U=P1\{0,1,∞}, S4 action factoringS3. Coarsemoduli is A1 with J=(λ²−λ+1)^3/(λ²(λ−1)²). OverR=Z[1/2,i] the canonical octahedral construction descends by torsors andworkschar3,5. Generic automorphismV must be retained. This is not an equivalence with the coarseaffineline asgroupoid.
3. **A.7 new correction:** the prior correction to67/091 (SpecR connected, evenRdomain) does NOT make eigenspaces of a rank2 projective module invertible. Counterexample R=Z[x,y,z]/(x²+yz−1), M=R², σ=[[x,y],[z,−x]]. Atm=(2,x−1,y,z), P=ker(σ−1)=im(σ+1) has minimal numberofgenerators2 andgenericrank1. Exact matrixfactorization provesit. The full categorical eigenspace/gluing equivalence is sound. Dedekind/PID or2invertible withconnectedbase give safe rankone corollaries.
4. **A.7 PID count:** nonsplitclasses are (R/2R)^×/image(R^×); R=Z[(1+√−11)/2] is normEuclidean with coveringnorm≤15/16, hasunits±1, residueF4 andthree nonsplitclasses. The splitclass addsone. ForZ exactlyone nonsplitclass.
5. **A.7 realcurves:** E_a=C/(Z+i√aZ), E'_a=C/(Z+(1+i√a)Z/2), both withconjugation, a>0, are distinct complete pointedrealelliptic classes. On fixed complexcurve, genericstructures form {E_a,E_1/a} or {E'_a,E'_1/a}; squarecase {E_1,E'_1}; hexagonal {E'_3,E'_(1/3)}. H1(R,E_a)=Z/2, H1(R,E'_a)=0; nontrivialtorsor antiholomorphic involution z↦barz+1/2 isfree and quotientKleinbottle.
6. **A.6 literal49(b):** withoutmaximality/saturation a cyclotomic invariantprocyclic subgroupI yields infinitelymanynI, so the proposed barecriterion is not a bijectionwithnodes/marks. Ordinaryétalefundamentalgroup versuslogarithmicgroup is a separate necessarydistinction.
7. **A.6 presentation:** SL2 and GL2 presentations on050 are correctwith reflectionrelationsr_i²=1 stated. Correct matrices r1=diag(−1,1), r2=[[0,1],[1,0]], r3=[[1,1],[0,−1]]. PureMod0,4 isfreeofrank2, notPSL2Z; fullgroupquotientbyitsKlein4 isPSL2Z, andthe stabilizerofonedistinguishedmark isPSL2Z. The two transcribedassertions involvingT^{+!}_{0,4} cannotbothmeanpuremappingclassgroup.

## Current gates requiring work

A.6(a),49(a): need exact reconstructionofnormalpropagatortensor from arithmeticlog fundamentalgroup, inadditiontostabledualgraph and hyperboliccomponentreconstruction. Mochizuki2007 Remark2.8.1 suggests this buthasexplicitfield/action hypotheses; do not erase them.

A.6(a),49(c): manuscript asks todefine a generalanabeliancompactification, withnoaxioms fixed. Ordinaryfundamentalgroup doesnotdistinguishboundaryblowups; a purportedgeneralanswer needschoice/minimalityandnewreconstructiontheorem. No suchtheorem establishedinthisrun.

NB048: 'threeclasses' ambiguous; completeprofiniteconjugacyclasses areinfinite. Need avoid silentlychoosinganinterpretation.

A.6(b): full source-checked comparisonofpants/Lego/involutions andBirmansequence tobe written; exact lowcomplexityexceptions retained.

## Computations

`code/part_a567_checks.py` exact finite and symboliccheck. 24oddprimes3..97,120triples each(2880candidates). All pass; characteristic5 stabilizer120/fiveKlein groups, others24/one. Symbolicmatrix, unit-group andhexagonal checks pass. Runtime recordedinoutput. Initialreflectionchoice failed, then structuralSymPy-equality failed; bothinitialscripts/outputspreserved; correctedfinalscriptpasses. No mathematicalresult wasclaimedonthefailedchecks.

## Independent review to root

Checked root A.1 Koebeq≤16 obstruction against67/074--079: sound forliteralunrestrictedtangenttensor target. Checked rootA.2 Schwarziansecondjet proof: coefficients andbformula consistent; two lengthtriplesproduceb=1/2 and5/4. These are targetedproofchecks, notindependentfullreproofsofroot'ssourceidentifications.
