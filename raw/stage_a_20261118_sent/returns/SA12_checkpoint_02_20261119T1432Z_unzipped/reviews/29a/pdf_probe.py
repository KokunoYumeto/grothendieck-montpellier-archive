"""Render selected public reference pages and save OCR for locator searches.
OCR is only a locator aid; mathematical statements are read from rendered pages.
"""
from pathlib import Path
import subprocess,sys
pdf=Path(sys.argv[1]); prefix=sys.argv[2]; pages=[int(p) for p in sys.argv[3:]]
cache=Path(__file__).parent/'reference_cache'
for p in pages:
    out=cache/f'{prefix}_{p}'
    subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-singlefile','-scale-to','1700','-png',str(pdf),str(out)],check=True)
    subprocess.run(['tesseract',str(out)+'.png',str(out),'--psm','3'],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    txt=Path(str(out)+'.txt').read_text()
    print(f'PDF page {p}: '+repr(txt[:500]))
