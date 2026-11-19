"""Fetch already identified primary scholarly sources, retaining exact byte files and logs."""
from pathlib import Path
import urllib.request,subprocess,json,sys,datetime
R=Path(__file__).resolve().parents[1]; O=R/'work/early/references'; O.mkdir(parents=True,exist_ok=True)
sources={
 'sullivan_1975':'https://www.math.stonybrook.edu/~dennis/publications/PDF/DS-pub-0017.pdf',
 'dgms_1975':'https://www.math.stonybrook.edu/~dennis/publications/PDF/DS-pub-0024.pdf',
 'nagpal_snowden_2016':'https://websites.umich.edu/~asnowden/papers/dp-061016.pdf',
 'horel_2024':'https://geoffroy.horel.org/binomial.pdf',
 'cenkl_1989':'https://msp.org/pjm/1989/140-1/pjm-v140-n1-p02-p.pdf',
 'garvin_1998':'https://matwbn.icm.edu.pl/ksiazki/bcp/bcp45/bcp45112.pdf',
 'ekedahl_2002':'https://arxiv.org/pdf/math/0107004',
 'pursuing_stacks':'https://arxiv.org/pdf/2111.01000',
}
for key in sys.argv[1:] or sources:
 url=sources[key]; p=O/(key+'.pdf')
 try:
  if not p.exists():
   req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
   p.write_bytes(urllib.request.urlopen(req,timeout=30).read())
  if p.read_bytes()[:4]!=b'%PDF': raise ValueError('not PDF')
  cp=subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True,text=True)
  print(json.dumps({'date':datetime.datetime.now(datetime.timezone.utc).isoformat(),'key':key,'url':url,'bytes':p.stat().st_size,'pdftotext_returncode':cp.returncode,'stderr':cp.stderr}))
 except Exception as ex: print(json.dumps({'key':key,'url':url,'error':repr(ex)}))
