"""Render a PDF for visual review and create labelled contact sheets.

The initial render command was run explicitly before this script was saved;
without --render this script reuses those exact PNGs. No mathematical check is
inferred from visual review. Human/AI observations are recorded separately.
"""
from pathlib import Path
import argparse, hashlib, json, subprocess, time
from PIL import Image, ImageDraw
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--render', action='store_true')
args = parser.parse_args()
start = time.perf_counter()
qa = ROOT / 'qa'
qa.mkdir(exist_ok=True)
command = ['pdftoppm', '-r', '90', '-png', str(ROOT/'RESEARCH_SA09_paper.pdf'), str(qa/'page')]
previous={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in qa.glob('page-*.png')}
if args.render:
    for old in list(qa.glob('page-*.png')) + list(qa.glob('contact-*.png')):
        old.unlink()
    subprocess.run(command, check=True)
pages = sorted(qa.glob('page-*.png'))
assert len(pages) == len(PdfReader(ROOT/'RESEARCH_SA09_paper.pdf').pages)
sheets = []
for start_page in range(0, len(pages), 6):
    canvas = Image.new('RGB', (1390, 1320), '#d8dde3')
    draw = ImageDraw.Draw(canvas)
    for offset, path in enumerate(pages[start_page:start_page+6]):
        im = Image.open(path).convert('RGB')
        im.thumbnail((450, 635))
        x, y = (offset % 3) * 460 + 10, (offset // 3) * 655 + 24
        canvas.paste(im, (x, y))
        draw.text((x, y-19), 'Page '+str(start_page+offset+1), fill='black')
    name = qa / ('contact-%02d.png' % (start_page//6+1))
    canvas.save(name)
    sheets.append(name.name)
result = {'render_command':command, 'dpi':90, 'rendered_page_count':len(pages),
          'contact_sheets':sheets, 'script_runtime_seconds':round(time.perf_counter()-start,6),
          'render_rerun':args.render}
(qa/'render_manifest.json').write_text(json.dumps(result,indent=2))
current={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in pages}
comparison={'previous_page_count':len(previous),'final_page_count':len(current),
 'unchanged_pages':[name for name in current if previous.get(name)==current[name]],
 'changed_or_new_pages':[name for name in current if previous.get(name)!=current[name]],
 'final_pdf_sha256':hashlib.sha256((ROOT/'RESEARCH_SA09_paper.pdf').read_bytes()).hexdigest()}
(qa/'final_image_comparison.json').write_text(json.dumps(comparison,indent=2))
print(json.dumps(result))
print(json.dumps(comparison))
