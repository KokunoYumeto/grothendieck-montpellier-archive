"""Stitch horizontal bands of the two halves of a landscape scan side by side.

Usage: python -I -B stitch.py OUT.jpg SCAN y0 y1 [xa0 xa1 xb0 xb1] [W]
  SCAN  e.g. 152_scan003 (halves _a = left, _b = right)
  y0,y1 band in display coordinates (long side 2000)
  xa0..xa1 range in the left half, xb0..xb1 range in the right half (display coords)
  W     output width (default 2000)
"""
import sys, os
from PIL import Image

IMG_DIR = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/img/MPL_152+120"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def part(name, x0, y0, x1, y1):
    im = Image.open(os.path.join(IMG_DIR, "MPL_152+120_" + name + ".jpg")).convert("RGB")
    w, h = im.size
    f = max(1.0, max(w, h) / 2000.0)
    return im.crop((int(x0 * f), int(y0 * f), int(x1 * f), int(y1 * f)))


def main():
    out, scan = sys.argv[1], sys.argv[2]
    y0, y1 = float(sys.argv[3]), float(sys.argv[4])
    xs = [float(v) for v in sys.argv[5:9]] if len(sys.argv) >= 9 else [0, 1400, 0, 1400]
    W = int(sys.argv[9]) if len(sys.argv) >= 10 else 2000
    a = part(scan + "_a", xs[0], y0, xs[1], y1)
    b = part(scan + "_b", xs[2], y0, xs[3], y1)
    h = max(a.size[1], b.size[1])
    m = Image.new("RGB", (a.size[0] + b.size[0] + 8, h), (200, 0, 0))
    m.paste(a, (0, 0))
    m.paste(b, (a.size[0] + 8, 0))
    s = W / m.size[0]
    m = m.resize((W, int(m.size[1] * s)), Image.LANCZOS)
    m.save(os.path.join(OUT_DIR, out), quality=90)
    print(out, m.size)


if __name__ == "__main__":
    main()
