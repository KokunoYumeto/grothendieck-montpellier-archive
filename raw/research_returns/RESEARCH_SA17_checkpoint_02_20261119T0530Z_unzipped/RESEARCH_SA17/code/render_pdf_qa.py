"""Reproduce the second-checkpoint PDF contact sheets; inspect them manually."""
from pathlib import Path
import fitz, json
from PIL import Image, ImageDraw

root = Path(__file__).resolve().parents[1]
doc = fitz.open(root/'RESEARCH_SA17_paper.pdf')
out = root/'logs/pdf_qa'
out.mkdir(exist_ok=True)
terms = ['For every prime', 'For every T/', 'C_torsion_trace',
         'element subsets of', 'Frobenius trace one']
pages = {0,1,7,11,17,23,29,35,41,47,53,len(doc)-1}
for i,page in enumerate(doc):
    if any(t in page.get_text() for t in terms):
        pages.add(i)
pages.update(i for i in [13,14,20,21,24,25,34,35,36,40,41,42,43] if i<len(doc))
pages = sorted(pages)
for index,start in enumerate(range(0,len(pages),8)):
    group = pages[start:start+8]
    canvas = Image.new('RGB',(1600,2320),'#999999')
    for n,i in enumerate(group):
        pix = doc[i].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
        img = Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
        img.thumbnail((780,550))
        x=(n%2)*800+(800-img.width)//2
        y=(n//2)*580
        canvas.paste(img,(x,y+24))
        ImageDraw.Draw(canvas).text((x,y+4),f'Page {i+1}',fill='black')
    canvas.save(out/f'spread_{index+1}.jpg',quality=90)
for i in [13,20,35,41]:
    if i<len(doc):
        doc[i].get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False).save(str(out/f'page_{i+1}.png'))
(root/'logs/pdf_qa_render.json').write_text(json.dumps({
    'pages_total':len(doc),'pages_rendered':[i+1 for i in pages],
    'visual_check':'Required separately; rendering is not inspection.'},indent=2)+'\n')
print('Rendered pages', [i+1 for i in pages])
