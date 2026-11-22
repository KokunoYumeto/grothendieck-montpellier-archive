#!/usr/bin/env python3
"""Record the completed root visual inspection of the corrected build30c."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
p = root/'logs/pdf_qa.json'
record = json.loads(p.read_text())
assert record['after']['build'] == 'build_root_30c final pass'
assert record['pages'] == 325
for key in ['over_2pt','missing_glyphs','undefined_refs','bib_warnings']:
    assert record['after'][key] == 0, key
pdf = root/'RESEARCH_SA20_paper.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest() == record['pdf_sha256']
for name, digest in record['source_sha256'].items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest() == digest, name
record['visual_review'] = 'passed'
record['reviewed_utc'] = datetime.now(timezone.utc).isoformat()
record['reviewer'] = 'GPT-6 Astra (OpenAI, ChatGPT Pro mode), root'
record['pdf_bytes'] = pdf.stat().st_size
record['corrected_layout_pages'] = [67,68,282]
record['visually_inspected_contact_sheets'] = [f'qa/sheet_{i:02d}.png' for i in range(1,7)]
record['full_resolution_pages_explicitly_viewed'] = [68,69,72,282]
record['visual_findings'] = (
    'All six current contact sheets explicitly viewed, covering every rendered page. '
    'Full-resolution pages68,69,72,282 additionally viewed. The new A135--A138 proofs, '
    'relative obstruction sequences, stabilization square, metric formulas, updated gates '
    'and source-status bibliography are legible with no clipping or overlap. The corrected '
    'A136 component-group display is on page68; its preceding layout page67 was also rendered '
    'and viewed. The only remaining1.1506pt overflow on page282 is visually harmless and '
    'within the required2pt limit. No further source change or rebuild is needed.')
p.write_text(json.dumps(record, indent=2)+'\n')
(root/'logs/render_qa_build30.json').write_text(json.dumps(record, indent=2)+'\n')
readme = root/'README.md'
readme.write_text(readme.read_text().replace('311-page PDF','325-page PDF'))
print(json.dumps({k:record[k] for k in ['pages','pdf_bytes','pdf_sha256','visual_review','reviewed_utc','before','after']},indent=2))
