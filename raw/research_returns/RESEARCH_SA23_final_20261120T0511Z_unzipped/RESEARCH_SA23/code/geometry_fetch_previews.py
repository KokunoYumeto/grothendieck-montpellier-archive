from pathlib import Path
import urllib.request,time,concurrent.futures
urls={
'geometry_FC_googlebook.html':'https://books.google.com/books?id=qJr6CAAAQBAJ&pg=PA3',
'geometry_FC_googlebook_old.html':'https://books.google.com/books?id=jWPT4gQF3oMC&pg=PA3',
'geometry_Raynaud_specialisation.pdf':'https://www.numdam.org/item/PMIHES_1970__38__27_0.pdf'}
def f(it):
 n,u=it;t=time.monotonic();p=Path('RESEARCH_SA23/notes')/n
 try:
  if p.exists():return n,'retained',p.stat().st_size
  d=urllib.request.urlopen(u,timeout=25).read();p.write_bytes(d);return n,len(d),round(time.monotonic()-t,2)
 except Exception as e:return n,type(e).__name__,str(e)
for r in concurrent.futures.ThreadPoolExecutor(max_workers=3).map(f,urls.items()):print(r,flush=True)
