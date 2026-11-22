"""Record only the actual scope of a bounded, unsuccessful original-source search."""
from pathlib import Path
import datetime,json,hashlib
R=Path("RESEARCH_SA23");raw=[]
for n in range(154,158):
 p=R/f"notes/algebra_history_web{n}.json";obj=json.loads(p.read_text())
 raw.append({"path":str(p.relative_to(R)),"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"recorded_utc":obj["recorded_utc"]})
event="\t".join(["geo-H-history","2026-11-20","GPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters","used and rechecked in this run","Distinct Dunford-SchwartzII public-repository search: exact title/filename, academic-domain and author-site queries found no original relevant pages. New Wiley opening403 stopped. Prior Google/djvu/archive routes not retried. No original historical-note pages read and no claim about unseen contents.","notes/algebra_dunfordII_public_repository_search.md;notes/algebra_dunfordII_query_manifest.json;logs/algebra_dunfordII_record64.json"])
p=R/"notes/algebra_history_CHECK_EVENTS.tsv"
if event not in p.read_text():
 with p.open("a") as f:f.write(event+"\n")
record={"utc_recorded":datetime.datetime.now(datetime.timezone.utc).isoformat(),"raw":raw,"original_pages_read":[],"result":"Access-limited; no dating witness; contents of requested book pages remain unchecked","event":event}
s=json.dumps(record,ensure_ascii=False,indent=2);(R/"logs/algebra_dunfordII_record64.json").write_text(s+"\n");print(s)

