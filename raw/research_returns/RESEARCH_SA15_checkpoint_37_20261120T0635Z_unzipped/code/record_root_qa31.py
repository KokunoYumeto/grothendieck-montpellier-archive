"""Record actual root inspection of the twelve CP31 PNGs, not a new proof check."""
from pathlib import Path
import datetime, hashlib, json
w = Path(__file__).resolve().parents[1]
dest = w / 'notes/qa31_root_actual_review.json'
assert not dest.exists()
observations = {
    1: 'Title, credit, abstract, and contents are legible; all contents rows and page numbers fit.',
    14: 'Section heading, statement status, root-cover displays, and proof continuation fit without overlap.',
    28: 'Cohomology displays, citations, theorem heading, and crystalline restriction arrows are legible and contained.',
    55: 'Dense prose, subheadings, and dimension expressions fit with regular spacing and a clean continuation.',
    85: 'Algorithm statement, Frobenius products, equation tag 43, and scope remark fit without clipping.',
    126: 'Normalization sequence, numerical displays, citations, and bottom corollary heading are legible.',
    174: 'Actual residual 0.41342pt overflow page inspected: formulas and prose remain visibly contained; no clipping or overlap.',
    374: 'Generic-kernel scope correction, source comparison, theta subsection heading, and delta bound display fit.',
    375: 'Theta intersection calculation, isotropic subgroup bound, and explicit scope limitation fit without overlap.',
    376: 'Frobenius-fibre interpolation formulas, three tags, and concluding obstruction remark fit and are legible.',
    699: 'Bibliographic entries and long Stacks URL wrap within the text block; page continuation is clean.',
    700: 'Final bibliography continuation and all entries fit; final page has no clipping or missing glyphs.'
}
pages = sorted(observations)
pdf = w / 'RESEARCH_SA15_paper.pdf'
pdfhash = hashlib.sha256(pdf.read_bytes()).hexdigest()
assert pdfhash == '307b136ec8a9dda4c99a89cfcc739236769b157265d101455efdb47aa00a6d9c'
r = {
    'checkpoint': 31,
    'reviewer': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
    'actual_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status': 'PASS: all twelve images individually opened and visually inspected',
    'pdf_sha256': pdfhash,
    'pages': pages,
    'observations': {str(p): observations[p] for p in pages},
    'png_sha256': {str(p): hashlib.sha256((w / f'outputs/qa31/page_{p:03d}.png').read_bytes()).hexdigest() for p in pages},
    'truncated_prior_attempt': 'An earlier three-image tool call returned only a context-truncation message. It received no inspection credit; pages 1, 14, and 28 were subsequently reopened individually and actually inspected.',
    'scope': 'Visual layout verification only. No mathematical proof-check claim is made by this record.'
}
dest.write_text(json.dumps(r, indent=2) + '\n')
print(json.dumps(r, indent=2))
