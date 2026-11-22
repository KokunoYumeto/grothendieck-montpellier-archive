"""Download and render the exact public mirror linked by the Circle bibliography."""
import hashlib,json,subprocess,time,urllib.request
from pathlib import Path
import fitz
BASE=Path(__file__).resolve().parents[1]
url="https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-Trace-ope.pdf"
start=time.monotonic();result={"url":url}
try:
    with urllib.request.urlopen(url,timeout=25) as response:
        data=response.read()
        path=BASE/"sources"/"algebra_history_trace1961_original.pdf"
        path.write_bytes(data)
        result.update(status=response.status,final_url=response.url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),file=str(path))
    doc=fitz.open(path)
    (path.with_suffix(".txt")).write_text("\n\f\n".join(page.get_text() for page in doc))
    result.update(pages=len(doc),metadata=doc.metadata,renders=[])
    for number in range(1,len(doc)+1):
        prefix=BASE/"sources"/("algebra_history_trace1961_original_p"+str(number).zfill(3))
        command=["pdftoppm","-f",str(number),"-l",str(number),"-scale-to","2200","-png","-singlefile",str(path),str(prefix)]
        run=subprocess.run(command,capture_output=True,text=True)
        result["renders"].append({"command":command,"returncode":run.returncode,"stdout":run.stdout,"stderr":run.stderr,"file":str(prefix)+".png"})
except Exception as error:result["error"]=repr(error)
result["seconds"]=round(time.monotonic()-start,6)
report={"utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),"result":result}
text=json.dumps(report,indent=2,ensure_ascii=False)
(BASE/"logs"/"algebra_history_retro38.json").write_text(text+"\n")
print(text)
