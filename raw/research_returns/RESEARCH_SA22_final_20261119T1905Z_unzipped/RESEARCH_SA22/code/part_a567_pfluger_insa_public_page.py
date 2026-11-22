#!/usr/bin/env python3
"""One ordinary GET of an observed public INSA page; metadata only in code/."""
from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser
import hashlib,json,time,urllib.request,urllib.error

url="https://insa.ndl.gov.in/"
base=Path("/workspace/scratch/9c53b536a97f")
cache=base/"source_reading/pfluger_insa"
cache.mkdir(parents=True,exist_ok=True)
started=datetime.now(timezone.utc).isoformat()
begin=time.perf_counter()
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.forms=[];self.links=[];self.scripts=[];self.current=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=="form":
            self.current={"attributes":a,"fields":[]};self.forms.append(self.current)
        elif tag in ("input","select","button","textarea") and self.current is not None:
            self.current["fields"].append({"tag":tag,"attributes":a})
        elif tag=="a" and "href" in a:self.links.append(a)
        elif tag=="script" and "src" in a:self.scripts.append(a["src"])
    def handle_endtag(self,tag):
        if tag=="form":self.current=None
record={"started_utc":started,"request_url":url,"request_count":1,"retries":0}
try:
    with urllib.request.urlopen(url,timeout=30) as response:
        body=response.read()
        record.update(status=response.status,final_url=response.geturl(),content_type=response.headers.get("Content-Type"))
except urllib.error.HTTPError as e:
    body=e.read()
    record.update(status=e.code,final_url=e.geturl(),error=str(e))
except Exception as e:
    body=b""
    record.update(status=None,error=repr(e))
path=cache/"repository_home.html"
path.write_bytes(body)
record.update(body_bytes=len(body),raw_cache_path=str(path),sha256=hashlib.sha256(body).hexdigest())
if record.get("status")==200:
    parser=Page();parser.feed(body.decode("utf-8","replace"))
    record.update(forms=parser.forms,advertised_links=parser.links,advertised_scripts=parser.scripts)
record["elapsed_seconds"]=time.perf_counter()-begin
record["ended_utc"]=datetime.now(timezone.utc).isoformat()
record["scope"]="One public home-page read and metadata parsing; no content item, search submission, login or mathematical check."
output=base/"RESEARCH_SA22/code/part_a567_pfluger_insa_public_page_output.json"
output.write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n")
print(json.dumps(record,ensure_ascii=False,indent=2))

