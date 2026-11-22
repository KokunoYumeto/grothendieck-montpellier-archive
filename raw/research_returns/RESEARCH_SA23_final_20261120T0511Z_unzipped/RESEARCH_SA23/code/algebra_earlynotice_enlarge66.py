"""Enlarge original CR1951 header and record source page geometry, without changing content."""
from pathlib import Path
import fitz,json,datetime,time,hashlib
R=Path("RESEARCH_SA23");t=time.monotonic();p=R/"sources/algebra_earlynotice_AG5.pdf";d=fitz.open(p);page=d[1];r=page.rect
spec=[("header",(.30,.035,.73,.09)),("announcement",(.16,.325,.84,.444))]
out={"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"source":str(p.relative_to(R)),"source_sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"pdf_page":2,"printed_page":1557,"page_rect":list(r),"clips":[]}
for label,(x0,y0,x1,y1) in spec:
 clip=fitz.Rect(x0*r.width,y0*r.height,x1*r.width,y1*r.height)
 dest=R/f"sources/algebra_earlynotice_AG5_{label}_enlarged.png"
 page.get_pixmap(matrix=fitz.Matrix(4,4),clip=clip).save(dest)
 out["clips"].append({"label":label,"rect":list(clip),"path":str(dest.relative_to(R))})
out["elapsed_seconds"]=time.monotonic()-t
s=json.dumps(out,indent=2);(R/"logs/algebra_earlynotice_enlarge66.json").write_text(s+"\n");print(s)

