from pathlib import Path
import urllib.request
import hashlib
import subprocess
import concurrent.futures

root = Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
sources = [
 ('CartanWeil2011', 'https://audin.pages.math.unistra.fr/livres/smf_doc-math_6.pdf'),
 ('CartanNotebooks2014', 'https://irma.math.unistra.fr/bib/attachments/cahierscartan.pdf'),
 ('CartanWeilRecovered1940', 'https://audin.pages.math.unistra.fr/histoire/EncoreUneLettre.pdf'),
]
def fetch(item):
    name, url = item
    result = {'name': name, 'url': url}
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(request, timeout=40) as response:
            data = response.read()
            result['final_url'] = response.url
            result['status'] = response.status
        path = root / f'notes/category_date_{name}.pdf'
        path.write_bytes(data)
        result['bytes'] = len(data)
        result['sha256'] = hashlib.sha256(data).hexdigest()
        command = ['pdftotext', '-layout', str(path), str(path.with_suffix('.txt'))]
        p = subprocess.run(command, capture_output=True, text=True)
        result['extraction_command'] = command
        result['extraction_status'] = p.returncode
        result['extraction_stdout'] = p.stdout
        result['extraction_stderr'] = p.stderr
    except Exception as e:
        result['error'] = repr(e)
    return result
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    for result in pool.map(fetch, sources):
        print(repr(result), flush=True)
