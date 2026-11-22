"""Check the added actual flex branch substitution; retain the initial root run."""
from pathlib import Path
from contextlib import redirect_stdout
import csv, datetime, io, json
w = Path(__file__).resolve().parents[1]
program = w / 'agents/monodromy/code/ss_uniform_collision_identities.py'
author = w / 'agents/monodromy/outputs/ss_uniform_collision_identities.json'
dest = w / 'outputs/root_ss_uniform_collision_identities_final.json'
assert not dest.exists()
assert (w / 'outputs/root_ss_uniform_collision_identities.json').exists()
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
    (w / 'outputs/root_ss_uniform_collision_identities_final.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes() == before
out = json.loads(dest.read_text())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
assert out['source_branch_degree3_coefficient'] == 'h*k+F'
assert out['translated_branch_degree3_coefficient'] == 'T+v*k'
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    csv.writer(f, delimiter='\t').writerow([
        'prop:ss-uniform-graph-mixed-contact', now,
        'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort',
        'computation or formal certificate',
        f"PASS: author replaced the formerly tautological final expression check with actual symbolic substitutions in the source section at O and after elliptic translation. Root read the added code and verified coefficients h*k+F and T+v*k, then k=F/h. Final author-preserving rerun {out['elapsed_seconds']}s; initial root run and author initial program/output remain retained. The independently proved geometry is unchanged."])
print(json.dumps({'status': out['status'], 'elapsed_seconds': out['elapsed_seconds'],
                  'actual_audit_time': now}, indent=2))
