from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

OWN = Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work/agents/reduction_descent')
source = OWN / 'B_residual_wild_high_quotient_candidate.tex'
program = OWN / 'code/verify_residual_wild_high_quotient.py'
output = program.with_suffix('.output.json')
before = source.read_text()
prior = OWN / 'notes/B_residual_wild_high_quotient.before_certificate.tex'
assert not prior.exists()
prior.write_text(before)
data = json.loads(output.read_text())
old = '''No fresh original-source reading is claimed here. The standalone
finite supplement is retained separately and will be cited with
its exact scope and actual runtime after execution. No finite
parameter row is treated as a formal-group existence assertion.'''
new = r'''No fresh original-source reading is claimed here. The retained
standalone program
\path{code/reduction_descent/verify_residual_wild_high_quotient.py}
reconstructs 78,761 inverse-Newton quotient distributions, including
all nine tested equality boundaries, and checks 210,956 complete
prime/divisible case rows over the four stated small primes.
Its independent finite-character enumeration retains 32 normalized
distinct-character rows, the four ordered crossing rows representing
(B-RD91.7), and the 20 both-large rows. It reconstructs all 250
linear functionals on the two tame forms of the trace-zero plane,
excludes all eight nonzero intertwiners between the opposite tame
characters, and checks 75,571 cyclotomic break inequalities.
The first author run passed at 03:02:51.567982 UTC on 20 November
2026 in 0.6828030579927145 seconds. No executed computation failed.
The program, full output, and pre-certificate source are retained.
These finite checks do not replace the uniform field and quotient
proofs, and no parameter row is treated as a formal-group existence
assertion.'''
assert old in before
source.write_text(before.replace(old,new))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
labels = re.findall(r'\\label\{([^}]+)\}', source.read_text())
assert len(labels) == 5
record = {
    'status':'CANDIDATE_READY_FOR_FULL_INDEPENDENT_AUDITS',
    'actual_utc':datetime.now(timezone.utc).isoformat(),
    'candidate':str(source),
    'candidate_sha256':sha(source),
    'labels':labels,
    'program':str(program),
    'program_sha256':sha(program),
    'output':str(output),
    'output_sha256':sha(output),
    'author_runtime_seconds':data['runtime_seconds'],
    'author_actual_utc':data['actual_utc'],
    'scope':'Five assertions: first-level strict break, p-divisibility at actual p^3, p5 crossing and large quotient alternatives, large-branch layer shapes (3,4)/(4,4), and exact limitations. No complete residual-wild or least-index closure.',
    'primary_source_scope':'No fresh original-source read; entire internal B60/B69/B82/B84/B86 dependency proofs reread.',
    'failed_executions':[],
    'preserved_prior':str(prior)
}
dest=OWN/'outputs/B91_candidate_record.json'
assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n')
with (OWN/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([record['actual_utc'],label,'CANDIDATE_AUTHOR_CHECKED',record['scope'],'B_residual_wild_high_quotient_candidate.tex;outputs/B91_candidate_record.json','Complete author proof; exact standalone output PASS '+str(data['runtime_seconds'])+'s; independent audits pending'])+'\n')
print(json.dumps(record,indent=2))
