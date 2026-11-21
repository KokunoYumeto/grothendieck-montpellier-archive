from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageOps, ImageDraw
import json
import subprocess

base=Path(__file__).resolve().parents[2]
tmp=base/'qa_tmp/revision10_complete'; tmp.mkdir(parents=True,exist_ok=True)
pages=[313, 315]
def render(n):
    dest=tmp/f'p{n:03}'
    subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1050','-singlefile','-png',str(base/'deliverables/CUE_GCT.pdf'),str(dest)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
with ThreadPoolExecutor(max_workers=6) as pool:
    list(pool.map(render,pages))
files=[]
for start in range(0,len(pages),9):
    group=pages[start:start+9]
    sheet=Image.new('RGB',(1950,2820),'#d2d2d2'); draw=ImageDraw.Draw(sheet)
    for k,n in enumerate(group):
        im=Image.open(tmp/f'p{n:03}.png').convert('RGB')
        im.thumbnail((630,900))
        x=(k%3)*650+(650-im.width)//2; y=(k//3)*940+28
        sheet.paste(im,(x,y)); draw.text(((k%3)*650+14,(k//3)*940+8),f'Page {n}',fill='black')
    path=base/f'work/qa/revision10_complete_{start//9+1:02}.jpg'; sheet.save(path,quality=88); files.append(path.name)
(base/'work/qa/revision10_complete_pages.json').write_text(json.dumps({'pages':pages,'files':files},indent=2)+'\n')
print(json.dumps({'pages':pages,'files':files}))
