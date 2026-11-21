from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv

ROOT=Path(__file__).resolve().parent.parent
stamp=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()
p=ROOT/'work/build_package.py';s=p.read_text()
assert "'work/root/end_wall_support_report.md'" not in s
s=s.replace("'work/root/five_row_strict_nonvanishing.md'])", "'work/root/five_row_strict_nonvanishing.md','work/root/end_wall_support_report.md','work/theta/outer5/two_below_all_powers_report.md'])")
s=s.replace("'work/rectangular/canonical_second_cofactor_strip.md',", "'work/rectangular/canonical_second_cofactor_strip.md','work/rectangular/outer_five_canonical_rank_law.md','work/rectangular/finite_base_canonical_ranges.md',")
reviews=['OUTER_FIVE_CANONICAL_REVIEW.md','TWO_BELOW_ALL_POWERS_REVIEW.md','END_WALL_SUPPORT_REVIEW.md']
s=s.replace("'work/archive/STRICT_CHAMBER_REVIEW.md'])", "'work/archive/STRICT_CHAMBER_REVIEW.md',"+','.join(repr('work/archive/'+x) for x in reviews)+"])")
s=s.replace('T046 evaluates c=2k−2 for k≥5;', 'T050 evaluates c=2k−2 for every possible k≥2;')
s=s.replace('G026 evaluates the entire first-power zero-twist two-row slice;', 'G026 evaluates the entire first-power zero-twist two-row slice, completing all k=1 together with T045 and G021;')
s=s.replace('The remaining support classification lies on equal-consecutive-row walls, after the already evaluated G021,T045–48,G026 families.', 'G029 also completely classifies both outer equal-row walls with the other three gaps positive, by twelve finite exceptions and six stable rays with exact multiplicity vectors and complementary-wall signs. The remaining support classification lies on the two central equal-row walls and intersections of at least two equal-row walls, after the already evaluated coefficient families.')
s=s.replace('and G025 settles actual image nonvanishing for every five-row shape with all gaps at least two.', 'R031 determines the entire actual canonical rank law with target outer degree five, in every inner degree. R032 adds five explicit preceding-degree families to the degree-five recursive base and injects every remaining second-row-band annihilator into explicit finite Pieri modules.')
needle="      ('Q-MAP',"
entry="      ('Q-MAP-OUTER5','R-031 OF1–11; Jacob Def1.1.11,§4.2,Table4.4; CIM Theorem1.1','Determine every canonical rank with target outer degree five','proved','The actual rank is the source multiplicity for n≤4, the target multiplicity minus the eight published kernel copies for n=5, and the full target for n≥6; scalar-one adjunction and exact fourth-square normalization are proved. All313 small-degree shapes were independently evaluated.'),\n      ('Q-IDEAL-ORDER1','G-026;T-045;G-021, exact c=λ2−λ3 dictionary','Evaluate every outer-five flag family of ideal order one','proved','G026 covers c=0, T045 covers c=1, and G021 covers every c≥2, including all support and determinant parity.'),\n"
assert needle in s;s=s.replace(needle,entry+needle)
p.write_text(s)

paragraph=r'''
## Completed outer walls, two-below endpoints and degree-five canonical ranks

G-029 classifies support on both outer equal-row walls with the other three gaps positive. Its twelve exceptional points and six rays give complete multiplicity vectors. Every other input has all seven labels. The proof retains the exact invariant-section maps and the stable first-axis isomorphism while exhausting an infinite domain by a closed 24-state/192-edge graph. The only remaining wall classification lies on the two central walls and intersections of at least two walls, further reduced by the evaluated coefficient families.

T-050 completes the entire c=2k−2 family for every possible k≥2 through an actual oriented pair restriction quotient. Its eight endpoint branches have fixed positive lattice-point formulas and exact support. G026, T045 and G021 together already complete every order-one family: c=0, c=1, and c≥2 exhaust its nonnegative twist.

R-031 determines every actual canonical rank with target outer degree five: source multiplicity at n≤4, target minus the eight specified kernel copies at n=5, and full target at n≥6. Its exact adjoint pairing, fourth-square transverse-grid normalization and published43×43 matrix have been checked. R-032 propagates the complete finite lower kernels into five preceding-degree families and gives an actual injection of every remaining second-row-band annihilator into explicit Pieri modules, with a positive chain-polytope upper bound.
'''
for name in ['work/root/paper_front.md','work/root/remaining_gates.md','deliverables/IMPLICATIONS.md']:
 with (ROOT/name).open('a') as f:f.write(paragraph)
with (ROOT/'work/root/geometric_dictionary.md').open('a') as f:
 f.write(r'''

## Exact transport of G029, T050 and R031–R032

**G-029.** The graph edges are multiplication by the explicit invariant flag sections of G024. Its contractions use the actual G027 section map and multiplication by u on the balanced chart. The complementary outer wall uses the perfect exterior-column pairing and its determinant sign. These are SGA3 I4.5,4.7.2–4.7.3 comodule morphisms; the Schur operations are SGA6 V4.2,4.4,4.8–4.9 and cote133/024–029 via A010. EGA II2.4.1–2.4.2 supplies the Proj charts, II2.5.2,2.5.4 the exact associated-sheaf transport. The finite equivariant resolution of G027§6 gives the locally free K0 class of SGA6 VI3.3. Thus the wall support tables compute the ranks of these specified component maps.

**T-050.** The actual signed restriction complex of G027 identifies the complete order-k jet cokernel with the oriented pair module. Its displayed symmetric multiplication and determinant(v,z1,z2)^c map fix the Schur component and the even determinant twist. Taking its finite equivariant free resolution gives the same exact coherent-to-locally-free K0 transport. This extends the positive coefficient formula to every permitted k without asserting an unproved extension of a different geometric line-restriction map. Each final Newton polytope counts the already identified Schur multiplicity.

**R-031.** The tensor averaging pairing identifies the dual of h_{d,e} with h_{e,d} with scalar one. The transverse-block calculation identifies the fourth-square map with the stated rational multiple of Jacob's adjacency operator. Its invertible right-multiplication matrix and the multilinear Schur–Weyl component map prove actual injectivity. These normalized maps define the corresponding graded coordinate-image scheme by EGA I9.5.2, commute with SGA3 base extension, and act on the same SGA6 Schur classes. The image multiplicities are the graded coordinate-image ranks. Jacob's source computation and the independently verified finite matrix are distinguished in the proof and check ledger.

**R-032.** Every step of the annihilator injection is the displayed symmetric coproduct followed by common polarization, with its explicit binomial scalar. The perfect pairing carries the final injection to a bound for the actual coordinate-image cokernel, not only an inequality between abstract Schur characters. Successive Pieri component maps identify the polynomial chain counts with the specified tensor codomain. The construction is rational and functorial, hence transports to SGA3 representation group schemes and their SGA6 representation K0; its graded coordinate-image ranks use EGA I9.5.2. The exact Schur/plethystic archive dictionary is cote133/024–029 via A010.
''')
with (ROOT/'deliverables/LEDGER.md').open('a') as f:
 f.write('\n## Research update — '+stamp+'\n'+paragraph)

eventpath=ROOT/'work/root/CHECK_EVENTS.tsv'
with eventpath.open(newline='') as f:r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;events=list(r)
checks=[
 ('G-029','targeted proof check','Read whole EW1–8, all twelve finite points and six ray vectors, complementary-wall determinant exponent, stable chart isomorphism, all seed/generator bounds and the raised-threshold graph exhaustion. Verified the normalization-offset induction without assuming it commutes with later b,c increments; PASS.'),
 ('T-050','targeted proof check','Read whole ER1–15: actual Cech jet quotient, vanishing of every higher subset term, pair determinant multiplication and orientation, all eight endpoint branches, exact degree bounds, positive constants and all support lists; PASS. Independent full constant reconstruction is separately attributed.'),
 ('R-031','targeted proof check','Read entire OF1–11 proof and complete finite rank tables. Re-read the corrected right-multiplication convention for Jacob B42, its inverse implication, multilinear Schur–Weyl transfer, scalar-one adjunction, transverse-grid normalization, n1–4 injectivity and all n≥5 propagation; PASS.'),
 ('R-032','targeted proof check','Read whole FK1–12 and complete28-row base-kernel table: all common-polarization maps, successive injective restrictions on entire multiplicity spaces, exact tail antichains, first-row bound, complete support-exclusion inequalities, positive chain-polytope bound and rank-two example; PASS.'),
 ('SRC-JACOB','used and rechecked in this run','Opened/read primary thesis Definition1.1.11p9, Definition4.1.1p92 and relevant§4.2 statements pp95–99, including the transpose/right-multiplication convention, transverse adjacency operator,43×43 representation and determinant2^223·3^67. Table4.4 entries were independently transcribed and checked by the rectangular and archive agents. No claim to rerun the original2,627,625-orbit enumeration or read the entire thesis.'),
 ('G-029','computation or formal certificate','Executed all30 parity seeds,8 generators,24 deficient states and192 transitions, including exact trace fields; every recorded exit and finite/ray value agrees. The independent Jacobi–Trudi reconstruction and stable-value checks are separately logged.'),
]
for sid,typ,outcome in checks:
 row={k:'' for k in fields};row.update(statement_id=sid,date=stamp,who_model_effort_run='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01',type=typ,outcome=outcome);events.append(row)
with eventpath.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
print(stamp,'integrated G029,T050,R031,R032; six root checks')
