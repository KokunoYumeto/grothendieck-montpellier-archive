"""Make enlarged, boundary-marked crops for actual ink-candidate inspection."""
from pathlib import Path
import argparse,json,hashlib
import fitz
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('stem');args=a.parse_args()
j=json.loads((P/'records'/('INK_AUDIT_'+args.stem+'.json')).read_text());data=(P/j['pdf']).read_bytes()
assert hashlib.sha256(data).hexdigest()==j['pdf_sha256']
d=fitz.open(stream=data,filetype='pdf');dest=P/'qa/rendered'/('ink_candidates_'+args.stem+'_'+j['pdf_sha256'][:8]);dest.mkdir(parents=True,exist_ok=True)
panels=[];mapping=[]
for row in j['candidate_pages']:
    page=d[row['page']-1]
    for n,c in enumerate(row['components'],1):
        x0,y0,x1,y1=c['bbox_pt'];clip=fitz.Rect(max(0,x0-155),max(0,y0-13),min(page.rect.width,x1+55),min(page.rect.height,y1+13))
        pix=page.get_pixmap(matrix=fitz.Matrix(3,3),clip=clip,alpha=False)
        panel=Image.new('RGB',(max(720,pix.width),pix.height+25),'white');im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);panel.paste(im,(0,25));draw=ImageDraw.Draw(panel)
        draw.text((3,3),f"PDF p{row['page']}, component{n}: {c['bbox_pt']} ({c['pixels']} pixels)",fill='black')
        for x in [18*72/25.4,page.rect.width-45*72/25.4]:
            xx=(x-clip.x0)*3
            if 0<=xx<panel.width:draw.line((xx,25,xx,panel.height),fill='red',width=1)
        yy=(page.rect.height-22*72/25.4-clip.y0)*3+25
        if 25<=yy<panel.height:draw.line((0,yy,panel.width,yy),fill='red',width=1)
        panels.append(panel);mapping.append({'page':row['page'],'component':n})
contacts=[]
for start in range(0,len(panels),6):
    batch=panels[start:start+6];out=Image.new('RGB',(max(x.width for x in batch),sum(x.height for x in batch)+12*(len(batch)-1)),(235,235,235));yy=0
    for im in batch:out.paste(im,(0,yy));yy+=im.height+12
    path=dest/f'contact_{start//6+1:02d}.png';out.save(path);contacts.append({'image':str(path.relative_to(P)),'components':mapping[start:start+6]})
(dest/'CONTACT_MAP.json').write_text(json.dumps({'pdf_sha256':j['pdf_sha256'],'contacts':contacts},indent=2)+'\n')
print(json.dumps({'contacts':len(contacts),'components':len(panels),'directory':str(dest.relative_to(P))}))
