"""Record late, fully scoped standalone checks; leave the verified PDF unchanged."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
checks=[
 ('B1:two-boundary-cokernel','part_b/b1_uniform_ramification_obstruction.md',
  'Root read the complete two-boundary calculation. All support-triangle shifts, weight-minus-one and minus-two invariant/coinvariant exactness, Picard comparison under divisor Tate, projective-space motivic vanishing and flat-tensor quotient pass. Root did not independently reopen the owner-added purity sources. This fixed-open obstruction does not prove survival under subsequent shrinking and does not reduce the universal colimit gate.'),
 ('C6:pure-encoding-constraints','part_d/post08/pure_local_encoding_constraints.md',
  'Root read the complete corrected note, checking the symmetric and alternating hyperbolic signs, the rank equation2r=s+t iff the original map is an isomorphism, and the rational-parameter p^n-to-zero Kisin contradiction. Weight-monodromy is explicitly conditional in the first diagnostic. These exclude proposed constructions, not all pure encodings.'),
 ('C6:BGV-literal-twist-purity','part_d/post08/bgv_twist_purity_scope.md',
  'Root read BGV2306.05099v2 Definition2.42(3), Example2.43(2), Example3.29(1), Definition4.40, Remark4.41 and Proposition4.44 with its local proof in the retained primary text. The covariant realization of1(1)[2] overF2 has eigenvalue1/2 and weight-minus-two, contradicting the literal algebraic-integer clause on the full Tate-stable heart. The used compact-monodromy equivalence does not depend on4.44(2); no downstream theorem is refuted.')
]
path=root/'ROOT_CHECK_EVENTS.tsv'
with path.open(newline='') as f: rows=list(csv.DictReader(f,delimiter='\t'))
for label,filename,outcome in checks:
    if not any(r['statement_id']==label and r['outcome']==outcome for r in rows):
        rows.append(dict(statement_id=label,date=now,who='GPT-6 Astra / root / current run',
                         type='targeted proof check',outcome=outcome))
with path.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
    w.writeheader();w.writerows(rows)
out=dict(recorded_utc=now,checks=[dict(statement_id=l,file=f,
         sha256=hashlib.sha256((root/f).read_bytes()).hexdigest(),outcome=o) for l,f,o in checks])
(root/'code/record_cp08_standalone_audits_output.json').write_text(json.dumps(out,indent=2)+'\n')
entry='''

### Standalone diagnostics retained at checkpoint08

The fixed two-boundary B1 note identifies a precise cokernel in terms of a rational Gysin relation on the threefold components. It does not assert survival under further shrinking. The pure-local encoding note proves the limited hyperbolic-rank and smooth-parameter obstructions, with the weight--monodromy condition explicitly retained. Root and independent readers checked these written arguments; the exact source-read scopes are separate.

A further source check found a literal Tate-twist issue in the archived BGV v2 purity definition: its algebraic-integrality clause is incompatible with the negative-weight Tate object. The exact normalization, elementary counterexample and rational-arithmetic certificate are retained in the standalone note. The compact-monodromy equivalence used here does not depend on the affected purity clause. This is not a refutation of that equivalence or of an uninspected later version. No open universal row changes status.
'''
for filename in ['RESEARCH_SA05_report.md','PROGRESS_LEDGER.md']:
    path=root/filename;text=path.read_text()
    if '### Standalone diagnostics retained at checkpoint08' not in text:path.write_text(text+entry)
print(json.dumps(dict(recorded_utc=now,checks=len(checks)),indent=2))
