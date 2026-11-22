import concurrent.futures, pathlib, time, urllib.request
SOURCES = {
    "KatzMessing1974.pdf": "https://www.math.mcgill.ca/goren/SeminarOnCohomology/Katz-Messing.pdf",
    "NakkajimaYobuko2022.pdf": "https://arxiv.org/pdf/1902.09110",
    "LiLiu2022.pdf": "https://arxiv.org/pdf/2204.03411",
    "SGA2.pdf": "https://wstein.org/sga/SGA2/sga2-smf.pdf",
}
root=pathlib.Path(__file__).resolve().parents[1]/"references"
root.mkdir(exist_ok=True)
def fetch(item):
 name,url=item; start=time.monotonic()
 try:
  if (root/name).exists(): return f"{name}\tCACHED\t{(root/name).stat().st_size} bytes\t{url}"
  with urllib.request.urlopen(url, timeout=30) as r: data=r.read()
  if not data.startswith(b"%PDF"): raise ValueError("not PDF")
  (root/name).write_bytes(data)
  return f"{name}\t{len(data)} bytes\t{time.monotonic()-start:.3f}s\t{url}"
 except Exception as exc: return f"{name}\tFAILED\t{time.monotonic()-start:.3f}s\t{exc}"
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 out="\n".join(pool.map(fetch,SOURCES.items()))
print(out)
with (root.parent/"outputs"/"fetch_sources.txt").open('a') as log: log.write(out+"\n")
