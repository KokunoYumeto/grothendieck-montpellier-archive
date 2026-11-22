from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parents[3]
own = Path(__file__).resolve().parents[1]
expected = '78c3b71c63eca5f3df36dbcd08672db03f7c682114fec9e641df1eb808bc71e9'
digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
assert digest(root / 'RESEARCH_SA15_paper.pdf') == expected
observations = {
    723: 'B99 heading, field assumptions, proved lemma and displays B-RD99.1--5 are legible. The complete bottom display and footer are visible, with no clipping or overlap.',
    724: 'The dense first-coefficient proof, B-RD99.6--9 and the separate right-hand tag placement are clear. Page continuation and all subscripts/superscripts are readable.',
    725: 'The Herbrand and field-intersection displays B-RD99.10--12, the Colmez citation paragraph and the new cyclotomic lemma fit. The reported small citation overflow causes no visible clipping, overlap or missing glyph.',
    726: 'Cyclotomic different formulas B-RD99.13--16, theorem statement and lower page continuation are clear. The long B-RD99.16 comparison is fully visible; a supplementary PDF bounding-box read confirms its first text x=86.75pt inside the approximately 76.54pt text margin.',
    727: 'B99 terminal inequality, precise scope and audit/provenance paragraphs are readable. B100 subsection and lemma begin with clean spacing and continue normally to the next page.',
    728: 'B100 arc inequalities and integral recursion are clear. Wrapped B-RD100.4 has two distinct aligned lines, a separate unobstructed tag and no collision; B-RD100.5 is fully visible above the footer.',
    729: 'Eisenstein orders and semilinear descent formulas B-RD100.6--8, the proof ending and the ambiguity theorem B-RD100.9 are legible. Tags on their own right-hand lines do not overlap prose.',
    730: 'The two exact sequences, character trace difference, mixed-threshold corollary and exact-index theorem are clear. B-RD100.10--14 and the lower-bound proof fit without clipping or missing characters.',
    731: 'B100 upper-bound recurrence B-RD100.15, proof end, complete scope/certificate and independent-audit paragraphs are legible. The code path is wrapped inside the body and the final paragraph clears the footer.',
    732: 'The transition to Section C, subsection heading, propositions/corollary and formulas are clean. The page is fully visible with normal margins and no missing citation or mathematical glyph.',
}
page_records = []
for page, observation in observations.items():
    image = root / f'outputs/qa37/page_{page:03d}.png'
    page_records.append(dict(page=page, png=str(image), png_sha256=digest(image),
                             status='PASS', observation=observation))
record = dict(status='PASS', actual_utc=datetime.now(timezone.utc).isoformat(),
              pdf_sha256=expected, pdf_pages=810, pages=list(observations),
              scope='Every complete individual PNG723--732 was actually opened via view_image, '
                    'at most two images per call, and visually inspected. Mathematical layout, '
                    'tags, proved statuses, citations, source paths, glyphs, page continuations '
                    'and margins were checked. No PDF or canonical input was edited.',
              page_observations=page_records, defects=[])
destination = own / 'outputs/CP37_visual_QA.json'
assert not destination.exists()
destination.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(dict(status='PASS', actual_utc=record['actual_utc'],
                     pages=record['pages'], pdf_sha256=expected,
                     record=str(destination), record_sha256=digest(destination)), indent=2))
