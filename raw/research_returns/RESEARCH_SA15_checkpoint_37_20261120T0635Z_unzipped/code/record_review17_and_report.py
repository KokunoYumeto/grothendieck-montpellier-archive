"""Record actual review17 only when due, using the current promoted proof gates."""
from pathlib import Path
import json,subprocess,sys
w=Path(__file__).resolve().parents[1]
for rel in ['agents/reduction_descent/B_one_slope_quotient.tex',
            'agents/reduction_descent/B_next_tame_boundary.tex',
            'agents/monodromy/nonordinary_good_theta_norm_transfer.tex']:
    assert '\\status{Candidate' not in (w/rel).read_text(),rel
subprocess.run([sys.executable,str(w/'code/update_current26.py')],cwd=w,check=True)
subprocess.run([sys.executable,str(w/'code/record_review.py'),'17',str(w/'notes/review17_assessment.json')],cwd=w,check=True)
r=json.loads((w/'notes/progress_review_17.json').read_text())
assert r['no_movement_streak']==0 and r['movement']
text=('\n### Actual hourly review17\n\n'
      f"Actual review17 was recorded at {r['actual_utc']}, against review16 at {r['baseline_actual_utc']}. "
      'The every-fixed f0 three/five monodromy family and the exact height-two tame sectors strictly shrink the previous gates. '
      'The no-movement streak is zero and the disposition is Continue. '
      'The theta counterexample, equivalent boundary reformulations, finite candidate probes and packaging were not counted as qualifying movement. '
      'GeneralA.3/A.4, primitive mixed ranks, higher-dimensionalB.3 and remainingB.4 indices remain open. '
      'The next actual hourly review is due22:50:40UTC; checkpoint26 is due22:20:40UTC and checkpoint27 is due23:05:40UTC.\n')
for rel in ['notes/checkpoint26_changes.md','RESEARCH_SA15_report.md']:
    with (w/rel).open('a') as f:f.write(text)
print(text)
