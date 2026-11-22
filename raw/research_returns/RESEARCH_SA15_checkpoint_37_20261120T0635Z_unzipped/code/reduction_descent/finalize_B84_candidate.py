from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re

own=Path(__file__).resolve().parents[1]
candidate=own/'B_tame_residual_one_prime_recovery_candidate.tex'
raw=candidate.read_bytes()
pre=own/'notes/B_tame_residual_one_prime_recovery.before_certificate.tex'
assert not pre.exists();pre.write_bytes(raw)
out=own/'code/verify_tame_residual_one_prime_recovery.output.json'
result=json.loads(out.read_text());assert result['status']=='PASS'
tail=r'''\smallskip
\noindent\emph{Exact supplement and provenance.}
The retained program
\path{code/reduction_descent/verify_tame_residual_one_prime_recovery.py}
checks the three symbolic displacement identities,
80,536 point-field parameter rows over 96 prime/index
samples, including 6,600 mixed prime/divisible exclusions,
and the exact two normalized \(p=5\) character rows and
their common quadratic-twist orbit. All parameter pairs
are checked for \(p=5,7,11,13\) at the four displayed
index factors; larger primes through 101 use explicitly
retained boundary samples. The author run passed in
\(0.12348706599732395\) seconds with no failed execution.
The uniform common-point-field and two-break proof is
independent of those finite ranges. All executed code,
output and prior source versions remain retained.
The exact internal B69 quotient and inverse-polygon proof,
B60 fixed-coefficient break lemma and B82/B83 common-field
arguments were reread; no new original-source read is
claimed.
'''
assert raw.decode().count(r'\end{remark}')==1
s=raw.decode().replace(r'\end{remark}',tail+r'\end{remark}')
candidate.write_text(s)
code=own/'code/verify_tame_residual_one_prime_recovery.py'
record={'status':'CANDIDATE_FULL_PROOF_AND_EXACT_SUPPLEMENT','actual_utc':datetime.now(timezone.utc).isoformat(),
        'candidate':str(candidate),'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),
        'program':str(code),'program_sha256':hashlib.sha256(code.read_bytes()).hexdigest(),
        'author_output':str(out),'author_output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
        'author_runtime_seconds':result['runtime_seconds'],'labels':re.findall(r'\\label\{([^}]+)\}',s),
        'counts':result['counts'],'scope':result['scope'],'executed_failures':[],
        'source_scope':'Complete internal actual quotient, inverse-polygon and fixed-coefficient arguments; no new original-source claim.'}
(own/'outputs/B84_candidate_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
