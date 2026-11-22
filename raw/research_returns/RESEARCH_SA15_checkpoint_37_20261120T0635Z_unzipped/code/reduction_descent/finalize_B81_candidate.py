from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

own=Path(__file__).resolve().parents[1]
candidate=own/'B_first_wild_Cartan_exclusion_candidate.tex'
before=candidate.read_bytes()
preserved=own/'notes/B_first_wild_Cartan_exclusion.before_certificate.tex'
assert not preserved.exists()
preserved.write_bytes(before)
needle='unrestricted \\(125\\)-recovery assertion.'
s=before.decode()
assert s.count(needle)==1
s=s.replace(needle,needle+r'''

\smallskip
\noindent\emph{Exact supplement and provenance.}
The standalone program
\path{code/reduction_descent/verify_first_wild_Cartan_exclusion.py}
verifies eight symbolic identities, 24 initial-binomial rows,
96 vanishing-boundary comparisons, 14,109 exhaustive permitted
first-break rows and 1,584 impossible prime-degree rows at
\(p=5,7,11\), together with 56,436 later-break comparisons.
It checks all 17,667 principal-unit \(p\)th powers in the
quadratic rings modulo \(p^3\) at those three primes and
their three exact terminal-image fibre counts. Its 75,984
scalar tests use the two field basis vectors and every
prime from 5 through 101. The author run passed in
\(0.4355178660043748\) seconds, with no failed execution.
All executed source and output are retained. These finite
checks supplement the complete uniform proof; they construct
no formal-group comparison. The full B80 coefficient argument
and the B79 actual displacement and orientation argument were
reread. No new original-source read is claimed.''')
candidate.write_text(s)
program=own/'code/verify_first_wild_Cartan_exclusion.py'
output=program.with_suffix('.output.json')
run=json.loads(output.read_text())
assert run['status']=='PASS'
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert len(labels)==4
record={
    'status':'CANDIDATE_COMPLETE_CHECKED',
    'actual_utc':datetime.now(timezone.utc).isoformat(),
    'candidate':str(candidate),
    'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),
    'labels':labels,
    'program':str(program.relative_to(own)),
    'program_sha256':hashlib.sha256(program.read_bytes()).hexdigest(),
    'author_output':str(output.relative_to(own)),
    'author_output_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
    'author_run':run,
    'scope':'At e=p(p-1), an actual p^3-congruent different-special-character pair with irreducible residual inertia cannot have wild order p^4. Together with B79, any such failure has wild order p^r,5<=r<=8. No potential-CM inference and no larger/reducible image exclusion.',
    'source_scope':'Entire internal B80 first-coefficient argument and B79 actual layer/valuation/orientation proof reread; no new original-source read.',
    'preserved_precertificate':str(preserved),
    'executed_failures':[],
    'audits_pending':['root complete proof/code','obstructions_crystals complete proof/code']}
(own/'outputs/B81_candidate_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='author_run'},indent=2))
