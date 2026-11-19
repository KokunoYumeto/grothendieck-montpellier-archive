"""Extract only scans used in Part B, via HTTP byte ranges, to temporary storage."""
import io,json,time,urllib.request
from pathlib import Path
from pypdf import PdfReader,PdfWriter

URL='https://grothendieck.umontpellier.fr/129.pdf'
CACHE=Path('/workspace/scratch/b00be283d10d/fetched/B/129_ranges')
CACHE.mkdir(parents=True,exist_ok=True)

class Remote(io.RawIOBase):
    chunk=262144
    def __init__(self):
        with urllib.request.urlopen(urllib.request.Request(URL,method='HEAD'),timeout=20) as r:
            self.size=int(r.headers['Content-Length'])
        self.pos=0
        self.cache={}
    def readable(self):return True
    def seekable(self):return True
    def tell(self):return self.pos
    def seek(self,pos,whence=0):
        self.pos=pos if whence==0 else self.pos+pos if whence==1 else self.size+pos
        return self.pos
    def read(self,n=-1):
        if n<0:n=self.size-self.pos
        n=max(0,min(n,self.size-self.pos))
        result=[]
        while n:
            c=self.pos//self.chunk
            if c not in self.cache:
                p=CACHE/f'{c:04}.bin'
                if p.exists():data=p.read_bytes()
                else:
                    start=c*self.chunk;end=min(start+self.chunk,self.size)-1
                    request=urllib.request.Request(URL,headers={'Range':f'bytes={start}-{end}'})
                    with urllib.request.urlopen(request,timeout=30) as r:
                        assert r.status==206
                        data=r.read()
                    p.write_bytes(data)
                    print(json.dumps({'range':[start,end],'bytes':len(data)}),flush=True)
                self.cache[c]=data
            data=self.cache[c];offset=self.pos%self.chunk
            take=min(n,len(data)-offset)
            assert take>0
            result.append(data[offset:offset+take]);self.pos+=take;n-=take
        return b''.join(result)

started=time.monotonic()
reader=PdfReader(Remote());writer=PdfWriter()
for p in [93,113,114]:writer.add_page(reader.pages[p])
out=CACHE.parent/'129_selected.pdf'
with out.open('wb') as h:writer.write(h)
print(json.dumps({'pages':[94,114,115],'output':str(out),'seconds':time.monotonic()-started}),flush=True)
