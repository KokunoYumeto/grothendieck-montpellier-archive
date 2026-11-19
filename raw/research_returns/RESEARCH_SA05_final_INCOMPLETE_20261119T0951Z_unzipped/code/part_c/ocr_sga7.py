"""Render/OCR a bounded original SGA7-I page range for theorem-number audit."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess
import json
import time

root=Path(__file__).resolve().parents[2]
source=root/'part_c/sources/SGA7I_original.pdf'
out=root/'part_c/sources/sga7_scan'
out.mkdir(exist_ok=True)
pages=list(range(328,357))
def inspect(page):
    stem=out/f'pdf_{page:03d}'
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-scale-to','1800','-png','-singlefile',str(source),str(stem)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    subprocess.run(['tesseract',str(stem)+'.png',str(stem),'--psm','3'],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    text=stem.with_suffix('.txt').read_text()
    return {'pdf_page':page,'printed_page':page-5,'text_chars':len(text),'locator_lines':[line for line in text.splitlines() if any(s in line for s in ['2.1.8','2.2.5','2.2.9','2.4.','3.5.','3.6.','3.6,'])]}
start=time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as pool: records=list(pool.map(inspect,pages))
combined='\n\n'.join(f'=== PDF PAGE {p}; PRINTED PAGE {p-5} ===\n'+(out/f'pdf_{p:03d}.txt').read_text() for p in pages)
(out/'bounded_ocr.txt').write_text(combined)
result={'source':str(source.relative_to(root)),'pages':records,'runtime_seconds':time.perf_counter()-start,'scope':'OCR locators only; selected page images separately viewed for formula verification.'}
(root/'code/part_c/ocr_sga7_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
