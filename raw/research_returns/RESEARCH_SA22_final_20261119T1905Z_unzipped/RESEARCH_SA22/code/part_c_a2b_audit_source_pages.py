"""Render already saved original Solynin passages for a renewed source audit.

No network request and no finite/numerical mathematical check is performed.
Printed page3 is PDF page1 in the saved original Russian article.
"""
import datetime
import json
import pathlib
import time
import fitz

root = pathlib.Path(__file__).resolve().parents[1]
start = datetime.datetime.now(datetime.timezone.utc).isoformat(); tick = time.monotonic()
source = root / 'sources/a2b_Solynin1999.pdf'; document = fitz.open(source)
rows = []
for printed in (9, 21, 23, 28, 32, 33):
    index = printed - 3
    destination = root / 'qa' / ('part_c_a2b_audit_solynin_' + str(printed).zfill(2) + '.png')
    document[index].get_pixmap(matrix=fitz.Matrix(1.8, 1.8)).save(destination)
    rows.append({'printed_page': printed, 'pdf_page': index + 1,
                 'image_path': str(destination), 'embedded_text': document[index].get_text()})
payload = {'started_utc': start, 'elapsed_seconds': time.monotonic() - tick,
           'source': str(source), 'source_pdf_pages': len(document),
           'network_requests': 0, 'mathematical_finite_checks': 0, 'rendered_pages': rows}
output = root / 'code/part_c_a2b_audit_source_pages_output.json'
output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
output.with_suffix('.txt').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'started_utc': start, 'elapsed_seconds': payload['elapsed_seconds'],
                  'source_pdf_pages': len(document), 'rendered_printed_pages': [r['printed_page'] for r in rows]}, indent=2))
