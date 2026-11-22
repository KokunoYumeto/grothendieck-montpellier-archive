"""At18:10UTC, review first and then create immutable checkpoint24."""
from datetime import datetime, timezone
from pathlib import Path
import json, subprocess, time
root = Path(__file__).resolve().parents[1]
due = datetime(2026, 11, 20, 18, 10, tzinfo=timezone.utc)
remaining = (due - datetime.now(timezone.utc)).total_seconds()
assert remaining <= 60
if remaining > 0:
    time.sleep(remaining)

subprocess.run(['python3', 'code/run_logged.py', 'formal_review16',
                'python3', 'code/formal_review16.py'], cwd=root, check=True)
review = json.loads((root / 'code/output/formal_review16.json').read_text())
assert review['latest_successful_checkpoint'] == 23
assert not review['stopping_condition_met'], 'Prepare the final package if the stopping condition is met.'
with (root / 'CHECKPOINT24_SCOPE.md').open('a') as f:
    f.write('\n\n## Formal review16 completed before creation\n\n'
            'Actual review: ' + review['actual_utc'] + '. Movement: '
            + str(review['movement']) + '. Consecutive no-movement reviews: '
            + str(review['consecutive_no_movement_reviews']) + '.\n\n')
    for reduction in review['strict_main_gate_reductions']:
        f.write(reduction + '\n\n')

for name, args in [
    ('assemble_checkpoint24', ['python3', 'code/assemble.py']),
    ('inventory_checkpoint24', ['python3', 'code/program_inventory.py']),
    ('checkpoint24_create', ['python3', 'code/checkpoint.py', '24'])
]:
    subprocess.run(['python3', 'code/run_logged.py', name] + args, cwd=root, check=True)
