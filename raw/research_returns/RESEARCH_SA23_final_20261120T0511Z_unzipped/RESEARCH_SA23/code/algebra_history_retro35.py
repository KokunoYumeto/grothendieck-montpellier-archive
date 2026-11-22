"""Search the downloaded retrospective texts and preserve all hit locators."""
import json
from pathlib import Path
import re
import subprocess
import time
import unicodedata
import fitz
BASE = Path(__file__).resolve().parents[1]
stems=["rets_transcription","esquisse1972_original","cv1972_original","rapport1984_original"]
patterns={
 "lids_variant":r"lids[kc]?\w*",
 "trace_word":r"\btraces?\b",
 "genus_zero":r"genre\s+(zero|0)",
 "fredholm":r"fredholm",
 "hilbert":r"hilbert",
 "weyl":r"weyl",
 "eigenvalues":r"valeurs?\s+propres?",
 "determinant":r"determinant",
 "nuclear":r"nucleaire",
}
def norm(text):
    text=unicodedata.normalize("NFKD",text.casefold())
    text="".join(c for c in text if not unicodedata.combining(c))
    return text.replace("´","").replace("\u00ad","").replace("-\n","")
report={"utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),"patterns":patterns,"documents":[]}
for stem in stems:
    path=BASE/"sources"/("algebra_history_"+stem+".pdf")
    doc=fitz.open(path)
    hits=[]
    for index,page in enumerate(doc,1):
        raw=page.get_text("text"); text=norm(raw)
        for name,pattern in patterns.items():
            for match in re.finditer(pattern,text):
                hits.append({"term":name,"physical_pdf_page":index,
                             "context":re.sub(r"\s+"," ",text[max(0,match.start()-180):match.end()+220])})
    entry={"stem":stem,"pages":len(doc),"counts":{name:sum(h["term"]==name for h in hits) for name in patterns},
           "hits":hits}
    report["documents"].append(entry)
    print(json.dumps({k:v for k,v in entry.items() if k!="hits"},ensure_ascii=False))
text=json.dumps(report,indent=2,ensure_ascii=False)
(BASE/"notes"/"algebra_retrospective_search_hits.json").write_text(text+"\n")
(BASE/"logs"/"algebra_history_retro35.json").write_text(text+"\n")
