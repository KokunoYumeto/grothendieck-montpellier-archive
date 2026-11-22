"""Prepare selective hit review and original page renders; no inference from missing OCR."""
import json,subprocess,time
from pathlib import Path
import fitz
BASE=Path(__file__).resolve().parents[1]
report=json.loads((BASE/"notes"/"algebra_retrospective_search_hits.json").read_text())
review=[]
for document in report["documents"]:
    for hit in document["hits"]:
        if hit["term"]!="trace_word" or any(w in hit["context"] for w in ["operateur","hilbert","somme","sommable","fonctionnelle","fredholm","noyau","nucleaire","spectr","determinant"]):
            review.append({"stem":document["stem"],**hit})
out=BASE/"notes"/"algebra_retrospective_selected_hits.json"
out.write_text(json.dumps(review,indent=2,ensure_ascii=False)+"\n")
renders=[]
for stem,page_numbers in [("esquisse1972_original",[1]),("cv1972_original",[1,3])]:
    source=BASE/"sources"/("algebra_history_"+stem+".pdf")
    doc=fitz.open(source)
    if stem=="esquisse1972_original":
        page_numbers += [i+1 for i,p in enumerate(doc) if "The trace of certain operators" in p.get_text()]
    for number in page_numbers:
        prefix=BASE/"sources"/("algebra_history_"+stem+"_p"+str(number).zfill(3))
        command=["pdftoppm","-f",str(number),"-l",str(number),"-scale-to","2000","-png","-singlefile",str(source),str(prefix)]
        run=subprocess.run(command,capture_output=True,text=True)
        renders.append({"command":command,"returncode":run.returncode,"stdout":run.stdout,"stderr":run.stderr,"png":str(prefix)+".png"})
log={"utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),"review_file":str(out),"reviewed_hit_count":len(review),"renders":renders}
text=json.dumps(log,indent=2,ensure_ascii=False)
(BASE/"logs"/"algebra_history_retro37.json").write_text(text+"\n")
print(text)
