"""Fetch the two explicitly cited public arXiv author sources once.

This records retrieval provenance only; it is not a mathematical certificate.
It does not extract or touch the user's original archive.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from io import BytesIO
from pathlib import Path
import gzip
import json
import tarfile
import time
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
TASKS = [
    ("2019", "https://arxiv.org/src/1902.03540v3"),
    ("2018_pairing", "https://arxiv.org/src/1410.3046v4"),
]


def fetch(task):
    tag, url = task
    started = time.perf_counter()
    row = {"url": url, "utc": datetime.now(timezone.utc).isoformat()}
    dest = ROOT / "literature" / f"B_Suzuki{tag}_source"
    dest.mkdir(exist_ok=True)
    try:
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(req, timeout=50) as response:
            data = response.read(10_000_001)
            row.update(status=response.status, final_url=response.url)
        if len(data) > 10_000_000:
            raise ValueError("unexpectedly large source archive")
        row.update(bytes=len(data), sha256=sha256(data).hexdigest())
        (dest / "source.download").write_bytes(data)
        written = []
        try:
            archive = tarfile.open(fileobj=BytesIO(data), mode="r:*")
        except tarfile.ReadError:
            content = gzip.decompress(data) if data[:2] == b"\x1f\x8b" else data
            if b"\\documentclass" not in content and b"\\begin{document}" not in content:
                raise ValueError("download is not a recognizable TeX source")
            name = "main.tex"
            (dest / name).write_bytes(content)
            written.append(name)
        else:
            with archive:
                for member in archive.getmembers():
                    if not member.isfile():
                        continue
                    suffix = Path(member.name).suffix.lower()
                    if suffix not in {".tex", ".bib", ".sty", ".bbl", ".cls"}:
                        continue
                    safe_name = member.name.replace("/", "__").replace("\\", "__")
                    content = archive.extractfile(member).read()
                    (dest / safe_name).write_bytes(content)
                    written.append(safe_name)
        row["written"] = written
        row["outcome"] = "retrieved"
    except Exception as exc:
        row.update(outcome="failed", error=f"{type(exc).__name__}: {exc}")
    row["elapsed_seconds"] = time.perf_counter() - started
    return row


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(fetch, TASKS))
    path = ROOT / "logs" / "B_Suzuki_source_fetch.json"
    path.write_text(json.dumps(results, indent=2))
    print(json.dumps(results, indent=2))
