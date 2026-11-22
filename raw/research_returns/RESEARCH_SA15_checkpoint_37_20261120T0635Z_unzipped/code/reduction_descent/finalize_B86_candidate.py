from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
own=Path(__file__).resolve().parents[1]
candidate=own/'B_first_wild_cyclotomic_quotient_candidate.tex';raw=candidate.read_bytes()
pre=own/'notes/B_first_wild_cyclotomic_quotient.before_certificate.tex'
assert not pre.exists();pre.write_bytes(raw)
code=own/'code/verify_first_wild_cyclotomic_quotient.py';out=code.with_suffix('.output.json')
result=json.loads(out.read_text());assert result['status']=='PASS'
paragraph=r'''
\smallskip
\noindent\emph{Exact supplement.}
The retained standalone program
\path{code/reduction_descent/verify_first_wild_cyclotomic_quotient.py}
checks the symbolic determinant, bracket, point-field
evaluation and strict-gap identities, every small
parameter for primes 5 through 101, and all diagonal
characters on the displayed additive point quotients
for primes through 31. It also computes every
coefficient of the six shifted cyclotomic polynomials
at \(p=5,7,11\), \(n=2,3\), and verifies their
Eisenstein conditions. An explicit nonzero determinant
with traceless terminal power is retained as a guard
against the invalid simpler inference. The author run
passed in \(RUNTIME\) seconds. No execution failed.
The finite ranges do not replace the actual field
inclusion and quotient-ramification proofs. Every
executed program, output and prior proof version is
retained.
'''.replace('RUNTIME',str(result['runtime_seconds']))
s=raw.decode();assert s.count(r'\end{remark}')==1
s=s.replace(r'\end{remark}',paragraph+r'\end{remark}');candidate.write_text(s)
now=datetime.now(timezone.utc).isoformat()
sources={'actual_utc':now,'status':'FULL_SPECIFIED_ORIGINAL_PASSAGES_READ',
         'reads':[{'title':'The Stacks Project, Theorem10.160.8,Tag032A',
                   'url':'https://stacks.math.columbia.edu/tag/032A','web_ref':'turn115081002view1',
                   'scope':'Complete theorem and full coefficient-ring existence proof, including mixed-characteristic formal-smoothness induction.'},
                  {'title':'Pierre Colmez, Corps locaux, notes du cours de M2',
                   'url':'https://webusers.imj-prg.fr/~pierre.colmez/CL.pdf',
                   'web_refs':['turn115081002view0','turn658536524view0','turn658536524view1'],
                   'retained_original_pdf':'sources/colmez_corps_locaux.pdf',
                   'retained_text':'sources/colmez_corps_locaux.txt',
                   'scope':'Proposition2.12/full tame-uniformizer Hensel proof p11; Proposition3.7/full two-divisibility norm-polynomial proof pp14-15. Also reread full Theorem3.10 and Proposition3.13 on pp15-16, although only3.7 is needed in the final proof. Opening definitions allow complete discrete valuation fields with arbitrary perfect residue.'}],
         'bibliography_scope':'Existing Stacks032A and ColmezCorpsLocaux entries reused. Canonical bibliography remains frozen; no edit made.',
         'priority_scope':'No novelty or historical priority claim. No theorem imported from a search snippet.'}
(own/'notes/B86_source_read_record.json').write_text(json.dumps(sources,indent=2)+'\n')
record={'status':'CANDIDATE_FULL_PROOF_AND_EXACT_SUPPLEMENT','actual_utc':now,
        'candidate':str(candidate),'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),
        'program':str(code),'program_sha256':hashlib.sha256(code.read_bytes()).hexdigest(),
        'author_output':str(out),'author_output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
        'author_runtime_seconds':result['runtime_seconds'],'labels':re.findall(r'\\label\{([^}]+)\}',s),
        'counts':result['counts'],'scope':result['scope'],'source_record':'notes/B86_source_read_record.json',
        'dependency_scope':'B85 remains separately candidate pending both audits; no canonical/theorem promotion here.',
        'executed_failures':[]}
(own/'outputs/B86_candidate_record.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
