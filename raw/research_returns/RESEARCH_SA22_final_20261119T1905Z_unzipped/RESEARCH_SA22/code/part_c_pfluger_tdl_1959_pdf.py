"""Read the public PDF actually embedded in the new TDL26669 record.

The full journal file is kept outside the deliverable project. Only original
metadata and selected inspection images are stored within the audit project.
"""
import datetime
import hashlib
import json
import pathlib
import time
import urllib.error
import urllib.request
import fitz

root = pathlib.Path(__file__).resolve().parents[1]
private = root.parent / 'source_reading'; private.mkdir(exist_ok=True)
metadata = json.loads((root / 'code/part_c_pfluger_tdl_1959_record_output.json').read_text())
url = next(x['attrs']['data'] for x in metadata['result']['advertised_elements']
           if x.get('tag') == 'object' and x.get('attrs', {}).get('type') == 'application/pdf')
started = datetime.datetime.now(datetime.timezone.utc).isoformat(); tick = time.monotonic()
record = {'url': url, 'method': 'GET', 'provenance': 'Actual public object.data in the opened TDL26669 record'}
destination = private / 'part_c_tdl_jims_1959.pdf'
try:
    with urllib.request.urlopen(url, timeout=40) as response:
        body = response.read()
        record.update(status=response.status, final_url=response.url,
                      content_type=response.headers.get('Content-Type'), bytes=len(body),
                      sha256=hashlib.sha256(body).hexdigest())
    if not body.startswith(b'%PDF-'): raise ValueError('Response is not a PDF; no PDF reading claimed')
    destination.write_bytes(body); record['saved_path'] = str(destination)
    document = fitz.open(destination); record['pdf_pages'] = len(document)
    text = '\n'.join('---PDF PAGE ' + str(i + 1) + '---\n' + p.get_text() for i, p in enumerate(document))
    text_path = destination.with_suffix('.txt'); text_path.write_text(text)
    record['embedded_text_characters'] = len(text); record['text_path'] = str(text_path)
    selection = sorted(set(range(min(8, len(document)))) | set(range(max(0, len(document)-4), len(document))))
    rendered = []
    for i in selection:
        image_path = root / 'qa' / ('part_c_tdl_jims_1959_pdf_' + str(i + 1).zfill(3) + '.png')
        document[i].get_pixmap(matrix=fitz.Matrix(1.4, 1.4)).save(image_path)
        rendered.append({'pdf_page': i + 1, 'image_path': str(image_path), 'embedded_text': document[i].get_text()[:5000]})
    record['rendered_pages'] = rendered
except Exception as error:
    record['error'] = type(error).__name__ + ': ' + str(error)
    if isinstance(error, urllib.error.HTTPError): record['status'] = error.code
payload = {'started_utc': started, 'elapsed_seconds': time.monotonic() - tick, 'requests': 1, 'result': record}
output = root / 'code/part_c_pfluger_tdl_1959_pdf_output.json'
output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
output.with_suffix('.txt').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(payload, ensure_ascii=False, indent=2))
