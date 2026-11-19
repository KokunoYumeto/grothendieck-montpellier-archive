"""Render the source pages whose mathematical displays were lost by OCR."""
from pathlib import Path
import hashlib
import json
import fitz

root = Path(__file__).resolve().parent
source = root/'sources'/'Serre1970LocalFactors.pdf'
document = fitz.open(source)
records = []
for page_index, printed_page in ((1, '19-01'), (2, '19-02'),
                                 (7, '19-07'), (8, '19-08')):
    target = root/'sources'/f'Serre1970LocalFactors_page_{printed_page}.png'
    document[page_index].get_pixmap(matrix=fitz.Matrix(1.6, 1.6)).save(target)
    data = target.read_bytes()
    records.append({'source':str(source),'pdf_page':page_index+1,
                    'printed_page':printed_page,'image':str(target),
                    'sha256':hashlib.sha256(data).hexdigest()})
text = json.dumps(records, indent=2)
(root/'render_c6_primary_pages_output.json').write_text(text+'\n')
print(text)
