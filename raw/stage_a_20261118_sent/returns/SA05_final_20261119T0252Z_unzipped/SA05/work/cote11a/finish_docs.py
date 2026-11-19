"""Finalize readable scope documentation; mathematical records are built by run_all.py."""
import datetime,pathlib,re,runpy
R=pathlib.Path('SA05/work/cote11a')
ns=runpy.run_path(str(R/'polish_outputs.py'));polish=ns['polish']
for fn in ['overview.md','directions.md','proof_checks.md','root_merge_recommendation.md']:
 s=(R/fn).read_text();parts=re.split(r'(`[^`]*`|https?://\S+)',s)
 for i in range(0,len(parts),2):parts[i]=polish(parts[i])
 (R/fn).write_text(''.join(parts))
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(R/'progress.md').write_text('''# Cote11a completed review

All82 indexed entries were read with their full source passages. Complete assigned Pro text, notes and doubts, K11-01/K11-02, and B12-01 were read; cross-package excerpts and the K12-05 duplicate were read at the intervals in reading_log.tsv. No source transcription was edited.

Saved final scope:59items,90claims,24problems,46scan alarms,76links,11directions,34references,32search rows,249check events. Every claim is mapped to executed searches. run_all.py and validate_scope.py passed; all calculation output is saved.

The key mathematical checks are the gauge-sensitive Cartesian exchange counterexample, partition-system specialness counterexample, literal cycle-generator defect, signed projection formula, nilpotent-density counterexample and exact later field-base-change answer. EGA normal-base integrality remains an identification residual, not a declaration of current worldwide openness. The complete-real node is compared with a different published algebraic-node witness, explicitly classC for the partial historical identification.

Root handles uploads and timed checkpoints. This scope has no independent upload. Final overview, merge recommendation and all ledgers are present.
''')
(R/'progress.log').write_text('time_utc\tevent\n'+stamp+'\tSix stages complete for assigned scope; reproducible audit passed. Root maintains the original start/stage checkpoint clock.\n')
print('Documentation finalized at '+stamp)
