#!/usr/bin/env python3
"""Record a completed human/model inspection; never infer approval from a render.

The caller must actually inspect the images first and supply the exact build run,
viewed full-resolution pages, and inspection statement. Previous approvals are
preserved independently of the mutable latest-build pointer.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, shutil

parser = argparse.ArgumentParser()
parser.add_argument('--run', required=True)
parser.add_argument('--full-pages', required=True)
parser.add_argument('--inspection', required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
pending = json.loads((root/'logs/paper_visual_qa_pending.json').read_text())
build = json.loads((root/'logs/integrated_build_summary.json').read_text())
pdf = root/'build/RESEARCH_SA22_paper.pdf'
digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
assert pending['run_id'] == build['run_id'] == args.run
assert pending['pdf_sha256'] == build['pdf_sha256'] == digest
assert not build['source_changed_during_build']
assert build['overfull_above_2pt'] == 0
assert not build['undefined_warnings'] and not build['missing_glyphs']
assert not build.get('rerun_warnings', [])
assert args.inspection.startswith('PASS:')
pages = [int(x) for x in args.full_pages.split(',')]
assert set(pages).issubset(pending['rendered_pages'])
archive = root/'logs/visual_qa_runs'
archive.mkdir(exist_ok=True)
latest = root/'logs/paper_visual_qa.json'
if latest.exists():
    prior = json.loads(latest.read_text())
    target = archive/(prior['run_id']+'.json')
    if not target.exists():
        shutil.copy2(latest, target)
    # A clarification for the same PDF must not erase its earlier approval.
    prior_digest = hashlib.sha256(latest.read_bytes()).hexdigest()[:16]
    immutable = archive/(prior['run_id']+'_approval_'+prior_digest+'.json')
    if not immutable.exists():
        shutil.copy2(latest, immutable)
inspected_at = datetime.now(timezone.utc).isoformat()
for supplemental in pending.get('supplementary_renderings', []):
    supplemental_pages = set(supplemental.get('rendered_pages', []))
    assert supplemental_pages.issubset(pages), (
        'Supplementary pages require explicit full-resolution inspection',
        sorted(supplemental_pages-set(pages)))
    supplemental['inspection_at_render_time'] = supplemental.get(
        'inspection_at_render_time', supplemental.get('inspection', ''))
    supplemental['inspection'] = (
        'PASS: every supplementary page was explicitly inspected at full resolution; '
        'see the enclosing actual-inspection statement and page list.')
    supplemental['inspected_utc'] = inspected_at
pending.update({
    'inspection': args.inspection,
    'inspected_by': 'GPT-6 Astra (OpenAI), inherited reasoning effort, run /root, ChatGPT Pro mode',
    'inspected_utc': inspected_at,
    'full_resolution_pages_viewed': pages,
})
encoded = json.dumps(pending, indent=2)+'\n'
latest.write_text(encoded)
(archive/(args.run+'.json')).write_text(encoded)
build['visual_qa'] = 'PASS: actual rendered-page inspection recorded in logs/paper_visual_qa.json'
(root/'logs/integrated_build_summary.json').write_text(json.dumps(build, indent=2)+'\n')
shutil.copy2(pdf, root/'RESEARCH_SA22_paper.pdf')
print(json.dumps({'run_id': args.run, 'pdf_pages':pending['pdf_pages'],
                  'pdf_sha256':digest, 'rendered_pages_viewed':len(pending['rendered_pages']),
                  'full_resolution_pages_viewed': pages, 'inspection':args.inspection}, indent=2))
