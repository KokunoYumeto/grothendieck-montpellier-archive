from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
own=Path(__file__).resolve().parents[1]
candidate=own/'B_first_wild_reducible_terminal_candidate.tex'
raw=candidate.read_bytes();pre=own/'notes/B_first_wild_reducible_terminal.before_certificate.tex'
assert not pre.exists();pre.write_bytes(raw)
s=raw.decode();needle='index remains in \\(\\{2,3\\}\\).'
assert s.count(needle)==1
s=s.replace(needle,needle+r'''

\smallskip
\noindent\emph{Exact supplement and provenance.}
The retained standalone program
\path{code/reduction_descent/verify_first_wild_reducible_terminal.py}
checks three symbolic break identities, all 17,664 nonzero
matrices and 1,723,680 outside-line images at \(p=5,7,11\),
and the 23 possible maximal terminal planes at those primes.
It checks 24 layer-shape rows, 71,456 small divisible-parameter
character comparisons, 3,628 field-integrality rows, and
35,000 rows each for high-line mismatch and two-break recovery.
The author run passed in \(0.42271842100308277\) seconds.
No executed computation failed; all source and output are
retained. These finite checks do not construct a formal
group or replace the uniform arguments above. The full
internal B60 fixed-coefficient proof, B69 actual Newton
and line-character arguments, and B49 coefficient bounds
were reread. No new original-source read is claimed.''')
candidate.write_text(s)
program=own/'code/verify_first_wild_reducible_terminal.py';output=program.with_suffix('.output.json')
run=json.loads(output.read_text());assert run['status']=='PASS'
labels=re.findall(r'\\label\{([^}]+)\}',s);assert len(labels)==5
record={'status':'CANDIDATE_COMPLETE_CHECKED','actual_utc':datetime.now(timezone.utc).isoformat(),
        'candidate':str(candidate),'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),
        'labels':labels,'program':str(program.relative_to(own)),
        'program_sha256':hashlib.sha256(program.read_bytes()).hexdigest(),
        'author_output':str(output.relative_to(own)),
        'author_output_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
        'author_run':run,'preserved_precertificate':str(pre),
        'scope':'Actual p3 comparisons at first wild e=p(p-1). With two slopes, wild orderp4 and one B=pb with p not dividing b, terminal break equality recovers the high line and character. Nontrivial residual wild inertia and different finite characters therefore require wild orderp^r,5<=r<=9. Residual-tame exchanged high-line sector and larger images remain open.',
        'source_scope':'Internal B60 lower-break, B69 actual Newton/line-character and B49 coefficient proofs reread; no new primary-source reading claimed.',
        'checkpoint_scope':'Separate from frozen CP29 canonical paper; no promotion or current-gate change.',
        'executed_failures':[],'audits_pending':['root complete proof/code','companion complete proof/code']}
(own/'outputs/B82_candidate_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='author_run'},indent=2))
