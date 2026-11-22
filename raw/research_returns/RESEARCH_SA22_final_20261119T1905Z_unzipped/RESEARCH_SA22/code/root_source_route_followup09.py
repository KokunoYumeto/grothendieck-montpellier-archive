"""Inspect cached public GIFs and retry two previously unavailable public metadata URLs.

This is source-access documentation, not a mathematical certificate. No article
storage identifier is decoded or requested. There are exactly two network GETs.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import base64
import hashlib
import json
import struct
import time

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT.parent / "source_reading" / "fatcat_availability_1729"
OUTPUT = ROOT / "code/root_source_route_followup09_output.json"
assert not OUTPUT.exists(), "Preserve the original run record."
started = time.perf_counter()
started_utc = datetime.now(timezone.utc).isoformat()
landing = ROOT / "code/part_c_lieberman_historical_landing_output.json"
raw_landing = landing.read_bytes()
images = []
for index, item in enumerate(json.loads(raw_landing).get("images", [])):
    src = item.get("src", "")
    if not src.startswith("data:image/gif;base64,"):
        continue
    data = base64.b64decode(src.split(",", 1)[1], validate=True)
    assert data[:6] in (b"GIF87a", b"GIF89a")
    width, height = struct.unpack("<HH", data[6:10])
    images.append(dict(index=index, alt=item.get("alt", ""),
                       bytes=len(data), width=width, height=height,
                       sha256=hashlib.sha256(data).hexdigest(),
                       interpretation=("One-pixel placeholder; no readable original page."
                           if (width, height) == (1, 1) else
                           "Catalogue image labelled American Journal of Mathematics cover; not an article page.")))

jobs = [("fujiwara1995", "10.1215/S0012-7094-95-08002-8"),
        ("lieberman1968", "10.2307/2373533")]

def fetch(job):
    work, doi = job
    url = "https://api.fatcat.wiki/v0/release/lookup?" + urlencode({"doi": doi})
    now = time.perf_counter()
    record = dict(work=work, doi=doi, url=url,
                  started_utc=datetime.now(timezone.utc).isoformat(),
                  scope="One delayed availability check after the earlier HTTP503; no retry within this run.")
    try:
        req = Request(url, headers={"User-Agent": "ResearchSourceAudit/1.0", "Accept": "application/json"})
        with urlopen(req, timeout=25) as response:
            data = response.read()
            record.update(http_status=response.status, final_url=response.url,
                          content_type=response.headers.get("Content-Type"),
                          bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        CACHE.mkdir(parents=True, exist_ok=True)
        dest = CACHE / (work + ".json")
        dest.write_bytes(data)
        record["source_cache"] = str(dest)
        try:
            parsed = json.loads(data)
            record["json_type"] = type(parsed).__name__
            record["top_level_keys"] = sorted(parsed) if isinstance(parsed, dict) else []
            record["interpretation"] = "Metadata response requires a separate content inspection; no original-text claim."
        except ValueError:
            record["interpretation"] = "Non-JSON response; no release or file metadata assumed."
    except HTTPError as error:
        data = error.read()
        record.update(http_status=error.code, error=str(error), error_body_bytes=len(data),
                      error_body_sha256=hashlib.sha256(data).hexdigest(),
                      error_excerpt=data[:400].decode(errors="replace"),
                      interpretation="No metadata record obtained; this is not evidence of absence.")
    except Exception as error:
        record.update(error=f"{type(error).__name__}: {error}",
                      interpretation="No metadata record obtained; this is not evidence of absence.")
    record["elapsed_seconds"] = time.perf_counter() - now
    return record

network_start = time.perf_counter()
with ThreadPoolExecutor(max_workers=2) as pool:
    requests = list(pool.map(fetch, jobs))
network_seconds = time.perf_counter() - network_start
result = dict(started_utc=started_utc,
              scope="Cached GIF header inspection plus exactly two delayed public DOI-metadata availability checks.",
              cached_landing_sha256=hashlib.sha256(raw_landing).hexdigest(),
              gif_headers=images, network_requests=requests,
              network_wall_seconds=network_seconds,
              elapsed_seconds=time.perf_counter() - started)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
