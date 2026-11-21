from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv
R=Path('.')
now=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()

p=R/'work/build_package.py';s=p.read_text()
s=s.replace("'work/root/all_five_row_support_report.md'","'work/root/third_power_fixed_twist_report.md','work/root/all_five_row_support_report.md'")
s=s.replace("'work/rectangular/second_row_two_canonical_rank_law.md'","'work/rectangular/second_row_two_canonical_rank_law.md','work/rectangular/second_row_three_canonical_rank_law.md'")
s=s.replace("'work/archive/LINEAR_CANONICAL_RANGES_REVIEW.md'","'work/archive/LINEAR_CANONICAL_RANGES_REVIEW.md','work/archive/TWO_COLUMN_UNIT_FAMILY_REVIEW.md','work/archive/SECOND_ROW_TWO_RANK_REVIEW.md','work/archive/SECOND_ROW_THREE_RANK_REVIEW.md'")
s=s.replace('The remaining direct positive-formula gate is cancellation-free evaluation of those explicit bounded tables for k≥3 and0≤c≤2k−4','G032 completes all ideal orders k≤3, including every c=0,1,2 at order3. The remaining direct positive-formula gate is cancellation-free evaluation of those explicit bounded tables for k≥4 and0≤c≤2k−4')
s=s.replace("      ('Q-IDEAL-ORDER2'", "      ('Q-IDEAL-ORDER3','G-032 FT1–10;T-051,T-050,T-045,G-021','Evaluate every outer-five coefficient of ideal order at most three','proved','The three new low-twist slices and previously proved high twists exhaust k3. The finite rank-three restriction character yields17 selected positive polytopes in at most8 variables, with24 boundary branches and1552320 certified constants. The exact determinant/complement maps cover λ2≤n+3 orλ4≥n−3.'),\n      ('Q-MAP-SECOND3','R-036 CT1–20','Determine every actual canonical rank in the complete second-row-at-most-three band','proved','The actual signed exterior-invariant algebra excludes all tails except2^j and3,2^j. The latter unit target exists for n≥3 and j≤a−3 and has image1 exactly for j≤n−3. The cubic-minor scalar, n2 extension failure and complete band cokernel are proved. Every n≥a reaches the full band.'),\n      ('Q-IDEAL-ORDER2'")
s=s.replace('every n≥a reaches the full band. The remaining critical annihilator','every n≥a reaches the full band. R036 computes the entire second-row≤3 rank law and exact cokernel, through the signed invariant-algebra map and normalized cubic-minor scalar. The remaining critical annihilator')
p.write_text(s)

note='''## Third ideal order and complete cubic-tail ranks

G032 completes every outer-five coefficient of ideal order at most three. The new c=0,1,2 slices at k=3 have seventeen selected positive polytopes with at most eight variables, twenty-four fixed boundary branches, exact support and1,552,320 nonnegative fixed constants. The actual rank-three Schur extraction and determinant pairings carry the result to every λ₂≤n+3 orλ₄≥n−3. The remaining direct coefficient-formula gate has shrunk to k≥4 and0≤c≤2k−4, after the completed complementary and special families are removed. G031 already decides all zeros there.

R036 computes every actual canonical rank in the complete second-row-at-most-three band. The new unit targets(an−2j−3,3,2^j) exist for a,n≥3 and0≤j≤a−3, and their actual image is one precisely for j≤n−3. The signed exterior-invariant algebra gives a surjective morphism that excludes every other possible tail; the centered cubic-minor polynomial and full third-moment calculation give the exact map scalar and the n=2 extension obstruction. Together with R035 this gives the entire band cokernel and proves full band surjectivity for n≥a. Root and archive whole-proof readings both passed.
'''
for name in ['work/root/paper_front.md','deliverables/IMPLICATIONS.md']:
 p=R/name;p.write_text(p.read_text()+'\n\n'+note)
p=R/'deliverables/LEDGER.md';p.write_text(p.read_text()+f'\n\n## Research update — {now}\n\n'+note)
p=R/'work/root/remaining_gates.md';s=p.read_text().replace('k≥3 and0≤c≤2k−4','k≥4 and0≤c≤2k−4').replace('k≥3 and 0≤c≤2k−4','k≥4 and 0≤c≤2k−4').replace('Checkpoint06 is due04:31:08Europe/Berlin.','Checkpoint06 was saved at04:31:08Europe/Berlin; Checkpoint07 is due05:16:08Europe/Berlin.')
s+='\n\n'+note;p.write_text(s)
p=R/'work/root/current_ranges.md';p.write_text(p.read_text()+'''\n\n## R036: complete second-row-three rank and cokernel\n\nFor a,n≥3, every unit cubic-tail target(an−2j−3,3,2^j),0≤j≤a−3, is reached exactly for j≤n−3. Together with the R035 two-column unit family and the top row, these exhaust all targets with λ₂≤3. The exact cokernel is the sum of the two-column units j=n,…,a−1 and cubic-tail units j=n−2,…,a−3. At n=2 the cubic targets are absent by the exact chart nondivisibility proof. All n≥a are surjective throughout this whole band.\n''')
p=R/'work/root/geometric_dictionary.md';p.write_text(p.read_text()+r'''

## Third-order section classes and cubic canonical images

**G-032.** The map is the exact normal substitution and rank-three Young extraction
\(M=\operatorname{Hom}_{GL_3}(S_{(a+c,b+c,c)}\mathbb Q^3,J_3)\).
Exterior column contraction gives
\(M\simeq\operatorname{sgn}^cH^0(\mathcal I_Z^3(c)S_{(a,b)}Q)\),
because \(\det Q=\operatorname{sgn}\otimes\mathcal O(1)\).
The oriented quotient/restriction complex gives its exact class; the finite
skew-Schur character and subset-chain bijection calculate this same
Schur-operation coefficient. The complement morphism is the perfect
exterior pairing into \((\det\mathbb Q^5)^H\), retaining its
\(\operatorname{sgn}^H\) character. The affine/projective maps are
EGA II2.4.1–2.4.2 and2.5.2/2.5.4; the associated-bundle functor is
SGA3 I4.5,4.7.2–4.7.3, and its exact representation operation is
SGA6 VI3.3 with the free λ-ring evaluation V4.2,4.4,4.8–4.9.
The archive comparison is cote133/028 through the actual tensor-word,
torus-weight and Young maps of A012.

**R-036.** The actual exterior-algebra surjection sends a two-form or
three-form on the auxiliary space to the sum of its products in each
projected standard row. Signed equality-partition expansion proves its
surjectivity, and the skew Cauchy idempotents exclude every unlisted
tail. The affine-minor polynomial gives an explicit highest section of
the Chow coordinate module. The normalized grid pullback sends that
section by the exact scalar CT20 to the corresponding section with
interchanged block degrees; its adjoint determines the full stated
image and cokernel. Over a rational base scheme, the map
\(M\mapsto\mathscr F(E)\times_{GL(V)}M\) carries each tensor map
and rational projector to an associated-bundle arrow. The frame maps
are SGA3 I4.5,4.7.2–4.7.3; the representation-to-K0 morphism is
SGA6 VI3.3, and its λ-operation is V4.2,4.4,4.8–4.9. The actual Chow
scheme-image ideal is EGA I9.5.2, with projective module construction
EGA II2.5.2/2.5.4. This evaluates the cote133/028 tensor/Schur operation
through A012, including all characteristic-zero projector denominators.
''')
p=R/'work/root/third_power_fixed_twist_report.md';s=p.read_text().replace('It is a map into the original\ncoordinate ring, not an identification made only on dimensions.','It is a map into the original coordinate ring.').replace('finite symmetric\n-group dual','finite symmetric-group dual');s+='\nThe direct evaluator additionally passed2310 exact value comparisons,2282 literal witness-matrix checks and84 exhaustive small-witness enumerations; the receipt is `THIRD_POWER_EVALUATOR_CHECK.json`.\n';p.write_text(s)

p=R/'work/root/CHECK_EVENTS.tsv'
fields=next(csv.reader(p.open(newline=''),delimiter='\t'))
who='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01'
events=[
 ('R-036','targeted proof check','Read entire saved CT1–20 proof and full endpoint/geometry paragraphs. Independently checked signed orbit-algebra generation, determinant contraction, finite-rank cutoff, cubic highest vector, exact nonzero value, n2 nondivisibility, normalized third moments, determinant derivative, all factorials and adjoint rank inference. PASS. Gram derivative wording made explicit before completion.'),
 ('G-032','targeted proof check','Read the entire saved FT1–10 proof, all51 boundary catalog rows and completion/geometry sections. Checked actual rank3 normal Schur extraction, orientation and parity, every residue-degree bound and branch origin, finite Newton identity, eight/five-variable bijection, all k3 twist coverage and exact complement pairing. PASS. Independent certificate review follows separately.'),
 ('G-032','computation or formal certificate','Executed all1552320 finite Newton constants:3 bulk arrays of504000 and24 boundary arrays of1680. All nonnegative, every active positive-order constant strictly positive. Added and executed every prefix-product overflow bound after archive pointed out that a zero third factor alone does not bound the first multiplication. All bounds pass.'),
 ('G-032','computation or formal certificate','Compared3353 actual balanced Schur cycle coefficients across all valid k1..3,c0..2,b0..8,x0..7 inputs; checked2310 evaluator values,2282 literal witness-matrix points and84 exhaustive small-witness cases. All PASS; exact scripts and receipts retained.'),
]
with p.open('a',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t')
 for sid,kind,outcome in events:
  row={'statement_id':sid,'date':now,'who_model_effort_run':who,'type':kind,'outcome':outcome}
  w.writerow({k:row.get(k,'') for k in fields})
print(now)
