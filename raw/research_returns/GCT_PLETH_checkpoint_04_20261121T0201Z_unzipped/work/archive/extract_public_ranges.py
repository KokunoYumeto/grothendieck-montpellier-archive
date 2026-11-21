"""Download specified original scan pages using ordinary HTTP byte ranges."""
import io, urllib.request, concurrent.futures, pathlib, json, sys, time
from pypdf import PdfReader, PdfWriter
from pypdf._page import PageObject
from pypdf.generic import NameObject
BASE=pathlib.Path(__file__).parent/'public_scans'
class Remote(io.RawIOBase):
    def __init__(self,cote):
        self.url=f'https://grothendieck.umontpellier.fr/{cote}.pdf'
        self.root=BASE/'ranges'/str(cote);self.root.mkdir(parents=True,exist_ok=True)
        with urllib.request.urlopen(urllib.request.Request(self.url,method='HEAD'),timeout=20) as r:self.size=int(r.headers['Content-Length'])
        self.pos=0;self.block=65536
    def readable(self):return True
    def seekable(self):return True
    def tell(self):return self.pos
    def seek(self,offset,whence=0):
        self.pos=offset if whence==0 else self.pos+offset if whence==1 else self.size+offset
        return self.pos
    def get(self,i):
        p=self.root/f'{i:06}.bin'
        a=i*self.block;b=min(self.size-1,a+self.block-1)
        if p.exists() and p.stat().st_size==b-a+1:return p.read_bytes()
        req=urllib.request.Request(self.url,headers={'Range':f'bytes={a}-{b}'})
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req,timeout=30) as r:
                    data=r.read()
                    if r.status!=206 or len(data)!=b-a+1:raise IOError(f'bad range {r.status}, bytes {len(data)}')
                p.write_bytes(data);return data
            except Exception:
                if attempt==2:raise
    def read(self,n=-1):
        if n<0:n=self.size-self.pos
        end=min(self.size,self.pos+n)
        if end<=self.pos:return b''
        lo=self.pos//self.block;hi=(end-1)//self.block
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
            data=b''.join(ex.map(self.get,range(lo,hi+1)))
        out=data[self.pos-lo*self.block:end-lo*self.block];self.pos=end;return out
def main(cote,pages):
    t=time.time();r=Remote(cote);p=PdfReader(r,strict=True)
    root=p.root_object.raw_get('/Pages')
    def selected(ref,index,inherit):
        node=ref.get_object();inherit=dict(inherit)
        for k in ['/Resources','/MediaBox','/CropBox','/Rotate']:
            if k in node:inherit[k]=node.raw_get(k)
        if '/Kids' not in node:
            if index:raise IndexError(index)
            page=PageObject(p,ref);page.update(node)
            for k,v in inherit.items():
                if k not in page:page[NameObject(k)]=v
            return page
        kids=node['/Kids'];count=int(node['/Count'])
        if len(kids)==count:return selected(kids[index],0,inherit)
        for kid in kids:
            child=kid.get_object();n=int(child.get('/Count',1))
            if index<n:return selected(kid,index,inherit)
            index-=n
        raise IndexError(index)
    print(json.dumps({'cote':cote,'total_pages':int(root.get_object()['/Count']),'requested':pages}),flush=True)
    for j in pages:
        w=PdfWriter();w.add_page(selected(root,j-1,{}));out=BASE/f'{cote}-original-p{j:03}.pdf'
        with out.open('wb') as f:w.write(f)
        print(json.dumps({'cote':cote,'page':j,'file':str(out),'elapsed_seconds':round(time.time()-t,2)}),flush=True)
if __name__=='__main__':main(int(sys.argv[1]),[int(x) for x in sys.argv[2:]])
