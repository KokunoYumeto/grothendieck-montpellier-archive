"""Render a reproducible spread and selected changed sections for actual visual review."""
from pathlib import Path
import argparse, datetime, hashlib, json, re, time
import fitz

parser = argparse.ArgumentParser()
parser.add_argument('--tag', required=True)
args = parser.parse_args()
assert re.fullmatch(r'[a-zA-Z0-9_-]+', args.tag)
root = Path(__file__).resolve().parents[1]
start = time.perf_counter()
pdf = root/'RESEARCH_SA23_paper.pdf'
doc = fitz.open(pdf)
diagnostics = json.loads((root/'logs/build_diagnostics.json').read_text())
assert all(item['returncode'] == 0 for item in diagnostics['commands'])
assert len(diagnostics['commands']) == 4
assert diagnostics['overfull_gt_2pt'] == 0
texts = [' '.join(page.get_text().split()).casefold() for page in doc]
pages = set(number for number in [1,20,40,60,len(doc)] if number <= len(doc))
anchors = {}
for key, needle, following in [
    ('alternative1956', 'a complete reconstruction from the printed', 2),
    ('remaining_date', 'the remaining documentary question', 1),
    ('abelian_stack', 'the unrestricted abelian moduli stack fails', 0),
]:
    hits = [i+1 for i, text in enumerate(texts) if needle in text]
    # A contents-page hit is not a section inspection target.
    hits = [number for number in hits if number > 4]
    anchors[key] = hits
    for number in hits:
        pages.update(range(number,min(len(doc),number+following)+1))
paths = []
for number in sorted(pages):
    path = root/'verification'/f'paper_{args.tag}_{number:03d}.png'
    doc[number-1].get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False).save(path)
    paths.append(str(path.relative_to(root)))
record = {'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'tag':args.tag, 'pdf_pages':len(doc), 'pages_rendered':sorted(pages),
          'anchors':anchors, 'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
          'rendered':paths, 'visual_inspection':'pending direct image inspection',
          'build_overfull_count':diagnostics['overfull_count'],
          'build_overfull_gt_2pt':diagnostics['overfull_gt_2pt'],
          'elapsed_seconds':time.perf_counter()-start}
(root/'logs'/f'root_pdf_review_{args.tag}.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
