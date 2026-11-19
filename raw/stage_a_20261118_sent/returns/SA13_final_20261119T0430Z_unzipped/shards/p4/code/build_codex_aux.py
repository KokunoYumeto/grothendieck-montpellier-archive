"""Authored stages 3--5 for the fully read Codex K34-05--08 extension.

This is serialization of individual research decisions, not keyword verdicting.
Run after build_codex.py; the merge preserves the independent core records.
"""
import csv, json
from pathlib import Path
import build_codex as b

OUT=b.OUT
P=[]
def problem(n,title,locations,as_stated,modern,state,why,worth,refs,claim_ids):
    P.append(dict(id=f'MP-SA13-{n}',title=title,
      occurrences=[p for k,a,z in locations for p in b.L(k,a,z)],
      as_he_states=as_stated,plausible_today=modern,state_of_art=state,
      why_open=why,worth=worth,refs=refs,claims=[f'C-SA13-{i}' for i in claim_ids]))

problem(230,'An adic local-to-global spectral sequence',[(5,118,128),(5,331,340)],
 'Can the finite-coefficient nearby-cycle spectral sequence pass to the proposed ℓ-adic limit with constructibility and suitable projective systems?',
 'Use compatible constructible adic complexes and derived inverse limits; finite global groups alone do not justify an ordinary inverse limit of sheaves.',
 'Deligne SGA4½, Finitude3.2, and the later adic nearby-cycle formalism supply constructibility. This resolves the missing finiteness input, with a modern categorical formulation.',
 'The author explicitly reserves limit verifications and adds the constructibility/system requirement.',
 'A precise comparison of the manuscript inverse-system conventions with the derived formulation is useful; a new finiteness theorem is not suggested.',
 ['P4_DeligneFinitude1977','P4_Illusie2021'],[803,805,848,852])
problem(231,'The smooth-case transition multiplier',[(5,130,141)],
 'Reduce to X=S and verify the support-cohomology transition written as multiplication by the finite field-extension degree.',
 'The divisor class pulls back by the ramification index e. Field degree is equal to e only after suitable residue/defect hypotheses; a tame ℓ-power tower still kills the colimit.',
 'Absolute purity and Gysin functoriality establish the corrected multiplier. The explicit imperfect-residue extension in proof_audit.md §11 has [L:K]=p and e=1.',
 'The verification is explicitly left to the reduction X=S. No reason beyond that omission is documented.',
 'High-value short correction: retain the smooth-acyclicity proof but replace its multiplier and state the killing tower.',
 ['P4_Riou2014','P4_Illusie2021'],[806,807,808])
problem(232,'What is the Griffiths result referred to here?',[(5,367,384)],
 'A normal-crossing monodromy discussion refers to a result of Griffiths without a complete citation.',
 'Identify the exact text and the particular bound, filtration or complex-geometric hypothesis intended before assigning a publication match.',
 'The general i+1 monodromy bound is independently verified in Illusie2021 Theorem2.3. The precise Griffiths bibliographic identity remains unresolved: class F, not an unproved mathematical conjecture.',
 'The supplied passage gives no complete bibliographic locator.',
 'Worth an archive/ink and correspondence lookup; thematic Griffiths citations are not an adequate identification.',
 ['P4_Illusie2021'],[819,820])
problem(233,'Absolute purity for regular schemes',[(6,79,117)],
 'Every regular scheme should satisfy the stated cohomological purity theorem; mixed characteristic is historically singled out as unproved.',
 'For a regular closed immersion of codimension c between noetherian regular schemes, with n invertible, Ri!Λ≃Λ(−c)[−2c].',
 'Gabber absolute purity, as proved in Riou2014 ExposéXVI Theorem3.1.1, settles this formulation without an excellence assumption. The coefficient invertibility remains necessary.',
 'The manuscript explicitly states the historical conjecture and available restrictions; its written context is not a present-day claim.',
 'Settled. Useful as an exact source-concordance task and for checking every subsequent twist and shift.',
 ['P4_Riou2014'],[824,825,826,827])
problem(234,'The second square in the residue diagram',[(6,493,538)],
 'The two localization sequences and cup products should form a morphism of exact sequences; the second square is admitted pending verification.',
 'Choose the Kummer boundary and Gysin conventions together. The boundary is a graded derivation; the sign depends on whether the Kummer class is the left or right cup factor.',
 'Riou2014 §§2--4 gives Gysin and Kummer compatibility, including an explicitly opposite root-torsor sign in Lemma3.4.8. proof_audit.md §12 provides the derived localization verification in a fixed convention.',
 'The author explicitly says the second square seems to need checking.',
 'Worth a small fully signed lemma, especially before implementing the exterior-power formula; no unresolved purity theorem remains here.',
 ['P4_Riou2014'],[829,834,836])
problem(235,'The coefficient scope of principal-divisor restriction',[(6,413,478)],
 'Restriction from the partially punctured strict-local scheme to the last divisor is asserted to be an isomorphism in the displayed induction.',
 'The sufficient inherited hypothesis is that the locally constant coefficient extends to the original strict-local X. Arbitrary locally constant coefficients on U′ need not satisfy the restriction assertion.',
 'The Artin--Schreier example in proof_audit.md §12 disproves the broad interpretation. The inherited coefficient scope is a reading problem; the repaired assertion for coefficients extending to X is verified. It is not an unresolved modern theorem.',
 'No explicit authorial doubt is attached to the scope; this is a mathematically motivated reading problem, not an attributed open question.',
 'High value: inspect the carried F-convention before treating the induction as a general theorem with arbitrary local coefficients.',
 ['P4_Riou2014','P4_IllusieLog2002'],[833])
problem(236,'Resolution and the full nearby-cycle programme',[(7,444,475),(7,541,585)],
 'It seems plausible that resolution-based nearby-cycle results extend to excellent traits in all characteristics, and to arbitrary U with the full rather than tame sheaves.',
 'Separate the geometric resolution conjecture from constructibility and quasi-unipotence of nearby cycles. The latter have proofs that do not settle the former.',
 'Deligne Finitude3.2 supplies constructibility and Illusie2021 Theorem2.3 gives monodromy. Temkin2024 still formulates the relevant general local-uniformization/resolution problems; no proof of arbitrary resolution was identified.',
 'The manuscript expressly calls both extensions plausible. No authorial reason for abandoning them is inferred.',
 'Do not pursue broad resolution as a short project. A worthwhile finite task is to inventory which exact consequences survive without it.',
 ['P4_DeligneFinitude1977','P4_Illusie2021','P4_Temkin2024'],[850,851,852,854])
problem(237,'Wild inertia on a normal-crossing degeneration',[(7,580,612)],
 'Does wild inertia P act trivially on the full nearby-cycle sheaves, and on proper generic cohomology, under the written normal-crossing and prime-to-p multiplicity assumptions?',
 'Under the corresponding log-smooth normal-crossing hypotheses, compare full and tame nearby cycles; for proper log-smooth families also allow the stated open-stratum version.',
 'Rapoport--Zink1982 §2 and Nakayama1998 Theorem0.1/Corollary0.1.1 settle the tame behaviour. Illusie2002 Theorem8.3 and Corollaries8.4,8.4.3 give the precise log-smooth comparison, including nonvertical situations.',
 'The author explicitly asks the local question and says the global cohomological statement is not then proved.',
 'Settled in the verified hypotheses. Preserve the distinction between trivial wild action and nontrivial tame unipotence.',
 ['P4_RapoportZink1982','P4_Nakayama1998','P4_IllusieLog2002'],[855,856])
problem(238,'The integral monodromy filtration qualifier',[(5,345,383),(7,488,544)],
 'The normal-crossing calculation should give a canonical finite filtration with inertia-trivial graded pieces; the transcription includes a stronger integral purity qualifier.',
 'The rational/integral filtration from the relevant spectral sequence is defined, but saturation of every lattice step requires a distinct argument and may depend on torsion.',
 'The i+1 nilpotence bound is verified. No exact source for the additional saturated/pure integral formulation on this leaf was identified; class C is limited to that qualifier.',
 'This is a distinct reading-and-hypothesis issue; the author does not flag the whole nilpotence theorem as open.',
 'Worth a focused torsion example and source check, after fixing which integral filtration is intended.',
 ['P4_SGA7IIntro','P4_Illusie2021','P4_IllusieLog2002'],[819,853])
problem(239,'A general Kummer tower need not reduce dimension by one',[(8,271,290)],
 'For strict-local noetherian X of dimension n and U=D(t), is cdℓ U(∞)≤n−1 after adjoining all prime-to-p roots of t?',
 'The assertion is false in the stated arbitrary noetherian generality. More restrictive excellent or geometrically normal-crossing settings must be treated separately.',
 'Orgogozo2014 XVIII_B §§2.1--2.4 constructs a dimension-two regular strict-local nonexcellent A with H³(D(t),Z/ℓ)≠0. Since the tower group has cdℓ=1, Cartan--Leray implies cdℓ U(∞)≥2. This last deduction is ours, not a literal statement of Orgogozo.',
 'The manuscript asks the question explicitly and notes that its cited standard conjecture would yield only n.',
 'High-value resolved obstruction. The follow-up is to isolate the best valid additional hypotheses, without calling every narrower variant open.',
 ['P4_OrgogozoDimension2014','P4_IllusieDimension2014','P4_IllusieLog2002'],[868])
problem(240,'Lefschetz consequences and the lci improvement',[(8,291,373)],
 'The global and local Lefschetz bounds are conditional on purity, resolution and affine Lefschetz; a sharper i≤n−d vanishing for lci fibres is deferred.',
 'Use rectified depth, Gabber affine Lefschetz and perverse nearby cycles. If X/S is flat lci of relative dimension n, usual RΦΛ[n] is perverse; support dimension d gives the stated shifted lower bound.',
 'SGA7 I4.5--4.7 proves the historical characteristic-zero local results. Illusie2003 §§2.6,2.7,2.10 extends the depth/lci statements over general traits. Pilloni--Stroh2014 Theorem1.1.2 supplies affine Lefschetz.',
 'The author lists the missing ingredients and expressly defers the sharper assertion.',
 'Settled after precise lci and coefficient hypotheses. A useful task is a single table translating rectified depth and the manuscript shift.',
 ['P4_SGA7IIntro','P4_Illusie2003','P4_PilloniStroh2014'],[869,870,871,872,874])
problem(241,'Checking the pinching counterexample',[(8,348,365)],
 'Pinch two sections together only over the closed point to obtain the example showing the need for the stronger hypotheses.',
 'Two proper connected generic components specialize to a connected special fibre. The map on H0 is diagonal and Φman¹≠0. The special fibre has embedded nilpotent structure at the pinch.',
 'The affine fibre-product construction and H0 calculation are independently checked in proof_audit.md §18; no conclusion that this is a flat lci family is drawn.',
 'The manuscript sketches the example, with a doubtful H exponent; it is not a conjecture.',
 'A useful small example to retain, because suppressing the embedded structure would produce a false lci counterexample.',
 ['P4_Illusie2003'],[873])
problem(242,'Uniformity in the punctured-fibre vanishing premise',[(8,487,534)],
 'A vanishing statement at x is used to deduce vanishing of hypercohomology on the punctured special fibre and the local comparison.',
 'Require the relevant Φman sheaves to vanish throughout the punctured special fibre, equivalently at all its geometric points. An isolated nonsmooth point gives this sufficient condition.',
 'Original SGA7 I4.5 proof(1) explicitly ranges over generizations of x. The corrected inference and degree boundaries are independently proved in proof_audit.md §19.',
 'This is a substantive mathematical omission in the supplied wording; it is not presented as an authorial open problem.',
 'High-value local repair. The omitted point and the punctured support must not be interchanged.',
 ['P4_SGA7IIntro','P4_SGA7XIII'],[878,879,880,881,882])

path=OUT/'problems.json'
old=json.loads(path.read_text())
path.write_text(json.dumps([x for x in old if int(x['id'].split('-')[-1])<230]+P,ensure_ascii=False,indent=2)+'\n')

R=[]
def reading(k,a,z,read,alt,evidence,weight='high',confidence='mathematical high; ink undetermined'):
    for loc in b.L(k,a,z):
        R.append(dict(cote=34,scan=loc['scan'],line=f"{loc['start']}–{loc['end']}",reading=read,alternative=alt,evidence=evidence,weight=weight,confidence=confidence))

reading(5,27,32,'K̄α in the finite-extension term','Kα, reserving K̄ for the colimit geometric field','The displayed filtered system runs over finite subextensions; a bar in each term makes the construction redundant.')
reading(5,110,117,'unindexed support/cohomology sheaf','The q-th support cohomology sheaf in E₂^{pq}','The local-to-global spectral sequence has independent p and q gradings.')
reading(5,130,141,'i≠0 / degree-one support / missing twist / field degree','Purity degree2 with twist(−1); pullback multiplier e, not unconditional [L:K]','Codimension-one purity and the imperfect-residue extension in proof_audit.md §11; several independent possible readings are retained.')
reading(5,166,181,'full I in the nilpotence statement; open U without a geometric bar','The stated open subgroup I′; U over the geometric generic field','The monodromy theorem gives quasi-unipotence before finite base change. A nongeneric-geometric open has extra base Galois cohomology.')
reading(5,184,191,'Yα mapped to itself','The intended finite-level object mapped to Y','The base-change comparison would otherwise be an identity with the wrong target.')
reading(5,249,258,'gα called an immersion','Composite Xα→X→S or the indicated structural map','The Leray expression uses the composite structural morphism; it is not an immersion in general.')
reading(5,317,326,'(n,ℓ)=1 in the tame root tower','(n,p)=1','Tame ramification is prime to residue characteristic p, whereas ℓ-power roots are essential for killing ℓ-primary cohomology.')
reading(5,360,384,'graded pieces trivial under I; integral pure filtration; Griffiths reference','I′ where required; verify the separate saturation adjective and exact Griffiths source','The i+1 nilpotence theorem is verified, but the additional integral qualifier and precise bibliographic identity are not.')
reading(5,391,401,'H*(Y) in the open compactification conclusion','Check H*(U) and the cohomology/support convention','The surrounding compactification argument concerns the open U. SGA7 XIII2.1.9 retains regularity and tame hypotheses at the boundary.')
reading(6,55,67,'Z−Y in the open complement','Y−Z','Z is the regular closed divisor inside Y; the indicated open has the opposite set difference.')
reading(6,120,154,'purity degree1; support/codimension target mismatch','Degree2 for a divisor; H^{i−2d}(Y,F(−d))→H^i(X,F)','The Gysin source is the closed stratum with the codimension shift and Tate twist.')
reading(6,290,299,'deleted U=∪Ui','The live U=∩Ui; do not restore the cancelled union','Removing the union of divisors is the intersection of the individual complements.')
reading(6,332,345,'μX or a Kummer sheaf with no level/site','μn on the relevant open with n invertible','Kummer exactness and the torsor class require a specified invertible n and étale site.')
reading(6,449,478,'locally constant F on U′ without a carried extension hypothesis','Check whether F is still the restriction of a locally constant sheaf on X','The Artin--Schreier counterexample disproves the broad coefficient interpretation; no ink decision is made.')
reading(6,493,538,'unsigned second square of the residue/cup diagram','Fix the Kummer boundary, cup order and Gysin signs together','The graded boundary derivation forces a sign; Riou2014 Lemma3.4.8 uses an explicit convention that must not be imported silently.')
reading(7,19,31,'one μm acting on the simultaneous root cover','μm^r for r independently adjoined roots','The finite cover has rank m^r and independently rotates each root.')
reading(7,223,239,'kernel exactly H for arbitrary n','Require n>1 for a nonzero coefficient representation','For n=1 the module is zero and every group element acts trivially; the coset representation cannot detect H.')
reading(7,329,344,'finite index for the multiplicity map without positivity','Require at least one positive mi; image is gcd(mi) times the tame group','If all mi vanish, the map is zero and has infinite-index image.')
reading(7,411,426,'lcm of all mi including zeros; divπ','lcm of the nonzero vertical multiplicities; divt in the actual base equation','A horizontal divisor has multiplicity0. Including it makes the lcm construction unusable.')
reading(7,553,575,'Rg′*(Ψ) in the Leray input; cancelled quadratic exponent','Rg′*(Λ) in the indicated construction; retain the improved q+1 bound','The source complex and the earlier spectral-sequence estimate are distinct. The cancelled arithmetic expression is not restored.')
reading(7,723,738,'X in the tame stalk formula','The strict localization X′ where the proof is local','The formula computes a stalk at x using the strict-local geometric generic fibre.')
reading(8,69,84,'cross references2.1.1,2.1.2','Check2.1.2,2.1.3 against the displayed deductions','The proof invokes the refined stalk bound and its sheaf counterpart, not two arbitrary preceding formulas.',weight='medium')
reading(8,142,164,'λ as the ordinary generic point','λ must be the geometric generic point of the strict-local trait S1','For r=0 the ordinary field still has nonzero Kummer H1, contradicting the claimed affine bound.')
reading(8,220,250,'dimension condition and unstated generic smoothness in duality','Separate dimXs from the parameter n; restore smooth proper pure-dimensional generic fibre for Poincaré duality','The page later acknowledges generic smoothness in the Lefschetz discussion; the numerical shifts require dimension n.')
reading(8,250,266,'hyperplane codimension d','Codimension d+1','To avoid a d-dimensional closed support, use d+1 sufficiently general hyperplanes; the Gysin degree is2(d+1).')
reading(8,295,309,'SGA1 XIV','SGA2 XIV','The invoked depth/global and local Lefschetz statements are in SGA2, not SGA1.')
reading(8,348,365,'H^(0|1) in the pinching example','H0 and its diagonal specialization map','Two generic connected components and one connected special fibre are detected by H0; the cone gives Φman1.')
reading(8,489,505,'vanishing at the removed point x used on Vs; injective for i≥m−1','Vanishing at every point of Vs; injective for i≤m−1','Hypercohomology needs vanishing on its actual space, and the long exact sequence gives the low-degree range.')
reading(8,509,521,'support at x inside V̄; V(m); unreduced degree','Support inside X̄; X(m); reduced H^{i−1}(V̄)','The punctured V̄ omits x, so its support-at-x group is zero by definition; localization in X̄ gives the one-degree shift.')
reading(8,521,534,'deleted isolé in the nonsmooth-point application','Retain isolatedness in the mathematical hypothesis pending scan inspection','Only then is the punctured special fibre smooth, and only then does its support complex vanish.')
reading(8,536,557,'extension-by-zero sheaf confused with the support complex','j!Λ in triangle B; Ri!Λ/support in triangle A','The two localization triangles have different first terms even though their middle term is the same.')

def merge_tsv(name,fields,new,keep):
    path=OUT/name
    with path.open(newline='') as f:old=list(csv.DictReader(f,delimiter='\t'))
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader()
        w.writerows([r for r in old if keep(r)]+new)
merge_tsv('readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],R,lambda r:r['cote']!='34')

SPECS=[
('P4-S17','SGA7 vanishing cycles cone strict localization geometric generic fibre; Deligne XIII1.3 2.1.4 2.1.9; Illusie Grothendieck vanishing cycles2021',
 'Original SGA7I andII SLMath scans; Illusie authorPDF https://www.imo.universite-paris-saclay.fr/~illusie/Illusie-Grothendieck-nearby-cycles12.pdf',
 'Exact cone and stalk conventions read. The manuscript complex is usual RΦ shifted by−1. XIII2.1.9 is a boundary-base-change proposition with normal-crossing/tame hypotheses, not the general monodromy theorem.',
 ['P4_SGA7IIntro','P4_SGA7XIII','P4_Illusie2021']),
('P4-S18','Deligne Théorèmes de finitude3.2 SGA4½ cycles évanescents constructible; SGA7XIII2.3.1',
 'IAS publications index opened; original https://library.slmath.org/nonmsri/sga/sga/pdf/sga4h.pdf and SGA7II downloaded and selected pages inspected',
 'SGA4½ Finitude3.2 supplies full nearby-cycle constructibility; the older XIII2.3.1 version has its stated characteristic restrictions. Inverse limits require the adic-system formalism.',
 ['P4_DeligneFinitude1977','P4_SGA7XIII','P4_Illusie2021']),
('P4-S19','Gabber absolute purity regular noetherian Riou2014 Theorem3.1.1; Gysin Kummer residue sign3.4.8',
 'Numdam full primary https://www.numdam.org/item/AST_2014__363-364__301_0.pdf',
 'RiouXVI3.1.1,3.1.3--4 and3.4.8 read. The theorem has n invertible and no excellence condition; cup and torsor signs are specified rather than guessed.',
 ['P4_Riou2014']),
('P4-S20','Grothendieck monodromy exponent i+1 SGA7I3.4 Griffiths canonical filtration; Illusie2021 Theorem2.3; pro-p cohomology',
 'Original SGA7I printedp12 image; Illusie2021 authorPDF; Illusie2002 Numdam fullPDF',
 'General i+1 bound verified. Original I3.4 actually prints the off-by-one q′=min(q,max crossings); modern Illusie2002(8.4.4.1) gives min(q+1,logrank). Exact Griffiths identity and extra integral saturation qualifier remain unresolved.',
 ['P4_SGA7IIntro','P4_Illusie2021','P4_IllusieLog2002']),
('P4-S21','resolution singularities excellent schemes positive characteristic current Temkin height reduction; arXiv MathOverflow zbMATH variants',
 'Primary https://arxiv.org/html/2301.09160v2 and publication metadata opened; current2026 search follow-up not usable when full text failed',
 'Temkin2024 formulates the resolution/local-uniformization problems. No exact all-characteristic resolution theorem found. The nearby-cycle consequences must be assessed independently.',
 ['P4_Temkin2024','P4_DeligneFinitude1977','P4_Illusie2021']),
('P4-S22','SGA7I normal crossings tame nearby cycles Kummer torsor exterior algebra multiplicities gcd; Illusie2002 8.4.4',
 'Original SGA7I §§3.1--3.3; primary Illusie2002 and Riou2014 PDFs',
 'Finite root covers, induced coefficient algebra, exterior cohomology and the multiplicity homomorphism checked. Nonzero coefficient, positive multiplicity and correct r-fold group are retained.',
 ['P4_SGA7IIntro','P4_IllusieLog2002','P4_Riou2014']),
('P4-S23','Rapoport Zink1982 local zeta normal crossing wild inertia; Nakayama nearby cycles log smooth Theorem0.1; Illusie2002 Cor8.4.3',
 'Rapoport authorPDF https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/UeberdielokaleZetafunktion.pdf ; Nakayama Cambridge fullPDF ; Illusie NumdamPDF',
 'RZ§2, Nakayama0.1/0.1.1, and Illusie8.3--8.4.4 read. Proper log-smooth open-stratum tameness includes the relevant nonvertical case. Publication dates distinguished from later online hosting.',
 ['P4_RapoportZink1982','P4_Nakayama1998','P4_IllusieLog2002']),
('P4-S24','SGA7I4.2 nearby cycles stalk dimension; affine Lefschetz Gabber Pilloni Stroh Astérisque2014 XV',
 'Original SGA7I printedpp14--16; full primary https://www.numdam.org/item/AST_2014__363-364__293_0.pdf',
 'Refined pointwise dimension bound and the geometric generic point checked. Pilloni--Stroh1.1.2 retains its quasi-excellence hypothesis. Hyperplane codimension and Gysin shifts checked independently.',
 ['P4_SGA7IIntro','P4_PilloniStroh2014','P4_Illusie2021']),
('P4-S25','strict local dimension cohomological dimension punctured principal open Kummer infinite roots; MathOverflow zbMATH variants; Orgogozo2014 XVIII_B examples nonexcellent',
 'Primary https://www.numdam.org/item/AST_2014__363-364__461_0.pdf ; author revised XVIII_App https://www.cmls.polytechnique.fr/perso/orgogozo/travaux_de_Gabber/18A-cohomological-dimension/dimensionA.pdf',
 'Orgogozo §§2.1--2.4 gives regular strict-local dimension2 with H3(D(t),Z/ℓ) nonzero. Our continuous Cartan--Leray deduction refutes the manuscript tower bound in arbitrary noetherian generality.',
 ['P4_OrgogozoDimension2014','P4_IllusieDimension2014']),
('P4-S26','SGA2XIV depth local Lefschetz SGA7I4.5 4.6; Illusie Perversité et variation2003 2.6 2.7 2.10',
 'Original SGA7I printedpp15--20; publisher https://link.springer.com/article/10.1007/s00229-003-0407-z ; reproduced primary article https://studylibfr.com/doc/350158/perversit%C3%A9-et-variation',
 'Uniform punctured-fibre premise and shifted vanishing range checked. Illusie2003 extends the historical characteristic-zero lci/depth results to general traits under the explicit coefficient and flat-lci hypotheses.',
 ['P4_SGA7IIntro','P4_Illusie2003','P4_PilloniStroh2014'])]
S=[]
for sid,query,sources,outcome,refs in SPECS:
    S.append(dict(search_id=sid,date=b.DATE,queries=query,sources=sources,outcome=outcome,
       claim_ids=';'.join(c['id'] for c in b.claims if sid in c['search_ids']),reference_keys=';'.join(refs)))
merge_tsv('search_log.tsv',['search_id','date','queries','sources','outcome','claim_ids','reference_keys'],S,lambda r:int(r['search_id'].split('S')[-1])<17)

LINKS=[]
def link(kind,fr,to,what,evidence):
    LINKS.append(dict(kind=kind,**{'from':fr,'to':to},what=what,evidence=evidence,note_ids='Codex K34-05--08; no NOTES_INDEX verdict rows'))
link('folder','K34-05:84--94','K34-07:130--132; K34-08:144--148','The support complex, strict-local stalk formula and two localization triangles use one consistent one-degree shift.','Both complete supplied passages read; C802,C816,C876,C878,C882 retain distinct constructions.')
link('folder','K34-06:102--115','K34-07:116--128','Purity and the residue-cup induction feed the Kummer-tower calculation and the wild-inertia question.','Both complete supplied passages read; the unresolved cup-square and F-scope issues are not concealed by the later use.')
link('folder','K34-07:125--128','K34-08:134--143','The nearby-cycle bounds supply global and local Lefschetz consequences, with additional smoothness/depth hypotheses.','Both complete supplied passages read; resolution is a historical dependency, not a theorem proved on either side.')
link('published work','K34-05:84--99; K34-07:130--132','P4_SGA7XIII §§1.3,2.1.4,2.1.9','Nearby-cycle definitions, strict-local stalks and the boundary-qualified compactification comparison.','Original SGA7II selected pages and supplied text read. XIII2.1.9 is not used as a general unqualified open-base-change theorem.')
link('published work','K34-06:102--113','P4_Riou2014 XVI3.1.1,3.1.4,3.4.8','Absolute purity and the normal-crossing cup/residue formula.','Full primary article opened; coefficient invertibility and sign conventions checked.')
link('published work','K34-05:97--99; K34-07:125--128','P4_Illusie2021 Theorem2.3; P4_IllusieLog2002(8.4.4.1)','The i+1 monodromy bound and corrected local crossing bound.','Original SGA7I3.4 image checked as well: its printed q′ formula is off by one and is not silently normalized.')
link('published work','K34-07:128','P4_Nakayama1998 Theorem0.1; P4_IllusieLog2002 Cor8.4.3','Later solution of the local and proper global wild-inertia questions in log-smooth hypotheses.','Full primary texts read; Rapoport--Zink1982 retained as an earlier normal-crossing antecedent.')
link('published work','K34-08:139','P4_OrgogozoDimension2014 XVIII_B §§2.1--2.4','A later nonexcellent counterexample refutes the arbitrary-noetherian infinite-root dimension bound.','Primary example read; the Kummer-tower conclusion is an explicitly identified new deduction by continuous Cartan--Leray.')
link('published work','K34-08:140--148','P4_SGA7IIntro4.5--4.7; P4_Illusie2003 §§2.6--2.10','Local depth, lci vanishing and the need for uniform punctured-fibre hypotheses.','Original and modern primary texts read; the manuscript Φ shift is applied throughout.')
merge_tsv('links.tsv',['kind','from','to','what','evidence','note_ids'],LINKS,lambda r:not r['note_ids'].startswith('Codex K34-05--08'))

E=[]
def event(n,typ,outcome):E.append(dict(statement_id=f'C-SA13-{n}',date=b.DATE,who=b.WHO,type=typ,outcome=outcome))
for c in b.claims:
    event(int(c['id'].split('-')[-1]),'used and rechecked in this run',
      'Hypotheses and degree conventions compared with the cited exact result or explicitly unresolved source scope. This source comparison does not certify an omitted proof. '+c['fate'])
for n,scope in [
 (802,'the cone shift and localization sequence'),(803,'finite inverse systems and the Mittag--Leffler exactness argument'),
 (807,'the imperfect-residue finite separable DVR extension with e=1 and degree p'),
 (813,'exact invariants for continuous pro-p actions on ℓ-primary torsion modules'),
 (814,'the finite pro-p image in GLd(Zℓ), ℓ≠p'),(816,'the low-degree sequence and high-degree shift'),
 (831,'exterior ranks and residue induction under the extending-coefficient hypothesis'),
 (833,'the Artin--Schreier local-system counterexample to the broad coefficient scope'),
 (834,'the signed boundary/cup identity in the localization triangle'),
 (835,'the regular finite root cover and its rank'),(836,'multiplication by m^q and killing in the root tower'),
 (840,'the continuous induced coefficient algebra'),(842,'the n=1 exception to exact kernel recovery'),
 (844,'the Koszul cohomology of a free pro-ℓ group'),(845,'the multiplicity homomorphism and its gcd image'),
 (846,'the all-zero multiplicity exception'),(849,'filtration length implies nilpotence'),
 (853,'the corrected spectral-sequence nilpotence length'),(862,'the nongometric-generic Kummer obstruction'),
 (864,'the support-dimension optimization in the spectral sequence'),(865,'the exact-sequence boundary'),
 (867,'the codimension d+1 Gysin shift'),(868,'continuous Cartan--Leray obstruction from Orgogozo’s primary example'),
 (871,'the low-degree comparison diagram'),(873,'the affine fibre-product pinch and diagonal H0 map'),
 (878,'localization triangle A'),(879,'uniform punctured-fibre vanishing and its exact degree range'),
 (880,'support cohomology in Xbar and reduced punctured cohomology'),(881,'isolated nonsmoothness implies punctured local acyclicity'),
 (882,'localization triangle B and its distinction from A')]:
    event(n,'independent re-proof','Checked '+scope+'; full hypotheses and proof in proof_audit.md §§10--19. No broader assertion is inferred from a toy calculation.')
for n in [802,807,816,831,836,842,844,845,846,849,853,864,865,867,868,871,873,879,880]:
    event(n,'computation or formal certificate','Exact finite arithmetic/linear-algebra and degree-bound checks in code/codex_computations.py; output in outputs/codex_computations.txt. General geometric proofs are recorded separately.')
for n,refined in [(807,'C-SA13-807, corrected multiplier e'),(833,'C-SA13-833, coefficient extends to X'),(842,'C-SA13-842, n>1'),(846,'C-SA13-846, some mi>0'),(862,'C-SA13-862, geometric generic point'),(868,'C-SA13-868, negative answer in the stated generality'),(879,'C-SA13-879, uniform punctured-fibre premise')]:
    event(n,"refuted, with the refined statement's id",'Literal broad assertion or proposed bound refuted with stated example hypotheses. Refined statement: '+refined+'. No manuscript text changed.')
merge_tsv('check_events.tsv',['statement_id','date','who','type','outcome'],E,lambda r:not r['statement_id'].startswith('C-SA13-') or int(r['statement_id'].split('-')[-1])<800)
print(f'Codex auxiliary records saved: {len(P)} problems; {len(R)} scan-specific readings; {len(S)} search groups; {len(LINKS)} links; {len(E)} check events.')
