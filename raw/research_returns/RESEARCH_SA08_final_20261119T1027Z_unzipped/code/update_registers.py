"""Consolidate independently maintained research statement/event registers."""
from pathlib import Path
import argparse
import csv
import json
from datetime import datetime, timezone

parser = argparse.ArgumentParser()
parser.add_argument('--preserve-bibliography', action='store_true',
                    help='Consolidate late audit events while keeping an approved PDF bibliography unchanged.')
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
titles = [
 ('Universal PD resolution and acyclic range','Proved','A_main.tex','136:4-12'),
 ('Literal all-X multiplicative answer H^i(X;I_i)','Proved','A_main.tex','136:7-12'),
 ('Weightwise products, every T divided-power action, graded PD-Rees answer','Proved','A_main.tex','136:4-12,48-72'),
 ('Unrestricted literal L1 is false for an infinite discrete simplicial set','Refuted','A_main.tex','136:7-12'),
 ('Universal total-weight completion and binomial Cauchy product','Proved','A_main.tex','136:233-239'),
 ('All PD triples computed by images of derived coefficient tails','Proved','A_main.tex','136:4-12'),
 ('Completed derived-tail formula without associated-graded regularity','Proved under stated hypotheses','A_main.tex','136:233-239'),
 ('Completed ordinary consecutive-tail image formula under gr S=Gamma_k(T)','Proved under stated hypotheses','A_main.tex','136:233-239'),
 ('Ordinary tails fail for t=0: finite F2 two-sphere counterexample','Refuted','A_main.tex','136:4-12,233-239'),
 ('Canonical graded PD exterior algebra and stable differential quotient','Proved','A_divided_powers.tex','136:74-78,215-220'),
 ('Graded divided powers descend to universal weighted cohomology','Proved','A_divided_powers.tex','136:11-12,77'),
 ('Finite integral cocycle formula determines all induced divided powers','Proved','A_divided_powers.tex','136:48-72,77'),
 ('Scalar formula in degree zero or factorial-injective target; odd counterexample','Proved under stated hypotheses','A_divided_powers.tex','136:11-12,77'),
 ('Weight-zero exterior products and divided powers: corrected L3','Proved','A_weight_zero.tex','136:77'),
 ('Numerical-polynomial coefficient associated graded is Gamma','Proved','A_binomial.tex','Lead L2'),
 ('Strict simplicial relative DGA binomial bridge impossible in weight two','Refuted','A_binomial.tex','Lead L2'),
 ('Ordinary numerical Kahler cotangent complex and complete associated-graded lattice algorithm','Proved','A_binomial.tex','Lead L2'),
 ('Full weighted PD cochains determine the integral weak homotopy type in the nilpotent finite-type scope','Proved under stated hypotheses','A_literature.tex','136:11-12; A.4'),
 ('Exact comparisons with Horel, Toen, Cartan, numerical spaces and filtered circles','Known','A_literature.tex','A.4'),
 ('Kageyama PD simplices are the universal relative PD simplex in cumulative coordinates','Proved','A_literature.tex','136:4-12'),
 ('Filtered-circle associated graded remains different after extending coefficients to Gamma','Refuted','A_literature.tex','Lead L2'),
]
fields=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
dependencies={2:'A-001',3:'A-001;A-002',4:'A-002;A-003',5:'A-003',
6:'A-001;A-003',7:'A-006',8:'A-007',9:'A-006',11:'A-010;A-001',
12:'A-003;A-011',13:'A-012',14:'A-003;A-010;A-012',16:'A-015',
17:'A-015;Stacks 08QQ,08QX,08R2',18:'D006E;Mandell2006 Main Theorem',
20:'A-001;Kageyama2022 section2.1',21:'A-003;HedenlundMoulinos Proposition5.17'}
rows=[]
events=[]
for n,(title,status,file,pages) in enumerate(titles,1):
    ident=f'A-{n:03d}'
    rows.append(dict(zip(fields,[ident,title,status,'sections/'+file,dependencies.get(n,''),pages,
        'A-016 is the strict obstruction; A-026 separately proves nonexistence for the actual all-X relative filtered lift, including derived/E-infinity models.' if n==16 else ''])))
    events.append([ident,'2026-11-19','GPT-6 Astra (OpenAI); inherited effort; run /root',
        'independent re-proof' if status.startswith('Proved') else ('used and rechecked in this run' if status=='Known' else "refuted, with the refined statement's id"),
        status+'; complete proof in sections/'+file])
for ident,code,out in [
 ('A-009','A_t0_sphere2.py','A_t0_sphere2.json'),
 ('A-012','A_exterior_pd_bar.py','A_exterior_pd_bar.jsonl'),
 ('A-016','A_binomial_obstruction.py','A_binomial_obstruction.json'),
 ('A-017','A_numerical_differentials.py','A_numerical_differentials.json'),
 ('A-021','A_model_comparison.py','A_model_comparison.json')]:
    events.append([ident,'2026-11-19','GPT-6 Astra (OpenAI); inherited effort; run /root',
        'computation or formal certificate',f'Executed code/{code}; full output logs/{out}; scope is stated in code.'])
for ident in ['A-006','A-008','A-009','A-016']:
    events.append([ident,'2026-11-19','GPT-6 Astra (OpenAI); inherited effort; run /root/automorphisms',
       'targeted proof check','Independent audit received; details in notes/B_support_A.md.'])
for ident in ['A-006','A-007','A-017']:
    events.append([ident,'2026-11-19','GPT-6 Astra (OpenAI); inherited effort; run /root/shadows_coalgebras',
       'targeted proof check','Independent proof audit received; derived cycles, triangle and product checked.'])
for p in sorted(list((root/'notes').glob('*_results.csv'))+list((root/'logs').glob('*_results.csv'))):
    rows.extend(csv.DictReader(p.open(newline='')))
for p in sorted(list((root/'notes').glob('*_CHECK_EVENTS.tsv'))+list((root/'logs').glob('*_CHECK_EVENTS.tsv'))):
    events.extend(list(csv.reader(p.open(newline=''),delimiter='\t'))[1:])
# Use the user's requested event vocabulary in the consolidated register.
# Preserve the more specific original wording in the outcome and retain every
# original fragment unchanged. An audit is not promoted to an independent proof.
event_types={
    'independent proof audit':'targeted proof check',
    'independent full proof audit':'targeted proof check',
    'independent targeted proof check':'targeted proof check',
    'independent proof and targeted check':'targeted proof check',
    'primary-source check':'used and rechecked in this run',
    'literature/source check':'used and rechecked in this run',
    'documentary verification; no proof of lead':'used and rechecked in this run',
    'original-image inspection':'used and rechecked in this run',
    'independent counterexample proof':'independent re-proof',
    'independent proof':'independent re-proof',
}
for event in events:
    original=event[3]
    replacement=event_types.get(original,original)
    if original.startswith('refuted, with the refined statement '):
        replacement="refuted, with the refined statement's id"
    if replacement!=original:
        event[3]=replacement
        event[4]+=' [Original event description: '+original+']'
with (root/'RESEARCH_SA08_results.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
with (root/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(events)
bibs=sorted(list((root/'notes').glob('*_references.bib'))+list((root/'logs').glob('*_references.bib')))
if not args.preserve_bibliography:
    (root/'RESEARCH_SA08_references.bib').write_text('% Every entry records opened/not opened.\n\n'+'\n\n'.join(p.read_text() for p in bibs))
print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'statements':len(rows),'events':len(events),'bibliography_fragments':[p.name for p in bibs], 'bibliography_preserved':args.preserve_bibliography},indent=2))
