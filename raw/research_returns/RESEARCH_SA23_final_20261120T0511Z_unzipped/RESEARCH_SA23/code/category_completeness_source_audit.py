"""Preserve primary-source page identification for the final scope audit.

This is a locator/rendering aid, not a mathematical proof or a keyword-based
negative bibliographical inference.  The associated audit note records the
theorem architecture actually read.
"""
from pathlib import Path
import hashlib
import fitz

root = Path(__file__).resolve().parents[1]
pdf_path = root / "notes/geometry_Fredholm1956.pdf"
text_path = root / "notes/geometry_Fredholm1956_full.txt"
pdf = fitz.open(pdf_path)
print("source:", "https://www.numdam.org/article/BSMF_1956__84__319_0.pdf")
print("pdf_pages:", len(pdf))
print("pdf_sha256:", hashlib.sha256(pdf_path.read_bytes()).hexdigest())
print("text_sha256:", hashlib.sha256(text_path.read_bytes()).hexdigest())
for printed in (331, 348, 350, 359, 383):
    index = printed - 318
    page = pdf[index]
    image_path = root / f"notes/category_fredholm1956_p{printed}.png"
    page.get_pixmap(matrix=fitz.Matrix(1.7, 1.7)).save(image_path)
    print(f"printed_page={printed}; PDF_page_1_based={index+1}; image={image_path.name}")
print("Theorem architecture read: I.3 pp330–331; II.2–5 pp346–369; III.1–3 pp369–383.")
print("Negative conclusion comes from those statements and proofs, not string counts.")
