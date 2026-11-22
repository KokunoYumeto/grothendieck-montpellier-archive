"""Render explicitly selected original-source pages; rendering is not inspection."""
from pathlib import Path
import argparse, datetime, hashlib, json, re, time
import fitz
root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--source', required=True)
parser.add_argument('--tag', required=True)
parser.add_argument('--pages', required=True)
parser.add_argument('--width', type=int, default=1600)
args = parser.parse_args()
assert re.fullmatch(r'[A-Za-z0-9_-]+', args.tag)
pages = [int(number) for number in args.pages.split(',')]
source = root / args.source
started = time.perf_counter()
images = []
with fitz.open(source) as document:
    for number in pages:
        page = document[number - 1]
        target = root / 'sources' / f'{args.tag}_p{number:03d}.png'
        scale = args.width / page.rect.width
        page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False).save(target)
        images.append(str(target.relative_to(root)))
record = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'source': args.source, 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
          'physical_pdf_pages': pages, 'rendered_width': args.width, 'images': images,
          'visual_inspection': 'Not implied by rendering; record actual image displays separately.',
          'elapsed_seconds': time.perf_counter() - started}
(root / 'logs' / ('render_source_pages_' + args.tag + '.json')).write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
