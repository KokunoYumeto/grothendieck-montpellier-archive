"""Fetch explicitly supplied, observed Lean paths from the pinned secondary mirror.

This downloads source text for reading; it does not execute or compile it.
The manifest belongs to /root/theta_032, avoiding concurrent root-ledger edits.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys
import urllib.request

WORK = Path(__file__).resolve().parent
ROOT = WORK / "alpoge_mirror"
MANIFEST = WORK / "theta_nab_manifest.json"
BASE = (
    "https://raw.githubusercontent.com/CocoSgt/riemann-hypothesis-lean/"
    "7cbf7a0c32fca1badf05931879a37c3f8a2b03b4/src/"
)


def fetch(relative):
    if not re.fullmatch(r"(?:[A-Za-z0-9_]+/)+[A-Za-z0-9_]+\.lean", relative):
        return relative, None, "invalid path"
    path = ROOT / relative
    if path.exists():
        return relative, None, "existing"
    try:
        request = urllib.request.Request(BASE + relative, headers={"User-Agent": "source-audit"})
        with urllib.request.urlopen(request, timeout=35) as response:
            data = response.read()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        metadata = {
            "url": BASE + relative,
            "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(),
            "observed_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
        return relative, metadata, "saved"
    except Exception as error:
        return relative, None, str(error)


if __name__ == "__main__":
    entries = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    with ThreadPoolExecutor(max_workers=6) as pool:
        for relative, metadata, status in pool.map(fetch, sys.argv[1:]):
            if metadata:
                entries[relative] = metadata
            print(status, relative, metadata["bytes"] if metadata else "")
    MANIFEST.write_text(json.dumps(entries, indent=2) + "\n")
