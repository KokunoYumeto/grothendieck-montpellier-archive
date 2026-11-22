"""OCR the whole accessible memoir printing for a documented negative source check.

This is source retrieval, not a mathematical proof or first-printing collation.
The source scan explicitly identifies itself as the fourth printing (1966).
"""
from pathlib import Path
import concurrent.futures, datetime, hashlib, json, os, subprocess, tempfile, time
import fitz

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'notes/geometry_PTT_1966_scan.pdf'
OUT = ROOT / 'sources/root_memoir_ocr'
OUT.mkdir(parents=True, exist_ok=True)

def page_ocr(index):
    started = time.monotonic()
    target = OUT / f'page_{index+1:03}.txt'
    with tempfile.TemporaryDirectory(prefix='memoir_page_') as tmp:
        image = Path(tmp) / 'page.png'
        with fitz.open(SOURCE) as doc:
            doc[index].get_pixmap(dpi=135).save(image)
        env = dict(os.environ, OMP_THREAD_LIMIT='1')
        run = subprocess.run(['tesseract', str(image), 'stdout', '-l', 'eng',
                              '--psm', '3'], capture_output=True, text=True, env=env)
        if run.returncode:
            raise RuntimeError(f'Page {index+1}: {run.stderr}')
        target.write_text(run.stdout)
        return {'page':index+1, 'seconds':time.monotonic()-started,
                'characters':len(run.stdout)}

if __name__ == '__main__':
    started = time.monotonic()
    with fitz.open(SOURCE) as doc:
        count = len(doc)
    records = []
    workers = min(12, os.cpu_count() or 1)
    print(f'OCR {count} pages; {workers} workers; fourth printing 1966', flush=True)
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
        jobs = [pool.submit(page_ocr, i) for i in range(count)]
        for job in concurrent.futures.as_completed(jobs):
            records.append(job.result())
            if len(records) % 50 == 0:
                print(f'Completed {len(records)}/{count}', flush=True)
    records.sort(key=lambda x:x['page'])
    combined = ''.join(f'\n\n=== PDF PAGE {i:03} ===\n'+
                       (OUT/f'page_{i:03}.txt').read_text()
                       for i in range(1,count+1))
    (OUT/'complete_text.txt').write_text(combined)
    result = {'source':str(SOURCE.relative_to(ROOT)),
              'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'printing':'fourth printing 1966; copyright1955',
              'pages':count,'workers':workers,
              'seconds':time.monotonic()-started,'records':records,
              'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    (ROOT/'logs/root_ocr_memoir.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='records'}),flush=True)
