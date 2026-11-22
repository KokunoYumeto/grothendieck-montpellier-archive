"""Record root's actual full coherent-gerbe and sector proof audit."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1]
p=root/'parts/B/post21_research/D_coherent_root_sector_compression_B.tex'
h=hashlib.sha256(p.read_bytes()).hexdigest()
assert h=='705b9db44b90b7aefffc731ea54600605eb5a63a11095c6113e670ccea0dd4a6'
r={
 'utc':datetime.now(timezone.utc).isoformat(),'actor':'root','model':'GPT-6 Astra Pro (OpenAI)',
 'effort':'inherited; no separate control exposed','run':'SA12 run1','outcome':'PASS',
 'check_type':'full actual-file mathematical proof and exact primary-source audit',
 'path':str(p.relative_to(root)),'sha256':h,
 'actual_read_scope':'Read complete initial5fa9ef1e candidate in an untruncated output; then read the entire nonsplit-central-inertia correction at6a57ed6f and the explicit descended-Azumaya elementary-transform bridge at705b9db4. The rest is unchanged.',
 'checks':[
  'The field cover is a representable finite-etale torsor over the root_e stack, even when the cyclic deck order has a p-part; only its radial inertia order is prime to p. Root_n base change is exactly root_n of the field-cover resolution.',
  'Strict-local puncture H2=0 trivializes the realized finite lifting gerbe. Finite-presentation descent supplies local actual objects; their finite cyclic Isom torsors have tame inertia dividing n, extend to root_n, and full faithfulness extends all composition, associativity and unit data. The extension is of the actual twisted-band gerbe, so its coherent deck action is inherited.',
  'The degree-m splitting cover gives algebraic single-sector anchors of rank m. The inverse image of μ_h in total inertia acts through one character, without choosing a central splitting. The scalar-zero End algebra descends to an Azumaya algebra on root_m by the local s^h grading.',
  'Extending the punctured Azumaya module and taking its reflexive hull is used only for geometric coverage on regular surfaces. The all-ring family equivalence uses actual locally free modules and matrix Morita descent; it does not assume flatness of a relative reflexive hull.',
  'Hom sector offsets have exactly one congruence class c mod h. The sign in Hom(−cD_n) matches the invariant basis s^c, and products/p-Frobenius have the stated bounded carries. Within-phase object differentials have zero offset, so no h extra normal layers enter.',
  'Normalized line comparisons cost at most p+1+d′=O(vm). Elementary transforms occur in the descended Azumaya-module category on root_m and preserve the selected sector. The connected degree-m spectral curve controls the Euler quotient, with no h multiplier.',
  'Fixed partial resolutions and compressed I=O(−hD_n) give J=O(Em), O(ν v m s²) variables per layer and weighted degree O(Em). The final deck functor is k-linear on coefficients and preserves I; no p^ν coordinate map is substituted.',
  'The actual coherent ν-stage skew cycle generates q-unit frames after a iterations. Their fixedness imposes the deck descent condition with the retained gerbe cocycle, without a new a-fold parameter equation or a false assertion about a based coset lift. Paired-jet contraction and finite-etale nilpotent invariance give actual finite-presentation Isom and open-and-closed unit classes.'
 ],
 'fresh_primary_reads':[{'url':'https://stacks.math.columbia.edu/tag/03Q4','ref':'turn932846424view0',
   'scope':'Full Lemma59.51.2 and Theorem59.51.3 statements and written proofs, section lines35–51, actually read. The output also contains later results; this audit does not claim full source dependency reproof beyond that scope.'}],
 'reused_inputs':'Fresh earlier root complete0EYG/0BUA tame-cover proofs, full strict-local Kummer/H2 manuscript proof, Lieblich root-extension/uniqueness, algebraic one-curve anchor/Morita/GE proof, connected minimal windows, fixed partial resolutions, exact weighted HPL and finite-unit/frame comparison. Root read the full original D_one_curve_gerbes_unit_jets.tex again this turn. No new complete reread of every unchanged linked primary source is claimed.',
 'movement_scope':'These three units are inputs to the separately stated unbounded-field projective semilinear count and crown consequence, not three independent movement events.'}
out=root/'parts/D/post21_research/audit_B_coherent_root_sectors_root.json'
assert not out.exists();out.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'utc':r['utc'],'path':str(out.relative_to(root)),'sha256':h,'outcome':'PASS'},indent=2))
