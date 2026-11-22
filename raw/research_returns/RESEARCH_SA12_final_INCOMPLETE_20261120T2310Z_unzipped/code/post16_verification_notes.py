"""Record completed root audits and the one typesetting-only source repair."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
rel='parts/C/post16_research/D_integral_antinef_energy_cycle.tex'
digest=hashlib.sha256((root/rel).read_bytes()).hexdigest()
changed=[]
for name in ['code/output/integrate_post16.json','code/output/integrate_post16_all.json']:
 p=root/name; data=json.loads(p.read_text())
 for row in data['files']:
  if row['path']==rel:
   row['sha256_before_typesetting_fix']=row['sha256'];row['sha256']=digest
 data['typesetting_fix_utc']=now
 data['typesetting_fix']='Moved tag D.IC.2 outside the split environment; unchanged mathematical text.'
 p.write_text(json.dumps(data,indent=2)+'\n');changed.append(name)
p=root/'parts/C/post16_research/integration_manifest_C_integral_cycle.json'
data=json.loads(p.read_text());data['sha256_before_typesetting_fix']=data['sha256'];data['sha256']=digest
data['bytes']=(root/rel).stat().st_size;data['typesetting_fix_utc']=now
data['typesetting_fix']='Root moved tag D.IC.2 outside split after build101 amsmath error; no mathematical change.'
p.write_text(json.dumps(data,indent=2)+'\n')
p=root/'parts/D/post16_research/ROOT_POST16_AUDIT_NOTES.md'
with p.open('a') as f:f.write('''

## Complete-local theorem, Artinian framing, and simple products

At12:36UTC root completed the actual full-file audit of the complete-local three-unit Brauer-zero packet. The audit checked the Picard modulo-n generators, source-only Maranda correction, the factor-through-free maps for the Frobenius-tensor source, the exact semilinear presentation equations, the target cokernel/Nakayama test, and the fixed-word Artinian rigidity and orbit argument. Complete equicharacteristic normal surface rings require no finite-type algebraization. The primary written proofs freshly read were Stacks Theorem59.91.11, tag095T (proper base change); Lemmas37.4.1 and37.4.2, tag0C6Q (Picard obstruction and lifting through thickenings); and Theorem30.27.1, tag088E (Grothendieck existence). This records the exact displayed proofs, not a fresh traversal of every recursive prerequisite. URLs: https://stacks.math.columbia.edu/tag/095T, https://stacks.math.columbia.edu/tag/0C6Q, https://stacks.math.columbia.edu/tag/088E.

Root fully read the actual C Artinian-framing fragment and checked the Cech small-extension argument with a specified previous isomorphism, the finite-free section/cokernel base changes, and the exact boundary obstruction. Its hypotheses concern actual vector bundles on the fixed resolution with full closed fibres; no arbitrary MCM full-pullback base-change assertion is substituted.

Root wrote and fully audited the selected-simple-product corollary. At12:38--12:39UTC root freshly read the complete statement and proof of Lucchini--Marion--Tracey, Proposition2.6, printed pp11--13, including equations(2.1),(2.2), in the retained published primary text. A previously truncated search was followed by a complete bounded read of lines480--600. The generating-tuple bound uses the outer-automorphism estimate as stated in the same retained source. B/C/D complete actual-file audits passed. Only kernels satisfying the chosen embedded Brauer-zero condition are included. No all-kernel or general crown conclusion is claimed.

All17 post16 units were assembled at12:41UTC. There is one strict main reduction: unbounded scalar order in Brauer-zero projective counts, with global and complete-local surface versions and their geometric/descent/selected-product closures. Integral cycles, RDP Hom and framing, finite jets and actual-bundle Artinian rigidity remain auxiliary. No requested row closes. The formal review10 record is not changed retrospectively.

## Literature searches before describing the new bounds

At approximately12:33UTC root searched both web engines, with queries: `"projective representations" "Brauer" "growth" fundamental group`; `"Frobenius" "twisted sheaves" "representation" finite field`; `"rational double points" "full sheaves" rigidity Hom`; `"Brauer" "representation growth" "fundamental"`; `"Frobenius periodic" "projective" "representations"`; `"full sheaves" "Ext" "rational double" rigidity`; and `Lieblich Moduli of twisted sheaves 3.2.3.10 arxiv`. Results included Lieblich's period-index and twisted-sheaf work, finite-group representation growth, and local torsors of rational double points. No exact uniform quadratic count matching the theorem was located in these searches. This is neither an exhaustive novelty search nor a priority claim. Only the actually opened primary inputs are used as proofs. Search-only arXiv abstracts, a recent mirror result, and secondary summaries were not promoted to checked literature.

## Typesetting-only repair

Build101 stopped at the integral-cycle display because its equation tag was inside a split environment. Root moved that tag outside split, preserving the formula and proof. Build102 completed with no overfull boxes; citation and reference warnings at this intermediate stage required sequential bibliography25 and further LaTeX passes. Visual certification is recorded separately only after the final PDF is actually inspected.
''')
record={'utc':now,'source':rel,'sha256':digest,'manifests_updated':changed,'mathematical_change':False,'actual_audit_notes_appended':True}
(root/'code/output/post16_verification_notes.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
