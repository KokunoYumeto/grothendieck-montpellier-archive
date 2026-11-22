"""Record the completed actual visual inspection of checkpoint 06 pages."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
render = json.loads((root / 'qa/checkpoint06_render.json').read_text())
pdf = root / 'build/RESEARCH_SA12_paper.pdf'
log = (root / 'build/RESEARCH_SA12_paper.log').read_text()
assert render['pdf_pages'] == 125
assert len(render['rendered_pages']) == 86
assert not re.search(r'Overfull|Warning|undefined|Missing character', log)
for number in range(1, 11):
    assert (root / f'qa/checkpoint06_contact_{number}.png').is_file()
old = root / 'qa/pdf_verified_checkpoint05.json'
if not old.exists():
    old.write_text((root / 'qa/pdf_verified.json').read_text())
now = datetime.now(timezone.utc)
record = {
    'utc': now.isoformat(), 'build': 'build_pass42',
    'pages': 125, 'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'overfull_before': 1, 'maximum_overfull_before_pt': 131.29002,
    'overfull_before_build': 'build_pass39',
    'overfull_after': 0, 'warnings_after': 0,
    'undefined_citations_after': 0, 'undefined_references_after': 0,
    'missing_characters_after': 0,
    'rendered_and_inspected_pages': render['rendered_pages'],
    'visual_outcome': (
        'Root actually viewed all ten contact sheets separately at04:34-04:36 UTC, '
        'covering86 pages of the final125-page build. The sample includes the '
        'complete quadratic-tower counterexample and its sharp consequences, '
        'the arbitrary-field Picard stabilization and auxiliary lemmas, '
        'the log-canonical and elliptic nonprojective-surface proofs, the '
        'remaining gates, and bibliography. The formerly overfull file path '
        'on page29 now wraps normally. No clipped, overlapping or out-of-margin '
        'text was observed. The earlier truncated image output was not counted '
        'as inspection. The final build log has zero overfull boxes, warnings, '
        'unresolved citations/references or missing characters.'
    )
}
(root / 'qa/pdf_verified.json').write_text(json.dumps(record, indent=2) + '\n')
ledger = root / 'PROGRESS_LEDGER.md'
ledger.write_text(ledger.read_text() + '\n\n## Scheduled checkpoint06: preparation completed '
    + now.strftime('%Y-%m-%d %H:%M UTC') + '\n\n'
    'The125-page integrated paper has zero overfull boxes and no warnings, '
    'missing characters, or unresolved citations/references. Build39 had one '
    'overfull file path of131.29002pt; the source was fixed and its final page '
    'was visually inspected. All ten contact sheets, covering86 spread pages '
    'including every newly added proof section, were actually viewed. The '
    'current PDF hash is recorded and enforced by the checkpoint writer. '
    'The report remains INCOMPLETE: only D.1, D.2(ii), and their dependent '
    'component of L8 remain requested open work. Every Part A, B and C row is '
    'decided. The archive is due04:40 UTC; formal review03 remains05:10 UTC.\n')
print(json.dumps(record, indent=2))
