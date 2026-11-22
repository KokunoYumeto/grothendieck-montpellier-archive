"""Export compact provenance from five already executed source-discovery calls.

This is an offline record operation; it performs no query, download or proof
check. Full returned source bodies remain in the outside reading cache.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import time

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT.parent / "source_reading/recorded_web_search"
names = ["root_core_originals_search_1751", "root_core_originals_verify_1751",
         "root_core_discovery_home_1752", "root_semantic_originals_search_1753",
         "root_semantic_originals_verify_1753"]
output = ROOT / "code/root_core_semantic_routes_output.json"
assert not output.exists()
started = time.perf_counter()
started_utc = datetime.now(timezone.utc).isoformat()
records = []
for name in names:
    path = CACHE / (name + ".json")
    raw = path.read_bytes()
    value = json.loads(raw)
    headers = []
    for block in value["result"].get("content", []):
        if block.get("type") != "text":
            continue
        for match in re.finditer(r"([^\n]+) \((https?://[^\n]+)\)\n【([^】]+)】", block["text"]):
            headers.append(dict(title=match[1], url=match[2], ref=match[3]))
    records.append(dict(name=name, request=value["request"], seconds=value["seconds"],
                        source_headers=headers, raw_cache=str(path),
                        raw_bytes=len(raw), raw_sha256=hashlib.sha256(raw).hexdigest()))
record = dict(started_utc=started_utc, scope="Offline metadata export from the five actual preserved tool returns; no new requests.",
              queries=12, separate_open_commands=1, web_calls=5, records=records,
              conclusions=[
                  "No target original was obtained from the requested CORE or Semantic Scholar domain queries.",
                  "Search results included broader-domain later bibliographies and already known metadata; they are not an exhaustive service inventory.",
                  "The actual CORE Discovery page open returned403Forbidden and stopped that route.",
                  "The NDL/CiNii Fujiwara candidates were handed to PartB for duplicate-route assessment, without a new publisher request.",
                  "No original-source gate or mathematical status changed."],
              seconds=time.perf_counter() - started)
output.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({k:v for k,v in record.items() if k != "records"}, indent=2))
