#!/usr/bin/env python3
"""Extract the separately retrieved project background once for endpoint checks."""
import json,zipfile
from pathlib import Path
src=Path('/workspace/scratch/81b6665e34a6/project_sources/LM4_SUCCESSOR_background.zip')
dst=src.with_suffix('')
if dst.exists(): raise SystemExit('Already extracted; refusing to unpack twice')
with zipfile.ZipFile(src) as z:
 for n in z.namelist():
  if n.startswith('/') or '..' in Path(n).parts: raise SystemExit('Unsafe archive member')
 z.extractall(dst)
 print(json.dumps({'archive':src.name,'files':len(z.namelist()),'destination':str(dst)}))
