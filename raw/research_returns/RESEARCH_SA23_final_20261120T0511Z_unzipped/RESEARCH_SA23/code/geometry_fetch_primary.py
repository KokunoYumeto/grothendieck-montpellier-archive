"""Retain public primary-source files used in the geometry audit."""
from pathlib import Path
import urllib.request, concurrent.futures, time
root=Path('RESEARCH_SA23/notes')
urls={
'geometry_Weyl1949_p408.png':'https://cdn.ncbi.nlm.nih.gov/pmc/blobs/eef2/1063049/5476cfccf96b/pnas01544-0068.png',
'geometry_Weyl1949_p409.png':'https://cdn.ncbi.nlm.nih.gov/pmc/blobs/eef2/1063049/0d86e07dd6a1/pnas01544-0069.png',
'geometry_Weyl1949_p410.png':'https://cdn.ncbi.nlm.nih.gov/pmc/blobs/eef2/1063049/3ddeeed296b9/pnas01544-0070.png',
'geometry_Weyl1949_p411.png':'https://cdn.ncbi.nlm.nih.gov/pmc/blobs/eef2/1063049/2eb046f61f22/pnas01544-0071.png'}
def run(pair):
 name,url=pair;t=time.monotonic();p=root/name
 try:
  if p.exists():return name,'retained',p.stat().st_size
  data=urllib.request.urlopen(url,timeout=30).read();p.write_bytes(data)
  return name,len(data),round(time.monotonic()-t,3),url
 except Exception as e:return name,type(e).__name__,str(e),url
for r in concurrent.futures.ThreadPoolExecutor(max_workers=4).map(run,urls.items()):print(r,flush=True)
