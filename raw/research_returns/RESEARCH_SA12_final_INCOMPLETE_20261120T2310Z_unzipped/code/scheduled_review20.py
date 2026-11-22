"""Run review20 at22:10UTC; start only during the preceding final minute."""
from pathlib import Path
from datetime import datetime, timezone
import json
import subprocess
import time

root = Path(__file__).resolve().parents[1]
due = datetime(2026, 11, 20, 22, 10, tzinfo=timezone.utc)
remaining = (due - datetime.now(timezone.utc)).total_seconds()
assert -2 <= remaining <= 60, 'Start in the final minute before22:10UTC.'
assert (root / 'code/output/review20_main_assessment.json').exists()
assert not (root / 'code/output/formal_review20.json').exists()
if remaining > 0:
    time.sleep(remaining)
subprocess.run(['python3', 'code/run_logged.py', 'formal_review20',
                'python3', 'code/formal_review20.py'], cwd=root, check=True)
subprocess.run(['python3', 'code/run_logged.py', 'assemble_after_review20',
                'python3', 'code/assemble.py'], cwd=root, check=True)
