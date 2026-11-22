#!/usr/bin/env python3
"""Retain exact primary-source download attempts for the finite-jet audit."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import datetime, hashlib, json, subprocess, time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ("asakura2006_dlog_v4", "https://arxiv.org/pdf/math/0511190v4"),
    ("ballico_gasparim_koppe2009", "https://sitios.ucn.cl/~etgasparim/Xjpaa2.pdf"),
    ("BEK2014_charzero_lifting", "https://page.mi.fu-berlin.de/esnault/preprints/helene/112-bek.pdf"),
    ("patel_ravindra_author_torsion", "https://www.math.purdue.edu/~patel471/torsionWL.pdf"),
]

def one(item):
    name, url = item
    start = time.perf_counter()
    row = {"name": name, "url": url}
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            row["status_code"] = response.status
            row["final_url"] = response.url
            content = response.read()
        if not content.startswith(b"%PDF"):
            raise ValueError("Response is not a PDF; no source file written")
        path = ROOT / "sources" / (name + ".pdf")
        path.write_bytes(content)
        row.update(bytes=len(content), sha256=hashlib.sha256(content).hexdigest(), path=str(path.relative_to(ROOT)))
        proc = subprocess.run(["pdftotext", "-layout", str(path), str(path.with_suffix(".txt"))], capture_output=True, text=True)
        row["pdftotext_returncode"] = proc.returncode
    except Exception as exc:
        row["error"] = str(exc)
    row["seconds"] = time.perf_counter() - start
    return row

if __name__ == "__main__":
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(one, SOURCES))
    result = {"started_utc": started, "finished_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "seconds": time.perf_counter()-start, "sources": rows}
    target = ROOT / "output" / "charzero_lifting_sources.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
