from pathlib import Path
from urllib.request import Request, urlopen
import time, hashlib, fitz

url = 'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/GroupesB-T.pdf'
root = Path('RESEARCH_SA23/sources')
started = time.monotonic()
data = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60).read()
p = root / 'category_Grothendieck_ICM1970.pdf'
p.write_bytes(data)
print(url, len(data), hashlib.sha256(data).hexdigest(), 'seconds', time.monotonic()-started)
doc = fitz.open(p)
(root / 'category_Grothendieck_ICM1970.txt').write_text('\n\f\n'.join(page.get_text() for page in doc))
for n in (1, 4, 5, 6):
    out = root / f'category_Grothendieck_ICM1970_p{n}.png'
    doc[n-1].get_pixmap(matrix=fitz.Matrix(1.7, 1.7)).save(out)
    print('rendered', n, out)
