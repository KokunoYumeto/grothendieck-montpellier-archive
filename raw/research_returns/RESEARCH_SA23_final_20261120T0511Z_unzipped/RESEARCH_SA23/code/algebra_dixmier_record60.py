"""Record bounded Dixmier first-edition retrieval, without claiming book content."""
from pathlib import Path
import datetime, hashlib, json
R=Path("RESEARCH_SA23")
files=[]
for n in range(141,148):
 p=R/f"notes/algebra_history_web{n}.json"
 obj=json.loads(p.read_text())
 files.append({"path":str(p.relative_to(R)),"bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"recorded_utc":obj["recorded_utc"]})
event="\t".join(["geo-H-history","2026-11-20","GPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters","used and rechecked in this run","Bounded Dixmier1957 route: CiNii first-edition records, Open Library edition records, Google Books1969 metadata, Gabay publisher reprint description and Cambridge1958 review metadata read. Original1957 book pages and review text not opened. Explicit1969/1996 edition boundary preserved; no dated cote1 identification.","notes/algebra_dixmier1957_source_search.md;notes/algebra_dixmier1957_query_manifest.json;logs/algebra_dixmier_record60.json"])
path=R/"notes/algebra_history_CHECK_EVENTS.tsv"
existing=path.read_text()
if event not in existing:
 with path.open("a") as f:f.write(event+"\n")
record={"utc_recorded":datetime.datetime.now(datetime.timezone.utc).isoformat(),"raw_batches":files,"actual_reading":"Public metadata and publisher contents only; no original1957 book pages or original Cooper review text","result":"No dated identification of cote1; original first-edition content remains unopened","event":event}
s=json.dumps(record,ensure_ascii=False,indent=2)
(R/"logs/algebra_dixmier_record60.json").write_text(s+"\n")
print(s)

