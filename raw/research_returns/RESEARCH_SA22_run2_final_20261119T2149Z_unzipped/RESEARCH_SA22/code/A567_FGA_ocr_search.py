"""Targeted OCR search of the opened FGA scan; not a full proof audit."""
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time

import fitz

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "literature/A567_FGA.pdf"
START = time.perf_counter()


def page_text(i):
    doc = fitz.open(PDF)
    page = doc[i]
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), colorspace=fitz.csGRAY)
    with tempfile.TemporaryDirectory(prefix="a567_fga_") as tmp:
        image = Path(tmp) / "page.png"
        pix.save(image)
        env = os.environ.copy()
        env["OMP_THREAD_LIMIT"] = "1"
        result = subprocess.run(
            ["tesseract", str(image), "stdout", "-l", "eng", "--psm", "3"],
            capture_output=True, text=True, env=env, check=True,
        )
    doc.close()
    return i, result.stdout


def main():
    with fitz.open(PDF) as doc:
        n = len(doc)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        rows = sorted(pool.map(page_text, range(n)))
    out = ROOT / "literature/A567_FGA_ocr.txt"
    out.write_text("\n\n".join(f"[PDF PAGE {i + 1}]\n{text}" for i, text in rows))
    matches = []
    for i, text in rows:
        for line in text.splitlines():
            if any(stem in line.casefold() for stem in ("morcel", "morceaux")):
                matches.append({"pdf_page": i + 1, "line": line})
    report = {
        "source_url": "https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/FGA.pdf",
        "pdf_sha256": hashlib.sha256(PDF.read_bytes()).hexdigest(),
        "pages_ocr_processed": n,
        "ocr_engine": "tesseract, eng, psm3, 144dpi; imperfect French OCR",
        "scope": "Term search only; no claim of complete reading or term absence beyond OCR output",
        "terms": ["morcel", "morceaux"],
        "matches": matches,
        "elapsed_seconds": time.perf_counter() - START,
    }
    (ROOT / "logs/A567_FGA_ocr_search.json").write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
