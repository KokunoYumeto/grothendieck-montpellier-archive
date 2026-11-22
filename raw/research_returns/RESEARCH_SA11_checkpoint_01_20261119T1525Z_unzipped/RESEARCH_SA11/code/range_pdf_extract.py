#!/usr/bin/env python3
"""Extract specified public archival PDF pages using verified HTTP byte ranges."""
import io,urllib.request,pathlib,json,time,sys,re
from pypdf import PdfReader,PdfWriter
ROOT=pathlib.Path(__file__).resolve().parent.parent
class HTTPFile(io.RawIOBase):
 def __init__(self,url,name):
  self.url=url;self.name=name;self.pos=0;self.block=65536;self.cache={};self.log=[]
  req=urllib.request.Request(url,headers={'Range':'bytes=0-0'})
  with urllib.request.urlopen(req,timeout=30) as r:
   cr=r.headers.get('Content-Range','');self.size=int(cr.rsplit('/',1)[1]) if cr else int(r.headers['Content-Length'])
   if r.status!=206:raise RuntimeError('Source did not honor byte ranges')
   r.read(1)
 def seekable(self):return True
 def readable(self):return True
 def tell(self):return self.pos
 def seek(self,offset,whence=0):
  self.pos=offset if whence==0 else self.pos+offset if whence==1 else self.size+offset
  return self.pos
 def get(self,k):
  if k not in self.cache:
   a=k*self.block;b=min(self.size-1,a+self.block-1);t=time.perf_counter()
   req=urllib.request.Request(self.url,headers={'Range':f'bytes={a}-{b}'})
   with urllib.request.urlopen(req,timeout=45) as r:
    if r.status!=206:raise RuntimeError('Source stopped honoring byte ranges')
    v=r.read(self.block+1)
   if len(v)!=b-a+1:raise RuntimeError(('Range length',a,b,len(v)))
   self.cache[k]=v;self.log.append({'start':a,'end':b,'seconds':time.perf_counter()-t})
   print(f'{self.name}: fetched {a}-{b}',flush=True)
  return self.cache[k]
 def read(self,n=-1):
  if n<0:n=self.size-self.pos
  n=min(n,self.size-self.pos)
  if n<=0:return b''
  out=[]
  while n:
   k,off=divmod(self.pos,self.block);v=self.get(k);take=min(n,len(v)-off)
   out.append(v[off:off+take]);self.pos+=take;n-=take
  return b''.join(out)
def main():
 name=sys.argv[1];pages=[int(x) for x in sys.argv[2].split(',')]
 start=time.perf_counter();url=f'https://grothendieck.umontpellier.fr/{name}.pdf'
 f=HTTPFile(url,name);reader=PdfReader(f);writer=PdfWriter()
 for p in pages:writer.add_page(reader.pages[p-1])
 dest=ROOT/'sources'/f'manuscript{name}_selected.pdf'
 with dest.open('wb') as out:writer.write(out)
 report={'url':url,'source_size':f.size,'source_pages':len(reader.pages),'selected_scan_pages':pages,'downloaded_bytes':sum(len(x) for x in f.cache.values()),'elapsed_seconds':time.perf_counter()-start,'ranges':f.log,'output':str(dest)}
 (ROOT/'audit'/f'root_range_{name}.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
