"""Perform the due21:10UTC review and create the scheduled immutable checkpoint."""
from pathlib import Path
from datetime import datetime, timezone
import time, subprocess

root = Path(__file__).resolve().parents[1]
due = datetime(2026, 11, 20, 21, 10, tzinfo=timezone.utc)
remaining = (due - datetime.now(timezone.utc)).total_seconds()
assert remaining <= 60
if remaining > 0:
    time.sleep(remaining)
for name, args in [
    ('formal_review19', ['python3', 'code/formal_review19.py']),
    ('assemble_checkpoint28', ['python3', 'code/assemble.py']),
    ('inventory_checkpoint28', ['python3', 'code/program_inventory.py']),
    ('checkpoint28_create', ['python3', 'code/checkpoint.py', '28'])
]:
    subprocess.run(['python3', 'code/run_logged.py', name] + args, cwd=root, check=True)
