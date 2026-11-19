"""Match E.2.29's literal matrix prescription to the retained exact artifact."""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import hashlib
import json

started = datetime.now(timezone.utc).isoformat()
clock = perf_counter()
base = Path(__file__).resolve().parents[2]
artifact = base / 'output/RESEARCH_SA07/code/build_A5_boundary_nilpotent.json'
data = json.loads(artifact.read_text())
assert data['boundary_basis_columns'] == list(range(43))
rows = list(range(30)) + [31,32,33,34,35,36,38,43,44,50,51,54,58]
assert data['boundary_basis_rows'] == rows
assert data['standard_seed'] == 1 and data['N_raw_divisor'] == 10
q = [(60 if j == 0 else 0) - data['E'][0][j] for j in range(61)]
assert q == data['proper_detector']
assert data['boundary_image'][0] == 324 and data['detected_value'] == 19440
print('PASS: E.2.29 first43 columns, all43 row indices, seed1, divisor10, first-row detector, Nb coordinate324 and qNb19440 match the retained JSON.')
print('Scope: literal correspondence of the paper prescription to the separately verified exact matrix artifact; no new profinite or Galois assertion.')
metadata = {
    'started_utc': started,
    'runtime_seconds': perf_counter() - clock,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'matrix_json_sha256': hashlib.sha256(artifact.read_bytes()).hexdigest(),
    'exit_code': 0,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(metadata, indent=2) + '\n')
print(json.dumps(metadata))
