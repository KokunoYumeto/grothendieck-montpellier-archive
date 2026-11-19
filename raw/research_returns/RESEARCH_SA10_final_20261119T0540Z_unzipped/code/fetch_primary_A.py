#!/usr/bin/env python3
from pathlib import Path
import urllib.request, json, time, hashlib
root=Path('/workspace/scratch/83000dc30063'); dest=root/'primary';dest.mkdir(exist_ok=True)
sources={
 '151.pdf':'https://grothendieck.umontpellier.fr/151.pdf',
 'SGA4_tome1.pdf':'https://www.cmls.polytechnique.fr/perso/orgogozo/SGA4/tomes/tome1.pdf',
 'Schmitt_ModCurves.pdf':'https://www.math.uni-bonn.de/~schmitt/ModCurves/Script.pdf'}
for name,url in sources.items():
 t=time.perf_counter();p=dest/name
 if not p.exists():p.write_bytes(urllib.request.urlopen(url,timeout=60).read())
 print(json.dumps({'filename':name,'url':url,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'seconds':time.perf_counter()-t}),flush=True)
