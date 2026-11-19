"""Fetch primary printed literature only; pdftotext is never used on manuscripts."""
from pathlib import Path
from urllib.request import urlopen
from datetime import datetime, timezone
import hashlib
import subprocess

root = Path(__file__).resolve().parents[2]
out = root / 'sources' / 'literature'
sources = {
    'EGA_III_1': 'https://www.numdam.org/item/PMIHES_1961__11__5_0.pdf',
    'Illusie_formal_2004': 'https://indico.ictp.it/event/a0255/session/14/contribution/9/material/0/0.pdf',
    'Bourbaki_Topologie_5_10': 'https://www.devoir.tn/superieur/Doc/Livres/Math%C3%A9matiques/Maths-cours-de-reference-350-livres/Bourbaki/Topologie-g%C3%A9n%C3%A9rale/Topologie-G%C3%A9n%C3%A9rale-Chapitres-5-%C3%A0-10-El%C3%A9ments-de-Math%C3%A9matique-N-Bourbaki.pdf',
}
for key, url in sources.items():
    target = out / (key + '.pdf')
    try:
        if not target.exists():
            with urlopen(url, timeout=45) as response:
                data = response.read()
            if not data.startswith(b'%PDF'):
                raise ValueError('not a PDF')
            target.write_bytes(data)
        data = target.read_bytes()
        print(datetime.now(timezone.utc).isoformat(), key, url, len(data), hashlib.sha256(data).hexdigest(), flush=True)
        subprocess.run(['pdftotext', '-layout', str(target), str(target.with_suffix('.txt'))], check=True)
    except Exception as exc:
        print(key, type(exc).__name__, str(exc), flush=True)
