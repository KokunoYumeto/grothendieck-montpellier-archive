from pathlib import Path
import fitz, json
from PIL import Image, ImageOps, ImageDraw

base = Path(__file__).resolve().parent.parent
pdf = fitz.open(base / 'deliverable/ALPOGE_GCT.pdf')
out = base / 'work/qa6new'
out.mkdir(exist_ok=True)
texts = [p.get_text() for p in pdf]
def first(s):
    return next(i + 1 for i,t in enumerate(texts) if s in t)
def last(s):
    return max(i + 1 for i,t in enumerate(texts) if s in t)
pages = {1, 4, 5}
pages.update(range(first('P-F52y'), first('P-F53p') + 2))
pages.update(range(first('P-F54v'), first('P-F56au') + 2))
pages.update(range(first('O-PH2'), min(len(pdf),first('O-THETA') + 3) + 1))
pages = sorted(pages)
thumbs = []
for n in pages:
    pix = pdf[n-1].get_pixmap(matrix=fitz.Matrix(1.35,1.35),alpha=False)
    target = out / f'page-{n:03}.png'
    pix.save(target)
    im = Image.open(target).convert('RGB')
    im.thumbnail((740,1040))
    framed = Image.new('RGB',(760,1080),'#d9d9d9')
    framed.paste(im,((760-im.width)//2,25))
    ImageDraw.Draw(framed).text((12,6),f'Page {n}',fill='black')
    thumbs.append(framed)
contacts=[]
for j in range(0,len(thumbs),6):
    sheet=Image.new('RGB',(1520,3240),'white')
    for k,im in enumerate(thumbs[j:j+6]):
        sheet.paste(im,((k%2)*760,(k//2)*1080))
    path=out / f'contact_{29+j//6:02}.png'
    sheet.save(path)
    contacts.append({'file':str(path),'pages':pages[j:j+6]})
(out/'manifest.json').write_text(json.dumps({'pdf_pages':len(pdf),'contacts':contacts},indent=2))
print(json.dumps({'pdf_pages':len(pdf),'contacts':contacts},indent=2))
