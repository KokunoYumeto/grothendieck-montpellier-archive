"""Retrieve exact manuscript scans by HTTP range; reuse read-only B cache.

Based on the independently written range reader in B_fetch_pdf_ranges.py.
Only C-prefixed output/cache files are written by this script.
"""
from pathlib import Path
from urllib.request import Request, urlopen
import argparse, io, json, os, time
from pypdf import PdfReader, PdfWriter, PageObject
from pypdf.generic import NameObject

root = Path(__file__).resolve().parents[1]
url = 'https://grothendieck.umontpellier.fr/136.pdf'
length = 161283368

class RangeFile(io.RawIOBase):
    def __init__(self):
        self.pos=0; self.block=262144; self.calls=[]; self.cache={}
        self.output=root/'sources/C_range_cache'; self.output.mkdir(exist_ok=True)
    def readable(self): return True
    def seekable(self): return True
    def tell(self): return self.pos
    def seek(self, offset, whence=0):
        self.pos=(0 if whence==0 else self.pos if whence==1 else length)+offset
        return self.pos
    def read(self, size=-1):
        if size<0: size=length-self.pos
        size=min(size,length-self.pos)
        if size<=0: return b''
        end=self.pos+size; pieces=[]
        while self.pos<end:
            block=self.pos//self.block
            lo=block*self.block; hi=min(length,lo+self.block)-1
            if block not in self.cache:
                local=self.output/str(block)
                previous=root/'sources/B_range_cache'/str(block)
                if local.exists(): data=local.read_bytes()
                elif previous.exists(): data=previous.read_bytes()
                else:
                    begin=time.monotonic()
                    req=Request(url, headers={'Range':f'bytes={lo}-{hi}',
                                              'User-Agent':'SA08 source verification'})
                    for attempt in range(4):
                        try:
                            with urlopen(req,timeout=50) as response:
                                if response.status!=206:
                                    raise RuntimeError(f'Range status {response.status}')
                                data=response.read()
                            break
                        except Exception as error:
                            print('retry',block,attempt,repr(error),flush=True)
                            if attempt==3: raise
                    temporary=local.with_name(local.name+f'.{os.getpid()}.tmp')
                    temporary.write_bytes(data)
                    temporary.replace(local)
                    record={'start':lo,'end':hi,'bytes':len(data),
                            'seconds':time.monotonic()-begin}
                    self.calls.append(record); print(json.dumps(record),flush=True)
                assert len(data)==hi-lo+1
                self.cache[block]=data
            count=min(end-self.pos,hi+1-self.pos)
            pieces.append(self.cache[block][self.pos-lo:self.pos-lo+count])
            self.pos+=count
        return b''.join(pieces)

def select_page(node,index,inherited=None):
    node=node.get_object(); inherited=dict(inherited or {})
    for key in ['/Resources','/MediaBox','/CropBox','/Rotate']:
        if key in node: inherited[key]=node[key]
    if node.get('/Type')=='/Page':
        assert index==0
        page=PageObject()
        for key,value in inherited.items(): page[NameObject(key)]=value
        for key,value in node.items():
            if key!='/Parent': page[key]=value
        return page
    kids=node['/Kids']
    if len(kids)==int(node['/Count']): return select_page(kids[index],0,inherited)
    for kid in kids:
        count=int(kid.get_object().get('/Count',1))
        if index<count: return select_page(kid,index,inherited)
        index-=count
    raise IndexError(index)

parser=argparse.ArgumentParser()
parser.add_argument('--scans',type=int,nargs='+',required=True)
parser.add_argument('--tag',required=True)
args=parser.parse_args()
begin=time.monotonic(); remote=RangeFile(); reader=PdfReader(remote,strict=True)
writer=PdfWriter(); tree=reader.trailer['/Root']['/Pages']
for scan in args.scans:
    writer.add_page(select_page(tree,scan-1)); print('copied scan',scan,flush=True)
output=root/'sources'/f'C_cote136_{args.tag}.pdf'
with output.open('wb') as stream: writer.write(stream)
record={'url':url,'scans':args.scans,'source_bytes':length,
        'transferred':sum(call['bytes'] for call in remote.calls),
        'calls':remote.calls,'output':str(output),'seconds':time.monotonic()-begin}
(root/'logs'/f'C_cote136_{args.tag}.json').write_text(json.dumps(record,indent=2))
print(json.dumps({k:v for k,v in record.items() if k!='calls'}),flush=True)
