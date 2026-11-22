"""Read-only rerun of the parent graph certificate, with isolated output.

Only the final output destination is redirected.  The original author
program and output bytes are checked to remain unchanged.
"""
from pathlib import Path
import hashlib
import json

agent = Path(__file__).resolve().parents[1]
work = agent.parents[1]
source = work / 'code/mixed_degree_three_partial_normalizations.py'
author = work / 'outputs/mixed_degree_three_partial_normalizations.json'
target = agent / 'outputs/independent_mixed_degree_three_partial_normalizations.json'
source_bytes = source.read_bytes()
author_bytes = author.read_bytes()
old = "(w/'outputs/mixed_degree_three_partial_normalizations.json')"
new = 'Path(' + repr(str(target)) + ')'
text = source_bytes.decode()
assert text.count(old) == 1
namespace = {'__file__': str(source), '__name__': '__main__'}
exec(compile(text.replace(old, new), str(source), 'exec'), namespace)
assert source.read_bytes() == source_bytes
assert author.read_bytes() == author_bytes
out = json.loads(target.read_text())
out['author_sha256_preserved'] = hashlib.sha256(author_bytes).hexdigest()
out['source_sha256_preserved'] = hashlib.sha256(source_bytes).hexdigest()
out['audit_scope'] = 'Complete original graph program read; output-only redirection; exact finite graph assertions only.'
target.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({'isolated_output': str(target), 'runtime_seconds': out['runtime_seconds'],
                  'author_sha256_preserved': out['author_sha256_preserved']}, indent=2))
