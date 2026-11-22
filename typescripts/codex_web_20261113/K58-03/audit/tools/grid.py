from PIL import Image,ImageDraw
import sys
n,l,t,r,b=map(int,sys.argv[1:6]);w=int(sys.argv[6]) if len(sys.argv)>6 else 1100
im=Image.open(f'K58-03_58_scan{n:03}.jpg').convert('L')
r=min(r,im.width);b=min(b,im.height);im=im.crop((l,t,r,b));scale=w/im.width;h=round(im.height*scale);im=im.resize((w,h),Image.Resampling.LANCZOS)
p=Image.new('L',(w+43,h+19),249);p.paste(im,(43,19));d=ImageDraw.Draw(p)
for x in range((l+99)//100*100,r+1,100):
 at=43+round((x-l)*scale);d.text((at-8,2),str(x),fill=50);d.line((at,14,at,19),fill=50)
for y in range((t+49)//50*50,b+1,50):
 at=19+round((y-t)*scale);d.text((1,at-6),str(y),fill=35);d.line((30,at,42,at),fill=50)
p.save(f'work/grid{n}.jpg',quality=95)
