from pathlib import Path
import fitz
base=Path(__file__).resolve().parents[1]
doc=fitz.open(base/"sources/Saito1992.pdf")
for page in [8,9,32,33,35,37,38,39]:
    dest=base/"output"/f"Saito1992_pdf{page+1}_printed{page+288}.png"
    doc[page].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(dest)
    print(dest)
