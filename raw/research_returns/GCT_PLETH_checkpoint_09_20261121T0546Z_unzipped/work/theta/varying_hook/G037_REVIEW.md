# Independent whole-proof review of G037

Reviewed 2026-11-21 by GPT-6 Astra Pro; effort setting not surfaced.

**Result: PASS.** I read the complete `work/root/stable_hook_report.md`,
(HK.1)–(HK.19) and every following section, and the complete
`work/root/stable_hook_positive.py`. This review is separate from the
root agent's 4872 module comparisons, 238 original plethysms and
polytope witnesses; I do not claim a second execution of those checks.

## Exact modules and differentials

The stable chart gives the stated hook tail and determinant sign. Its
first partition gap is nonnegative even at
\(a=1,r=m-2,n=a+t\). The Koszul multiplication differential and
exterior derivative satisfy the total-degree homotopy identity, so all
positive-degree exactness assertions have an actual contracting map.
In the exterior Pieri decomposition, the displayed highest vector is
of the first shape and has a nonzero differential. The second shape
does not occur in the target. This proves the exact hook Young-image
identification, including the full-column endpoint and \(r=0\).

The cycle determinant in (HK.7) and Macdonald's super principal
specialization give the stated multiplicity series. Cell \((1,1)\)
cancels its literal exterior trivial-line factor, and after total-degree
regrading cell \((2,1)\) cancels the Koszul factor \(1+u\).
The identity expressing each minimum exponent as a sum of nonnegative
cell quantities is correct, so negative contents introduce no negative
numerator degrees. Repeated weights retain distinct subset labels.

For the invariant component, Solomon's differential basis, the
invariant dot form and Euler's scalar division give the actual Koszul
complex on \(e_2,\ldots,e_m\). In each multidegree, changing from
\(v_j\) to \(v_i,v_j-v_i\) identifies the kernel with the indicated
exterior algebra. The wedge expression in (HK.14) is polynomial:
every surviving denominator occurs at most once. Least support and
subset choices are unique, proving the displayed positive basis count.

## Polytope inverses and support

The tableau assignment constraints enforce exactly a standard Young
tableau. The two descent inequalities give a unique descent bit in
both weak-upward and strictly-downward cases. The cell bits select
exactly \(r\) distinct retained cells. The degree equation and the
stated coin bounds count precisely the coefficient of (HK.12).
There are \(m^2+3m-4\) variables. In the trivial branch the unique
\(z_i\) fixes the least positive exponent, all lower exponents
vanish, the selected \(y\)-indices lie strictly above it, and the
positive exponent requirements are exact. Conversely a basis vector
fixes all variables. This proves the single-polytope assertion, with
\(3m-3\) variables in that branch.

The support proof's lowest fake-degree coefficient and next coefficient
agree with the hook product. For a non-row rectangle the retained
content weights occupy a consecutive interval. When there is a
nonempty proper subset, the sorted-cut argument always supplies a
one-unit increase, including a cut through repeated weights or at the
largest weight. The exceptional \(r=0,m-2\) subsets have only one
sum. The one-retained-cell case \(m=3\) has no interior subset and
therefore agrees with the same endpoint statement. The trivial branch
has the stated minimum; the next degree exists unless the tag uses
all invariant generators. Coin weights two and three fill every later
degree. Thus (HK.2) and (HK.3) cover every endpoint.

## Evaluation, encoding and implementation

The q-hook truncation and elementary-polynomial computation have
polynomial degree and coefficient size in \(m\). The exact rational
parity identity remains valid even when a term in (HK.15) has numerator
degree equal to denominator degree; the implementation does not impose
an incorrect proper-fraction requirement. Denominator roots remain
roots of unity under the iteration, and each numerator multiplication
adds only polynomially many bits. This proves the claimed bit bound.

The explicit/unary outer-degree convention, and the ordinary
binary-part guarantee when \(t\ge1\), are stated accurately.
The complete sparse-matrix implementation has the same signs,
cardinality constraints, bounds and physical determinant twist as the
proof. No input-dependent character table or elimination enters its
formula generator. No unresolved mathematical or encoding gap was
found.
