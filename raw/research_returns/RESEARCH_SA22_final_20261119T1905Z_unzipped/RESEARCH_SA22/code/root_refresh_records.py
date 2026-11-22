"""Refresh required delivery records in dependency order, retaining measured run data."""
from pathlib import Path
from datetime import datetime, timezone
import json, subprocess, sys, time

R = Path(__file__).resolve().parents[1]
number = int(sys.argv[1])
target = R / 'code' / f'root_refresh_records_{number:02d}_output.json'
if target.exists():
    raise RuntimeError('Refresh records are immutable; choose a new sequence number')
started = time.perf_counter()
out = {'started_utc': datetime.now(timezone.utc).isoformat(),
       'scope': 'Necessary statement/event/bibliography assembly, consistency audit and report generation; no mathematical certificate rerun.',
       'results': []}
for script in ['assemble_records.py', 'audit_records.py', 'root_reconcile_report.py']:
    before = time.perf_counter()
    process = subprocess.run([sys.executable, str(R/'code'/script)], cwd=R, text=True, capture_output=True)
    item = {'script': 'code/'+script, 'seconds': time.perf_counter()-before,
            'exit_code': process.returncode, 'stdout': process.stdout, 'stderr': process.stderr}
    out['results'].append(item)
    if process.returncode:
        break
out['seconds'] = time.perf_counter()-started
out['completed'] = len(out['results']) == 3 and all(x['exit_code'] == 0 for x in out['results'])
target.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
sys.exit(0 if out['completed'] else 1)
