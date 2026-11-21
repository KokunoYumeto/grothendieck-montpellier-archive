# A-077. Exact singleton counterexample and corrected formulas T-057

**Status: the enlarged RT.5 candidate is refuted; the stated corrected
formulas are proved and pass independent review.** Reviewer:
GPT-6 Astra Pro; effort not exposed; run /root/archive_audit.
The entire `rank_three_trace_review.md`, RT.1–RT.8 and all four
sections, was read. Its G034 triple/routing review agrees with
the full independent review A-074. This record concerns the
new singleton counterexample and the two precise refinements.

The actual singleton projection removes a horizontal strip from
$(a+c,b+c,c)$, giving the finite sum over
$i+j+l<k$, $i\le x$, $j\le b$, $l\le c$ of
$S_{(a+c-i,b+c-j,c-l)}V$, where $\dim V=3$.
These inequalities are exactly the interlacing inequalities:
the first two lower bounds are $a+c-i\ge b+c$ and
$b+c-j\ge c$, and the last is $c-l\ge0$.
This fixes the actual representation to which all comparisons refer.

The proposed expression RT.5 discards the $j\le b$ boundary
after removing $\det(V)^{c-l}$ from every formal summand.
At $(k,c,b,x)=(5,8,2,0)$ the actual three-row sum has
dimension 210, while that expression has dimension 220.
The full determinant at $(i,j,l)=(0,4,0)$ is

$$
s_{(10,6,8)}(V)=-s_{(10,7,7)}(V),
$$

because its shifted alternant rows $(12,7,8)$ require one
transposition. The latter partition has dimension 10.
After the invalid determinant removal, the two-row polynomial
determinant would be $s_{(2,-2)}=0$ under $h_j=0$ for
negative $j$, losing exactly the negative ten. This supplies
a precise counterexample and identifies the failed map step.

The independent calculation uses the literal horizontal-strip
sum and the rank-three Weyl dimension formula
$(p-q+1)(p-r+2)(q-r+1)/2$, compared with the proposed
two-row determinant
$h_ph_q-h_{p+1}h_{q-1}$, $h_j=\binom{j+2}{2}$ for
$j\ge0$ and zero otherwise. It reproduces all three examples:

| $(k,c,b,x)$ | Actual singleton | Rejected expression |
|---|---:|---:|
| $(5,8,2,0)$ | 210 | 220 |
| $(5,8,2,1)$ | 525 | 540 |
| $(6,9,3,0)$ | 560 | 575 |

The exact executed receipt is
`GENERIC_SINGLETON_COUNTEREXAMPLE_RECEIPT.json`. These values refute
only that extension of RT.5; they do not assert an obstruction
to a different formula.

For $0\le c<k$ and $b+c\ge2k$, one has $b\ge k+1$.
Consequently $j\le b$ is automatic in the simplex.
Remove the full-height columns first on the actual Pieri branches.
For each fixed $l$, the two remaining parts are
$a+l-i$ and $b+l-j$. Their second part is at least
$b-k+1+2l\ge2$. The involution
$(i,j)\mapsto(x+j+1,i-x-1)$ then removes $i\le x$
by the exact two-row determinant sign change. Every part
through this operation stays within the declared polynomial
range before straightening. Thus RT.5 is valid on this
entire smaller domain through the specified Pieri and
exterior-column maps.

For $c\ge k$, retain the full three-row determinant.
The exact identity
$h_n(V\oplus u)=\sum_{j\ge0}h_{n-j}(V)u^j$
and row multilinearity expand the Schur determinant into
the unrestricted $(i,j,l)$ simplex at total degree below
$k$. The actual line-branching projector identifies those
coefficients with the horizontal-strip sum. Since
$l<k\le c$, no extra third-row truncation enters.
This proves RT.8, including the initial endpoints, while
retaining the negative straightened terms which the rejected
expression loses.

The refined statements are therefore T057/RT.5 on $c<k$
and T057/RT.7–RT.8 on $c\ge k$. Each is an unconditional
identity on its stated range with the actual maps specified.
