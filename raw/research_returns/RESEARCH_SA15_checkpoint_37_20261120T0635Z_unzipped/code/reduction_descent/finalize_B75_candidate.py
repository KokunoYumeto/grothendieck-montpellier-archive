from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

own=Path(__file__).resolve().parents[1]
source=own/'B_terminal_frobenius_pair_candidate.tex'
raw=source.read_bytes()
before=own/'notes/B_terminal_frobenius_pair.before_certificate.tex'
assert not before.exists()
before.write_bytes(raw)
t=raw.decode()
old='''A finite exact character/threshold supplement is being prepared;
the argument itself is the all-prime character calculation above.'''
new=r'''The retained exact supplement is
\path{code/reduction_descent/verify_terminal_frobenius_pair.py}.
The author run passed in \(0.08401663199765608\) seconds
at 22:54:37 UTC on 19 November 2026. For all \(24\) primes
from \(5\) through \(101\), it checks the \(75{,}960\)
compatible terminal character pairs, including \(1{,}132\)
unequal Frobenius pairs, and \(144\) full-monodromy threshold
inequalities. The explicit next arithmetic pair is separately
marked as having no asserted realization. A \(p=5,e=128,n=3\)
scope check records that the formal bound applies while the
mixed full-monodromy obstruction does not, preventing an
incorrect index-two conclusion. These finite checks support
the formulas; the proof remains the all-prime calculation
and the already audited actual quotient induction. No
executed computation failed.'''
assert old in t
source.write_text(t.replace(old,new))
outpath=own/'code/verify_terminal_frobenius_pair.output.json'
out=json.loads(outpath.read_text())
assert out['status']=='PASS'
labels=re.findall(r'\\label\{([^}]+)\}',source.read_text())
assert len(labels)==4
now=datetime.now(timezone.utc).isoformat()
record={
    'status':'CANDIDATE_COMPLETE_PROOF_AND_EXACT_SUPPLEMENT',
    'actual_utc':now,
    'candidate':source.name,
    'candidate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'pre_certificate_sha256':hashlib.sha256(raw).hexdigest(),
    'labels':labels,
    'scope':'p>=5, mu_p in K, perfect residue and p not dividing e. Whole formal actual p^n recovery for n>=3 and e<p^(n-1)(p+1); full B4 upper nu<=n-1 only for n>=4. Exact nu3 on p^3<e<p^3(p+1), including p5/e628..748; nextp5/e752 remains3..4.',
    'program':'code/verify_terminal_frobenius_pair.py',
    'program_sha256':out['program_sha256'],
    'output':'code/verify_terminal_frobenius_pair.output.json',
    'output_sha256':hashlib.sha256(outpath.read_bytes()).hexdigest(),
    'author_runtime_seconds':out['elapsed_seconds'],
    'author_actual_utc':out['actual_utc'],
    'counts':out['counts'],
    'source_scope':'Self-contained finite-character arithmetic and complete audited B74 quotient induction/B63 mixed threshold. No new external theorem or primary-source reread claimed.',
    'checkpoint_scope':'Separate from frozen CP27 canonical paper; no global wiring or report mutation.',
    'independent_audits':'Requested; no promotion from this record.',
    'executed_failures':[]
}
(own/'outputs/B75_candidate_record.json').write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'CANDIDATE_COMPLETE_CHECKED',record['scope'],source.name+';outputs/B75_candidate_record.json','Complete all-prime proof and exact author checker PASS; independent audits pending; separate from frozen CP27'])+'\n')
print(json.dumps(record,indent=2))
