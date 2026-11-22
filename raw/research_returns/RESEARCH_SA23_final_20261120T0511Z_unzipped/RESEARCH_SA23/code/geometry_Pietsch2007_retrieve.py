from pathlib import Path
import hashlib,json,time,re,urllib.request
import fitz
base=Path("/workspace/scratch/a7ef7e55112c/RESEARCH_SA23")
dest=base/"notes/geometry_Pietsch2007.pdf"
url="https://susanka.org/HSforQM/%5BPietsch%5D_History_of_Banach_Spaces_and_Linear_Operators.pdf"
started=time.time()
with urllib.request.urlopen(url, timeout=50) as response:
    data=response.read()
    status=response.status
dest.write_bytes(data)
doc=fitz.open(dest)
texts=[p.get_text() for p in doc]
(base/"notes/geometry_Pietsch2007_full.txt").write_text("\n\f\n".join(texts))
needles=["Lidski", "personal communication", "unpublished", "Grothendieck", "letter"]
hits={word:[{"pdf_page":i+1,"text":t} for i,t in enumerate(texts) if word.lower() in t.lower()] for word in needles}
(base/"logs/geometry_Pietsch2007_hits.json").write_text(json.dumps(hits,ensure_ascii=False,indent=2))
selected=[424,425,437,438,713,779,800,643]
out=base/"notes/geometry_Pietsch2007_pages"
out.mkdir(exist_ok=True)
for index in selected:
    page=doc[index]
    (out/f"pdfindex_{index:03}.txt").write_text(texts[index])
    page.get_pixmap(matrix=fitz.Matrix(1.8,1.8)).save(out/f"pdfindex_{index:03}.png")
log={"url":url,"http_status":status,"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest(),"pdf_pages":len(doc),"selected_zero_based_pages":selected,"elapsed_seconds":time.time()-started,"keyword_page_counts":{k:len(v) for k,v in hits.items()}}
(base/"logs/geometry_Pietsch2007_retrieval.json").write_text(json.dumps(log,ensure_ascii=False,indent=2))
print(json.dumps(log))

