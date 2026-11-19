import concurrent.futures, datetime, hashlib, json, pathlib, subprocess, time, urllib.request
ROOT=pathlib.Path(__file__).resolve().parents[1]
SOURCES={
 "BlochEsnaultKerz2014": "https://page.mi.fu-berlin.de/esnault/preprints/helene/112-bek.pdf",
 "CortinasHaesemeyerWeibel2009": "https://arxiv.org/pdf/math/0703133",
}
def fetch(item):
 name,url=item; started=time.perf_counter(); target=ROOT/"sources"/(name+".pdf")
 data=urllib.request.urlopen(url,timeout=50).read(); assert data.startswith(b"%PDF")
 target.write_bytes(data)
 subprocess.run(["pdftotext","-layout",str(target),str(target.with_suffix(".txt"))],check=True)
 return {"name":name,"url":url,"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest(),"runtime_seconds":time.perf_counter()-started,"path":str(target)}
start=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 results=list(pool.map(fetch,SOURCES.items()))
report={"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"runtime_seconds":time.perf_counter()-start,"sources":results}
s=json.dumps(report,indent=2); (ROOT/"output/fetch_product_curve_sources.json").write_text(s+"\n"); (ROOT/"output/fetch_product_curve_sources.out").write_text(s+"\n"); print(s)
