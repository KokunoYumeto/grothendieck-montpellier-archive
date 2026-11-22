"""Record root's actual build65 visual inspection before scheduled checkpoint09."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
render = json.loads((root / 'qa/checkpoint09_render.json').read_text())
pdf = root / 'build/RESEARCH_SA12_paper.pdf'
log = (root / 'build/RESEARCH_SA12_paper.log').read_text()
assert render['pdf_pages'] == 194
assert len(render['rendered_pages']) == 59
assert not re.search(r'Overfull|Warning|undefined|Missing character', log)
for number in range(1, 8):
    assert (root / f'qa/checkpoint09_contact_{number}.png').is_file()
assert (root / 'qa/pdf_verified_checkpoint08.json').is_file()
now = datetime.now(timezone.utc)
record = {
    'utc': now.isoformat(), 'build': 'build_pass65',
    'pages': 194, 'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'overfull_before': 0, 'overfull_after': 0,
    'maximum_overfull_after_pt': 0, 'warnings_after': 0,
    'undefined_citations_after': 0, 'undefined_references_after': 0,
    'missing_characters_before': 0, 'missing_characters_after': 0,
    'intermediate_build_errors': (
        'Builds59 and60 stopped on one raw underscore in the newly added '
        'C_StacksProjectiveBase bibliography note. The note was replaced '
        'by plain wording, the bibliography regenerated, and the complete '
        'build repeated to stable references. The failed logs are retained.'
    ),
    'rendered_and_inspected_pages': render['rendered_pages'],
    'visual_outcome': (
        'Root actually viewed all seven build65 contact sheets at '
        '06:42--06:43 UTC, covering59 pages of the194-page paper. '
        'The selection includes the complete post-checkpoint08 proof block '
        'on pages134--158, the rational-tail failed-inference example '
        'on pages162--163 with adjacent pages, the updated unresolved '
        'discussion and full bibliography on pages181--194, plus a fresh '
        'spread over Parts A, B, C and earlier D. No clipping, overlap, '
        'missing glyph, or text outside the margins was observed. '
        'Build65 has zero overfull boxes, warnings, undefined references '
        'or citations, and missing characters. Previous complete visual '
        'records remain preserved; this selection avoids needlessly '
        'duplicating every previously inspected old proof page.'
    )
}
(root / 'qa/pdf_verified.json').write_text(json.dumps(record, indent=2) + '\n')
entry = (
    '\n\n## Scheduled checkpoint09: verified preparation '
    + now.strftime('%Y-%m-%d %H:%M UTC') + '\n\n'
    'The final194-page build65 contains226 statements and580 assembled '
    'check events. Twenty post-checkpoint08 geometric statements and the '
    'fully checked rational-tail failed-inference example are included. '
    'The tail example is auxiliary and is not counted as main-gate movement. '
    'There are23 finite-certificate programs. Root actually inspected all '
    'seven contact sheets, covering59 pages, including every new proof, '
    'the updated unresolved discussion and bibliography, and a spread '
    'through the older parts. The final log has zero overfull boxes '
    '(zero before and after), warnings, missing characters, or unresolved '
    'citations/references. The intermediate bibliography underscore error '
    'was corrected, with failed logs retained. The final PDF hash is '
    'recorded and enforced by the immutable checkpoint writer. General '
    'D.1, general D.2(ii), and residual L8 remain open; the report remains '
    'INCOMPLETE. Checkpoint09 is due06:55 UTC, and formal review05 is '
    'due07:10 UTC. This preparation is not an extra checkpoint or review.\n'
)
for name in ['PROGRESS_LEDGER.md', 'report_supplement.md']:
    with (root / name).open('a') as f:
        f.write(entry)
print(json.dumps(record, indent=2))
