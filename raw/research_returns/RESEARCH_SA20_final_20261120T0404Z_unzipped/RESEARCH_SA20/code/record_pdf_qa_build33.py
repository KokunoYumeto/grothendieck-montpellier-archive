#!/usr/bin/env python3
"""Record the root's completed explicit visual review of build33c."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
path = root / 'logs/pdf_qa.json'
record = json.loads(path.read_text())
assert record['after']['build'] == 'build_root_33c final pass'
assert record['pages'] == 424 and len(record['rendered_pages']) == 84
for key in ['over_2pt', 'missing_glyphs', 'undefined_refs', 'bib_warnings']:
    assert record['after'][key] == 0, key
assert record['after']['overfull_boxes'] == 1
assert record['after']['max_overflow_pt'] == 1.1506
pdf = root / 'RESEARCH_SA20_paper.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest() == record['pdf_sha256']
for name, digest in record['source_sha256'].items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == digest, name
record['visual_review'] = 'passed'
record['reviewed_utc'] = datetime.now(timezone.utc).isoformat()
record['reviewer'] = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode), root'
record['visually_inspected_contact_sheets'] = [
    f'qa/build33/sheet_{i:02d}.png' for i in range(1, 8)
]
record['full_resolution_pages_explicitly_viewed'] = [
    142, 144, 145, 147, 216, 217, 218, 219, 378, 417
]
record['visual_findings'] = (
    'We explicitly viewed all seven fresh build33c contact sheets, covering '
    'all 84 rendered pages, and the ten listed pages at full resolution. '
    'All 59 changed body pages identified against build32g are included, '
    'together with new proof ranges 142–147 and 216–219, current gates and '
    'bibliography 399–424, front matter, the remaining overflow page, and '
    'a representative spread. We found no clipping, overlap, missing '
    'glyphs, or separated new theorem headings. The projective germ '
    'extension, horn construction, split-kernel sequence, polynomial '
    'sign equivalence, rotation relation, and finite verification record '
    'are legible. The corrected Kwieciński author name on page 417 has '
    'proper spacing. The remaining 1.1506pt overflow on page 378 is '
    'visually harmless and below the required 2pt limit. This review '
    'concerns build33c only: truncated output and earlier build33b views '
    'were not substituted for fresh inspection.'
)
path.write_text(json.dumps(record, indent=2) + '\n')
(root / 'logs/render_qa_build33.json').write_text(json.dumps(record, indent=2) + '\n')
readme = root / 'README.md'
readme.write_text(readme.read_text().replace('415-page PDF', '424-page PDF'))
print(json.dumps({key: record[key] for key in [
    'pages', 'pdf_bytes', 'pdf_sha256', 'visual_review', 'reviewed_utc',
    'before', 'after'
]}, indent=2))
