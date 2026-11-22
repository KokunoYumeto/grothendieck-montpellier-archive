#!/usr/bin/env python3
"""Compact metadata for the bounded article-registry attempt; no network."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,time
base=Path("/workspace/scratch/9c53b536a97f")
cache=base/"source_reading/recorded_web_search"
code=base/"RESEARCH_SA22/code"
names=("search1","search2","refs","id_search","homes")
outcomes={
 "search1":"Two exact site-restricted system2 queries returned an empty-search response; not an exhaustive catalogue search.",
 "search2":"Two stronger queries returned later references; an indexed EMS bibliography supplies Zbl0112.05303 and MR0132827, but not target original text or an opened registry record.",
 "refs":"The actual indexed Math-Net bibliography URL redirected to its homepage; no target reference-page contents or registry link were obtained by this open.",
 "id_search":"Exact Zbl identifier and EuDML title queries returned the same EMS reference and unrelated records; no actual target registry record.",
 "homes":"Official zbMATH home returned403Forbidden and was not retried. EuDML home timed out; no form or catalogue record was read. Both bounded routes stopped.",
}
started=datetime.now(timezone.utc).isoformat();begin=time.perf_counter();manifest=[]
for name in names:
 p=cache/("part_a567_pfluger_article_registry_"+name+"_raw.json")
 raw=p.read_bytes();data=json.loads(raw);sources=[];notices=[]
 for c in data["result"].get("content",[]):
  if c.get("type")!="text":continue
  for block in re.split(r"\n-{50,}\n",c["text"]):
   m=re.search(r"【(turn[^】]+)】",block)
   if not m:
    if "Empty search results" in block:notices.append("Empty search results; no results returned for these queries.")
    elif block.strip():notices.append("Non-source service notice retained only in raw cache.")
    continue
   prefix=block[:m.start()].strip();s={"source_ref":m.group(1)}
   titleurl=re.match(r"^(.*?)\s*\((https?://[^\s)]+)",prefix,re.S)
   if titleurl:s.update(heading=titleurl.group(1),url=titleurl.group(2))
   else:s["heading"]=prefix
   sourcecmd=re.search(r"Source: (open|click|find)\((\{.*?\})\);",block)
   if sourcecmd:
    cmd=json.loads(sourcecmd.group(2));s["source_command"]={"name":sourcecmd.group(1),"arguments":cmd}
    if "url" not in s and str(cmd.get("ref_id","")).startswith("http"):s["url"]=cmd["ref_id"]
   redirect=re.search(r"Redirected to URL:\s*(\S+)",block)
   if redirect:s["reported_redirect_url"]=redirect.group(1).rstrip(";")
   count=re.search(r"Total lines:\s*(\d+)",block)
   if count:s["reported_extracted_total_lines"]=int(count.group(1))
   failure=re.search(r"^Failed to fetch.*$",block,re.M)
   if failure:s["service_failure"]=failure.group(0)
   sources.append(s)
 record={k:v for k,v in data.items() if k!="result"}
 record.update(record_schema="bounded_web_execution_metadata_v1",sources=sources,
  returned_source_blocks=len(sources),source_count_scope="Returned source blocks, not total search-engine hits.",
  service_notices=notices,bounded_outcome=outcomes[name],
  raw_cache_path=str(p),raw_cache_sha256=hashlib.sha256(raw).hexdigest(),raw_cache_bytes=len(raw),
  source_gate="Pfluger1960 original unread; no mathematical status change.")
 target=code/("part_a567_pfluger_article_registry_"+name+"_metadata.json")
 payload=(json.dumps(record,ensure_ascii=False,indent=2)+"\n").encode();target.write_bytes(payload)
 manifest.append({"record_path":str(target),"metadata_bytes":len(payload),"metadata_sha256":hashlib.sha256(payload).hexdigest(),
  "raw_cache_path":str(p),"raw_bytes":len(raw),"raw_sha256":hashlib.sha256(raw).hexdigest(),
  "started":data["started"],"tool_call_seconds":data["tool_call_seconds"],"source_count":len(sources)})
out={"operation":"Metadata-only summarization of five already cached web records; zero network and mathematical tests.",
 "started_utc":started,"elapsed_seconds":time.perf_counter()-begin,
 "timing_scope":"Includes reads, parsing and compact writes; excludes final output serialization.",
 "records":manifest}
(code/"part_a567_pfluger_article_registry_metadata_output.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))

