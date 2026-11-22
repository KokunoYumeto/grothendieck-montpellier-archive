from pathlib import Path
import hashlib
import json
import time
import fitz

root = Path(__file__).resolve().parents[1]
source = root / 'notes/geometry_Fredholm1956.pdf'
out = root / 'notes/geometry_fredholm1956_inputs'
out.mkdir(exist_ok=True)
start = time.perf_counter()
doc = fitz.open(source)
records = []
for printed in (327, 328, 348):
    index = printed - 318
    page = doc[index]
    text_path = out / f'p{printed}.txt'
    image_path = out / f'p{printed}.png'
    text_path.write_text(page.get_text(), encoding='utf-8')
    page.get_pixmap(matrix=fitz.Matrix(1800 / page.rect.width, 1800 / page.rect.width)).save(image_path)
    records.append({'printed_page': printed, 'physical_pdf_page': index + 1,
                    'text_path': str(text_path.relative_to(root)),
                    'image_path': str(image_path.relative_to(root))})
result = {'source': str(source.relative_to(root)),
          'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
          'page_count': len(doc), 'pages': records,
          'elapsed_seconds': time.perf_counter() - start,
          'preflight': 'PDF has 67 pages; modern Numdam cover is physical page1; printed319 is physical page2. Initial rg used nonexistent geometry_Fredholm1956.txt and exited2; rg --files identified geometry_Fredholm1956_full.txt. No source was changed.'}
log = root / 'logs/geometry_fredholm1956_input_check.json'
log.write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
