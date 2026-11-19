"""Archive primary sources opened for the Part C extensions; preserve failures."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request
import hashlib
import json
import subprocess
import time

root = Path(__file__).resolve().parents[2]
target = root / 'part_c/sources'
target.mkdir(exist_ok=True)
sources = [
    ('SGA7I_original', 'https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf'),
    ('illusie2014cd', 'https://www.numdam.org/item/AST_2014__363-364__455_0.pdf'),
    ('flachmorin2012topos', 'https://www.math.u-bordeaux.fr/~bmorin/Weiletaletopos05-20-12.pdf'),
    ('esnaultwittenberg2016', 'https://www.numdam.org/item/10.24033/asens.2288.pdf'),
    ('mukai1981', 'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/BDBEBAC584BE15236C2D62C383A34245/S002776300001922Xa.pdf/duality-between-dx-and-with-its-application-to-picard-sheaves.pdf'),
    ('fulaterveervial2021', 'https://irma.math.unistra.fr/~lfu/articles/MCK.pdf'),
    ('serre1970_local_factors', 'https://www.college-de-france.fr/media/jean-pierre-serre/UPL7750118224972622059_Serre_facteurs_locaux.pdf'),
]

def fetch(item):
    name, url = item
    start = time.perf_counter()
    path = target / (name + '.pdf')
    result = {'name': name, 'url': url}
    try:
        if not path.exists():
            request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (mathematical source verification)'})
            with urllib.request.urlopen(request, timeout=45) as response:
                data = response.read()
            assert data.startswith(b'%PDF'), 'not a PDF'
            path.write_bytes(data)
        data = path.read_bytes()
        text = target / (name + '.txt')
        subprocess.run(['pdftotext', '-layout', str(path), str(text)], check=True)
        result.update(status='saved', bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), text_bytes=text.stat().st_size)
    except Exception as exc:
        result.update(status='failed', error=str(exc))
    result['runtime_seconds'] = time.perf_counter()-start
    return result

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(fetch, sources))
output = {'sources': results, 'runtime_seconds': time.perf_counter()-start}
(root / 'code/part_c/fetch_new_sources_output.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps(output, indent=2))
