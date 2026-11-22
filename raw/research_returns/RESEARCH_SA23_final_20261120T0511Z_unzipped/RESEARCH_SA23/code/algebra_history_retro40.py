"""Preserve retrospective audit events and correct imprecise manual web-log labels."""
import json,time
from pathlib import Path
BASE=Path(__file__).resolve().parents[1]
changes=[]
for number in range(66,71):
    path=BASE/"notes"/("algebra_history_web"+str(number)+".json")
    data=json.loads(path.read_text())
    previous=data.pop("utc",None)
    data["utc_interval"]="2026-11-20 03:10:48--03:12:26 UTC"
    data["timestamp_annotation"]="The former manually estimated label was not an observed clock reading; replaced by the bracketing observed clock interval. Source results unchanged."
    data["superseded_unverified_manual_label"]=previous
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n")
    changes.append(str(path))
events=[
 ["geo-H-history","2026-11-20","GPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters","used and rechecked in this run","Original Grothendieck 1961 Studia note pp141-143 visually read in two PDF spreads; p142 Proposition2 proof(a) uses full Hilbert trace theorem without proof; p143 receipt20June1960 and Cartier proof-stage reference distinguished from any cote1 date.","notes/algebra_trace1961_source_audit.md;logs/algebra_history_retro38.json;notes/algebra_retrospective_references.bib"],
 ["geo-H-history","2026-11-20","GPT-6 Astra Pro (OpenAI), inherited effort, algebra_letters","used and rechecked in this run","Full1502-page modern French R&S transcription searched;104 selected contexts reviewed;97 original-scan pages OCR-searched with English OCR limitation; original CVpp1,3 and thematic reportpp1,13 visually collated; no identified date for cote1 proof. Broad1949-1953 period label is not a manuscript date.","notes/algebra_retrospective_source_search.md;logs/algebra_history_retro34.json;logs/algebra_history_retro35.json;logs/algebra_history_retro37.json;logs/algebra_history_retro39.json"]
]
eventfile=BASE/"notes"/"algebra_history_CHECK_EVENTS.tsv"
with eventfile.open("a") as stream:
    for event in events:stream.write("\t".join(event)+"\n")
report={"utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),"timestamp_annotations_corrected":changes,"events_appended":events}
text=json.dumps(report,indent=2,ensure_ascii=False)
(BASE/"logs"/"algebra_history_retro40.json").write_text(text+"\n")
print(text)
