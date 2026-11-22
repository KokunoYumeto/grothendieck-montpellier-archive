"""Record actual final build57 visual inspection for scheduled checkpoint08."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
render = json.loads((root / 'qa/checkpoint08_render.json').read_text())
pdf = root / 'build/RESEARCH_SA12_paper.pdf'
log = (root / 'build/RESEARCH_SA12_paper.log').read_text()
assert render['pdf_pages'] == 175
assert len(render['rendered_pages']) == 129
assert not re.search(r'Overfull|Warning|undefined|Missing character', log)
for number in range(1, 16):
    assert (root / f'qa/checkpoint08_contact_{number}.png').is_file()
assert (root / 'qa/pdf_verified_checkpoint08_build54.json').is_file()
now = datetime.now(timezone.utc)
record = {
    'utc': now.isoformat(), 'build': 'build_pass57',
    'pages': 175, 'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'overfull_before': 0, 'overfull_after': 0,
    'maximum_overfull_after_pt': 0, 'warnings_after': 0,
    'undefined_citations_after': 0, 'undefined_references_after': 0,
    'missing_characters_before': 1, 'missing_characters_after': 0,
    'rendered_and_inspected_pages': render['rendered_pages'],
    'visual_outcome': (
        'Root actually viewed all fifteen final build57 contact sheets at '
        '06:06--06:07 UTC, covering129 pages of the175-page paper. This includes '
        'every page106--175, all post-checkpoint07 proof additions, the three '
        'generic-fibre statements and proofs on pages132--135, the updated '
        'remaining-gate section and full bibliography, plus spread samples '
        'from Parts A, B and C and earlier D. No clipping, overlap or text '
        'outside the margins was observed. Build57 has zero overfull boxes, '
        'warnings, undefined citations/references and missing characters. '
        'This final inspection supersedes the provisional173-page build54 '
        'inspection, whose record is retained separately.'
    )
}
(root / 'qa/pdf_verified.json').write_text(json.dumps(record, indent=2) + '\n')
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## Scheduled checkpoint08: final preparation ' + now.strftime('%Y-%m-%d %H:%M UTC') + '\n\n'
        'The final175-page build57 includes all205 statements and494 assembled '
        'check events, including the three fully audited generic-fibre results. '
        'It supersedes the provisional173-page preparation above. The final '
        'log has zero overfull boxes, warnings, missing characters and unresolved '
        'citations/references. Root actually inspected all fifteen final contact '
        'sheets, covering129 pages, at06:06--06:07 UTC. The final PDF hash is '
        'recorded for enforcement by the immutable checkpoint writer. '
        'The report remains INCOMPLETE because general D.1, D.2(ii), and the '
        'dependent residual L8 remain open. There are21 finite-certificate '
        'programs; formal review04 and checkpoint08 remain scheduled for06:10 UTC.\n')
print(json.dumps(record, indent=2))
