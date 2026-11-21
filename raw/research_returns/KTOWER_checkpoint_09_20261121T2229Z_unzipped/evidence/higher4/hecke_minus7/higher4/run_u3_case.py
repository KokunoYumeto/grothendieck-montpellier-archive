"""Run the unchanged generic U3 producer followed by its independent verifier."""
from pathlib import Path
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
k, modulus = map(int, sys.argv[1:])
case = HERE / f'e{k+1}_m{modulus}'
case.mkdir(exist_ok=True)
start = time.monotonic()
commands = [
    [sys.executable, str(HERE / 'prepare_ring_model.py'),
     '--k', str(k), '--modulus', str(modulus)],
    [str(HERE / ('compute_ring_schur64_fast' if modulus < 2**63
                 else 'compute_ring_schur_gmp_fast')),
     str(case / 'model.txt'), str(case / 'schur.json')],
    [sys.executable, str(HERE / 'verify_ring_schur.py'), str(case)],
]
for stage, command in enumerate(commands, 1):
    print(json.dumps({'stage': stage, 'case': case.name, 'state': 'starting'}), flush=True)
    with (case / f'stage{stage}.log').open('w') as log:
        subprocess.run(command, cwd=HERE, stdout=log, stderr=subprocess.STDOUT, check=True)
    print(json.dumps({'stage': stage, 'case': case.name, 'state': 'complete',
                      'elapsed_seconds': time.monotonic()-start}), flush=True)
report = json.loads((case / 'verify_ring_schur.json').read_text())
print(json.dumps({key: report[key] for key in (
    'status', 'modulus', 'k', 'dimension', 'det_schur_operator',
    'gcd_norm_determinant_modulus', 'elapsed_seconds')}), flush=True)
