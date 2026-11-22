#!/usr/bin/env python3
"""Fetch the authors' public final manuscript and public arXiv TeX source.

All downloaded source material remains excluded from deliverables; retain
URLs, response status, byte counts and hashes. No access-control workaround.
"""
from pathlib import Path
import datetime, hashlib, io, json, subprocess, tarfile, time, urllib.request
from ROOT_fetch_ring_sources import main, root

main([("ROOT_MondalReinecke2025.pdf", "https://www.math.purdue.edu/~mondalsh/papers/unipotent-homotopy-theory.pdf")],
     "ROOT_MondalReinecke_pdf_fetch.json",
     "Exact modern higher unipotent group-scheme construction relevant to subject15; no historical identity inferred from its abstract")
pdf=root/"literature/ROOT_MondalReinecke2025.pdf"
if pdf.exists():
    subprocess.run(["pdftotext", "-layout", str(pdf), str(pdf.with_suffix('.txt'))], check=True)
url="https://arxiv.org/src/2302.10703v3"
record={"url":url,"requested_utc":datetime.datetime.now(datetime.timezone.utc).isoformat()}
started=time.perf_counter()
try:
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req,timeout=40) as response:
        data=response.read()
        record.update(http_status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'))
    destination=root/"literature/ROOT_MondalReinecke2025_source"
    destination.mkdir(exist_ok=True)
    with tarfile.open(fileobj=io.BytesIO(data),mode="r:*") as archive:
        archive.extractall(destination,filter="data")
    record.update(status="downloaded_and_extracted",bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
                  files=[str(p.relative_to(root)) for p in destination.rglob('*') if p.is_file()])
except Exception as error:
    record.update(status="failed",error=repr(error))
record["elapsed_seconds"]=time.perf_counter()-started
(root/"logs/ROOT_MondalReinecke_source_fetch.json").write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
