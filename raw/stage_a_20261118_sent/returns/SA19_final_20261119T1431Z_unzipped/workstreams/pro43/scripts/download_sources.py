"""Retrieve already-opened primary-source URLs; keep retrieval failures explicit."""
from pathlib import Path
from urllib.request import urlopen, Request
from concurrent.futures import ThreadPoolExecutor
import subprocess,sys
BASE=Path(__file__).resolve().parents[1]/'research'
SOURCES={
 'Oda1969':'https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf',
 'Serre1961':'https://www.numdam.org/item/BSMF_1961__89__105_0.pdf',
 'EGAIII1':'https://www.numdam.org/item/PMIHES_1961__11__5_0.pdf',
 'EGAIV3':'https://www.numdam.org/item/PMIHES_1966__28__5_0.pdf',
 'Atiyah1961':'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/atiyahthom.pdf',
 'RibeiroRosengarten2026':'https://gabribeiro.com/papers/extensions.pdf',
 'ArtinMilne1976':'https://www.jmilne.org/math/articles/1976c.pdf',
 'SGA2':'https://arxiv.org/pdf/math/0511279',
 'Cartan1951XV':'https://www.numdam.org/item/SHC_1950-1951__3__A15_0.pdf',
 'Cartan1951XVI':'https://www.numdam.org/item/SHC_1950-1951__3__A16_0.pdf',
}
def run(pair):
    name,url=pair; path=BASE/(name+'.pdf')
    try:
        if not path.exists():
            with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45) as response:
                data=response.read()
            if not data.startswith(b'%PDF'): raise ValueError('response is not a PDF')
            path.write_bytes(data)
        result=subprocess.run(['pdftotext','-layout',str(path),str(BASE/(name+'.txt'))],capture_output=True,text=True)
        return f'{name}\t{path.stat().st_size}\t{url}\tpdftotext={result.returncode}\t{result.stderr.strip()}'
    except Exception as e: return f'{name}\tFAILED\t{url}\t{type(e).__name__}: {e}'
if __name__=='__main__':
    selected={k:v for k,v in SOURCES.items() if not sys.argv[1:] or k in sys.argv[1:]}
    with ThreadPoolExecutor(max_workers=3) as pool:
        for line in pool.map(run,selected.items()): print(line,flush=True)
