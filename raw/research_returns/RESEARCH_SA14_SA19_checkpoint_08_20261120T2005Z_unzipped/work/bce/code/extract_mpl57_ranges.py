import io, os, json, time, urllib.request
from pypdf import PdfReader, PdfWriter
URL='https://grothendieck.umontpellier.fr/57.pdf'
SIZE=129262979
BLOCK=131072
CACHE='work/bce/sources/mpl57_range_cache'
os.makedirs(CACHE,exist_ok=True)
class Remote(io.RawIOBase):
    def __init__(self):self.pos=0;self.cache={};self.requests=[]
    def readable(self):return True
    def seekable(self):return True
    def tell(self):return self.pos
    def seek(self,offset,whence=0):
        self.pos=offset if whence==0 else self.pos+offset if whence==1 else SIZE+offset
        return self.pos
    def read(self,n=-1):
        if n<0:n=SIZE-self.pos
        n=min(n,SIZE-self.pos)
        out=[]
        while n>0:
            b=self.pos//BLOCK
            if b not in self.cache:
                lo=b*BLOCK;hi=min(SIZE-1,lo+BLOCK-1)
                req=urllib.request.Request(URL,headers={'Range':f'bytes={lo}-{hi}'})
                cachepath=f'{CACHE}/{b}.bin'
                if os.path.exists(cachepath):
                    self.cache[b]=open(cachepath,'rb').read()
                else:
                    for attempt in range(4):
                        try:
                            with urllib.request.urlopen(req,timeout=30) as r:
                                if r.status!=206:raise RuntimeError(('range ignored',r.status))
                                self.cache[b]=r.read()
                            open(cachepath,'wb').write(self.cache[b]);break
                        except Exception as e:
                            print('retry',b,attempt,type(e).__name__,flush=True)
                            if attempt==3:raise
                self.requests.append([lo,hi,len(self.cache[b])])
            data=self.cache[b];start=self.pos%BLOCK;take=min(n,len(data)-start)
            if take<=0:break
            out.append(data[start:start+take]);self.pos+=take;n-=take
        return b''.join(out)
r=Remote();started=time.time();reader=PdfReader(r,strict=True)
rootpages=reader.trailer['/Root']['/Pages']
count=int(rootpages['/Count']);print('pages',count,flush=True)
from pypdf._page import PageObject
chosen=[]
def select(obj,base=0,inherited=None):
    inherited=dict(inherited or {})
    for key in ['/Resources','/MediaBox','/CropBox','/Rotate']:
        if key in obj:inherited[key]=obj.raw_get(key)
    if obj['/Type']=='/Page':
        if base+1 in range(309,316):
            page=PageObject(reader, obj.indirect_reference);page.update(obj)
            for key,value in inherited.items():
                if key not in page:page[key]=value
            chosen.append(page);print('selected original scan',base+1,flush=True)
        return
    for kidref in obj['/Kids']:
        kid=kidref.get_object();n=int(kid.get('/Count',1))
        if base<315 and base+n>=309:select(kid,base,inherited)
        base+=n
select(rootpages)
w=PdfWriter()
for page in chosen:w.add_page(page)
out='work/bce/sources/MPL57_scans309-315_original.pdf'
w.write(out)
meta={'url':URL,'total_bytes':SIZE,'pdf_pages':count,'selected_one_based_pages':list(range(309,316)),'range_requests':r.requests,'transferred_bytes':sum(x[2] for x in r.requests),'elapsed_seconds':time.time()-started,'output':out}
open('work/bce/code/extract_mpl57_ranges.output.json','w').write(json.dumps(meta,indent=2))
print(json.dumps(meta),flush=True)
