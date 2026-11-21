"""Fetch only the public primary sixth-power audit sources."""
from pathlib import Path
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import hashlib,json
HERE=Path(__file__).resolve().parent/'sixth_source_audit'
BASE='https://raw.githubusercontent.com/openai/math/main/'
PAPER='preprints/Foulkes-Conjecture-for-the-Sixth-Symmetric-Power-September-25-2026/'
FILES={
 'verification/verify_computations.py':PAPER+'verification/verify_computations.py',
 'README.md':PAPER+'README.md',
 'LEAN_SCOPE_210.md':'lean/docs/210.md',
}
for name in (
 'verification/programs/appendix-a.cpp',
 'verification/programs/appendix-b.cpp',
 'verification/support/expected-results.json',
 'verification/support/expected/appendix-a.stdout',
 'verification/support/expected/appendix-a.stderr',
 'verification/support/expected/appendix-b.stdout',
 'verification/support/expected/appendix-b.stderr',
 'build/sections/certificates.tex',
 'build/sections/verification.tex',
):
    FILES[name]=PAPER+name
def fetch(item):
    rel,remote=item
    raw=urlopen(BASE+remote,timeout=40).read()
    dest=HERE/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
    return dict(path=rel,url=BASE+remote,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def main():
    data=list(ThreadPoolExecutor(max_workers=4).map(fetch,FILES.items()))
    (HERE/'PRIMARY_FETCH.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
if __name__=='__main__':main()

