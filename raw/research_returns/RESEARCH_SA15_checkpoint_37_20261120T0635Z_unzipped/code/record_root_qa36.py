"""Record fifteen final CP36 images actually opened and visually inspected by root."""
from pathlib import Path
import datetime, hashlib, json
w = Path(__file__).resolve().parents[1]
out = w / 'notes/qa36_root_actual_review.json'
assert not out.exists()
observations = {
 1: 'Title, exact AI credit, explicit incomplete abstract, original-scan limitation and first contents page are fully visible and legible.',
 2: 'Dense contents continuation, wrapped two-line entry and aligned page numbers are clear; subsection numbers and titles remain separated.',
 3: 'Three-digit subsection numbers, titles and dotted leaders fit without clipping or overlap.',
 4: 'New A.4 titles point to432,437,440,443; long titles, page numbers and the Part B transition remain clear.',
 5: 'Dense Part B contents, multiline entry and page-number column are aligned and readable.',
 6: 'B96-B98 contents entries point to700,706,711; the Parts C-F and bibliography outline is clear.',
 7: 'First body cohomology definitions and Lemmas1.1-1.2 are legible with normal display and heading spacing.',
 14: 'Coherent counterexample proof continuation, program path, status paragraphs and the next heading fit without clipping.',
 28: 'Root-cover proof, direct sums, field construction, maps and citations remain legible within the text block.',
 55: 'Ordinary plane septic subsection2.12, rank15 formula and short subheadings have clear spacing and no collision.',
 85: 'A.5 residue conclusion, precise scope qualification, equations17-18, Frobenius conventions and citations are explicit and legible.',
 126: 'Boxed all-degree rank formula with dagger tag, isogeny matrix, kernel map and divisors are intact and legible.',
 175: 'The residual0.41342pt overflow paragraph concerning the integral inverse formula was freshly inspected; there is no visible clipping or margin collision.',
 792: 'Bibliography proof-opening scopes, dense Stacks entries and long DOI/URL text wrap within the margins.',
 793: 'Final bibliography continuation, proof-opening qualifications and page footer are fully visible with normal margins.'
}
pdfhash = hashlib.sha256((w / 'RESEARCH_SA15_paper.pdf').read_bytes()).hexdigest()
assert pdfhash == '8ee230dfe7b2f9c158426266a505adbfd9af67caee6782e6521ccce607b8aaf8'
r = {
 'checkpoint': 36,
 'status': 'PASS: all fifteen assigned final images actually opened and visually inspected',
 'reviewer': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'actual_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'pdf_sha256': pdfhash,
 'pages': sorted(observations),
 'observations': {str(p): v for p, v in observations.items()},
 'png_sha256': {str(p): hashlib.sha256((w / f'outputs/qa36/page_{p:03d}.png').read_bytes()).hexdigest() for p in observations},
 'scope': 'Actual layout QA only; no new mathematical proof audit. Every contents page, first body page, spread sample, residual overflow and final bibliography pages were actually viewed.',
 'truncated_image_calls': 1,
 'truncated_call_handling': 'The earlier paired85/126 call was truncated and was not credited; both were subsequently reopened completely and individually, as were175,792,793.'
}
out.write_text(json.dumps(r, indent=2) + '\n')
changes = w / 'notes/checkpoint36_changes.md'
with changes.open('a') as f:
 f.write('\n### Retained compilation and preflight failures\n\nThe first actual compilation failed because the undated Kleiman entry had an empty year, producing an invalid author-year bibliography item. The bibliography now records n.d. without inventing a date. Three overwide B96/B98 displays were split across lines in the consolidation formatter; canonical mathematical text was unchanged. The first preflight retry then stopped before a second TeX build because its register merge required the removed auxiliary file. The auxiliary file was restored with only the invalid Kleiman citation and forced-numerical marker removed. Both failed command streams, the actual failed build inputs/logs, every prior/diff and the successful second build are retained. The preflight failure is separate from the two actual compilation attempts.\n')
print(json.dumps({'status': r['status'], 'actual_utc': r['actual_utc'], 'pages': r['pages'], 'pdf_sha256': pdfhash}, indent=2))
