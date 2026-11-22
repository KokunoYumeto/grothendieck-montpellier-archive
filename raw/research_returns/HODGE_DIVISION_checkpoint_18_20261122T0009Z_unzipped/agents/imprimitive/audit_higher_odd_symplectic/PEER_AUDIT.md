# Independent whole-proof audit: D-HOS-03–06

**Verdict: PASS in the precise stated scope. No mathematical repair requested.**

Reviewer: `/root/imprimitive`, GPT-6 Astra Pro, inherited effort not exposed,
HODGE_DIVISION. Actual final clock reading: **2026-11-21 20:08:30 UTC**.

Entire reviewed proof:
`agents/g34_eightfolds/bireflection/higher_odd_symplectic_section.tex`,
SHA-256 `eb760afa97ee57230236ce9058085a4225a78a502e2aa57df5c9efb9637a9ccc`.
All lines were read, including both expanded trace-form and row-normalizer
arguments. The complete author checker and its output were read as well.
No edits were made to the author's files.

## Universal mathematical review

### D-HOS-03: inner operators

The projective kernel is exactly the center for a nontrivial ordinary
irreducible representation in this quasisimple range. Taking a power to
prime projective order cannot increase projective support. A projective
p-element becomes unipotent after a central sign; a prime-to-p element
is semisimple, including the projective involution with square `-I`.

For an invariant isotropic subspace, the symmetric shear construction is
injective, additive, unipotent and symplectic. Its conjugation action is
`C -> A C A^t`; a nontrivial prime-order action has a fixed-point-free
moving summand. The exact trivial-weight average and cyclic-weight
orbit estimate give the asserted support without requiring the global
intertwiner's prime power to be scalar.

If the symmetric-square action is trivial, semisimplicity forces
`A=±I`. The averaging projector constructs a paired eigenvector with
the same eigenvalue. The moving part of the complementary symplectic
operator is nondegenerate and has positive even dimension. The displayed
line radical has exactly the Heisenberg law used in already reviewed
D-HOS-01, including its central coefficient `2z` and the `lambda` twist
in conjugation. Its lower bound includes every isotypic multiplicity,
not just a Weil constituent.

If no invariant isotropic subspace exists, the primary decomposition
has only distinct self-reciprocal factors, each with multiplicity one.
The trace-pairing definition gives the claimed skew-Hermitian extension
form; multiplying by a scalar negated by the involution makes it
Hermitian. Finite-field norm surjectivity supplies an isotropic line
when the multiplicity is at least two, excluding that case. Thus the
centralizer is the product of norm-one tori. The column-orthogonality
bound, elementary degree floor and the displayed endpoint inequalities
give the claimed elliptic estimate. No unproved semisimple character
ratio is used.

### D-HOS-04: diagonal projective involutions

A natural similitude lift satisfies `h^2=cI` and multiplier `mu=±c`.
The split eigenvalue case gives an isotropic eigenline. In the nonsquare
case the trace form over `Fq[sqrt(c)]` is alternating when the adjoint
involution is trivial and skew-Hermitian when it is nontrivial; its
isotropic extension-field line gives an invariant isotropic Fq-plane.
The normalized shear action is exactly `mu^-1 A C A^t`. If it were
trivial, the eigenvalue-square and pair-product identities would force
`A=alpha I` with `alpha` in Fq and `alpha^2=mu`, contradicting the
nonsquare multiplier. The nonzero minus-one shear space gives the
required weight pairs. All signs and the bilinear-versus-Hermitian
distinction check.

### D-HOS-05: arbitrary normalizers

The cover and outer-group classification inputs apply in the entire
stated range. Perfectness removes a central ambiguity in lifting an
automorphism from the simple quotient. Prime fields are handled by
squaring a diagonal operator: either a noncentral inner operator remains,
or the actual induced automorphism is an involution and D-HOS-04 applies.
For arbitrary fields the commutator argument handles a noncentral
commutator by D-HOS-03 and a nonidentity scalar commutator by its full
ordinary moving rank. This yields half the inner bound for q>=25.

The remaining q=9 descent is sound. From `h sigma(h)=cI`, associativity
forces `c` into F3, and the multiplier has norm one and is a square in
F9. The scalar norm repair makes the semilinear map square to one.
The additional form rescaling satisfies the exact Galois covariance
identity. The fixed-space decomposition and the nondegenerate descended
alternating form provide a symplectic F3-basis and a GSp9 change of basis.
Relabeling the representation by this similitude is legitimate even
when the representation is not separately invariant under that diagonal
class. The row subgroup is normalized transitively by the explicitly
named GL_(n-1) block. All nonzero weights have one multiplicity; their
Frobenius fixed count is `3^(n-1)`. This gives `13/54` at the endpoint.

### D-HOS-06: actual source obstruction

The full normalizer bound survives tensor convolution. Nontrivial factor
cycles have support at least one quarter by the weighted word-orbit
argument; the closing operator is diagonalizable because a power is
scalar. Every factor satisfies the same bound, so arbitrary mixed ranks
and fields and all compatible permutations are allowed. Genuine scalar
inertias have full ordinary moving rank.

The previously proved polarized intermediate-cover factorization is used
with its correct larger-inducing-field scope. Genus at least two is
impossible; genus one has at most six inertia points and period dimension
at most six. A rank-nine source therefore needs genus zero and at least
twelve genuine branch points. The exact budget gives
`e <= 165669/181 < 916`, while every factor already has degree at least
`3*7^3=1029`. This proves image dimension at most eight; no sufficiency
of a parameter count is inferred. Fields 3 and 5 remain outside this
theorem.

## Independent executed certificate

`independent_check.py` imports no author arithmetic, matrix code or
selected finite input. It uses exact Fractions, independently constructed
symbolic matrices, and the different field presentation
`F9=F3[t]/(t^2+t+2)`.

Actual result: **PASS, 1.410285 seconds**. The retained output is
`independent_checked.json`.

- Exact reconstruction of `delta*=9234/55223`, the q=25 and q=9
  bounds, and the total-degree ceiling `165669/181`.
- Independent symbolic Heisenberg symplectic and product identities
  in the paired `(e,f,W)` ordering, including nondiagonal symplectic
  conjugation and both central signs.
- Both quadratic companion-matrix normalized shear actions, with
  moving ranks one and two.
- All **5760 GL2(F9) matrices**, with all **240** scalar-square
  semilinear cocycles (120 for each central sign), complete scalar and
  form repairs, an actual fixed symplectic basis, and **19440** vector
  descent identities.
- Complete row-weight counts in dimensions three, four and five:
  `729/27`, `6561/81`, `59049/243` total/fixed weights.

These are finite symbolic checks supporting the universal proofs, not
a claim to enumerate all ranks or a substitute for the primary-space
argument. Code SHA-256:
`6496efb349bf61332c944d80a37a21496da4414d8c262bdb4a0801d8e606f0d8`.
Output SHA-256:
`4e51637339e2d0761e5bb02c79c8e637a1cd7256bea8a5a42ae58e1250f32ec9`.

## Fresh source reads and boundaries

1. M. W. Liebeck, *Character ratios for finite groups of Lie type, and
   applications*, Contemporary Mathematics 694 (2017), 193–208.
   Complete simply connected conventions on author p. 2 and
   Theorem 2.4 with the relevant surrounding text on pp. 3–4 were
   reread. Rendered p. 4 confirms **1/(sqrt(q)-1)**, with the
   subtraction outside the radical. URL:
   https://www.ma.imperial.ac.uk/~mwl/princeton-survey-final.pdf .
   This is the published explicit restatement of Gluck used as a known
   input; no new proof of Gluck's entire theorem is claimed.
2. Li–Xia, Memoirs AMS 279 (2022), no. 1375, DOI
   `10.1090/memo/1375`: full §2.2.2/Table 2.1, author p. 14,
   freshly reread at the retained author version
   https://arxiv.org/pdf/1408.0350v3 . Its PSp row has
   `Out=C_(2,q-1) x C_f`, excluding only the even-characteristic
   rank-two exception. Publisher-versus-author pagination remains
   explicitly distinguished.
3. Hiss–Husen–Magaard, Memoirs AMS 234 (2015), no. 1104,
   DOI `10.1090/memo/1104`: ordinary-cover paragraph p. 4 and
   complete exceptional multiplier list in Chapter 5, Table 1, p. 35,
   freshly reread at https://arxiv.org/pdf/1211.6350v2 . No exception
   lies in the new theorem's rank/odd-field range.

D-HOS-01–02 had already received a complete independent review in this
run; their statements and invoked portions were reread here. The present
event does not claim another fresh independent reconstruction of every
line of those two earlier lemmas or of the general polarized Shapiro
bridge.
