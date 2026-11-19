"""Download already identified public primary sources for exact page inspection."""
from pathlib import Path
import urllib.request,subprocess
ROOT=Path(__file__).resolve().parents[4]
DEST=ROOT/'work/p3_primary'
DEST.mkdir(exist_ok=True)
sources={
 'sga7xx':'https://web.math.princeton.edu/~nmk/old/thmgrif.pdf',
 'sga7xviii':'https://web.math.princeton.edu/~nmk/old/etudecoho.pdf',
 'sga7xxi':'https://web.math.princeton.edu/~nmk/old/niveaucoho.pdf',
 'sga7xxii':'https://web.math.princeton.edu/~nmk/old/congzeta.pdf',
 'sga4xvii_xviii':'https://publications.ias.edu/sites/default/files/Number4.pdf',
}
for name,url in sources.items():
    path=DEST/(name+'.pdf')
    try:
        if not path.exists():
            req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
            with urllib.request.urlopen(req,timeout=30) as f: data=f.read()
            if not data.startswith(b'%PDF'): raise ValueError('not a PDF')
            path.write_bytes(data)
        subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True)
        print(name, path.stat().st_size,'bytes; downloaded and text extracted')
    except Exception as e:
        print(name,type(e).__name__,str(e))
