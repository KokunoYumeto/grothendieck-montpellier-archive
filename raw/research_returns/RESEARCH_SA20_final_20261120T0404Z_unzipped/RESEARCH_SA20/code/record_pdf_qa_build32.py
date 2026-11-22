#!/usr/bin/env python3
"""Record the root's completed explicit visual review of build32g."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
path = root / 'logs/pdf_qa.json'
record = json.loads(path.read_text())
assert record['after']['build'] == 'build_root_32g final pass'
assert record['pages'] == 415 and len(record['rendered_pages']) == 117
for key in ['over_2pt', 'missing_glyphs', 'undefined_refs', 'bib_warnings']:
    assert record['after'][key] == 0, key
pdf = root / 'RESEARCH_SA20_paper.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest() == record['pdf_sha256']
for name, digest in record['source_sha256'].items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
record['visual_review'] = 'passed'
record['reviewed_utc'] = datetime.now(timezone.utc).isoformat()
record['reviewer'] = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode), root'
record['visually_inspected_contact_sheets'] = [
    f'qa/build32/sheet_{i:02d}.png' for i in range(1, 11)
]
record['full_resolution_pages_explicitly_viewed'] = [
    96, 108, 126, 130, 134, 140, 142, 206, 370
]
record['visual_findings'] = (
    'We explicitly viewed all ten fresh build32g contact sheets, covering all '
    '117 rendered pages, and the nine listed pages at full resolution. '
    'The complete new proof ranges83–142 and201–211, current gates and '
    'bibliography391–415, front matter, remaining overflow page, and a '
    'representative spread are legible with no clipping or overlap. '
    'The A147 heading and A5.19.2 formula now fit within the margins. '
    'The A152,A155,A156,A161 headings remain with their theorem statements. '
    'The A151 estimates, A157 join diagram, A158 norming formulas, A159 '
    'finite bounds, A160 exact-boundary construction, and A161 Moore '
    'presentation were inspected at full resolution. The remaining '
    '1.1506pt overflow on page370 is visually harmless and below the '
    'required2pt limit. This review concerns build32g only; earlier '
    'build32f views were not substituted for fresh inspection.'
)
path.write_text(json.dumps(record, indent=2) + '\n')
(root / 'logs/render_qa_build32.json').write_text(json.dumps(record, indent=2) + '\n')
readme = root / 'README.md'
readme.write_text(readme.read_text().replace('345-page PDF', '415-page PDF'))
print(json.dumps({key: record[key] for key in [
    'pages', 'pdf_bytes', 'pdf_sha256', 'visual_review', 'reviewed_utc',
    'before', 'after'
]}, indent=2))
