#!/usr/bin/env python3
"""Extract cited original pages with HTTP ranges, preserving an access log."""
import io, json, pathlib, sys, time, urllib.request
from pypdf import PdfReader, PdfWriter, PageObject

class RangedFile(io.RawIOBase):
    def __init__(self,url,length,block=262144):
        self.url=url; self.length=length; self.block=block; self.pos=0
        self.cache={}; self.events=[]
    def readable(self): return True
    def seekable(self): return True
    def tell(self): return self.pos
    def seek(self,offset,whence=0):
        self.pos=offset if whence==0 else self.pos+offset if whence==1 else self.length+offset
        return self.pos
    def read(self,size=-1):
        if size<0: size=self.length-self.pos
        end=min(self.length,self.pos+size); out=[]
        while self.pos<end:
            i=self.pos//self.block
            if i not in self.cache:
                a=i*self.block; b=min(self.length,a+self.block)-1; start=time.monotonic()
                req=urllib.request.Request(self.url,headers={'Range':f'bytes={a}-{b}'})
                for attempt in range(4):
                    try:
                        with urllib.request.urlopen(req,timeout=60) as r:
                            if r.status!=206: raise RuntimeError(f'Range not honoured: {r.status}')
                            data=r.read()
                        break
                    except urllib.error.HTTPError:
                        if attempt==3: raise
                if len(data)!=b-a+1: raise RuntimeError('Incomplete range')
                self.cache[i]=data; self.events.append({'start':a,'end':b,'seconds':round(time.monotonic()-start,3)})
                print(f'range {a}-{b}',flush=True)
            data=self.cache[i]; a=self.pos-i*self.block; n=min(end-self.pos,len(data)-a)
            out.append(data[a:a+n]); self.pos+=n
        return b''.join(out)

if __name__=='__main__':
    url,length,pages,outpath,logpath=sys.argv[1:]
    f=RangedFile(url,int(length)); start=time.monotonic(); reader=PdfReader(f,strict=True)
    writer=PdfWriter(); wanted=[int(x) for x in pages.split(',')]
    def page_at(ref,index,inherited=None):
        obj=ref.get_object(); inherited=dict(inherited or {})
        for key in ('/Resources','/MediaBox','/CropBox','/Rotate'):
            if key in obj: inherited[key]=obj[key]
        if obj['/Type']=='/Page':
            page=PageObject(reader,ref); page.update(inherited); page.update(obj); return page
        kids=obj['/Kids']
        if int(obj['/Count'])==len(kids): return page_at(kids[index],0,inherited)
        for kid in kids:
            child=kid.get_object(); count=int(child.get('/Count',1))
            if index<count: return page_at(kid,index,inherited)
            index-=count
        raise IndexError(index)
    for p in wanted:
        writer.add_page(page_at(reader.trailer['/Root']['/Pages'],p-1)); print(f'page {p} added',flush=True)
    with open(outpath,'wb') as out: writer.write(out)
    pathlib.Path(logpath).write_text(json.dumps({'url':url,'source_length':int(length),'pages':wanted,'ranges':f.events,'seconds':time.monotonic()-start},indent=2))
