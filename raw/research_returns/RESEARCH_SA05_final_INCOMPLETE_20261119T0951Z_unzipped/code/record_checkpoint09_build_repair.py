"""Record the observed checkpoint-09 integration failure and its repair."""
from datetime import datetime, timezone
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
report = root / 'RESEARCH_SA05_report.md'
heading = '### Checkpoint 09 build repair and visual check'
entry = '''
### Checkpoint 09 build repair and visual check

The first checkpoint-09 build stopped during the second LuaLaTeX pass because
two newly added bibliography annotations contained unescaped underscores in
program paths (the Taylor–Yoshida and Vial entries). The retained initial
failure is `code/checkpoint09_initial_build_failure.txt`. We wrapped those
literal paths in `\\path{...}`, reran BibTeX and then the full build. The
repair and its output are retained in `code/fix_checkpoint09_bibliography.py`,
its JSON output, and `code/checkpoint09_bibtex_repair_output.txt`. This was a
typesetting repair and did not change a mathematical statement. Duplicate
terminal periods in the new B.1 and C.4 status strings were also removed.

The initial failed build had zero overfull boxes; the final complete build
has zero overfull boxes and zero LaTeX/BibTeX warnings. All 45 pages listed in
`code/checkpoint_09_verification_output.json` were actually inspected in the
five rendered page panels, including the new B.1 and C.4 proofs and the final
bibliography pages. No clipping, overlapping text, or unreadable layout was
found. The final PDF has 180 pages. This layout check does not certify a new
mathematical result and does not count as movement at a formal review.
'''
text = report.read_text()
assert heading not in text
report.write_text(text + entry)
result = {'recorded_utc': datetime.now(timezone.utc).isoformat(),
          'initial_overfull_boxes': 0, 'final_overfull_boxes': 0,
          'final_latex_bibtex_warnings': 0, 'pages_actually_inspected': 45,
          'scope': 'Observed build repair and visual inspection only.'}
(root / 'code/checkpoint09_build_repair_output.json').write_text(
    json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
