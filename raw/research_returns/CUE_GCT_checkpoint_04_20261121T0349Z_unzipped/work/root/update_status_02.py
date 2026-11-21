from pathlib import Path
from datetime import datetime, timezone
R=Path(__file__).resolve().parent
OUT=R.parents[1]/'deliverables'
now=datetime.now(timezone.utc).isoformat()
p=R/'intro.tex';s=p.read_text()
a=s.index('The principal positive results')
b=s.index('\\subsection{Stipulated analytic inputs',a)
s=s[:a]+r'''The principal positive results are exact rather than heuristic. R-01--R-09 identify the CUE character and ratios operations, positive projector formulas, orbit-closure Gram ranks, and the missing quotient numerator. R-10 closes the height-two rectangle and quadratic determinant case. G-05 excludes every at-most-three-row multiplicity obstruction. G-07/R-12 give an exact four-row permanent-minus-determinant shifted-plethysm formula at size four. R-13 classifies quaternary permanent dominance by exact certificates for sizes one through sixteen and a dimension exclusion thereafter. R-15--R-16 give algebraic dimension growth and an unbounded range of genuine padding. G-10 makes the resulting degree threshold explicit. G-11 identifies rectangular outer highest weights and an explicit degree progression for these gaps, including $n=m+1$ for every $m\geq8$ and each fixed ratio below $\sqrt5/2$ eventually. G-12 excludes that rectangular sector at and above $n=4m/3$. G-08--G-09 give explicit low-row exclusion bounds at larger padding.

On isolation, I-01 gives the genuine Hoza transfer for independent vertex variables. I-03--I-04 identify coefficient flags and projected matroid cones; I-14 gives the weaker joint-span condition. The rank-profile construction I-21 now supplies an explicit polynomial-size hitting set for width at most three in one unknown variable order, in every characteristic with the stated field-node convention. It has a complete checked proof here; its mechanism is credited to a recent unrefereed preprint, whose broader claims are not assumed. The unresolved target is a bound polynomial jointly in the growing width, length and degree. The precise conditional matrix-invariant consequence remains I-08.

Purity gives sparse constructions, an actual-sheaf Gram criterion with full conductor accounting, and limitations of energy approximation. P-11 identifies explicit common arithmetic evaluation points with hitting-set encodings in its rational model. P-12 constructs such a point for the width-three class, together with an integer hitting curve and an exact trace-dual coefficient-span map, using I-21 and elementary algebraic number theory. No additional RH input is required for that construction.

''' +s[b:];p.write_text(s)
p=R/'open_gates.tex';s=p.read_text()
s=s.replace('while G-07 and R-12 solve a specific four-row quotient calculation exactly.','while G-07 and R-12 solve a specific four-row quotient calculation exactly. R-15--R-16 and G-10--G-11 now prove explicit rectangular multiplicity gaps in their specified linear-padding range. G-12 proves that this outer-rectangular sector is excluded for $n\\geq4m/3$. The unresolved asymptotic range and its higher-row or nonrectangular multiplicities remain separate.')
a=s.index('The strongest current gate is explicit joint coefficient-span preservation')
b=s.index('\\paragraph{U-03',a)
s=s[:a]+r'''I-21 closes the width-at-most-three, one-unknown-order case by an explicit rank-preserving selector map, including arbitrarily many rank-two cuts. The remaining target is a hitting set whose size and construction time are polynomial jointly in length, degree and growing width. Explicit joint coefficient-span preservation in I-14 remains a sufficient gate; I-03--I-04 give the stronger cone-hitting alternative. The direct Hoza transfer must respect the monomial quotient and coefficient cancellation. The independent-variable theorem, rank-profile specialization, and arithmetic encoding do not yet supply the required uniform width dependence. The attempts register records the exact constructions tested and their failure points.

''' +s[b:]
s=s.replace('P-11 removes a detour: a sufficiently explicit common algebraic point is itself a hitting-set encoding, independently of GRH.','P-11 removes a detour: a sufficiently explicit common algebraic point is itself a hitting-set encoding, independently of GRH. P-12 constructs that point and an integer curve for the width-three class; the corresponding general-width construction remains open.')
p.write_text(s)
p=OUT/'IMPLICATIONS.md';s=p.read_text()
s=s.replace('Subsequent padding/dimension deductions are recorded under their live IDs in the paper and question register.','R15–R16 give an algebraic lower bound on the quaternary permanent image dimension and prove four-row multiplicity gaps in an unbounded range of genuine padding. G10 supplies an explicit degree threshold. G11 strengthens the conclusion to the specified rectangular outer shape (nd/4)^4 on an explicit degree progression, including n=m+1 for every m>=8 and every fixed ratio 1<n/m<sqrt(5)/2 eventually. G12 excludes these rectangular gaps for n>=4m/3 and makes the padded rectangular multiplicities zero when the inequality is strict. The new statements concern the location and multiplicities of representations, and do not improve the established quadratic border-determinantal-complexity lower bound; exact source context is retained in the paper.')
s=s.replace('The precise matrix-invariant consequence is the conditional implication I08. The antecedent remains unresolved.','I21 gives a complete checked polynomial hitting set for width at most three in one unknown variable order, over any characteristic with the explicit working-field convention. The rank-profile mechanism is credited to the recent unrefereed Liu preprint, and only the independently proved specialization is used. The remaining uniform target is polynomial in the width as well as length and degree. The precise matrix-invariant consequence is the conditional implication I08; it needs growing widths, so its general antecedent remains unresolved.')
s=s.replace('GRH does not construct the missing encoding.','P12 now constructs the common algebraic point, integral hitting curve, and exact trace-dual span recovery for width three. Its field degree and coordinate descriptions are polynomial in length and total degree, with a large fixed exponent. The construction is unconditional and uses the checked rank-profile map. The general-width arithmetic encoding remains open.')
s=s.replace('The separate dictionary in the paper supplies an exact locator and proof transport for each finding.','The separate dictionary in the paper supplies an exact locator and proof transport for each finding. The newer results add reductive invariant quotients and explicit Veronese algebras for the rectangular gaps, an integral cocharacter degeneration for their padding exclusion, local Artin rank charts for width-three preservation, and a finite flat arithmetic algebra with an explicit trace-dual basis.')
p.write_text(s)
p=OUT/'LEDGER.md';s=p.read_text();s=s.replace('No checkpoint has yet been created.','Checkpoint01 has been created and persisted; subsequent checkpoint entries record their actual times.')
s+='''

## '''+now+''' — rectangular shapes and width-three gate closed

This is an ordinary dated progress entry, not the scheduled three-hour review. No stagnation review has yet occurred.

| Main question | Current state | Strictly smaller gate or resolved subcase |
|---|---|---|
| Q1 Rectangular bridge | General uniform positive extraction open; new explicit restricted gaps proved | R15–R16 prove an unbounded genuine-padding range; G10 supplies a degree threshold; G11 specifies rectangular outer weights and a degree progression. G12 proves their exclusion for n>=4m/3. |
| Q2 Haar and boundary | Exact identities and stronger restricted orbit-closure ranks proved | The SL4 Haar projector is the rectangular invariant piece; the reductive quotient dimension and effective Veronese comparison force its positive multiplicity gap in G11. General orbit-boundary extraction remains open. |
| Q3 Isolation | Width<=3, one unknown order resolved by I21 | Explicit 21-parameter map and finite polynomial hitting set. Remaining gate: size and construction time polynomial jointly in growing width, length and degree. The matrix-invariant consequence needs this growing-width bound. |
| Q4 Purity/arithmetic | Width-three common algebraic point and integer hitting curve constructed in P12 | Explicit primitive field, bounded discriminant, and trace-dual coefficient-span preservation; no extra GRH input. General-width kernel-avoiding arithmetic or sheaf encoding remains open. |
| Q5 Zero statistics | Listed dependency audit complete | Source-specific RH predicates and support ranges retained; no new claim about full correlations or automorphic RH. |
| Q6 Grothendieck | Dictionary extended through R16, G12, I21, P12 | Quotient/Proj/Hilbert transport, cocharacter special fiber, local-Artin rank charts, finite flat arithmetic trace map. Original manuscript images remain unavailable. |

### Checks and source boundaries

Root whole-proof readings are recorded for R16, I21, P12, G10–G12. Independent full reviews of G10–G12 and R16 were obtained, with exact source checks. The broader claims of recent preprints are not substituted for these proved narrower statements. The three-hour review is still due at approximately03:49:46 UTC.

### Document status

The local XeLaTeX format was repaired and the manuscript now compiles. A current build and visual page inspection are being performed before the next checkpoint; no completed visual review is asserted in this entry.
''';p.write_text(s)
p=R.parents[1]/'work/assemble.py';s=p.read_text()
s=s.replace('A reduced determinantal-quartic divisor and certified permanent projections yield a complete four-row shifted-plethysm difference in a fixed case.','A reduced determinantal-quartic divisor gives an exact shifted-plethysm difference. Algebraic permanent-image dimensions and invariant quotients produce explicit rectangular multiplicity gaps in a range of genuine padding, with a separate rectangular exclusion threshold.')
s=s.replace('Purity gives quantified sparse and trace-space constructions; exact or uniformly conditioned energy reconstruction has explicit size barriers.','A checked rank-profile construction yields polynomial hitting sets for width three in an unknown order and an explicit arithmetic point with trace-coordinate span recovery. Purity gives additional sparse and trace-space constructions; uniformly conditioned energy reconstruction has explicit size barriers.')
s=s.replace('\\setcounter{tocdepth}{2}','\\makeatletter\n\\renewcommand*\\l@subsection{\\@dottedtocline{2}{1.5em}{2.8em}}\n\\makeatother\n\\setcounter{tocdepth}{2}')
p.write_text(s)
print(now)
