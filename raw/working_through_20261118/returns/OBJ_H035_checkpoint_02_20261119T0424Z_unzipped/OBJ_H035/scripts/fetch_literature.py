"""Fetch opened primary literature for exact-locator checks; no manuscript OCR."""
from pathlib import Path
from urllib.request import urlopen
from datetime import datetime, timezone
import hashlib
import subprocess

root = Path(__file__).resolve().parents[2]
out = root / 'sources' / 'literature'
out.mkdir(exist_ok=True)
sources = {
    'EGA_III_2': 'https://www.numdam.org/item/PMIHES_1963__17__5_0.pdf',
    'EGA_IV_2': 'https://www.numdam.org/item/PMIHES_1965__24__5_0.pdf',
    'Murre_294': 'https://www.numdam.org/article/SB_1964-1966__9__243_0.pdf',
}
for key, url in sources.items():
    target = out / (key + '.pdf')
    try:
        if not target.exists():
            with urlopen(url, timeout=50) as r:
                data = r.read()
            if not data.startswith(b'%PDF'):
                raise ValueError('not a PDF')
            target.write_bytes(data)
        data = target.read_bytes()
        print(datetime.now(timezone.utc).isoformat(), key, url, len(data), hashlib.sha256(data).hexdigest(), flush=True)
        subprocess.run(['pdftotext','-layout',str(target),str(target.with_suffix('.txt'))],check=True)
    except Exception as e:
        print(key, type(e).__name__, str(e), flush=True)
