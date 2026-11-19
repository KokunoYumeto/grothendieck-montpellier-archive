"""Reproduce the root's public primary-source cache; no mathematical computation.

Existing files are hashed, not downloaded again. Failed requests remain explicit.
The first four entries were initially fetched in an interactive Python cell;
this file records their exact URLs and reproducible retrieval procedure.
"""
from pathlib import Path
import concurrent.futures, hashlib, json, time, urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / 'sources'
URLS = {
    'cote67.pdf': 'https://grothendieck.umontpellier.fr/67.pdf',
    'hubbard_koch.pdf': 'https://arxiv.org/pdf/1301.0062',
    'hubbard_koch_source.tar': 'https://arxiv.org/src/1301.0062',
    'mondello.pdf': 'https://arxiv.org/pdf/0804.0605',
    'mondello_source.tar': 'https://arxiv.org/src/0804.0605',
    'wolpert_cusps.pdf': 'https://www.math.umd.edu/~swolpert/preprints/Cusps.pdf',
    'wolpert_universal.pdf': 'https://math.umd.edu/~swolpert/preprints/The_families_hyperbolic_metric.pdf',
    'penner1987.pdf': 'https://macbuse.github.io/GRENOBLE/1104160216.pdf',
    'beurling_ahlfors.pdf': 'https://www.math.stonybrook.edu/~bishop/classes/math638.F20/Beurling-Ahlfors.pdf',
    'bishop2007.pdf': 'https://annals.math.princeton.edu/wp-content/uploads/annals-v166-n3-p01.pdf',
    'firat_three.pdf': 'https://arxiv.org/pdf/2102.03936',
    'firat_three.tar': 'https://arxiv.org/src/2102.03936',
    'firat_bootstrap.pdf': 'https://arxiv.org/pdf/2302.12843',
    'firat_bootstrap.tar': 'https://arxiv.org/src/2302.12843',
    'kra1990.pdf': 'https://www.ams.org/jams/1990-03-03/S0894-0347-1990-1049503-1/S0894-0347-1990-1049503-1.pdf',
    'earle_marden2012.pdf': 'https://www.ams.org/books/conm/575/11411/conm575-11411.pdf',
    'hinich_plumbing.pdf': 'https://arxiv.org/pdf/math/0606240',
    'hinich_plumbing_source.tar': 'https://arxiv.org/src/math/0606240',
    'taylor_dton.pdf': 'https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/dton.pdf',
}

def fetch(item):
    name, url = item
    target = SOURCES / name
    before = time.monotonic()
    try:
        cached = target.exists()
        if cached:
            content = target.read_bytes()
        else:
            request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(request, timeout=45) as response:
                content = response.read()
            if name.endswith('.pdf') and not content.startswith(b'%PDF'):
                raise ValueError('Response is not a PDF')
            target.write_bytes(content)
        return dict(file=name, url=url, bytes=len(content), cached=cached,
                    sha256=hashlib.sha256(content).hexdigest(),
                    seconds=round(time.monotonic()-before, 6), status='available')
    except Exception as error:
        return dict(file=name, url=url, seconds=round(time.monotonic()-before, 6),
                    status='failed', error=str(error))

if __name__ == '__main__':
    SOURCES.mkdir(exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        records=list(executor.map(fetch, URLS.items()))
    output=ROOT/'code'/'part_a_fetch_sources_output.json'
    output.write_text(json.dumps(records, indent=2)+'\n')
    print(json.dumps(records, indent=2))
