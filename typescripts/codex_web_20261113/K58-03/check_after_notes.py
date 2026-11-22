#!/usr/bin/env python3
"""Compare final hashes against both witness hash records and the frozen file set."""
from pathlib import Path
import re,hashlib
root=Path(__file__).resolve().parent
log=(root/'progress.log').read_text()
stages=[re.search(r'^'+s+r' (\d{4}-\S+Z)$',log,re.M) for s in ['transcription frozen','witness check done','mathnotes done']]
assert all(stages) and stages[0].start()<stages[1].start()<stages[2].start()
recorded={p:h for h,p in re.findall(r'^witness SHA256 ([0-9a-f]{64}) (.+)$',log,re.M)}
sidecar={p:h for h,p in (line.split('  ',1) for line in (root/'audit/witness.sha256').read_text().splitlines())}
required={str(p.relative_to(root)) for p in (root/'pages').glob('*.tex')}|{'K58-03_transcription.tex'}
assert len(required)==16 and recorded==sidecar and set(recorded)==required
for name in sorted(required):
 digest=hashlib.sha256((root/name).read_bytes()).hexdigest()
 assert digest==recorded[name],name
pages=sorted((root/'pages').glob('*.tex'))
assert (root/'K58-03_transcription.tex').read_bytes()==b''.join(p.read_bytes() for p in pages)
print('Post-notes SHA-256 check passed: all 15 pages and the assembled fragment match the witness hashes in progress.log and audit/witness.sha256.')
print('Freezing, witness completion and notes completion:',*[m[1] for m in stages])
