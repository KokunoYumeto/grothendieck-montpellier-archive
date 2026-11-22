from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import difflib

OWN = Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work/agents/reduction_descent')
source = OWN / 'B_residual_wild_crossing_candidate.tex'
program = OWN / 'code/verify_residual_wild_crossing.py'
output = program.with_suffix('.output.json')
record_path = OWN / 'outputs/B92_candidate_record.json'
prior = OWN / 'notes/B_residual_wild_crossing.before_certificate.tex'
assert not prior.exists() and not record_path.exists()
data = json.loads(output.read_text())
assert data['status'] == 'PASS'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert data['source_sha256'] == sha(program)
before = source.read_text()
old = '''is not silently restored after quotienting. Exact program and
execution provenance will be appended after the standalone checks.'''
new = r'''is not silently restored after quotienting. The retained standalone
program \path{code/reduction_descent/verify_residual_wild_crossing.py}
reconstructs all 12 degree-five translation lines, the four possible
three-dimensional diagonal lines, the five relevant point-field
coefficient cases and the separate excluded diagonal case. It checks
625 actual triangular fifth powers and 3,125 quotient matrix-digit
rows, then tests 2,138,160 necessary common-high break pairs. The
surviving necessary profiles are exactly \((24,9234)\) and
\((72,2742)\); the actual diagonal-field comparison excludes only
the second crossing. The first author run passed at
03:16:05.929610 UTC on 20 November 2026 in
1.205554521002341 seconds. The complete program, output and
pre-certificate source are retained; no executed computation failed.
These finite checks supplement the actual field and coefficient
proofs and imply no realization of a surviving numerical profile.
The complete internal B60, B69, B87, B88, B90 and B91 dependency
proofs were reread; no fresh external original-source opening is
claimed in this candidate.'''
assert old in before
after = before.replace(old,new)
prior.write_text(before)
source.write_text(after)
(OWN / 'notes/B92_certificate.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=str(source)+':before',tofile=str(source)+':after')))
labels = re.findall(r'\\label\{([^}]+)\}', after)
assert len(labels) == 5
record = {'status':'CANDIDATE_READY_FOR_FULL_INDEPENDENT_AUDITS','actual_utc':datetime.now(timezone.utc).isoformat(),'candidate':str(source),'candidate_sha256':sha(source),'labels':labels,'program':str(program),'program_sha256':sha(program),'output':str(output),'output_sha256':sha(output),'author_actual_utc':data['actual_utc'],'author_runtime_seconds':data['runtime_seconds'],'scope':'Actual tame 25 comparison gives full first image and four cyclic breaks; residual-wild crossings have full parahoric order5^8; common-high actual diagonal comparison excludes (15,95), leaving (5,45). Both-large and irreducible-residual sectors unchanged; no least-index closure or realization claim.','source_scope':'Complete internal B60/B69/B87/B88/B90/B91 proofs reread. No fresh external original-source opening claimed.','failed_executions':[],'preserved_prior':str(prior)}
record_path.write_text(json.dumps(record,indent=2)+'\n')
with (OWN / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([record['actual_utc'],label,'CANDIDATE_AUTHOR_CHECKED',record['scope'],source.name+';outputs/B92_candidate_record.json','Complete author proof and exact supplement PASS '+str(data['runtime_seconds'])+'s; independent full audits pending'])+'\n')
print(json.dumps(record,indent=2))
