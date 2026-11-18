# usage: python -I -B stack.py OUTNAME spec1 spec2 ...   spec = scanNNN[_a|_b]:x0,y0,x1,y1,scale[,rot]
import sys
from PIL import Image, ImageDraw
base = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_148_029-072/MPL_148_029-072_148_"
outdir = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/work/MPL_148_029-072_148-059-148-072/"
ims = []
for spec in sys.argv[2:]:
    f, rest = spec.split(":")
    v = rest.split(",")
    x0, y0, x1, y1 = map(int, v[:4]); sc = float(v[4])
    im = Image.open(base + f + ".jpg").convert("RGB").crop((x0, y0, x1, y1))
    im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
    if len(v) > 5:
        im = im.rotate(float(v[5]), expand=True, fillcolor=(255, 255, 255))
    ims.append(im)
W = max(i.width for i in ims); H = sum(i.height for i in ims) + 6 * len(ims)
out = Image.new("RGB", (W, H), (255, 255, 255))
y = 0
d = ImageDraw.Draw(out)
for i in ims:
    out.paste(i, (0, y)); y += i.height
    d.rectangle([0, y, W, y + 5], fill=(255, 0, 0)); y += 6
out.save(outdir + sys.argv[1] + ".png")
print(sys.argv[1], out.size)
