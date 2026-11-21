"""Extract selected official facsimile pages using verified HTTP byte ranges.

This reads source bytes without downloading every large manuscript volume.
External PDF/image evidence stays outside the redistribution directory.
"""
from pathlib import Path
import io, json, hashlib, urllib.request, concurrent.futures, threading, datetime, sys
from pypdf import PdfReader,PdfWriter
from pypdf._page import PageObject
import fitz
ROOT=Path(__file__).resolve().parents[2]
EVIDENCE=ROOT.parent/'external_sources'/'Grothendieck_other_evidence'
EVIDENCE.mkdir(parents=True,exist_ok=True)

class RangeReader(io.RawIOBase):
    def __init__(self,url,size,tag):
        self.url=url;self.size=size;self.pos=0;self.block=262144
        self.cache={};self.logs=[];self.tag=tag
        self.dir=EVIDENCE/('ranges_'+tag);self.dir.mkdir(exist_ok=True)
    def readable(self):return True
    def seekable(self):return True
    def tell(self):return self.pos
    def seek(self,offset,whence=0):
        new=offset if whence==0 else self.pos+offset if whence==1 else self.size+offset
        if new<0:raise ValueError('negative seek')
        self.pos=new;return new
    def getblock(self,i):
        if i in self.cache:return self.cache[i]
        a=i*self.block;b=min(self.size,a+self.block)-1
        path=self.dir/f'{a}_{b}.bin'
        if path.exists():data=path.read_bytes()
        else:
            for attempt in range(3):
                try:
                    req=urllib.request.Request(self.url,headers={'Range':f'bytes={a}-{b}'})
                    with urllib.request.urlopen(req,timeout=45) as r:
                        assert r.status==206,(r.status,a,b)
                        assert r.headers.get('Content-Range')==f'bytes {a}-{b}/{self.size}'
                        data=r.read()
                    assert len(data)==b-a+1,(len(data),a,b)
                    path.write_bytes(data);break
                except Exception:
                    if attempt==2:raise
        assert len(data)==b-a+1
        self.cache[i]=data
        self.logs.append({'first':a,'last':b,'sha256':hashlib.sha256(data).hexdigest()})
        return data
    def read(self,n=-1):
        if n is None or n<0:n=self.size-self.pos
        n=min(n,max(0,self.size-self.pos))
        if n>16*1024*1024:raise RuntimeError(f'Refusing unexpectedly broad read of {n} bytes')
        if not n:return b''
        a=self.pos;b=a+n
        ids=list(range(a//self.block,(b-1)//self.block+1))
        missing=[i for i in ids if i not in self.cache]
        if len(missing)>1:
            with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(self.getblock,missing))
        elif missing:self.getblock(missing[0])
        data=b''.join(self.cache[i] for i in ids)
        out=data[a%self.block:a%self.block+n]
        self.pos=b;return out

def choose_page(node,index):
    node=node.get_object()
    if node['/Type']=='/Page':
        assert index==0
        return node
    kids=node['/Kids'];count=int(node['/Count'])
    if count==len(kids):return choose_page(kids[index],0)
    for kid in kids:
        obj=kid.get_object();sub=1 if obj['/Type']=='/Page' else int(obj['/Count'])
        if index<sub:return choose_page(obj,index)
        index-=sub
    raise IndexError(index)

def extract(row,page_number):
    cote=row['cote'];rr=RangeReader(row['url'],row['bytes'],str(cote))
    reader=PdfReader(rr,strict=True)
    pages=reader.trailer['/Root']['/Pages']
    original=choose_page(pages,page_number-1)
    page=PageObject(reader,original.indirect_reference);page.update(original)
    parent=original
    while '/Parent' in parent:
        parent=parent['/Parent']
        for attr in ('/Resources','/MediaBox','/CropBox','/Rotate'):
            if attr not in page and attr in parent:page[attr]=parent.raw_get(attr)
    target=EVIDENCE/f'cote{cote}_scan{page_number:03d}.pdf'
    w=PdfWriter();w.add_page(page);w.write(target)
    d=fitz.open(target);assert len(d)==1
    img=target.with_suffix('.png');d[0].get_pixmap(matrix=fitz.Matrix(2.1,2.1),alpha=False).save(img)
    result={'cote':cote,'scan':page_number,'url':row['url'],'source_bytes':row['bytes'],'source_etag':row['etag'],'source_last_modified':row['last_modified'],'source_pdf_pages':int(pages['/Count']),'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'extracted_pdf':str(target),'extracted_pdf_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'retrieved_bytes':sum(len(v) for v in rr.cache.values()),'source_ranges':sorted(rr.logs,key=lambda x:x['first']),'note':'Only selected source byte ranges retrieved; full-source SHA256 not claimed. Extracted page rendered; visual reading recorded separately.'}
    (ROOT/'agents/archive'/f'ORIGINAL_cote{cote}_scan{page_number:03d}_manifest.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='source_ranges'}),flush=True)
    return result

if __name__=='__main__':
    pages={2:17,12:41,43:37,119:217,4:7,16:38,79:51,89:18}
    rows=json.loads((ROOT/'agents/archive/OTHER_COTES_SOURCE_MANIFEST.json').read_text())
    selected={int(x) for x in sys.argv[1:]} if len(sys.argv)>1 else set(pages)
    jobs=[r for r in rows if r['cote'] in selected]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        futures={ex.submit(extract,r,pages[r['cote']]):r['cote'] for r in jobs}
        for f in concurrent.futures.as_completed(futures):
            try:f.result()
            except Exception as e:print(json.dumps({'cote':futures[f],'error':repr(e)}),flush=True)
