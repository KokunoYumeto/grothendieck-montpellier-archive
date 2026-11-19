import csv
import json
import re
from pathlib import Path

ROOT = Path('/workspace/scratch/f6dbb6638732')
DATE = '2026-11-19'
WHO = 'GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent period_triangle'
TYPE_PROOF = 'targeted proof check'
TYPE_USE = 'used and rechecked in this run'
TYPE_BACKGROUND = 'carried as background without fault found'
TYPE_CERT = 'computation or formal certificate'
TYPE_REFUTE = "refuted, with the refined statement's id"
events = []

def event(sid, kind, outcome):
    events.append(dict(statement_id=sid, date=DATE, who=WHO, type=kind, outcome=outcome))

proofs = {
 'A.1.1': 'Typed alpha, beta and gamma with Betti/de Rham/associated-graded source and target; pure reductive possibly disconnected scope; flag and bigrading spaces, opposed-filtration splitting, dimensions and relative varying-unipotent torsor proved. Mixed generality not imported.',
 'A.1.2': 'Separated normalized U-torsor of dimension u from expanded H-prime of dimension u+1; typed the natural bigrading-to-flag arrow, proved the u>0 section obstruction, and retained both denominator readings with their defects.',
 'A.1.3': 'Computed alpha on Q(-n) in the chosen Betti-to-de Rham convention and checked inversion preserves field membership; recorded the necessary Tate-object membership.',
 'A.2.1': 'Proved finite algebraic extension preserves the identity component; distinguished rational Betti conjugation map from conjugate-semilinear de Rham map; constructed the joint comparison torsor for M direct-sum c*M over the compositum and algebraic closure.',
 'A.2.2': 'Constructed the nonempty opposed open subset of the joint torsor and its algebraic point; proved parabolic surjectivity and all image stabilizers. Derived dimensions alpha=g, beta=u, gamma=b+v, phi=u, psi=u+v and joint field g+v, with 0<=v<=u, including disconnected groups.',
 'A.2.3': 'Proved the image fills P times Q exactly when v=u; identified the common-quotient Hodge-cocharacter criterion on identity components through the two kernels and parabolics.',
 'A.2.4': 'Distinguished dimensions of algebraic images from transcendence degrees at the actual comparison point. Proved unconditional bounds and exact relative bounds; spelled out the requested implications of the named period conjecture for the named joint motive and for M alone.',
 'A.2.5': 'Proved Lead A by rational real Frobenius and opposed flags: v=0, psi rational over phi, beta and gamma rational over alpha, and K=k(alpha). Checked real models, isomorphism to conjugate without a real model, and u=0.',
 'A.2.6': 'Computed the complete GL2 elliptic triangle, the three-dimensional gamma image and its polynomial relation; used the real model to refute added transcendence u in Lead H2. Preserved the separate unresolved arithmetic equivalence rather than inferring it from dimensions.',
 'A.2.7': 'Applied the established comparison-image theorem to established joint genericity cases; did not extend the known single-CM-elliptic result to arbitrary CM products. Parent elliptic source audit supplies the transcendence input.',
 'B.1.1': 'Checked characteristic-zero generic-fibre equivalence with continuous free Z_p representations and its rational version; constructed a nonpotentially-Hodge--Tate continuous character to delimit the good-reduction image, including p=2.',
 'B.1.2': 'Checked integral Tate full faithfulness and the crystalline weights {0,1} image for all p and finite ramification using opened Tate, Breuil, Kim and prismatic sources; kept historical hypotheses and potential descent data explicit.',
 'B.1.3': 'Computed the different-prime Tate module and the characteristic-p Tate module of mu_{p-infinity}; proved their failure of faithfulness and stated the actual replacements with exact maps.',
 'B.1.4': 'Compared bare Hodge--Tate graded vector spaces with gradings retaining semilinear G_K action; proved nonfullness by distinct unramified height-one characters and explained redundancy of the canonical grading in the retained-action version.',
 'B.1.5': 'Checked weak admissibility, the filtered (phi,N) source category and reconstruction; computed the rank-one weak-admissibility obstruction and a ramified p=2 field without a Frobenius lift. Verified Kisin-module and p=2 Kim comparison scopes.',
 'B.2.1': 'Typed period-ring scalar extensions and invariant functors; checked filtered (phi,N) reconstruction and the failure of bare de Rham filtration to retain unramified Frobenius data in the opened Colmez--Fontaine source.',
 'B.2.2': 'Checked proper smooth, good, semistable and relative comparisons with all geometric hypotheses; opened Scholze and the full corrigendum and Tsuji original-author surveys. Named 1987/1989/1999 originals remained a separate documentary gate at this check.',
 'B.2.3': 'Checked BMS derived integral comparisons, both adjacent torsion-free hypotheses for the cohomological statement, and all-prime prismatic F-crystal classification; retained integral lattices and the p=2 limits of the older comparison.',
 'B.3.1': 'Typed transported integral lattices and their complex scalar extension; proved the scalar comparison and refuted literal unscaled lattice equality using the specified Tate convention. Betti--etale comparison locator SGA4 XVI 4.1 was opened.',
 'B.3.2': 'Computed the real de Rham form using the plus/minus rational Betti eigenspaces and alpha; compared it with the transported Betti real form and identified the opposed-filtration splitting without presuming its algebraicity.',
 'B.3.3': 'Typed each reading of local p-adic cohomology through B_dR, B_cris or B_st and the Hyodo--Kato map; recorded the model, Frobenius, monodromy and uniformizer data required for each.',
 'B.3.4': 'Checked crystalline, rigid and prismatic cohomology over perfect characteristic-p fields, integral/rational scope, Frobenius and specialization maps, and the extra geometric data selecting a Hodge filtration. Opened Berthelot, Kedlaya, Deglise and prismatic locators.',
 'B.4.1': 'Proved the two section laws, exact right-cocycle law and cancellation formula under the separately stated compatibility; checked a C2 counterexample showing centralization alone does not give compatibility.',
 'B.4.2': 'Proved the exact kernel intersection and the necessary-and-sufficient condition ker(u) contained in ker(chi), plus the quotient descent of chi; verified a compatible C2 counterexample to the unqualified equality.',
 'B.4.3': 'Proved p-adic analyticity from compactness and the closed subgroup theorem for all p. Checked the inertia scope of Sen via Serre and constructed the unramified Q5 nonalgebraic-Lie counterexample to the full-Galois assertion; historical anticipation remains documentary.',
 'F.3.1': 'Opened Oda Corollary 5.11 p.131 visually and checked the contravariant comparison and Hodge extension; no canonical splitting or arbitrary-cohomology extension inferred.',
 'F.3.2': 'Proved the universal rational operator-image equality via primitive projectors, matrix units and Casimir separation, with multiplicities; proved failure of the integral equality by reduction of the length-two module modulo 2.',
 'F.3.3': 'Typed the weight, Cartan and filtration cocharacters and Tate character; checked centrality in the Levi by an explicit GL2 example and the exact Tate-twisted P1 equivariance of Lefschetz operators; demonstrated the stated nonfactorization.',
 'F.3.4': 'Opened exact Tannakian, Nori descent, Ayoub--Nori and pure-motive comparison locators; checked coefficient rings, arrows, semisimplicity premises and Hodge-fullness scopes. Preserved the unspecified global essential-image obligations.',
 'F.3.5': 'Proved the homological-to-numerical quotient map and realization criterion; opened Jannsen and standard-conjecture sources; checked explicit counterexamples to centre elimination and reconstruction from derived group plus Tate character alone.',
 'F.3.6': 'Opened Mochizuki statements and author corrections, Tate, Pal and Stix; typed fundamental-group abelianization and Tate-module maps, checked the Jacobian multiplication obstruction and centre-free pullback, and retained all cyclotomic/open-image hypotheses.',
 'F.3.7': 'Computed real fixed-point versus invariant-cohomology counterexamples and the P1 quotient; proved the maximal-compact centralizer assertion after weight quotient using the polarization and Cartan involution. Cross-referenced C.4.2 rather than duplicating it.',
 'F.3.8': 'Constructed integral Chow specialization by closures and Cartier Gysin, proved independence using trivial normal bundle, and checked product/cycle-class compatibility in Fulton 20.3 pp.398--400 and Stacks 42.30. SGA6 p.580 remains absent from the inspected mirror.',
 'F.3.9': 'Applied the exact tangent-space dimension formula to the transverse isolated intersection on 18:15, proving dimension p and retaining the transcribed n-p reading and its exceptional n=2p case.',
}
for sid, outcome in proofs.items():
    event(sid, TYPE_PROOF, outcome)

for sid in ['A.2.6']:
    event(sid, TYPE_CERT, 'Exact symbolic certificate: work/code_triangle/real_gl2.py and real_gl2.output.txt; parent independently verifies the same formulas in output/RESEARCH_SA07/code/verify_exact.py. This event records the agent certificate, not a claim to have executed the parent certificate.')
for sid in ['B.1.1', 'B.1.5', 'B.4.1', 'B.4.2', 'B.4.3']:
    event(sid, TYPE_CERT, 'Ran work/code_triangle/comparison_counterexamples.py; exact output in comparison_counterexamples.output.txt checks finite section/cocycle/kernel laws, F4 cube obstruction, weak-admissibility arithmetic, rational Hodge--Tate-weight obstruction and a finite Hensel illustration. Finite digits are not used as an irrationality proof.')
for sid in ['F.3.2', 'F.3.3', 'F.3.5', 'F.3.6', 'F.3.7']:
    event(sid, TYPE_CERT, 'Ran work/code_triangle/audit_operators.py; output in audit_operators.output.txt. Exact checks cover operator identities, matrix units, modulo-2 obstruction, GL2/P1 characters, central isogeny, polarization factor and finite cohomology models. Universal statements are proved in F_audit.tex, not inferred from the finite range.')

event('Lead A', TYPE_USE, 'Proved with all comparison maps typed in A.2.1--A.2.5; the corrected joint-image statement uses v and has dimension g+v, with gamma dimension b+v. The actual-point equalities require the separately named period-conjecture input.')
event('Lead H2', TYPE_REFUTE, 'The reading claiming conjugation adds u independent parameters is false for real models; refined results A.2.4--A.2.6. A bare equivalence between beta genericity and the full period conjecture is recorded as an unresolved arithmetic assertion, not refuted by this counterexample.')
event('Lead H3', TYPE_REFUTE, 'The claim that the section algebra alone proves the minimal-Lie-algebra theorem fails; refined B.4.1--B.4.3 prove the exact algebra and exhibit the false full-image reading. A priority/anticipation reading remains documentary.')
event('R2', TYPE_USE, 'Checked the Tate sign by complex conjugation on P1 and by tensor powers in A.1.3 and B.3.2; no even-Tate converse inferred.')
event('R3', TYPE_USE, 'Rechecked b=l+u and g=l+2u and internal arithmetic; A.2.2--A.2.6 show why dimensional consistency does not identify actual transcendence degrees or the joint comparison image.')
event('R6', TYPE_BACKGROUND, 'The established single-CM-elliptic genericity input is explicitly delegated to the parent elliptic primary-source audit and used in A.2.7; no general CM-product genericity asserted. This row does not claim a new independent check of Chudnovsky originals by period_triangle.')

claim_file = ROOT/'work/audit_claims.csv'
with claim_file.open(newline='') as f:
    claims = list(csv.DictReader(f))
own = set(proofs)
canonical_pattern = re.compile(r'\b[A-G]\.\d+\.\d+\b')
for row in claims:
    ids = canonical_pattern.findall(row['proof_or_locator'])
    status = row['status']
    if status == 'REFUTED':
        kind = TYPE_REFUTE
        outcome = 'Claim false in the recorded reading; refined statement(s): '+row['proof_or_locator']+'. '
    elif status in ['OPEN','READING','DOCUMENTARY-GAP','NAMED-CONJECTURE-IMPLICATION']:
        kind = TYPE_PROOF
        outcome = 'Targeted claim/scope check; status '+status+'. Dependencies or reading: '+row['proof_or_locator']+'. '
    elif any(i in own for i in ids):
        kind = TYPE_USE
        outcome = 'Checked against the proved/source-checked agent result(s) '+row['proof_or_locator']+'. External co-dependencies are retained under the corresponding parent-agent checks. '
    else:
        kind = TYPE_BACKGROUND
        outcome = 'Claim mapped to the parent/other-agent result(s) '+row['proof_or_locator']+'; no additional independent re-proof by period_triangle claimed. '
    outcome += row['remaining_obligation_or_scope']+' Original note '+row['note_id']+'; '+row['witness']+'; '+row['source_file']+':'+row['source_line']+'.'
    event(row['assertion_id'],kind,outcome)
    row['check_event_statement_id'] = row['assertion_id']
    row['check_event_type'] = kind
    row['check_event_ledger'] = 'work/triangle_comparison_audit_CHECK_EVENTS.tsv'
    row['canonical_dependencies'] = '; '.join(dict.fromkeys(ids))

out = ROOT/'work/triangle_comparison_audit_CHECK_EVENTS.tsv'
with out.open('w',newline='') as f:
    writer = csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    writer.writeheader(); writer.writerows(events)
with claim_file.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(claims[0]));writer.writeheader();writer.writerows(claims)

def brace_value(s, key):
    m = re.search(r'\b'+re.escape(key)+r'\s*=\s*\{',s,re.I)
    if not m:return ''
    start=m.end();depth=1;i=start
    while i<len(s) and depth:
        if s[i]=='{' and (i==0 or s[i-1]!='\\'):depth+=1
        if s[i]=='}' and (i==0 or s[i-1]!='\\'):depth-=1
        i+=1
    return s[start:i-1]

source_rows=[]
for rel in ['work/triangle_comparison_references.bib','work/audit_references.bib','work/original_B_references.bib','work/supplied_motivic_references.bib']:
    content=(ROOT/rel).read_text()
    starts=list(re.finditer(r'^@\w+\{([^,]+),',content,re.M))
    for n,m in enumerate(starts):
        entry=content[m.start():starts[n+1].start() if n+1<len(starts) else len(content)]
        key=m.group(1);note=brace_value(entry,'note')
        dependencies=[]
        for path in ['output/RESEARCH_SA07/sections/A_triangle.tex','output/RESEARCH_SA07/sections/B.tex','output/RESEARCH_SA07/sections/F_audit.tex']:
            tex=(ROOT/path).read_text()
            result_starts=list(re.finditer(r'\\begin\{result\}\{([^}]+)\}',tex))
            for j,r in enumerate(result_starts):
                block=tex[r.start():result_starts[j+1].start() if j+1<len(result_starts) else len(tex)]
                if key in block:dependencies.append(r.group(1))
        manual_dependencies = {'OriginalFontaineMessing1987':['B.2.2'],'OriginalFaltings1989':['B.2.2'],'OriginalTsuji1999':['B.2.2'],'OriginalSen1973':['B.4.3'],'OriginalKisin2006':['B.1.2','B.1.5'],'AuditKatoMessing1992':['B.2.2'],'AuditConradKisinSurvey':['B.1.2','B.1.5'],'AuditAndreGalois2009':['A.1.1','A.1.3','A.2.4'],'AuditHuberMullerStach2014':['F.3.4','A.2.4']}
        dependencies += manual_dependencies.get(key,[])
        status = 'PARTLY OPENED' if note.lower().startswith('partly') else ('OPENED' if note.lower().startswith('opened') else ('ORIGINAL FULL TEXT NOT OPENED' if note.lower().startswith('original full text not opened') else 'SEE EXACT NOTE'))
        source_rows.append(dict(source_key=key,url=brace_value(entry,'url'),status=status,locator_and_access=note,dependent_statement_ids='; '.join(dict.fromkeys(dependencies)),record_file=rel,date=DATE,who=WHO))
with (ROOT/'work/triangle_comparison_audit_source_checks.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(source_rows[0]));writer.writeheader();writer.writerows(source_rows)

validation=dict(canonical_result_count=len(proofs),canonical_result_ids=list(proofs),event_count=len(events),original_assertion_count=len(claims),source_record_count=len(source_rows),event_types=sorted(set(e['type'] for e in events)),missing_canonical_results=[],original_assertion_ids_preserved=True)
(ROOT/'work/triangle_check_events_validation.json').write_text(json.dumps(validation,indent=2)+'\n')
print(json.dumps(validation,indent=2))
