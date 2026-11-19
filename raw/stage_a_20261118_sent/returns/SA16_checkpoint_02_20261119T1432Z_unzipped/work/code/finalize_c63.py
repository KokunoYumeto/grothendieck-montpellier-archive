#!/usr/bin/env python3
"""Final, manually authored reconciliation after reading the primary sources.

This supplements build_c63.py; no verdicts or mathematical judgments are inferred
from keywords. Run this script, rather than the preliminary serializer, to obtain
the final cote-63 registers.
"""
import build_c63 as b
import json,csv,re

C={a['id']:a for a in b.claims}; P={a['id']:a for a in b.problems}
def revise(n,**fields): C[f'C-SA16-{n}'].update(fields)
def problem(n,**fields): P[f'MP-SA16-{n:02}'].update(fields)

# Printed section numbers, checked against the actual Antwerp page images.
for a in b.claims+b.problems:
    for k,v in list(a.items()):
        if isinstance(v,str):
            a[k]=v.replace('Serre1973','SerrePadic1973').replace('Maier2007','Maier2009')
        elif k=='refs': a[k]=[x.replace('Serre1973','SerrePadic1973').replace('Maier2007','Maier2009') for x in v]
revise(802,fate='Tate1975 §2 and Deligne1975 §1 give the coordinate changes. The generic model requires the negative c6 sign independently calculated here.')
revise(804,computation=C['C-SA16-804']['computation'].replace('§2','§3'),fate='Tate1975 §3 gives the local minimal equation theorem and the obstruction over a general Dedekind base.')
revise(805,fate='Tate1975 §3 gives the minimality bounds; §§7–8 give the algorithm, including the wild residue characteristics.')
revise(806,statement=C['C-SA16-806']['statement']+' In addition, E0(K) has finite index in E(K), as stated in Theorem4.1 on scan7. This component-group finiteness does not require a finite residue field, whereas the reduction quotient E0(K)/E1(K) can be infinite when the residue field is infinite.',present_status='As of November2026: Established. The component quotient E(K)/E0(K) is finite under these hypotheses; finiteness of the residue field is needed for the finite point-count and Haar-volume setting, not for Theorem4.1’s component index.')
revise(808,computation='c63_kodaira.py verifies the four exact point-count/Euler-factor identities. Each reduction coset has minimal-differential volume 1/q; multiplication by the component index gives the total volume.',fate='Tate1975 §5 gives precisely this measure normalization and formula.')
revise(809,computation='c63_kodaira.py checks the affine component counts and computes Smith normal forms of the associated A, D and E Cartan matrices. It covers I_n and I_n* for 1≤n≤20 and every exceptional type. The lattice-to-component-group identification is carried from the geometric classification, not established merely by drawing a graph.',fate='The Kodaira/Néron classification is reproduced in Tate1975 §6; §§7–8 give its effective tests.')
revise(810,statement='For an elliptic curve over a complete DVR with perfect residue field, Ogg’s formula is f=v(Δ_min)+1−m, where m counts geometric irreducible components. Outside residue characteristics 2 and 3 the additive discriminant valuations are 2,3,4,6,n+6,8,9,10. In the additive case f=2 and p≠2,3, multiplication by 12 is an automorphism of E0(K): this follows from its formal subgroup and additive reduction quotient. Since E(K)/E0(K) is killed by 12, the natural map E(K)[12]→E(K)/E0(K) is an isomorphism. The additive hypothesis is essential.',computation='c63_kodaira.py checks f=0,1,2 for the good, multiplicative and tame additive rows. The 12-torsion assertion is independently proved: for any coset represented by P, solve 12Q=12P uniquely in E0(K), giving the unique 12-torsion lift P−Q. No finite table is substituted for the wild Ogg theorem.')
revise(811,computation=C['C-SA16-811']['computation'].replace('Tate1975 §6','Tate1975 §§7–8'))
revise(816,fate='Deligne1975 §2, pp.58–59, gives this rigidified normal form.')
revise(817,fate='Deligne1975 §3, p.60, gives this gauge on the open where 2 and c4 are units.')
revise(818,fate='Deligne1975 §4, pp.61–63, treats the characteristic-2 and characteristic-3 normal forms.')
revise(819,fate='Deligne1975 Proposition5.1, p.63, classifies the geometric singularity by Δ and c4; Tate1975 §1 gives the same criterion.')
revise(820,fate='Deligne1975 Proposition5.3, pp.64–65, gives the finite unramified Isom scheme and its surjectivity criterion. Proposition5.4 treats generic quadratic twisting.')
revise(821,fate='Deligne1975 §5, pp.67–68, records these groups. A relative automorphism group scheme need not have only two global sections on a disconnected base.')
revise(822,fate='Deligne1975 §6, pp.69–71, gives the integral and exceptional-characteristic rings; Katz1973 supplies the modular interpretation.')
revise(823,statement='In characteristic 2 the Hasse section is represented by a1. In characteristic 3 it is represented, up to the sign normalization of Frobenius and the invariant differential, by b2; Deligne1975 Remark6.3 explicitly prints −b2. Both have weight p−1 and cut out the supersingular divisor. The intrinsic definition uses Frobenius/Verschiebung over arbitrary characteristic-p bases. Over a perfect field every ordinary elliptic curve has its Serre–Tate canonical lift to Witt vectors. This does not give a canonical lift for supersingular curves or an unqualified universal coefficient formula.',refs=['Deligne1975','Katz1973','Katz1981SerreTate'])
revise(827,refs=C['C-SA16-827']['refs']+['Maier2009'])
revise(829,fate='Guerzhoy2006 Theorem1 gives eventual normalized congruences for 13,17,19,23 under its rationality and pole hypotheses. Guerzhoy2010, remark after Theorem1, gives a modulus p^(m−C) for these four primes. This supplies an additive threshold for that theorem’s class, but neither reference makes the sharp C=0 assertion for 17,19,23. The higher-dimensional p=29,31 discussion is separate.',refs=['Guerzhoy2006','Guerzhoy2010','SerrePadic1973','Katz1973'])
revise(832,computation='c63_numerics.py checks n=0,1,2, reaching partition index 416301. Its packed Newton inverse is independently compared with Euler’s exact recurrence through index3000. These checks are finite.',fate='Atkin1969 records the exact progression in the copied paper. EichhornEngleKronholm2022, equation(2), repeats it, but their reference[3] is the 1954 Atkin–Swinnerton-Dyer paper and does not establish a 1960s first-publication date. Atkin1968Density is a checked bibliographic lead; its full proof was not accessible. The exact first circulation date remains unassigned.',fate_date='Recorded in the 1969 exposition; first discovery/publication not independently fixed in this run.',present_status='As of November 2026: Established in the literature and reproduced exactly in the archived author’s exposition; this run checks three cases and does not claim a new all-n proof.',refs=['Atkin1969','Atkin1968Density','EichhornEngleKronholm2022'])
revise(834,fate=C['C-SA16-834']['fate']+' Guerzhoy2010 gives quantitative m−C bounds for j at the four primes in the remark following Theorem1.',refs=C['C-SA16-834']['refs']+['Guerzhoy2010'])
revise(835,fate='Guerzhoy2006 gives eventual congruences for its stated class of functions. Guerzhoy2010 supplies modulus p^(m−C) for j at 13,17,19,23; its displayed quantitative theorem does not assert the same rate for every F in Conjecture3. Literal uniqueness of functions is false: uniqueness must concern residue classes or a specified normalized eigenline.',refs=['Atkin1969','Guerzhoy2006','Guerzhoy2010','Maier2009'])
revise(835,statement='In Conjecture3 the level prime is q≤23 and the auxiliary Hecke prime p differs from q. For every integer α≥1, the page asks for normalized functions Fα on Γ0(q), holomorphic on the upper half-plane, zero at infinity and with possible poles at0, with integral Fourier coefficients satisfying the stated Hecke congruences modulo q^α and compatibility F_(α+1)≡Fα mod q^α. For each admissible F it asks for a fixed β such that, for every α≥1, Uq^(α+β)F≡k+k_(αβ)Fα mod q^α, with constants k and k_(αβ). The one-dimensional assertion is thus modulo the constants. The next page discusses a distinct larger-prime extension. Literal uniqueness of actual functions Fα is false: at q=13, replacing Fα by Fα+13^αg² with g=(η(13τ)/η(τ))² preserves all residue conditions, normalization and pole restrictions but changes the function.')
revise(836,statement='Refinement of C-SA16-835: Fα is a residue class modulo p^α, or a normalized vector in a specified p-adic eigenline. Eventual convergence ∀α∃M(α) alone does not imply M(α)≤α+β. For j and p=13,17,19,23, Guerzhoy2010 supplies the quantitative exponent m−C and hence an additive threshold; its printed theorem does not assert this for every F in the manuscript. The unrestricted formulation, coefficient ring, exceptional primes and uniqueness module still need specification. Serre’s p-adic modular-form topology is the uniform coefficient valuation, not merely coefficientwise convergence.',fate='Guerzhoy2010 Theorem1 and its following remark quantify the j case; SerrePadic1973 §1.1 defines the p-adic function space. Neither proves literal uniqueness or the unspecified all-prime/all-function formulation.',fate_date='Serre1973; Guerzhoy preprint2008, publication2010.',present_status='As of November 2026: Quantitative convergence is established for j in the cited scope. An identical rate for every admissible F is not established by the opened theorem; the claim is kept separate from its proved specialization.',refs=['SerrePadic1973','Katz1973','Guerzhoy2006','Guerzhoy2010'])
for n in [838,839]:
    C[f'C-SA16-{n}']['refs'].append('Stark2007')
revise(839,computation='c63_numerics.py recomputes all reduced primitive form counts and evaluates every listed singular modulus at 130 decimal digits. It supplies an analytic bound on the omitted q-series tail. Floating-point rounding is not interval-certified, and numerical agreement does not prove integrality or completeness of the class-number-one list.')
revise(848,statement='For the coefficient α of the real structure, discriminant normalization ω^12=Δ leaves a μ12 choice, under which α changes by a μ6 phase. Thus (α/|α|)^6 is invariant. The independent derivation gives phase(E2*(τ)^6/Δ(τ)), away from the square and equilateral zero orbits. This is a real-analytic modular invariant, not automatically a holomorphic or algebraic rational function of j.',computation='The period/quasiperiod calculation in hodge_proof.md and c63_hodge.py proves the formula, its transformation law and its zero-locus qualification.',fate='Katz1976 supplies the real-analytic weight-2 comparison coefficient. The exact normalized phase formula is derived in this run from that coefficient and the discriminant transformation law; no external priority claim is made.',present_status='As of November 2026: The invariant formula asked for on the page is supplied with its domain. Questions about limiting phase at the zeros are separate and not developed here.',confidence='high')
revise(847,computation='c63_hodge.py verifies M=[[a,(|a|²−1)/β],[β,ā]], M·M̄=I and detM=1 with β=−2iρ. An independent review corrected the first dossier draft’s lower-right minus sign; the initial failed residual is retained. At τ=i, a=0,ρ=1,σ=−1/4 contradict the archived scalar sign. At τ=3i the same program verifies a≈1−π with an analytic Fourier-tail bound, contradicting |a|≤1.')
revise(855,statement='The crossed draft proposes sending a generic-fibre cycle to the special fibre of its schematic closure and descending this operation modulo rational equivalence. Its displayed number(7.11.2) belongs to a draft arrangement. The matching published question is Grothendieck’s SGA6, ExposéX §7.14, especially(7.14.2) and the following difficulty about undefined special-fibre intersections. In the published setup the base is a DVR and the family is flat of finite type, with quasi-projectivity for Chow groups. Fulton’s later theorem treats flat quasi-projective schemes over an excellent DVR and defines specialization on integral Chow groups.',status_on_pages='open on the pages; the attempted argument is crossed and “Je dis” is replaced by “Il faudrait montrer”',computation='No numerical calculation occurs. Both the supplied fragment and SGA6 X§7.14 were read. Fulton1975 §§4.1–4.4 was checked for the Gysin descent, the equality i* i*=0 in its properly typed form i^* i_*=0, and the resulting unique specialization map. The printed proof, not an unproved formal closure operation, supplies the rational-equivalence step.',**{'class':'A'},fate='The same question and obstruction occur in Grothendieck’s own SGA6 X§7.14 (1971). Fulton1975 §4.4, pp.164–165, proves the excellent-DVR quasi-projective form, after the rational-equivalence lemma in §4.1. Thus classA records the published question; its subsequent solution is by another author, a secondary classB fate.',fate_date='SGA6 seminar1966–1967, publication1971; Fulton manuscript received20August1974, publication1975.',present_status='As of November 2026: Identified published question; the scoped specialization theorem is established. The cancellation remains part of the diplomatic evidence and is not treated as proof or disproof.',refs=['SGA6','Fulton1975','FultonIntersection'],confidence='high',attribution='Grothendieck; identified draft of the SGA6 specialization discussion')
revise(856,refs=['Deuring1941','SerreBourbaki1973'],fate='The letter’s further discussion cannot be identified without its surrounding correspondence. Deuring’s publication metadata is independently recoverable from SerreBourbaki1973’s bibliography and publisher records.')
revise(829,fate='Guerzhoy2006 Theorem1 gives eventual normalized congruences for 13,17,19,23 under its rationality and pole hypotheses. Guerzhoy2010, remark after Theorem1, gives modulus p^(m−C) specifically for j at these four primes, hence an additive threshold in that specialization. It does not extend that quantitative assertion to every F, and neither reference establishes the sharp C=0 assertion for17,19,23 by this argument. The higher-dimensional p=29,31 discussion is separate.',computation='c63_algebra.py checks the matrix, irreducibility of the slope polynomial, determinant11 and M^840=I over F29. Thus M^841=M, the reported Frobenius-sized recurrence; the period is not being claimed to equal841. It does not prove all higher-power lifting claims.')
revise(845,fate='Katz1976 Lemma4.0.7 proves the CM direction; Question4.0.8 on p.501 states the exact converse. Bertrand1978 §6 Conjecture3, printed p.36-10, reformulates it; Waldschmidt2004 p.277 still records the corresponding G2* transcendence question. Spence2018 Theorem5.8 proves finiteness of maximal special subvarieties, not that every algebraic (j,chi*) pair is CM. Searches through19November2026 found no verified resolution of the exact converse. Schneider’s algebraic-tau theorem alone does not answer it.',refs=['Katz1976','Bertrand1978','Waldschmidt2004','Spence2018','MOHodgeCM2010'])
problem(266,state_of_art='Katz1976 Lemma4.0.7 proves the CM implication and Question4.0.8 states the exact converse. Bertrand1978 §6 Conjecture3 and Waldschmidt2004 p.277 retain this converse as a question. Spence2018 Theorem5.8 concerns maximal special subvarieties and does not classify all individual algebraic (j,chi*) values. No verified resolution was found in targeted searches through19November2026; this is a medium-confidence search conclusion, not a proof of global openness.',refs=['Katz1976','Bertrand1978','Waldschmidt2004','Spence2018','MOHodgeCM2010'])
for a in b.claims+b.problems:
    if 'refs' in a:a['refs']=list(dict.fromkeys(a['refs']))

problem(260,state_of_art='Guerzhoy2006 proves eventual convergence for its class. For the specific series j−744, Guerzhoy2010 Theorem1 and following remark supply exponents (μ−1)m−C for p=5,7,11 and m−C for p=13,17,19,23. Literal uniqueness is refuted by adding p^α g². The unrestricted all-function rate is not supplied by those printed theorems.',refs=['Atkin1969','Guerzhoy2006','Guerzhoy2010','SerrePadic1973'])
problem(242,occurrences=['C-SA16-811;H63-02 scan14 physical line430'],state_of_art='Tate1975 §§7–8 give the algorithm; the conductor formula and m=ν+5 imply ν≤v(Δ)−6. Therefore the page’s tentative ν≤v(Δ)−3 is a valid weaker bound, not a false inequality.',worth='Worth documenting the valid weak bound and its stronger consequence in the companion; no separate modern research project is needed.')
problem(261,occurrences=['C-SA16-859;H63-07 scan63 physical line285'])
problem(277,plausible_today='Let R be an excellent DVR and X flat and quasi-projective over R. Closure followed by the special-fibre Gysin map defines CH_p(X_K)→CH_p(X_k). In a smooth setting it is compatible with intersection products.',state_of_art='The exact question is published in SGA6 X§7.14, equations(7.14.1–2); its final paragraph isolates the failure of the naive rational-equivalence argument. Fulton1975 §§4.1–4.4 proves the needed descent and functorial specialization under the stated excellent-DVR hypotheses.',why_open='The source itself says that special-fibre intersections used in the proposed argument need not be defined. The crossed draft visibly encounters that same obstruction; the reuse of the sheet adds no further mathematical conclusion.',worth='The mathematical problem is settled in the cited scope; the useful next task is textual comparison with the final SGA6 wording.',refs=['SGA6','Fulton1975'])

# Reading alarms preserve the diplomatic source. Published parallels can share a typo.
b.readings[:]=[a for a in b.readings if a['line']!='H63-02:430']
# The tentative nu bound is true (though weak): no mathematical reason to alter ink.
for a in b.readings:
    if a['line']=='K63-02:24-62': a['alternative']='Check conjugates and β inverse against M=[[a,(|a|²−1)/β],[β,ā]]'
    if a['line']=='H63-03:168': a['evidence']+=' The same omission is visible in the published Deligne1975 p.57 formula; it may be an inherited source typo, not a transcription error.'
    if a['line']=='H63-08:bibliography': a['evidence']=a['evidence'].replace('Serre1973','SerreBourbaki1973')
b.R('H63-04',34,'269-281','b2 as the characteristic-3 Hasse section','Compare the sign normalization: Deligne1975 Remark6.3 prints −b2','The published p.71 image was inspected. The zero divisor is unchanged, but an equality of normalized sections needs the Frobenius/differential convention.','medium','medium')

# Directly read folder endpoints: these are links, not invented Pro entry rows.
for frm,to,what,evidence in [
 ('63:H63-01 scans4–5','63:K63-01 scans36–37;H63-09 scans87–91','Repeated Weierstrass invariants and coordinate changes.','All three formula sets read; independent polynomial residuals in c63_algebra.py and c63_more_algebra.py isolate sign and omitted-factor variants.'),
 ('63:H63-02 scan10','63:H63-04 scans24–31','Reduction types and small-characteristic automorphisms.','Both use Weierstrass forms, but reduction over a DVR and automorphisms over a field are distinct claims.'),
 ('63:H63-03 scans15–24','63:H63-04 scans25–34','Continuous Deligne text: duality, equations, normal forms, automorphisms and modular forms.','Adjacent manuscript and transcription sections read; later printed ordering checked on pp.53–71.'),
 ('63:H63-05 scans42–48','63:H63-06 scans49–55','Continuous Atkin report on congruences and numerical experiments.','First paper’s continuation read; primes13 and17–23 do not share every proved bound.'),
 ('63:H63-05 scans46–48','63:H63-07 scans61–64','The numerical conjectures are reformulated as congruence Hecke operators.','Both passages read; literal uniqueness and iteration-depth quantifiers compared explicitly.'),
 ('63:H63-08 scans80–81','63:K63-01 scans67–71','CM tables versus Hodge/quasiperiod questions.','Both ends read; class-number-one enumeration is not a proof of the de Rham algebraicity converse.'),
 ('63:K63-01 scans67–71','63:K63-02 scans73–77','Hodge calculations continue into real-structure and discriminant-phase normalization.','The exact cross-term signs and the involution matrix are rechecked in c63_hodge.py.'),
 ('63:H63-04 scans32–34','63:K63-02 scans96–100','c4/c6 divisors and their mixed-characteristic local equations.','Both ends read; multiplicity and tangent claims are distinct from characteristic-p Hasse interpretation.'),
 ('63:K63-02 scan98','63:K63-02 scan100','The distinct-tangent claim is later retracted to equal tangents.','Both places read; exact mixed-characteristic factorization refutes the later retraction, without changing either reading.'),
 ('63:K63-01 scans70,72','63:K63-02 scan101','Reused sheets preserve unrelated Banach-algebra and intersection-theory fragments.','All fragments read; no elliptic implication inferred merely from their physical placement.')]:
    b.L('folder',frm,to,what,evidence)
for frm,to,what,evidence in [
 ('63:H63-01 scans4–8;H63-02 scans9–14','Tate1975 §§1–8, pp.33–52','The archived letter is Tate’s text, later printed as his algorithm paper.','Archive title/text and opened Antwerp index/page images compared; attribution retained as Tate.'),
 ('63:H63-03 scans15–24;H63-04 scans25–34','Deligne1975 §§1–6, pp.53–71;Deligne1968 M/68/28','The copied Deligne text and its preprint/publication sequence.','Archive heading and equations compared with actual printed pages; IHES catalog verifies the1968 preprint.'),
 ('63:H63-03 scans15–17','EGAIII §7.8.4,§7.8.6,§7.9.9','Cohomology, base change and local freeness used by the genus-one construction.','Numdam EGAIII2 pp.73–78 read; constant fibre dimensions alone were not used over a nonreduced base.'),
 ('63:H63-08 scan78','SGA4 XII5.1;XVI1.2;SGA7II XXI5.2.2;Deligne1974','The preface’s cohomological program and later Weil/integrality theorems.','Archive preface read; proper and smooth base-change coefficient hypotheses checked separately in the published statements.'),
 ('63:K63-02 scan101','SGA6 ExposéX §7.14, equations(7.14.1–2), final paragraph','A published occurrence of the same specialization question and obstruction.','Both ends read; the draft number(7.11.2) changes to(7.14.2), and the published text explicitly retains the gap.')]:
    b.L('published work',frm,to,what,evidence)

# Actual mathematical checks. A source comparison is not promoted to a re-proof.
computation_ids=[801,802,803,807,808,809,810,815,817,818,821,824,825,826,827,828,829,830,831,832,839,840,841,842,843,844,846,847,848,849,850,851,852,853,857,858]
for n in computation_ids:
    a=C[f'C-SA16-{n}'];b.E(a['id'],'computation or formal certificate',a['computation'])
proof_ids=[804,805,806,812,813,814,816,819,820,822,823,828,833,835,836,843,844,847,848,849,850,851,852,853,854,855,857,858]
for n in proof_ids:
    a=C[f'C-SA16-{n}'];typ='independent re-proof' if n in [843,844,847,848,851,852,853,854,857] else 'targeted proof check'
    b.E(a['id'],typ,a['computation'])
for n in [811,824,825,826,827,828,829,830,834,836,837,838,839,845,850,855,856]:
    a=C[f'C-SA16-{n}'];b.E(a['id'],'carried as background without fault found','Exact literature-scope comparison: '+a['fate'])
refinements=[]
for n,refined,text in [
 (802,'C-SA16-803','The generic model has c6=−c4.'),
 (821,'R-SA16-821','The generic automorphism functor is the constant order-two group scheme; sections can vary on connected components.'),
 (824,'R-SA16-824','For the7-part the corrected lower bound is floor((b+2)/2), for b≥1.'),
 (835,'C-SA16-836','Uniqueness must be stated modulo p^α or in a specified normalized eigenline.'),
 (841,'R-SA16-841','The characteristic-2 order24 group is not a common supergroup of all geometric automorphism groups; the characteristic-3 group of order12 cannot embed in it.'),
 (847,'R-SA16-847','With the printed definitions 4ρσ=|α|²−1; no universal bound |α|≤1 follows, and τ=3i is a counterexample.'),
 (851,'R-SA16-851','The four mixed-characteristic tangent lines are distinct; the local group action contains a nontrivial transvection.')]:
    b.E(f'C-SA16-{n}',f'refuted, with refined statement {refined}',text+' Evidence: '+C[f'C-SA16-{n}']['computation'])
    if refined.startswith('R-'): refinements.append({'id':refined,'source_claim':f'C-SA16-{n}','statement':text})

# Conservatively repair obvious prose joins, without touching quoted archival text,
# IDs, equations or source labels. This is typography, not classification.
fix={'OverZ':'Over Z','overZ':'over Z','OverQ':'Over Q','overC':'over C','overS':'over S','overF':'over F','theHesse':'the Hesse','theCM':'the CM','theDVR':'the DVR','aDVR':'a DVR','theSL':'the SL','theF4':'the F4','the13':'the 13','the196':'the 196','the202':'the 202','forp13':'for p13','forp5':'for p5','atp13':'at p13','onΓ':'on Γ','inΓ':'in Γ','ofΓ':'of Γ','invariantΔ':'invariant Δ','allfour':'all four','all-αpartition':'all-α partition','notidentifiable':'not identifiable','specifiedprime':'specified prime','everyprime':'every prime','dependingon':'depending on','groupoforder':'group of order','andsmall':'and small','andno ':'and no ','givefour':'give four','givesfour':'gives four'}
for a in b.claims+b.problems:
    for key,value in a.items():
        if isinstance(value,str) and key not in ['id','his_statement','lines']:
            for old,new in fix.items(): value=value.replace(old,new)
            a[key]=value

registry=b.P/'reference_registry.json'
if registry.exists():
    for r in json.loads(registry.read_text()):
        typ='used and rechecked in this run' if r['note']=='verified' else 'carried as background without fault found'
        b.E(r['key'],typ,r['verification_scope']+' Locator: '+r['locators'])
b.save()
(b.P/'refinements.json').write_text(json.dumps(refinements,ensure_ascii=False,indent=2)+'\n')
