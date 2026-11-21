from pathlib import Path
from PIL import Image, ImageDraw
import argparse, subprocess, tempfile, json
base=Path(__file__).resolve().parent.parent
parser=argparse.ArgumentParser();parser.add_argument('index',type=int);args=parser.parse_args()
out=base/'work'/'qa'/f'checkpoint{args.index:02d}'
out.mkdir(parents=True,exist_ok=True)
with tempfile.TemporaryDirectory(prefix='k17_pdf_pages_') as tmp:
    prefix=str(Path(tmp)/'page')
    subprocess.run(['pdftoppm','-scale-to','850','-png',str(base/'K17_package'/'K17.pdf'),prefix],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    pages=sorted(Path(tmp).glob('page-*.png'),key=lambda p:int(p.stem.split('-')[-1]))
    width=360; height=510; gap=16; label=24; cols=3; rows=3
    sheets=[]
    for start in range(0,len(pages),cols*rows):
        sheet=Image.new('RGB',(cols*(width+gap)+gap,rows*(height+label+gap)+gap),'#d5d8dc')
        draw=ImageDraw.Draw(sheet)
        for offset,path in enumerate(pages[start:start+cols*rows]):
            im=Image.open(path).convert('RGB');im.thumbnail((width,height))
            col=offset%cols;row=offset//cols;x=gap+col*(width+gap);y=gap+row*(height+label+gap)
            draw.text((x,y),f'Page {start+offset+1}',fill='black')
            sheet.paste(im,(x,y+label))
        dest=out/f'contact_{start//(cols*rows)+1:02d}.png';sheet.save(dest,optimize=True);sheets.append(str(dest))
    (out/'manifest.json').write_text(json.dumps({'pages':len(pages),'contact_sheets':sheets},indent=2)+'\n')
print(json.dumps({'pages':len(pages),'contact_sheet_count':len(sheets),'directory':str(out)}))
