"""Resolve public links actually embedded in the Grothendieck Circle bibliography."""
import hashlib,json,time,urllib.request
from pathlib import Path
import fitz
BASE=Path(__file__).resolve().parents[1]
url="https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG-bibliotex.pdf"
start=time.monotonic()
result={"url":url}
try:
    with urllib.request.urlopen(url,timeout=25) as response:
        data=response.read()
        path=BASE/"sources"/"algebra_history_AG_bibliotex.pdf"
        path.write_bytes(data)
        result.update(status=response.status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),file=str(path))
    doc=fitz.open(path); links=[]
    for index,page in enumerate(doc,1):
        for link in page.get_links():
            rect=fitz.Rect(link["from"]); rect.x0=0
            rect.y0-=12;rect.y1+=12
            links.append({"physical_pdf_page":index,"nearby_text":page.get_textbox(rect),"uri":link.get("uri"),"kind":link["kind"]})
    result.update(pages=len(doc),links=links)
except Exception as error: result["error"]=repr(error)
result["seconds"]=round(time.monotonic()-start,6)
report={"utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime()),"result":result}
text=json.dumps(report,indent=2,ensure_ascii=False)
(BASE/"logs"/"algebra_history_retro36.json").write_text(text+"\n")
print(text)
