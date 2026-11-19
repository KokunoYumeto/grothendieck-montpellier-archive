import sys
from PIL import Image
# usage: crop.py image out scale x0,y0,x1,y1[,rot] ...   (coordinates in the given image's pixels; rot in degrees)
src, out, scale = sys.argv[1], sys.argv[2], float(sys.argv[3])
im = Image.open(src).convert('RGB')
parts = []
for b in sys.argv[4:]:
    v = [float(x) for x in b.split(',')]
    c = im.crop(tuple(int(x) for x in v[:4]))
    if len(v) > 4 and v[4]:
        c = c.rotate(v[4], expand=True, fillcolor=(255, 255, 255))
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    parts.append(c)
W = max(p.width for p in parts)
H = sum(p.height for p in parts) + 8 * (len(parts) - 1)
canvas = Image.new('RGB', (W, H), (255, 255, 255))
y = 0
for p in parts:
    canvas.paste(p, (0, y))
    y += p.height + 8
    if y < H:
        for x in range(W):
            canvas.putpixel((x, y - 4), (255, 0, 0))
canvas.save(out, quality=92)
print(out, canvas.size)
