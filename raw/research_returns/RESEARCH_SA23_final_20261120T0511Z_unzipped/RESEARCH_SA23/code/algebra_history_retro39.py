"""OCR the two public R&S scan supplements; preserve commands, outputs, and search indices."""
from concurrent.futures import ThreadPoolExecutor
import json, os, re, subprocess, time, unicodedata
from pathlib import Path
import fitz
BASE=Path(__file__).resolve().parents[1]
started=time.monotonic()
languages=subprocess.run(["tesseract","--list-langs"],capture_output=True,text=True)
language="fra" if re.search(r"(?m)^fra$",languages.stdout) else "eng"
jobs=[]
for stem in ["rets_firstpart_original","rets_complements_original"]:
    pdf=BASE/"sources"/("algebra_history_"+stem+".pdf")
    doc=fitz.open(pdf)
    folder=BASE/"sources"/("algebra_history_"+stem+"_ocr")
    folder.mkdir(exist_ok=True)
    for index,page in enumerate(doc,1):
        png=folder/("page_"+str(index).zfill(3)+".png")
        page.get_pixmap(dpi=150).save(png)
        jobs.append((stem,index,png))
def work(job):
    stem,index,png=job
    prefix=png.with_suffix("")
    command=["tesseract",str(png),str(prefix),"-l",language,"--psm","3"]
    env=dict(os.environ);env["OMP_THREAD_LIMIT"]="1"
    start=time.monotonic()
    run=subprocess.run(command,capture_output=True,text=True,env=env,timeout=45)
    return {"stem":stem,"physical_pdf_page":index,"command":command,"returncode":run.returncode,
            "stdout":run.stdout,"stderr":run.stderr,"text_file":str(prefix)+".txt","seconds":round(time.monotonic()-start,6)}
with ThreadPoolExecutor(max_workers=6) as pool:
    outcomes=list(pool.map(work,jobs))
documents=[]
patterns={"lids_variant":r"lids[kc]?\w*","trace_word":r"\btraces?\b","genus_zero":r"genre\s+(zero|0)","fredholm":r"fredholm","hilbert":r"hilbert","weyl":r"weyl"}
for stem in ["rets_firstpart_original","rets_complements_original"]:
    hits=[];parts=[]
    for entry in outcomes:
        if entry["stem"]!=stem:continue
        path=Path(entry["text_file"])
        raw=path.read_text() if path.exists() else ""
        parts.append(raw)
        text=unicodedata.normalize("NFKD",raw.casefold())
        text="".join(c for c in text if not unicodedata.combining(c))
        text=text.replace("-\n","")
        for name,pattern in patterns.items():
            for match in re.finditer(pattern,text):
                hits.append({"term":name,"physical_pdf_page":entry["physical_pdf_page"],
                             "context":re.sub(r"\s+"," ",text[max(0,match.start()-180):match.end()+220])})
    out=BASE/"sources"/("algebra_history_"+stem+"_ocr.txt")
    out.write_text("\n\f\n".join(parts))
    documents.append({"stem":stem,"pages":len(parts),"text_file":str(out),
                      "counts":{name:sum(h["term"]==name for h in hits) for name in patterns},"hits":hits})
report={"utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),"seconds":round(time.monotonic()-started,6),
        "languages_command":{"command":["tesseract","--list-langs"],"returncode":languages.returncode,"stdout":languages.stdout,"stderr":languages.stderr},
        "ocr_language":language,"outcomes":outcomes,"documents":documents}
text=json.dumps(report,indent=2,ensure_ascii=False)
(BASE/"logs"/"algebra_history_retro39.json").write_text(text+"\n")
(BASE/"notes"/"algebra_retrospective_ocr_hits.json").write_text(json.dumps(documents,indent=2,ensure_ascii=False)+"\n")
print(json.dumps({k:v for k,v in report.items() if k not in ["outcomes","documents"]},indent=2))
for document in documents:print(json.dumps({k:v for k,v in document.items() if k!="hits"},ensure_ascii=False))
