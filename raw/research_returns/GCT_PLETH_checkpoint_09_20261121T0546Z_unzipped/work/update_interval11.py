from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv
now=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()
p=Path('work/build_package.py');s=p.read_text()
assert "'work/root/all_order_one_twist_report.md'" not in s
s=s.replace("'work/root/all_order_zero_twist_report.md'","'work/root/all_order_zero_twist_report.md','work/theta/outer5/variable_wall/one_twist_report.md','work/theta/outer5/variable_wall/one_twist_strip_report.md','work/root/all_order_one_twist_report.md'")
s=s.replace("'work/rectangular/four_one_tail_canonical_rank_law.md'","'work/rectangular/four_one_tail_canonical_rank_law.md','work/rectangular/four_three_one_tail_canonical_rank_law.md'")
s=s.replace("'work/archive/ZERO_WALL_COMPLETE_REVIEW.md'","'work/archive/ZERO_WALL_COMPLETE_REVIEW.md','work/archive/FOUR_ONE_TAIL_RANK_REVIEW.md','work/archive/ONE_TWIST_CHAMBER_REVIEW.md','work/archive/ONE_TWIST_STRIP_REVIEW.md','work/theta/outer5/variable_wall/GENERAL_TRIPLE_REVIEW.md'")
s=s.replace('for k≥4,b≥1 and1≤c≤2k−4','for k≥4,b≥2 and2≤c≤2k−4')
s=s.replace('G031 already decides every zero throughout this remaining region.','G034 also evaluates both entire adjacent walls λ2−λ3=1 andλ3−λ4=1, through T055,T056, the exact rank-three triple telescope and two further cones. G031 already decides every zero throughout this remaining region.')
s=s.replace("      ('Q-CENTRAL-WALLS'","      ('Q-ADJACENT-WALLS','G-034 OW1–14; T-055 OT1–12; T-056 OS1–6','Evaluate both entire central-gap-one walls in every outer-five degree','proved','The c1 wall has a complete disjoint route through low orders, exact complementary defects0..3, the T055 chamber, T056 strip and two lower cones. A full rank-three triple identity computes the actual oriented quotient character. Stable-first-row multiplication and the perfect complementary-column pairing cover every original partition and both wall gaps, retaining outer-label signs.'),\n      ('Q-CENTRAL-WALLS'")
s=s.replace('R038 refines the already known binary isomorphism','R040 adds the complete unit family(an−2m−2,4,3,2^(m−3),1), with target1 for a≥m+2,n≥3 and image1 exactly n≥m+2; its weighted-minor scalar and inverse include all finite-row zero endpoints. R038 refines the already known binary isomorphism')
p.write_text(s)
note='''## Complete adjacent central walls and a second width-four image family

G034 completes both central-gap-one walls, λ₂−λ₃=1 andλ₃−λ₄=1, in every outer-five degree. T055 and T056 handle the upper chamber and its final strip. The new rank-three triple identity evaluates every selected triple by two exact boundary coefficients, with the actual normal Young projector, complementary-line Pieri map and subset orientation retained. The lower cones have47 and34 positive polytopes in at most nine variables. All nine evaluator routes, determinant signs and stable-first-row transports are explicit. The two cones have3,024,000 certified base constants; the unified evaluator passed1120 coefficient comparisons and672 additional actual coefficients at96 original partition inputs. The remaining direct coefficient gate is now k≥4,b≥2,2≤c≤2k−4, after completed complementary and special families. The general varying-outer-degree polynomial-description question remains open.

R040 determines the second higher-row width-four unit family λ=(an−2m−2,4,3,2^(m−3),1), m≥3. Its target multiplicity is one for a≥m+2,n≥3; its actual canonical image is one exactly for n≥m+2. The weighted affine-minor identity cancels every row-degree-four term explicitly, so the vectors extend at inner degree three. The exact normalized scalar and inverse are supplied, while a perfect rectangle-four pairing proves the finite exceptional zero endpoint. All six entries in the uniform nonzero specialization were also verified as exact rational identities in symbolic m.
'''
for name in ('work/root/paper_front.md','deliverables/IMPLICATIONS.md'):
 p=Path(name);p.write_text(p.read_text()+'\n\n'+note)
p=Path('deliverables/LEDGER.md');p.write_text(p.read_text()+f'\n\n## Research update — {now}\n\n'+note+'\nThe review03 snapshot was taken before these new completions and deliberately did not count them. Their later completion does not alter that historical record.\n')
p=Path('work/root/remaining_gates.md');s=p.read_text().replace('The remaining direct five-row coefficient gate is k≥4,b≥1,1≤c≤2k−4','T055,T056 and G034 also complete every c=1 or b=1 wall, through the actual rank-three triple telescope, fixed positive cones and exhaustive complement/stable maps. The remaining direct five-row coefficient gate is k≥4,b≥2,2≤c≤2k−4')
s=s.replace('R039 gives the complete higher-row width-four unit-family rank and inverse.','R039 gives the complete higher-row width-four unit-family rank and inverse. R040 gives the second unit family with tails(4,3,2^(m−3),1), target1 for a≥m+2,n≥3 and image1 exactly n≥m+2, including the exact finite-row complement zero.')
p.write_text(s)
p=Path('work/root/geometric_dictionary.md');p.write_text(p.read_text()+r'''

## The adjacent walls and weighted mixed-minor image

**T-055, T-056 and G-034.** The rank-three normal Young projector
extracts the same coherent section module as the normal-order and
balanced homogenization isomorphisms of G027/T049. The pair character
is carried by actual exterior-dual, dual-Pieri and binary-contraction
maps. The triple character comes from the actual complementary-line
Pieri map and the complete coefficient telescope OW6–8, retaining
the selected-subset orientation. The section class in K0 therefore
has the exact positive lattice-point count OW11–12. The frame,
coordinate and associated-sheaf arrows are EGA II2.4.1–2.4.2,
2.5.2/2.5.4; SGA3 I4.5/4.7.2–4.7.3; and SGA6 VI3.3.
The Schur operations are SGA6 V4.2,4.4,4.8–4.9, and the archive
cote133/028 comparison is A012's tensor-word, weight and Young map.
Stable first-row multiplication and perfect determinant-column pairing
are specified on every branch, including both central-gap-one walls.

**R-040.** The exterior-invariant-algebra surjection, unique vertical
Pieri strip and rectangle-four pairing give the exact unit space and
its finite exceptional zero. The complementary-minor tensor and its
weighted affine Cauchy–Binet form define the same highest polynomial
section by the printed identity D=−a²F. Its literal row-degree-four
cancellation proves extension at degree three. The normalized Chow
pullback of R037 EP3–5 has scalar HC17 and inverse HC18. These exact
matrices carry through the frame functor to SGA3 I4.5/4.7.2–4.7.3,
SGA6 VI3.3 associated bundles, and the EGA I9.5.2 image module.
Cote133/028 is again carried by the actual Schur/tensor composition
map of A012; no coefficient-only comparison replaces the image map.
''')
p=Path('work/root/CHECK_EVENTS.tsv');fields=next(csv.reader(p.open(newline=''),delimiter='\t'));who='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01'
events=[
('T-055','targeted proof check','Read whole OT1–12, all tables and scopes. Checked actual c1 module and sign, triple degree deletion, singleton involution, q≥1 dual Pieri and q=0 binary contraction exact sequence, pair-swap zero, phase initial M=−2 endpoint, all positivity logic and fixed nine-variable bijection. PASS.'),
('T-056','targeted proof check','Read whole OS1–6 and all concluding scopes. Checked full horizontal-strip degree b+2, all singleton/pair ranges, actual justification of negative-B substitution, two-variable phase keys, seventeen orders, eight-variable projection with zero-coordinate inverse, base/support proof and low-order routing. PASS.'),
('G-034','targeted proof check','Read entire saved OW1–14, all cone/certificate/support tables and geometric/check sections. Checked full rank3 alternant, two q/r boundary sums, p telescope, high-degree reversal cutoff and phase, exact actual-module maps, both affine phase substitutions, coefficient domination, all complement and stable transports, and exhaustive inverse-cone coverage. Corrected negative-coefficients wording to negative-index coefficients. PASS.'),
('G-034','computation or formal certificate','Executed13230 independent normal-Schur triple comparisons, all898 cone phase constructions and79 domination margins,3024000 base constants,336 complete restriction traces and168 actual coefficients. Unified positive evaluator passes1120 coefficient comparisons in nine routes,140 new-cone matrix witnesses, and672 actual coefficients at96 original partitions covering both walls, stable shifts and determinant parity. Initial degree1 coin-tag export omission corrected; full route rerun PASS.'),
('R-040','targeted proof check','Read whole HC1–18 and all verification/geometry scope. Checked unique invariant branch, rectangle4 zero endpoint, tensor highest equations, weighted determinant derivative and sign, row4 cancellation, full nonzero specialization, degree3 extension, arbitrary-fourth-moment cancellation, scalar/inverse and all source endpoints. PASS.'),
('R-040','computation or formal certificate','Independently verified all six HC13 specialization entries as exact rational identities in symbolic m using the four-coordinate metric diag(1,1,1,m−3). The resulting F=-20 identity holds symbolically, including m3 by the zero residual coordinate. R040_SYMBOLIC_SPECIALIZATION_CHECK.txt PASS.'),
]
with p.open('a',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t')
 for sid,kind,outcome in events:w.writerow({key:{'statement_id':sid,'date':now,'who_model_effort_run':who,'type':kind,'outcome':outcome}.get(key,'') for key in fields})
p=Path('work/root/all_order_one_twist_report.md');p.write_text(p.read_text()+'\nThe direct partition entry passed672 actual Schur coefficients at96 original partitions, covering both adjacent walls, determinant shifts and stable first-row powers zero and three. Every partition also exported its selected polytope provider. The receipt is `ONE_WALL_PARTITION_ENTRY_CHECK.json`.\n')
print(now)
