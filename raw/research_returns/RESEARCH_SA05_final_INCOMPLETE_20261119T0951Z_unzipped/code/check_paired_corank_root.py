"""Independently rerun the exact paired arithmetic-corank certificate."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import time

root = Path(__file__).resolve().parents[1]
gp = root.parent / 'tool_builds/pari-2.19.1/Olinux-x86_64/gp-dyn'
source = root / 'part_b/code/paired_corank.gp'
started = time.monotonic()
proc = subprocess.run([str(gp), '-q', '-f', str(source)], cwd=root,
                      text=True, capture_output=True, timeout=55)
out = root / 'part_b/output/paired_corank_root.txt'
out.write_text(proc.stdout + '\nSTDERR:\n' + proc.stderr)
sentinel = 'PAIRED_CORANK_CERTIFICATE_COMPLETE' in proc.stdout
unexpected_stderr = [line for line in proc.stderr.splitlines() if line.strip()
    and not re.fullmatch(r'\s*\*\*\*\s+Warning: new stack size = 64000000 \(61\.035 Mbytes\)\.', line)]
result = {
    'recorded_at': datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
    'command': [str(gp), '-q', '-f', str(source)],
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'exit_code': proc.returncode, 'completion_sentinel': sentinel,
    'unexpected_stderr': unexpected_stderr,
    'symbolic_identity_passes': proc.stdout.count('PASS: exact rank and all symbolic cover-map identities.'),
    'seconds': round(time.monotonic() - started, 6),
    'output': str(out.relative_to(root)),
    'scope': 'Exact algebraic two-descent, Selmer cover basis, rational points and symbolic covering-map identities. Local closure ranks use the written formal-group proof; no numerical local logarithm, analytic rank or BSD assumption is used.',
}
result_path = root / 'code/check_paired_corank_root_output.json'
if result_path.exists():
    old = json.loads(result_path.read_text())
    old['run_note'] = 'Initial wrapper falsely treated the announced stack-size change as an error; all mathematical assertions and the completion sentinel already passed. The amended wrapper permits only that exact informational line.'
    with (root / 'code/check_paired_corank_root_history.jsonl').open('a') as stream:
        stream.write(json.dumps(old) + '\n')
result_path.write_text(
    json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
if proc.returncode or not sentinel or unexpected_stderr or result['symbolic_identity_passes'] != 3:
    raise SystemExit('The exact GP certificate did not pass.')
