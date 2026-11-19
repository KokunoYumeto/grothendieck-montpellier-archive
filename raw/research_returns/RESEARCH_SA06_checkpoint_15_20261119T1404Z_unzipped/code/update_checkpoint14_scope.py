#!/usr/bin/env python3
"""Update the master summaries for the independently audited C.3bd/be results."""
from pathlib import Path
from datetime import datetime, timezone
import json
import time

root = Path(__file__).resolve().parents[1]
started = datetime.now(timezone.utc).isoformat()
t0 = time.perf_counter()
changes = {
    'code/build_registers.py': [
        ('C.3a–bc;C.1f', 'C.3a–be;C.1f'),
        (
            'C.3ab/ad/ar/au/ax/az/bc are restricted positive top theorems; bc proves',
            'C.3be proves CH_1(Spec R)_Q=CH^(N−1)(puncture)_Q=0 for every excellent henselian local domain of dimension N>=2 with residue field Fpbar, including mixed characteristic; neither normality, a regular puncture, nor a finite-type field model is required. The ordinary quotient vanishes wherever defined. The proof uses a normalized surface through each curve, finite K0 detection, determinant, and the negative exceptional intersection matrix; it does not require higher-dimensional resolution. This residue-field-restricted result does not settle the universal arbitrary-field top gate. C.3bd supplies the earlier algebraizable normal dimension2/3 corollary with the stated regular puncture. C.3ab/ad/ar/au/ax/az/bc are additional restricted positive top theorems; bc proves'
        ),
    ],
    'RESEARCH_SA06_paper.tex': [
        (
            'Over $\\overline{\\mathbb F}_p$, a specified simple normal crossing\nresolution with an ample negative exceptional combination gives the\nstronger vanishing of the entire top rational Chow group of the puncture.',
            'For every excellent henselian local domain of dimension $N\\ge2$\nwith residue field $\\overline{\\mathbb F}_p$, we prove\n$\\mathrm{CH}_1(\\operatorname{Spec}R)_{\\mathbb Q}=0$ and hence\n$\\mathrm{CH}^{N-1}$ of its puncture is zero rationally.\nThis includes mixed characteristic and requires neither ambient\nnormality nor a regular puncture. The determinant and normalized-surface\nargument uses resolution only in dimension two. The corresponding\nordinary quotient vanishes wherever its field-family definition applies.'
        ),
    ],
}
updated = []
for name, replacements in changes.items():
    path = root / name
    text = path.read_text()
    for old, new in replacements:
        if text.count(old) != 1:
            raise SystemExit(f'Expected one exact old passage in {name}')
        text = text.replace(old, new)
    path.write_text(text)
    updated.append(name)
result = {'started_utc': started, 'runtime_seconds': time.perf_counter()-t0,
          'updated_files': updated,
          'scope': 'Summary maintenance only; no mathematical check or movement.'}
(root / 'logs/update_checkpoint14_scope.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
