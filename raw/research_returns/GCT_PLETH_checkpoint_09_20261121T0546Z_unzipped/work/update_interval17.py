from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv
stamp=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()
p=Path('work/build_package.py');s=p.read_text()
assert "'work/root/fixed_second_part_report.md'" not in s
s=s.replace("'work/root/stable_third_row_report.md'", "'work/root/stable_third_row_report.md','work/root/fixed_second_part_report.md'")
s=s.replace("'work/archive/FIXED_ORDER_HOOK_REVIEW.md'", "'work/archive/FIXED_ORDER_HOOK_REVIEW.md','work/archive/FIXED_SECOND_PART_REVIEW.md'")
row=('Q-STABLE-FIXED-SECOND-PART','G-040 FS1–18; A097 independent review','Give a positive polynomial construction for every fixed second part of a stable two-row tail','proved for every fixed b with the stated encoding','For every b≥2, all m≥3,a≥b,t≥0,n≥a+t and every outer label, the positive bounded-polytopes construction has at most3m+2b variables and construction/value/support complexity f(b)(m+binary input lengths+1)^g(b). The actual transfer has a finite cokernel in degrees b−1 through2b−2; all invariants e_i with i≥b kill it, leaving at most b−2 low variables. Actual minimal-cover cancellations, the high-variable multidegree inverse, fixed-variable Gröbner bounds and triangular monomial lifts prove the formula. The general finite algorithm is fully specified and checked; executable closed formulas and computation receipts currently cover b2/3. No polynomial complexity is claimed for unrestricted varying b.')
anchor="      ('Q-STABLE-SECOND-PART2'"
assert anchor in s;s=s.replace(anchor,'      '+repr(row)+',\n'+anchor)
s=s.replace('stable two-row tails with second part2/3 G038–G039,','stable two-row tails with every fixed second part G040 (small closed formulas G038–G039),')
p.write_text(s)

note=r'''## Every fixed second part of a stable two-row tail

G040 is now proved and independently checked in full. For every fixed b≥2 it gives the entire stable family
\[
\lambda=(mn-a-b-(m-1)t,a+t,b+t,t^{m-3}),
\quad m\ge3,\ a\ge b,\ t\ge0,\ n\ge a+t,
\]
with every outer label. Its positive bounded polytopes use at most3m+2b variables. Construction, coefficient evaluation and support decision have the explicit type of bound f(b)(m+binary parameter lengths+1)^g(b). This statement retains its dependence on b and the explicit-m encoding convention at t0.

The actual derivative transfer has finite cokernel supported from b−1 to2b−2. Therefore e_i kills it for every i≥b; the residual low ring has at most b−2 variables. The two minimal-cover cancellations and the explicit inverse in each high-variable multidegree give the precise free, low-kernel and weighted-cycle decomposition. Aschenbrenner Theorem3.2 and Liang Corollary42 bound the remaining kernel calculation by a polynomial for fixed b. The finite nullspace algorithm recovers the full reduced Gröbner basis, and each retained initial monomial has a specified triangular lift to an actual kernel vector. Distinct-shape LR restriction/induction computes the free input characters without duplicating corner-removal orders. Rational-series extraction gives binary-degree values and support.

Root read the entire proof, and A097 independently checked all eight sections, the primary degree bounds and exact bit-size argument. The final tightening to b−2 low variables includes the empty low ring at b2. The general algorithm is specified mathematically; no generic execution is claimed. G038/G039 retain their executed closed formulas and independent receipts. This removes every fixed-second-part stable two-row family from the remaining positive-description gate, while the unrestricted dependence on b and general varying shapes remains active.
'''
for filename in ('deliverables/LEDGER.md','deliverables/IMPLICATIONS.md'):
 p=Path(filename);p.write_text(p.read_text()+'\n\n'+('## Research update — '+stamp+'\n\n' if 'LEDGER' in filename else '')+note)
p=Path('work/root/remaining_gates.md');s=p.read_text()
s=s.replace('G040 proposes a complete fixed-second-part construction through finite cokernels and bounded fixed-variable Gröbner calculations; its independent whole-proof review is in progress, so it is not counted here as completed.','G040 completes every stable two-row tail with fixed second part b, through its finite actual cokernel, at most b−2 low invariant variables, exact minimal covers, high-variable inverse and bounded Gröbner basis. Its construction, value and support bounds are f(b)(m+binary lengths+1)^g(b), with at most3m+2b variables. Root and A097 whole-proof checks pass. The unrestricted dependence on b and the remaining general varying shapes remain active; generic execution of G040 is separate from its completed proof.')
p.write_text(s)
p=Path('work/root/paper_front.md');s=p.read_text()
s=s.replace('and three by explicit small positive formulas. T064–T065 complete','and three by explicit small positive formulas. G040 gives a positive\npolynomial construction for every fixed second part b, with all\nactual maps and the precise dependence on b. T064–T065 complete')
s=s.replace('| Fixed-order unstable hooks, a≥2k |','| Every fixed second part b of a stable two-row tail | G040: polynomially many pieces for fixed b, at most3m+2b variables | Complete declared family; exact fixed-b construction, values and support |\n| Fixed-order unstable hooks, a≥2k |')
p.write_text(s)
p=Path('work/root/geometric_dictionary.md')
p.write_text(p.read_text()+r'''

## Every fixed second part through a finite coherent cokernel

**G040.** FS3 is the actual derivative transfer of polynomial
bundles. Its finite coherent cokernel has support in degrees
b−1 through2b−2 and is annihilated by e_i for i≥b. The exact
covariant module therefore descends to the low affine base
\(\operatorname{Spec}\mathbb Q[e_2,\ldots,e_{\min(m,b-1)}]\).
The specified minimal homogeneous covers and invertible triangular
basis changes split off the free summand of the original transfer
kernel. FS13 is a literal inverse in each high-variable multidegree.
The leading-term filtration on the residual low-variable kernel,
with its displayed triangular lifts, carries every retained lattice
point to a vector in the same coherent kernel. Thus the finite
positive description is transported to the original balanced flag
and its determinant line, rather than inferred from an unrelated
character equality. The precise module/sheaf and projective
locators are EGA II2.4.1–2.4.2 and2.5.2/2.5.4; the frame maps
are SGA3 I4.5/4.7.2–4.7.3; the representation-K0 and Schur
operations are SGA6 VI3.3 and V4.2,4.4,4.8–4.9. The archive
transport is A012's integral tensor-word/Young comparison for
cote133/028. The rational maps retain the stated characteristic-zero
base and explicit-m input convention.
''')
p=Path('work/root/CHECK_EVENTS.tsv');fields=next(csv.reader(p.open(newline=''),delimiter='\t'))
with p.open('a',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t')
 w.writerow(dict(statement_id='G-040',date=stamp,who_model_effort_run='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01',type='targeted proof check',outcome='Fresh whole-proof reading of FS1–18 and every section, after author construction. Verified actual transfer/cokernel, near-row Specht construction and matrix heights, both minimal covers and free cancellations, every high-variable inverse and endpoint, ordinary-degree kernel/GB bounds with retained weighted shifts, finite-nullspace recovery, initial-kernel grid basis, corrected distinct-shape LR products, exact value/support and encoding bounds. Tightened low ring to B=min(m,b−1), ℓ≤b−2 with explicit b2 empty-ring case, independently confirmed by archive auditor. Read the full A097 independent audit. PASS; general-purpose execution is not claimed.'))
print(stamp,'integrated G040 after whole-proof and independent checks')
