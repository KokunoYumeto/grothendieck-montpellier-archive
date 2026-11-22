"""Render the two retained publisher-preview pages for actual primary inspection."""
from pathlib import Path
import fitz, hashlib, json
from PIL import Image
root = Path(__file__).resolve().parents[1]
source = root / 'parts/C/post23_research/sources/Grothendieck_Murre_1971_ch9_preview.pdf'
assert hashlib.sha256(source.read_bytes()).hexdigest() == '8875d99455752dfe6a9b7274ea98e81f2e5138ccffae4f8e15da90693c40ce29'
doc = fitz.open(source)
assert len(doc) == 2
paths = []
for index, page in enumerate(doc):
    pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
    image = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    path = root / f'qa/GM1971_ch9_root_p{122+index}.webp'
    image.save(path, 'WEBP', lossless=True, quality=100, method=4)
    assert Image.open(path).convert('RGB').tobytes() == image.tobytes()
    paths.append(str(path.relative_to(root)))
print(json.dumps({'source': str(source.relative_to(root)), 'rendered_pages': [122, 123], 'paths': paths, 'inspection_claim': 'Rendering only; actual view is recorded separately.'}, indent=2))
