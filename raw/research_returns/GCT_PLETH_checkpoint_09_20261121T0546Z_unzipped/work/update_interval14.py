from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv

stamp=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()
p=Path('work/build_package.py');s=p.read_text()
assert "'work/rectangular/tail_moment_canonical_range.md'" not in s
s=s.replace("'work/rectangular/double_four_tail_canonical_block.md'","'work/rectangular/double_four_tail_canonical_block.md','work/rectangular/tail_moment_canonical_range.md'")
s=s.replace("'work/archive/FIVE_POINT_POWERS.md'","'work/archive/FIVE_POINT_POWERS.md','work/archive/ALL_HOOK_CYCLE_MODULES.md'")
s=s.replace("'work/archive/FIRST_HOOK_KERNEL_REVIEW.md'","'work/archive/FIRST_HOOK_KERNEL_REVIEW.md','work/archive/TAIL_MOMENT_CANONICAL_RANGE_REVIEW.md'")
s=s.replace("      ('Q-MAP-SINGLE4'","      ('Q-MAP-TAIL-MOMENTS','R-046 TM1–22; Sarkar Theorem D/6.4 for the coefficient threshold','Prove actual canonical surjectivity at the tail moment threshold','proved','For a,n≥2 and λ⊢an, put ν=(λ2,...),D=|ν|,t=ν1. The actual h_(n,a) is surjective on the full λ-isotypic component for D+t≤2n+1. Independent-row polarization, triangular Möbius moment substitution and finite centered evaluation factor the actual transpose with scalar1. This proves every even-tail component in full multiplicity at n≥|ρ|+ρ1 and every λ2≤b band at n≥floor(ab/2).'),\n      ('Q-MAP-SINGLE4'")
s=s.replace('R038 refines the already known binary isomorphism','R046 proves full isotypic surjectivity for tail size D and width t with D+t≤2n+1, through an injective exact moment factorization; the remaining gate excludes this entire range. R038 refines the already known binary isomorphism')
p.write_text(s)

note=r'''## Exact canonical moment range and all hook modules

R046 proves actual full isotypic surjectivity of \(h_{n,a}\) for every \(a,n\ge2\) and \(\lambda\vdash an\) with tail \(\nu=(\lambda_2,\ldots)\), size \(D\), and width \(t\) satisfying \(D+t\le2n+1\). The normalized factorization is independent-row polarization, an invertible split-moment substitution, and finite centered power-sum evaluation. Exterior row occupancy and zero-padding transpose prove faithfulness of that exact evaluation map. The coefficient stability threshold is credited to Sarkar Theorem D/6.4; the conclusion here is proved for the specified canonical map. Every even-tail family \(2\rho\) therefore has full target multiplicity at \(n\ge|\rho|+\rho_1\), and every second-row-at-most-\(b\) component is reached at \(n\ge\lfloor ab/2\rfloor\). The proof has complete root and independent archive readings, with276 finite coefficient comparisons and independently checked split-moment normalizations.

A088 gives the actual invariant-base modules for every G037 hook cycle. Every nontrivial effective Specht multiplicity module is graded free over \(I=\mathbb Q[e_2,\ldots,e_m]\); explicit lifts by the Euler homotopy, extended on a homogeneous basis, split each actual differential. For the trivial label the weighted Koszul presentation gives the exact minimum generator number and generic rank, proves the stated failure of local freeness at the invariant origin in every lower hook degree, and gives an explicit exterior basis away from the origin. The top hook cycle is free of rank one. Both full proofs and exact source maps are retained.
'''
for name in ('deliverables/IMPLICATIONS.md','deliverables/LEDGER.md'):
 p=Path(name);p.write_text(p.read_text()+'\n\n'+('## Research update — '+stamp+'\n\n' if 'LEDGER' in name else '')+note)
p=Path('work/root/remaining_gates.md');s=p.read_text()
s=s.replace('Higher repeated-four tails and the general finite-row moment factorization remain active work.','R046 proves the exact finite-row moment factorization and full isotypic surjectivity whenever tail size D plus tail width t is at most2n+1. It upgrades all even-tail preimages to full multiplicity at the same bound, and proves every second-row≤b band at n≥floor(ab/2). Higher repeated-four tails below this moment bound remain active work.')
s=s.replace('The current remaining task is a uniform bound or further exact evaluation for varying shapes beyond these hook tails.','A088 extends the actual invariant-base module result to all hook degrees, including the exact trivial Koszul presentation and its locus of local freeness. The current remaining task is a uniform bound or further exact evaluation for varying shapes beyond these stable hook tails and for unstable hook charts.')
p.write_text(s)
p=Path('work/root/paper_front.md');s=p.read_text().replace('with explicit matrices and finite endpoints.','with explicit matrices and finite endpoints. R046 proves actual full isotypic surjectivity whenever tail size plus tail width is at most2n+1, by the exact normalized moment factorization.')
p.write_text(s)
p=Path('work/root/geometric_dictionary.md');p.write_text(p.read_text()+r'''

## All hook modules and faithful finite moments

**A088.** The actual homogeneous Koszul maps over
\(\operatorname{Spec}\mathbb Q[e_2,\ldots,e_m]\) define coherent
cycle sheaves. The basis lifts and graded splitting in §1 give
their free nontrivial Specht sheaves. The trivial component's
weighted Koszul presentation gives the exact Fitting-rank test
at the invariant origin and the exhibited local frame on each
\(D(e_i)\); its top cycle has the displayed global generator.
The comparison uses the actual differential-form map of Solomon,
the associated-bundle maps of SGA3 I4.5/4.7.2–4.7.3,
EGA II2.4.1–2.4.2 and2.5.2/2.5.4, and Schur operations
in SGA6 VI3.3 and V4.2,4.4,4.8–4.9. Archive cote133/028
is transported by A012's explicit tensor-word and Young maps.

**R046.** TM4–22 are morphisms of rational coordinate algebras
and their associated coherent isotypic sheaves. The Chow
pullback and normalized grid pairing of R037 EP3–5 identify
the composite with the actual canonical map. Centered row
projection, zero-padding transpose and the displayed Möbius
automorphism give the specified injective morphisms, so the
scheme-theoretic image has the asserted whole component.
Use EGA I9.5.2 for that image, SGA3 I4.5/4.7.2–4.7.3
for frame descent, and SGA6 VI3.3 and V4.2,4.4,4.8–4.9
for the exact Schur and Grothendieck-group operations. The
integral lattice has the displayed finite factorial and row
denominators inverted; the theorem itself is in characteristic
zero, without an unproved integral rank assertion.
''')
p=Path('work/root/CHECK_EVENTS.tsv');fields=next(csv.reader(p.open(newline=''),delimiter='\t'))
events=[('R-046','targeted proof check','Read the entire TM1–22 proof and all eight sections. Checked dehomogenization, Young row-degree bound, exterior occupancy GL character stability, the scalar-one zero-padding map and moment faithfulness, injective independent-row evaluation, full Möbius triangular inverse, literal normalized canonical factorization, transpose and every stated range. PASS.'),('A-088','targeted proof check','Read the complete four-section proof. Checked actual homogeneous coinvariant section, basis-wise Euler lifts and I-linear extension, projective/free argument via graded Nakayama, exact weighted Koszul presentation, minimal generators versus generic rank, top-cycle generator and every localized exterior basis. PASS.'),('SRC-SARKAR-R046','used and rechecked in this run','Read retained primary main.tex Theorem D/6.4 and its full §6 proof, including the exterior occupied-row threshold and centered standard representation passage. Exact coefficient threshold is credited; R046 separately proves the actual canonical factorization.')]
with p.open('a',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t')
 for sid,kind,outcome in events:w.writerow(dict(statement_id=sid,date=stamp,who_model_effort_run='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01',type=kind,outcome=outcome))

# Break the three-stage map vertically without altering any factor.
p=Path('work/rectangular/tail_moment_canonical_range.md');s=p.read_text()
s=s.replace(r'\boxed{\text{independent-row polarization}\quad'+ '\n'+r' \longrightarrow\quad'+ '\n'+r' \text{invertible split-moment substitution}\quad'+ '\n'+r' \longrightarrow\quad'+ '\n'+r' \text{finite centered power-sum evaluation}.}',r'\boxed{\begin{gathered}\text{independent-row polarization}\\'+ '\n'+r' \longrightarrow\ \text{invertible split-moment substitution}\\'+ '\n'+r' \longrightarrow\ \text{finite centered power-sum evaluation}\end{gathered}}')
p.write_text(s)
print(stamp,'integrated R046 and A088, with A089 audit')
