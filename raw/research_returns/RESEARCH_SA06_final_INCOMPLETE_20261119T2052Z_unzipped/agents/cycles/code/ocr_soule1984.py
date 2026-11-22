"""Create a navigational OCR; decisive equations are checked on page images."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import os
import subprocess
import time

base = Path(__file__).resolve().parents[1]
out = base / "output" / "Soule1984_pages"
out.mkdir(exist_ok=True)
start = time.perf_counter()
subprocess.run(["pdftoppm", "-f", "2", "-scale-to", "1800", "-png",
                str(base / "sources" / "Soule1984.pdf"), str(out / "page")], check=True)
pages = sorted(out.glob("page-*.png"))
def process(path):
    env = os.environ.copy()
    env["OMP_THREAD_LIMIT"] = "1"
    proc = subprocess.run(["tesseract", str(path), "stdout", "--psm", "3"],
                          capture_output=True, text=True, check=True,
                          timeout=45, env=env)
    return f"\n\n===== PDF PAGE {path.stem.split('-')[-1]} =====\n\n" + proc.stdout
with ThreadPoolExecutor(max_workers=4) as pool:
    text = "".join(pool.map(process, pages))
(base / "sources" / "Soule1984_ocr.txt").write_text(text)
record = {"pages": len(pages), "characters": len(text),
          "runtime_seconds": time.perf_counter() - start,
          "scope": "Navigational OCR, not a substitute for visual formula verification"}
(base / "output" / "ocr_soule1984.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
