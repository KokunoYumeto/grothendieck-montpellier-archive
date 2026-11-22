#!/usr/bin/env python3
"""Record only metadata from the already executed three-query batch."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
base=Path("/workspace/scratch/9c53b536a97f")
raw_path=base/"source_reading/recorded_web_search/part_a567_remaining_originals_openrepo_batch_raw.json"
started=datetime.now(timezone.utc).isoformat();begin=time.perf_counter()
raw=raw_path.read_bytes();d=json.loads(raw)
texts=[c["text"] for c in d["result"].get("content",[]) if c.get("type")=="text"]
assert len(d["commands"]["system1_search_query"])==3
assert any("Empty search results" in t for t in texts)
out={k:v for k,v in d.items() if k!="result"}
out.update(record_schema="bounded_web_execution_metadata_v1",
 raw_cache_path=str(raw_path),raw_cache_sha256=hashlib.sha256(raw).hexdigest(),raw_cache_bytes=len(raw),
 returned_source_blocks=0,individual_query_hit_counts=None,
 outcome="The combined three-query response explicitly reports empty search results. No plausible original record was exposed; no follow-up open or request.",
 excluded_repeated_repository="HAL: prior title/DOI zero-result searches already recorded for all three targets.",
 source_status={"Pfluger1960":"unread","Lieberman1968":"unread","Fujiwara1995":"unread"},
 followup_web_operations=0,ordinary_http_requests=0,mathematical_tests=0,
 normalization_started_utc=started,normalization_elapsed_seconds=time.perf_counter()-begin,
 normalization_timing_scope="Cached record read, hash and metadata assembly only; excludes final output serialization.")
target=base/"RESEARCH_SA22/code/part_a567_remaining_originals_openrepo_batch_metadata.json"
target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(out,ensure_ascii=False,indent=2))

