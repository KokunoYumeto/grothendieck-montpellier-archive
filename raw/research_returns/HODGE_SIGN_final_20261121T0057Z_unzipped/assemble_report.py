#!/usr/bin/env python3
"""Assemble the single-file paper and normalize the research registers.

Run from HODGE_SIGN_work or pass its path. Mathematical computations live in
the separate Wilson and step-10 scripts; this script does not validate proofs.
"""
from pathlib import Path
import csv
import re
import sys

R = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent

def table(path, header, rows):
    with (R / path).open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(header)
        w.writerows(rows)

parts = ['paper_front.tex','section_main.tex','section_geometry.tex',
         'section_arithmetic_sl2.tex','section_order.tex','section_q03.tex','paper_end.tex']
missing = [p for p in parts if not (R/p).exists()]
if missing:
    raise SystemExit(f'Missing paper fragments: {missing}')
paper = '\n\n'.join((R/p).read_text(encoding='utf-8') for p in parts)
(R/'HODGE_SIGN.tex').write_text(paper, encoding='utf-8')
citations = set()
for m in re.finditer(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}', paper):
    citations.update(x.strip() for x in m.group(1).split(','))
bib = set(re.findall(r'\\bibitem\{([^}]+)\}', paper))
if citations - bib:
    raise SystemExit(f'Unresolved bibliography keys: {sorted(citations-bib)}')

q = []
def add(i, source, question, state, findings, scope=''):
    q.append([i,source,question,state,findings,scope])
add('Q1','Task1; Alpoge Remark p3 fn3, timeline3/5; Katz ACT3.4.1/A5',
    'State and prove the abstract sign-only theorem with its geometric hypotheses',
    'proved','HS-01,HS-02,HS-03,SG-08,SG-09,SG-10,SG-11',
    'Effective Gysin remainder, Fourier-compatible generic sections, all-extension bound; numerical weights, not new algebraicity or semisimplicity')
add('Q2','Task2; cote16 scans034/036/038/040/049/050; Fable4',
    'Is step5 parity the Hodge-index sign and the same positive-involution route?',
    'refuted as an identification; finite-field conclusion proved by a different use of the same hyperplane machinery',
    'HS-05,SG-01,SG-03,SG-08--11',
    'Quadric squares alternate while trace parity does not; odd evanescent pairing is alternating. No general standard conjecture follows')
add('Q3','Task3; SA06 E.3u and C.1a--q; letter cited in SA06',
    'Does the sign-only proof give the requested absolute values?',
    'proved for every smooth projective finite-field fibre and the specified Tate factor',
    'SG-02,SG-06,SG-07,SG-10',
    'Local weight6 on Q6; shifted global line Re(s)=7/2 for zeta(s-3) uses stipulated Alpoge RH; no general number-field GRH asserted')
add('Q4','Task4; cote44 scans002/004/008/009; Remark step13; H9',
    'Do sign-only purity and Bost slopes yield the proposed arithmetic index theorem and Th4/Th5?',
    'refuted as the proposed implication and raw Th5 identity; actual slope consequence proved',
    'AR-01,AR-02,AR-03,AR-04,AR-05',
    'Counterexample P2xP2 with Z=a^2-ab+b^2, Z|Y=0, deg Z^2=3. Source ellipsis retained. Known divisor/curve cases cited separately')
add('Q5','Task5; cote34 scans053--064/074; BRIDGES Q03',
    'Derive the requested openness after reading1.1',
    'literal assertion refuted; precise corrected openness assertions proved',
    'Q3-01,Q3-02,Q3-03,Q3-04,Q3-05,Q3-06,Q3-07,Q3-08',
    'Open in H, not P; section-dependent soluble version and intrinsic outer-action version. Theorem1.1 for all open subgroups is cited background')
add('Q6','Task6; cote16 scans014--018; Remark step10; H8; actual divisibility declarations',
    'Identify Arthur and Lefschetz SL2 and compare small-parameter divisibility',
    'unqualified and untwisted identification refuted; precise model and actual conditional bounds computed',
    'SL-01,SL-02,SL-03,SL-04,SL-05,SL-06,SL-07,SL-08',
    'Wilson indices and conditional period valuations are distinct data; normalized integral comparison would require the additional data in U-04')
add('Q1a','Alpoge Remark p3 fn3','Can smoothness alone give the asserted effective middle sign?',
    'refuted','HS-04,HS-04B','Kummer sheaf on A1 minus plus/minus1 restricted to xy=1 violates weak Lefschetz and gives a negative leading multiplicity')
add('Q1b','SGA4 XIV3.1; Katz ACT3.4.1/A5','Must base cohomology be concentrated in one degree?',
    'refuted as a necessary hypothesis','SG-08','Higher terms cancel by Gysin; lowest Kunneth degree gives the desired tensor summand')
add('Q1c','Main proof SG-09','Does the restricted path family contain sufficiently generic sections?',
    'proved','SG-09','Fix nondegenerate edges; vary vertex coordinate functions; graph immersion and Katz weak Lefschetz')
add('Q1d','Main proof SG-09','Must good sections exist over the original finite field?',
    'refuted as a necessary hypothesis','SG-09','Use a separate finite extension e_k for each k; take all further extension degrees first')
add('Q1e','Main proof SG-11','Does the upper bound extend to all compact-support degrees and constructible sheaves?',
    'proved','SG-11','Dimension induction uses border Gysin surjectivity; localization keeps degree i')
add('Q2a','SA06 E.3u; cote16 evanescent part','Compute the split sixfold primitive motive, sign and local spectrum',
    'proved','SG-01,SG-02','Q(-3), square -2, Frobenius q^3; Hodge-normalized square+2')
add('Q2b','Fable4; Milne2002 Remarks3.7--3.8','Are algebraic classes on the hexagonal CM elliptic powers Lefschetz classes?',
    'proved','SG-04','Cohomology classes, not all Chow classes; argument extends to CM elliptic powers and finite-field elliptic powers')
add('Q2c','Fable4; Milne2002 Th3.3','Does this prove the same class-generation claim for arbitrary higher-genus CM curves or all CM abelian varieties?',
    'current gate','U-02','Need a no-exotic-class argument or the actual Hodge-conjecture hypothesis; not supplied by parity')
add('Q2d','MilneAV11.1(b),13.2,14.1','Are the absolute values known for every abelian variety without the full Hodge standard conjecture?',
    'proved as a deduction from cited background','SG-05','Degree-one Rosati positivity plus exterior powers; main sign-only theorem gives a second route')
add('Q3a','SA06 E.3u','Does the ambient Q6 primitive Tate line restrict nontrivially to the smooth degree14 hypersurface?',
    'refuted','SG-07','Projection formula plus ordinary ample-section weak Lefschetz gives j* zeta=0')
add('Q3b','SA06 C.1; BRIDGES Q01/Q02','Does purity recover Griffiths kernels or imply general number-field motive GRH?',
    'current gate beyond the proved finite-field assertion','SG-06,U-01','Cycle-class injectivity and non-Artin--Tate arithmetic L-functions are separate; no such implication is claimed')
add('Q4a','Cote44 scan004 Th5; H9(a)','Do integral fibres remove all higher vertical-cycle corrections?',
    'refuted','AR-01','All pencil fibres in the counterexample are geometrically integral, but raw height0 differs from intersection3')
add('Q4b','H9(b); cote44 scan008','Does the proposed raw formula give the claimed positivity equivalence?',
    'refuted as a deduction through that formula','AR-01,AR-04','Primitive cycles need not inject into the generic algebraic Jacobian; a corrected quotient comparison is additional')
add('Q4c','Bost4.5--4.6; actual Formalism.F.SlopeInequality','What does divisibility plus slopes actually imply?',
    'proved','AR-05','log d <= mu_max(M)-mu(L)+log C; equal-rank index inequality also proved')
add('Q4d','Cote44 Th4; Moriwaki A/B; Kunnemann4.1; Shioda8','Which already known cases can be stated accurately?',
    'proved as cited background with its original hypotheses','AR-04','Curve Jacobians and vacuous cellular case; arithmetic divisors and specified projective-space metrics; corrected elliptic surface heights')
add('Q5a','Cote34 scan064 Remark1.17','Is closure[pi0,H] open in pi-prime?',
    'refuted','Q3-01','Spec(Fq), H=1; also Gm/F2 with H=Z3(1)')
add('Q5b','Cote34 scan053 Theorem1.1','Is closure[P,H] open in H?',
    'proved','Q3-04','No solubility assumption needed')
add('Q5c','Corrected Remark1.17 with a section','Is closure[s(pi0),H] open in soluble H?',
    'proved','Q3-05,Q3-06','Finite derived length; all-open-subgroup FAb argument')
add('Q5d','Corrected intrinsic outer-action variant','If arithmetic outer action on soluble H is trivial, is H finite?',
    'proved','Q3-07','Centralizer and derived-series argument, no section')
add('Q5e','Cote34 scan074; WeilI on curves','Does higher-dimensional purity supply a new missing input?',
    'refuted as a requirement for the corrected statements','Q3-02,Q3-B01','Curve RH plus the known1.1 reductions suffice; no semisimplicity used')
add('Q6a','H8 block statement and (i)--(iii)','Are the exterior blocks and integral hard-Lefschetz consequences correct?',
    'proved with corrected range and normalization','SL-01,SL-02,SL-03','Wilson range t<=t+m<=v-t; diagonal form is not always Smith form; numerical checks n<=6')
add('Q6b','Cote16 scan014 versus016; H8 scalar explanation','Can ordinary contraction be the endpoint inverse-string lowering operator?',
    'refuted','SL-04','n=2 gives D^2L^2(1)=4; normalized lowering sends Omega to xi/2')
add('Q6c','Cote16 scans015--018','What is the normalized universal integral Lefschetz ring?',
    'proved','SL-08','Product over i=0..n of M_(n-i+1)(Z), with specified degree projectors and unit-step strings')
add('Q6d','Mok2.2.9--10; untwisted geometric cohomology','Can the commuting Arthur factor identify with untwisted L and Frobenius?',
    'refuted','SL-07','FL=qLF versus commutation; integer degreewise Tate twists remove this particular obstruction')
add('Q6e','Integral Sym^d examples','Does rational SL2 determine the divisibility for m=1,2,3?',
    'refuted','SL-05','Stable monomial/binomial lattices have divided indices (2,1),(3,1),(4,1)')
add('Q6f','Actual ColChain, PathBound, Numbers, NumFacts declarations','What small-parameter divisibility can actually be calculated?',
    'proved as conditional bounds and numerical parameter computations','SL-06','See step10 tables; arithmetic family m even>=2; admissibility and period inputs remain explicit')
add('Q6g','H8(iv), normalized comparison beyond literal identification','Is there a specific integral theta/Lefschetz intertwiner making all indices equal?',
    'current gate','U-04,U-05','Specify a realization, normalization, lattices, operators and denominator compatibility; no implication follows from an Arthur block alone')
add('Q6h','H8(iv); specified ordinary-power string ambient order',
    'Compute Z[L,D,degree-projectors] inside the full product matrix order for n=1,2,3',
    'proved','SL-09',
    'Indices1,32,2^13*3^10; normalized lowering gives1. Elementary fibre-product proof and exact HNF certificate')

row_meanings = {
'a':'Very general quintic; Griffiths summand', 'b':'Letter A,A-prime,A-double-prime modulo algebraic equivalence',
'c':'Divisor-to-curve map and quintic projective products', 'd':'Endpoints, low dimensions and surface index',
'e':'V times P1 and vacuous primitive letter B', 'f':'Universal letter-A ranges',
'g':'Universal quintic over Q(t1,...,t113)', 'h':'Generic hyperplane Gysin image',
'i':'Universal restriction/Gysin ranges and split quadrics', 'j':'Middle positivity and Griffiths injectivity',
'k':'Cycle-class injectivity and finite generation', 'l':'Radical correspondences',
'm':'Semisimplicity modulo algebraic equivalence', 'n':'Endpoint image criterion and standard D',
'o':'Projective stabilization and radicals', 'p':'Abelian stabilization and Beauville pieces',
'q':'Blow-up exceptional cycle/radical formula'}
for letter,meaning in row_meanings.items():
    add(f'SA06-C.1{letter}','INTAKE_RESEARCH_SA06_20261120.md section1 and4',
        f'Finite-field absolute values for {meaning}',
        'proved for smooth projective finite-field fibres','SG-06,SG-10',
        'Prior cycle-theoretic assertion not re-proved or upgraded; full individual scope recorded in the paper table')
table('QUESTIONS.tsv',['id','source_and_locator','question','state','finding_ids','scope_or_gate'],q)

# Preserve event statements verbatim while normalizing the five common columns.
event_files=['root_events.tsv','agent_sign_events.tsv','agent_q03_events.tsv',
             'agent_arithmetic_events.tsv','agent_sign_gate_events.tsv',
             'agent_order_events.tsv']
events=[]
for name in event_files:
    p=R/name
    if not p.exists():
        continue
    with p.open(encoding='utf-8-sig',newline='') as f:
        for r in csv.DictReader(f,delimiter='\t'):
            events.append([r.get('statement_id',''),r.get('date_utc',r.get('date','')),
                           r.get('who_model_effort_run',r.get('who','')),
                           r.get('type',''),r.get('outcome','')])
table('CHECK_EVENTS.tsv',['statement_id','date_utc','who_model_effort_run','type','outcome'],events)

trans=[]
for name in ['agent_sign_transcription.tsv','agent_q03_transcription_notes.tsv']:
    with (R/name).open(encoding='utf-8-sig',newline='') as f:
        for r in csv.DictReader(f,delimiter='\t'):
            trans.append([r['cote'],r['scan'],r['line'],r['our_reading'],r['required_reading'],r['reason'],r['certainty']])
other=[]
with (R/'agent_arithmetic_transcription.tsv').open(encoding='utf-8-sig',newline='') as f:
    for r in csv.DictReader(f,delimiter='\t'):
        loc=r['source_locator']
        m=re.search(r'ARCHIVE_(\d+)_scan(\d+)\.tex\s*(.*)',loc)
        if m:
            trans.append([m[1],m[2],m[3] or loc,r['reading_or_issue'],r['proposed_treatment'],r['mathematical_reason'],r['confidence']])
        else:
            other.append([r['id'],loc,r['reading_or_issue'],r['proposed_treatment'],r['mathematical_reason'],r['confidence']])
table('TRANSCRIPTION_NOTES.tsv',['cote','scan','line','our_reading','required_reading','reason','certainty'],trans)
table('SOURCE_CORRECTIONS.tsv',['id','source_locator','our_reading','required_reading','reason','certainty'],other)
print(f'Assembled {len(paper.splitlines())} LaTeX lines; {len(q)} questions; {len(events)} check events; {len(trans)} archive notes.')
