"""OCR working copies of two lawfully downloaded originals; no mathematical test."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import os
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
JOBS = [
    ("part_a567_nakamura1990_original", 205, 13),
    ("part_a567_ihara_nakamura1997_original", 125, 28),
]

started = time.perf_counter()
with tempfile.TemporaryDirectory(prefix="part_a567_ocr_") as tmp:
    folder = Path(tmp)
    pages = []
    for stem, first_printed, last_pdf in JOBS:
        sub = folder / stem
        sub.mkdir()
        subprocess.run(
            ["pdftoppm", "-f", "2", "-l", str(last_pdf), "-r", "170",
             "-gray", "-png", str(SOURCES / f"{stem}.pdf"), str(sub / "page")],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
        )
        for image in sorted(sub.glob("page-*.png")):
            pdf_page = int(image.stem.split("-")[-1])
            pages.append((stem, first_printed + pdf_page - 2, image))

    def read_page(item):
        stem, printed, image = item
        env = dict(os.environ)
        env["OMP_THREAD_LIMIT"] = "1"
        result = subprocess.run(
            ["tesseract", str(image), "stdout", "--psm", "3"],
            env=env, check=True, capture_output=True, text=True,
        )
        return stem, printed, result.stdout

    read = list(ThreadPoolExecutor(max_workers=4).map(read_page, pages))
    for stem, _, _ in JOBS:
        selected = sorted((p, text) for name, p, text in read if name == stem)
        out = "OCR WORKING TEXT; formula glyphs must be verified against the PDF.\n\n"
        out += "\n".join(f"===== PRINTED PAGE {p} =====\n{text}" for p, text in selected)
        (SOURCES / f"{stem}_ocr.txt").write_text(out)
        print(stem, "pages", len(selected), "OCR characters", len(out), flush=True)
print("Wall seconds", round(time.perf_counter() - started, 6), flush=True)
