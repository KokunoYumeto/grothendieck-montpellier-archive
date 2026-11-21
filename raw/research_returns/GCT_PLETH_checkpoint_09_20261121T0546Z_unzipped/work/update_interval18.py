from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv
stamp=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()
p=Path('work/build_package.py');s=p.read_text()
assert "'work/theta/unstable_hook/pair_boundary_hook_report.md'" not in s
s=s.replace("'work/theta/unstable_hook/hook_endpoint_report.md'", "'work/theta/unstable_hook/hook_endpoint_report.md','work/theta/unstable_hook/pair_boundary_hook_report.md'")
s=s.replace("'work/archive/FIXED_SECOND_PART_REVIEW.md'", "'work/archive/FIXED_SECOND_PART_REVIEW.md','work/archive/HOOK_ENDPOINT_REVIEW.md'")
row=('Q-HOOK-PAIR-BOUNDARY','T-066 PB1–15; G027 FA4/6/8–9; T049 DP1–10','Evaluate every valid hook boundary a=2k−1','proved with the stated fixed-order and encoding bounds','For k≥2 and every physical m,r,t, the exact restriction complex has only ambient, singleton-jet and pair terms. The pair module is Ind_(S2×S_(m−2))^(Sm)(1⊗Λ^(r−1)h_(m−2)), zero at r0, with the proved orientation and determinant signs. Its multiplicity is the horizontal-two-strip indicator. The coefficient is stable hook minus jet plus pair; the net deleted-point correction is nonnegative and at most D_k. All explicit matrices and fixed-order bounds are retained. Together T064–T066 cover every valid a≥2k−1; the missing k1,a1 endpoint has no physical input.')
anchor="      ('Q-FIXED-ORDER-HOOKS'";assert anchor in s
s=s.replace(anchor,'      '+repr(row)+',\n'+anchor)
s=s.replace('The remaining hook range is a<2k.','T066 also completes every valid boundary a=2k−1; the remaining hook range is a≤2k−2.')
p.write_text(s)
note=r'''## Exact pair term at the next hook boundary

T066 completes every valid a=2k−1 boundary, with k≥2. The physical partition inequality is exactly the high-degree requirement N≥mk of the already proved restriction complex. A skew-column bound forces every selected-subset term of size at least three to vanish. The singleton normal substitution is triangular with injective associated graded and equal Pieri dimensions, giving the actual hook jet space. The sole pair normal term is its Cartan multiplication, and its slot interchange, subset orientation and determinant twists give exactly
\[
\operatorname{Ind}_{S_2\times S_{m-2}}^{S_m}
 (\mathbf1\otimes\Lambda^{r-1}\mathfrak h_{m-2})
\]
for r≥1, and zero for r0. Thus the exact sequence has a surjective jet-to-pair map, and the net correction is the nonnegative difference of the jet multiplicity and the horizontal-two-strip indicator. The prescribed low-excess stable points realize that correction by disjoint positive deletion cells with the earlier D_k bound. Root and author whole-proof/code readings pass. The author receipt records6386 coefficient/parity comparisons,1669 selected-point cases with18844 points and105 literal cases with36012 cells. Rectangular's original MN computation independently checks456 coefficients,324 with an active pair parameter. These numerical events remain distinct from the actual-complex proof. Independent whole-proof archive review is queued.

Together T064–T066 complete every valid hook chart with a≥2k−1. The remaining active hook interval is a≤2k−2, where the same exact complex is being evaluated with all surviving selected subsets. No uncompleted generalization is counted as movement.
'''
for filename in ('deliverables/LEDGER.md','deliverables/IMPLICATIONS.md'):
 p=Path(filename);p.write_text(p.read_text()+'\n\n'+('## Research update — '+stamp+'\n\n' if 'LEDGER' in filename else '')+note)
p=Path('work/root/remaining_gates.md');s=p.read_text().replace('The current remaining hook range is a<2k.','T066 completes every valid a=2k−1 boundary by the actual three-term restriction complex, including the unique pair module and its complete signs; the net correction remains positive point deletion. The current remaining hook range is a≤2k−2.')
p.write_text(s)
p=Path('work/root/paper_front.md');s=p.read_text().replace('T064–T065 complete\nthe fixed-order unstable hook chart throughout every valid a≥2k.','T064–T066 complete\nthe fixed-order unstable hook chart throughout every valid a≥2k−1.')
s=s.replace('| Fixed-order unstable hooks, a≥2k | T064–T065:', '| Fixed-order unstable hooks, a≥2k−1 | T064–T066:')
p.write_text(s)
p=Path('work/root/geometric_dictionary.md');p.write_text(p.read_text()+r'''

## The exact pair correction in the fat-frame complex

**T066.** The coherent restriction complex is G027 FA4 on the
degree-N part of the fat linear arrangement, with T049's actual
diagonal quotient and every ordered-subset orientation. The physical
partition inequality is exactly N≥mk. Exact Schur multiplicity
projection preserves the complex. The a-rectangle exterior pairing
gives its ambient hook module; normal Taylor substitution and the
horizontal local frames give the singleton jet object. The pair's
Cartan multiplication and complementary-column pairing give its
displayed induced exterior-power representation with all determinant
lines. Concentration leaves the exact sequence PB15, so the net
correction is the dimension of the actual image sheaf's fiber.
Its lattice-point deletion is carried to that same kernel dimension.
The flag/projective and coherent sheaf locators are EGA
II2.4.1–2.4.2 and2.5.2/2.5.4; descent is SGA3 I4.5 and
4.7.2–4.7.3; Schur operations and the representation-K0 identity
are SGA6 VI3.3 and V4.2,4.4,4.8–4.9. Cote133/028 uses
the same actual tensor-word and Young maps of A012.
''')
p=Path('work/root/CHECK_EVENTS.tsv');fields=next(csv.reader(p.open(newline=''),delimiter='\t'))
with p.open('a',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t')
 w.writerow(dict(statement_id='T-066',date=stamp,who_model_effort_run='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01',type='targeted proof check',outcome='Read complete PB1–15, all five sections, full executable and saved author receipt; rechecked the actual FA4/FA6/FA8–9 and DP quotient setup. Verified N≥mk equivalence, every q≥3 vanishing, singleton filtered isomorphism/Pieri dimensions, unique pair Cartan map, subgroup orientation and determinant signs, all r0/top-leg/k1-invalid endpoints, exact sequence and positive bounded-excess deletion with full routes. PASS. Author and rectangular computations are separately credited; independent archive review is queued.'))
print(stamp,'integrated T066 and A098')
