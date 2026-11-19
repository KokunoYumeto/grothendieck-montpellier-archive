"""OCR public scanned sources for navigation; images, not OCR, decide mathematics."""
from pathlib import Path
import sys, subprocess, json
import fitz
base=Path(__file__).resolve().parents[1]
external=base.parents[2]/'public_sources'/'agent45'
pdf=external/sys.argv[1]
doc=fitz.open(pdf)
pages=[int(x)-1 for x in sys.argv[2:]] or list(range(len(doc)))
chunks=[]
for p in pages:
    image=external/f'{pdf.stem}_{p+1:03}.png'
    doc[p].get_pixmap(matrix=fitz.Matrix(2,2)).save(image)
    result=subprocess.run(['tesseract',str(image),'stdout','-l','eng'],capture_output=True,text=True,check=True)
    chunks.append(f'\nPDF PAGE {p+1}\n'+result.stdout)
target=external/f'{pdf.stem}_ocr.txt'
target.write_text('\n'.join(chunks))
print(json.dumps({'source':str(pdf),'ocr':str(target),'pdf_pages':[p+1 for p in pages],'method':'tesseract eng at 144dpi; navigation only'}))
