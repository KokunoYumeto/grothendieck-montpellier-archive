# Literal GD requirements for odd auxiliary discriminants

Reviewer `/root/lean_chain`; GPT-6 Astra Pro; effort not exposed.
21 November 2026. This is a source-scope deduction, not a Lean kernel
build or a review of the separate proposed field-family arithmetic.

The complete `HeightAndVanishing/Counts.lean` definition at lines 9–22,
the complete `gdFacts` proof, and the complete
`SmallClassNumbers/ClassNumberThree.gd` proof were read in the pinned
tree. Hashes and time are in `gd_odd_field_review_manifest.json`.

Let p≥7 be prime, D<0 an odd fundamental discriminant, E=Q(sqrt(D)),
and suppose p does not divide D h(D). Let e≥1 be even and suppose
(p−1) does not divide 2e. Set N=2 and psi=1. Then every literal GD
field is satisfied:

| Source field | Required content | Discharge |
|---|---|---|
| `l_odd` | p≠2 | p≥7 |
| `e_pos` | 1≤e | Hypothesis |
| `N_even` | N even | N=2 |
| `ord` | p does not divide order(psi) | order(1)=1 |
| `ine` | comp(p,psi)^2=1 | The trivial character remains trivial |
| `par` | PsiEven(e,psi) | psi(−1)=1=(−1)^e |
| `quad` | [E:Q]=2 | Negative fundamental discriminant |
| `imag` | E totally complex | D<0 |
| `l_cop` | p does not divide abs(D)h(D) | Hypothesis |
| `cop` | gcd(abs(D),N)=1 | D odd and N=2 |
| `eta` | The displayed cyclotomic/Dirichlet kernel is not contained in G_E | Ramification argument below |
| `gen` | (p−1) does not divide 2e | Hypothesis |

For `eta`, the second intersected kernel is the whole group: at N=2
the unit group is trivial, so the `chiP` Dirichlet character is trivial.
The first kernel is the kernel of the mod-p cyclotomic character.
If it were contained in G_E, Galois correspondence would put E inside
Q(mu_p). But a prime q dividing D is ramified in E, is distinct from p,
and is unramified in Q(mu_p). This is impossible. Equivalently, one can
choose a nontrivial quadratic inertia element at q; it lies in the
cyclotomic and trivial-Dirichlet kernels and does not lie in G_E.

No split-at-p condition, regular-weight cutoff e<p, or restriction to
class number one occurs in GD. A bound 0<h(D)<p is sufficient for the
class-number factor of `l_cop`.

For the proposed progressions p≡3 mod4 and
e=(p−3)/2+(p−1)t, t≥0, positivity and evenness are automatic, and
2e≡−2 modulo p−1 proves `gen`. Thus once a separate proof establishes
odd fundamental D and p not dividing D h(D), no additional GD obstacle
remains. This note does not certify those separate family calculations.
