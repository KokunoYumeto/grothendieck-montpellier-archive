"""Render requested one-based primary-source pages for visual formula checks."""
from pathlib import Path
import argparse
import json
import time
import fitz

parser = argparse.ArgumentParser()
parser.add_argument('pdf', type=Path)
parser.add_argument('pages', nargs='+', type=int)
args = parser.parse_args()
start = time.monotonic()
document = fitz.open(args.pdf)
destination = args.pdf.parent / 'source_page_checks'
destination.mkdir(exist_ok=True)
outputs = []
for page in args.pages:
    if not 1 <= page <= len(document):
        raise ValueError(f'Page {page} outside the document')
    output = destination / f'{args.pdf.stem}_p{page:03}.png'
    document[page - 1].get_pixmap(matrix=fitz.Matrix(1.6, 1.6)).save(output)
    outputs.append(str(output.resolve()))
record = {'source': str(args.pdf.resolve()), 'one_based_pages': args.pages,
          'outputs': outputs, 'seconds': round(time.monotonic() - start, 3)}
root = Path(__file__).resolve().parents[1]
with (root / 'code' / 'render_primary_pages_output.jsonl').open('a') as stream:
    stream.write(json.dumps(record) + '\n')
print(json.dumps(record))
