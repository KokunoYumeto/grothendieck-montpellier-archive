from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work')
OWN = ROOT / 'agents/reduction_descent'
observations = {
    631: 'Actually viewed the complete image individually. B88 certificate ending and B89 opening fit the text block; B-RD89.1 through B-RD89.4, sums, valuations, citation and footer are legible, with no clipping, overlap or missing glyph.',
    632: 'Actually viewed the complete image individually. B89 continuation, scope and audit paragraphs are readable; the long retained-program path wraps within the margin. B90 heading, W/U display and point-field definitions fit; the lemma continues normally onto page 633.',
    633: 'Actually viewed the complete image individually. Both B90 tables, stabilizer display, valuation columns and B-RD90.2 through B-RD90.5 are legible and contained in the margins. Superscripts, subscripts and tame-character notation show no glyph loss or overlap.',
    634: 'Actually viewed the complete image individually. The two break-case calculations, B-RD90.6 through B-RD90.10, proposition opening and field-intersection formula fit cleanly. Proof ending and next proposition are separated normally; no clipping or overprinting.',
    635: 'Actually viewed the complete image individually. Lower/upper-break tables and terminal-character table are fully readable, with equation tags separate from their data. The corrected Colmez Proposition 3.7, Theorem 3.10 and Proposition 3.13(ii) pointer is legible; theorem opening continues normally.',
    636: 'Actually viewed the complete image individually. Determinant-coset count table, exact average, nonintegral 1896/5 contradiction, scope and audit paragraphs all fit. B-RD90.14 and B-RD90.15 tags are clear; the long verifier path wraps without clipping. No overlap or missing glyph.',
    637: 'Actually viewed the complete image individually. Section C begins cleanly with propositions, corollary, two counterexample displays and citations; the page is fully legible with normal margins and footer. No clipping, overlap, missing glyph or broken section transition.'
}
record = {
    'status': 'PASS',
    'actual_utc': datetime.now(timezone.utc).isoformat(),
    'pdf_sha256': '406ade402449604644a2b030e0cc8a05508a0eb52ec119cddc8108009a6c562a',
    'pdf_pages': 714,
    'pages': list(observations),
    'scope': 'Actual visual inspection of each of seven complete PNG images individually via view_image; layout, displayed mathematics, tables, equation tags, citations, path wrapping, continuations, margins, glyphs and footer. No source edit or rebuild.',
    'page_observations': [
        {'page': page,
         'png': str(ROOT / f'outputs/qa32/page_{page:03d}.png'),
         'png_sha256': hashlib.sha256((ROOT / f'outputs/qa32/page_{page:03d}.png').read_bytes()).hexdigest(),
         'status': 'PASS',
         'observation': observation}
        for page, observation in observations.items()
    ],
    'defects': []
}
out = OWN / 'outputs/CP32_visual_QA.json'
assert not out.exists(), 'Preserve any existing QA record before replacing it.'
out.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({'record': str(out), 'actual_utc': record['actual_utc'], 'status': record['status'], 'pages': record['pages'], 'record_sha256': hashlib.sha256(out.read_bytes()).hexdigest()}))
