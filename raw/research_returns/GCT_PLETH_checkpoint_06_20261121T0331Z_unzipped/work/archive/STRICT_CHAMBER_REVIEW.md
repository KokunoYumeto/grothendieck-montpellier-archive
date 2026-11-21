# Independent audit of exact strict five-row support

Statement **A-052**, reviewing G-028 in
work/root/five_row_strict_nonvanishing.md, SC.1–SC.8 and all five
sections. Checked 21 November 2026 by GPT-6 Astra Pro,
run /root/archive_audit; effort setting not exposed.

**Complete proof PASS.** The finite seed and increment certificates,
the exhaustive monoid argument, the exact ray module, every determinant
parity, and the specified canonical-map consequences were checked.
The independent calculations are in GAP1_SEEDS_INDEPENDENT_RECEIPT.json
and STRICT_CANONICAL_TARGET_RECEIPT.json.

## Minimal seeds and the actual injection

For positive gaps \(g_i=1+p_i+2t_i\), the given \(t\) satisfies the
weighted congruence because the total partition size is divisible by
five. A minimal admissible \(u\le t\) exists in a finite coordinate box.
If its total were at least five, list any five indexed residues
\(i\in\{1,2,3,4\}\); two of the six partial sums coincide modulo five.
Removing the resulting nonempty zero-sum subvector preserves the
congruence and contradicts minimality. This proves the total-at-most-four
bound used in the enumeration.

The difference \(v=t-u\) is nonnegative and has weighted sum divisible
by five, since multiplication by two is invertible modulo five.
Consequently it is the gap vector of a partition \(\eta\) of size
divisible by five, and
\[
\lambda=d\mathbf1+\sigma+2\eta.
\]
The specific G-024 multiplier is the nonzero invariant
\(\sum_g(gh_\eta)^2\) in the flag-polynomial domain, followed by the
determinant to the power \(d\). Its degree, balanced weight and slot
action give exactly the displayed embedding and sign twist.
Thus transferring seed lower bounds uses a particular injective
linear map.

The independent program enumerates all sixteen parities and all
componentwise minimal vectors of total at most four. It finds exactly
76 seeds. It reconstructs their class traces by integer
Jacobi–Trudi determinants and, in the two-cycle cases, Jacobi–Trudi
evaluation and interpolation over \(\mathbf F_{61}\), independently
of the root alternant/Pieri implementation. The polynomial degrees
and signed reconstruction bounds are those proved in the independent
G-025 check; here the largest inner degree, including increments,
is fourteen. The interpolation degree is at most 35, below 61,
and the two-cycle signed trace bound is below \(61/2\).
All 532 seed traces and all 532 multiplicities agree. Exactly 71
seeds have every multiplicity positive, and the five remaining
vectors agree with the displayed table.

## Exhaustion by fourteen generators

Every indecomposable nonzero element of the weighted zero-sum monoid
has total at most five. A longer element contains a zero-sum subvector
of total at most five by the same partial-sum argument; it is proper,
contradicting indecomposability. Recursive subtraction therefore
decomposes every element into the fourteen explicitly enumerated
generators. Independent coordinate-box testing confirms the fourteen
items and excludes all other vectors in the proved finite range.

For each of the five deficient seeds, the independent program computes
all fourteen generator increments. These are 70 further cases,
490 class traces and 490 irreducible multiplicities. Exactly the four
listed seed–axis pairs remain deficient. No middle label vanishes.

For either isolated seed, every nonzero monoid increment contains a
generator whose first increment already has full support; the
remaining monoid sum supplies an actual G-024 injection. For the
two long-axis seeds, this same reasoning leaves only repeated
increments along the indicated single axis. For the staircase seed,
a mixed sum of the two surviving axes dominates \((1,0,0,1)\).
Subtracting this generator preserves nonnegativity and the
weighted congruence. Its positive increment therefore injects into
the mixed sum. These arguments exhaust all decompositions, without
assuming uniqueness of a monoid expression.

The two parity classes of each axis combine as \(L=1+10a\) and
\(L=6+10a\). Their union is exactly the positive integers congruent
to one modulo five. Thus the finite certificate proves positivity
outside precisely the two stated rays and two isolated normalized
partitions.

## Exact rays and determinant parity

At \(L=5t+1\), the first normalized ray is
\((5t+4,3,2,1,0)\), of inner degree \(t+2\). At \(t\ge1\),
the G-027 dictionary has \(k=0\), \(\alpha=(3,2,1)\), and
sign exponent three. The actual quotient-section and inverse
balanced-chart maps identify its balanced module with
\(\epsilon\otimes S_{321}\mathfrak h_5\).
The independent literal \(3\times3\) Jacobi–Trudi determinant gives
\[
(64,0,0,-2,0,0,-1)
\]
in the seven stated conjugacy classes, and hence multiplicities
\((0,2,3,3,3,2,0)\). Its nonzero class traces are on even
permutations, so the displayed sign twist preserves this trace vector.
The \(t=0\) endpoint is the separately computed staircase seed.

For the reverse ray, the rectangle has width \(H=L+3\).
The perfect exterior-column pairing sends balanced degree \(n\)
to \(H-n\), contributes determinant power \(H\), and dualizes
the finite-group module. Every symmetric-group irreducible is
self-dual, and both ray multiplicity vectors are invariant under
partition transpose. Thus the exact pairing proves the reverse-ray
values, including its determinant parity. The additional shift
\(d\mathbf1\) contributes \(\epsilon^d\).
Both extreme coefficients remain zero on each ray; it interchanges
the single missing extreme label at either isolated partition.
The other extreme coefficient is exactly one there.

## Actual degree-five canonical ranks

The cited CIM square-map kernel has eight distinct multiplicity-one
components. Exactly four are strict. The two independent target
calculations used here are:

1. literal balanced Jacobi–Trudi traces and the trivial-character
   inner product;
2. the full power-sum expansion of \(h_5[h_5]\), followed by
   Murnaghan–Nakayama evaluation, using 898 cycle-index terms.

Both methods give the following complete result.

| Partition | Target | Known kernel | Actual image |
|---|---:|---:|---:|
| \((12,7,3,2,1)\) | 2 | 1 | 1 |
| \((12,5,4,3,1)\) | 1 | 1 | 0 |
| \((10,8,4,2,1)\) | 3 | 1 | 2 |
| \((9,7,6,3,0)\) | 2 | 1 | 1 |

The square map has the same source and target multiplicities, so
subtracting its specified kernel gives these actual image ranks.
For every other strict degree-five type, its kernel component is
zero. The already audited normalized-transpose and McKay propagation
maps give the stated target surjectivity at \(n\ge6\). G-028
makes no unproved complete rank claim at \(n=3,4\).

The final geometric statement refers to that same coordinate
pullback and its affine schematic-image algebra. In particular,
the missing \((12,5,4,3,1)\) image component follows from the
computed rank-zero map, while its ambient target multiplicity is one.

## Exact verification scope

The proof was read in full. The independent finite calculations
cover 76 seeds, fourteen monoid generators, seventy increment cases,
1,022 class traces, 1,022 multiplicities, seven stabilized-ray traces,
and the four square-map targets by two methods. The previously
audited CIM and McKay source results supply their actual kernel and
propagation maps; their original large numerical matrices were not
regenerated here. All events distinguish these scopes.

