"""Render the authored PDF for visual QA; also report basic page geometry."""
from pathlib import Path
import fitz, json
from PIL import Image, ImageDraw

R=Path(__file__).resolve().parents[2]
out=R/'work/build/visual_qa';out.mkdir(exist_ok=True)
doc=fitz.open(R/'deliverables/JAC1964.pdf')
W,H=238,337
issues=[]
for start in range(0,len(doc),20):
    sheet=Image.new('RGB',(4*(W+12),5*(H+30)),'#e6e6e6')
    draw=ImageDraw.Draw(sheet)
    for j,p in enumerate(list(doc)[start:start+20]):
        pix=p.get_pixmap(matrix=fitz.Matrix(W/p.rect.width,W/p.rect.width),alpha=False)
        thumb=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
        x=(j%4)*(W+12)+6;y=(j//4)*(H+30)+22
        sheet.paste(thumb,(x,y));draw.text((x,y-17),f'Page {start+j+1}',fill='black')
    sheet.save(out/f'contact_{start//20+1:02d}.png')
for i,p in enumerate(doc):
    for b in p.get_text('blocks'):
        if b[0]<45 or b[2]>p.rect.width-45 or b[1]<35 or b[3]>p.rect.height-25:
            issues.append({'page':i+1,'bbox':list(b[:4]),'text':b[4][:100]})
anchors=['The seven-theorem programme','H9-T14','AR-13','JAC-P10','AR-18','Theorem AR-15','What remains to be proved','H9-T18','AR-25','JAC-P18','H9-T20.','H9-T21.','H9-T22.','AR-26.','AR-27.','AR-28.']
pages={0}
for a in anchors:
    hits=[i for i,p in enumerate(doc) if a in p.get_text()]
    if hits:pages.add(hits[-1] if a=='What remains to be proved' else hits[0])
for i in sorted(pages):
    doc[i].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(out/f'page_{i+1:03d}.png')
report={'pdf_pages':len(doc),'margin_alerts':issues,'rendered_full_pages':[i+1 for i in sorted(pages)],'status':'Rendered; visual review is recorded separately, not inferred from rendering.'}
(out/'render_report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
