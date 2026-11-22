from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
own=Path(__file__).resolve().parents[1]
candidate=own/'B_first_wild_swapped_quotients_candidate.tex';raw=candidate.read_bytes()
pre=own/'notes/B_first_wild_swapped_quotients.before_certificate.tex'
assert not pre.exists();pre.write_bytes(raw)
s=raw.decode();needle='the proposition or the final corollary.'
assert s.count(needle)==1
s=s.replace(needle,needle+r'''

\smallskip
\noindent\emph{Exact supplement and provenance.}
The retained standalone program
\path{code/reduction_descent/verify_first_wild_swapped_quotients.py}
checks the two symbolic lattice conjugations and the two
exact residual matrices. For every prime from 5 through 101
it checks all 71,456 opposite-quotient parameter pairs,
36,848 nonsquare residual eigenvalue pairs, 24 literal
commutator and power rows, 24 dimension-bound rows and
74,804 residual-tame parameter branches. The order-two
exceptions at primes congruent to 3 modulo 4 are retained
explicitly, rather than included in the theorem.
The author run passed in \(0.3601258019916713\) seconds,
with no failed execution. The initial and clarified proofs,
every executed program and its output are retained. The
complete internal B69 point-field and actual quotient
proofs were reread and their relevant steps rederived
at the present wild index. No new original-source read
is claimed. These finite checks establish no formal-group
existence and do not replace the uniform proofs.''')
candidate.write_text(s)
program=own/'code/verify_first_wild_swapped_quotients.py';output=program.with_suffix('.output.json')
run=json.loads(output.read_text());assert run['status']=='PASS'
labels=re.findall(r'\\label\{([^}]+)\}',s);assert len(labels)==5
record={'status':'CANDIDATE_COMPLETE_CHECKED','actual_utc':datetime.now(timezone.utc).isoformat(),
        'candidate':str(candidate),'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),
        'labels':labels,'program':str(program.relative_to(own)),
        'program_sha256':hashlib.sha256(program.read_bytes()).hexdigest(),
        'author_output':str(output.relative_to(own)),
        'author_output_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
        'author_run':run,'preserved_precertificate':str(pre),
        'scope':'For p congruent1mod4 at e=p(p-1), the residual-tame two-divisible-parameter exchanged-high-line sector forces both opposite first matrix entries, hence at least five wild matrix dimensions. Combined with B81/B82, every actual p3 different-special-character comparison has wild order at least p5, including3125 atp5/e20. No larger-image exclusion or exact least-index claim.',
        'source_scope':'Full internal B69 point-field and actual quotient arguments reread and rederived at the wild index. Actual lattice and commutator calculations explicit; no fresh original-source reading.',
        'checkpoint_scope':'Post-CP29 candidate, not part of the immutable CP29 paper.',
        'executed_failures':[],'audits_pending':['root full proof/code','companion full proof/code']}
(own/'outputs/B83_candidate_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='author_run'},indent=2))
