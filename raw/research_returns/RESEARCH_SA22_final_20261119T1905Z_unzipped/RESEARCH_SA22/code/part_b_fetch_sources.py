#!/usr/bin/env python3
"""Reproducible primary-source retrieval for Part B; preserves existing PDFs."""
import concurrent.futures, hashlib, json, subprocess, time, urllib.request
from pathlib import Path

root=Path(__file__).resolve().parents[1]
sources=root/'sources'
jobs=[
 ('milne_adt.pdf','https://jmilne.org/math/Books/ADTnot.pdf'),
 ('deligne_milne_tc.pdf','https://www.math.columbia.edu/~dejong/tannakian/Deligne-Milne-Tannakian-Categories.pdf'),
 ('greenberg1966.pdf','https://www.numdam.org/item/PMIHES_1966__31__59_0.pdf'),
 ('cisinski_deglise_motives.pdf','https://arxiv.org/pdf/0912.2110'),
 ('saito_charcycle.pdf','https://arxiv.org/pdf/1510.03018'),
 ('geisser_duality.pdf','https://arxiv.org/pdf/math/0608456'),
 ('artin1969_approx.pdf','https://www.numdam.org/item/PMIHES_1969__36__23_0.pdf'),
 ('raynaud_picard1970.pdf','https://www.numdam.org/item/PMIHES_1970__38__27_0.pdf'),
 ('sga4_xiv.pdf','https://www.normalesup.org/~forgogozo/SGA4/14/14.pdf'),
 ('sga4_xviii.pdf','https://www.normalesup.org/~forgogozo/SGA4/18/18.pdf'),
 ('sga4_xii.pdf','https://www.normalesup.org/~forgogozo/SGA4/12/12.pdf'),
 ('sga4_xvi.pdf','https://www.normalesup.org/~forgogozo/SGA4/16/16.pdf'),
 ('kleiman1968.pdf','https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf'),
 ('mumford1969.pdf','https://www.dam.brown.edu/people/mumford/alg_geom/papers/1969e--0-cycles-Euclid.pdf'),
 ('kahn2003.pdf','https://numdam.org/item/10.1016/j.ansens.2003.02.002.pdf'),
 ('broe.pdf','https://arxiv.org/pdf/2608.28651'),
 ('haine2024.pdf','https://math.berkeley.edu/~phaine/files/nonabelian_basechange_etale_homotopy-published.pdf'),
 ('ceresa_collino1983.pdf','https://msp.org/pjm/1983/105-2/pjm-v105-n2-p04-s.pdf'),
 ('voisin_hodge.pdf','https://www.cmls.polytechnique.fr/perso/voisin/Articlesweb/template.pdf'),
 ('bloch_excerpt.pdf','https://assets.cambridge.org/97805211/18422/excerpt/9780521118422_excerpt.pdf'),
]
def fetch(job):
 name,url=job;start=time.perf_counter();p=sources/name
 try:
  status='existing'
  if not p.exists():
   b=urllib.request.urlopen(url,timeout=25).read()
   if not b.startswith(b'%PDF'):return {'file':name,'url':url,'status':'non-PDF','bytes':len(b)}
   p.write_bytes(b);status='downloaded'
  b=p.read_bytes()
  if not p.with_suffix('.txt').exists():subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True,check=True)
  return {'file':name,'url':url,'status':status,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'seconds':time.perf_counter()-start}
 except Exception as e:return {'file':name,'url':url,'status':'error','error':str(e),'seconds':time.perf_counter()-start}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:results=list(ex.map(fetch,jobs))
(root/'code'/'part_b_fetch_sources_output.json').write_text(json.dumps(results,indent=2)+'\n')
for r in results:print(r['file'],r['status'],r.get('bytes',r.get('error')))
