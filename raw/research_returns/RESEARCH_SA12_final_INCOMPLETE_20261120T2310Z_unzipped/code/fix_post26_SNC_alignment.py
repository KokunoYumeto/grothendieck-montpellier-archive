"""Change only the display environment in D.SR.10; preserve exact reversal."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

root = Path(__file__).resolve().parents[1]
rel = 'parts/D/post26_research/D_controlled_SNC_refinement_root.tex'
p = root / rel
before = p.read_bytes()
oldsha = hashlib.sha256(before).hexdigest()
assert oldsha == '133ace3200261b2d0f6bc177a71e5ba36d25022d131e38f7016152423a8f819d'
old = r''' \begin{split}
 \rho_*\mathcal O_{bZ'}&=\mathcal O_{bZ},
       &R^1\rho_*\mathcal O_{bZ'}&=0,\\
 H^i(bZ',\rho^*L|_{bZ'})&=H^i(bZ,L|_{bZ})
       &&(i=0,1).
 \end{split}'''
new = old.replace(r'\begin{split}', r'\begin{aligned}').replace(r'\end{split}', r'\end{aligned}')
s = before.decode()
assert s.count(old) == 1
after = s.replace(old, new, 1)
assert after.replace(new, old, 1) == s
snapshot = 'parts/D/post26_research/D_controlled_SNC_refinement_root_promoted_before_alignment.source.txt'
(root / snapshot).write_bytes(before)
p.write_text(after)
change = dict(
    utc=datetime.now(timezone.utc).isoformat(), path=rel,
    before_sha256=oldsha, after_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
    before_snapshot=snapshot,
    change='Only begin/end split changed to begin/end aligned in display D.SR.10, whose four alignment columns require aligned. No equation, quantifier, prose, proof or status changed.',
    exact_reversal_verified=True, observed_failure='build_pass175: extra alignment tab in D.SR.10',
    movement=False
)
manifest = root / 'parts/D/post26_research/integration_manifest_controlled_SNC_refinement_root.json'
m = json.loads(manifest.read_text())
assert m['sha256'] == oldsha
m['sha256'] = change['after_sha256']
m['bytes'] = p.stat().st_size
m['typography_changes'] = [change]
manifest.write_text(json.dumps(m, indent=2) + '\n')
(root / 'code/output/post26_SNC_alignment_change.json').write_text(json.dumps(change, indent=2) + '\n')
print(json.dumps(change, indent=2))
