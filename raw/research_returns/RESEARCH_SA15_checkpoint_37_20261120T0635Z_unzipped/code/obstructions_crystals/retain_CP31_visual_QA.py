"""Retain actual nine-page CP31 image observations after all images were viewed."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
pdf = root / 'RESEARCH_SA15_paper.pdf'
expected = '307b136ec8a9dda4c99a89cfcc739236769b157265d101455efdb47aa00a6d9c'
assert hashlib.sha256(pdf.read_bytes()).hexdigest() == expected
pages = list(range(387, 396))
observations = {
    '387': 'Principal translated-theta proof and symmetric level-three lemma are legible. Citation links, long statement and final lift comparison fit; no clipping or overlap.',
    '388': 'TCM2 through TCM5 display the complete cross pairing and theta identities with intact tags and superscripts. Theorem 2.446 begins cleanly and continues normally onto page389.',
    '389': 'Fixed-point proof continuation and odd-cover corollaries are clear. TCM6, rank calculation and the symmetric descent paragraph remain within margins.',
    '390': 'Scope/provenance and section2.123 heading fit. Lemma2.450 and DE-CI1 through DE-CI3 have clear indices and target twists; lower-page display is fully visible.',
    '391': 'Translation continuation, Proposition2.451 and three numbered conclusions have clean spacing. DE-CI4/5 and the fixed linear J display are legible with no overlap.',
    '392': 'DE-CI6 and actual coherent Frobenius paragraph are intact. Birational-kernel corollary and explicit scope remark render correctly; next subsection heading has introductory text below it.',
    '393': 'Squared-frame stable-image proof and KWI1 through KWI5 are clear. Summation limits and Frobenius superscripts render correctly; the three hypotheses of Proposition2.455 fit.',
    '394': 'Conditional wall statement, inertia group and KWI6 through KWI9 are complete. Quotient and annihilator notation is readable. The remaining-gates remark fits without clipping.',
    '395': 'Local-wall scope/provenance continues cleanly. The following section2.125, its introductory status and Lemma2.457 display readable math and citations; equation104 and lower-page continuation are intact.',
}
images = {str(p): hashlib.sha256((root / f'outputs/qa31/page_{p:03d}.png').read_bytes()).hexdigest() for p in pages}
now = datetime.now(timezone.utc).isoformat()
record = {
    'status': 'PASS', 'actual_utc': now, 'pdf_sha256': expected, 'pdf_pages': 700,
    'pages': pages,
    'method': 'Each of the nine final PNGs was individually opened using view_image and actually inspected. This record was written only after all nine image outputs were observed.',
    'scope': 'Visual layout only: final TCM/common-incidence/local-wall pages and immediate continuation; text, math, citations, tags, margins, glyphs and page breaks. No source or PDF edits.',
    'observations': observations, 'image_sha256': images, 'defects': [],
}
out = own / 'CP31_visual_QA.json'
with out.open('x') as f:
    json.dump(record, f, indent=2)
    f.write('\n')
with (own / 'CHECK_EVENTS.tsv').open('a') as f:
    f.write('\t'.join([now, 'CP31_actual_visual_QA', 'actual_final_PNG_inspection',
                       'outputs/qa31/page_387.png through page_395.png',
                       'All nine images actually viewed; exact final PDF hash verified',
                       'PASS; no layout defect observed', str(out.relative_to(root))]) + '\n')
print(json.dumps({'status': 'PASS', 'actual_utc': now, 'pages': pages, 'record': str(out.relative_to(root)), 'pdf_sha256': expected}))
