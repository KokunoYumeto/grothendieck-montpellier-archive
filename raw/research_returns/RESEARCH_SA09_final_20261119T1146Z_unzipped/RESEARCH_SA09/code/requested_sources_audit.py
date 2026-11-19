#!/usr/bin/env python3
"""Fetch lawful publisher/distributor previews and audit local PDF locators.

We do not request subscription chapter PDFs or attempt authentication.  A
preview is retained as a preview, never treated as a copy of the full book.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import subprocess
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
TASKS = [
    ("https://api.pageplace.de/preview/DT0400.9780511892271_A23680352/preview-9780511892271_A23680352.pdf", "happel_1988_lawful_preview.pdf"),
    ("https://assets.cambridge.org/97805213/39223/index/9780521339223_index.pdf", "happel_1988_publisher_index.pdf"),
    ("https://link.springer.com/content/pdf/bfm:978-1-4613-0041-0/1", "lang_algebra_2002_publisher_frontmatter.pdf"),
    ("https://page-one.springer.com/pdf/preview/10.1007/978-1-4613-0041-0_6", "lang_algebra_2002_ch6_publisher_preview.pdf"),
]


def fetch(task):
    url, name = task
    dest = ROOT / "sources" / name
    start = time.perf_counter()
    result = {"url": url, "file": str(dest.relative_to(ROOT))}
    try:
        if dest.exists():
            result["status"] = "reused"
        else:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 scholarly-source-audit"})
            with urllib.request.urlopen(req, timeout=30) as response:
                data = response.read()
                result["http_status"] = response.status
                result["resolved_url"] = response.url
            if not data.startswith(b"%PDF"):
                raise ValueError("Response is not a PDF; not retained as a source")
            dest.write_bytes(data)
            result["status"] = "downloaded"
        result["bytes"] = dest.stat().st_size
        result["sha256"] = hashlib.sha256(dest.read_bytes()).hexdigest()
        text_path = ROOT / "logs" / (dest.stem + ".txt")
        subprocess.run(["pdftotext", "-layout", str(dest), str(text_path)], check=True, capture_output=True)
        result["text_file"] = str(text_path.relative_to(ROOT))
        pages = text_path.read_text(errors="replace").split("\f")
        if pages and not pages[-1].strip():
            pages.pop()
        result["pdf_pages"] = len(pages)
        result["last_page_first_lines"] = pages[-1].strip().splitlines()[:8]
    except Exception as exc:
        result["status"] = "failed"
        result["error"] = str(exc)
    result["seconds"] = round(time.perf_counter() - start, 3)
    return result


def dold_audit():
    source = ROOT / "sources" / "dold_puppe_1961.pdf"
    temp = ROOT / "logs" / "dold_puppe_1961_locator_text.txt"
    subprocess.run(["pdftotext", "-layout", str(source), str(temp)], check=True)
    pages = temp.read_text(errors="replace").split("\f")
    locators = {}
    # Printed p.201 follows the Numdam cover page.  Record evidence at each
    # matching PDF page; the human audit checks the printed folio separately.
    for needle in ["(3.3)", "3.6", "3.8", "(3.19)", "(3.20)", "(3.21)"]:
        pattern = re.compile(re.escape(needle).replace(r"\.", r"\.\s*"))
        locators[needle] = []
        for idx, page in enumerate(pages):
            lines = page.splitlines()
            matches = [i for i, line in enumerate(lines) if pattern.search(line)]
            for i in matches:
                locators[needle].append({"pdf_page_one_based": idx + 1,
                                         "context": lines[max(0, i - 3):min(len(lines), i + 5)]})
    return {"source": str(source.relative_to(ROOT)), "text": str(temp.relative_to(ROOT)),
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(), "locators": locators}


def main():
    with ThreadPoolExecutor(max_workers=4) as pool:
        downloads = list(pool.map(fetch, TASKS))
    result = {"utc": datetime.now(timezone.utc).isoformat(), "downloads": downloads,
              "dold_puppe": dold_audit()}
    path = ROOT / "logs" / "requested_sources_audit.json"
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
