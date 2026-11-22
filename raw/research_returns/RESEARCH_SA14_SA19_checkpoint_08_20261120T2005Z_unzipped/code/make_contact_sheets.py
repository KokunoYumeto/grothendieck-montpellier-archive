"""Make four-page contact sheets for explicit PDF layout inspection."""
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
import sys,json
root=Path(__file__).resolve().parents[1]
folder=root/'tmp/pdfs'/('qa_'+sys.argv[1])
pages=sorted(folder.glob('page-*.png'),key=lambda p:int(p.stem.split('-')[-1]))
outputs=[]
for n,start in enumerate(range(0,len(pages),4),1):
 canvas=Image.new('RGB',(1600,2320),'#d8d8d8')
 draw=ImageDraw.Draw(canvas)
 for k,p in enumerate(pages[start:start+4]):
  im=Image.open(p).convert('RGB');im.thumbnail((780,1110))
  x=(k%2)*800+(800-im.width)//2;y=(k//2)*1160+32
  canvas.paste(im,(x,y));draw.text(((k%2)*800+12,(k//2)*1160+8),p.stem,fill='black')
 out=folder/f'contact-{n:02d}.png';canvas.save(out);outputs.append(str(out))
print(json.dumps(outputs,indent=2))
