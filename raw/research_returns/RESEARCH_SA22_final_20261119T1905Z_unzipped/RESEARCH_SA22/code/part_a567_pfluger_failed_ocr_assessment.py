#!/usr/bin/env python3
"""Assess only the prior failed OCR row; no network and no source text output."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
base=Path("/workspace/scratch/9c53b536a97f/RESEARCH_SA22")
path=base/"code/root_pfluger_public_ocr_inventory_output.json"
started=datetime.now(timezone.utc).isoformat();begin=time.perf_counter()
raw=path.read_bytes();data=json.loads(raw)
errors=data["errors"]
assert len(errors)==1
item=errors[0]
allowed=("identifier","filename","bytes_advertised","title","url","error","seconds")
compact={k:item[k] for k in allowed if k in item}
positions=[i for i,r in enumerate(data["results"]) if r.get("identifier")==item["identifier"]]
assert item["identifier"]=="journalvolumevin0000unse"
assert "1914" in item["title"] and "VI, NO-3" in item["title"]
out={
 "started_utc":started,
 "source_output_path":str(path),
 "source_output_sha256":hashlib.sha256(raw).hexdigest(),
 "source_output_bytes":len(raw),
 "locators":{"errors_index_zero_based":0,"results_indices_zero_based":positions},
 "failed_item_compact_metadata":compact,
 "catalogue_identification":{"volume":"VI","number":"3","month":"June","year":1914},
 "target_identification":{"volume":"24 (new series)","year":1960,"pages":"401-412"},
 "disposition":"NO NEW REQUEST: explicit June1914 volumeVI issue3 metadata excludes the sought1960 volume24 target.",
 "evidence_scope":"The existing compact catalogue title was read. The failed OCR body and original scan were not read, and no content-based date assertion is made.",
 "later_retry_review":"Not needed or performed: the metadata exclusion already decides against another request.",
 "network_requests":0,
 "mathematical_tests":0,
 "source_gate":"Pfluger1960 original remains unread.",
 "elapsed_seconds":time.perf_counter()-begin,
 "timing_scope":"Local source-ledger read, compact failed-row extraction and hash; excludes final output serialization. Earlier inline triage had no separately measured Python runtime."
}
dest=base/"code/part_a567_pfluger_failed_ocr_assessment_output.json"
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(out,ensure_ascii=False,indent=2))

