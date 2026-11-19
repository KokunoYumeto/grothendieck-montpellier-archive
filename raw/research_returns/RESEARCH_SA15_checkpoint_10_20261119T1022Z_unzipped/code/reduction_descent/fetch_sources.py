from pathlib import Path
import urllib.request,subprocess,concurrent.futures
p=Path(__file__).resolve().parents[1]/'sources'
items=[
 ('drinfeld_elliptic','https://math.hawaii.edu/~xander/sp12_drinfeld/Drinfeld%20--%20Elliptic%20Modules%20I.pdf'),
 ('serre_tate_good','https://www.wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf'),
 ('kisin_crystalline','https://people.math.harvard.edu/~kisin/papers/crys.pdf'),
 ('kisin_moduli','https://annals.math.princeton.edu/wp-content/uploads/annals-v170-n3-p03.pdf'),
]
def f(item):
 name,url=item
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  b=urllib.request.urlopen(req,timeout=18).read()
  if not b.startswith(b'%PDF'):return (name,url,'not PDF',len(b))
  (p/(name+'.pdf')).write_bytes(b)
  proc=subprocess.run(['pdftotext','-layout',str(p/(name+'.pdf')),str(p/(name+'.txt'))],capture_output=True)
  return (name,url,'downloaded',len(b),proc.returncode)
 except Exception as e:return (name,url,str(e))
with concurrent.futures.ThreadPoolExecutor() as pool:
 for row in pool.map(f,items):print(row,flush=True)
