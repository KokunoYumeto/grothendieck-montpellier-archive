#!/usr/bin/env python3
"""Apply the audited semilocal C.3be refinement to the main report register."""
from pathlib import Path
from datetime import datetime, timezone
import json
import time

root=Path(__file__).resolve().parents[1]
started=datetime.now(timezone.utc).isoformat()
t0=time.perf_counter()
path=root/'code/build_registers.py'
text=path.read_text()
old=('C.3be proves CH_1(Spec R)_Q=CH^(N−1)(puncture)_Q=0 for every excellent '
     'henselian local domain of dimension N>=2 with residue field Fpbar, including '
     'mixed characteristic; neither normality, a regular puncture, nor a finite-type '
     'field model is required.')
new=('C.3be proves CH_1(Spec R)_Q=CH^(N−1)(puncture)_Q=0 for every excellent '
     'local domain of dimension N>=2 with residue field Fpbar, including mixed '
     'characteristic; neither henselianity, normality, a regular puncture, nor a '
     'finite-type field model is required. Finite semilocal normalization replaces '
     'the earlier single henselian branch.')
if text.count(old)!=1:
    raise SystemExit('Expected one exact certified intermediate C.3be passage')
path.write_text(text.replace(old,new))
result={'started_utc':started,'runtime_seconds':time.perf_counter()-t0,
        'updated_file':str(path.relative_to(root)),
        'scope':'Summary maintenance after the semilocal proof audit; no movement.'}
(root/'logs/refine_checkpoint14_scope.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
