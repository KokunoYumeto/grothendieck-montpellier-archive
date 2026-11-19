"""Retrieve public reference PDFs for local visual checking; cache is excluded from the deliverable."""
from pathlib import Path
import urllib.request, hashlib, json
cache=Path('reference_cache'); cache.mkdir(exist_ok=True)
urls={
 'standard_conjectures_check.pdf':'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf',
 'wittform.pdf':'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/wittform.pdf',
}
log=[]
for name,url in urls.items():
 p=cache/name
 try:
  if not p.exists(): p.write_bytes(urllib.request.urlopen(url,timeout=45).read())
  b=p.read_bytes(); log.append({'url':url,'cache':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
 except Exception as e: log.append({'url':url,'error':str(e)})
print(json.dumps(log,indent=2))
Path('SA05/work/cote11b/outputs/reference_acquisition.json').write_text(json.dumps(log,indent=2)+'\n')
