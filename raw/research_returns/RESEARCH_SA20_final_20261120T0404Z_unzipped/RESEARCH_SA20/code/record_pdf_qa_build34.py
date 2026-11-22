#!/usr/bin/env python3
"""Record the root's actual complete visual review of build34b."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root=Path(__file__).resolve().parents[1]
path=root/'logs/pdf_qa.json'
record=json.loads(path.read_text())
assert record['after']['build']=='build_root_34b final pass'
assert record['pages']==430 and len(record['rendered_pages'])==116
assert len(record['all_changed_body_pages'])==91
for key in ['over_2pt','missing_glyphs','undefined_refs','bib_warnings']:
    assert record['after'][key]==0,key
assert record['after']['overfull_boxes']==1
assert record['after']['max_overflow_pt']==1.1506
pdf=root/'RESEARCH_SA20_paper.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()==record['pdf_sha256']
for name,digest in record['source_sha256'].items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
record['visual_review']='passed'
record['reviewed_utc']=datetime.now(timezone.utc).isoformat()
record['reviewer']='GPT-6 Astra (OpenAI, ChatGPT Pro mode), root'
record['visually_inspected_contact_sheets']=[f'qa/build34/sheet_{i:02d}.png' for i in range(1,11)]
record['full_resolution_pages_explicitly_viewed']=[147,148,149,150,151,152,383,411,425]
record['visual_findings']=(
    'We explicitly viewed all ten fresh build34b contact sheets, covering all116 rendered pages '
    'and all91 changed body pages relative to build33c. The new proof spans147–152; gates and '
    'bibliography404–430, the remaining overflow page383, front matter and a spread are included. '
    'We separately viewed the nine listed pages at full resolution. No clipping, overlap, missing '
    'glyphs or stranded new headings remain. Build34a had left the Bartels–Lück proof subheading '
    'at the foot of page151; a five-line Needspace command moved it with its paragraph to page152. '
    'This final review uses only freshly rendered build34b images. The relative normal-invariant '
    'argument, trace formulas, exact sequences, finite T4 record and source decorations are legible. '
    'The sole1.1506pt overflow on page383 is visually harmless and below the required2pt limit.'
)
path.write_text(json.dumps(record,indent=2)+'\n')
(root/'logs/render_qa_build34.json').write_text(json.dumps(record,indent=2)+'\n')
readme=root/'README.md'
readme.write_text(readme.read_text().replace('424-page PDF','430-page PDF'))
target=root/'agents/singularities_duality/part_aspherical_four_relative_comparison.tex'
layout={'utc':record['reviewed_utc'],'change':'Inserted Needspace{5 baselineskip} before the Bartels–Lück proof subheading; no mathematical text change.',
        'final_source_sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
(root/'logs/A163_layout_revision.json').write_text(json.dumps(layout,indent=2)+'\n')
print(json.dumps({k:record[k] for k in ['pages','pdf_bytes','pdf_sha256','visual_review','reviewed_utc','before','after']},indent=2))
