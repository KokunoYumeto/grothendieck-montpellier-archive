from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

own=Path(__file__).resolve().parents[1]
source=own/'B_iterated_high_quotient_candidate.tex'
raw=source.read_bytes()
before=own/'notes/B_iterated_high_quotient.before_certificate.tex'
assert not before.exists()
before.write_bytes(raw)
t=raw.decode()
old='Let \\(n\\ge2\\). Suppose actual \\(p^n\\)-torsion modules of'
new='Let \\(n\\ge2\\) and \\(0\\le j\\le n-1\\). Suppose actual\n\\(p^n\\)-torsion modules of'
assert old in t
t=t.replace(old,new)
old='''The finite induction supplement is being prepared separately;
it is not the source of the universal induction proof.'''
new=r'''The retained finite supplement is
\path{code/reduction_descent/verify_iterated_high_quotient.py}.
Its final author run passed in \(0.863016332994448\) seconds
at 22:44:19 UTC on 19 November 2026. It exhaustively verifies
four actual rank-two module quotients at \(p=5,7\), levels
two and three, and \(81{,}600\) induced-matrix point identities.
It checks all \(196\) permitted sectors for
\((p,n)=(5,3),(5,4),(7,3)\), including every compatible small
parameter pair, and \(406\) explicitly sampled deeper sectors
for \(p=5,7,11,13\) and \(3\le n\le8\).
The complete and sampled parameter-pair counts are respectively
\(88{,}870\) and \(161{,}887\); among the checked stages,
\(16{,}832\) stop when only the final first level remains.
The program also checks the unordered character orbit under
each isogeny and the precise lower/upper-bound arithmetic.
These are finite algebra checks, not a proof of formal-group
existence or a substitute for the induction.

The first executed program and its successful output are
preserved. A subsequent harmless rewrite replaced division by
multiplication in one integer inequality, and the final exact
integer version was rerun successfully. No executed check
failed. The source chain is the fully audited actual quotient,
Newton, lower-break and mixed-threshold proofs B69/B71/B73/B63;
no additional theorem is inferred from the bounded B73
literature search.'''
assert old in t
source.write_text(t.replace(old,new))
outpath=own/'code/verify_iterated_high_quotient.output.json'
out=json.loads(outpath.read_text())
initial=json.loads((own/'code/verify_iterated_high_quotient.initial.output.json').read_text())
assert out['status']==initial['status']=='PASS'
assert out['counts']==initial['counts']
labels=re.findall(r'\\label\{([^}]+)\}',source.read_text())
assert len(labels)==5
now=datetime.now(timezone.utc).isoformat()
record={
    'status':'CANDIDATE_COMPLETE_PROOF_AND_EXACT_SUPPLEMENT',
    'actual_utc':now,
    'candidate':source.name,
    'candidate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'pre_certificate_sha256':hashlib.sha256(raw).hexdigest(),
    'labels':labels,
    'scope':'For p>=5, mu_p in K, perfect residue and p not dividing e: actual p^n with n>=3 determines the full B4 height-two character when e<p^n. Hence nu_min<=n-1, and nu_min=3 on p^3<e<p^4. No exact claim throughout p^4<e<p^5 or for p-divisible absolute ramification.',
    'program':'code/verify_iterated_high_quotient.py',
    'program_sha256':out['program_sha256'],
    'output':'code/verify_iterated_high_quotient.output.json',
    'output_sha256':hashlib.sha256(outpath.read_bytes()).hexdigest(),
    'author_runtime_seconds':out['elapsed_seconds'],
    'author_actual_utc':out['actual_utc'],
    'counts':out['counts'],
    'independent_audits':'Complete mathematical reads reported provisionally; final exact source/code audits requested, no promotion from this record.',
    'executed_failures':[],
    'successful_prior_version':{
        'program':'code/verify_iterated_high_quotient.initial.py',
        'output':'code/verify_iterated_high_quotient.initial.output.json',
        'runtime_seconds':initial['elapsed_seconds'],
        'actual_utc':initial['actual_utc'],
        'change':'Replaced an integer-valued division inequality by cross multiplication; mathematical counts unchanged.'
    },
    'dependency_read_scope':'B69 unrestricted comparison and actual quotient rules, B71 intrinsic marked-low proof, B73 full proof, B63 full mixed threshold/lower construction. No new external main-proof read claimed.'
}
(own/'outputs/B74_candidate_record.json').write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'CANDIDATE_COMPLETE_CHECKED',record['scope'],source.name+';outputs/B74_candidate_record.json','All-prime induction supplied; author exact finite code PASS; final independent audits pending'])+'\n')
print(json.dumps(record,indent=2))
