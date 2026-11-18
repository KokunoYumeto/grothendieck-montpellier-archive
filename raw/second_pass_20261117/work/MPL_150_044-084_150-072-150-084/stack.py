"""Stack several crops vertically into one image for viewing.

Usage: python -I -B stack.py OUT.png WIDTH IN1.png IN2.png ...
Each input is scaled to WIDTH (keeping aspect) and separated by a grey band.
"""
import sys
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out = os.path.join(HERE, sys.argv[1])
    width = int(sys.argv[2])
    ims = []
    for name in sys.argv[3:]:
        im = Image.open(os.path.join(HERE, name)).convert('L')
        h = int(im.height * width / im.width)
        ims.append(im.resize((width, h), Image.LANCZOS))
    total = sum(i.height for i in ims) + 12 * (len(ims) - 1)
    canvas = Image.new('L', (width, total), 255)
    y = 0
    for i in ims:
        canvas.paste(i, (0, y))
        y += i.height
        if y < total:
            canvas.paste(Image.new('L', (width, 12), 128), (0, y))
            y += 12
    canvas.save(out)
    print(out, canvas.size)


if __name__ == '__main__':
    main()
