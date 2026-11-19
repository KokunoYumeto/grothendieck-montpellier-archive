"""Extract selected pages of a public linearized PDF by HTTP range requests.

Needed when the official high-resolution PDF streams slowly. This retrieves
only referenced objects. Source images are kept outside deliverables.
"""
import io,sys
from urllib.request import Request,urlopen
from pathlib import Path
from pypdf import PdfReader,PdfWriter,PageObject

class RangeFile(io.RawIOBase):
    def __init__(self,url):
        self.url=url
        with urlopen(Request(url,method='HEAD'),timeout=30) as r:
            self.n=int(r.headers['Content-Length'])
        self.pos=0; self.cache={}; self.block=65536
    def seekable(self): return True
    def readable(self): return True
    def tell(self): return self.pos
    def seek(self,offset,whence=0):
        self.pos=offset if whence==0 else self.pos+offset if whence==1 else self.n+offset
        return self.pos
    def read(self,n=-1):
        if n<0: n=self.n-self.pos
        n=min(n,self.n-self.pos)
        if n<=0: return b''
        a=self.pos; b=a+n
        result=[]
        while a<b:
            ix=a//self.block
            start=ix*self.block; end=min(start+self.block,self.n)-1
            if ix not in self.cache:
                with urlopen(Request(self.url,headers={'Range':f'bytes={start}-{end}'}),timeout=30) as r:
                    data=r.read()
                    assert r.status==206 and len(data)==end-start+1,(r.status,len(data),start,end)
                self.cache[ix]=data
                print('block',ix,'bytes',len(data),flush=True)
            c=min(end+1,b)
            result.append(self.cache[ix][a-start:c-start]); a=c
        self.pos=b
        return b''.join(result)

def page_at(node,index):
    node=node.get_object()
    if node['/Type']=='/Page':
        assert index==0
        return node
    for kidref in node['/Kids']:
        kid=kidref.get_object()
        count=int(kid.get('/Count',1))
        if index<count:
            return page_at(kid,index)
        index-=count
    raise IndexError(index)

if __name__=='__main__':
    url,out,*page_numbers=sys.argv[1:]
    r=PdfReader(RangeFile(url),strict=True)
    w=PdfWriter()
    for p in page_numbers:
        q=page_at(r.trailer['/Root']['/Pages'],int(p)-1)
        page=PageObject(r)
        page.update(q)
        page.indirect_reference=q.indirect_reference
        w.add_page(page,excluded_keys=['/Annots'])
    with Path(out).open('wb') as f:w.write(f)
    print('saved',out,flush=True)
