"""Extract selected public-PDF pages by validated HTTP ranges; provenance only."""
import io, urllib.request, pathlib, json, time, hashlib
from pypdf import PdfReader, PdfWriter
import fitz
ROOT=pathlib.Path(__file__).resolve().parents[1]
class RangeFile(io.RawIOBase):
    def __init__(self,url,size,block=65536):
        self.url,self.size,self.block,self.pos=url,size,block,0
        self.cache={};self.requests=[]
    def readable(self):return True
    def seekable(self):return True
    def tell(self):return self.pos
    def seek(self,offset,whence=0):
        self.pos=offset if whence==0 else self.pos+offset if whence==1 else self.size+offset
        return self.pos
    def read(self,n=-1):
        if n<0:raise OSError('Whole-source recovery disabled for selective extraction')
        n=min(n,self.size-self.pos)
        if n<=0:return b''
        parts=[]
        while n:
            idx=self.pos//self.block
            if idx not in self.cache:
                lo=idx*self.block;hi=min(self.size-1,lo+self.block-1)
                cache_dir=ROOT/'literature/A567_cote43_ranges';cache_dir.mkdir(exist_ok=True)
                cache_file=cache_dir/f'{idx:04d}.bin'
                cached=cache_file.exists() and cache_file.stat().st_size==hi-lo+1
                if cached:data=cache_file.read_bytes()
                else:
                    req=urllib.request.Request(self.url,headers={'Range':f'bytes={lo}-{hi}'})
                    for attempt in range(3):
                        try:
                            with urllib.request.urlopen(req,timeout=30) as response:
                                data=response.read();assert response.status==206 and len(data)==hi-lo+1
                                assert response.headers['Content-Range']==f'bytes {lo}-{hi}/{self.size}'
                            break
                        except Exception:
                            if attempt==2:raise
                            time.sleep(1)
                    cache_file.write_bytes(data)
                    print('Fetched source range',lo,hi,flush=True)
                self.cache[idx]=data;self.requests.append([lo,hi,len(data),cached])
            b=self.cache[idx];off=self.pos-idx*self.block;k=min(n,len(b)-off)
            parts.append(b[off:off+k]);self.pos+=k;n-=k
        return b''.join(parts)
start=time.perf_counter();u='https://grothendieck.umontpellier.fr/43.pdf';rf=RangeFile(u,78615706)
r=PdfReader(rf,strict=True);top=r.trailer['/Root']['/Pages'];page_count=int(top['/Count']);print('Page count',page_count,flush=True)
def selected_page(node,index,inherited=None):
    node=node.get_object();inherited=dict(inherited or {})
    for name in ['/Resources','/MediaBox','/CropBox','/Rotate']:
        if name in node:inherited[name]=node[name]
    if node['/Type']=='/Page':
        from pypdf._page import PageObject
        page=PageObject(r,node.indirect_reference)
        page.update(node)
        from pypdf.generic import NameObject
        for key,value in inherited.items():
            if key not in page:page[NameObject(key)]=value
        return page
    if int(node['/Count'])==len(node['/Kids']):
        return selected_page(node['/Kids'][index],0,inherited)
    for ref in node['/Kids']:
        child=ref.get_object();count=int(child.get('/Count',1))
        if index<count:return selected_page(child,index,inherited)
        index-=count
    raise IndexError(index)
w=PdfWriter();folios=[91,92,93,94,95,96,97]
for folio in folios:
    pg=selected_page(top,folio);w.add_page(pg)
    one=PdfWriter();one.add_page(pg);buf=io.BytesIO();one.write(buf)
    (ROOT/f'literature/A567_cote43_folio{folio:03d}_extract.pdf').write_bytes(buf.getvalue())
    doc=fitz.open(stream=buf.getvalue(),filetype='pdf');doc[0].get_pixmap(matrix=fitz.Matrix(1.8,1.8)).save(ROOT/f'qa/A567_cote43_{folio:03d}.png')
    print('Rendered original folio',folio,flush=True)
p=ROOT/'literature/A567_cote_43_folios91_to97_extract.pdf'
with p.open('wb') as f:w.write(f)
d=fitz.open(p)
for i,folio in enumerate(folios):d[i].get_pixmap(matrix=fitz.Matrix(1.8,1.8)).save(ROOT/f'qa/A567_cote43_{folio:03d}.png')
log={'url':u,'source_size':rf.size,'source_pdf_page_count':page_count,'source_folios':folios,'source_pdf_pages':[i+1 for i in folios],'source_ranges_last_flag_is_cache_reuse':rf.requests,'network_bytes_this_run':sum(x[2] for x in rf.requests if not x[3]),'validated_source_bytes_used':sum(x[2] for x in rf.requests),'extract_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'elapsed_seconds':time.perf_counter()-start}
(ROOT/'logs/A567_cote43_91_to97_range_extract.json').write_text(json.dumps(log,indent=2));print(json.dumps(log),flush=True)
