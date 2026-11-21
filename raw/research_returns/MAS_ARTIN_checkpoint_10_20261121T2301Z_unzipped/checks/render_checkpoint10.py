"""Render every new module page and its neighbors for actual visual QA."""
from pathlib import Path
import hashlib
import json
import re
import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "MAS_ARTIN.pdf"
OUT = ROOT.parent / "private_sources" / "qa" / "cp10final"
OUT.mkdir(parents=True, exist_ok=True)
doc = fitz.open(PDF)
texts = [page.get_text() for page in doc]
new_pages = []
for i, text in enumerate(texts):
    mo = [int(x) for x in re.findall(r"MA-MO\.(\d+)", text)]
    if any(550 <= number <= 999 for number in mo) or re.search(r"MA-(GA|PI)\.", text):
        new_pages.append(i + 1)
assert new_pages, "Expected new source/operator modules were not located"
pages = set(range(1, min(10, len(doc)) + 1))
pages.update(range(max(1, len(doc) - 8), len(doc) + 1))
for number in new_pages:
    pages.update(range(max(1, number - 1), min(len(doc), number + 2) + 1))
for i, text in enumerate(texts):
    if "Unproved assertions and remaining research gates" in text:
        pages.update(range(max(1, i), min(len(doc), i + 5) + 1))
pages = sorted(pages)
for j in range(0, len(pages), 4):
    group = pages[j:j + 4]
    sheet = Image.new("RGB", (1200, 1750), "white")
    draw = ImageDraw.Draw(sheet)
    for k, number in enumerate(group):
        pix = doc[number - 1].get_pixmap(matrix=fitz.Matrix(1.2, 1.2), alpha=False)
        im = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        im.thumbnail((585, 835))
        x = (k % 2) * 600 + (600 - im.width) // 2
        y = (k // 2) * 875 + 25
        sheet.paste(im, (x, y))
        draw.text(((k % 2) * 600 + 15, (k // 2) * 875 + 5), f"Page {number}", fill="black")
    sheet.save(OUT / f"sheet_{j // 4 + 1:02d}.png")
report = {
    "pdf_sha256": hashlib.sha256(PDF.read_bytes()).hexdigest(),
    "pdf_pages": len(doc), "new_module_pages": new_pages,
    "rendered_pages": pages, "sheets": (len(pages) + 3) // 4,
    "scope": "Rendering only. A subsequent actual image inspection is required before a visual pass."
}
(OUT / "render_report.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
