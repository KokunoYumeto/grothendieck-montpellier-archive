#!/usr/bin/env python3
"""Summarize the two saved TIFR web outputs; no network operations."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,time
base=Path("/workspace/scratch/9c53b536a97f")
cache=base/"source_reading/recorded_web_search"
code=base/"RESEARCH_SA22/code"
started=datetime.now(timezone.utc).isoformat();begin=time.perf_counter();records=[]
for name in ("discovery","open"):
 p=cache/("part_a567_pfluger_tifr_"+name+"_raw.json")
 raw=p.read_bytes();d=json.loads(raw);sources=[]
 for c in d["result"].get("content",[]):
  if c.get("type")!="text":continue
  for block in re.split(r"\n-{50,}\n",c["text"]):
   m=re.search(r"【(turn[^】]+)】",block)
   if not m:continue
   prefix=block[:m.start()].strip();head=re.match(r"^(.*?)\s*\((https?://[^\s)]+)",prefix,re.S)
   s={"source_ref":m.group(1)}
   if head:s.update(heading=head.group(1),url=head.group(2))
   count=re.search(r"Total lines:\s*(\d+)",block)
   if count:s["reported_extracted_total_lines"]=int(count.group(1))
   sources.append(s)
 compact={k:v for k,v in d.items() if k!="result"}
 compact.update(record_schema="bounded_web_execution_metadata_v1",sources=sources,
  returned_source_blocks=len(sources),source_count_scope="Returned source blocks, not total hits.",
  raw_cache_path=str(p),raw_cache_sha256=hashlib.sha256(raw).hexdigest(),raw_cache_bytes=len(raw),
  bounded_outcome=("Three targeted TIFR metadata queries exposed generic library and service records but no target volume/offprint record."
   if name=="discovery" else "Read official SIRC service page; it describes OPAC/holdings, but rendered OPAC labels expose no query form or target record. No holdings absence or original reading claimed."),
  source_gate="Pfluger1960 original remains unread; no mathematical status change.")
 out=code/("part_a567_pfluger_tifr_"+name+"_metadata.json")
 payload=(json.dumps(compact,ensure_ascii=False,indent=2)+"\n").encode();out.write_bytes(payload)
 records.append({"metadata_file":str(out),"metadata_sha256":hashlib.sha256(payload).hexdigest(),
  "raw_cache_path":str(p),"raw_cache_sha256":hashlib.sha256(raw).hexdigest(),
  "raw_cache_bytes":len(raw),"metadata_bytes":len(payload),"source_count":len(sources),
  "started":d["started"],"ended":d["ended"],"tool_call_seconds":d["tool_call_seconds"]})
output={"operation":"Metadata-only summarization; zero network and mathematics.",
 "started_utc":started,"elapsed_seconds":time.perf_counter()-begin,
 "timing_scope":"Includes raw reads, parsing and compact writes; excludes final output serialization.",
 "records":records}
(code/"part_a567_pfluger_tifr_metadata_output.json").write_text(json.dumps(output,indent=2)+"\n")
print(json.dumps(output,indent=2))

