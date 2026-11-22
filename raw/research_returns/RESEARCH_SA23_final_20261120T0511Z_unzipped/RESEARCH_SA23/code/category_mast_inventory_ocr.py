from pathlib import Path
import subprocess
import concurrent.futures
import hashlib
import json
import os
import time

root = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
source = root / 'sources/mast_cnpq_inventory2025.pdf'
out = root / 'notes/category_mast_inventory_ocr'
out.mkdir(exist_ok=True)
selected_images = {1, 2, 3, 40, 41, 42, 43, 44, 45, 46, 47, 48, 187, 188, 189}
print(json.dumps({'source': str(source), 'sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'pages': 189, 'purpose': 'Public inventory OCR finding aid; all relevant claims require visual checking', 'scale_to': 1800, 'ocr_language': 'eng', 'workers': 4}), flush=True)

def process(page):
    started = time.monotonic()
    render = ['pdftoppm', '-f', str(page), '-l', str(page), '-singlefile', '-scale-to', '1800', '-png', str(source)]
    r = subprocess.run(render, capture_output=True, timeout=60)
    if r.returncode:
        return {'page': page, 'render_command': render, 'error': r.stderr.decode(errors='replace'), 'status': r.returncode}
    if page in selected_images:
        (out / f'page_{page:03d}.png').write_bytes(r.stdout)
    command = ['tesseract', 'stdin', 'stdout', '-l', 'eng', '--psm', '3']
    environment = os.environ.copy()
    environment['OMP_THREAD_LIMIT'] = '1'
    o = subprocess.run(command, input=r.stdout, capture_output=True, env=environment, timeout=60)
    (out / f'page_{page:03d}.txt').write_bytes(o.stdout)
    record = {'page': page, 'render_command': render, 'render_status': r.returncode,
              'render_stderr': r.stderr.decode(errors='replace'),
              'image_bytes': len(r.stdout), 'image_sha256': hashlib.sha256(r.stdout).hexdigest(),
              'image_retained': page in selected_images, 'ocr_command': command,
              'ocr_status': o.returncode, 'ocr_stderr': o.stderr.decode(errors='replace'),
              'text_bytes': len(o.stdout), 'text_sha256': hashlib.sha256(o.stdout).hexdigest(),
              'seconds': round(time.monotonic()-started, 3)}
    (out / f'page_{page:03d}.json').write_text(json.dumps(record, indent=2)+'\n')
    return record

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for record in pool.map(process, range(1, 190)):
        print(json.dumps(record), flush=True)
full = ''.join(f'\n===== PHYSICAL PDF PAGE {page} =====\n'+(out / f'page_{page:03d}.txt').read_text() for page in range(1,190))
(root / 'notes/category_mast_inventory_full.txt').write_text(full)
print(json.dumps({'complete': True, 'full_text_characters': len(full), 'ocr_is_finding_aid_only': True}), flush=True)
