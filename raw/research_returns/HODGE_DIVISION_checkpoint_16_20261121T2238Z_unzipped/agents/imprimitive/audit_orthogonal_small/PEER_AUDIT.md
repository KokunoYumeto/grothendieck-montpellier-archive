# Independent whole-proof audit: D-OSM-01–04

**Verdict: PASS, with the ninth-family hypotheses retained exactly.**

Reviewer: `/root/imprimitive`, GPT-6 Astra Pro, inherited effort not exposed,
HODGE_DIVISION. Actual final clock reading: **2026-11-21 20:15:28 UTC**.

The entire frozen root proof `research/orthogonal_small_section.tex`
was read, SHA-256
`44c6d392c14925b173191439b3668d3b75e42f1358bad411749033e92b842d21`.
The bibliography SHA-256 is
`7401537dc18dad4b38297cabdda235684a1553ec35b2f3b238eebfe966f27650`.
The complete root GAP exporter and spectrum probe, Python checker and
their relevant outputs were read. No author's files were edited.

## Mathematical proof review

### Complete finite inputs and central covers

All fifteen inputs are complete ordinary tables. For each core, all
nonlinear rows are retained, including every nonfaithful central
character. Thus central quotients of the universal perfect cover are
included. This is particularly necessary for `Spin_8^+(3)`, whose
noncyclic center cannot act faithfully in an irreducible complex
representation; no such faithfulness is assumed.

The complete exceptional-multiplier list in HHM Chapter 5, Table 1,
p. 35, contains the exceptional `Omega_7(3)` case. The exact official
multiplier and outer metadata identify the sixfold cover there, the
fourfold `Spin_8^+(3)` cover, and every other displayed universal
cover. The interpretation of those strings was freshly read in the
official CTblLib manual §3.7-3. The six core/outer class fusions are
consistent with genuine nontrivial outer actions, not central products.

### Full normalizers

For the six order-two outer cases, a compatible normalizer induces an
automorphism of the represented central quotient, which lifts to the
universal perfect cover. A lift trivial on the simple quotient is
trivial by perfectness. Choose an element of the retained extension
inducing the same full automorphism, including any necessary inner
component. The intertwiner's square differs from the required core
square by a scalar; rescaling it solves that exact relation and gives
an irreducible extension of the core representation. Hence the complete
retained extension rows cover the operator up to scalar, which preserves
projective support. This argument also handles a nonsplit square
relation and does not identify character tables of arbitrary isoclinic
groups.

For the two natural-dimension-eight groups over F3, their core support
ratios exceed `2/5`. A nontrivial commutator of a nonscalar normalizer
with a core element either has that moving-rank bound or is a
nonidentity scalar and has full moving rank. The rank-commutator
inequality therefore gives `1/5` for every compatible outer action.
This handles the whole S4 outer group of the plus type without needing
a table for its full extension. The same argument gives `13/82` for
`2.O9(3)`, improved to `1/4` on its two nonselfdual rows.

### Tensor products and actual period rank

For factor-preserving operators the normalized eigenspace distribution
is a convolution. For a nontrivial factor cycle, scalar-normalized
finite order makes the return operator diagonalizable; cyclic word
orbits give at least one-quarter support. Genuine nonidentity scalar
inertias have full ordinary moving rank. Thus the eight-family mixed
statement has the uniform `1/5` bound with no transitivity or
self-duality premise.

The actual polarized intermediate-cover identity is used with its
already proved larger-inducing-field scope. Genus at least two is
impossible at the displayed degree floors; genus one has at most six
effective branches and period dimension at most six. Rank nine would
force genus zero, at least twelve genuine inertias, and moving sum
`2e+6`. The common fifth bound forces `e<=15`, contrary to the
smallest allowed degree 27. This is a necessary period-rank obstruction;
it does not infer dominance from the size of a parameter space.

### The ninth family

Transitivity preserves self-duality under the factor automorphisms and
therefore makes all `Omega_9(3)` factors fall in one of the two cases.
If they are nonselfdual, the full-normalizer quarter bound forces
`e<=6`, whereas their degrees are much larger.

If they are selfdual, the tensor product of their unique invariant form
lines is the unique form line for the irreducible core. The full inducing
image consequently acts by a multiplier. That multiplier must be
nontrivial: if it were trivial the inducing representation would be
selfdual, and finite-group induction would make the original
representation selfdual. The hypothesis that the original is
nonselfdual is therefore used at the correct point. Product one and
generation force at least two nontrivial multiplier inertias. Their
fixed spaces are totally isotropic, each costing at least `e/2`.
The other ten cost at least `13e/82`. The exact result
`e<=41/4<780` is correct. No statement about arbitrary intransitive
mixed cores involving this ninth family is justified or asserted.

## Independent executed arithmetic

Input SHA-256:
`5236207618c2564af7ed4871c0f92a667664255d2e60be87f037257356669b79`.

`independent_check.py` reuses only this auditor's previously reviewed
cyclotomic-polynomial engine. It imports neither the root's Ramanujan
arithmetic, selected-row list nor result file. Every spectrum is
reconstructed in an exact polynomial quotient by a cyclotomic
polynomial. Indicators and restriction norms are computed by a complete
Galois polynomial substitution, providing an arithmetic route distinct
from the root's normalized Ramanujan trace.

**Actual execution: PASS, 39.612917 seconds.**

| Quantity | Independently checked |
|---|---:|
| Complete ordinary tables | 15 |
| Selected nonlinear/core-compatible rows | 2938 |
| Nonscalar full spectra | 778260 |
| Frobenius–Schur indicators, including linear rows | 3141 |
| Normal fusions | 6 |
| Distinct cached exact Fourier problems | 241074 |

Every spectrum has nonnegative integral multiplicities with the right
degree sum. Power-map orders and compatibilities, full class unions,
the identity fusion kernel, degree-square sums, class-size sums and
all restriction norms were checked. Each selected extension row is
verified pointwise against its unique core row. Every displayed minimum
ratio and minimum degree agrees with the proof.

The two nonselfdual rows of `2.O9(3)` are independently recovered as
224 and 225, both degree 838656 and minimum support ratio `1/2`.
All its other indicators are `+1`. The additional `check_metadata.py`
also passes: it checks all nine multiplier/outer records, six genuine
outer fusions and all fifteen freshly read official class counts.

Code SHA-256:
`6af956f44ac1ea8517dcefbc9a646039c277d37da14008c892cb2cfc07d239f7`.
Output SHA-256:
`abacbd8741adf56adaa3049bce4922dd00f6997353460601f483530f60d5ec05`.
All per-row minimum witnesses and per-table full-spectrum hashes are
retained in `independent_checked.json`.

The root's GAP full orthogonality computation is recorded as completed
in its export log, which was read through `ORTHOGONAL EXPORT COMPLETE`.
This audit does not claim to have independently rerun all pairwise
GAP orthogonality computations or to have reconstructed the original
group-theoretic table constructions.

## Fresh primary-data reads and provenance boundary

All fifteen complete official CTblLib information pages were freshly
opened and read; URLs and exact retained provenance are in
`source_log.json`. The official manual §3.7-3 through §3.7-6 was also
freshly read at:
https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/doc/chap3.html .

The source distinctions are accurate:

- The `6.O7(3)` pair, `O8-(2)` pair and both `O10±(2)` pairs
  have ATLAS provenance. The centerless even-field outer pages explicitly
  identify full automorphism groups.
- `2^2.O8+(3)` records the `PossibleCharacterTablesOfTypeV4G`
  construction. The accepted specific official table is the premise;
  no new uniqueness theorem for that general construction is claimed.
- `2.O8-(3)` and `2.O9(3)` are attributed to Max Neunhöffer,
  April 2008.
- Both `O12±(2)` cores record Magma V2.23-9 computations on
  4 September 2018. The plus outer table is attributed to J. S. Frame
  (1986), with Aachen technical support; the minus outer table to
  J. S. Frame and H. Pahlings (1987), through the CAS library.

The generated webpages display library version 1.3.10; the actual
retained mathematical export records CTblLib 1.3.11 with GAP 4.16.1.
No collective ATLAS attribution or independently proved provenance is
substituted for these exact source statements. No new cycle-supplier
existence or motivic conclusion is asserted by this finite-core audit.
