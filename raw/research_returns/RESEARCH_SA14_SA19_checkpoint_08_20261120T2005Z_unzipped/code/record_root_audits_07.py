"""Record the actual completed root proof audits for the next checkpoint."""
from pathlib import Path
import csv, datetime, json

root = Path(__file__).resolve().parents[1]
p = root / 'CHECK_EVENTS.tsv'
rows = list(csv.DictReader(p.open(), delimiter='\t'))
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
checks = [
    ('F12-F12b-root', 'independent re-proof',
     'PASS: normal-p invariants, faithful metabelian image, fixed abelian-cover inertia argument, F8 without restricted simplicity, inflation-restriction without a degree assumption, and F7a. Equal-characteristic surface scope retained; coefficient ell different from p remains. work/root/F12_audit.md.'),
    ('A2Y-root', 'independent re-proof',
     'PASS: connected smooth Bertini divisor gives negative-H1 injection; the s/s^p Frobenius square excludes a kernel when Frobenius on H1(O_Y) is injective. Independently opened published Langer Section11 and Cor11.2 p2116: a W2 lift of Y alone excludes the class in total degree1, without a dimension-below-p or polarization-lifting condition. work/root/A2Y_audit.md.'),
    ('F13-root', 'independent re-proof',
     'PASS: specified-normal-subgroup modular monomial proof; complete local Stein and intersection bounds under finite etale resolution covers; purity and unramified induction; positive-break p-group semisimplicity. Kato-Saito Th1.3 and Abbes-Saito Prop3.15(3) independently opened. HT Th7.34 finite-type and Th4.7 geometric-trait scope checked. Complete-local H1/rank estimate remains open. work/root/F13_audit.md. Postdates review03.'),
    ('A2-purity-shortcut-root', 'targeted proof check',
     'PASS as a refutation of the shortcut only: checked the finite-flat Hopf ideal and exact codimension-two zero locus, elliptic section and inverse, and the Jacobian smoothness calculation with discriminant 1+u^6. Re-ran work/bce/code/check_group_purity.py successfully for p=2,3,5,7 and the characteristic-two elliptic identities in 0.060578812 seconds. This varying Picard family is not a fixed ambient hyperplane counterexample and is not main-question movement.')
]
seen = {(r['statement_id'], r['outcome']) for r in rows}
added = 0
for ident, kind, outcome in checks:
    if (ident, outcome) not in seen:
        rows.append(dict(statement_id=ident, date=now,
            who='GPT-6 Astra (OpenAI, ChatGPT Pro mode), root run; effort inherited, not exposed',
            type=kind, outcome=outcome))
        added += 1
with p.open('w', newline='') as out:
    w = csv.DictWriter(out, fieldnames=['statement_id','date','who','type','outcome'], delimiter='\t')
    w.writeheader()
    w.writerows(rows)
result = dict(time_utc=now, checks_considered=len(checks), added=added, events=len(rows))
(root / 'code/record_root_audits_07_output.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
