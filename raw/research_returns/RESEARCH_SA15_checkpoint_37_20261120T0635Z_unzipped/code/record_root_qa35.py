"""Record the fourteen final CP35 images actually opened and visually inspected by root."""
from pathlib import Path
import datetime, hashlib, json
w = Path(__file__).resolve().parents[1]
out = w / 'notes/qa35_root_actual_review.json'
assert not out.exists()
observations = {
 1: 'Title, exact AI credit, explicit incomplete abstract, source limitation and first contents page are fully visible and legible.',
 2: 'Dense contents continuation, wrapped two-line entry and aligned page numbers are clear; subsection numbers and titles remain separated.',
 3: 'Three-digit subsection numbers, titles and dotted leaders fit without clipping or overlap.',
 4: 'New product determinant and wedge/module entries point to pages383,385,426,429; headings and the Part B contents continuation fit.',
 5: 'Dense Part B contents, multiline entry and page-number column are aligned and readable.',
 6: 'B94 and B95 entries point to675 and682; C-F contents and the first body-section transition have normal spacing.',
 14: 'Proof continuation, code path, status paragraphs, displayed maps and the next heading are legible and contained.',
 28: 'Dense complete-intersection proof, direct sums, finite-field construction, maps and source citations remain legible within the text block.',
 55: 'Contact-quartic argument, dimension displays, short subheadings and page continuation have clear spacing with no collision.',
 85: 'The A.5 scope and exact-algorithm qualification are explicit; equation tags, cohomological maps and section heading fit.',
 126: 'Boxed all-degree rank formula, dagger tag, matrix and normalization exact sequence are intact and legible.',
 175: 'The actual residual0.41342pt overflow paragraph concerning the integral inverse formula was freshly inspected; no visible clipping or margin collision occurs.',
 764: 'Bibliography entries, precise source-opening scopes and long DOI/URL text wrap within the margins.',
 765: 'Final bibliography continuation and page footer are fully visible with normal margins and no clipping.'
}
pdfhash = hashlib.sha256((w / 'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
assert pdfhash == 'd951489941df01521c8f1309fa88a77580a9cc0248672284f0bfaf9cc649d738'
r = {
 'checkpoint': 35,
 'status': 'PASS: all fourteen assigned final images actually opened and visually inspected',
 'reviewer': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'actual_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'pdf_sha256': pdfhash,
 'pages': sorted(observations),
 'observations': {str(p): v for p, v in observations.items()},
 'png_sha256': {str(p): hashlib.sha256((w / f'outputs/qa35/page_{p:03d}.png').read_bytes()).hexdigest() for p in observations},
 'scope': 'Actual layout QA only; no new mathematical proof audit. Every contents page, spread sample, residual overflow and final bibliography pages were freshly viewed.',
 'truncated_image_calls': 1,
 'truncated_call_handling': 'The initial four-image call was truncated and was not credited; all four images were subsequently reopened completely in pairs.'
}
out.write_text(json.dumps(r, indent=2) + '\n')
print(json.dumps({'status': r['status'], 'actual_utc': r['actual_utc'], 'pages': r['pages'], 'pdf_sha256': pdfhash}, indent=2))
