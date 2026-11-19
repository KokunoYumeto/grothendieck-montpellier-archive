"""Fetch exact primary sources explored for the remaining E.3 generation gate."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
sources={
    "Saito1979": "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8BE754AE13330E3050F3588FCD123D87/S0027763000024855a.pdf/abelian_varieties_attached_to_cycles_of_intermediate_dimension.pdf",
    "Peters2026Incidence": "https://arxiv.org/pdf/2607.22233",
    "AkhtarPontryagin": "https://reza-akhtar.github.io/research/final/pont.pdf",
    "PelaezReyes2025Incidence": "https://arxiv.org/pdf/2501.19147",
}

def fetch(item):
    name,url=item
    start=time.perf_counter()
    record={"name":name,"url":url,"date_utc":datetime.now(timezone.utc).isoformat()}
    try:
        req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
        with urllib.request.urlopen(req,timeout=35) as response:
            data=response.read()
        if not data.startswith(b"%PDF"):
            raise ValueError("Response is not a PDF")
        path=ROOT/"sources"/(name+".pdf")
        path.write_bytes(data)
        txt=path.with_suffix(".txt")
        run=subprocess.run(["pdftotext","-layout",str(path),str(txt)],capture_output=True,text=True)
        record.update(status="downloaded",bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),pdf=str(path),text=str(txt),pdftotext_exit=run.returncode)
    except Exception as exc:
        record.update(status="failed",error=f"{type(exc).__name__}: {exc}")
    record["elapsed_seconds"]=time.perf_counter()-start
    return record

with ThreadPoolExecutor(max_workers=4) as pool:
    records=list(pool.map(fetch,sources.items()))
(ROOT/"output/fetch_generation_gate_sources.json").write_text(json.dumps(records,indent=2)+"\n")
print(json.dumps(records,indent=2))
