from pathlib import Path
import urllib.request,json,time,re
R=Path(__file__).resolve().parents[1];T=time.perf_counter();u='https://gdz.sub.uni-goettingen.de/id/PPN252457811_1907'
out={'url':u}
try:
 with urllib.request.urlopen(u,timeout=40) as f:b=f.read();out.update(status=f.status,bytes=len(b))
 (R/'sources/gdz_1907_landing.html').write_bytes(b)
 out['links']=[x for x in re.findall(r'https?[^\s<>\"\']+',b.decode(errors='replace')) if any(w in x.lower() for w in ['iiif','manifest','pdf','mets'])]
except Exception as e:out['error']=repr(e)
out['seconds']=time.perf_counter()-T
(R/'code/root_gdz_discovery_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
