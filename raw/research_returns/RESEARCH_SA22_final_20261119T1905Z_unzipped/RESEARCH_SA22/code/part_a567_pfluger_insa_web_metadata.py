#!/usr/bin/env python3
"""Summarize already cached INSA web results; zero network operations."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,time
base=Path("/workspace/scratch/9c53b536a97f")
cache=base/"source_reading/recorded_web_search"
code=base/"RESEARCH_SA22/code"
started=datetime.now(timezone.utc).isoformat();begin=time.perf_counter()
records=[]
for name in ("discovery","open"):
 p=cache/("part_a567_pfluger_insa_"+name+"_raw.json")
 raw=p.read_bytes();data=json.loads(raw)
 sources=[]
 for content in data["result"].get("content",[]):
  if content.get("type")!="text":continue
  for block in re.split(r"\n-{50,}\n",content["text"]):
   ref=re.search(r"【(turn[^】]+)】",block)
   if not ref:continue
   prefix=block[:ref.start()].strip()
   m=re.match(r"^(.*?)\s*\((https?://.*)\)$",prefix,re.S)
   if not m:raise ValueError(prefix)
   source={"source_ref":ref.group(1),"heading":m.group(1),"url":m.group(2)}
   n=re.search(r"Total lines: (\d+)",block)
   if n:source["reported_extracted_total_lines"]=int(n.group(1))
   sources.append(source)
 result={k:v for k,v in data.items() if k!="result"}
 result.update(record_schema="bounded_web_execution_metadata_v1",sources=sources,
   returned_source_blocks=len(sources),
   returned_source_blocks_scope="Returned blocks, not total search-engine hits.",
   raw_cache_path=str(p),raw_cache_sha256=hashlib.sha256(raw).hexdigest(),raw_cache_bytes=len(raw),
   bounded_outcome=("One INSA discovery query identified the official library and actual institutional repository; no original target passage."
    if name=="discovery" else "Read both actual public pages. Repository displayed three communities, none named JIMS. Official library advertises a public OPAC; that separate holdings link was not followed."),
   source_gate="Pfluger1960 original remains unread; no mathematical status change.")
 dest=code/("part_a567_pfluger_insa_"+name+"_web_metadata.json")
 payload=(json.dumps(result,ensure_ascii=False,indent=2)+"\n").encode()
 dest.write_bytes(payload)
 records.append({"metadata_file":str(dest),"metadata_sha256":hashlib.sha256(payload).hexdigest(),
  "raw_cache_path":str(p),"raw_cache_sha256":hashlib.sha256(raw).hexdigest(),
  "raw_cache_bytes":len(raw),"metadata_bytes":len(payload),"source_count":len(sources)})
out={"operation":"Metadata-only summarization of two already cached web outputs; no network or mathematics.",
 "started_utc":started,"elapsed_seconds":time.perf_counter()-begin,
 "timing_scope":"Includes both raw reads, parsing and compact writes; excludes this final output serialization.",
 "records":records}
(code/"part_a567_pfluger_insa_web_metadata_output.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))

