"""Obtain Samuel's original ICM paper from the official proceedings.

The web tool rejected the complete volume at 74705952 bytes; try the old
individual-paper locator before obtaining the volume and extracting pp470-487.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time
import urllib.request
import fitz

ROOT=Path(__file__).resolve().parents[1]
out=ROOT/"output/fetch_samuel_source.json"
urls=[
    "https://www.mathunion.org/ICM/ICM1958/Main/icm1958.0470.0487.ocr.pdf",
    "https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1958/ICM1958.ocr.pdf",
]
record={"utc":datetime.now(timezone.utc).isoformat(),"web_attempts":[
    "Full official volume rejected by web retrieval because content length74705952 exceeds limit",
    "Old individual-paper official locator inaccessible in web retrieval",
],"attempts":[]}
start=time.perf_counter()
for i,url in enumerate(urls):
    attempt={"url":url}
    try:
        request=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
        with urllib.request.urlopen(request,timeout=35) as response:
            data=response.read()
        if not data.startswith(b"%PDF"):
            raise ValueError("Response is not PDF")
        attempt.update(status="downloaded",bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        path=ROOT/"sources"/("Samuel1960.pdf" if i==0 else "ICM1958_full.pdf")
        path.write_bytes(data)
        doc=fitz.open(path)
        if i==1:
            matches=[]
            for index in range(430,min(550,len(doc))):
                text=doc[index].get_text().upper()
                if "SAMUEL" in text and "RELATIONS" in text and "470" in text:
                    matches.append(index)
            if len(matches)!=1:
                raise ValueError(f"Did not uniquely locate Samuel first page: {matches}")
            begin=matches[0]
            article=fitz.open()
            article.insert_pdf(doc,from_page=begin,to_page=begin+17)
            path=ROOT/"sources/Samuel1960.pdf"
            article.save(path)
            record["extracted_pdf_pages_one_based"]=[begin+1,begin+18]
        txt=ROOT/"sources/Samuel1960.txt"
        conversion=subprocess.run(["pdftotext","-layout",str(path),str(txt)],capture_output=True,text=True)
        record.update(article_pdf=str(path),article_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),article_bytes=path.stat().st_size,text=str(txt),pdftotext_exit=conversion.returncode)
        record["attempts"].append(attempt)
        break
    except Exception as exc:
        attempt.update(status="failed",error=f"{type(exc).__name__}: {exc}")
        record["attempts"].append(attempt)
record["elapsed_seconds"]=time.perf_counter()-start
out.write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps(record,indent=2))
