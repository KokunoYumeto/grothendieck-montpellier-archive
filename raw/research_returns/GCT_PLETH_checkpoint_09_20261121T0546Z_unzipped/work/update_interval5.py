from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv

ROOT=Path(__file__).resolve().parent.parent
stamp=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()
p=ROOT/'work/build_package.py';s=p.read_text()
s=s.replace("'work/theta/outer5/hook_all_powers_report.md',", "'work/theta/outer5/hook_all_powers_report.md',\n 'work/theta/outer5/two_row_ray_report.md','work/theta/outer5/two_row_below_ray_report.md','work/theta/outer5/two_row_line_correction_report.md',")
s=s.replace("'work/root/staircase_five_report.md'])", "'work/root/staircase_five_report.md','work/root/even_increment_transport.md','work/root/five_row_interior_nonvanishing.md'])")
s=s.replace("'work/rectangular/canonical_below_square_families.md',", "'work/rectangular/canonical_below_square_families.md','work/rectangular/canonical_next_row_below_square.md',")
s=s.replace("'work/archive/GENERAL_TWO_ROW_SCHUR_COMPLEX.md'])", "'work/archive/GENERAL_TWO_ROW_SCHUR_COMPLEX.md','work/archive/TWO_ROW_POSITIVE_REVIEW.md','work/archive/STAIRCASE_PROOF_REVIEW.md'])")
s=s.replace("Remaining direct region: λ2+λ3>2n>λ3+λ4; evaluate its actual H1 correction and finite-group covariants.", "T045 also evaluates c=2k−1 for all valid shapes; T046 evaluates c=2k−2 for k≥5 through its actual line restriction. G023 evaluates every central staircase. Remaining direct region is the strict central cone after these removals; evaluate its remaining actual H1 corrections and finite-group covariants.")
needle="      ('Q-MAP','Sra III"
insert="      ('Q-NONVANISH5','G-024--G-025; exact flag multiplication','Classify nonvanishing for all outer-degree-five Schur labels','open with finite-width wall gate','G025 proves all seven multiplicities at least two whenever every consecutive gap is at least two. It also proves the actual symmetric canonical image is nonzero in every such degree, with full target rank at n≥5 and exact image rank1 at the sole n4 shape. Any remaining vanishing label has a gap zero or one; G021,T045,T046 and G023 further evaluate their stated subfamilies.'),\n"
assert needle in s;s=s.replace(needle,insert+needle)
s=s.replace("R-024 gives recursive second-row ranges from actual degree-five and square bases. The remaining critical annihilator", "R-024 gives recursive second-row ranges from actual degree-five and square bases; R025--R027 remove explicit multiplicity-one cofactor families throughout their below-square intervals, and G025 settles actual image nonvanishing for every five-row shape with all gaps at least two. The remaining critical annihilator")
# All executables are reproducible from the supplied source; avoid distributing ELF builds.
s=s.replace("if p.suffix=='' and p.name.startswith", "if p.suffix=='' and p.open('rb').read(4)==b'\\x7fELF':continue\n            if p.suffix=='' and p.name.startswith")
p.write_text(s)

p=ROOT/'work/root/five_row_interior_nonvanishing.md';s=p.read_text()
s=s.replace('7410\\pmod {1000003}.', '21,210,071,040\\quad\\text{over }\\mathbf Z,\\qquad\n7410\\pmod {1000003}.')
s=s.replace('The complete integer-modular computation is', 'The independent integer reconstruction gives the normalized value\n\\(115072/1125\\). It uses three-row cofactors and four-row Laplace\nexpansion in `work/archive/check_n4_polarization_integer.cpp`; the\nexplicit intermediate bound is below \\(2^{118}\\), so its signed\n128-bit arithmetic is exact. The receipt is\n`work/archive/N4_POLARIZATION_INTEGER_RECEIPT.json`.\nThe complete integer-modular computation is')
s=s.replace('The larger seed values in the\ntable are certified by the displayed exact determinant/Pieri\nalgorithm.', 'All76 seeds are additionally reconstructed independently by literal\nJacobi–Trudi determinants and two-cycle interpolation over the field\nwith61 elements, with the exact bounded-degree coefficient recovery\nrecorded in `work/archive/GAP2_SEEDS_INDEPENDENT_RECEIPT.json`.\nThe displayed determinant/Pieri algorithm and the final table certify\nevery seed value.')
p.write_text(s)

with (ROOT/'work/root/paper_front.md').open('a') as f:
 f.write('''
## Further completed ranges in this checkpoint interval

T-044 independently verifies every two-row quotient on the quadratic ray. T-045 evaluates all valid shapes one twist below it, including every first-power endpoint through the actual polarization right inverse. T-046 constructs the actual pair-line cohomology correction two twists below it for every point order at least five, then supplies55 active positive polytopes and complete support. These calculations evaluate further regions inside the strict central gate.

G-022 proves every outer Schur label occurs on an all-rank staircase family with an explicit uniform bound. G-023 evaluates the entire five-row staircase with seven active positive polytopes. G-024 supplies an explicit invariant sum-of-squares section whose multiplication injects every outer-label multiplicity into the corresponding even increment. G-025 uses76 fully computed minimal congruence seeds to prove that every five-row output with all four consecutive gaps at least two has every outer label with multiplicity at least two. Its actual canonical image is nonzero in every degree; the only degree-four shape has image multiplicity one and target multiplicity three, proved by a literal polarization value, and all degrees at least five have full target rank on this family. Thus the remaining nonvanishing question is confined to gaps zero or one.

R-027 extends the first-row r²+1 cofactor families down to the stated lower degrees below the square bound, including both endpoints through exact apolar evaluations. Its whole proof, like T-044--T-046 and G-024--G-025, has a separately recorded complete reading.
''')

dictionary='''
## Maps for the further central and nonvanishing families

**T-044--T-046.** The signed tensor/Young-idempotent construction gives the same actual ideal-tensored Schur complex of locally free sheaves. T-045 computes the first-power connecting map as one fifth of contraction and gives its explicit polarization right inverse. T-046 restricts point jets to the ten pair lines and identifies the full first-cohomology cokernel through those actual sheaf maps; the induced determinant line fixes its stabilizer character. Taking the derived direct image and its exact representation class is SGA6 VI3.3, transported by the SGA3 I4.5,4.7.2--4.7.3 frame torsor. Its explicit finite group character and positive polytopes evaluate the same cote133/024--029 composition as G-015.

**G-022--G-023.** The cycle endomorphism diag(t)g on the Schur bundle and its balanced coefficient extraction compute the literal finite-normalizer projector. The Weyl-determinant identity gives the exact cycle trace polytopes. The box injection, forest denominator proof and fixed positive Newton formulas are rank computations for that same SGA6 Schur operation, with the SGA3 frame maps specified in ST5--6 and SF3--7.

**G-024--G-025.** The flag-minor polynomial f_eta is an explicitly constructed invariant section. Multiplication by it, then by the indicated determinant section, is an injective map of actual balanced Schur components in a polynomial domain. Its cokernel gives an effective representation class in SGA6 VI3.3; no unidentified realization is used. IN17 is the exact inclusion--grid-permutation--projection pullback for multiplying linear forms. Its nonzero rational value and the precise CIM/McKay maps give a nonzero graded Chow coordinate-image section in EGA I9.5.2. These maps evaluate cote133/024--029 through A-010, with their integral polynomial expressions and stated characteristic-zero projectors.

**R-027.** The explicit cofactor sections, normalized last-slot inclusion and common-polarization coefficient map descend to the same coordinate-image scheme as R-025--R-026. The endpoint apolar chain rules and Vandermonde scalar identify the actual nonzero component, giving rank one in its EGA I9.5.2 graded image and its SGA6 VI3.3 representation class. The splitting-field evaluation uses an injective scalar-extension map, as recorded in the proof.
'''
with (ROOT/'work/root/geometric_dictionary.md').open('a') as f:f.write(dictionary)

with (ROOT/'work/root/remaining_gates.md').open('a') as f:
 f.write('''
## Strict reductions after the first formal review

The direct outer-five gate now excludes all c=2k−1 valid shapes (T045), all c=2k−2 shapes with k≥5 (T046), and the complete central staircase (G023), in addition to G021's outside regions. The remaining lower twists need their actual first-cohomology corrections evaluated; the small orders on c=2k−2 retain their stated exceptional scalar defects.

For nonvanishing, G025 removes every shape with all four consecutive gaps at least two, for every outer label, and proves actual symmetric canonical-image nonvanishing there. A remaining vanishing coefficient must have at least one gap zero or one. G024 gives the exact even-increment multiplication map and transports all completed seeds and staircase bounds. The full positive-formula problem still requires exact coefficients, beyond these proved lower bounds.

For varying-rank actual maps, R027 removes its first-row r²+1 families throughout the lower-degree intervals proved there. The remaining annihilator retains the exact support and maps in R023--R024 after those explicit components are removed.
''')

with (ROOT/'deliverables/LEDGER.md').open('a') as f:
 f.write('\n## Research update after review01 — '+stamp+'\n\n')
 f.write('T045 closes the full c2k−1 two-row family, and T046 evaluates the actual pair-line correction at c2k−2 for k≥5. G024 constructs the exact all-label even-increment embedding. G025 removes every five-row shape with all consecutive gaps≥2 from the nonvanishing gate, and settles actual symmetric canonical-image nonvanishing in every degree of that family. All76 seeds are independently reconstructed, with315 additional literal plethysm checks; the degree-four map is evaluated over the integers. R027 extends the first-row r²+1 actual-image families throughout its stated below-square degrees. These are main-gate reductions after review01. This entry is an ongoing update, not another scheduled review; next review remains03:01:08UTC.\n')
with (ROOT/'deliverables/IMPLICATIONS.md').open('a') as f:
 f.write('''
## Further explicit nonvanishing and actual image information

G025 proves that every outer-degree-five output shape with all four consecutive gaps at least two contains every outer label with multiplicity at least two. Its actual symmetric canonical image is nonzero in every degree: full target multiplicity at n≥5, and exact rank1 against target multiplicity3 at the sole n4 shape. This follows from the explicit flag-domain embeddings, the complete76-seed certificate, the established exact canonical kernels and a literal nonzero grid evaluation. Thus candidate vanishing components in outer degree five are confined to gaps zero or one. G024 provides the exact invariant multiplication map that carries the nonvanishing proof through even increments.

T045--T046 evaluate additional central coefficient families and their precise line-cohomology correction. R027 supplies additional rank-one actual image components below the general square bound. These results further evaluate the composition operations of cote133/024--029 and their SGA6 representation classes, through the specified SGA3 frame and EGA coordinate-image maps. They do not provide the missing uniform polynomial preprocessing bound for the general GCT positive-formula problem, and no complexity-class separation is asserted.
''')

eventpath=ROOT/'work/root/CHECK_EVENTS.tsv'
with eventpath.open(newline='') as f:r=csv.DictReader(f,delimiter='\t');fields=r.fieldnames;events=list(r)
checks=[
 ('T-044','targeted proof check','Read whole R1–R12 proof: exact relative flag pairing and sign, locally split ideal-tensored Schur complex, all cohomology endpoints, three-product trace, residue degree and finite-constant specification, support and literal lattice bijection; PASS. Full120960000-entry computation is attributed to its executor.'),
 ('T-045','targeted proof check','Read whole B1–B13 proof and all three parameter domains: scalar cohomology maps, exact1/5 contraction, marked-tensor polarization right inverse, invalid empty endpoint, hook kernel, shifted trace and positive-constant formulas, all support and degree bounds; PASS.'),
 ('T-046','targeted proof check','Read whole L1–L23 proof: actual point-to-line sheaf restrictions, complete overlap functionals, four explicit direction separators, both surjections, exact Cox target dimension including k5, complete Schur cokernel diagram, determinant sign, seven induced traces and all positive-formula/support bounds; PASS. Separate agents independently read the full proof.'),
 ('R-027','targeted proof check','Read whole NR1–NR26 proof: both multiplicity-one complements, exact lower annihilator inclusion, all interior coefficient inequalities, two explicit Vandermonde matrices, endpoint apolar substitutions and signs, complete factorial domination and r2/r3 endpoints; PASS. NR24 comma corrected as a typesetting fix.'),
 ('G-024','targeted proof check','Read whole EI1–EI5 proof after writing: deterministic balanced tableau, literal flag-minor degree, real Vandermonde nonzero evaluation, invariant sum of squares, injective equivariant multiplication, determinant twist, every parameter and exact geometric transport; PASS.'),
 ('G-025','targeted proof check','Read whole IN1–IN18 proof and76-row table after writing: minimal zero-sum reduction, integral partition transport, single-cycle and both two-cycle determinant signs, actual Pieri recursion, finite seed enumeration, exact normalized grid coefficient, source/target multiplicities, every degree and dimension endpoint, and exact Chow map; PASS. Independent all76-seed reconstruction and integer polarization are separately attributable.'),
 ('G-025','computation or formal certificate','Executed all76 seed computations from exact Pieri/cycle alternants: every one of532 coefficients≥2; max seed inner12. Checked n4 source1,target3 by literal MN; primality and denominator invertibility by exact integers. Executed all1048576 modular polarization evaluations: coefficient7410mod1000003. Complete scripts and receipts retained; PASS.'),
 ('G-021','targeted proof check','Archive full §8 review identified a row/column notation error in TR18; corrected X_{1i} to the invariant product X_{i1}. Rechecked against GF6/GF9 and the actual balanced chart. The map and theorem now have the exact saved convention; PASS.'),
 ('SRC-BCI-EVEN','used and rechecked in this run','Read primary author text: unnumbered Theorem§1.1 p1, Lemma2.1 p4, supporting tensor lemmas and full§3 pp7–8. Used the exact balanced-tableau existence and known even-partition statement; G024 proves its own specified flag-polynomial embedding. No original source computation was rerun.'),
]
for sid,typ,outcome in checks:
 row={k:'' for k in fields};row.update(statement_id=sid,date=stamp,who_model_effort_run='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01',type=typ,outcome=outcome);events.append(row)
with eventpath.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(events)
print(stamp,'integrated G024–G025,T044–T046,R027; nine exact root events')
