#!/usr/bin/env python3
"""Fetch and inventory the exact arXiv source supporting the bar-PD audit."""
from __future__ import annotations
import gzip
import hashlib
import io
import json
from pathlib import Path
import tarfile
import time
from urllib.request import Request, urlopen


def main() -> None:
    start = time.perf_counter()
    root = Path(__file__).resolve().parents[2]
    target = root / "sources" / "B_Richter"
    target.mkdir(parents=True, exist_ok=True)
    url = "https://arxiv.org/src/0811.4704v1"
    archive = target / "0811.4704v1.source"
    if not archive.exists():
        req = Request(url, headers={"User-Agent": "MathematicalSourceAudit/1.0"})
        with urlopen(req, timeout=60) as response:
            archive.write_bytes(response.read())
    data = archive.read_bytes()
    files = []
    try:
        tar = tarfile.open(fileobj=io.BytesIO(data), mode="r:*")
    except tarfile.ReadError:
        try:
            tex = gzip.decompress(data)
        except gzip.BadGzipFile:
            tex = data
        name = target / "richter_0811.4704v1.tex"
        name.write_bytes(tex)
        files.append(name)
    else:
        with tar:
            for member in tar.getmembers():
                if not member.isfile():
                    continue
                relative = Path(member.name)
                if relative.is_absolute() or ".." in relative.parts:
                    raise ValueError("Unsafe source archive path")
                name = target / relative
                name.parent.mkdir(parents=True, exist_ok=True)
                stream = tar.extractfile(member)
                assert stream is not None
                name.write_bytes(stream.read())
                files.append(name)
    out = {
        "url": url,
        "published_pdf_url": "https://math.mit.edu/~hrm/palestine/richter-divided-power.pdf",
        "source_sha256": hashlib.sha256(data).hexdigest(),
        "files": [
            {
                "path": str(name.relative_to(root)),
                "bytes": name.stat().st_size,
                "sha256": hashlib.sha256(name.read_bytes()).hexdigest(),
            }
            for name in files
        ],
        "runtime_seconds": time.perf_counter() - start,
    }
    logfile = root / "deliverable" / "logs" / "B_richter_source.json"
    logfile.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out))


if __name__ == "__main__":
    main()
