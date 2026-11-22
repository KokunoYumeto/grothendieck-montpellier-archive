from pathlib import Path
import urllib.request, concurrent.futures, time
base=Path(__file__).resolve().parents[1]/'literature'
items={
 'C_cote68.pdf':'https://grothendieck.umontpellier.fr/68.pdf',
 'C_EGA_IV4.pdf':'https://www.numdam.org/item/PMIHES_1967__32__5_0.pdf',
 'C_Madiman_Wang_Woo.pdf':'https://arxiv.org/pdf/1710.00812',
 'C_Madiman_Wang_Woo.source':'https://arxiv.org/src/1710.00812',
}
def get(item):
 name,url=item;p=base/name;t=time.monotonic()
 if p.exists():return {'name':name,'existing':True,'bytes':p.stat().st_size}
 try:
  with urllib.request.urlopen(url,timeout=45) as r:b=r.read()
  p.write_bytes(b)
  return {'name':name,'url':url,'bytes':len(b),'seconds':round(time.monotonic()-t,3)}
 except Exception as e:return {'name':name,'url':url,'error':repr(e),'seconds':round(time.monotonic()-t,3)}
if __name__=='__main__':
 for x in concurrent.futures.ThreadPoolExecutor(max_workers=4).map(get,items.items()):print(x,flush=True)
