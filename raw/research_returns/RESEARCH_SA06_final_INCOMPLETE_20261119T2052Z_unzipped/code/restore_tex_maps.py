#!/usr/bin/env python3
"""Restore a local PDF font map from installed AMS and RSFS Type1 font maps."""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import json

t=perf_counter()
r=Path(__file__).resolve().parents[1]
base=Path('/usr/share/texlive/texmf-dist/fonts/map/dvips')
sources=sorted((base/'amsfonts').glob('*.map'))+[base/'rsfs/rsfs.map']
lines=[]
for p in sources:
    if not p.is_file():raise FileNotFoundError(p)
    lines.extend(p.read_text().splitlines())
target=r.parent/'texmf/fonts/map/pdftex/updmap/pdftex.map'
target.parent.mkdir(parents=True,exist_ok=True)
target.write_text('\n'.join(lines)+'\n')
result={'utc':datetime.now(timezone.utc).isoformat(),'sources':[str(x) for x in sources],
        'target':str(target),'runtime_seconds':perf_counter()-t}
(r/'logs/restore_tex_maps.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
