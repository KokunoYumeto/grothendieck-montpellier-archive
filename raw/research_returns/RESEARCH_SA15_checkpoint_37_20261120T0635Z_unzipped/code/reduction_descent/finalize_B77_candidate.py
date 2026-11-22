from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

own = Path(__file__).resolve().parents[1]
source = own / 'B_first_wild_finite_patterns_candidate.tex'
raw = source.read_bytes()
saved = own / 'notes/B_first_wild_finite_patterns.before_certificate.tex'
assert not saved.exists()
saved.write_bytes(raw)
outpath = own / 'code/verify_first_wild_finite_patterns.output.json'
data = json.loads(outpath.read_text())
assert data['status'] == 'PASS'
t = raw.decode()
assert t.count(r'\end{remark}') == 1
paragraph = r'''
The retained exact supplement is
\path{code/reduction_descent/verify_first_wild_finite_patterns.py}.
Its first author run passed in \(0.6461968240037095\) seconds
at 23:15:03 UTC on 19 November 2026. For the \(24\) primes
from \(5\) through \(101\), it checks \(174\) norm-one
good-degree rows, \(348{,}000\) closed coefficientwise logarithm
inequalities, \(2{,}560{,}584\) low-degree coefficient bounds,
and all \(24\) weighted three-step upper bounds. The explicit
\(p=5\) primitive-norm fibres and quadratic-twist pair orbits
are retained separately. These finite arithmetic checks do
not imply existence of a BT group or a torsion congruence.
The complete code, output, finite ranges and pre-certificate
proof are retained; no executed computation failed.
'''
t = t.replace(r'\end{remark}', paragraph + r'\end{remark}')
source.write_text(t)
labels = re.findall(r'\\label\{([^}]+)\}', t)
assert len(labels) == 4
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'CANDIDATE_COMPLETE_PROOF_AND_EXACT_SUPPLEMENT',
    'actual_utc': now, 'candidate': source.name,
    'candidate_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'pre_certificate_sha256': hashlib.sha256(raw).hexdigest(),
    'labels': labels,
    'scope': 'p>=5, e=p(p-1), height2, mu_p in K and perfect residue: least full B4 index lies in{2,3}; every actual p^3 failure is whole/whole with nonsquare finite determinant. At p5/e20 the normalized joint degree is24 and the two remaining type patterns are A/B and A/C up to interchange and common quadratic twist. No actual counterexample or exact wild least index is asserted.',
    'program': 'code/verify_first_wild_finite_patterns.py',
    'program_sha256': hashlib.sha256((own / 'code/verify_first_wild_finite_patterns.py').read_bytes()).hexdigest(),
    'output': str(outpath.relative_to(own)),
    'output_sha256': hashlib.sha256(outpath.read_bytes()).hexdigest(),
    'author_runtime_seconds': data['runtime_seconds'],
    'author_actual_utc': data['actual_utc'], 'counts': data['counts'],
    'source_scope': 'Complete B50 closed-logarithm/square-twist, B64 actual-target graph/saturation proof and B51 finite-character arithmetic reread. B76 mixed and determinant reduction used as proved. Original Bondarko and Tate passages are previously fully audited dependencies; no new external source read claimed.',
    'independent_audits': 'Full proof and exact-code audit requested from root and OC; no promotion yet.',
    'executed_failures': [], 'checkpoint_scope': 'Separate post-CP27 candidate; no global wiring.'
}
(own / 'outputs/B77_candidate_record.json').write_text(json.dumps(record, indent=2) + '\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'CANDIDATE_COMPLETE_CHECKED', record['scope'],
                            'B_first_wild_finite_patterns_candidate.tex;outputs/B77_candidate_record.json',
                            'Complete proof and exact supplement PASS; full independent audits pending']) + '\n')
print(json.dumps(record, indent=2))
