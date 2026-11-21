# The first unstable hook order in every outer degree

## T-061. An exact evaluation kernel and a positive deleted-point formula

Let \(m\ge4\), \(a\ge2\), \(0\le r\le m-2\), \(t\ge0\), and
\(\mu\vdash m\), with
\[
(m-2)a\ge m+r.
\]
Put
\[
\begin{aligned}
n&=a+t-1,\\
\lambda&=((m-1)a+t-m-r,a+t,(t+1)^r,t^{m-2-r}),\\
D&=a+r,\qquad
\nu=\begin{cases}\mu,&t\text{ even},\\\mu',&t\text{ odd}.
\end{cases}
\end{aligned}
\tag{UH.1}
\]
These are precisely the valid hook-tail parameters of ideal order one:
\(\lambda_2-n=1\). Set \(q=m-1-r\), and let
\[
\mathcal T_{m,r}=
\{(q+1,1^r),(q,1^{r+1})\}
\ \cup\ \{(q,2,1^{r-1}):r\ge1,\ q\ge2\}.
\tag{UH.2}
\]
The displayed partitions are distinct; the last term is included only
under its stated conditions. Let \(c_{m,a,r}(\nu)\) be the complete
stable-hook coefficient of G037, namely
\([\,[\nu]:S_{(a,1^r)}\mathfrak h_m\,]\).

Then the exact formula is
\[
\boxed{
p_{\mu,(n)}^\lambda
=c_{m,a,r}(\nu)-\mathbf1_{\nu\in\mathcal T_{m,r}}.}
\tag{UH.3}
\]
The subtraction has an explicit positive realization. At \(a=2\),
the coefficient is one for
\(\nu=(m-r-2,2,1^r)\) and zero otherwise. At \(a\ge3\), an
unaffected label uses G037's single polytope. For an affected label,
§4 specifies one actual lattice point of that polytope and §5 partitions
its complement into disjoint bounded polytopes. There are at most
\(2(m^2+3m-4)\) selected pieces, with at most \(m^2+3m-4\)
variables each. All matrices and the removed point are constructed
in polynomial time in \(m\) and the binary parameter lengths.
The exact coefficient and its nonvanishing are computed in the same
polynomial bit bound by G037 and (UH.3).

As in G037, ordinary binary-part input bounds follow when \(t\ge1\),
because the output then has \(m\) positive parts. At \(t=0\),
the polynomial bound in \(m\) is asserted for explicit/unary outer
degree, without a bound polynomial in a compressed \(\log m\) input.

## 1. The actual first-order section module

Let \(E=\mathfrak h_m\), of dimension \(m-1\), with its rational
invariant dot form. Let \(v_i=e_i-m^{-1}\mathbf1\), and
\(Z=\{[v_1],\ldots,[v_m]\}\subset\mathbb P(E)\).
Every \(m-1\) of these vectors form a basis and their sole relation
is \(\sum_i v_i=0\). Write \(Q\) for the tautological quotient
on \(\mathbb P(E)\).

The exact flag vanishing model G015 gives, after the full determinant
factor is removed,
\[
(S_\lambda\mathbb Q^m)_{(n^m)}
\simeq\operatorname{sgn}^{t}\otimes
H^0\bigl(\mathbb P(E),\mathcal I_Z\otimes
\mathcal O(a)\otimes\Lambda^rQ^*\bigr).
\tag{UH.4}
\]
Here \(\mathcal O(a)\Lambda^rQ^*=\Omega^r(a+r)\).
To specify the pushforward from the full flag, trivialize \(Q\)
on an affine base chart. The remaining flag factor has the exterior
Young line of weight \((1^r)\), whose sections are \(\Lambda^rQ^*\)
by the exact Borel–Weil/Plücker map used in G015. The Čech maps
on this product chart are scalar maps over \(\mathbb Q\); tensoring
them with the base ideal module is exact over that field. Their
degree-zero kernel therefore gives precisely the sheaf in (UH.4).
These local comparisons glue. No flatness of the point ideal is assumed.

The Euler inclusion of \(\Omega^r(a+r)\) into
\(\mathcal O(a)\otimes\Lambda^rE^*\) identifies its sections
with G037's actual Koszul kernel \((Z_r)_D\). Its point evaluation is
\[
\operatorname{ev}_a:S_{(a,1^r)}E^*\longrightarrow
\bigoplus_{i=1}^m\Lambda^r\operatorname{ann}(v_i),
\qquad F\longmapsto(F(v_i))_i.
\tag{UH.5}
\]
The values lie in the displayed annihilator because the Euler
contraction of \(F\) is zero. The fiber line is trivialized by the
specified affine vector \(v_i\), so literal permutations introduce
no additional scalar. The form identifies all duals equivariantly.
Consequently the right side is
\[
T_{m,r}=\operatorname{Ind}_{S_{m-1}}^{S_m}
\Lambda^r\mathfrak h_{m-1},
\tag{UH.6}
\]
and (UH.4) is exactly \(\operatorname{sgn}^t\otimes\ker\operatorname{ev}_a\).

## 2. Surjectivity, including the smallest degree

First let \(a\ge3\). Write \(z_i\) for the centered coordinate
function and \(s_2=\sum_jz_j^2\). Define
\[
p_i=\frac{m}{m-2}z_i^2-
\frac{s_2}{(m-2)(m-1)},\qquad
\ell_i=\frac{m}{m-1}z_i.
\tag{UH.7}
\]
Direct substitution gives \(p_i(v_j)=\delta_{ij}\) and
\(\ell_i(v_i)=1\). For
\(\phi_i\in\Lambda^r\operatorname{ann}(v_i)\), put
\[
s_i(\phi_i)=p_i\ell_i^{a-3}\,
\iota_z(\ell_i\wedge\phi_i).
\tag{UH.8}
\]
This is a polynomial horizontal \(r\)-form of coefficient degree
\(2+(a-3)+1=a\), since \(\iota_z^2=0\). Its value is
\(\phi_i\) at \(v_i\) and zero at every other point.
The sum of these maps is an actual rational equivariant right inverse
to (UH.5): the coordinate formulas and affine frame are permuted
literally. This proves surjectivity for every \(r\) at \(a\ge3\).

At \(a=2\), consider the map into the same evaluation target from
\(E^*\otimes\Lambda^{r+1}E^*\), sending
\(l\otimes\theta\) to the values of \(l\iota_z\theta\).
Its adjoint under the natural perfect pairings is
\[
(\psi_i)_i\longmapsto
\sum_{i=1}^m v_i\otimes(v_i\wedge\psi_i),
\qquad\psi_i\in\Lambda^r(E/\mathbb Qv_i).
\tag{UH.9}
\]
The wedge is well defined and injective on each quotient exterior
power. Because the kernel of \(\mathbb Q^m\to E\),
\(e_i\mapsto v_i\), is the constant line, a tuple in (UH.9)'s
kernel has \(v_i\wedge\psi_i=\eta\) independent of \(i\).
Thus
\[
\eta\in\bigcap_i\bigl(v_i\wedge\Lambda^rE\bigr)
\subseteq\Lambda^{r+1}E.
\]
Choose any \(m-1\) frame vectors as a basis. A wedge lying in every
one of their principal exterior ideals must contain every basis
vector. It is zero when \(r+1<m-1\). Therefore (UH.9) is injective
for \(r\le m-3\), and evaluation is surjective in that range.
The validity inequality at \(a=2\) gives \(r\le m-4\), so this
includes every declared degree-two parameter.

For precision, at the excluded endpoint \(a=2,r=m-2\), the
intersection is \(\det E\), and the cokernel has the sign character
and dimension one. Thus the surjectivity bound was not extended
past the proved degree range. At \(a=1\) no parameter satisfies
the first-gap inequality in (UH.1).

The adjoint proof also specifies a rational splitting at \(a=2\):
if \(B\) is the map just used, take invariant positive dot forms and
use \(B^*(BB^*)^{-1}\), followed by \(l\otimes\theta\mapsto
l\iota_z\theta\). The surjectivity proof makes the Gram inverse
well defined. Together with (UH.8), this supplies actual splittings
at every valid parameter, not only a character comparison.

## 3. The at-most-three correction labels and the degree-two value

The exterior representation in (UH.6) is the hook
\([(m-1-r,1^r)]\) of \(S_{m-1}\). Inducing one box gives exactly
the addable-box partitions in (UH.2), each once. This is the usual
Frobenius induction product followed by the one-box Pieri identity:
Macdonald I§7(7.1)–(7.3), pp112–113, and I§5(5.16), p73.
The coset map and rational Young projections give the corresponding
actual module decomposition. The exact surjection (UH.5) consequently
proves (UH.3), including every outer determinant twist.

At \(a=2\), first remove the determinant shift \(t\) through
the perfect exterior-column map of T005. The inner degree becomes
one and the output becomes
\[
\lambda^0=(m-r-2,2,1^r,0^{m-r-2}).
\]
Its nonzero entries form a partition precisely because \(r\le m-4\).
The actual tensor-word/Young construction gives
\(S_\mu(\operatorname{Sym}^1V)=S_\mu V\); the determinant
shift has already changed the effective outer label to \(\nu\).
Thus the coefficient is exactly the indicator stated after (UH.3).
Equivalently, the evaluation kernel is the single Specht type
\([(m-r-2,2,1^r)]\), with its rational Young inclusion. This
also agrees with the degree-two evaluation splitting just proved.

## 4. A specified stable-hook lattice point to remove

Assume \(a\ge3\) and \(\nu\in\mathcal T_{m,r}\). We construct
one point of G037's actual polytope. The construction is polynomial
in \(m\) and the binary degree, and includes its smallest cases.

For a non-row \(\nu\), let \(T_0\) be the row-superstandard
tableau, with consecutive labels in successive rows. Its comajor
degree is \(b(\nu)\). Choose the \(r\) smallest retained cell
weights \(w(i,j)=j-i+1\), breaking ties lexicographically.
This gives the minimum degree \(L\) from G037. For the two hook
labels in (UH.2) the minima are respectively \(r+2\) and
\(r+1\); for the third label the minimum is \(r+2\).
The row label occurs only at \(r=0\) and is treated below.

If \(D-L\ne1\), it is nonnegative and, in these parameters,
at least two. Represent it by coins two and three: take one coin
three when it is odd, and fill the remainder with coins two.
The tableau, subset and coins give the required point.

The remaining case is \(a=3\) for a label with \(L=r+2\).
The following changes increase the numerator degree by exactly one:

| Effective label | Change from the minimum tableau/subset |
|---|---|
| \((q+1,1^r)\), \(r\ge1\) | Swap the entries at \((1,q+1)\) and \((2,1)\). |
| \((q,2,1^{r-1})\), \(r\ge2\) | Swap the entries at \((2,2)\) and \((3,1)\). |
| \((q,2)\), \(q\ge3\) | Use first row \(1,\ldots,q-1,q+2\), second row \(q,q+1\). |
| \((2,2)\) | Keep \(T_0\) and choose retained cell \((1,2)\) instead of \((2,2)\). |

Each displayed tableau remains standard. In the first two rows of
the table, the affected descent moves one step earlier and the
remaining descents are unchanged, increasing comajor by one. In
the third row the sole descent moves from \(q\) to \(q-1\).
In the last row the chosen weight increases from one to two.
Thus the total degree becomes exactly \(D\), with no coins needed.

For the row label \(\nu=(m)\), one has \(r=0\) and \(D=a\ge3\).
Represent \(D\) using coins two and three as above, set the single
least-support bit to the first positive exponent, and set every
subset bit to zero. This gives exactly one point of (HK.19).

Finally fill every assignment bit, descent bit, subset bit and coin
coordinate with the values just specified. The construction fixes
every variable. These formulas give the function
`canonical_removed_point` in the executable; its result is checked
against the literal G037 matrices.

## 5. Positive disjoint cells and the executable formula

Let \(P\) be the relevant stable-hook polytope in its given order of
\(N\le m^2+3m-4\) coordinates, and let \(v\in P\cap\mathbb Z^N\)
be the point just constructed. For each \(j=1,\ldots,N\), use two
copies of the original constraints, adding
\[
x_i=v_i\quad(i<j),\qquad
x_j\le v_j-1
\quad\text{or}\quad x_j\ge v_j+1.
\tag{UH.10}
\]
These are bounded rational polytopes. Their lattice sets are disjoint:
the tag records the first coordinate at which a point differs from
\(v\), and the sign of that difference. Conversely every integer
point of \(P\setminus\{v\}\) has exactly this tag. Thus their
total lattice count is the original stable coefficient minus one.
Together with the actual evaluation splitting, this proves the
positive formula for its kernel. No rank calculation remains.

An unaffected label uses \(P\) itself. The degree-two indicator is
the zero-dimensional one-point polytope or the empty union. The
program `first_unstable_hook_positive.py` exports every literal matrix,
the original parameters, its effective label, and the removed point.
Its exact coefficient routine calls G037's proved binary-degree
evaluator and removes the specified target multiplicity. This is
polynomial bit computation, and (UH.10) is a positive polynomial-size
description of the same value.

## 6. Scheme and K0 transport, endpoints and scope

The original comparison is G015's coordinate map and polynomial
extension criterion with \(k=1\), retaining the determinant line.
The projective pushforward in (UH.4), the Euler inclusion and the
point restriction are actual maps of coherent sheaves. The rational
right inverses (UH.8)–(UH.9) induce the finite-group module splitting
whose covariant rank is computed by (UH.3). The kernels and images
therefore carry the same Schur-operation class through the established
SGA3 I4.5/4.7.2–4.7.3, SGA6 VI3.3 and SGA6 V4.2,4.4,4.8–4.9
dictionaries, with the archive-cote133 tensor/Young comparison A012.
The explicit affine/projective constructions use the EGA locators
already checked for G015. All maps are rational and spread after
their finite denominators are inverted; the multiplicity statement
is on the characteristic-zero generic fiber.

The valid small parameters are exhausted: \(a=1\) is impossible;
\(a=2\) is exactly \(r\le m-4\); every \(a\ge3\) is valid
for every \(r\le m-2\). The last assertion follows from
\((m-2)3-m-r\ge m-4\ge0\). Thus the first unstable hook order
has a complete positive formula in varying outer degree, hook length
and outer label. Higher ideal orders remain a separate explicit
section problem.

## 7. Executed checks and review status

The author and the root agent have each read the entire proof, including
all degree-two endpoints, the explicit right inverse, the four
numerator-degree adjustments and the literal first-difference cells.
Both readings passed. The archive's complete independent proof audit
also passed, with its receipt
`work/archive/FIRST_UNSTABLE_HOOK_INDEPENDENT_RECEIPT.json`.

The reproducible script `check_first_unstable_hook.py` passed 9,336
coefficient comparisons in both determinant parities for every label
at \(m=4,\ldots,8\), every allowed \(r\), and \(a=2,\ldots,15\).
Its comparison side uses original cycle traces, hook Jacobi–Trudi,
and literal fixed-point induction, without a content polynomial or
the three-label formula. All 3,162 specified removed points passed
the original stable-polytope matrices for \(m=4,\ldots,20\), every
\(r\), and the six degrees \(3,4,5,6,10,10^{20}+1\).

For \(m=4,5\), 129 positive-degree cases produced 3,012 literal
polytopes. All 212 original integer witnesses belonged to exactly
one retained cell or were the unique removed point, leaving 161
retained witnesses with the asserted coefficient. The 19 valid
degree-two cases also passed their zero-dimensional formula. The
full receipt is `FIRST_UNSTABLE_HOOK_RECEIPT.json`.

The archive independently performed exact rational elimination on
25 adjoint evaluation matrices for \(m=4,\ldots,8\), including the
five excluded top sign cokernels, and checked 15 valid degree-two
kernel dimensions. Its separate tableau/coin enumeration verified
120 deleted-point cases, 8,832 exported matrices, 549 original and
429 retained points, and 81 large-degree or extreme-leg points.
The rectangular agent independently compared 496 original plethysm
coefficients at \(m=4,5,6\), \(a=2,3,4\), every valid leg, and both
determinant parities, using Schur cycle traces and literal deleted-point
induction; all passed. That receipt is
`work/rectangular/FIRST_UNSTABLE_HOOK_MN_CHECK.tsv`.

Whole-proof readings and finite comparisons have separate ledger
events. The executable formula does not use a general plethysm
oracle or an input-sized evaluation-matrix inverse.
