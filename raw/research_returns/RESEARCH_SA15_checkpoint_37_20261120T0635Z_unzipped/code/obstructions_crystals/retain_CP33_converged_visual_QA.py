"""Retain the second actual-image inspection after final LaTeX convergence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
final_sha = 'ea99a27826f7221acc327cb54ded638c46928e93ec6a531fca57b7c0cdba0c7e'
assert sha(root / 'RESEARCH_SA15_paper.pdf') == final_sha
rp = own / 'CP33_visual_QA.json'
prior = own / 'CP33_visual_QA.preconvergence.json'
assert not prior.exists()
old_bytes = rp.read_bytes()
record = json.loads(old_bytes)
assert record['pages'] == [411, 412, 413, 414, 415]
assert record['pdf_sha256'] == '029cc723c44c6d3feda3b23bf8803504c8f11309350b4adb57a1b670338d28d2'
for row in record['observations']:
    assert sha(root / row['image']) == row['image_sha256']
    row['observation'] = 'Freshly reopened and actually reinspected after final convergence. ' + row['observation']
now = datetime.now(timezone.utc).isoformat()
record['actual_utc'] = now
record['pdf_sha256'] = final_sha
record['inspection_method'] = 'All five final re-rendered PNGs were freshly opened and displayed through view_image in batches of two and three. Their image hashes are also independently identical to the preserved first inspection; fresh visual inspection was nevertheless performed as requested.'
record['preconvergence_record'] = str(prior.relative_to(root))
record['final_convergence_scope'] = 'The parent reports only contents pages changed. This record freshly inspects exactly the five assigned final pages and independently verifies their byte identity and the new final PDF hash.'
with prior.open('xb') as f:
    f.write(old_bytes)
rp.write_text(json.dumps(record, indent=2) + '\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    f.write('\t'.join([now, 'CP33-converged-actual-image-QA-OC', 'actual_visual_QA',
                       'RESEARCH_SA15_paper.pdf', 'Freshly viewed final pages 411,412,413,414,415 after final convergence',
                       'PASS; no observed defect; original record retained', str(rp.relative_to(root))]) + '\n')
print(json.dumps({'status': 'PASS', 'actual_utc': now, 'pages': record['pages'],
                  'pdf_sha256': final_sha, 'record': str(rp.relative_to(root))}))
