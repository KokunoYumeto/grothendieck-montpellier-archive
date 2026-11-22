"""OCR the opened Goodman--Pollack 1980 scan, retaining every rendered page.
AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 2026-11-19.
"""
from pathlib import Path
import subprocess, time, json, concurrent.futures
root=Path('/workspace/scratch/eccd14a17414/RESEARCH_SA11_work')
out=root/'audit/extension_GP1980_render'
out.mkdir(exist_ok=True)
start=time.monotonic()
subprocess.run(['pdftoppm','-r','180','-png',
                str(root/'sources/extension_Pollack5.pdf'),str(out/'page')],
               check=True,capture_output=True)
def ocr(path):
    subprocess.run(['tesseract',str(path),str(path.with_suffix('')),'--psm','3'],
                   check=True,capture_output=True)
    return path.with_suffix('.txt').read_text()
paths=sorted(out.glob('page-*.png'))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    texts=list(executor.map(ocr,paths))
(root/'sources/extension_GP1980_ocr.txt').write_text(
    '\n\n'.join('PDF PAGE '+str(i+1)+'\n'+text for i,text in enumerate(texts)))
result=dict(pages=len(paths),runtime_s=time.monotonic()-start,
            ocr='tesseract psm3 180dpi',source='published two-up scan, pages 220-235')
(root/'audit/extension_ocr_goodman_pollack_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
