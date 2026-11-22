from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path('/workspace/scratch/24868f40e6da/RESEARCH_SA15_work')
OWN = ROOT / 'agents/reduction_descent'
observations = {
    645: 'Actually viewed the entire PNG individually. B90 certificate and audit ending, B91 heading and first lemma fit normally. Long retained-code path wraps within the text block. B-RD91.1–3 and their tags are legible; no clipping, overlap, missing glyph or footer defect.',
    646: 'Actually viewed the entire PNG individually. B91 quotient cases, exact p3-to-p2 formula, equality-boundary paragraph and proof continuation are legible. B-RD91.4–6 and the piecewise display fit within margins; bold proved statuses wrap normally.',
    647: 'Actually viewed the entire PNG individually. Crossing rows, proof and large-parameter theorem are clear. B-RD91.7–10, matrix-entry characters and layer dimensions have readable subscripts and superscripts. The final proof line continues normally to the next page.',
    648: 'Actually viewed the entire PNG individually. Cyclotomic contradiction, B-RD91.11, remaining-scope remark, exact counts and audit runtimes are clear. The code path wraps without clipping, and all text stays above the footer. No overlap or missing mathematical glyph.',
    649: 'Actually viewed the entire PNG individually. B92 section and actual25 lemma open cleanly. Four-character break table, inverse valuations, both break-pair rows and coefficient table B-RD92.1–5 are entirely visible, including the bottom table rows; margins and footer remain clear.',
    650: 'Actually viewed the entire PNG individually. B92 point-field case elimination and parahoric lemma are readable. The full matrix-group display, two-crossing table, quotient matrix and four-character row B-RD92.6–9 fit with separated tags and no clipping.',
    651: 'Actually viewed the entire PNG individually. Parahoric proof continuation and common-high lemma are legible. B-RD92.10–12, both break formulas and the strict-case table fit inside the margins, including the table near the page bottom. No overlap or glyph loss.',
    652: 'Actually viewed the entire PNG individually. Common-high endpoint proof, the (15,95) exclusion theorem and both actual field-break displays72/336 are fully readable. B-RD92.13–14 and the remaining-scope opening fit normally; the scope continues cleanly onto653.',
    653: 'Actually viewed the entire PNG individually. B92 certificate and independent-audit paragraphs are legible, with the long verifier path wrapping within the margins. Section C begins cleanly with its proposition, citation and counterexample display. No clipped text, overlap, missing glyph or footer defect.'
}
record = {
    'status': 'PASS',
    'actual_utc': datetime.now(timezone.utc).isoformat(),
    'pdf_sha256': '029cc723c44c6d3feda3b23bf8803504c8f11309350b4adb57a1b670338d28d2',
    'pdf_pages': 731,
    'pages': list(observations),
    'scope': 'Actual individual viewing of all nine complete PNGs via view_image in three bounded batches. Inspected tables, equations and tags, proved statuses, prose, citations, path wrapping, page continuations, glyphs, margins and footers. No source edit or rebuild.',
    'page_observations': [
        {'page': p, 'png':str(ROOT / f'outputs/qa33/page_{p:03d}.png'),
         'png_sha256':hashlib.sha256((ROOT / f'outputs/qa33/page_{p:03d}.png').read_bytes()).hexdigest(),
         'status':'PASS', 'observation':obs}
        for p,obs in observations.items()
    ],
    'defects': []
}
out=OWN/'outputs/CP33_visual_QA.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')
with (OWN/'CHECK_EVENTS.tsv').open('a') as f:
    f.write('\t'.join([record['actual_utc'],'CP33-visual-QA','PASS','Actual full-image layout inspection of pages645–653','outputs/CP33_visual_QA.json','All nine individual images viewed; zero clipping, overlap, missing-glyph or table/tag defects; exact PNG/PDF hashes retained'])+'\n')
print(json.dumps({'record':str(out),'actual_utc':record['actual_utc'],'status':'PASS','pages':record['pages'],'record_sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
