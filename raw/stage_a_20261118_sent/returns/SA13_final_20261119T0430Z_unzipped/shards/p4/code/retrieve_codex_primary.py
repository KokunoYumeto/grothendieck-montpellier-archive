"""Retrieve discovered, public original primary texts; raw PDFs stay in work."""
from pathlib import Path
import urllib.request,hashlib,json,subprocess,concurrent.futures
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).resolve().parents[1]/'outputs'
WORK=ROOT/'work/p4_primary'
URLS={
 'deligne_sga45.pdf':'https://publications.ias.edu/sites/default/files/Number32.pdf',
 'sga4h_original.pdf':'https://library.slmath.org/nonmsri/sga/sga/pdf/sga4h.pdf',
 'sga7ii_original.pdf':'https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-2.pdf',
 'riou_purity2014.pdf':'https://www.numdam.org/item/AST_2014__363-364__301_0.pdf',
 'illusie_log2002.pdf':'https://www.numdam.org/item/AST_2002__279__271_0.pdf',
 'illusie2021.pdf':'https://www.imo.universite-paris-saclay.fr/~illusie/Illusie-Grothendieck-nearby-cycles12.pdf',
 'rapoport_zink1982.pdf':'https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/UeberdielokaleZetafunktion.pdf',
 'pilloni_stroh2014.pdf':'https://www.numdam.org/item/AST_2014__363-364__293_0.pdf'
}
def fetch(pair):
 name,url=pair
 try:
  p=WORK/name
  if p.exists() and p.read_bytes().startswith(b'%PDF'):
   data=p.read_bytes()
   return dict(file=name,url=url,final_url=url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),status='cached prior public download')
  with urllib.request.urlopen(url,timeout=35) as r: data=r.read(); final=r.url
  assert data.startswith(b'%PDF'),'not PDF'
  p.write_bytes(data)
  subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
  return dict(file=name,url=url,final_url=final,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),status='downloaded and extracted')
 except Exception as e:return dict(file=name,url=url,status='failed',error=str(e))
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: rows=list(pool.map(fetch,URLS.items()))
 (OUT/'codex_primary_manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
 for r in rows:print(r['file'],r['status'],r.get('bytes',r.get('error')))
