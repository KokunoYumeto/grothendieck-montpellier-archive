"""OCR a declared public PDF as a finding aid, retaining measured page coverage."""
from pathlib import Path
import argparse, concurrent.futures, datetime, hashlib, json, os, re, subprocess, tempfile, time
import fitz
root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--source', required=True)
parser.add_argument('--tag', required=True)
parser.add_argument('--pattern', default='Groth|Fredholm|Nachbin|Hilbert|tensor|Summa|IMPA')
parser.add_argument('--workers', type=int, default=6)
args = parser.parse_args()
assert re.fullmatch(r'[A-Za-z0-9_-]+', args.tag)
source = root / args.source
out = root / 'sources' / (args.tag + '_ocr')
out.mkdir(parents=True, exist_ok=True)
started = time.perf_counter()
with fitz.open(source) as doc:
    count = len(doc)
def read_page(index):
    begin = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix=args.tag + '_') as temporary:
        image = Path(temporary) / 'page.png'
        with fitz.open(source) as doc:
            doc[index].get_pixmap(dpi=150, alpha=False).save(image)
        result = subprocess.run(['tesseract', str(image), 'stdout', '-l', 'eng', '--psm', '3'],
                                capture_output=True, text=True,
                                env=dict(os.environ, OMP_THREAD_LIMIT='1'))
        if result.returncode:
            raise RuntimeError(f'Page {index+1}: {result.stderr}')
        (out / f'page_{index+1:03d}.txt').write_text(result.stdout)
        return {'pdf_page': index + 1, 'characters': len(result.stdout),
                'elapsed_seconds': time.perf_counter() - begin,
                'diagnostic': result.stderr.strip()}
with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
    records = list(pool.map(read_page, range(count)))
pattern = re.compile(args.pattern, re.IGNORECASE)
hits = []
combined = []
for index in range(1, count + 1):
    text = (out / f'page_{index:03d}.txt').read_text()
    combined.append(f'\n=== PHYSICAL PDF PAGE {index} ===\n{text}')
    matched = [{'line': number, 'text': line} for number, line in enumerate(text.splitlines(), 1)
               if pattern.search(line)]
    if matched:
        hits.append({'pdf_page': index, 'matches': matched, 'full_page_ocr': text,
                     'visual_verification': 'not implied by OCR'})
(out / 'complete_text.txt').write_text('\n'.join(combined))
(root / 'notes' / (args.tag + '_hits.json')).write_text(json.dumps(hits, ensure_ascii=False, indent=2) + '\n')
record = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'source': args.source, 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
          'pages': count, 'workers': args.workers, 'dpi': 150, 'language_model': 'eng',
          'pattern': args.pattern, 'hit_pages': [hit['pdf_page'] for hit in hits],
          'source_status': 'OCR finding aid only; relevant source images require direct visual verification.',
          'elapsed_seconds': time.perf_counter() - started, 'per_page': records}
(root / 'logs' / ('ocr_public_pdf_' + args.tag + '.json')).write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({key:value for key,value in record.items() if key != 'per_page'}, indent=2))
