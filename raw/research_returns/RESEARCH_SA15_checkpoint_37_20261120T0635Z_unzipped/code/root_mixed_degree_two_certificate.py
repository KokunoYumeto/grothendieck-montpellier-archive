"""Author-preserving rerun after full reading of the independent reconstruction."""
from pathlib import Path
from contextlib import redirect_stdout
import datetime, hashlib, io, json
w = Path(__file__).resolve().parents[1]
program = w/'agents/monodromy/code/verify_mixed_degree_two_group.py'
author = w/'agents/monodromy/outputs/verify_mixed_degree_two_group.json'
dest = w/'outputs/root_verify_mixed_degree_two_group.json'
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
             {'__name__':'__main__', '__file__':str(program)})
finally:
    Path.write_text = old_write
    (w/'outputs/root_verify_mixed_degree_two_group.stdout.txt').write_text(capture.getvalue())
assert before == author.read_bytes()
out = json.loads(dest.read_text())
assert out['status'] == 'PASS'
summary = {'status':'PASS', 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'runtime_seconds':out['runtime_seconds'], 'author_sha256_preserved':hashlib.sha256(before).hexdigest(),
           'scope':'Two exact coefficient points. Geometric monodromy requires the separate full proof.'}
(w/'outputs/root_mixed_degree_two_certificate_summary.json').write_text(json.dumps(summary, indent=2)+'\n')
print(json.dumps(summary, indent=2))
