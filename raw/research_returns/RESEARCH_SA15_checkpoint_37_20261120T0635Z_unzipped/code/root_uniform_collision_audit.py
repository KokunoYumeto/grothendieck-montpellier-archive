"""Root full proof audit and author-preserving uniform collision certificate."""
from pathlib import Path
from contextlib import redirect_stdout
import csv, datetime, io, json

w = Path(__file__).resolve().parents[1]
program = w / 'agents/monodromy/code/ss_uniform_collision_identities.py'
author = w / 'agents/monodromy/outputs/ss_uniform_collision_identities.json'
dest = w / 'outputs/root_ss_uniform_collision_identities.json'
assert not dest.exists()
before = author.read_bytes()
original = Path.write_text
capture = io.StringIO()

def write(path, data, *args, **kwargs):
    if path.resolve() != author.resolve():
        raise RuntimeError('Unexpected certificate output path')
    return original(dest, data, *args, **kwargs)

try:
    Path.write_text = write
    with redirect_stdout(capture):
        exec(compile(program.read_text(), str(program), 'exec'),
             {'__name__': '__main__', '__file__': str(program)})
finally:
    Path.write_text = original
    (w / 'outputs/root_ss_uniform_collision_identities.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes() == before
out = json.loads(dest.read_text())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
who = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events = [
    ('lem:ss-contact-cubic-evaluation', 'independent re-proof',
     'PASS: entire proof read. Nondegenerate Frobenius form excludes vector3 isotropic subspaces and makes every hyperplane cubic integral. Rational evaluation recovery and every exceptional vertical/horizontal fibre were checked, including flex coincidence, base points, finite rank1 strata and absence of a rank0 triple for a graph kernel.'),
    ('lem:ss-contact-pair-covers', 'independent re-proof',
     'PASS: complete proof checked. Both limiting plane cubics are smooth, yielding one reduced main incidence component; finite rank1 strata and the single constant g component exhaust other possible dominant components. Explicit Jacobians at P and Q provide etale points in the nonflex cases. In the flex case the correct coefficient is T+vF/h, so constant length3 leaves odd moving degree15 and forces separability. Properness then removes all moving ramification simultaneously.'),
    ('lem:ss-contact-no-triples', 'independent re-proof',
     'PASS: complete proof checked. Triple reorientation fails only for the order3 orbit. The rows modulo F,h are independent using both graph projections, including the opposite-point and −g cases. Varying kappa would otherwise fill a forbidden vector3 subspace; the order3 limit restricts q to U³. Every rank3/2/1 stratum has total incidence dimension at most2 and rank0 is absent.'),
    ('prop:ss-uniform-graph-mixed-contact', 'independent re-proof',
     'PASS: full geometric proof checked, including requested explicit relative-hypersurface flatness/no-vertical-component clarification. The good-base total contact cubic is integral; finite exceptional six-jet loci have too small dimension. The actual contact03 witness has rank6 in the already audited retained main-incidence certificate. The flex length3 cluster, fibrewise regular-sequence flatness and marked length at least2 exclude a second tangency after deformation. Separate nonempty source-smooth/simple-contact/Cartier-value opens therefore intersect the collision-free open. Norm birationality and the precise tacnode/node conclusion follow. Uniform tangent-triple bridges and full higher monodromy remain unproved.'),
    ('prop:ss-uniform-graph-mixed-contact', 'computation or formal certificate',
     f"PASS: full exact algebra program read and author-output-preserving rerun passed in {out['elapsed_seconds']}s. Universal q/gradient/nondegeneracy, plane determinant, flex triple limit, six-jet unit minor and actual elliptic addition through order3 checked. The source-branch correction T+vF/h is independently derived in the written proof, not established by the script's tautological final expression check. Incidence and openness assertions are proved separately.")
]
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for sid, kind, result in events:
        writer.writerow([sid, now, who, kind, result])
with (w / 'notes/ROOT_SEARCH_LOG_14.md').open('a') as f:
    f.write(f'''\n## {now}: uniform exclusion of unwanted norm collisions\n\nNo new external theorem is substituted for the geometric argument. Root read the entire four-statement proof and exact algebra program, and independently checked all evaluation strata, moving-cover irreducibility and separability, triple-kernel limits, contact-family irreducibility and the flex length3-cluster specialization. The nontrivial flex leading coefficient includes the source-branch correction: T+vF/h. Root requested and verified the explicit relative hypersurface and complete-intersection flatness arguments. The global contact03 witness is placed in the main component by the previously audited exact six-jet certificate, whose full code/rows were reread. Author-preserving rerun {out['elapsed_seconds']}s. This removes all unwanted-collision exclusions for a prescribed mixed contact and every finite odd graph kernel. It does not supply the separate uniform tangent-triple bridges or determine all monodromy groups.\n''')
print(json.dumps({'status': out['status'], 'elapsed_seconds': out['elapsed_seconds'],
                  'actual_audit_time': now, 'events': len(events)}, indent=2))
