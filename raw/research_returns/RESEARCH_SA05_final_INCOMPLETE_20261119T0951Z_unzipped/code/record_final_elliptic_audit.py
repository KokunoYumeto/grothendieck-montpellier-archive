"""Record the final root read of the actual elliptic certificate and outputs."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
path=root/'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as f:rows=list(csv.DictReader(f,delimiter='\t'))
outcome=('Root read post09/code/check_elliptic_tangent.py and its actual output post09/output/elliptic_tangent_certificate.json at09:43–09:44UTC, and then read the complete earlier Part B point/smoothness program and retained output referenced by hash. The eight characteristic-two polynomial identities and the projective gradient ideal/F2-point calculation pass written verification. The actual new runtime was0.05908195899974089seconds. Root did not rerun either program; the infinite Tate-module and completion assertion is supported by the separately checked proof, not finite enumeration.')
rows.append({'statement_id':'B.1.elliptic-Milnor-completion','date':now,
             'who':'GPT-6 Astra / root / current run',
             'type':'targeted proof check','outcome':outcome})
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    w.writeheader();w.writerows(rows)
entry='''

### Actual geometric illustration of Milnor completion

The final standalone note `part_d/post09/milnor_elliptic_completion.md`
uses K=Fbar2(E), E:y²+y=x³, to exhibit a nonzero T3E subspace in the
actual3-adic completion of K1^M(K). The principal-divisor sequence and
compatible division of the explicit point(0,0) prove the inclusion and
nonvanishing. The tangent line gives arithmetic Frobenius phi²=[−2],
so geometric Frobenius satisfies F²=−1/2. These completed eigenvalues
are not roots of unity. The example illustrates completion in geometry;
it does not assert a prime-dependent failure for a geometric motive.

The complete proof was read independently by B and root. The program
`part_d/post09/code/check_elliptic_tangent.py` executed eight exact
characteristic-two polynomial checks at09:41:42UTC in0.059081959seconds,
with output `part_d/post09/output/elliptic_tangent_certificate.json`.
That output identifies by hash the existing Part B projective-smoothness
and F2-point certificate. Root read both programs and both saved outputs
at09:43–09:44UTC without rerunning them. The infinite completion proof is
not inferred from the finite certificate. This additional example does
not change any original open row or the review movement count.
'''
for name in ['RESEARCH_SA05_report.md','PROGRESS_LEDGER.md']:
    p=root/name;s=p.read_text()
    assert '### Actual geometric illustration of Milnor completion' not in s
    p.write_text(s+entry)
result={'recorded_utc':now,'new_root_event':1,'root_reran_program':False,
        'qualifying_movement':False}
(root/'code/record_final_elliptic_audit_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
