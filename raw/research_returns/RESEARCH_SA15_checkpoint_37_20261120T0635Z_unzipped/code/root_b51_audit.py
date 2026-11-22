"""Root full finite-character proof audit and author-preserving B51 rerun."""
from pathlib import Path
from contextlib import redirect_stdout
import csv, datetime, io, json

w = Path(__file__).resolve().parents[1]
program = w / 'agents/reduction_descent/code/verify_tame_primitive_norm_orbits.py'
author = program.with_suffix('.output.json')
dest = w / 'outputs/root_verify_tame_primitive_norm_orbits.json'
summary_path = w / 'outputs/root_b51_audit.json'
assert not dest.exists() and not summary_path.exists()
before = author.read_bytes()
old_write = Path.write_text
capture = io.StringIO()
def write(path, data, *args, **kwargs):
    assert path.resolve() == author.resolve()
    return old_write(dest, data, *args, **kwargs)
try:
    Path.write_text = write
    with redirect_stdout(capture):
        exec(compile(program.read_text(), str(program), 'exec'),
             {'__name__': '__main__', '__file__': str(program)})
finally:
    Path.write_text = old_write
    (w / 'outputs/root_verify_tame_primitive_norm_orbits.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes() == before
out = json.loads(dest.read_text())
assert out['status'] == 'PASS'
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events = [
    ('lem:B-RD51-orbits', 'independent re-proof',
     'PASS: entire statement and proof independently read and rederived. If d is an odd divisor of p+1, gcd(d,p-1)=1 and gcd((p-1)q,p+1)=q, so the norm map from mu_m has surjective image mu_(p-1) and every primitive-norm fibre has q elements. Frobenius is an involution on it, with no fixed point because a scalar norm is a square and cannot be primitive in the even-order group mu_(p-1). Thus the fibre is exactly q/2 rank-two eigenvalue orbits. The unit reduction map from Z/m units to Z/(p-1) units is surjective by avoiding extra prime divisors using CRT, so every primitive-norm fibre contains a primitive mth root. When q>=4 an element in another orbit gives a distinct abstract character pair of joint order m; q2 gives none. The reduction to q>=4 applies to actual BT comparisons only as a necessary condition, and no realization is asserted.'),
    ('cor:B-RD51-p5', 'independent re-proof',
     'PASS: the normalized p5 possibilities m8,24 reduce to24 since m8 has q2. The six norm exponents1 modulo4 in Z/24 have the three Frobenius orbits {1,5},{9,21},{13,17}; their faithful orders are24,8,24. Simultaneous quadratic twist adds12, interchanges the two24 types and fixes the8 type. There are exactly two unordered distinct-type pair orbits, represented by {A,B} and {A,C}. This retains both remaining cases and makes no torsion-congruence existence claim.'),
    ('B51-EXACT-CERTIFICATE', 'computation or formal certificate',
     f"PASS: complete program read, then independently rerun with author output unchanged, in {out['elapsed_seconds']} seconds. It checks {out['primitive_norm_fibres']} primitive-norm fibres and {out['distinct_character_pairs']} distinct character pairs for every prime5<=p<=101, including the exact p5 twist orbits. The program checks finite cyclic character arithmetic only.")
]
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for sid, kind, result in events:
        writer.writerow([sid, now, who, kind, result])
summary = {'status': 'PASS', 'actual_utc': now,
           'elapsed_seconds': out['elapsed_seconds'],
           'complete_mathematical_assertions': 2, 'events': len(events),
           'remaining_gate': 'Primitive-norm q=(p+1)/d>=4 only. At p5 joint24 with pair types24/8 or opposite quadratic-twist24/24; no BT realization claim.'}
summary_path.write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
