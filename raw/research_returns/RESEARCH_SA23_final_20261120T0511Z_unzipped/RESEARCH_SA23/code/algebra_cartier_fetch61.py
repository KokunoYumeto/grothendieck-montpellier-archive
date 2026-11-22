"""Retrieve the exact Cartier reference cited in Grothendieck's proof addition."""
from pathlib import Path
import urllib.request,datetime,time,hashlib,json,fitz,re
R=Path("RESEARCH_SA23");start=time.monotonic()
url="https://www.numdam.org/article/SB_1960-1961__6__85_0.pdf"
out={"started_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"url":url}
try:
 with urllib.request.urlopen(url,timeout=25) as response:
  raw=response.read();out.update(status=response.status,final_url=response.url,content_type=response.headers.get("Content-Type"))
 out.update(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
 p=R/"sources/algebra_cartier211_facsimile.pdf";p.write_bytes(raw)
 d=fitz.open(p);texts=[page.get_text() for page in d];p.with_suffix(".txt").write_text("\n\f\n".join(texts))
 pages=[]
 for i,page in enumerate(d):
  dest=R/f"sources/algebra_cartier211_page{i+1:03}.png"
  page.get_pixmap(matrix=fitz.Matrix(2,2)).save(dest)
  pages.append({"pdf_page":i+1,"image":str(dest.relative_to(R)),"text_chars":len(texts[i])})
 out.update(pages=len(d),renders=pages,search_hits=[])
 pattern=re.compile(r"grothendieck|trace|tr\\b|genre|fredholm|lidsk|weyl|lettre|communi|manuscrit|in[eé]dit",re.I)
 for i,txt in enumerate(texts):
  for match in pattern.finditer(txt):
   out["search_hits"].append({"pdf_page":i+1,"term":match.group(),"context":txt[max(0,match.start()-130):min(len(txt),match.end()+240)]})
except Exception as e:out["error"]=repr(e)
out["elapsed_seconds"]=time.monotonic()-start
s=json.dumps(out,ensure_ascii=False,indent=2);(R/"logs/algebra_cartier_fetch61.json").write_text(s+"\n");print(s)

