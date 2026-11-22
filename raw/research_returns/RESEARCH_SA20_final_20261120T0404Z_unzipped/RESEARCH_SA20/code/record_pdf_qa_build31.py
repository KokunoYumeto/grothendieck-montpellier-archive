#!/usr/bin/env python3
"""Record the completed root visual inspection of corrected build31d."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root=Path(__file__).resolve().parents[1]
p=root/'logs/pdf_qa.json'
record=json.loads(p.read_text())
assert record['after']['build']=='build_root_31d final pass'
assert record['pages']==345 and len(record['rendered_pages'])==71
for key in ['over_2pt','missing_glyphs','undefined_refs','bib_warnings']:
    assert record['after'][key]==0,key
pdf=root/'RESEARCH_SA20_paper.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==record['pdf_sha256']
for name,digest in record['source_sha256'].items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
record['visual_review']='passed'
record['reviewed_utc']=datetime.now(timezone.utc).isoformat()
record['reviewer']='GPT-6 Astra (OpenAI, ChatGPT Pro mode), root'
record['pdf_bytes']=pdf.stat().st_size
record['visually_inspected_contact_sheets']=[f'qa/sheet_{i:02d}.png' for i in range(1,7)]
record['full_resolution_pages_explicitly_viewed']=[77,82,138,139,301]
record['visual_findings']=(
    'Root explicitly viewed all six current contact sheets, covering all71 rendered pages, '
    'and additionally viewed full-resolution pages77,82,138,139,301. The A139 sphere '
    'stabilization proof, A140 realization and coefficient conventions, A141 supported '
    'loop and collar construction, A5.016 finite height and surface argument, and A5.017 '
    'finite-format certificate are legible with no clipping or overlap. The long checker '
    'filename now breaks within the margins on page138; the certificate formula is '
    'split into short aligned lines on page139. The1.1506pt overflow on page301 is '
    'visually harmless and within the required2pt limit. Updated gates and all '
    'bibliography pages were inspected. No further source correction is required.')
p.write_text(json.dumps(record,indent=2)+'\n')
(root/'logs/render_qa_build31.json').write_text(json.dumps(record,indent=2)+'\n')
readme=root/'README.md'
readme.write_text(readme.read_text().replace('325-page PDF','345-page PDF'))
print(json.dumps({k:record[k] for k in ['pages','pdf_bytes','pdf_sha256','visual_review','reviewed_utc','before','after']},indent=2))
