"""Follow Cartier211's explicit reference [1]; inspect local Cartier text too."""
from pathlib import Path
import datetime,time,hashlib,json,re,urllib.request,fitz
R=Path("RESEARCH_SA23");t=time.monotonic()
out={"started_utc":datetime.datetime.now(datetime.timezone.utc).isoformat()}
p=R/"sources/algebra_cartier211_facsimile.pdf";d=fitz.open(p)
pat=re.compile(r"grothendieck|\btr\b|trace|genre|fredholm|lidsk|weyl|lettre|communi|manuscrit|in[eé]dit",re.I)
out["cartier_corrected_pattern_note"]="The exploratory pattern in script61 over-escaped the tr word boundary; this local pass corrects it. All14 original text pages were independently displayed/read, so search counts are only an aid."
out["cartier_visual_pages"]={"pdf_pages":list(range(2,16)),"printed_pages":list(range(85,99))}
out["cartier_hits"]=[]
for i,page in enumerate(d):
 s=page.get_text()
 for m in pat.finditer(s):out["cartier_hits"].append({"pdf_page":i+1,"term":m.group(),"context":s[max(0,m.start()-100):min(len(s),m.end()+180)]})
url="https://www.jstage.jst.go.jp/article/kodaimath1949/9/4/9_4_161/_pdf/-char/en"
out["amemiya_shiga"]={"url":url,"discovery":"Download PDF link149 on the opened J-STAGE9(4) issue; web reader timed out, no access refusal observed."}
a=out["amemiya_shiga"]
try:
 with urllib.request.urlopen(url,timeout=25) as response:
  raw=response.read();a.update(status=response.status,final_url=response.url,content_type=response.headers.get("Content-Type"))
 a.update(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
 dest=R/"sources/algebra_amemiya_shiga1957.pdf";dest.write_bytes(raw);doc=fitz.open(dest)
 texts=[page.get_text() for page in doc];dest.with_suffix(".txt").write_text("\n\f\n".join(texts))
 a["pages"]=len(doc);a["hits"]=[]
 for i,s in enumerate(texts):
  for m in re.finditer(r"grothendieck|trace|genus|lidsk|weyl|communicat|letter|manuscript|unpublished|receiv|thank",s,re.I):
   a["hits"].append({"pdf_page":i+1,"term":m.group(),"context":s[max(0,m.start()-150):min(len(s),m.end()+250)]})
 selected=sorted(set([0,len(doc)-1]+[h["pdf_page"]-1 for h in a["hits"]]))
 a["renders"]=[]
 for i in selected:
  im=R/f"sources/algebra_amemiya_shiga1957_page{i+1:03}.png";doc[i].get_pixmap(matrix=fitz.Matrix(2,2)).save(im);a["renders"].append(str(im.relative_to(R)))
except Exception as e:a["error"]=repr(e)
out["elapsed_seconds"]=time.monotonic()-t
s=json.dumps(out,ensure_ascii=False,indent=2);(R/"logs/algebra_cartier_follow62.json").write_text(s+"\n");print(s)

