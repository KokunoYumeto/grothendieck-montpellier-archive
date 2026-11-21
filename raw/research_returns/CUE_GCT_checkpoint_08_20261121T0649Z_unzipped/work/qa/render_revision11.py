from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from PIL import Image,ImageDraw
import json,subprocess
B=Path(__file__).resolve().parents[2]
tmp=B/'qa_tmp/revision11';tmp.mkdir(parents=True,exist_ok=True)
pages=sorted(set(list(range(1,15))+list(range(89,99))+list(range(147,156))+list(range(241,257))+list(range(283,290))+list(range(292,294))+list(range(322,332))+[339,340,350,351,368]))
def render(n):
 subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1050','-singlefile','-png',str(B/'deliverables/CUE_GCT.pdf'),str(tmp/f'p{n:03}')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
with ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(render,pages))
files=[]
for start in range(0,len(pages),9):
 group=pages[start:start+9];sheet=Image.new('RGB',(1950,2820),'#d2d2d2');draw=ImageDraw.Draw(sheet)
 for k,n in enumerate(group):
  im=Image.open(tmp/f'p{n:03}.png').convert('RGB');im.thumbnail((630,900))
  x=(k%3)*650+(650-im.width)//2;y=(k//3)*940+28
  sheet.paste(im,(x,y));draw.text(((k%3)*650+14,(k//3)*940+8),f'Page {n}',fill='black')
 path=B/f'work/qa/revision11_{start//9+1:02}.jpg';sheet.save(path,quality=88);files.append(path.name)
(B/'work/qa/revision11_pages.json').write_text(json.dumps({'pages':pages,'files':files},indent=2)+'\n')
print(json.dumps({'pages':pages,'files':files}))
