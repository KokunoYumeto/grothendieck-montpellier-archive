import io, os, sys
from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader, PdfWriter
from pypdf._page import PageObject
class RangeFile(io.RawIOBase):
 def __init__(self,url,size):self.url=url;self.size=size;self.pos=0;self.cache={};self.block=32768;self.bytes=0
 def seekable(self):return True
 def readable(self):return True
 def tell(self):return self.pos
 def seek(self,off,whence=0):
  self.pos=off if whence==0 else self.pos+off if whence==1 else self.size+off
  return self.pos
 def read(self,n=-1):
  if n<0:n=self.size-self.pos
  n=min(n,self.size-self.pos)
  if n<=0:return b''
  first=self.pos//self.block;last=(self.pos+n-1)//self.block
  missing=[i for i in range(first,last+1) if i not in self.cache]
  if missing:
   a=min(missing)*self.block;b=min((max(missing)+1)*self.block,self.size)-1
   print('FETCH',self.url,a,b,'request',n,flush=True)
   with urlopen(Request(self.url,headers={'Range':f'bytes={a}-{b}'}),timeout=30) as r:
    if r.status!=206:raise RuntimeError(f'Range ignored {r.status}')
    raw=r.read()
   print('GOT',len(raw),flush=True)
   self.bytes+=len(raw)
   for i in range(a//self.block,b//self.block+1):self.cache[i]=raw[(i*self.block-a):((i+1)*self.block-a)]
  raw=b''.join(self.cache[i] for i in range(first,last+1))
  a=self.pos-first*self.block;self.pos+=n
  return raw[a:a+n]
 def readinto(self,b):
  x=self.read(len(b));b[:len(x)]=x;return len(x)
def nth(node,n):
 node=node.get_object()
 if node.get('/Type')=='/Page':
  assert n==0
  return node
 for kid in node['/Kids']:
  obj=kid.get_object();count=int(obj.get('/Count',1))
  if n<count:return nth(kid,n)
  n-=count
 raise IndexError(n)
if __name__=='__main__':
 cote=int(sys.argv[1]);pages=list(map(int,sys.argv[2:]));sizes={34:84513436,60:30326787}
 f=RangeFile(f'https://grothendieck.umontpellier.fr/{cote}.pdf',sizes[cote]);r=PdfReader(f,strict=True);root=r.trailer['/Root']['/Pages'];print('Opened',cote,root['/Count'],flush=True)
 for n in pages:
  page_dict=nth(root,n-1);page=PageObject(r,page_dict.indirect_reference)
  ancestor=page_dict
  while ancestor.get('/Parent'):
   ancestor=ancestor['/Parent'].get_object()
   for key in ('/MediaBox','/CropBox','/Resources','/Rotate'):
    if key not in page and key in ancestor:page[key]=ancestor[key]
  w=PdfWriter();w.add_page(page)
  out=Path(f'work/archive_sources/cote{cote}_scan{n}.pdf')
  with out.open('wb') as stream:w.write(stream)
  print('Saved',out,'fetched',f.bytes,flush=True)
