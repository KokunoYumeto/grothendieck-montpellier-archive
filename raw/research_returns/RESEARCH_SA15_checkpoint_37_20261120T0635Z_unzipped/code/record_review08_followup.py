"""Add the completed actual review to the current report, once."""
from pathlib import Path
import json,subprocess,sys
w=Path(__file__).resolve().parents[1]
r=json.loads((w/'notes/progress_review_08.json').read_text())
p=w/'notes/checkpoint14_changes.md';marker='## Actual hourly review08'
assert marker not in p.read_text()
with p.open('a') as f:
 f.write(f'\n{marker}\n\nThe actual review occurred at {r["actual_utc"]}, against immutable review07. It counted the proved A.3 structural extensions, the completed degree-three and uniform-source A.4 reductions, and the elimination of every B.4 residual27 branch except antisymplectic C4. The no-movement streak is {r["no_movement_streak"]}; disposition: {r["disposition"]}. Candidate uniform collision and nonproduct polarization arguments were excluded. The next review is due13:50:40UTC; checkpoint14 is due13:20:40UTC.\n')
subprocess.run([sys.executable,str(w/'code/update_current14.py')],check=True,cwd=w)
print(json.dumps({'actual_review':r['actual_utc'],'no_movement_streak':r['no_movement_streak'],
                  'next_review':r['next_review_due_utc'],'disposition':r['disposition']},indent=2))
