from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv
stamp=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()
p=Path('work/build_package.py');s=p.read_text()
assert "'work/rectangular/hook_tail_canonical_isomorphism.md'" not in s
s=s.replace("'work/rectangular/odd_part_occupancy_canonical_range.md'", "'work/rectangular/odd_part_occupancy_canonical_range.md','work/rectangular/hook_tail_canonical_isomorphism.md'")
s=s.replace("'work/archive/HOOK_ENDPOINT_REVIEW.md'", "'work/archive/HOOK_ENDPOINT_REVIEW.md','work/archive/ODD_PART_OCCUPANCY_REVIEW.md','work/archive/PAIR_BOUNDARY_HOOK_REVIEW.md'")
row=('Q-MAP-ALL-HOOK-TAILS','R-050 HM1–27; R046 TM14–17; Solomon §3; Langley–Remmel Thm3.1','Determine every actual canonical rank on a hook tail','proved','For all a,n≥1 and every valid λ=(an−t−r,t,1^r),t≥1,r≥0, the two actual normalized canonical maps are isomorphisms on the entire λ-isotypic component. The finite power-sum map from moments of degrees2..s is onto and faithful on all hook types by the exact hook specialization and invariant Koszul basis. The actual bounded-row input at row degree n maps injectively into moments2..n, so the exact canonical factorization applies even when n<t. The unit family λ=(an−D,T,1^(m−2)),T=binom(m,2)+1,D=binom(m+1,2)−1,a,n≥m has coefficient1 and the full nonzero scalar C_m(a,n) in HM24, including every square m.')
anchor="      ('Q-MAP-ODD-OCCUPANCY'";assert anchor in s
s=s.replace(anchor,'      '+repr(row)+',\n'+anchor)
s=s.replace('The remaining map gate excludes all of these full-isotypic ranges. R038','R050 then proves the actual canonical isomorphism on every hook tail (t,1^r), including all unstable inner degrees, with explicit nonzero unit scalars in every outer rank. The remaining map gate excludes all of these full-isotypic ranges and all hook tails. R038')
p.write_text(s)
note=r'''## Every actual canonical map on a hook tail

R050 proves full isomorphism in both directions on every valid component
\[
\lambda=(an-t-r,t,1^r),\qquad a,n\ge1,\ t\ge1,\ r\ge0.
\]
The actual power-sum map from moments of degrees2 through s is surjective; its exact hook multiplicities are the support sums in HM13, proved both by the specified virtual-alphabet specialization and the polynomial invariant Koszul basis. Hence that precise morphism is faithful on every hook component. The actual source highest polynomial has separate row degree at most n, so independent-row evaluation lies in moments2 through n even at n<t. Its injective evaluation, the triangular moment automorphism and the faithful finite-row map are exactly the normalized canonical composition. Both directional injections give the full isomorphism and specified inverse.

The explicit unit family has T=binom(m,2)+1,D=binom(m+1,2)−1 and λ=(an−D,T,1^(m−2)) for a,n≥m. The Vandermonde times affine-minor sum is a nonzero highest vector, and the complete normalized scalar is
\[
C_m(a,n)=(-1)^{\binom m2}\frac{(a)_m}{n}
\frac{\prod_{j=1}^{m-1}j!}{\prod_{d=2}^{m}(n)_d}.
\]
At a=n=m the scalar is (-1)^binom(m,2)(∏j!)²/(m!)^(m−1). Root and author complete proof readings pass. The recorded computations separately include4650 finite-row hook characters,729 independent multidegree hook plethysms,457 original source/target coefficient pairs and75 literal canonical polynomial pairings. The primary hook identity and invariant-form theorem retain their exact source locators; the result claims the proved actual-map form and no historical priority.

All hook-tail components are now removed from the remaining canonical-rank gate. R049's refined occupancy bound remains relevant to every other declared tail; its independent whole-proof review is A099. T066's independent whole-proof/code review is A100. The complete fixed-order hook coefficient construction and a finite multiple-coinvariant approach to stable tails are the next active coefficient tasks.
'''
for filename in ('deliverables/LEDGER.md','deliverables/IMPLICATIONS.md'):
 p=Path(filename);p.write_text(p.read_text()+'\n\n'+('## Research update — '+stamp+'\n\n' if 'LEDGER' in filename else '')+note)
p=Path('work/root/remaining_gates.md');s=p.read_text()
s=s.replace('The remaining varying-rank components retain their actual annihilator injections','R050 removes every hook tail (t,1^r) from the actual-map gate, with isomorphisms in both directions for all valid a,n, including n<t and all finite endpoints. Its finite moment morphism is faithful on hook components, and the actual bounded-row input gives the exact canonical injection. The unit Vandermonde/affine-minor family has complete nonzero scalars in every rank.\n\nThe remaining varying-rank components retain their actual annihilator injections')
s=s.replace('The unrestricted dependence on b and the remaining general varying shapes remain active;', 'A finite multiple-coinvariant Schur-determinant construction is being checked for all stable tails of fixed length, including arbitrary binary two-row sizes. The unrestricted dependence on b and the remaining general varying shapes remain active;')
p.write_text(s)
p=Path('work/root/paper_front.md');s=p.read_text()
s=s.replace('finite endpoints. R046 proves','finite endpoints. R050 proves actual canonical isomorphisms on every\nhook tail, with all inner degrees and explicit nonzero unit scalars\nin every rank. R046 proves',1)
s=s.replace('R047 gives the finite profile for tails',r'''R050 proves both actual canonical maps are isomorphisms on every
valid component \((an-t-r,t,1^r)\), for all a,n≥1. Its finite
moment morphism is faithful on hook types, and the source's actual
row bound supplies the canonical factorization even when n<t.
The Vandermonde/affine-minor unit family has its complete normalized
scalar, including every square a=n=m.

R047 gives the finite profile for tails''')
p.write_text(s)
p=Path('work/root/geometric_dictionary.md');p.write_text(p.read_text()+r'''

## Complete hook-tail canonical isomorphisms

**R050.** The finite moment algebra in degrees2 through s maps by
literal polarized power sums onto the centered row-invariant algebra.
Newton recurrence proves its finite generation bound. Its hook
Schur sheaves have the same dimensions as the target, carried by the
actual invariant differential-form and Euler/Koszul basis maps;
surjectivity therefore makes this specified map an isomorphism on
those sheaves. The input highest section retains its actual separate
row degree n under dehomogenization. Independent functional
evaluation lies in the same finite moment algebra, and its diagonal
polarization is an inverse on its image. The exact triangular moment
automorphism and Chow pullback give HM17 with scalar one. Opposite
injections prove the full bundle isomorphisms. The explicit
Vandermonde/affine-minor section and Cauchy–Binet evaluation give
the nonzero unit scalar and its reciprocal.
The image morphism is R037 EP3–5 and EGA I9.5.2. The projective
and coherent comparisons use EGA II2.4.1–2.4.2,2.5.2/2.5.4;
the frame descent uses SGA3 I4.5/4.7.2–4.7.3; the Schur and
representation-K0 operations use SGA6 VI3.3 and V4.2,4.4,4.8–4.9.
Cote133/028 is carried by A012's exact tensor-word/Young dictionary.
''')
p=Path('work/root/CHECK_EVENTS.tsv');fields=next(csv.reader(p.open(newline=''),delimiter='\t'))
with p.open('a',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t')
 w.writerow(dict(statement_id='R-050',date=stamp,who_model_effort_run='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01',type='targeted proof check',outcome='Read HM1–27 and all seven sections in full. Checked exact finite-degree power-sum generation/Newton maps, virtual alphabet hook computation, Solomon alternating-numerator argument and polynomial Koszul basis, summed componentwise faithfulness, bounded-row independent evaluation at n<t, scalar-one actual canonical factorization and both inverses. Checked complete unit highest vector, all row bounds, Cauchy–Binet/Euler constants, moment substitution scalar, square values and every vanishing/positive endpoint. PASS. Numerical receipts and primary-source full readings remain separately credited to the author; archive independent review is active.'))
print(stamp,'integrated R050 and A099/A100')
