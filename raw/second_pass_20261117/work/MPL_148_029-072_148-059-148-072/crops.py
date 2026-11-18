# usage: python -I -B crops.py SCANFILE_SUFFIX x0 y0 x1 y1 scale outname [rotate]
import sys
from PIL import Image
src = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_148_029-072/MPL_148_029-072_148_" + sys.argv[1] + ".jpg"
x0, y0, x1, y1 = map(int, sys.argv[2:6])
sc = float(sys.argv[6])
out = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/work/MPL_148_029-072_148-059-148-072/" + sys.argv[7] + ".png"
im = Image.open(src).crop((x0, y0, x1, y1))
im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
if len(sys.argv) > 8:
    im = im.rotate(float(sys.argv[8]), expand=True)
im.save(out)
print(out, im.size)
