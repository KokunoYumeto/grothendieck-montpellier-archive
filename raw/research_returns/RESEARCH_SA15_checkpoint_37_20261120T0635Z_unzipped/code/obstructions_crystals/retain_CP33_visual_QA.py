"""Record completed actual image inspection; no rendering or paper mutation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
expected = '029cc723c44c6d3feda3b23bf8803504c8f11309350b4adb57a1b670338d28d2'
assert sha(root / 'RESEARCH_SA15_paper.pdf') == expected
pages = [411, 412, 413, 414, 415]
observations = {
    411: 'Actually viewed individually. Section 2.130, DE-LP1 through DE-LP7, coefficient/Frobenius notation, lemma heading and first proof paragraph are legible. Tags and margins are clear; no overlap, clipped display or missing glyph observed.',
    412: 'Actually viewed individually. Derivation continuation, DE-LP8 through DE-LP10, scalar-elimination display and irreducibility theorem/proof fit within margins. The end-of-proof box and page break are clean.',
    413: 'Actually viewed individually. Geometric main-component corollary and scope remark are legible, with resolved numbered references and intact displayed ranks. The following unnumbered main-orbit heading has its introductory paragraph on the same page; no clipping or overlap.',
    414: 'Actually viewed individually. Main-orbit lemma, degree formula, pole-normalization equation and generic-rank display are all clear. The scope remark remains within the text block; mathematical superscripts and proof-end glyph are intact.',
    415: 'Actually viewed individually. The following geometric-generic section begins cleanly; theorem headings, specialization proof, linked source citation and the two-case rank formula render correctly. Bottom continuation is intentional and unclipped.',
}
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'PASS',
    'actual_utc': now,
    'reviewer': '/root/obstructions_crystals',
    'pdf_sha256': expected,
    'pdf_pages': 731,
    'pages': pages,
    'inspection_method': 'All five final PNGs actually opened and displayed through view_image, in bounded batches of two and three; text extraction was not substituted for visual review.',
    'observations': [
        {'page': p, 'image': f'outputs/qa33/page_{p:03d}.png',
         'image_sha256': sha(root / f'outputs/qa33/page_{p:03d}.png'),
         'observation': observations[p]}
        for p in pages
    ],
    'defects': [],
    'scope': 'Visual layout, displayed mathematics, glyphs, references and page breaks on exactly the assigned final pages. No claim to have freshly inspected unassigned pages, and no source or PDF change made.',
}
rp = own / 'CP33_visual_QA.json'
with rp.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    f.write('\t'.join([now, 'CP33-actual-image-QA-OC', 'actual_visual_QA',
                       'RESEARCH_SA15_paper.pdf', 'Actually viewed final pages 411,412,413,414,415',
                       'PASS; no observed visual defect', str(rp.relative_to(root))]) + '\n')
print(json.dumps({'status': record['status'], 'actual_utc': now,
                  'pages': pages, 'record': str(rp.relative_to(root)), 'pdf_sha256': expected}))
