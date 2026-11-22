"""Retrieve only selected, explicitly linked early notices; retain exact source discovery."""
from pathlib import Path
import datetime,json,time,urllib.request,hashlib,fitz,re,concurrent.futures
R=Path("RESEARCH_SA23");t=time.monotonic()
old=json.loads((R/"logs/algebra_history_retro36.json").read_text())["result"]["links"]
selected=[4,5,14,65,67]
urls={}
for n in selected:
 match=[x for x in old if x.get("uri") and x["uri"].endswith(f"/AG-{n}.pdf")]
 if len(match)!=1:raise ValueError((n,match))
 urls[n]=match[0]
def get(n):
 item=urls[n];url=item["uri"].replace("http://","https://",1)
 record={"AG_item":n,"discovery":item,"requested_url":url,"started_utc":datetime.datetime.now(datetime.timezone.utc).isoformat()}
 start=time.monotonic()
 try:
  with urllib.request.urlopen(url,timeout=25) as response:
   raw=response.read();record.update(status=response.status,final_url=response.url,content_type=response.headers.get("Content-Type"))
  p=R/f"sources/algebra_earlynotice_AG{n}.pdf";p.write_bytes(raw)
  record.update(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),pdf=str(p.relative_to(R)))
  doc=fitz.open(p);texts=[page.get_text() for page in doc]
  p.with_suffix(".txt").write_text("\n\f\n".join(texts))
  record["pages"]=len(doc);record["text_chars"]=[len(s) for s in texts]
  pat=re.compile(r"trace|\btr\b|spectr|gen[ru]e|fredholm|lidsk|weyl|d[eé]termin|valeurs?\s+propre|manuscrit|in[eé]dit|communi|lettre",re.I)
  record["hits"]=[]
  for i,s in enumerate(texts):
   for m in pat.finditer(s):
    record["hits"].append({"pdf_page":i+1,"term":m.group(),"context":s[max(0,m.start()-160):min(len(s),m.end()+250)]})
  record["renders"]=[]
  for i,page in enumerate(doc):
   im=R/f"sources/algebra_earlynotice_AG{n}_page{i+1:03}.png";page.get_pixmap(matrix=fitz.Matrix(2,2)).save(im)
   record["renders"].append(str(im.relative_to(R)))
 except Exception as e:record["error"]=repr(e)
 record["elapsed_seconds"]=time.monotonic()-start
 return record
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:results=list(pool.map(get,selected))
bib=fitz.open(R/"sources/algebra_history_AG_bibliotex.pdf")
record={"utc_recorded":datetime.datetime.now(datetime.timezone.utc).isoformat(),"selection_source":"Previously opened AG-bibliotex actual PDF annotations, retained in script36 log","bibliography_first_page":bib[0].get_text(),"bibliography_bourbaki_page":bib[3].get_text(),"results":results,"elapsed_seconds":time.monotonic()-t}
s=json.dumps(record,ensure_ascii=False,indent=2);(R/"logs/algebra_earlynotices_fetch65.json").write_text(s+"\n");print(s)

