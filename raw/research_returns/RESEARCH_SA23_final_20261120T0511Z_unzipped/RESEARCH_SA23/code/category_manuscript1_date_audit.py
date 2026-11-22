"""Render assigned physical pages 73–110 for actual manuscript dating checks."""
from pathlib import Path
import hashlib
import fitz

root = Path(__file__).resolve().parents[1]
path = root / "sources/root_manuscript1_ranged.pdf"
doc = fitz.open(path)
print("source:", path)
print("sha256:", hashlib.sha256(path.read_bytes()).hexdigest())
print("physical_page_count:", len(doc))
for physical in range(73, 111):
    page = doc[physical-1]
    out = root / f"notes/category_mss1_physical_{physical:03d}.png"
    page.get_pixmap(matrix=fitz.Matrix(1.8, 1.8)).save(out)
    print(f"physical={physical}; width={page.rect.width}; height={page.rect.height}; output={out.name}")
print("Rendering alone does not count as an actual reading or dating witness.")
