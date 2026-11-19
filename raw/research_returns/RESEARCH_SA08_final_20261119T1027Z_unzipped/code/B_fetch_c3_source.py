"""Fetch primary arXiv source for the active C3 model-category check."""
from pathlib import Path
from urllib.request import Request, urlopen
import argparse, hashlib, io, json, tarfile, time

p = argparse.ArgumentParser()
p.add_argument("identifier")
p.add_argument("tag")
a = p.parse_args()
root = Path(__file__).resolve().parents[1]
url = "https://arxiv.org/src/" + a.identifier
start = time.monotonic()
receipt = {"url": url, "identifier": a.identifier, "status": "not fetched"}
try:
    with urlopen(Request(url, headers={"User-Agent": "SA08 primary source audit"}), timeout=55) as r:
        data = r.read()
    archive = root / "sources" / ("B_" + a.tag + ".tar")
    archive.write_bytes(data)
    receipt.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), archive=str(archive))
    dest = root / "sources" / ("B_" + a.tag + "_source")
    dest.mkdir(exist_ok=True)
    names = []
    try:
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:*") as t:
            for m in t.getmembers():
                if not m.isfile() or not m.name.endswith((".tex", ".bib", ".txt", ".bbl")):
                    continue
                target = (dest / m.name).resolve()
                if not target.is_relative_to(dest.resolve()):
                    raise ValueError("Unsafe archive path")
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(t.extractfile(m).read())
                names.append(str(target.relative_to(dest)))
    except tarfile.ReadError:
        import gzip
        text = gzip.decompress(data)
        if b"\\documentclass" not in text:
            raise ValueError("Response is neither a source tar nor a recognizable TeX source")
        (dest / "main.tex").write_bytes(text)
        names = ["main.tex"]
    receipt.update(status="source fetched and text files extracted; mathematical scope not yet read", files=names)
except Exception as e:
    receipt.update(error=type(e).__name__ + ": " + str(e))
finally:
    receipt["seconds"] = time.monotonic() - start
    (root / "logs" / ("B_" + a.tag + "_fetch.json")).write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))
