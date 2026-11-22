"""Retain the complete prime-Heisenberg proof/source/program audit.

All author programs are copied literally to a new isolated directory.  No
author output is overwritten.  The three full mathematical JSON outputs are
compared, excluding only timestamps, timings and resource measurements.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import sys

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
author = root / 'agents/monodromy'
source = author / 'post_CP35_prime_Heisenberg_rank_candidate.tex'
source_hash = '1a03b3733ace0faf2b6e4419b2a079e9439fb95699deb3be386258564ed4c59d'
programs = [
    ('post_CP35_prime_Pfaffian_support_certificates.py',
     'c14ba47ef27ae745a688b8141d3ceed67bca874b470dd9e3d834c134c1c532ac',
     'a4f4fd3ef4ce350a6d2d78433a8ffc7dbfed601fa8d56655dec1bed6fe096988'),
    ('post_CP35_prime17_Pfaffian_support_certificate.py',
     'bfd084d2aa0d7313597b966e7856d0e1bd2f90dad89c07819bc6314dd97a3505',
     '1baf8e2da9a6b10768478d17543aed206c0658d44d34499a81e005df9e001424'),
    ('post_CP35_prime_multiplication_minor_probe.py',
     '0332b4482f3c570dfd647a595203f2eeaa61118d0b00a7df86c054ee0f5c6550',
     '2613dff7402b94b3d36c6ffcfc604af74e69793d50d33a2000b12e3f04aa32ab'),
]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
expected = {source: source_hash}
for name, program_hash, output_hash in programs:
    path = author / 'code' / name
    expected[path] = program_hash
    expected[path.with_suffix('.output.json')] = output_hash
for path, digest in expected.items():
    assert sha(path) == digest, str(path)
labels = re.findall(r'\\label\{([^}]+)\}', source.read_text())
assert len(labels) == 6
isolated = own / 'outputs/prime_Heisenberg_independent_run'
isolated.mkdir(exist_ok=False)
excluded = {'actual_utc', 'runtime_seconds', 'coefficient_reconstruction_seconds',
            'peak_rss_kib'}
mathematical = lambda d: {k: v for k, v in d.items() if k not in excluded}
reruns = []
for name, program_hash, output_hash in programs:
    original_path = author / 'code' / name
    copied = isolated / name
    copied.write_bytes(original_path.read_bytes())
    assert sha(copied) == program_hash
    run = subprocess.run([sys.executable, str(copied)], cwd=isolated,
                         capture_output=True, text=True)
    (isolated / (copied.stem + '.stdout.txt')).write_text(run.stdout)
    (isolated / (copied.stem + '.stderr.txt')).write_text(run.stderr)
    assert run.returncode == 0, run.stderr
    result = json.loads(copied.with_suffix('.output.json').read_text())
    original = json.loads(original_path.with_suffix('.output.json').read_text())
    assert result['status'] == 'PASS'
    assert mathematical(result) == mathematical(original), name
    reruns.append({
        'program': str(original_path.relative_to(root)),
        'program_sha256': program_hash,
        'author_output_sha256': output_hash,
        'isolated_program': str(copied.relative_to(root)),
        'isolated_output': str(copied.with_suffix('.output.json').relative_to(root)),
        'isolated_output_sha256': sha(copied.with_suffix('.output.json')),
        'actual_utc': result['actual_utc'],
        'runtime_seconds': result['runtime_seconds'],
        'status': result['status'],
        'all_mathematical_fields_identical': True,
    })
preserved = {str(p.relative_to(root)): {'before': h, 'after': sha(p)}
             for p, h in expected.items()}
(isolated / 'author_hashes.json').write_text(json.dumps(preserved, indent=2) + '\n')
assert all(v['before'] == v['after'] for v in preserved.values())
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'FULL PASS',
    'actual_utc': now,
    'candidate': str(source.relative_to(root)),
    'candidate_sha256': source_hash,
    'labels': labels,
    'full_read_scope': 'Entire final six-label candidate and all three complete standalone programs read; all proof steps independently rederived. No sampling replaces the universal coefficient argument.',
    'checks': [
        'Clock equivariance forces output index(i+j)/2 in W^(2), and shift equivariance forces dependence on i-j. Alternation gives c0=0 and c_a=c_-a. Independently deriving multiplication gives M_s(k,j)=c_2(k-j)s_2k-j, rather than an alternating reindexing of the dual contraction. The incidence B_y s=0 iff M_s^t y=0 has the displayed types.',
        'Each checker expands every perfect matching on indices1..p-1, with characteristic-two signs removed and repeated monomials cancelled by symmetric difference. For each exact nonempty coefficient support the chosen y-coefficient has exactly one surviving nonzero c-monomial. Thus every parameter on that support torus has a nonzero maximal Pfaffian over every characteristic-two field. The assertion is universal for the six listed primes only.',
        'The small-prime tuple computation covers1,3,7,31,63 supports. The full p17 recursion enumerates15!!=2027025 matchings, yielding1465345 terms in43263 nonzero y-coefficients and255 support witnesses. Four-bit packing is injective because total degree is8; support extraction, full-coefficient witness retention and cancellation are literal. Entire witness arrays, not only counts, agree on the isolated rerun.',
        'The separate multiplication program expands the row0/column0-deleted cofactor directly, using the actual M_s formula and characteristic-two determinant signs. Five-bit packing has no carry at the stated degrees. It checks the Euler s0 factor and all supports for3,5,7,11. It is a supplementary direct verification, not an extrapolation to17.',
        'For a degree-p central division algebra, a closed splitting point with residue E makes E^p a left D-module, so p divides[E:F]. Graph closure has first multiplicity a0=1. Over a splitting field the p split Chow basis correspondences are mutually orthogonal idempotents: middle exponents add to p-1 exactly for equal indices. Composition to the(p-1)st power and diagonal Gysin pullback give a zero-cycle degree sum a_i^(p-1), divisible byp. Fermat reduction counts between1 andp nonzero coefficients, hence allp. The second multiplicity is nonzero and the rational map is dominant. This proof is integral and does not assume separability or resolution.',
        'The finite projective Heisenberg actions factor throughD0=(Z/p)^2. Twisting by the Kummer(a,b)-torsor gives Brauer classes alpha and-2alpha for weights1 and-2. OverF=k(a)((b)), L=F(a^(1/p)) is unramified of residue degreep. The cyclic-algebra filtration v_b(ell_i)+i/p has a unique leading term; products retain a nonzero leading coefficient. Hence the degree-p cyclic algebra is division.',
        'Over the target Severi-Brauer function field alpha splits, so the source twist of class-2alpha is projective space. Its nonempty rational-map domain has a rational point over the infinite target function field. This constructs a rational map back whose composite is actually defined. The self-map dominance lemma forces dominance of the twisted original map, and faithfully flat extension/twisting gives original dominance. No undefined composition or characteristic restriction from an orthogonal application is imported.',
        'The radical map is Heisenberg-equivariant on its dual rank(p-1) open. Each scheme-theoretic fibre is the intersection of that open with the projective linear space ker(M_s^t). Dominance between equal-dimensional spaces forces the generic such space to be a point. Hence M_s has generic rankp-1, and its kernel minors define the actual rational inverse. Birationality and separability follow, rather than only injectivity on geometric points.',
        'The maximal-Pfaffian ideal is preserved by the theta action. The gcd line is therefore a one-dimensional character, trivial on the commutator centre. Its homogeneous central weight has absolute value2deg(g), forcing p|2deg(g). Since0<=deg(g)<p, the gcd is constant. This proves codimension at least2 for the base locus and makes no height3 claim.',
        'The final scope correctly distinguishes universal dual rank at the six listed primes from the all-prime conditional birationality theorem. It asserts no generic Euler bijectivity, no nonempty Euler wall, no connected nonzero Lang cover and no fixed-principal degree17 full group.',
    ],
    'primary_source_scope': {
        'fresh_original_reads': [
            {
                'title': 'Upper motives of algebraic groups and incompressibility of Severi-Brauer varieties',
                'author': 'N. A. Karpenko',
                'version': '18 April2009 preprint',
                'url': 'https://www.math.uni-bielefeld.de/lag/man/333.pdf',
                'read_scope': 'Full proofs of Lemmas2.21 and2.23 and Corollaries2.22 and2.24, printed pp9-10; preliminary introduction also opened. No full-paper audit claimed.',
                'tool_refs': ['turn478057882view0', 'turn915871961view1'],
            },
            {
                'title': 'On anisotropy of orthogonal involutions',
                'author': 'N. A. Karpenko',
                'url': 'https://sites.ualberta.ca/~karpenko/publ/aoinew.pdf',
                'read_scope': 'Complete correspondence preliminaries Example1.2 through Corollary1.9, and Theorem2.1 with its entire proof and Corollary2.3 proof, printed pp2-5. Proposition2.2 is an externally cited statement in the original, whose external proof was not opened; the candidate uses its own elementary prime-degree diagonal-trace proof instead.',
                'tool_refs': ['turn478057882view1', 'turn915871961view0', 'turn631917634view0'],
            },
        ],
        'source_boundary': 'The candidate contains a self-contained prime-degree proof. No orthogonal-involution characteristic restriction and no unopened proof of the general prime-power incompressibility theorem are used. One preceding web response was truncated at context rollover; the missing Theorem2.1 proof was subsequently actually retrieved and read in turn631917634view0.',
    },
    'reruns': reruns,
    'excluded_comparison_fields': sorted(excluded),
    'all_mathematical_output_identical': True,
    'all_author_bytes_unchanged': True,
    'author_hash_record': str((isolated / 'author_hashes.json').relative_to(root)),
    'scope': 'Complete six-assertion independent proof/source/code PASS. Universal exact coefficient certificates plus self-contained Severi-Brauer dominance and linear-fibre birationality; no actual geometric full-group conclusion.',
}
audit = own / 'prime_Heisenberg_independent_audit.json'
with audit.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now, label, 'independent_full_proof_source_code_audit',
                           str(source.relative_to(root)),
                           'Full typed tensor, universal support witnesses, prime SB twist and birationality; three literal isolated reruns',
                           'PASS', str(audit.relative_to(root))]) + '\n')
print(json.dumps({'status': 'FULL PASS', 'actual_utc': now,
                  'record': str(audit.relative_to(root)),
                  'candidate_sha256': source_hash,
                  'labels': labels,
                  'reruns': reruns,
                  'all_mathematical_output_identical': True,
                  'author_bytes_unchanged': True}))
