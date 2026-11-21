"""Record and transport the checked isolated-invertible-factor refinement."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json

R=Path(__file__).resolve().parent
W=R.parent
OUT=W.parent/'deliverables'
now=datetime.now(timezone.utc).isoformat()
guard=R/'integration_16_check_events.tsv'
assert not guard.exists()
who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
p=R/'grothendieck.tex'
s=p.read_text()
marker='\\subsection{What the manuscript record does and does not establish}'
addition=r'''
\paragraph{I-38. Triple-dominant pullback and isolated invertible transitions.}
The one-pole parameter morphism is dominant on every three
coordinate factors. Indeed, after solving for the center and
amplitude using two coordinates, the third is a nonconstant
rational function of the selector over their function field:
three distinct simple poles forbid both interpolation coefficients
from being constant. This argument establishes dominance even
when a characteristic-two Jacobian test is inseparable.

For the promised alternating rank pattern, exterior-square maps
of the rank-two factors have rank one, and there is at most one
invertible exterior-square map between two of them. Each scalar
connector is therefore a section depending on at most three
coordinates. Triple dominance preserves every required nonzero
connector. Compatible active rank-two summands and passive lines
then put the constant maps in the forms $I_3$ and
$\operatorname{diag}(I_2,0)$. The rank pattern survives the
irreducible multilinear reduction: a specialized singular factor
between two surviving invertible ones is absorbed into the latter
and makes it singular.

The second coefficient form at the one-pole center annihilates
both vectors $h_i=(a_i-y)^{-1}$ and $h_i^2$. Its only possible
entries are within two positions of the diagonal. The determinant
$h_jh_k(h_k-h_j)$ is a nonzero section, in every characteristic,
so row induction annihilates the whole form. Every passive
excursion of an output path has one of its zero entries as a
factor. This transports the contradiction of I-38 without
asserting preservation of each individual minor, and without
discarding passive propagation at invertible factors.
D-S6, V~2.1--2.2.1, supplies exterior powers; D-S3 supplies the
bundle changes of frame; D-FGA supplies the rank-open and
function-field formulation. Longer consecutive invertible runs
require connectors on four or more coordinates and remain outside
this triple-dominance proof.

'''
assert marker in s
p.write_text(s.replace(marker,addition+marker))

with guard.open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    w.writerow(['statement_id','date','who','type','outcome'])
    w.writerow(['I-38',now,who,'targeted proof check','PASS full root reading and independent rederivation: triple algebraic independence by function fields in every characteristic; exact preservation of no-adjacent-rank3 promise under disjoint-variable specialization; compound connectors with at most3 coordinates; rank preservation rather than every-minor preservation; nonzero endpoint projections; suffix-kernel passive lines and compatible I/P gauges; transported endpoint shears; Hh=Hh² formal identities and bandwidth2 elimination; all passive-path endpoint cases and inherited exact grid.'])
    w.writerow(['R-27',now,who,'computation or formal certificate','PASS finite boundary core only: independent path-matching enumeration with explicit epsilon-polynomial multiplication regenerates all33852 entries of the three124x91 jet matrices. Independent block-Toeplitz echelon ranks84,172,262 imply valuation counts84,4,2. Uniform proof is not asserted by this event. See check_r27_boundary_jets.py and r27_boundary_jet_checks.json.'])

p=R/'intro.tex';s=p.read_text()
needle='Mixed variable-dependent rank-two and rank-three factors remain outside that refinement.'
assert needle in s
s=s.replace(needle,'I-38 extends the same two-pair conclusion to affine words with isolated invertible factors: no two consecutive variable-dependent factors have rank three. Longer invertible runs and nonlinear singular factors remain open for this two-pair argument.')
p.write_text(s)
p=R/'open_gates.tex';s=p.read_text()
s=s.replace('Mixed variable-dependent rank-two/rank-three factors, nonlinear singular factors, and the growing-width question remain open.','I-38 additionally permits isolated invertible affine factors. Consecutive invertible runs of length at least two, nonlinear singular factors, and the growing-width question remain open.')
s=s.replace('arbitrary mixtures of rank-two and variable-dependent rank-three\naffine factors, and nonlinear singular factors.','affine words with two or more consecutive variable-dependent\nrank-three factors, and nonlinear singular factors. I-38 closes\nthe subclass with isolated invertible factors.')
p.write_text(s)
with (OUT/'IMPLICATIONS.md').open('a') as f:
    f.write('''

### Isolated invertible affine factors also need only two pairs

I38 extends I37 to width-three affine words in which no two consecutive variable-dependent factors are generically invertible, after constant factors have been absorbed. The one-pole center dominates every three coordinates, so it preserves the rank-one exterior-square connectors through one invertible factor. Its two tangent directions force the bandwidth-two Hessian to vanish in every characteristic. The exact sample count and P13 arithmetic exponent5 are unchanged. The adjacency promise survives the required irreducible multilinear specialization. Longer full-rank runs and nonlinear singular factors remain outside this proof; the growing-width main gate is unchanged.
''')
with (OUT/'LEDGER.md').open('a') as f:
    f.write('\n\n## '+now+' — isolated invertible affine factors\n\n')
    f.write('I38 passes complete author, root and purity proof readings. It extends the two-pair result to the precise no-consecutive-invertible affine subclass. This is a specified-class refinement, not a polynomial-in-width theorem. The failed abstract semiseparable-Hessian repair is being retained with its exact missing integrability conditions. This entry is not a scheduled review.\n')
proof=W/'isolation/I38_isolated_invertible_two_pairs.tex'
(R/'i38_whole_proof_review.json').write_text(json.dumps({'checked_utc':now,'who':who,'status':'PASS','sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'scope':'Entire I38 proof, with its exact adjacency promise'},indent=2)+'\n')
print(now)
