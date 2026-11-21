import sys
from pypdf import PdfReader, PdfWriter
from pypdf._page import PageObject
from pypdf.generic import NameObject
from aq_range_pdf import RangeFile
url,out,lo,hi=sys.argv[1:]
lo,hi=int(lo),int(hi)
remote=RangeFile(url)
reader=PdfReader(remote,strict=True)
writer=PdfWriter()
selected=[]
inheritable=("/MediaBox","/CropBox","/Resources","/Rotate")
def visit(ref,offset,inherited):
    node=ref.get_object()
    attrs=inherited.copy()
    for key in inheritable:
        if key in node: attrs[NameObject(key)]=node[key]
    if node.get("/Type")=="/Page":
        if lo<=offset<=hi:
            page=PageObject(reader,ref)
            page.update(attrs); page.update(node)
            selected.append((offset,page))
            print("selected",offset,"cache",len(remote.cache),flush=True)
        return 1
    kids=node["/Kids"]; count=int(node["/Count"])
    if count==len(kids):
        for i in range(max(0,lo-offset),min(len(kids),hi-offset+1)):
            visit(kids[i],offset+i,attrs)
    else:
        cursor=offset
        for child in kids:
            obj=child.get_object()
            size=1 if obj.get("/Type")=="/Page" else int(obj["/Count"])
            if cursor<=hi and cursor+size>lo:visit(child,cursor,attrs)
            cursor+=size
            if cursor>hi:break
    return count
root=reader.trailer["/Root"]["/Pages"]
print("total_pages",root["/Count"],flush=True)
visit(root,0,{})
for i,page in selected:
    writer.add_page(page)
    print("copied",i,"cache",len(remote.cache),flush=True)
with open(out,"wb") as f:writer.write(f)
print("saved",out,"bytes_fetched",sum(map(len,remote.cache.values())),flush=True)
