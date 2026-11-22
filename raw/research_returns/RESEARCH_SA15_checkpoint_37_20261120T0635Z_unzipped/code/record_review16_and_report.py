"""Record the actual scheduled review, then report exactly its observed result."""
from pathlib import Path
import json,subprocess,sys
w=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(w/'code/record_review.py'),'16',str(w/'notes/review16_assessment.json')],cwd=w,check=True)
r=json.loads((w/'notes/progress_review_16.json').read_text())
assert r['no_movement_streak']==0 and r['movement']
text=('\n### Actual hourly review16\n\n'
      f"Actual review16 was recorded at {r['actual_utc']}, against review15 at {r['baseline_actual_utc']}. "
      'The fixed-degree monodromy additions and exact height-two inertia sectors strictly shrink the prior gates. '
      'The no-movement streak is zero; the disposition is Continue. '
      'A.3 and A.4 in general, the primitive mixed cup-product gate, higher-dimensional B.3 and remaining B.4 indices stay open. '
      'No candidate outside the frozen paper is counted as a completed theorem. '
      'The next checkpoint is due21:35:40UTC and the next actual hourly review is due21:50:40UTC.\n')
for rel in ['notes/checkpoint24_changes.md','RESEARCH_SA15_report.md']:
 with (w/rel).open('a') as f:f.write(text)
print(text)
