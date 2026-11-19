"""Render exact source pages used in the remaining generation-gate audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import fitz

ROOT=Path(__file__).resolve().parents[1]
requests={
    "Samuel1960": [(7,477),(9,479),(12,482)],
    "Peters2026Incidence": [(2,3),(14,15)],
    "Saito1979": [(5,100),(16,111)],
    "Pelaez2026": [(5,6),(6,7),(8,9)],
}
records=[]
for name,pages in requests.items():
    doc=fitz.open(ROOT/"sources"/(name+".pdf"))
    for index,printed in pages:
        output=ROOT/"output"/f"{name}_printed{printed}.png"
        doc[index].get_pixmap(matrix=fitz.Matrix(1.65,1.65)).save(output)
        records.append({"source":name,"pdf_page_one_based":index+1,"printed_page":printed,"output":str(output),"sha256":hashlib.sha256(output.read_bytes()).hexdigest()})
result={"utc":datetime.now(timezone.utc).isoformat(),"renders":records}
(ROOT/"output/render_generation_sources.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"rendered_pages":len(records),"utc":result["utc"]}))
