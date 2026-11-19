#!/usr/bin/env python3
"""Fresh recovery downloads; retain measured times, URLs and hashes."""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import urllib.request, hashlib, json, concurrent.futures
root=Path(__file__).resolve().parents[1]
(root/'sources').mkdir(exist_ok=True)
(root/'output').mkdir(exist_ok=True)
items=[
 ('van_der_Kallen1971_dual_numbers.pdf','https://webspace.science.uu.nl/~kalle101/K2nd1971.pdf'),
 ('Weibel_Kbook_III.pdf','https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf'),
 ('ClingherMalmendierShaska2021_prym.pdf','https://arxiv.org/pdf/2005.04839v2'),
 ('JiangLiLu2026_derived_supersingular.pdf','https://arxiv.org/pdf/2610.24666v1'),
 ('GrossKaurUlirschWerner2026_semihomogeneous.pdf','https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6C9081AB500C372415662A2B2ED3339D/S2949764726100228a.pdf/semihomogeneous_vector_bundles_on_abelian_varieties_moduli_spaces_and_their_tropicalization.pdf'),
]
def fetch(item):
 name,url=item; start=perf_counter(); path=root/'sources'/name
 record={'filename':name,'url':url,'reconstructed_after_reset':True}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=45) as response: data=response.read()
  if not data.startswith(b'%PDF'): raise ValueError('Response is not a PDF')
  path.write_bytes(data)
  record.update(status='success',bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 except Exception as exc: record.update(status='failed',error=str(exc))
 record.update(utc=datetime.now(timezone.utc).isoformat(),seconds=perf_counter()-start)
 return record
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
 records=list(pool.map(fetch,items))
for record in records: print(json.dumps(record,sort_keys=True),flush=True)
(root/'output'/'residual_and_K2_sources_manifest.json').write_text(json.dumps(records,indent=2)+'\n')
