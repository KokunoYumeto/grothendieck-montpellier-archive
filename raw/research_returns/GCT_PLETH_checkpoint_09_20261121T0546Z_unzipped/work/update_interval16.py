from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv

stamp=datetime.now(ZoneInfo('Europe/Berlin')).isoformat()
p=Path('work/build_package.py');s=p.read_text()
new_formula=[
 'work/root/stable_second_row_report.md',
 'work/root/stable_third_row_report.md',
 'work/theta/unstable_hook/higher_hook_jets_report.md',
 'work/theta/unstable_hook/fixed_order_hook_report.md',
 'work/theta/unstable_hook/hook_endpoint_report.md',
]
new_rank=[
 'work/rectangular/repeated_four_mixed_tail_profile.md',
 'work/rectangular/one_row_improved_canonical_range.md',
 'work/rectangular/odd_part_occupancy_canonical_range.md',
]
new_audit=[
 'work/archive/FIRST_UNSTABLE_HOOK_REVIEW.md',
 'work/archive/REPEATED_FOUR_MIXED_PROFILE_REVIEW.md',
 'work/archive/STABLE_SECOND_ROW_REVIEW.md',
 'work/archive/HIGHER_HOOK_JETS_REVIEW.md',
 'work/archive/ONE_ROW_IMPROVED_RANGE_REVIEW.md',
 'work/archive/STABLE_THIRD_ROW_REVIEW.md',
 'work/archive/FIXED_ORDER_HOOK_REVIEW.md',
 'work/rectangular/sixth_power_source_scope_audit.md',
]
for f in new_formula+new_rank+new_audit:
 assert Path(f).exists(),f
 assert repr(f) not in s,f
s=s.replace("'work/theta/unstable_hook/first_unstable_hook_report.md'", "'work/theta/unstable_hook/first_unstable_hook_report.md',"+','.join(map(repr,new_formula)))
s=s.replace("'work/root/current_ranges.md'",','.join(map(repr,new_rank))+",'work/root/current_ranges.md'")
s=s.replace("'work/archive/TAIL_MOMENT_CANONICAL_RANGE_REVIEW.md'", "'work/archive/TAIL_MOMENT_CANONICAL_RANGE_REVIEW.md',"+','.join(map(repr,new_audit)))
rows=[
 ('Q-STABLE-SECOND-PART2','G-038 SR2.1–17; T032 C4–8','Give a positive formula for every stable tail (a,2) with varying outer degree','proved in the stated explicit encoding','For m≥3,a≥2,t≥0,n≥a+t and every outer label, the actual quadratic transfer kernel yields at most binom(m,2)+4 bounded polytopes with at most3m−3 variables. Exact coefficient and support algorithms have polynomial bit complexity in m and the binary parameters. Actual free cover cancellation and the two explicit Koszul exceptions prove positivity; all source comparisons and executed receipts are retained.'),
 ('Q-STABLE-SECOND-PART3','G-039 SR3.1–23; T032 C4–8','Give a positive formula for every stable tail (a,3) with varying outer degree','proved in the stated explicit encoding','For m≥3,a≥3,t≥0,n≥a+t and every outer label, the cubic transfer kernel yields at most binom(m,2)+7 bounded polytopes with at most3m−1 variables. The actual curvature quotient and Ricci splitting identify the finite invariant-base cokernel, whose minimal covers give a nonnegative free remainder and explicit ordinary/modified Koszul cycles. Degree evaluation and support are polynomial in m and binary parameter lengths.'),
 ('Q-HOOK-JET-RIGHT-INVERSE','T-062 HJ1–10; T-065 HE4–7','Construct actual higher-order hook jet splittings','proved','The explicit quadratic frame jets and horizontal contraction construct an equivariant right inverse for all a≥2k+1. The verified Segre regularity bound and rational Gram right inverse close every valid endpoint a=2k, with m4 and k1 handled by their exact direct maps. The flag ideal kernel and determinant twist give the identical plethysm multiplicity.'),
 ('Q-FIXED-ORDER-HOOKS','T-063 HJ11–16; T-064 FK1–15; T-065 HE1–7','Evaluate all valid hook parameters with a≥2k by positive polytopes','proved with the stated fixed-order and encoding bounds','For every k≥1,m≥4,a≥2k,t≥0,0≤r≤m−2 with (m−2)a≥mk+r, the stated unstable hook coefficient equals the stable G037 value minus the explicit nonnegative jet correction. D_k=Σ_p S(k−1,p)2^p(p+1)! bounds the correction. At most1+D_k(2(m²+3m−4)−1) disjoint bounded polytopes suffice, with m²+3m−4 variables each. Construction is f(k)(m+k+1)^(2k+O(1)) times a polynomial in binary lengths; coefficient and support evaluation have the stronger f(k)poly(m+binary lengths) bound. No unrestricted polynomial bound in varying k is asserted. The remaining hook range is a<2k.'),
 ('Q-MAP-REPEATED4-MIXED','R-047 RF1–20','Determine finite multiplicities and actual ranks for tails (4^h,3,2^j,1)','proved in the stated ranges','For h≥1,j≥0 put K=2h+j+3 and r_s=min(h,max(0,s−h−j−3)). Target multiplicity is r_a for a≥2,n≥4. For a,n≥4 with max(a,n)≥K, actual image multiplicity is min(r_a,r_n); n≥K gives the full target for every a≥2. Complementary-column and faithful moment maps supply each finite comparison.'),
 ('Q-MAP-ODD-OCCUPANCY','R-048 OI1–21; R-049 OO1–25','Sharpen full canonical surjectivity using the tail odd-part count','proved','For a,n≥2 and a valid nonempty tail ν of size D and width t≥2, let o be its number of odd parts, ε=t mod2, q=ceil((o−ε)/3), and M=floor((D+t−q)/2). The actual h_(n,a) reaches its entire target isotypic component at n≥M; both directions are isomorphisms at a,n≥M. The averaged extra-row morphism is literally id⊗q in the centered splitting, giving the exact kernel injection. Alternating highest weights, the finite-row character, faithful evaluation and normalized polarization prove the rank. The Euler-form hook family gives positive examples with unbounded improvement in the row threshold.'),
]
anchor="      ('Q-FIRST-UNSTABLE-HOOKS'"
assert anchor in s
s=s.replace(anchor,''.join('      '+repr(r)+',\n' for r in rows)+anchor)
s=s.replace("'G-009--G-011 give terminating positive formulas; no polynomial input-size bound for Hilbert bases, Reynolds lists, or elimination.'", "'G009–G011 give terminating positive formulas. Complete outer degrees3–5, stable hooks G037, stable two-row tails with second part2/3 G038–G039, and fixed-order hook charts a≥2k T064–T065 have explicit proved bounds. The remaining general varying-shape Hilbert bases, invariant lists and elimination data have no unrestricted polynomial input-size bound proved here.'")
s=s.replace('the remaining gate excludes this entire range. R038', 'the remaining gate excludes this entire range. R047 gives the finite repeated-four mixed profile and exact ranks with one dimension at its threshold. R048 and R049 replace the uniform tail threshold by M=floor((D+t−ceil((o−(t mod2))/3))/2), using the actual averaged row map, and give explicit positive ranks with unbounded row improvement. The remaining map gate excludes all of these full-isotypic ranges. R038')
p.write_text(s)

note=r'''## Stable two-row kernels, every fixed hook order, and sharper actual ranks

G038 completes every stable tail \((a,2)\), with varying outer degree and outer label: at most \(\binom m2+4\) bounded polytopes in at most \(3m-3\) variables. G039 completes every stable tail \((a,3)\), with at most \(\binom m2+7\) bounded polytopes in at most \(3m-1\) variables. Both supply polynomial-bit exact coefficient and support algorithms. The actual quadratic/cubic transfer kernels, finite cokernel modules, explicit cover cancellations and weighted cycle bases carry the positive counts to the original flag multiplicities. G039 includes the rational curvature quotient and Ricci inverse; every small-rank endpoint is treated. The ordinary binary-part encoding at positive determinant twist and explicit-m convention at zero twist remain stated. Root whole-proof/code readings pass, and A092/A095 give independent whole-proof checks and separate computations.

T062 constructs the higher-order jet right inverse. T063 gives the small correction for order two; T064 gives every order k with a≥2k+1 through actual monomial-orbit/exterior induction and bounded LR tableaux. T065 closes every valid a=2k endpoint using Nagel–Trok Theorem5.3 p233 and Lemma3.1 p225, with direct m4/k1 endpoint maps. The correction is at most D_k=Σ_p S(k−1,p)2^p(p+1)!, and the stable polytope has a fully specified finite list of points deleted by disjoint first-difference cells. Construction is polynomial for each fixed k, with the stronger stated fixed-parameter bound for exact values and support. The remaining unstable hook range is a<2k. Root whole-proof/code readings pass; A093 and A096 separately audit the higher jets and fixed-order positive construction. Endpoint and later boundary reviews retain their own status events.

R047 proves the entire finite multiplicity profile for tails (4^h,3,2^j,1), and exact actual canonical ranks when at least one dimension reaches K=2h+j+3. R048 proves the one-row improvement through explicit Pfaffian elimination. R049 sharpens the threshold for every tail: with size D, width t and o odd parts, set q=ceil((o−(t mod2))/3) and M=floor((D+t−q)/2). The normalized canonical map reaches its full target at n≥M. The literal averaged-extra-row morphism supplies id⊗q and its kernel injection, so the occupancy character calculation applies to the actual centered map. The Euler-contracted power-sum form has a fully evaluated Vandermonde scalar; its hook families give positive full-image examples with arbitrarily many additional rows below the preceding threshold. Root whole-proof readings pass; A091/A094 independently review R047/R048. R049's numerical character and scalar receipts remain distinct from its actual-map proof.

These completed ranges reduce the main coefficient and canonical-rank gates. They retain the finite Specht projector, determinant parity, all declared physical partition inequalities and exact geometric maps. They supply no separation of P and NP. The separate sixth-power source audit checks the current primary manuscript and certificate metadata; it adds no new canonical-map range and is not counted as movement. G040's general fixed-second-part construction is undergoing independent review and is tracked separately until that reading concludes.
'''
for filename in ('deliverables/LEDGER.md','deliverables/IMPLICATIONS.md'):
 p=Path(filename)
 p.write_text(p.read_text()+'\n\n'+('## Research update — '+stamp+'\n\n' if 'LEDGER' in filename else '')+note)

p=Path('work/root/paper_front.md');s=p.read_text()
s=s.replace('The canonical-map results include every target-outer-five rank,','G038 and G039 complete stable two-row tails with second part two\nand three by explicit small positive formulas. T064–T065 complete\nthe fixed-order unstable hook chart throughout every valid a≥2k.\nThe canonical-map results include every target-outer-five rank,')
s=s.replace('by the exact normalized moment factorization.','by the exact normalized moment factorization. R049 sharpens its row\nthreshold using the number of odd tail parts and proves positive\nfamilies with unbounded improvement. R047 gives the complete finite\nmixed repeated-four multiplicity profile and its stated actual ranks.',1)
s=s.replace('| Equal-middle and bounded-width families |', '| Stable two-row tails (a,2) and (a,3) | G038–G039: at most binom(m,2)+4 or +7 pieces; at most3m−3 or3m−1 variables | Every outer label in the declared stable range |\n| Fixed-order unstable hooks, a≥2k | T064–T065: explicit point-deletion polytopes | Every valid parameter, polynomial construction for each fixed k |\n| Equal-middle and bounded-width families |')
s=s.replace('The coefficient algorithm uses Bostan–Mori','G038–G039 retain the same encoding qualification; T064–T065\nstate their full dependence on ideal order k. The coefficient algorithm uses Bostan–Mori')
insert=r'''R047 gives the finite profile for tails \((4^h,3,2^j,1)\):
with \(K=2h+j+3\), its multiplicity at row count s is
\(r_s=\min(h,\max(0,s-h-j-3))\). The actual image is
\(\min(r_a,r_n)\) for \(a,n\ge4\), \(\max(a,n)\ge K\).

R049 gives full isotypic surjectivity for every tail of size D,
width t≥2 and odd-part count o at
\[
n\ge M=\left\lfloor\frac{D+t-q}{2}\right\rfloor,
\qquad q=\left\lceil\frac{o-(t\bmod2)}3\right\rceil.
\]
The averaged row morphism, exact kernel injection and normalized
moment factorization prove the actual rank statement. Its explicit
Euler-form family supplies nonzero full-image components with
unbounded row improvement. R048 includes the explicit Pfaffian
decomposition used in this argument.

'''
s=s.replace('G013–G014 and R017–R034 retain',insert+'G013–G014 and R017–R034 retain')
p.write_text(s)

p=Path('work/root/remaining_gates.md');s=p.read_text()
old='The current remaining task is a uniform bound or further exact evaluation for varying shapes beyond these stable hook tails and for hook charts of ideal order at least two. T061 completes every valid first unstable hook order with actual evaluation splittings and a positive deleted-point formula; its degree-two endpoint and full varying-degree encoding scope are proved.'
new='G038 and G039 complete every stable two-row tail with second part2 or3, including all outer labels, positive polytopes, exact values and support. T061–T065 complete every valid unstable hook chart with a≥2k, using actual jet splittings and positive deleted-point formulas; construction is polynomial for each fixed k and exact evaluation has the stronger stated fixed-parameter bound. The current remaining hook range is a<2k. Beyond the evaluated families, varying-shape polynomial description bounds remain active. G040 proposes a complete fixed-second-part construction through finite cokernels and bounded fixed-variable Gröbner calculations; its independent whole-proof review is in progress, so it is not counted here as completed.'
assert old in s;s=s.replace(old,new)
s=s.replace('Higher repeated-four tails below this moment bound remain active work.','R047 determines the entire finite profile for tails(4^h,3,2^j,1) and their actual rank when one row parameter reaches2h+j+3. R048 and R049 sharpen the full-isotypic threshold to floor((D+t−ceil((o−(t mod2))/3))/2), with o the odd-part count. R049 supplies an exact averaged-row kernel comparison and positive hook families with unbounded row improvement. Remaining repeated-four and general canonical components are restricted to the complement of these proved ranges.')
s=s.replace('Checkpoint08 is due at this review boundary, and Checkpoint09 at05:46:08UTC.','Checkpoint08 was delivered; Checkpoint09 is due05:46:08UTC.')
p.write_text(s)

geo=r'''## Higher transfer kernels, fat jets and the refined centered map

**G038–G039.** The actual equivariant derivative transfer on the free
P-modules over the reflection representation gives coherent kernels.
Their finite cokernels and minimal covers live over
\(\operatorname{Spec}\mathbb Q[e_2,\ldots,e_m]\). The explicit
basis cancellations give the free sheaf plus the displayed Koszul
syzygy sheaves. At second part three, the Kulkarni tensor quotient,
Ricci contraction and rational inverse identify the exact action of
e2; restriction to \(\mathbb Q[e_2^2,e_3,\ldots,e_m]\) and its
free rank-two extension retain every degree. Each least-support
monomial cycle is mapped back to the original transfer kernel.
The flag identification T032 C4–8 and determinant pairing then
give the stated original Schur coefficient. The sheaf, frame and
Schur-operation locators are EGA II2.4.1–2.4.2,2.5.2/2.5.4;
SGA3 I4.5/4.7.2–4.7.3; SGA6 VI3.3 and V4.2,4.4,4.8–4.9.
Cote133/028 is compared by A012's integral tensor-word and Young maps.

**T062–T065.** The frame's kth ideal sheaf on projective space,
twisted horizontal differential forms and exact finite jet quotient
are the specified coherent objects. The actual quadratic separators,
Taylor matrix, invariant Gram right inverse and horizontal Euler
contraction split the quotient in every asserted range. The endpoint
uses Nagel–Trok Theorem5.3 p233 and Lemma3.1 p225, with its precise
regularity-index convention. Flag projection and the determinant
line identify this kernel with the original multiplicity object.
The orbit/exterior induction maps and Young projectors compute the
finite quotient; the full lattice-point deletion supplies its positive
dimension formula. Projective and bundle comparisons use the same
EGA II and SGA3 locators, and their representation-K0 classes use the
specified SGA6 Schur operations. The fixed-order complexity and the
ordinary part-list encoding qualifications are retained under this
dictionary.

**R047–R049.** Perfect complementary-column pairings give R047's
finite reflection modules with determinant fourth power. R048's
explicit unipotent congruence and Pfaffian highest vectors give the
paired Schur decomposition. R049's map sends an extra row to the
small mean vector; on centered decompositions it is literally
\(1_{\Lambda T}\otimes q\), with the displayed kernel injection.
The alternating-weight occupancy bound removes that precise Schur
summand from the kernel character. Ordinary and skew Cauchy use
the identical Schur map of q because their rational Young projectors
commute with its tensor powers. Independent-row polarization and
the triangular moment automorphism identify the composite with
the normalized Chow pullback in R037 EP3–5. Thus EGA I9.5.2's
scheme-theoretic image has the asserted full component. The Euler
form and its nonzero Vandermonde evaluation give a literal section
in each positive family. Frame descent and representation-K0
transport again use SGA3 I4.5/4.7.2–4.7.3, SGA6 VI3.3 and
V4.2,4.4,4.8–4.9, with the rational denominators explicitly retained.
'''
p=Path('work/root/geometric_dictionary.md');p.write_text(p.read_text()+'\n\n'+geo)

events=[
 ('G-038','targeted proof check','Read the complete eight-section SR2.1–17 proof and executable. Checked every quadratic-transfer highest vector and endpoint, exact finite cokernel and I action, free cancellation and exceptional Koszul presentation, explicit star cycles, tensor-coset and unordered-pair isomorphism, fake-degree arithmetic, polytope bijections, support and bit/encoding bounds. PASS. A092 supplies a separate independent whole-proof review.'),
 ('G-039','targeted proof check','Read the complete eight-section SR3.1–23 proof and executable. Checked cubic-transfer kernel/cokernel, actual Young curvature quotient, all Ricci inverse constants, e2 action, minimal-cover cancellations, modified regular sequence and rank-two flat extension, tensor operators, m3 determinant endpoint, every positive cell and exact value/support complexity bound. PASS. A095 supplies a separate independent whole-proof review.'),
 ('G-038','computation or formal certificate','Executed check_stable_second_row_positive.py:135 independent free-numerator comparisons,2160 direct Schur/cycle module coefficients and2160 support checks,90 original MN plethysms,182 literal polytope cases with1636 witnesses. Maximum observed variables15/pieces8. Four a=10^30 evaluator examples separately exercised. STABLE_SECOND_ROW_POSITIVE_RECEIPT.json PASS.'),
 ('G-039','computation or formal certificate','Executed check_stable_third_row_positive.py:132 independent free-numerator comparisons,2295 direct Schur/cycle coefficients and2295 support checks,90 original MN plethysms,208 literal polytope cases with5912 witnesses. Maximum observed variables17/pieces11. Four a=10^30 evaluator examples separately exercised. STABLE_THIRD_ROW_POSITIVE_RECEIPT.json PASS.'),
 ('T-062','targeted proof check','Read the entire higher_hook_jets_report.md HJ1–16 and executable. Checked the actual quadratic frame derivative map, rational equivariant inverse, local Taylor basis and other-point vanishing, horizontal trivialization, coefficient degree, exact flag ideal pushforward, determinant and target action. PASS. A093 supplies a separate independent review and finite jet computations.'),
 ('T-063','targeted proof check','Whole report/code reading with T062. Checked Sm−2 branching target, correction at most4, every low-comajor tableau/subset/coin selection, trivial-label endpoints, parity transport, unique-owner disjoint point deletion and exact fixed-order complexity. PASS; author and archive computations retain their own events.'),
 ('T-064','targeted proof check','Read every section of FK1–15 and the entire executable. Checked actual jet-to-permutation symmetric-power map, all monomial-orbit/exterior restriction endpoints, bounded LR induction, uniform D_k injection bound, diagonal-width and excess estimates, bounded point enumeration, changed least-support bit under coin2 transport with inverse recovery, disjoint deletion and both complexity bounds. PASS. A096 independently reads the whole proof/code.'),
 ('T-065','targeted proof check','Read the complete HE1–7 proof and full endpoint executable. Checked exact Nagel–Trok regularity convention, every proper/full linear-space inequality, rational Taylor Gram right inverse, degree-one horizontal lift, physical m4 and k1 endpoints, identical flag/sign comparison, bounded-excess deletion and full a≥2k route. PASS. Root source reading is separately scoped; author whole-chain source review and computation are separately credited.'),
 ('R-047','targeted proof check','Read the whole RF1–20 proof and five sections. Checked last occupied-row exclusion, actual scalar-one centered restriction, complementary-column isomorphism and determinant fourth power, every finite profile endpoint, threshold inequalities, actual normalized moment factorization and rank transpose. PASS; A091 supplies independent whole-proof and finite character/complement checks.'),
 ('R-048','targeted proof check','Read the whole OI1–21 proof and six sections. Checked upper-unipotent block congruence, dense Pfaffian chart, paired highest-weight multiplicity proof, both parity exclusions, exact faithful centered evaluation and normalized canonical injection, and every explicit nonzero family. PASS; A094 independent review records91 theorem-range checks plus5 auxiliary width-one zeros, not96 theorem-range cases.'),
 ('R-049','targeted proof check','Read the complete OO1–25 proof and six sections. Checked the actual averaged-extra-row map and literal id⊗q splitting, surjectivity and exact kernel injection, character-only omitted-orbit use, all dual/exterior Pieri weight changes and endpoints, faithful Schur evaluation and normalized actual canonical factorization. Checked the exact Euler/Pieri kernel, coefficient degree, Vandermonde scalar/sign, zero-row padding and unbounded positive-family improvement. PASS; numerical character and scalar receipts remain separately scoped.'),
 ('SRC-MACDONALD-LR','used and rechecked in this run','Read the primary retained Macdonald second-edition I§9 pp142–147 in full: lattice-word convention, reversible substitution maps, Lemma9.7, full Littlewood–Robinson recording bijection and inverse. Applied the stated induction/restriction LR multiplicities to T064 and G040 through the specified Young/coset maps. No new proof of the known rule is claimed.'),
 ('SRC-NAGEL-TROK-ENDPOINT','used and rechecked in this run','Root read publisher text Lemma3.1 p225, Theorem5.3 p233 and surrounding regularity/induction passages; verified the exact ceiling convention and the application to every frame subspace in HE4–5. The author independently read the full §§2–5 proof chain. Root does not claim a separate complete re-proof of the cited general regularity theorem.'),
 ('SRC-ASCHENBRENNER-KERNEL','used and rechecked in this run','Read primary Ideal membership in polynomial rings over the integers §3 through Theorem3.2 PDFp16, including the complete homogeneous-system proof, adjugate/monic elimination and recursive bound. Applied (2md)^(2^N) to the actual bounded-degree J-matrix of G040. Source https://www.mat.univie.ac.at/~maschenbrenner/pdf/ideal2.pdf.'),
 ('SRC-LIANG-MODULE-GB','used and rechecked in this run','Read primary arXiv1905.07517v3 Corollaries38/42, Theorems40–41 and their passage to the non-graded bound. Corollary42 PDFp19 gives2(Dm)^(2^N) for the module Gröbner basis and applies to degree-zero free basis vectors with weighted shifts retained separately. Root checked the cited statements/passage; no full independent re-proof of all19 pages is claimed.'),
]
p=Path('work/root/CHECK_EVENTS.tsv');fields=next(csv.reader(p.open(newline=''),delimiter='\t'))
with p.open('a',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t')
 for sid,kind,outcome in events:
  w.writerow(dict(statement_id=sid,date=stamp,who_model_effort_run='root; GPT-6 Astra Pro; effort not exposed; GCT_PLETH_20261121_run01',type=kind,outcome=outcome))
print(stamp,'integrated interval16',len(events),'root events')
