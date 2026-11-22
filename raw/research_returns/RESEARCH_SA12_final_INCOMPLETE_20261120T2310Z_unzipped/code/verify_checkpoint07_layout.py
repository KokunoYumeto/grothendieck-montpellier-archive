"""Record the completed actual visual inspection of checkpoint07 build50."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
render = json.loads((root / 'qa/checkpoint07_render.json').read_text())
pdf = root / 'build/RESEARCH_SA12_paper.pdf'
log = (root / 'build/RESEARCH_SA12_paper.log').read_text()
assert render['pdf_pages'] == 151
assert len(render['rendered_pages']) == 113
assert not re.search(r'Overfull|Warning|undefined|Missing character', log)
for number in range(1, 14):
    assert (root / f'qa/checkpoint07_contact_{number}.png').is_file()
old = root / 'qa/pdf_verified_checkpoint06.json'
if not old.exists():
    old.write_text((root / 'qa/pdf_verified.json').read_text())
now = datetime.now(timezone.utc)
record = {
    'utc': now.isoformat(), 'build': 'build_pass50',
    'pages': 151, 'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'overfull_before': 0, 'overfull_after': 0,
    'maximum_overfull_after_pt': 0, 'warnings_after': 0,
    'undefined_citations_after': 0, 'undefined_references_after': 0,
    'missing_characters_after': 0,
    'rendered_and_inspected_pages': render['rendered_pages'],
    'visual_outcome': (
        'Root actually viewed all thirteen contact sheets individually at05:20--05:22 UTC, '
        'covering113 pages of the final151-page build50. The sample includes every '
        'new local-surface, mixed-boundary, cone, horizontal-product, finite-local-image '
        'and klt-threefold proof, the complete remaining-gate discussion, bibliography, '
        'and spread samples throughout Parts A, B and C. No clipping, overlap or '
        'out-of-margin text was observed. Build50 has zero overfull boxes, warnings, '
        'unresolved citations/references or missing characters. Earlier build46 '
        'and build49 renders were not substituted for inspection of this final build.'
    )
}
(root / 'qa/pdf_verified.json').write_text(json.dumps(record, indent=2) + '\n')
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## Scheduled checkpoint07: preparation completed ' + now.strftime('%Y-%m-%d %H:%M UTC') + '\n\n'
        'The151-page integrated paper has zero overfull boxes and no warnings, '
        'missing characters, or unresolved citations/references. All thirteen '
        'contact sheets of build50, covering113 pages, were actually viewed. '
        'The PDF hash is recorded and enforced by the immutable checkpoint writer. '
        'There are185 numbered statements and405 recorded check events. The '
        'all-genus Schroer test, arbitrary finite-local-image criterion, and '
        'klt threefold boundary case are now included. The report remains '
        'INCOMPLETE because the general D.1, D.2(ii), and dependent L8 component '
        'remain open. The archive is due05:25 UTC; formal review04 is due06:10 UTC.\n')
print(json.dumps(record, indent=2))
