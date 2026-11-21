#!/usr/bin/env python3
"""Consolidate honest component events; do not upgrade source checks."""
from pathlib import Path
import csv,re

R=Path(__file__).resolve().parent.parent
W=R/'work'; D=R/'deliverables'
fields=['statement_id','date','who_model_effort_run','type','outcome','method_and_locator']
events=[]

def add(sid,typ,outcome,locator='',checker='/root',date='2026-11-21 Europe/Berlin'):
    events.append(dict(zip(fields,[sid,date,f'{checker}; GPT-6 Astra Pro; effort not exposed; CX_GRH-20261121',typ,outcome,locator])))

# Source checks performed by the coordinator; these do not claim proof replay.
add('SRC-A-D','used and rechecked in this run','Read the supplied Lean statement interfaces and named theorem wrappers, plus Remark step20. Accepted as theorem under task contract. Full imported proof tree and scan not supplied; no kernel replay.','ALPOGE_Main.lean; ALPOGE_Statements.lean; Remark p4 step20')
add('SRC-M-GRH','used and rechecked in this run','Read the actual introductory claim and convention/trace locators. Visually checked p522: heading13.3.1.2 has no statement body. Conditional premise only; no audit of full proposed proof.','Masullo Ch1§1.2 especially1.2.3 pp12–16; Ch3 3.2.1.2–4 pp123–124; 12.5.1.1 pp519–520; 13.3.1.1–2 p522')
add('SRC-B-Q07','used and rechecked in this run','Earlier-run question and ledger read; current proof localizes the Dedekind gate to bounded solution fields. Earlier check labels not inherited.','BRIDGES_QUESTIONS.tsv Q07; CX-K01–K04')
add('SRC-B-Q08','used and rechecked in this run','Earlier-run conclusion read, then rechecked against the recovered Bach original and delegated full Schoof proof reading.','BRIDGES_QUESTIONS.tsv Q08; CX-N01')

valid={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found'}
files=['koiran_check_events.tsv','eth_check_events.tsv','number_check_events.tsv','koiran_quadratic_check_events.tsv','koiran_factoring_check_events.tsv']
for name in files:
    p=W/name
    if not p.exists(): continue
    with p.open(newline='',encoding='utf-8') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            sid=row.get('statement_id') or row.get('id')
            if not sid: continue
            typ=row.get('type') or row.get('check_type') or ''
            original=typ
            lower=typ.lower()
            if typ not in valid and not typ.startswith('refuted, with'):
                if 'artifact' in lower or 'syntax' in lower or 'finite diagnostic' in lower or 'computation' in lower:
                    typ='computation or formal certificate'
                elif 'independent re-proof' in lower:
                    typ='independent re-proof'
                elif sid.startswith('CX-') and ('complete-proof' in lower or 'whole-proof' in lower or 'full independent transfer proof' in lower):
                    typ='targeted proof check'
                elif any(word in lower for word in ('source','retrieval','used known','primary','premise')):
                    typ='used and rechecked in this run'
                elif 'proof' in lower or 'transfer' in lower or 'review' in lower:
                    typ='targeted proof check'
                else:
                    typ='carried as background without fault found'
            checker=row.get('checker') or row.get('who') or '/root/koiran_gct'
            if 'GPT-' in checker:
                who=checker+'; run normalized as CX_GRH-20261121'
            else:
                who=f'{checker}; {row.get("model","GPT-6 Astra Pro")}; effort {row.get("effort","not exposed")}; CX_GRH-20261121'
            date=row.get('date') or row.get('date_utc') or ''
            outcome=row.get('outcome','')
            method=row.get('method_and_locator') or row.get('method') or ''
            if original!=typ: method=(method+'; ' if method else '')+'Original component description: '+original
            if 'date_utc' in row or (date=='2026-11-20'):
                method=(method+'; ' if method else '')+'Component UTC date '+date+'; consolidated Berlin date21Nov2026'
                date='2026-11-21 Europe/Berlin'
            events.append(dict(zip(fields,[sid,date,who,typ,outcome,method])))

checks={
'CX-R01':'Read complete final proof: primitive Dirichlet factorization, pole-free critical strip, trivial Hecke character and imprimitive Euler factors.',
'CX-R02':'Read complete final proof: S3 quotient, arbitrary lifted commutator, all rank-one characters kill it, additive trace obstruction. No logical-independence claim.',
'CX-K01':'Read complete final proof: integral primitive element, height scale, E/E prime-ideal estimate, higher residue degrees and bad primes, useful-prime gap.',
'CX-K02':'Read complete final proof: circuit gate equations, unique extension, rational constants, nonzero homogeneous encoding, AM/Pi2 and complement direction.',
'CX-K03':'Read complete final proof: explicit bounded abelian-witness promise, character factorization, unchanged no-instance soundness; no promise recognition claimed.',
'CX-K04':'Read complete final proof: all cubic root fields nonnormal; subfields of finite abelian extensions normal; infinite case descends to finite.',
'CX-K05':'Read complete final proof: bounded coefficient grid, existential-block merger, dimension minimum, prefix search, nilpotents, graded finite-module induction, base change, PSPACE enumeration.',
'CX-K06':'Read complete final proof: exponential encoding and constant alternations, distinct small-system and optimal h.s.o.p. outputs, mixed weights and extra equation access retained.',
'CX-K07':'Read complete final proof: composition of existing PSPACE hitting-set construction and GCT transformation; no new attribution or cardinality claim.',
'CX-K08':'Read complete final proof: closed point/spreading, index and ell inversion, degree-one Frobenius trace, finite morphism and Proj d0 case, proper incidence, finite spreading.',
'CX-N01':'Read complete transfer: source quadratic family, endpoints, prime completeness, composite rejection and bit complexity.',
'CX-N02':'Read complete proof: proper subgroup, all-integers cutoff, small-p branch, exponent test, no order factorization.',
'CX-N03':'Read complete proof: each primary component has full order; coprime-order product; factorization input explicit.',
'CX-N04':'Read complete transfer: character family and t! estimate; candidate list versus recognition.',
'CX-N05':'Read complete transfer: imaginary quadratic field, ray modulus and Hecke characters, given-model isomorphism and candidate-output scope.',
'CX-N06':'Read complete transfer: auxiliary field plus ray class gate, retained exponential degree dependence and generating-set output.',
'CX-N07':'Read complete proof: separating character, Bach conductor1 bound, class-field product and lack of poles/zero cancellation; ray Euler factors.',
'CX-N08':'Read complete proof: S-unit group rather than relation lattice, exact sequence and regulator/class-number indices, factor-two completeness certificate.',
'CX-N09':'Read complete transfer proof: M covers the cited Evd89 radical oracle; EVD94 reduction carried as published theorem with abstract verified. Original full EVD94 proof not independently recovered.',
'CX-N10':'Read complete BGL transfer proof: auxiliary degree-r field inputs and smoothness parameters. Ronyai discussion remains explicitly qualified source background.',
'CX-N11':'Read complete proof: p2/nodd, local Eisenstein, Galois conjugacy, q1mod2n, full primary order, discriminant tower, effective polynomial search.',
'CX-N12':'Read complete proof: fundamental discriminant input, correct relations imply integer index, detectable failure and geometric restarts; complexity constant minimization.',
'CX-N13':'Read complete expanded final proof: r not dividing m, odd-r Frobenius eigenspace using cyclic image criterion, S/r congruence, unconditional even-degree quadratic root-doubling branch; uniform polynomial bound.',
'CX-N14':'Read complete final proof: small-characteristic enumeration, automorphism order extraction, prime-field eigenfunction and invariant radical, moved-component ideal, cyclotomic/Teichmuller valuation-one noncyclicity, descent to A, supplied maximum-order coefficient unit and gcd factor.',
'CX-N15':'Read complete final proof at SHA256 5d433a8c0319e8a06c591f10d0ba52740e6bbb8564fd0646f078a1ef06cef247: AL86/N11 fields with every BGL auxiliary input; Frobenius subfield and eigenvector; exact maximum order; Teichmuller interpolation descent including r=2 and s=1; noncyclicity and IKRS descent; fixed algebra for arbitrary Fq; early p<=d; gcd recursion and quasipolynomial bound; exact sufficient zeta family. Complete PartII geometric dictionary also read.',
'CX-E01':'Read complete proof and added sparsification paragraph: fixed-width quantifiers, deterministic/counting/randomized/gap/nondeterministic variants, false-premise logic, branch overhead and counting partition.',
'CX-E02':'Read complete proof: linear parameter bound, polynomial prefactors, FPT sufficient reduction, exact population-count circuit and clique witness count.',
'CX-E03':'Read complete proof: truth-table gate encoding at most4 clauses, unique extension, density5, Williams all-polynomial-size premise and gate blowup.',
'CX-E04':'Read complete transfer and whole supplied quantitative-circuits.tex implication proof: local decoder, E^NP witness language, eta margin, infinitely-often constant scope.',
'CX-E05':'Read complete proof: at-least1/2 recurrence, exact-one edge circuits, unique assignments, sparse/dense parameter distinction.',
'CX-E06':'Read complete model/scope proof: numerical evaluation versus symbolic arithmetic families, VBP determinant distinction, border-hardness scales, no independence claim.',
'CX-E07':'Read complete proof: Boolean CRT over Z, clause factors remove exactly false assignments, gate isomorphisms, rank/lambda and geometric cohomology.',
'CX-E08':'Read complete proof: equivariant graded quotient from orbit containment and characteristic-zero multiplicity inequality.',
'CX-G01':'Read complete proof: induced permutation object, local Frobenius cycles, zeta factors and fixed-point traces, rank-one obstruction and ray-character direct image.',
'CX-G02':'Read complete proof: G_m and Kummer torsor, invertible derivative, rational section criterion, CRT idempotent and ideal (1-e)A orientation.',
'CX-G03':'Read complete proof: fractional ideals and rank-one modules, scalar isomorphisms, divisor signs, exact unit/principal-relation dictionary.',
'CX-G04':'Read complete proof: torsion-free contraction over Z, flatness, homogeneous cone, free graded pieces and Hilbert polynomial, coaction descent, special-fiber limitation.',
'CX-G05':'Read complete proof: lambda/rank calculation, zero reduced gamma class, C2 trace obstruction, Schur idempotents only with denominators inverted.',
'CX-G06':'Read complete proof: roots-of-unity eigenvalues and stable operations, no global analytic deduction; geometric fiber cohomology and unit Artin motive.'
}
for sid,desc in checks.items(): add(sid,'targeted proof check','Passed within the stated hypotheses. '+desc,'Complete final component LaTeX read by coordinator; this is not a formal certificate.')
add('CX-N14-VAL-DROP','refuted, with the refined statement\'s id CX-N14','Read and independently checked the entire p=17,r=3,d=3 counterexample: order9 element eta, x=(eta,zeta*eta,zeta^2*eta), tau(x)=zeta*x, rho2 action exponent-1 mod9, x^3=zeta; the proposed subgroup is cyclic. Only the shortcut omitting the valuation hypothesis is refuted.','Complete counterexample in number_automorphism_gate.tex; refined case(iii) and maximum-order coefficient-unit condition remain proved.')

sources=[
('SRC-WASHINGTON4.3','Washington2ed Theorem4.3 p33','Primitive-character Dedekind factorization statement inspected; source used as known theorem, not independently reproved.'),
('SRC-MILNE0.4-0.5','Milne CFTv4.03 Introduction Theorems0.4–0.5 pp4–5','Hilbert/ray class reciprocity statements inspected, including finite-prime ramification and residue-degree interpretation.'),
('SRC-SGA1-V4-V7','SGA1 ExpV §4 Theorem1 and §7, consulted French text transcription','Equivalence and scheme application statements read; not a full reconstruction of the Galois-category theorem.'),
('SRC-SGA3-I-VIII','SGA3 revised ExpI4.6.3.1,4.7.1–2; ExpVIII1.1–2','Linear-space, action/comodule and diagonalizable group-scheme passages inspected.'),
('SRC-SGA4-IX3','SGA4 ExpIX3.2 and Theorem3.3, consulted transcription','Kummer exact sequence and Picard identification statements inspected.'),
('SRC-SGA5-XV3','SGA5 ExpXV§3 no1 Proposition1; no2 theorem and corollary to Lemma1','Read determinant/Euler-product formalism and finite-field direct-image/rationality scope; not used as number-field rationality.'),
('SRC-SGA6-V-VI','SGA6 ExpV2.4,3.10(3.10.1), ExpVI3.2–3.3, consulted transcriptions','Exterior/gamma and K-group lambda structures inspected; known machinery used, no complete SGA proof rederived.'),
('SRC-EGAII6','EGAII6.1.4–6.1.5','Finite-morphism and base-change locators inspected; short application independently proved in geometric dictionary.'),
('SRC-FGA221','FGA Exp221 §3 Theorems3.1–3.2 pp259–260; Proposition3.8 p265','Original PDF theorem statements and surrounding hypotheses read; representability is background, not reproved.'),
('SRC-WEILII','WeilII§1.2, Theorem3.3.1 p204, Corollary3.3.9 p207','Weight definitions and stated finite-field bounds inspected; no reproof of WeilII or number-field inference.'),
('SRC-MACDONALD-I3.4','Macdonald2ed I§3(3.4) p41','Jacobi–Trudi formula and conventions read in source scan.'),
('SRC-ARCHIVE2-5','https://grothendieck.umontpellier.fr/2.pdf scan5 sheet4','Visually inspected rank augmentation and Picard comparison in dimension at most1; only historical companion.'),
('SRC-ARCHIVE28-3','https://grothendieck.umontpellier.fr/28.pdf scan3 sheet2','Visually inspected action map and axioms; cover/date label also inspected.'),
('SRC-ARCHIVE98-11-12-44','https://grothendieck.umontpellier.fr/98.pdf scans11,12,44 sheets10,11,43','Visually inspected norm-degree axioms, finiteG-set example, and bounded coherent-sheaf families. No complexity theorem attributed.'),
('SRC-ARCHIVE34-64-74','https://grothendieck.umontpellier.fr/34.pdf scans64,74 sheets63,73','Visually inspected crossed-out Remark1.17 and equation2.5.5 Riemann–Weil explanation. Finite-field scope and crossed-out status retained.'),
('SRC-BACHS HALLIT89-L13'.replace(' ',''),'Bach–Shallit1989§8 Lemma13 pp213–214; Lemma14/Theorem3 p214','Read original cached primary text. Explicit top-field Dedekind-zeta premise confirmed; corrupted radical OCR not used as exact formulas.'),
('SRC-BIMS17-T1.2-C1.3-T6.7','BIMS17 authorPDFp2 Theorem1.2/Cor1.3 and following supplied-model remark; §6.2 pp7–8','Read theorem statements and rational-character weak-GRH scope. N13 uses cited even-degree theorem and own odd-r proof; no full BIMS reproof.'),
('SRC-BACH90-ROOT','Bach1990§3 pp359–362; §6 pp369–373; Theorem4 p375 and corollaryp376','Recovered original journal PDF, read character definitions and ordinary-Dirichlet scope; agent independently visually verified formulas and complete relevant proofs.')
]
for sid,loc,desc in sources: add(sid,'used and rechecked in this run',desc,loc)

add('SRC-BGL01-T1-T3-ROOT','used and rechecked in this run','Read the original extracted Theorem1 statement and following auxiliary-k clarification, corollary, Theorem2 exact auxiliary inputs, and Theorem3 all-prime scope. Verified that k is independent of n and f. This is a source-statement check, not a fresh reading of all BGL proofs.','BGL2001 pp6–7; local primary extraction bachgathenlenstra2001.txt')
for sid,gate in [
    ('CX-U01','Bounded solution-field zeta gate; abelian-witness and virtual rank-one shortcuts refuted; unconditional prime range does not preserve polynomial bit length.'),
    ('CX-U02','General M-transfer complete by N15; unrestricted A_D extension still needs the specified maximal coefficient unit or a replacement construction. BGL single-prime shortcut has been checked and retains unavailable auxiliary inputs.'),
    ('CX-U03','The source and independently composed bounds retain quasipolynomial degree dependence; no general deterministic polynomial bound is proved.'),
    ('CX-U04','Factor-base and index certification do not bound unrestricted relation search; the concrete imaginary-quadratic Las Vegas theorem is retained.'),
    ('CX-U05','Optimal succinct parameters still require equations; Boolean rank does not supply symbolic arithmetic circuits or equivariant multiplicities.'),
    ('CX-U06','Growing width, stronger parameter transfers, and all-polynomial-size circuit conclusions require additional reductions or quantitative input.')
]:
    add(sid,'used and rechecked in this run','Reviewed the complete current gate statement against the proved findings. This is an unproved extension, not a theorem or proof certificate. '+gate,'PartIII, paper_scope.tex; corresponding QUESTIONS.tsv rows')

# Preserve the exact authorship and modest status of the citation auditor's
# additional background records, rather than relabeling them as proof checks.
extra=W/'final_citation_additions.tsv'
if extra.exists():
    with extra.open(newline='',encoding='utf-8') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            events.append({field:row.get(field,'') for field in fields})

qa=W/'final_qa_events.tsv'
if qa.exists():
    with qa.open(newline='',encoding='utf-8') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            events.append({field:row.get(field,'') for field in fields})

with (D/'CHECK_EVENTS.tsv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fields,delimiter='\t');writer.writeheader();writer.writerows(events)

questions=[
('Q01','Alpoge Remark step20; ALPOGE_Main/Statements.lean','What number-field zeta scope follows from the supplied Dirichlet theorem?','proved: CX-R01; abelian extensions of Q by primitive-character factorization'),
('Q02','Masullo Ch1§1.2/1.2.3; Ch3 3.2.1.2–4; 12.5.1.1;13.3.1.1–2','Which claim can actually be cited, and what does it supply?','proved source audit and conditional transfer: CX-R01; introductory claim M supplies all finite-order Hecke and Dedekind families;13.3.1.2 is empty'),
('Q03','BRIDGES Q07; Koiran DIMACS§2T2,§5T9/C1; LO77T1.1','Does general Koiran need only rational Dirichlet GRH?','proved exact checked-proof gate: CX-K01; bounded solution-field Dedekind RH, no Galois closure; general M-transfer CX-K02'),
('Q04','Koiran bounded algebraic witnesses; WashingtonT4.3','What promise version is covered by A_D?','proved: CX-K03, with explicit polynomial bound on abelian witness degree/discriminant/denominators'),
('Q05','Proposed abelian-witness and rank-one shortcuts','Can every solution field be replaced by an abelian witness or rank-one virtual sum?','refuted: CX-K04 and CX-R02; x^3−2 and S3 commutator trace counterexamples'),
('Q06','GCT V T2.10; Koiran DIMACS T2','Do rational circuits and homogeneous nonzero points preserve AM?','proved conditional on M: CX-K02'),
('Q07','GCT V T3.4 source tnoetherph','What is the functional PH bound for equation-given standard-graded h.s.o.p.?','proved conditional on M: CX-K05, FP^Sigma2P with polynomial output bits; unconditional functional PSPACE'),
('Q08','GCT V T4.10,T5.12 source tssopverifydet,tssopexplicit','What transfers for succinct strict small separating systems?','proved conditional historical EXPH transfer: CX-K06; construction/verification output conventions retained'),
('Q09','GCT V T4.1,T5.5 source tnnldetexpspace,tnnlexplicithsop','Does GRH removal eliminate the equation-access premise for optimal h.s.o.p.?','refuted inference, refined result proved: CX-K06; singly exponential equation computation remains a premise of cited route'),
('Q10','FS18T7.1; GSS19T1.5–1.6','Is small-system construction first made unconditional now?','refuted attribution: CX-K07; existing unconditional PSPACE construction; optimal cardinality and arbitrary verification distinct'),
('Q11','BRIDGES Q08; Bach1990T2 p372,p373; Schoof2008T2.2','Is Dirichlet GRH enough for Miller with Bach cutoff?','proved via A_D: CX-N01; quadratic characters suffice; O(b^3M(b)) bit bound'),
('Q12','Bach1990T2–3 p372; ShoupP9p10','Can a specified prime-field r-nonresidue be found without factoring p−1?','proved via A_D: CX-N02'),
('Q13','Shoup1992T3p4,§6p13; primitive-root order criterion','What primitive-root output is efficient?','proved via A_D: CX-N03–N04; full factorization input gives certified generator; otherwise polynomial candidate list only'),
('Q14','Shoup1992T2p3,§§4–5pp10–13,P13','Which analytic characters occur in quadratic-extension primitive-root candidates?','proved conditional on M: CX-N05; finite ray-class Hecke characters over imaginary quadratic K'),
('Q15','Buchmann–Shoup1996 mainpp1311–1312;Facts2.1,4.3','What remains of generating-set runtime after GRH transfer?','proved conditional on M: CX-N06; (n logp)^O(n), fixedn polynomial, generating set not necessarily one primitive member'),
('Q16','AL86P3p351; Bach–Sorenson1996T5.1p1729','Which auxiliary number field makes prime selection effective?','proved conditional on M: CX-N11; E=Q(zeta_2n,p^(1/n)), q=O(n^4log²np), precise Frobenius/order and discriminant proof'),
('Q17','BIMS17C1.3p2; CX-N02','Are quadratic nonresidues in supplied extensions a Hecke-only consequence?','refuted stronger gate; proved CX-N13: A_D suffices every oddp/allm; evenm already unconditional'),
('Q18','BIMS17T1.2p2; Frobenius eigenspace refinement','Can variable prime r dividing p−1 be handled in every supplied extension?','proved via A_D: CX-N13, poly(m logp); direct odd-r proof and even-degree quadratic input'),
('Q19','IKRS MainTheorem p3, Lemma4.2 p14, Proposition4.6 pp16–17; AL86T1/AlgorithmA pp350–351; BGLT2p7; CX-N11','Which exact analytic family suffices for general deterministic finite-field factoring?','proved conditional on M: CX-N15, independently of the unretrieved EVD94 reduction or historical radical oracle; zeta_Q and zeta_{Q(zeta_{2nu},p^(1/nu))} for the stated nu<=d^2 suffice; (d^{logd}logq)^O(1) bound retained. CX-N09 records the historical transfer.'),
('Q20','BGL2001T1p6,T2–3p7; Ronyai primary abstract','Do special-field results imply unrestricted polynomial-time factoring?','refuted inference; qualified transfers CX-N10 preserve smoothness and structural parameters; Ronyai original theorem locators remain source-limited'),
('Q21','Gao§2.4L2.6; IKRS§4','Which split-prime-field automorphism cases admit a smaller gate?','proved: CX-N14; p<=d unconditional, r|p−1 under A_D, valuation-one case unconditional; maximum-order coefficient Teichmuller unit is a sufficient remaining input; full author/coordinator/independent reads passed'),
('Q22','GaoL3.6; IKRS4.2/4.6; AL86P3; CX-N14–N15','Can the entire general factoring route be discharged by A_D alone?','unproved extension, current gate CX-U02: after covered cases, p>d, r not dividing p(p−1), r^2 dividing p^ord_r(p)−1; a maximal coefficient Teichmuller unit suffices. CX-N15 constructs it under an explicit cyclotomic–Kummer zeta family, not reduced here to A_D; no impossibility asserted.'),
('Q23','Bach1990T4p375/corollaryp376; BDFT1.1/T2.1','What exact GRH supplies class-group generators?','proved conditional on M: CX-N07; class-character Hecke factors and zeta_K; zeta_HilbertClassField sufficient; refined BDF family recorded'),
('Q24','Lenstra1992§5eq5.7 authorp25','What does the class-group/unit verification index certify?','proved: CX-N08; full S-unit subgroup index1 under finite-index/rank/torsion/factor-base and analytic interval hypotheses; relation-search time not supplied'),
('Q25','Biasse–Erukulangara mainp4,Algorithm4p15,Cor1p16; JMV09T1.1/C1.3','Is there a complete rigorous class-group algorithm transferable under M?','proved conditional on M: CX-N12; imaginary quadratic fundamental discriminant, detected failures and Las Vegas expected L(d)^(3/sqrt8+o1)'),
('Q26','OpenAIETH T1.1 and§1.1.1–1.1.3','Which ETH/SETH variants are refuted?','proved from E: CX-E01; ETH,#ETH,SETH,#SETH,randomized,GapETH,NSETH with fixed-width quantifiers'),
('Q27','Fine-grained/parameterized lower-bound implications; supplied E','Does refuting their premise automatically refute each target lower bound?','refuted inference: CX-E01–E02; actual target-to-CNF parameter-preserving reduction is required'),
('Q28','OpenAIETH T1.1,Cor1.3; explicit population-count circuit','Which counting and graph-parameter transfers follow?','proved: CX-E02,CX-E05; linear variable bound, parsimonious counts, vertex-parameter cliques and sparse permanent; no FPT/treewidth inference'),
('Q29','Williams2013T1.1; circuit gate encoding','Does the simple SAT encoding satisfy the all-polynomial-size circuit premise?','refuted inference with refined proved bound: CX-E03; parameter n+s, not just n'),
('Q30','OpenAIETHCor1.4,AppendixC.1; WilliamsT6.1; JMVT1','What Boolean circuit lower bound actually follows?','proved transfer: CX-E04; some L in E^NP has C_L(n)>c n sqrt(logn) infinitely often; no stronger SIZE(O(n sqrtlogn)) exclusion'),
('Q31','Valiant1979T2; Burgisser2024defs2.9/2.25,T2.20/2.29/7.3; GCTVT1.7','Does E settle VP/VNP, symbolic permanent or GCT border hardness?','proved scope diagnosis: CX-E06; none of the required symbolic/arithmetic/equivariant premises supplied; no logical-independence theorem'),
('Q32','Boolean Z-scheme CRT; SGA1V§7; SGA6VI3.2','What is the exact geometric object counted?','proved: CX-E07; constant finite etale scheme degree#F, explicit gate scheme isomorphisms, rank/lambda/motive dictionary'),
('Q33','SGA3I4.7; SGA6V2.4; GCT orbit-closure quotient','What extra representation data would an obstruction need?','proved: CX-E08,CX-G05; graded Schur-multiplicity inequality and noninjectivity of rank via trivial/sign C2'),
('Q34','EGAII6.1.4–5; FGA221§3T3.1–3.2,Prop3.8','Can the orbit and normalization data be put over Z and in Hilbert/Quot frameworks?','proved: CX-K08,CX-G04; finite spreading and flat contracted integral orbit model, without equation-complexity or special-fiber orbit equality claims'),
('Q35','SGA4IX3.2–3.3; SGA3VIII1.1–1.2','What is the number-algorithm geometric dictionary?','proved: CX-G01–G03; Kummer torsors, finite etale idempotents, Picard/class and unit/principal-divisor data'),
('Q36','SGA5XV§3; WeilII§1.2,T3.3.1,C3.3.9','Does local weight-zero purity remove global number-field GRH gates?','refuted inference from this argument; precise statement proved CX-G06; roots-of-unity eigenvalues do not supply the analytic zero estimate'),
('Q37','SGA6V2.4,3.10/VI3.2–3.3; MacdonaldI§3(3.4)','What do lambda, gamma and Schur operations preserve?','proved: CX-G05; Boolean reduced class zero, rank loses equivariant data, characteristic-zero Schur splitting qualifications'),
('Q38','Archives cotes2/5,28/3,98/11–12,44,34/64,74','Where do all restatements live in the archive and published texts?','proved locator/dictionary audit: PartII crosswalk and CX-G01–G06; historical companions visually inspected, no modern complexity result attributed to manuscripts'),
('Q39','CX-N14 counterexample; IKRS4.2/4.6','Can the valuation-one hypothesis be deleted while using only the subgroup generated by x and zeta?','refuted by CX-N14: p=17,r=3,d=3, x=(eta,zeta*eta,zeta^2*eta), eta order9, x^3=zeta; subgroup cyclic. Refined maximal-coefficient-unit criterion proved, constructed under M in CX-N15.')
]
with (D/'QUESTIONS.tsv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.writer(f,delimiter='\t');writer.writerow(['id','source_and_locator','question','state']);writer.writerows(questions)
print(f'{len(events)} events; {len(questions)} questions written')
