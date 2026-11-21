"""Create the ninth immutable snapshot at the user-prescribed interval.

The wait runs in a background execution session, in at-most-30-second
increments. No checkpoint is written before its due time. This script
does not perform the separate hourly mathematical progress review.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import subprocess
import sys
import time

base = Path(__file__).resolve().parent
due = datetime.fromisoformat('2026-11-21T22:15:46+00:00')
output = base.parent / 'KTOWER_checkpoint_09.zip'
while True:
    remaining = (due - datetime.now(timezone.utc)).total_seconds()
    if remaining <= 0:
        break
    time.sleep(min(30, remaining))
assert not output.exists(), 'Never overwrite an earlier checkpoint'
subprocess.run([sys.executable, str(base/'merge_checks.py')], cwd=base, check=True)
result = subprocess.run(
    [sys.executable, str(base/'make_package.py'), str(output),
     '--not-before', '2026-11-21T22:15:46Z'],
    cwd=base, check=True, text=True, capture_output=True)
receipt = json.loads(result.stdout)
(base.parent/'KTOWER_checkpoint_09_creation.json').write_text(
    json.dumps(receipt, indent=2)+'\n')
print(json.dumps(receipt), flush=True)
