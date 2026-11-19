"""Download already-identified primary sources for text extraction; failures are logged.
No archive scans are requested or consulted.
"""
from pathlib import Path
import urllib.request,subprocess,json,concurrent.futures
W=Path(__file__).resolve().parents[1]/'outputs'
sources={
 'EGAIV3':'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EGA/EGAIV.3.pdf',
 'PeruccaSgobba2019':'https://orbilu.uni.lu/bitstream/10993/35969/1/PeruccaSgobba-update.pdf',
 'Schinzel1977':'https://matwbn.icm.edu.pl/ksiazki/aa/aa32/aa3235.pdf',
 'IharaInvent1986':'https://link.springer.com/content/pdf/10.1007/BF01389262.pdf'}
def fetch(k,url):
 p=W/(k+'.pdf')
 try:
  if not p.exists():
   with urllib.request.urlopen(url,timeout=25) as f:p.write_bytes(f.read())
  subprocess.run(['pdftotext','-layout',str(p),str(W/(k+'.txt'))],check=True,capture_output=True)
  return {'key':k,'url':url,'status':'downloaded and pdftotext succeeded','bytes':p.stat().st_size}
 except Exception as e:return {'key':k,'url':url,'status':'failed','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 results=list(pool.map(lambda kv:fetch(*kv),sources.items()))
(W/'fetch_primary.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
