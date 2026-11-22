from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

own = Path(__file__).resolve().parents[1]
source = own / 'B_wild_cyclic_point_candidate.tex'
raw = source.read_bytes()
saved = own / 'notes/B_wild_cyclic_point.before_certificate.tex'
assert not saved.exists()
saved.write_bytes(raw)
outpath = own / 'code/verify_wild_cyclic_point.output.json'
data = json.loads(outpath.read_text())
assert data['status'] == 'PASS'
needle = r'\end{remark}'
t = raw.decode()
assert t.count(needle) == 1
paragraph = r'''
The retained supplement is
\path{code/reduction_descent/verify_wild_cyclic_point.py}.
Its first author run passed in \(3.575578117000987\) seconds
at 23:06:45 UTC on 19 November 2026. It checks \(431{,}375\)
finite Newton parameter pairs, \(100{,}121\) inverse branches
and \(4{,}349\) integral torsion-valuation chains through level
six; \(2{,}734\) chains have wild absolute index. All five
cases of the proof occur in the retained finite data, including
three consecutive high inverse steps. The separate arithmetic
checks cover \(1{,}584\) uniform equality cases,
\(1{,}104{,}000\) good-degree transfers and \(396{,}000\)
cyclotomic denominators. These are exact rational calculations,
not constructions of points or formal groups. The full code,
output, finite ranges and pre-certificate proof are preserved;
no executed computation failed.
'''
t = t.replace(needle, paragraph + needle)
source.write_text(t)
labels = re.findall(r'\\label\{([^}]+)\}', t)
assert len(labels) == 5
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'CANDIDATE_COMPLETE_PROOF_AND_EXACT_SUPPLEMENT',
    'actual_utc': now, 'candidate': source.name,
    'candidate_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'pre_certificate_sha256': hashlib.sha256(raw).hexdigest(),
    'labels': labels,
    'scope': 'p>=5, arbitrary absolute index e, perfect residue. Rational p^n point forces a>(p^2-1)p^(2n-3-v_p(a)); mixed whole/filtered comparison forces e>p^(2n-3-v_p(e)). With mu_p in K and n>=v_p(e)+2, the determinant fixes dimension. At p5/e20 all actual125 failures are confined to the two-whole-potentially-supersingular branch. No exact wild least-index upper claim.',
    'program': 'code/verify_wild_cyclic_point.py',
    'program_sha256': hashlib.sha256((own / 'code/verify_wild_cyclic_point.py').read_bytes()).hexdigest(),
    'output': str(outpath.relative_to(own)),
    'output_sha256': hashlib.sha256(outpath.read_bytes()).hexdigest(),
    'author_runtime_seconds': data['runtime_seconds'],
    'author_actual_utc': data['actual_utc'],
    'counts': data['counts'], 'terminal_modes': data['terminal_modes'],
    'source_scope': 'Complete B63 Newton/inverse-polygon proof and B49 tame-inertia/quotient/twist/determinant proofs reread. Original Hopkins-Gross coefficient theorems are the same previously fully audited dependencies; no new external main-proof read claimed.',
    'independent_audits': 'Full proof and exact-code audit requested from root and OC; no promotion from finite checks.',
    'executed_failures': [], 'checkpoint_scope': 'Separate post-CP27 candidate; no immutable checkpoint changes.'
}
(own / 'outputs/B76_candidate_record.json').write_text(json.dumps(record, indent=2) + '\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'CANDIDATE_COMPLETE_CHECKED', record['scope'],
                            'B_wild_cyclic_point_candidate.tex;outputs/B76_candidate_record.json',
                            'Complete proof and exact supplement PASS; full independent audits pending']) + '\n')
print(json.dumps(record, indent=2))
