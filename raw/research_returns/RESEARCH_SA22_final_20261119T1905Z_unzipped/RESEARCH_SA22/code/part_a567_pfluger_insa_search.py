#!/usr/bin/env python3
"""Submit two terms through the exact previously observed public INSA form."""
from pathlib import Path
from datetime import datetime,timezone
from html.parser import HTMLParser
from concurrent.futures import ThreadPoolExecutor
import hashlib,json,re,time,urllib.request,urllib.error,urllib.parse
base=Path("/workspace/scratch/9c53b536a97f")
cache=base/"source_reading/pfluger_insa"
prior=json.loads((base/"RESEARCH_SA22/code/part_a567_pfluger_insa_public_page_output.json").read_text())
form=next(f for f in prior["forms"] if f["attributes"].get("action")=="/search")
assert any(f["attributes"].get("name")=="query" for f in form["fields"])
assert form["attributes"].get("method","GET").upper()=="GET"
action=urllib.parse.urljoin(prior["final_url"],form["attributes"]["action"])
class Text(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.parts=[]
 def handle_starttag(self,t,a):
  if t in ("script","style"):self.skip+=1
 def handle_endtag(self,t):
  if t in ("script","style"):self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip and d.strip():self.parts.append(d.strip())
def fetch(term):
 started=datetime.now(timezone.utc).isoformat();begin=time.perf_counter()
 url=action+"?"+urllib.parse.urlencode({"query":term})
 d={"term":term,"request_url":url,"started_utc":started,"request_count":1,"retries":0}
 try:
  with urllib.request.urlopen(url,timeout=30) as r:
   body=r.read();d.update(status=r.status,final_url=r.geturl(),content_type=r.headers.get("Content-Type"))
 except urllib.error.HTTPError as e:body=e.read();d.update(status=e.code,error=str(e),final_url=e.geturl())
 except Exception as e:body=b"";d.update(status=None,error=repr(e))
 p=cache/("search_"+term+".html");p.write_bytes(body)
 d.update(raw_cache_path=str(p),body_bytes=len(body),sha256=hashlib.sha256(body).hexdigest())
 if d.get("status")==200:
  t=Text();t.feed(body.decode("utf-8","replace"));text="\n".join(t.parts)
  tp=cache/("search_"+term+".txt");tp.write_text(text)
  d.update(text_cache_path=str(tp),text_sha256=hashlib.sha256(text.encode()).hexdigest(),
   no_results_markers=[s for s in t.parts if re.search(r"no results|no items|0 results|nothing found",s,re.I)],
   result_count_labels=[s for s in t.parts if re.search(r"showing \d|results found|items found",s,re.I)])
 d["elapsed_seconds"]=time.perf_counter()-begin;d["ended_utc"]=datetime.now(timezone.utc).isoformat()
 return d
started=datetime.now(timezone.utc).isoformat();begin=time.perf_counter()
with ThreadPoolExecutor(max_workers=2) as pool:records=list(pool.map(fetch,["Pfluger","Verheftung"]))
out={"started_utc":started,"elapsed_seconds":time.perf_counter()-begin,
 "source_form":{"source_record":"code/part_a567_pfluger_insa_public_page_output.json","action":action,"method":"GET(default in observed form)","field":"query"},
 "records":records,"scope":"Two public repository search requests only; no item files, login or mathematics."}
p=base/"RESEARCH_SA22/code/part_a567_pfluger_insa_search_output.json";p.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))

