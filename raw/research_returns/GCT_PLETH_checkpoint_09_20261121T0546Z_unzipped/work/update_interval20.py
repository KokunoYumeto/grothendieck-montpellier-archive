from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv
stamp=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()
p=Path('work/build_package.py');s=p.read_text()
assert "'work/theta/unstable_hook/all_fixed_order_hook_report.md'" not in s
s=s.replace("'work/theta/unstable_hook/pair_boundary_hook_report.md'", "'work/theta/unstable_hook/pair_boundary_hook_report.md','work/theta/unstable_hook/all_fixed_order_hook_report.md'")
for filename in ['work/archive/HOOK_TAIL_CANONICAL_REVIEW.md','work/archive/ALL_FIXED_ORDER_HOOK_REVIEW.md']:
 if Path(filename).exists() and repr(filename) not in s:
  s=s.replace("'work/archive/PAIR_BOUNDARY_HOOK_REVIEW.md'", "'work/archive/PAIR_BOUNDARY_HOOK_REVIEW.md',"+repr(filename))
row=('Q-ALL-FIXED-ORDER-HOOKS','T-067 AF1–21; G027 FA4/6; T049; G037','Evaluate every valid hook tail at every fixed positive ideal order','proved with explicit order and encoding bounds','For m≥4,k≥1,a≥1,t≥0,0≤r≤m−2 and (m−2)a≥mk+r, all outer labels have the positive formula AF20 with at most1+D_k(2(m²+3m−4)−1) disjoint bounded polytopes of at most m²+3m−4 variables. The exact complex has q≤k selected terms; complementary hook pairing gives residual Sym^A h_(m−q)⊗Λ^(r−s)h_(m−q), A≤k−q. The normal representation has rank and degree bounded by k, all subsequent LR additions have at most k cells, and every sign is specified. The signed correction is the actual jet-image multiplicity, between0 and D_k, giving complete point deletion. Values and support take f(k)poly(m+binary lengths); matrix construction has f(k)(m+k+1)^(2k+O(1)) times polynomial bit length. Together G037 and T067 cover all stable and unstable hook charts; unrestricted polynomial dependence on k remains open.')
anchor="      ('Q-HOOK-PAIR-BOUNDARY'";assert anchor in s
s=s.replace(anchor,'      '+repr(row)+',\n'+anchor)
s=s.replace('T066 also completes every valid boundary a=2k−1; the remaining hook range is a≤2k−2.','T067 completes the entire remaining physical hook range at every fixed k. Its explicit dependence on k and encoding scope are retained.')
p.write_text(s)
note=r'''## Every hook chart at every fixed positive ideal order

T067 completes the entire physical range (m−2)a≥mk+r. Its exact restriction complex has at most k selected-subset terms. The a-rectangle perfect pairing reduces every surviving residual Schur module to Sym^A(h_(m−q)) tensor Λ^(r−s)(h_(m−q)), with A≤k−q. Each normal highest space has rank and degree bounded only by k and is computed by explicit rational raising kernels or the fully specified alternant/class trace. Subsequent induction adds at most k boxes to a single large hook. The complete signs are sign_q^(a+1) after removal of the common determinant twist. This evaluates the entire finite signed complex.

The total correction is the multiplicity of the actual first jet image, so it lies between0 and D_k and is at most the stable coefficient. The same bounded-excess enumeration and disjoint deletion give the complete positive formula with the earlier piece/variable bounds. Exact values and support have f(k)poly(m+binary lengths) complexity, and the full matrix construction has its displayed fixed-order bound. Root has read the complete seven-section proof and executable and recorded PASS. Author and independent archive events and numerical receipts retain their separately dated actual scopes. No physical fixed-k hook interval remains; uniform polynomial dependence on unrestricted k is still a gate.
'''
for filename in ('deliverables/LEDGER.md','deliverables/IMPLICATIONS.md'):
 p=Path(filename);p.write_text(p.read_text()+'\n\n'+('## Research update — '+stamp+'\n\n' if 'LEDGER' in filename else '')+note)
p=Path('work/root/remaining_gates.md');s=p.read_text()
s=s.replace('The current remaining hook range is a≤2k−2.','T067 completes every remaining physical hook interval at every fixed k, through the entire q≤k restriction complex and its exact complementary-hook maps. Values/support and the positive construction have the displayed fixed-order bounds. No fixed-k physical hook interval remains; unrestricted polynomial dependence on k remains active.')
p.write_text(s)
p=Path('work/root/paper_front.md');s=p.read_text()
s=s.replace('T064–T066 complete\nthe fixed-order unstable hook chart throughout every valid a≥2k−1.','T067 completes every valid unstable hook chart at every fixed\npositive ideal order, with all exact maps, positive cells and stated\norder-dependent complexity bounds.')
s=s.replace('| Fixed-order unstable hooks, a≥2k−1 | T064–T066:', '| Every valid fixed-order unstable hook | T067:')
p.write_text(s)
p=Path('work/root/geometric_dictionary.md');p.write_text(p.read_text()+r'''

## Complete fixed-order hook charts

**T067.** G027 FA4 and T049 give the actual coherent restriction
complex and diagonal quotient. AF9–12 are perfect exterior-column
pairings on the normal and residual summands; their contractions
preserve the chosen determinant lines and ordered-subset orientation.
The residual skew module has disjoint row and column slots, yielding
the displayed symmetric/exterior tensor isomorphism. Rational normal
raising kernels, block-mean splittings and Young induction compute
the remaining exact terms. Its first image is the same jet sheaf
under the triangular Taylor and horizontal-form maps, proving all
correction bounds. The ordered primitive-Young kernel basis gives
the stated rational linear comparison with the retained point set.
Projective/coherent transport uses EGA II2.4.1–2.4.2,2.5.2/2.5.4;
frame descent uses SGA3 I4.5/4.7.2–4.7.3; representation-K0 and
Schur operations use SGA6 VI3.3 and V4.2,4.4,4.8–4.7–4.9,
with the specific operations V4.8 and Corollary4.9 understood as
in the preceding dictionary. Cote133/028 is carried by A012's
exact tensor-word and Young maps.
'''.replace('V4.2,4.4,4.8–4.7–4.9,\nwith the specific operations V4.8 and Corollary4.9 understood as\nin the preceding dictionary.','V4.2,4.4,4.8–4.9.'))
p=Path('work/root/CHECK_EVENTS.tsv');fields=next(csv.reader(p.open(newline=''),delimiter='\t'))
with p.open('a',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t')
 w.writerow(dict(statement_id='T-067',date=stamp,who_model_effort_run='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01',type='targeted proof check',outcome='Read AF1–21 and all seven sections plus the complete executable. Checked exact concentration q≤k, nondegenerate complementary-normal pairing, disjoint row/column skew maps, every rho/s/A bound and rank-stable normal kernel, Weyl/class trace formula, all subgroup signs, decorated induction with at most k added cells, actual jet-image inequalities, primitive-Young comparison, positive deletion and both bit/encoding bounds. PASS. Author and independent computations/reviews are separately recorded, without claiming an unexecuted root sweep.'))
print(stamp,'integrated complete T067')
