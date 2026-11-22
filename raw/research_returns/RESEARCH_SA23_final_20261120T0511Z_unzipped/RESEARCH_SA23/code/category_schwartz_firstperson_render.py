"""Render original retrospectives for bounded visual source inspection."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess

ROOT = Path(__file__).resolve().parents[1]
jobs = {
    'historical_roots1982': [1, 2, 3, 19],
    'souvenirs_dieudonne1994': [1, 2, 3, 4],
}
records = []
for stem, pages in jobs.items():
    pdf = ROOT / 'sources' / f'category_schwartz_{stem}.pdf'
    folder = ROOT / 'sources' / f'category_schwartz_{stem}_pages'
    folder.mkdir(exist_ok=True)
    for page in pages:
        prefix = folder / f'page_{page:02d}'
        command = ['pdftoppm', '-f', str(page), '-l', str(page), '-singlefile',
                   '-scale-to', '2400', '-png', str(pdf), str(prefix)]
        proc = subprocess.run(command, capture_output=True, timeout=40)
        image = prefix.with_suffix('.png')
        row = {'source': str(pdf.relative_to(ROOT)), 'page': page,
               'source_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
               'utc': datetime.now(timezone.utc).isoformat(), 'command': command,
               'returncode': proc.returncode, 'stdout': proc.stdout.decode(errors='replace'),
               'stderr': proc.stderr.decode(errors='replace')}
        if image.exists():
            row.update(image=str(image.relative_to(ROOT)),
                       image_sha256=hashlib.sha256(image.read_bytes()).hexdigest())
        records.append(row)
        print(json.dumps(row, ensure_ascii=False), flush=True)
        if proc.returncode: raise RuntimeError('Rendering failed')
        (ROOT / 'logs/category_schwartz_firstperson_render.json').write_text(
            json.dumps(records, ensure_ascii=False, indent=2) + '\n')
