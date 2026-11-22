import fitz,json,time
from PIL import Image,ImageOps,ImageDraw
from pathlib import Path
root=Path(__file__).resolve().parents[1];t=time.perf_counter()
doc=fitz.open(root/'build/RESEARCH_SA12_paper.pdf')
pages=sorted(set([1,4,5,9,15,20,25,30,35,40,len(doc)]))
thumbs=[]
for p in pages:
    if p>len(doc):continue
    pix=doc[p-1].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
    out=root/f'qa/checkpoint01_page_{p:02d}.png';pix.save(out)
    im=Image.open(out).convert('RGB');im.thumbnail((398,565))
    card=Image.new('RGB',(418,601),'#dddddd');card.paste(im,((418-im.width)//2,26))
    ImageDraw.Draw(card).text((10,7),f'Page {p}',fill='black');thumbs.append(card)
sheet=Image.new('RGB',(418*3,601*((len(thumbs)+2)//3)),'white')
for i,im in enumerate(thumbs):sheet.paste(im,((i%3)*418,(i//3)*601))
sheet.save(root/'qa/checkpoint01_contact.png')
(root/'qa/checkpoint01_render.json').write_text(json.dumps({'pdf_pages':len(doc),'rendered_pages':pages,'seconds':time.perf_counter()-t},indent=2))
print({'pages':len(doc),'rendered':pages,'seconds':time.perf_counter()-t})

