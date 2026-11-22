"""Complete initial tame-sector proof audit and retained independent rerun."""
from pathlib import Path
import csv, datetime, hashlib, json, subprocess, sys

w = Path(__file__).resolve().parents[1]
candidate = w / 'agents/reduction_descent/B_initial_tame_sector_candidate.tex'
assert hashlib.sha256(candidate.read_bytes()).hexdigest() == '950f85373f69014b75339d60735c757bfec1cb90576a0dd7d910d1d189709e7a'
source = w / 'agents/reduction_descent/code/verify_initial_tame_sector.py'
author = source.with_suffix('.output.json')
before = author.read_bytes()
dest = w / 'outputs/root_B68_audit.json'
snap = w / 'code/audit_snapshots/B68_root_independent_certificate.py'
assert not dest.exists() and not snap.exists()
snap.write_bytes(source.read_bytes())
run = subprocess.run([sys.executable, str(snap)], capture_output=True, text=True)
(w / 'outputs/root_B68_independent_certificate.stdout.txt').write_text(run.stdout)
(w / 'outputs/root_B68_independent_certificate.stderr.txt').write_text(run.stderr)
assert run.returncode == 0, run.stderr
data = json.loads(snap.with_suffix('.output.json').read_text())
old = json.loads(before)
omit = {'actual_utc', 'runtime_seconds'}
assert {k: v for k, v in data.items() if k not in omit} == {k: v for k, v in old.items() if k not in omit}
assert before == author.read_bytes()
(w / 'outputs/root_B68_independent_certificate.json').write_text(json.dumps(data, indent=2) + '\n')
checks = {
    'lem:B-RD68-rules': (
        'All arguments rederived at e=t(p-1),2<=t<=p-1, with s=e(p+1)=tN prime to p. '
        'After the common nonsquare twist c=1 mod(p-1), one Newton slope and reducible '
        'residual inertia would give a scalar Fp tame action and square determinant, a '
        'contradiction. The high line is L-rational; its integral valuation gives the '
        'integer odd B, slopes s-B,B/p, bound0<B<pe and character zeta^(c-B). Low-target '
        'inverse points have valuationB/p^3. In the common cyclic wild residual field R/L, '
        'the lower break is ps-(p+1)B for prime B and strictly smaller for divisible B. '
        'Mixed divisibility first forces B1>B2. The common primitive point field E/R is '
        'a torsor under the R-rational first-level module; its denominator forces degreep^2. '
        'A low translation then gives the opposite inequality from the common actual '
        'uniformizer break. For tame residuals, two prime b=B/p likewise give equal b '
        'in the actual common point field, and a high-only translation excludes unequal '
        'high lines. Equal high characters then recover c. The original L/R field slip '
        'was corrected before this audit and its exact old text/diff retained.'
    ),
    'lem:B-RD68-quotients': (
        'The coordinate of an actual cyclic quotient is the product over its rankp '
        'kernel, up to an integral unit. For the high quotient, the high-target inverse '
        'polygon has q roots of valuationalpha/q above B=e, and below it has p roots '
        'of valuation(s-pB)/p and q-p of valuationB/p. All are belowalpha; multiplication '
        'of valuations byp and the exact quotient multiplicities yield B_H=s-B orpB. '
        'Equality is excluded by Bodd, eeven. For a low line, each nonzero residual '
        'quotient class has a high representative, with quotient valuationalpha+(p-1)beta '
        '=s-B/p; all other p-points have valuationB/p^2 and countq-p. ThusB_J=B/p. '
        'The finite flat kernel has unique special rankp subgroupkerF, so the special '
        'quotient Frobenius-twists c to pc and preserves the unordered special orbit. '
        'The stable generic line ensures descent. The exact group '
        '{P inM[p^3]:p^2P inJ}/J is the quotient p^2-torsion, so the comparison is '
        'between actual groups with their specified lattices.'
    ),
    'prop:B-RD68-nonsquare': (
        'Irreducible residual inertia is now covered by the separately fully audited '
        'arbitrary-index B67 theorem. In the wild reducible case, prime and mixed B '
        'divisibilities follow from the rules. Both small divisible B give '
        '0<b=B/p<e/p<p-1 and b1=b2 mod(p-1), hence equality. Both large B have prime '
        'high quotients; opposite sides have opposite quotient divisibilities. In the '
        'tame case, two prime b are covered. For b1 prime and b2=pk, B2=p^2k>e '
        'becausee<p^2. Unequal high lines give the necessary inequality '
        'p^2(alpha1-pk)<=b1-pk. Butalpha1>=e+p andpk<e make its left side greater '
        'thanp^3, while the right side is less thanp^2. Thus high lines agree, and '
        'the quotient rules exclude both remaining parameter positions. If bothb '
        'are divisible, equal high lines give two prime high quotients; unequal ones '
        'allow a common stable line high in one model and low in the other, giving '
        'forbidden mixed quotient divisibility. This exhausts all cases.'
    ),
    'lem:B-RD68-square': (
        'A common finite square-root twist gives special norm-one eigenvalues and '
        'actual simultaneous good degreem dividingp+1. The disjoint spectra are the '
        'finite SPECIAL inertia orbits, not the common generic residual modules. '
        'The fresh full B64 graph proof supplies integral perfect pairings, '
        'self-orthogonality, integral special tame projectors and '
        'H_k=kerF^3 timeskerF^3. The actual quotient Q has the two Frobenius-twisted '
        'height2 special factors. For the map toQ timesM, the generic kernel is trivial '
        'and the special kernel is0 timeskerF^3. On THIS target, special orderp^2 '
        'and the invariant-differential derivative identity give unweighted recurrence '
        'min(a+q,pq+1,p^2q). Sincea>=e>=2(p-1)>=p, q1>=p+1 and '
        'q2>=min(a+p+1,p^2+p+1)>=a/(p-1), usinga/(p-1)<=p^2-1. The freshly '
        'reread coefficientwise logarithm, bounded Cartier projection and saturation '
        'argument of B64 then kill the special kernel byF^2, contradictingkerF^3. '
        'No source coefficient thickness is transferred to the quotient.'
    ),
    'thm:B-RD68': (
        'The B63 actual cyclic construction applies ate>p and(p-1)|e, proving '
        'failure of uniform p^2 determination. For an actualp^3 comparison, p-primee '
        'makes the cyclotomic p-part have orderp^2. The determinant dimensions0,1,2 '
        'are separated because their difference has absolute value less thanp; '
        'finite determinant values are then equal. Dimension0 is the Brauer lift '
        'of the residual semisimplification, dimension2 its Cartier-dual case. '
        'Dimension1 reduces to two filtered height1 systems, two whole formal '
        'systems, or a mixed pair. The first is detected modulo p, the mixed case '
        'is excluded by the fully audited exact threshold e<p^3, and the two '
        'whole cases are proved above. Hence nu_min(p,t(p-1),2)=2 for every '
        '2<=t<=p-1, p>=5, including(5,16,2).'
    ),
    'rem:B-RD68-scope': (
        'The full program was read and its exact independent rerun agrees in all '
        'mathematical data, with the author output preserved. The six-prime,60-sector '
        'enumeration checks Newton hulls, actual quotient root multiplicities, '
        'tangent congruences, point-field inequalities and actual-target bounds only. '
        'The all-prime conclusion is the symbolic proof. The theorem does not '
        'extend to t>=p or p-divisiblee and does not classify higher heights.'
    ),
}
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for label, detail in checks.items():
        writer.writerow([label, now, 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15',
                         'targeted proof check', 'PASS. ' + detail])
record = {
    'status': 'FULL ALL-PRIME PROOF, TYPED-DEPENDENCY AND EXACT-CERTIFICATE PASS',
    'actual_utc': now,
    'candidate': str(candidate.relative_to(w)),
    'candidate_sha256': hashlib.sha256(candidate.read_bytes()).hexdigest(),
    'independent_runtime_seconds': data['runtime_seconds'],
    'counts': data['counts'],
    'sectors_checked': data['sectors_checked'],
    'author_output_sha256': hashlib.sha256(before).hexdigest(),
    'author_output_unchanged': True,
    'all_mathematical_output_equals_author_output': True,
    'checks': checks,
    'corrected_before_verdict': [
        'Wild residual point field uses R-rational, not L-rational, first-level module.',
        'Disjoint eigenvalue orbits are finite SPECIAL inertia, not generic residual modules.',
    ],
    'source_scope': 'Fresh full B64 coefficient/logarithm/Cartier and graph arguments read. B67 complete root proof/source/code pass immediately precedes this audit. Earlier fully audited B63 actual threshold and construction are reused without claiming another fresh source retrieval.',
}
dest.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
