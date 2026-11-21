"""Record completed root readings and integrate the current checked comparisons."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json
B=Path(__file__).resolve().parent
now=datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256((B/p).read_bytes()).hexdigest()
items=[
 ('evidence/main_gate/senary_trace_detector.tex',['KT-SENARY-GENUS-TRACE-DETECTOR','KT-ANALYTIC-RESIDUE-NONSATURATION'], 'Whole written proof read; Kohnen normalization and Theorem21 pp20–22 read; Ibukiyama–Williams complete mass proof pp23–26 read, pp24–25 visually inspected. The stated 3^2 prefactor differs from the proof and exact local-factor product 3^3; the latter is used. General coefficient and density theorems remain imported. Fresh exact D=-3,-7,-79 controls saved.'),
 ('evidence/unitary_audit/reducible_comparison/quartic_quintic_obstruction.tex',['KT-ORDINARY-QUARTIC-CONDITION','KT-QUINTIC-RELATIVE-TARGET'], 'Whole 371-line proof and complete exact BCH script read. Frozen-copy rational replay PASS. Checked ordinary local conditions, opposite -2e positive-quartic unit, lower quintic mapping-fiber exact sequence and dimension 1+d, and independence from quartic lift. Prior cohomological and class-field inputs imported; no arithmetic value evaluated.'),
 ('evidence/unitary_audit/reducible_comparison/finite_coefficient_norm.tex',['KT-CUBIC-FINITE-COEFFICIENT-NORM'], 'Whole 131-line proof read. Finite scalar extension of continuous cochains and local kernels; bilinear ordinary quadratic defining cochains; homogeneous relative primitives at p and ramified auxiliary primes; quadratic polarization and prime-to-p restriction injectivity checked. No additive k extension is assumed cyclic. No norm value or source extraction obtained.'),
 ('evidence/main_gate/high_order_twist_source_scope.tex',['KT-HIGH-ORDER-TWIST-TARGET-SCOPE'], 'Whole written argument and exact archive Counts.GD lines9–22, component definitions lines75–86, Vlen116, and orb140–145 read. Local component condition is distinguished from global character order; fixed kernel and reduction-injectivity argument checked. A source-scope result, not an impossibility theorem.'),
]
review={'date_utc':now,'reviewer':'/root; GPT-6 Astra Pro; effort not exposed','type':'targeted proof check','outcome':'PASS','items':[{'path':p,'sha256':sha(p),'ids':ids,'scope':scope} for p,ids,scope in items],'computations':['evidence/root_senary_review/exact_mass_controls.json','evidence/root_quartic_review/quartic_bch_check.json'],'movement':False,'movement_reason':'These identify operations and obstructions, or check source scope; no previous arithmetic gate is closed or made strictly smaller.'}
rp='evidence/root_comparisons_2121_review.json'
(B/rp).write_text(json.dumps(review,indent=2)+'\n')
with (B/'ROOT_CHECK_EVENTS.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for p,ids,scope in items:
  for i in ids:w.writerow([i,now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','targeted proof check','PASS '+scope,rp])
 for i,scope,ev in [('KT-ORDINARY-QUARTIC-BCH-REPLAY','PASS fresh frozen-copy rational matrix exponential/product/logarithm replay; five monomials, six brackets and five involution signs. No arithmetic class evaluated.','evidence/root_quartic_review/quartic_bch_check.json'),('KT-SENARY-MASS-EXACT-CONTROLS','PASS fresh exact Bernoulli controls D=-3,-7,-79 and p31 cancellation. Not a new density theorem proof.','evidence/root_senary_review/exact_mass_controls.json')]:
  w.writerow([i,now,'/root; run KTOWER','GPT-6 Astra Pro','not exposed','computation or formal certificate',scope,ev])
with (B/'QUESTIONS.tsv').open(newline='') as f:r=csv.DictReader(f,delimiter='\t'); fields=r.fieldnames; rows=list(r)
for row in rows:
 if row['id']=='KT-Q1B':
  for _,ids,_ in items:
   for i in ids:
    if i not in row['finding_ids']:row['finding_ids']+='; '+i
  row['current_gate_or_scope']+=' The norm comparison now extends to every finite coefficient field by quadratic polarization. Positive quartic and lower quintic relative obstructions are explicit; the latter has dimension 1+d for the original strict rational class dimension d. A senary genus trace is an exact same-D two-unit detector, but individual coefficient units can cancel in the trace. None evaluates a required obstruction or proves simultaneous unit existence.'
with (B/'QUESTIONS.tsv').open('w',newline='') as f:w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
p=B/'sections/open_gates.tex';s=p.read_text();needle='These comparisons do not assert a smaller arithmetic\nvanishing gate.'
assert needle in s
s=s.replace(needle,needle+r'''
KT-CUBIC-FINITE-COEFFICIENT-NORM extends the matched formula
to every finite coefficient field by polarization, without
calling an additive extension of that field cyclic.
KT-ORDINARY-QUARTIC-CONDITION retains a positive quartic
obstruction controlled sufficiently by the opposite $-2e$
auxiliary unit. KT-QUINTIC-RELATIVE-TARGET identifies the lower
quintic space with dimension $1+d$, where $d$ is the original
strict rational class dimension. Neither obstruction is evaluated.
KT-SENARY-GENUS-TRACE-DETECTOR gives a second exact same-field
product detector; its $p=31,D=-79$ example shows why individual
coefficient units do not imply a unit trace. An analytic residue
alone supplies no missing integral saturation.
''')
p.write_text(s)
p=B/'sections/framework.tex';s=p.read_text();s=s.replace('KT-CUBIC-P-ONLY-NORM;','KT-CUBIC-P-ONLY-NORM;\nKT-CUBIC-FINITE-COEFFICIENT-NORM;\nKT-ORDINARY-QUARTIC-CONDITION; KT-QUINTIC-RELATIVE-TARGET;')
s=s.replace('KT-EISENSTEIN-QUADRATIC-DETECTOR &','KT-EISENSTEIN-QUADRATIC-DETECTOR;\nKT-SENARY-GENUS-TRACE-DETECTOR;\nKT-ANALYTIC-RESIDUE-NONSATURATION;\nKT-HIGH-ORDER-TWIST-TARGET-SCOPE &')
s=s.replace('unit detection and simultaneous nonvanishing remain open.','unit detection and simultaneous nonvanishing remain open.\nThe senary genus trace realizes the same product as a finite\nweighted sum of integral coefficient sections. Its mass factor\ncan vanish modulo $p$ despite every individual coefficient being\na unit. Higher order finite twists change the exact coefficient\nsheaf and Selmer target in Counts.GD and Vlen.')
p.write_text(s)
with (B/'LEDGER.md').open('a') as f:f.write('\n\n## Checked comparisons integrated — '+now+'\n\nRoot whole-proof PASS for the senary trace detector, quartic/quintic relative targets, finite-coefficient norm polarization and high-order twist source scope. Exact proof hashes and limits are in '+rp+'. Root fresh rational BCH replay and Bernoulli mass controls pass. These results do not count as arithmetic movement: same-D unit existence, norm evaluation, source-to-jet extraction and the original rational strict class remain open.\n')
with (B/'IMPLICATIONS.md').open('a') as f:f.write('\n\n## Integral detectors and higher ordinary obstructions\n\nThe finite-coefficient norm comparison now follows from a proved quadratic polarization identity. The positive quartic target needs an additional opposite-character unit as a sufficient condition; the lower quintic relative target has dimension 1+d and retains the original strict class dimension d. No nonzero arithmetic obstruction or source-to-jet map is supplied. The senary genus trace is another exact same-discriminant detector, with an explicit p31 mass-cancellation example; analytic residues alone do not establish integral saturation. These are statements about finite coefficient sheaves, extension obstructions, and their arithmetic cohomology in the existing SGA4/Milne and conormal crosswalk, not new all-weight K-vanishing or an Ihara-kernel theorem.\n')
print(json.dumps({'review':rp,'items':len(items),'timestamp':now}))
