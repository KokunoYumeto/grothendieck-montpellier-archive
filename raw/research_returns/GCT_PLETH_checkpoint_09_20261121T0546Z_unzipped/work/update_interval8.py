from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv,re

ROOT=Path(__file__).resolve().parent.parent
stamp=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()
p=ROOT/'work/build_package.py';s=p.read_text()
assert "'work/root/all_five_row_support_report.md'" not in s
s=s.replace("'work/theta/outer5/two_below_all_powers_report.md'])", "'work/theta/outer5/two_below_all_powers_report.md','work/theta/outer5/three_below_all_powers_report.md','work/root/second_power_zero_twist_report.md','work/root/all_five_row_support_report.md','work/theta/oscillator_charge_report.md'])")
s=s.replace("'work/rectangular/finite_base_canonical_ranges.md',", "'work/rectangular/finite_base_canonical_ranges.md','work/rectangular/two_column_tail_unit_family.md','work/rectangular/linear_second_row_canonical_ranges.md',")
reviews=['THREE_BELOW_ALL_POWERS_REVIEW.md','FINITE_BASE_CANONICAL_REVIEW.md','SECOND_POWER_ZERO_TWIST_REVIEW.md','ALL_WALL_SUPPORT_REVIEW.md','OSCILLATOR_PRIMARY_NOTES.md']
s=s.replace("'work/archive/END_WALL_SUPPORT_REVIEW.md'])", "'work/archive/END_WALL_SUPPORT_REVIEW.md',"+','.join(repr('work/archive/'+x) for x in reviews)+"])")
s=s.replace('T048 evaluates c=2k−3 for k≥8;', 'T051 evaluates c=2k−3 for every possible k≥2;')
s=s.replace('G026 evaluates the entire first-power zero-twist two-row slice, completing all k=1 together with T045 and G021;', 'G026 and G030 complete all ideal orders k≤2 with T045,T050,T051,G021, including both determinant/complement regions λ2≤n+2 orλ4≥n−2;')
s=s.replace('The remaining direct positive-formula gate is cancellation-free evaluation of those explicit bounded tables on the unevaluated walls and central regions.', 'The remaining direct positive-formula gate is cancellation-free evaluation of those explicit bounded tables for k≥3 and0≤c≤2k−4, after also removing the completed complementary and special families. G031 already decides every zero throughout this remaining region.')
old=next(line for line in s.splitlines() if "('Q-NONVANISH5'," in line)
new="      ('Q-NONVANISH5','G-024,G-028,G-031 NW1–8; complete344-node catalog','Classify nonvanishing for all outer-degree-five Schur labels','proved','G031 completes every proper nonempty gap support:172 seeds,344 deficient nodes,1896 point transitions and2084 bounded ray checks exhaust158 isolated points and196 stable ray bases. Its fixed normalization/table decision, together with G028 strict support and the determinant line, decides every coefficient in polynomial bit complexity. All maps, signs and interacting-ray endpoints are proved and independently checked.'),"
s=s.replace(old,new)
s=s.replace('R032 adds five explicit preceding-degree families to the degree-five recursive base and injects every remaining second-row-band annihilator into explicit finite Pieri modules.', 'R032 adds five preceding-degree families; R034 proves the arbitrary-power band injection and the exact capped linear thresholds B_t+Σ_(r=5)^(a−1)min(r,t), as well as b≥t(a−1). R033 gives the entire unit-multiplicity two-column-tail family and its stated actual image and rectangular-Kronecker consequences.')
needle="      ('Q-MAP-OUTER5',"
entry="      ('Q-THETA-CHARGE','T-052 OC1–31','Identify the exact frame quotient with a charged oscillator and actual theta branching multiplicity','proved','The block homogenization maps the regular diagonal quotient to positive-charge coinvariants of U(m−2,1)×U(m). A finite rational Fischer projector gives harmonics; complementary-column and Gram pairings give the exact balanced module, all determinant/vacuum shifts, and the stated Schur functor of an irreducible one-column oscillator.'),\n      ('Q-IDEAL-ORDER2','G-030 ZS1–11;T-045,T-050,T-051,G-021','Evaluate every outer-five flag family of ideal order at most two','proved','The disjoint twist families exhaust k=1,2, and the stable k=0 chart is explicit. Every shape with λ2≤n+2 orλ4≥n−2 has a fixed positive coefficient formula, exact support and specified complementary-column map.'),\n"
assert needle in s;s=s.replace(needle,entry+needle)
p.write_text(s)

paragraph=r'''
## Current complete support, charged theta model and stronger actual maps

G031 closes the complete outer-five nonvanishing question. Every one of the fourteen proper nonempty gap supports is exhausted by the fixed344-node catalog and the proved two-direction normalization. The proof checks every bounded initial ray transition, including the diagonal where both stable directions interact. Together with G028 and the determinant line, the fixed evaluator decides all seven labels in every degree with polynomial bit complexity. All344 printed rows, the TSV and evaluator index have an independent comparison.

G030 closes every ideal order at most two, and T051 closes the entire three-below family. The remaining direct positive coefficient gate is k≥3 and0≤c≤2k−4 after the previously completed determinant/complement and special families are removed. Its zero sets are already completely decided by G031.

T052 supplies an exact charged-oscillator realization of every outer degree: block homogenization, the regular diagonal quotient, the rational Fischer harmonic projector, the compact-member highest weight, the determinant/dual pairings and the Schur functor of the irreducible one-column module are all specified. The finite normalizer projector remains explicit in this comparison.

R034 proves actual canonical surjectivity on every second-row band in the stated capped linear profile, by a newly evaluated derivative kernel with all spectator factors retained. R033 computes the full two-column-tail unit family through the exact exterior transfer and its invariant tensor, and transports it to the stated actual canonical images and rectangular Kronecker coefficients. R031 already settles every target-outer-five canonical rank.
'''
for name in ['work/root/paper_front.md','deliverables/IMPLICATIONS.md']:
 with (ROOT/name).open('a') as f:f.write(paragraph)
gate=ROOT/'work/root/remaining_gates.md'
(ROOT/'work/root/gate_history_through_interval8.md').write_text(gate.read_text())
gate.write_text(r'''# Current unresolved items and strongest proved reductions

This section records the current gates. Earlier chronological gate descriptions are preserved in the dated ledger and gate_history_through_interval8.md.

## Positive formulas

G009–G011 prove terminating positive formulas for every coefficient and every actual canonical image multiplicity. The uniform polynomial-description gate concerns their Hilbert-basis size, Reynolds generator list, elimination presentation and witness bounds when the outer degree varies.

T037 gives the complete fixed direct positive formula in outer degree four. In outer degree five, G027/T049 replace every unspecified flag-cohomology rank by actual arrangement, diagonal-quotient and restriction maps; each class trace is48 explicitly signed bounded-table counts. G021,T045,T050,T051 give every c≥2k−3 permitted twist; G026/G030 finish all ideal orders at most two. G023 and the further completed special families remain fully evaluated. The residual direct positive-formula region has k≥3,0≤c≤2k−4 after removing the determinant/complement images and those special families. The remaining task is a cancellation-free fixed count for those explicit characters.

G031 has completed nonvanishing for every outer-five label and every output shape, including all equal-row walls and their intersections. There is no remaining outer-five support gate.

## Theta and the exact algebraic comparison

T052 identifies every coefficient with an actual charged oscillator harmonic multiplicity and the specified lowest module in a Schur functor of the one-column oscillator. The maps include all vacuum shifts, covers, determinant and dual pairings, the block homogenization and the finite rational projector. The remaining general positive conversion concerns the explicitly retained highest-type and finite-normalizer projector. The original Alpöge transfer still requires the particular equivariant period/theta morphism from the cited note to these specified spaces; that is a distinct requested comparison whose source map has not been supplied.

## Actual canonical ranks

R031 completely determines the canonical rank with target outer degree five. For varying degree, G013–G014 and R011–R032 prove their stated prime-semigroup, first-row, common-polarization, cofactor-strip, finite-base and recursive ranges. R034 adds the arbitrary-power band injection and the capped profile B_t+Σ_(r=5)^(a−1)min(r,t), with all multiplicities. R033 supplies its explicit two-column-tail unit targets, stated image ranges and rectangular-Kronecker consequences.

The remaining varying-rank gate is the actual annihilator after these proved removals. At the critical square-minus-one boundary it injects into the specified common-polarization kernel tensored with one row; its first-factor labels retain the exact lower bounds r²+1 on the first row and r(r−1) on the second row. Outside the completed band and component families, evaluate that remaining explicit image or kernel.

## Other precise gates

For width seven, T018 evaluates the end-node sector and G010 supplies a general finite count. The smaller direct gate is the remaining discriminant-valuation filtration on the specified G2 invariant spaces.

The archive assertion rows retain their precise crystalline Lefschetz/freeness, motivic self-duality, unlabeled-triangulation reconstruction and completed characteristic-class target inputs. All thirteen target leaves and the recorded neighboring pages have been read. Literal false assertions have their counterexamples and corrected maps; the coefficient-ring classification remains open after the proved DVR theorem and explicit local counterexample.

The Alpöge theorem is accepted as requested. The named Lean files and scan report are absent from the supplied files. No Masullo work or statement identifier was supplied. These are retained input gates, with no invented locator.

Review02 at04:01:21Europe/Berlin recorded genuine main-gate movement and a zero no-movement streak. The next formal review is05:01:08Europe/Berlin. Checkpoint06 is due04:31:08Europe/Berlin. This section records ongoing work and does not invoke the stopping rule.
''')
with (ROOT/'work/root/geometric_dictionary.md').open('a') as f:
 f.write(r'''

## Complete support, oscillator and linear-band transports

**G030–G031 and T051.** Their exact maps are the stated normal-order substitution, signed arrangement quotient, rank-adaptive Young extraction and invariant-section multiplication. The complete support catalog is transported by the actual first-end chart and last-end complementary-column pairing, with both determinant signs retained. The frame models exist over Z[1/5], and each fixed-degree Young projection is defined after inverting its factorial denominators. The generic-fiber ranks use SGA3 I4.5,I4.7.2–4.7.3, SGA6 V4.2,4.4,4.8–4.9, EGA II2.4.1–2.4.2 and II2.5.2,2.5.4. G027§6's finite free resolutions give the locally free K0 transport of SGA6 VI3.3. The archive comparison is cote133/024–029 via A010.

**T052.** The affine polynomial scheme has coordinates X_ai,Y_i and contraction equations R_a=Σ_iX_aiY_i. The block homogenization is an actual map on each multigraded module, compatible with multiplication by the diagonal generators. Its quotient is precisely the frame-arrangement module, and the rational polynomial q(ΣR_aC_a)/q(0) gives its harmonic splitting. The displayed GL(F), GL(W), torus and permutation actions are comodules and their Lie operators in SGA3 I4.5,I4.7.2–4.7.3. The real symplectic embedding and the explicit vacuum character provide the unitary realization after scalar extension. Complementary exterior columns and the rational Gram form give the exact Schur/dual comparison in SGA6 V4.2,4.4,4.8–4.9, and hence the cote133/024–029 dictionary. The coherent quotient and its finite resolutions use the same EGA II/SGA6 VI3.3 transport as G027.

**R033–R034.** The exterior transfer is the actual GL2 raising operator on the skew-Cauchy summand; its kernel, rational Gram coevaluation and projected matching tensor produce a specified invariant section. Its balanced flag map is UT16. The derivative kernel in LP7 is the actual Cauchy summand, with spectator tensor factors retained, and LP12 is the normalized coproduct/common-polarization injection. Duality is the scalar-one tensor pairing of R031. These rational natural transformations define the SGA3 representation-comodule maps and the SGA6 Schur operations just cited. Their image ranks belong to the EGA I9.5.2 graded coordinate-image scheme. UT19 further specifies the Chow-padding, determinant-realization and coordinate-restriction maps used in the rectangular comparison. Each fixed-degree construction has an integral model after clearing its displayed averaging and factorial denominators; all asserted ranks concern characteristic zero.
''')
with (ROOT/'deliverables/LEDGER.md').open('a') as f:
 f.write('\n## Research update — '+stamp+'\n'+paragraph)

eventpath=ROOT/'work/root/CHECK_EVENTS.tsv'
with eventpath.open(newline='') as f:r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;events=list(r)
checks=[
 ('G-030','targeted proof check','Read full ZS1–11 proof after construction: all normal Schur-table entries, missing-monomial negative coefficient convention, exact skew extraction and orientations, complete residue/initial-range degree proof,512400 fixed constants, every zero list, literal polytopes and the full first-two-order/complement corollary; PASS. Independent full constants and whole proof checks are separately logged.'),
 ('G-031','targeted proof check','Read full NW1–8 proof: both actual stable maps, minimum-one face endpoint,172-seed/zero-sum generation, all bounded ray transitions Q≤3, simultaneous-stability equality, complete induction in both directions, determinant parity and all outer-shape cases; PASS. Complete344-row catalog reconstruction and comparison are separately attributed to archive A060.'),
 ('G-031','computation or formal certificate','Executed all14 proper-face graph closures:344 nodes,1896 point edges,2084 bounded ray checks,158 isolated points and196 stable-ray bases. Evaluator compared3640 actual support entries in the complete congruent gap box0..5 with both determinant parities; every support and returned exact value agreed. Independent larger reconstruction is separately logged.'),
 ('T-051','targeted proof check','Read whole ET1–13 proof and endpoint sections: all pair exchange signs and omitted Schur terms, three exceptional triple modules and concrete maps, exact pair-to-triple quotient, every branch, degree/negative-index endpoint and positive count. Requested and re-read prose correction to subtract the triple dimension; PASS.'),
 ('T-052','targeted proof check','Read whole OC1–31 in two complete sequential reads: real centralizers and compatible complex structure, every Weyl bracket/adjoint/center, half-integral vacuum cover, charge homogenization and lowering coefficient, regular quotient, rational Fischer projector, strict-range harmonic tensor labels, all determinant/Gram dual maps, first-row transport, one-column irreducibility, Schur branching and endpoints; PASS.'),
 ('R-033','targeted proof check','Read whole UT1–19 proof: exterior-transfer sign and scalar, every skew-Cauchy summand, explicit hook polytabloid normalization, invariant Gram coevaluation and j! matching map, dense balanced-chart inverse, full unit coefficient range, actual image ranges and exact IP coordinate-ring chain; PASS.'),
 ('R-034','targeted proof check','Read whole LP1–22 proof: exact Cauchy derivative kernel with all spectator factors, arbitrary-L membership, successive band injectivity, explicit common-polarization inverse including b−L=t, both base iterations, every capped-threshold endpoint, rational extension and literal boundary counterexample; PASS.'),
 ('R-032','targeted proof check','Re-read FK11 after archive correction: chain polytopes use max(a,length λ) rows, preserving the full codomain count even for zero actual targets of length greater than a. The earlier root reading did not identify this padding issue; amended text and full bound now PASS.'),
 ('SRC-MACDONALD-SKEW','used and rechecked in this run','Opened/read primary second-edition ChapterI§5 equations(5.1)–(5.4), pp69–70, including the complete derivation, and containment(5.7)p71. Applied the exact product-coefficient and two-row skew determinant forms in G030; no claim to read the entire book.'),
]
for sid,typ,outcome in checks:
 row={k:'' for k in fields};row.update(statement_id=sid,date=stamp,who_model_effort_run='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01',type=typ,outcome=outcome);events.append(row)
with eventpath.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
print(stamp,'integrated G030–31,T051–52,R033–34; support gate closed')
