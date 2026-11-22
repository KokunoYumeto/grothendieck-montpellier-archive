from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
own=Path(__file__).resolve().parents[1]
candidate=own/'B_first_wild_diagonal_projection_candidate.tex';raw=candidate.read_bytes()
pre=own/'notes/B_first_wild_diagonal_projection.before_certificate.tex'
assert not pre.exists();pre.write_bytes(raw)
code=own/'code/verify_first_wild_diagonal_projection.py';out=code.with_suffix('.output.json')
result=json.loads(out.read_text());assert result['status']=='PASS'
paragraph=r'''
\smallskip
\noindent\emph{Exact supplement.}
The retained program
\path{code/reduction_descent/verify_first_wild_diagonal_projection.py}
checks three symbolic identities, all 71,456 parameter
pairs for every prime from 5 through 101, and 142,912
inverse-slope and prime-valuation rows. It also checks
1,132 literal degree-\(p\) translation images,
21,272 separated tame-weight pairs and 43,752 independent
diagonal extensions in the stated congruence class.
The author run passed in \(0.3171308919991134\) seconds,
with no failed execution. The actual point-field and
lower-break proofs do not depend on these finite ranges.
All executed code, output and prior source bytes are
retained; no formal-group realization follows from
the finite checks.
'''
s=raw.decode();assert s.count(r'\end{remark}')==1
s=s.replace(r'\end{remark}',paragraph+r'\end{remark}');candidate.write_text(s)
record={'status':'CANDIDATE_FULL_PROOF_AND_EXACT_SUPPLEMENT','actual_utc':datetime.now(timezone.utc).isoformat(),
        'candidate':str(candidate),'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),
        'program':str(code),'program_sha256':hashlib.sha256(code.read_bytes()).hexdigest(),
        'author_output':str(out),'author_output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
        'author_runtime_seconds':result['runtime_seconds'],'labels':re.findall(r'\\label\{([^}]+)\}',s),
        'counts':result['counts'],'scope':result['scope'],
        'source_scope':'Full internal B83 opposite quotient and lattice proof, B60 exact-break proof and relevant complete B69 quotient proof reread. No new original-source claim.',
        'origin':'Parent notes/root_B85_point_field_lead.md; rederived actual second-level point-field argument.',
        'executed_failures':[]}
(own/'outputs/B85_candidate_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
