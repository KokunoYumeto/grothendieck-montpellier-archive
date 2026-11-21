from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv,shutil

now=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()
p=Path('work/build_package.py');s=p.read_text()
assert "'work/root/stable_hook_report.md'" not in s
s=s.replace("'work/theta/charged_incidence_rees_report.md'","'work/theta/charged_incidence_rees_report.md','work/theta/varying_hook/first_hook_report.md','work/root/stable_hook_report.md'")
s=s.replace("'work/rectangular/single_four_tail_canonical_band.md'","'work/rectangular/single_four_tail_canonical_band.md','work/rectangular/double_four_tail_canonical_block.md'")
s=s.replace("'work/theta/outer5/variable_wall/G036_REVIEW.md'","'work/theta/outer5/variable_wall/G036_REVIEW.md','work/archive/NORMALIZED_BELOW_REVIEW.md','work/archive/GENERIC_HIGH_TWIST_REVIEW.md','work/archive/COMPLETE_OUTER_FIVE_REVIEW.md','work/archive/FOUR_EVEN_TAIL_SMALL_DEGREE_REVIEW.md','work/archive/FOUR_THREE_EVEN_TAIL_BLOCK_REVIEW.md','work/archive/SINGLE_FOUR_TAIL_BAND_REVIEW.md','work/archive/DOUBLE_FOUR_TAIL_BLOCK_REVIEW.md','work/theta/varying_hook/G037_REVIEW.md'")
s=s.replace("      ('Q-OUTER4'","      ('Q-STABLE-HOOKS','G-037 HK1–19; T-060 FH1–18; T-032 C4–8','Give a uniform positive formula and support for stable hook tails with varying outer degree and hook length','proved in the stated explicit encoding','Every λ=(mn−a−(m−1)t−r,a+t,(t+1)^r,t^(m−2−r)),m≥3,a≥1,0≤r≤m−2,t≥0,n≥a+t has one explicit bounded polytope with at most m²+3m−4 variables, a complete support test and polynomial-bit exact evaluation in m and the binary parameters. For t≥1 the ordinary binary-part list has m positive entries, giving a genuine polynomial-size #P verifier in that encoding. The exact Koszul differential, super-principal cell cancellation and invariant-form monomial basis supply the comparisons. The t0 compressed-encoding caveat is retained.'),\n      ('Q-OUTER4'")
s=s.replace('R038 refines the already known binary isomorphism','R045 determines the repeated-four block(an−8,4,4), including its four-by-four normalized matrix, rank min(4,a−2,n−2) for a≥3,n≥4, exact finite relations and all cubic/quadratic endpoints. R038 refines the already known binary isomorphism')
p.write_text(s)

note=r'''## Varying-degree hook formulas and the first repeated-four matrix

G037 treats every stable hook tail with varying outer degree, hook length and outer Schur label. For
\[
\lambda=(mn-a-(m-1)t-r,a+t,(t+1)^r,t^{m-2-r}),
\quad m\ge3,\ a\ge1,\ 0\le r\le m-2,\ n\ge a+t,
\]
there is one explicitly constructed bounded polytope with at most \(m^2+3m-4\) variables, a complete support test, and a coefficient evaluator of polynomial bit complexity in \(m\) and the binary parameters. For \(t\ge1\), the output has \(m\) positive parts, so this is also a polynomial-size #P description in ordinary explicitly listed binary-part encoding. The \(t=0\) compressed-input caveat is stated explicitly. The exact balanced flag map, hook Young projector, Euler/Koszul homotopy, two specified cell factors, and invariant differential-form basis carry the proof to the original plethysm. The actual computations passed4872 Schur/cycle coefficients and support tests,238 original plethysms and569 literal witnesses in520 polytope cases. T060 separately supplies the first-hook multiplicity modules: every nontrivial effective Specht component is graded free over the stated invariant algebra, while the trivial component has the exact positive monomial-cycle presentation and a proved m4 obstruction to that same freeness.

R045 completes the family \(\lambda=(an-8,4,4)\). For \(a\ge3,n\ge4\), target multiplicity is \(\min(4,a-2)\) and actual image is \(\min(4,a-2,n-2)\). The full four-by-four matrix, both determinants, every smaller finite relation and endpoint minor, and the actual rational preimages are specified. At inner degree three, the target has one or two copies and the actual image is exactly one; at inner degree two, target one and image zero. The independent-row evaluation map and its exact row-degree filtration justify every small-degree extension. Both root and archive whole-proof readings passed, and the archive independently reconstructed all sixteen universal moment entries and every residual polynomial.
'''
for name in ('deliverables/IMPLICATIONS.md','deliverables/LEDGER.md'):
 p=Path(name);p.write_text(p.read_text()+'\n\n'+('## Research update — '+now+'\n\n' if 'LEDGER' in name else '')+note)

p=Path('work/root/remaining_gates.md');s=p.read_text()
s=s.replace('The current task is a uniform bound or a further exact evaluation of those projectors as the outer degree varies.','G037 now evaluates every stable hook tail through an exact Koszul complex: a single polynomial-size polytope, exact support and binary-degree evaluation are proved with varying m and hook length, with the explicit input-encoding scope retained. T060 gives the corresponding first-hook free modules and the exact trivial cycle obstruction. The current remaining task is a uniform bound or further exact evaluation for varying shapes beyond these hook tails.')
s=s.replace('Repeated-four tails remain active work.','R045 completes the repeated-four tail(4,4), including the four-dimensional block and all smaller inner-degree endpoints. Higher repeated-four tails and the general finite-row moment factorization remain active work.')
p.write_text(s)

p=Path('work/root/geometric_dictionary.md');p.write_text(p.read_text()+r'''

## Varying hook kernels and the repeated-four matrix

**T-060 and G-037.** The stable flag algebra map T032/C4–8 and
determinant volume pairing identify the given Schur class with the
actual hook module on the sum-zero permutation representation.
The hook Young inclusion is the kernel of HK5, and the explicit
Euler/exterior derivative homotopy proves the exact complex.
Macdonald's virtual principal specialization computes the traces
of this same module; deleting cells(1,1),(2,1) gives the exact
positive numerator. Solomon's differential map, scaled by1/j,
identifies the invariant complex with the weighted Koszul complex
on e2,...,em. HK14 is an actual polynomial basis of its cycles.
The two integer-matrix bijections count precisely the resulting
tableau/subset and monomial-cycle labels. These coherent kernels,
frame torsors, associated bundles and Schur operations use EGA
II2.4.1–2.4.2,2.5.2/2.5.4; SGA3 I4.5/4.7.2–4.7.3;
SGA6 VI3.3 and V4.2,4.4,4.8–4.9. Cote133/028 is carried
by A012's actual tensor-word, weight and Young maps.

**R-045.** Diagonal evaluation of row-symmetric polynomial tensors
and rational polarization give the injective moment morphism DF7.
Translation of the actual functional proves the exact filtration
identity DF9. The four bracket polynomials have the full normalized
map DF20 and cubic map DF27; their determinants, finite relations
and endpoint minors supply actual preimages and image ranks.
The coordinate-ring morphism is R037 EP3–5, with EGA I9.5.2
scheme-theoretic image. The same finite matrices give the associated
bundle map on the SGA3 frame torsor and its SGA6 VI3.3 class.
The Schur-operation and cote133/028 comparisons are the same actual
Young/tensor maps used throughout the rank calculations.
''')

p=Path('work/root/CHECK_EVENTS.tsv');fields=next(csv.reader(p.open(newline=''),delimiter='\t'))
who='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01'
events=[
('T-060','targeted proof check','Read complete FH1–18 and all seven sections. Checked exact stable chart/sign, hook multiplication kernel/projector, I-linear section and graded projective/free argument, super-principal cancellation, trivial invariant-form/star basis, negative m4 numerator obstruction, complete support threshold, every polytope and bit/encoding bound. PASS.'),
('R-045','targeted proof check','Read complete DF1–28 and all seven sections. Checked bracket highest/row-degree maps, four invariant branches, injective diagonal expectation and exact degree filtration, full equality-partition certificate specification, all matrix factors/determinants, finite relations/rank minors, inverse order, cubic extension/scalars and quadratic LDL/polarization endpoint. PASS.'),
('G-037','computation or formal certificate','Executed check_stable_hook_positive.py:4872 direct hook-Schur/cycle character coefficients and4872 support tests for m3..8,a1..14,all hook lengths and labels;238 original power-sum/MN plethysms with t0/1;520 literal polytope cases569witnesses. Exact large a10^12 evaluation separately exercised and attributed as evaluator output. STABLE_HOOK_POSITIVE_RECEIPT.json PASS.'),
('SRC-MACDONALD-HOOK','used and rechecked in this run','Read local Macdonald second edition I§3 Examples2–3 printedp45, including complete interpolation proof and exact virtual principal specialization. Applied only with the displayed power sums and z=-u; source work/archive/Macdonald.txt and primary Berkeley PDF.'),
('SRC-SOLOMON-FORMS','used and rechecked in this run','Opened publisher original Invariants of finite reflection groups, Nagoya22(1963), read §3 unnumbered Theorem p59 and proof pp59–61; verified its differential-form map and specialized Euler contraction after division by j. DOI10.1017/S0027763000011028.'),
('SRC-BOSTAN-MORI','used and rechecked in this run','Opened author BoMo21.pdf and read §2.1 proof of Theorem1 and Algorithm1, PDFpp4–5/printedpp121–122. Verified the parity coefficient map used in G037/T060; G037 explicitly proves the same identity also for its possibly improper finite numerator and the roots-of-unity bit bound.'),
]
with p.open('a',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t')
 for sid,kind,outcome in events:w.writerow({key:{'statement_id':sid,'date':now,'who_model_effort_run':who,'type':kind,'outcome':outcome}.get(key,'') for key in fields})
print(now,'integrated T060/G037/R045 and complete audit reports')

