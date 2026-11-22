"""Render selected original cote 1 folios for direct reading."""
import argparse, hashlib, json, time
from pathlib import Path
import fitz
root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('pages', nargs='*', type=int, default=[1,79,80,111,112,142,143])
parser.add_argument('--width', type=int, default=1800)
args = parser.parse_args()
started = time.perf_counter()
source = root/'sources'/'root_manuscript1_ranged.pdf'
doc = fitz.open(source)
folder = root/'sources'/'root_cote1_folios'
folder.mkdir(exist_ok=True)
files=[]
for number in args.pages:
    page=doc[number-1]
    scale=args.width/page.rect.width
    target=folder/f'page_{number:03d}.png'
    page.get_pixmap(matrix=fitz.Matrix(scale,scale),alpha=False).save(target)
    files.append(str(target.relative_to(root)))
record={'input':str(source.relative_to(root)),'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'pages':args.pages,'width':args.width,'files':files,'elapsed_seconds':time.perf_counter()-started}
tag='_'.join(f'{p:03d}' for p in args.pages)
(root/'logs'/f'root_render_cote1_{tag}.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
