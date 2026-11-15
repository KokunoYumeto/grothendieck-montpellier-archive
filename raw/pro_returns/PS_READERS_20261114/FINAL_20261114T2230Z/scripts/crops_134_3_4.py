from PIL import Image,ImageDraw
from pathlib import Path
def sheet(key,boxes):
 panels=[]
 for n,(half,box) in enumerate(boxes,1):
  im=Image.open(Path('inputs/images/scans')/f'{key}_{half}.jpg').crop(box);im=im.resize((im.width*2,im.height*2));p=Image.new('RGB',(im.width,im.height+25),'white');p.paste(im,(0,25));ImageDraw.Draw(p).text((5,4),str(n),fill='black');panels.append(p)
 s=Image.new('RGB',(max(p.width for p in panels),sum(p.height+10 for p in panels)),'white');y=0
 for p in panels:s.paste(p,(0,y));y+=p.height+10
 s.save(Path('PS_READERS_WORK/qa/crops')/f'{key}_details.png')
