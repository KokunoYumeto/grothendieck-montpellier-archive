"""Read selected original cote136 pages with explicit HTTP ranges."""
from pathlib import Path
from urllib.request import Request,urlopen
import io,time,json,argparse
from pypdf import PdfReader,PdfWriter,PageObject
base=Path(__file__).resolve().parents[1]
partial=base/'sources'/'B_original_cote136.pdf'
if partial.exists():partial.rename(base/'sources'/'B_original_cote136.partial')
url='https://grothendieck.umontpellier.fr/136.pdf'
length=161283368
class RangeFile(io.RawIOBase):
    def __init__(self):self.pos=0;self.cache={};self.calls=[];self.block=262144;self.cache_dir=base/'sources'/'B_range_cache';self.cache_dir.mkdir(exist_ok=True)
    def readable(self):return True
    def seekable(self):return True
    def tell(self):return self.pos
    def seek(self,offset,whence=0):
        self.pos=(0 if whence==0 else self.pos if whence==1 else length)+offset
        return self.pos
    def read(self,size=-1):
        if size<0:size=length-self.pos
        size=min(size,length-self.pos)
        if size<=0:return b''
        end=self.pos+size;ans=[]
        while self.pos<end:
            bi=self.pos//self.block;lo=bi*self.block;hi=min(length,lo+self.block)-1
            if bi not in self.cache:
                t=time.monotonic()
                cached=self.cache_dir/str(bi)
                if cached.exists():
                    self.cache[bi]=cached.read_bytes()
                    continue
                req=Request(url,headers={'Range':f'bytes={lo}-{hi}','User-Agent':'SA08 source verification'})
                for attempt in range(4):
                    try:
                        with urlopen(req,timeout=55) as r:
                            if r.status!=206:raise RuntimeError(f'Range rejected: status{r.status}')
                            data=r.read()
                        break
                    except Exception as err:
                        print('retry',bi,attempt,type(err).__name__,str(err),flush=True)
                        if attempt==3:raise
                        time.sleep(2)
                cached.write_bytes(data)
                assert len(data)==hi-lo+1,(len(data),lo,hi)
                self.cache[bi]=data
                rec={'start':lo,'end':hi,'bytes':len(data),'seconds':time.monotonic()-t};self.calls.append(rec)
                print(json.dumps(rec),flush=True)
            count=min(end-self.pos,hi+1-self.pos)
            ans.append(self.cache[bi][self.pos-lo:self.pos-lo+count]);self.pos+=count
        return b''.join(ans)
t=time.monotonic();f=RangeFile();reader=PdfReader(f,strict=True)
writer=PdfWriter()
def select_page(node,index,inherited=None):
    node=node.get_object();inherited=dict(inherited or {})
    for key in ['/Resources','/MediaBox','/CropBox','/Rotate']:
        if key in node:inherited[key]=node[key]
    if node.get('/Type')=='/Page':
        assert index==0
        from pypdf.generic import NameObject
        page=PageObject()
        for key,value in inherited.items():page[NameObject(key)]=value
        for key,value in node.items():
            if key!='/Parent':page[key]=value
        return page
    kids=node['/Kids']
    if len(kids)==int(node['/Count']):
        return select_page(kids[index],0,inherited)
    for kid in kids:
        obj=kid.get_object();count=int(obj.get('/Count',1))
        if index<count:return select_page(kid,index,inherited)
        index-=count
    raise IndexError(index)
parser=argparse.ArgumentParser()
parser.add_argument('--scans',type=int,nargs='+',default=[142,143,144,145])
parser.add_argument('--tag',default='142_145')
args=parser.parse_args()
scans=args.scans
root=reader.trailer['/Root']['/Pages']
print('root page tree',root.get('/Count'),len(root['/Kids']),flush=True)
for scan in scans:
    writer.add_page(select_page(root,scan-1));print('copied scan',scan,flush=True)
output=base/'sources'/f'B_cote136_scans{args.tag}.pdf'
with output.open('wb') as out:writer.write(out)
report={'url':url,'scans':scans,'source_bytes':length,'transferred':sum(r['bytes'] for r in f.calls),'range_calls':f.calls,'output':str(output),'seconds':time.monotonic()-t}
receipt='B_cote136_ranges.json' if args.tag=='142_145' else f'B_cote136_ranges_{args.tag}.json'
(base/'logs'/receipt).write_text(json.dumps(report,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='range_calls'}),flush=True)
