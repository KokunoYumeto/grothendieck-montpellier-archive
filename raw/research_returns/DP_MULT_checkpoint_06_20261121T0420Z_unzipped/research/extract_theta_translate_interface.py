#!/usr/bin/env python3
"""Recover exact theta-translate declarations for DP59, not a global audit."""
from pathlib import Path
import sys,tarfile,re,json,hashlib
from datetime import datetime,timezone
here=Path(__file__).resolve().parent
sys.path.insert(0,str(here))
from verify_author_archive import PartsReader
root=here/'external_lean';parts=here.parents[1]/'author_archive'
exact={'ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ExtensionDescent/ThetaVV.lean'}
pat=re.compile(r'\b(?:def|abbrev|structure|theorem)\s+(?:SymLift|IsNormMul|ThetaGrp|Level)\b|\bMb\s*:')
prefixes=('ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/','ReciprocityTheory/ChartRestriction/')
records=[];started=datetime.now(timezone.utc).isoformat();scanned=0
with tarfile.open(fileobj=PartsReader([parts/f'lean.tar.gz.part{i:02d}' for i in range(1,15)]),mode='r|gz') as ar:
 for m in ar:
  if not m.isfile() or not m.name.startswith('lean/src/') or not m.name.endswith('.lean'):continue
  p=m.name[len('lean/src/'):]
  if p not in exact and not p.startswith(prefixes):continue
  data=ar.extractfile(m).read();txt=data.decode('utf-8');matches=[(i+1,l) for i,l in enumerate(txt.splitlines()) if pat.search(l)];scanned+=1
  if p not in exact and not matches:continue
  dest=root/p;old=dest.read_bytes() if dest.exists() else None
  if old is not None and old!=data:raise RuntimeError('Existing source differs: '+p)
  dest.parent.mkdir(parents=True,exist_ok=True)
  if old is None:dest.write_bytes(data)
  records.append({'path':p,'author_archive_member':m.name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'new_file':old is None,'matches':matches,'reading_scope':'Recovery and symbol scan only; subsequent targeted readings recorded separately.'})
d={'started_utc':started,'completed_utc':datetime.now(timezone.utc).isoformat(),'scanned_modules':scanned,'records':records,'who':'/root','model':'GPT-6 Astra Pro','effort':'not exposed by runtime','lean_executed':False}
(here/'DP59_translate_source_recovery.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({'new_modules':sum(r['new_file'] for r in records),'recovered_modules':len(records),'records':records},indent=2))
