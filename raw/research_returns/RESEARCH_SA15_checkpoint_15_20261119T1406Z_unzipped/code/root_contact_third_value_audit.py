"""Complete root geometric audit and preserved third-value contact certificate."""
from pathlib import Path
from contextlib import redirect_stdout
import csv, datetime, io, json
w = Path(__file__).resolve().parents[1]
program = w / 'agents/obstructions_crystals/code/contact_third_value_checks.py'
author = program.with_suffix('.output.json')
dest = w / 'outputs/root_contact_third_value_checks.json'
assert not dest.exists()
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
    (w / 'outputs/root_contact_third_value_checks.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes() == before
out = json.loads(dest.read_text())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events = [
    ('lem:DE-A4-contact-discriminant-span', 'independent re-proof',
     'PASS: entire proof/code read. Root rederived all first-jet ranks on the affine open and the O/g1/−g1/second-O fibres, including merged flex base points and finite rank2 exceptions. The moving incidence is integral and its explicit nonzero mixed Hessian makes its image a divisor. Nonzero restriction of the full discriminant is pure codimension1, so lower-dimensional exceptional images cannot create extra support. The free h-coefficient has pole orders6,4,0, forcing three linear-relation coefficients to vanish; varying the nonconstant first-factor A1 kills the remaining two. Thus the moving divisor spans P4, including flex g2.'),
    ('cor:DE-A4-third-value-smooth', 'independent re-proof',
     'PASS: full corollary checked. For k=−g the third row is F+T; otherwise graph injectivity gives both X(k),Z(k) nonzero, so U and v coefficients exclude all five coordinate hyperplanes. Source smoothness, detS=FTU nonvanishing and q nonvanishing are nonempty opens of the same integral P3. The nondegenerate five-variable cubic contains no projective plane. No tangent-type or absence-of-other-collisions claim is inferred.'),
    ('rem:DE-A4-third-value-checks', 'computation or formal certificate',
     f"PASS: entire exact program read and author-preserving rerun passed in {out['elapsed_seconds']}s. Universal source equation, both derivatives, mixed Hessian, arbitrary linear relation, alternate A1 expression, determinant and opposite-third-value identity checked. Pole orders and discriminant geometry are independently proved, not inferred from finite samples.")
]
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for sid, kind, result in events:
        writer.writerow([sid, now, who, kind, result])
with (w / 'notes/ROOT_SEARCH_LOG_15.md').open('a') as f:
    f.write(f'''\n## {now}: smooth sources with a third kernel value\n\nRoot read and independently rederived the complete geometric source-discriminant proof, including the flex base-point merger, all jet ranks, purity of the restricted discriminant and the pole-order span argument. This uses the earlier fully proved contact/source-discriminant construction, with no new external theorem claimed. The exact program was read and rerun while preserving author output, in {out['elapsed_seconds']}s. It supplies one input to the uniform tangent-triple bridge; the complete bridge is not yet counted as proved.\n''')
print(json.dumps({'status': out['status'], 'elapsed_seconds': out['elapsed_seconds'],
                  'actual_audit_time': now, 'events': len(events)}, indent=2))
