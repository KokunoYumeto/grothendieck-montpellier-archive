#!/usr/bin/env python3
"""Extract specified pages of a primary PDF via cached HTTP range reads."""
import io, json, pathlib, sys, time, urllib.request
from pypdf import PdfReader, PdfWriter, PageObject

class RangeFile(io.RawIOBase):
    def __init__(self, url, length, block=262144):
        self.url, self.length, self.block = url, length, block
        self.position, self.cache, self.transfers = 0, {}, []
        self.cache_dir=pathlib.Path('sources/Grothendieck/range_cache')
        self.cache_dir.mkdir(parents=True,exist_ok=True)
    def readable(self): return True
    def seekable(self): return True
    def tell(self): return self.position
    def seek(self, offset, whence=0):
        self.position = offset + (0 if whence == 0 else self.position if whence == 1 else self.length)
        return self.position
    def read(self, n=-1):
        if n < 0: n = self.length-self.position
        end = min(self.position+n, self.length)
        parts=[]
        while self.position<end:
            index=self.position//self.block
            if index not in self.cache:
                start=index*self.block; stop=min(start+self.block,self.length)-1
                path=self.cache_dir/f'{start}-{stop}.bin'
                if path.exists():
                    data=path.read_bytes()
                else:
                    for attempt in range(5):
                        try:
                            request=urllib.request.Request(self.url,headers={'Range':f'bytes={start}-{stop}'})
                            with urllib.request.urlopen(request,timeout=30) as response:
                                data=response.read()
                                if response.status != 206:
                                    raise RuntimeError(f'Range request returned HTTP {response.status}')
                            if len(data)!=stop-start+1: raise RuntimeError('Incomplete range')
                            path.write_bytes(data)
                            break
                        except Exception:
                            if attempt==4: raise
                            time.sleep(2)
                self.cache[index]=data
                self.transfers.append([start,stop,len(data)])
            start=self.position-index*self.block
            count=min(end-self.position,len(self.cache[index])-start)
            if count<=0: break
            parts.append(self.cache[index][start:start+count]); self.position+=count
        return b''.join(parts)

if __name__=='__main__':
    url,length,page_spec,destination,log=sys.argv[1:]
    started=time.monotonic()
    stream=RangeFile(url,int(length)); writer=PdfWriter()
    reader=PdfReader(stream, strict=True)
    pages=[int(x) for x in page_spec.split(',')]
    def get_page(node_ref, index, inherited=None):
        inherited=dict(inherited or {})
        node=node_ref.get_object()
        for key in ('/Resources','/MediaBox','/CropBox','/Rotate'):
            if key in node: inherited[key]=node[key]
        if node.get('/Type')=='/Page':
            if index: raise IndexError(index)
            page=PageObject(pdf=reader,indirect_reference=node_ref)
            page.update(node)
            from pypdf.generic import NameObject
            for key,value in inherited.items():
                if key not in page: page[NameObject(key)]=value
            return page
        for kid in node['/Kids']:
            child=kid.get_object()
            count=int(child.get('/Count',1))
            if index<count: return get_page(kid,index,inherited)
            index-=count
        raise IndexError(index)
    page_tree=reader.root_object.raw_get('/Pages')
    count=int(page_tree.get_object()['/Count'])
    for page in pages: writer.add_page(get_page(page_tree,page-1))
    writer.write(destination)
    result=dict(url=url,pages_1_based=pages,source_pages=count,
                range_transfers=stream.transfers,bytes_read=sum(len(x) for x in stream.cache.values()),
                seconds=round(time.monotonic()-started,3),destination=destination)
    pathlib.Path(log).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
