"""Inspect the ordinary public SPA bundle for its advertised article-read routes."""
from pathlib import Path
import re,json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter()
s=(R/'sources/informat_public_bundle.html').read_text()
urls=sorted(set(re.findall(r'https?://[^\s"\'`<>\\]+',s)))
urls=[u for u in urls if 'api' in u.lower() and not any(w in u.lower() for w in ['key=','token=','secret='])]
contexts=[]
for needle in ['baseURL','/articles/','/article/','api.informatics','api/journals','fullText','pdfUrl']:
 for m in list(re.finditer(re.escape(needle),s))[:8]:
  c=s[max(0,m.start()-120):m.end()+180]
  if not re.search(r'api.?key|secret|authorization',c,re.I):contexts.append(dict(needle=needle,context=c))
out=dict(source='public HTML-advertised application bundle, no challenge execution or credentials',bytes=len(s),seconds=time.perf_counter()-start,api_urls=urls,contexts=contexts)
(R/'code/root_pfluger_bundle_paths_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
