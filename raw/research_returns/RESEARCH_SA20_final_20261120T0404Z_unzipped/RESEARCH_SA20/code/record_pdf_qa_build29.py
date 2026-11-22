#!/usr/bin/env python3
"""Record the root's completed visual review of build29, without rebuilding."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
p = root/'logs/pdf_qa.json'
record = json.loads(p.read_text())
assert record['after']['build'] == 'build_root_29 final pass'
assert record['pages'] == 311
assert record['after']['over_2pt'] == 0
assert record['after']['missing_glyphs'] == 0
assert record['after']['undefined_refs'] == 0
assert record['after']['bib_warnings'] == 0
assert hashlib.sha256((root/'RESEARCH_SA20_paper.pdf').read_bytes()).hexdigest() == record['pdf_sha256']
for name, digest in record['source_sha256'].items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest() == digest, name
record['visual_review'] = 'passed'
record['reviewed_utc'] = datetime.now(timezone.utc).isoformat()
record['reviewer'] = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode), root'
record['visually_inspected_contact_sheets'] = [f'qa/sheet_{i:02d}.png' for i in range(1,7)]
record['full_resolution_pages_explicitly_viewed'] = [55,58,108,269]
record['visual_findings'] = ('All six current contact sheets explicitly viewed, covering every rendered page; '
    'full-resolution pages55,58,108,269 additionally viewed. New A132/A133/A134/A5.015 proofs, '
    'statement headings, diagrams, updated gates and new bibliography entries are legible with no clipping '
    'or overlap. The sole1.1506pt overflow on page269 is visually harmless and within the required2pt limit. '
    'The earlier heading-spacing repair remains effective. No further source edit or rebuild is needed.')
p.write_text(json.dumps(record,indent=2)+'\n')
(root/'logs/render_qa_build29.json').write_text(json.dumps(record,indent=2)+'\n')
readme = root/'README.md'
readme.write_text(readme.read_text().replace('296-page PDF','311-page PDF'))
print(json.dumps({k:record[k] for k in ['pages','pdf_sha256','visual_review','reviewed_utc','after']},indent=2))
