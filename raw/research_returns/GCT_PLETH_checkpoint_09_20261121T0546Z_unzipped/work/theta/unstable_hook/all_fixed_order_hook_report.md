# Every hook tail at fixed ideal order

## T-067. A complete varying-outer-degree positive formula

Let
\[
m\ge4,\quad k\ge1,\quad a\ge1,\quad t\ge0,
\quad0\le r\le m-2,\quad(m-2)a\ge mk+r,
\quad\mu\vdash m.
\tag{AF.1}
\]
Put
\[
n=a+t-k,\qquad
\lambda=((m-1)a+t-mk-r,a+t,(t+1)^r,t^{m-2-r}),
\tag{AF.2}
\]
and let \(\nu=\mu\) for even \(t\), \(\nu=\mu'\) for odd
\(t\). Condition (AF.1) implies \(a\ge k+1\), so \(n\ge1\),
and is exactly the first-row partition inequality in (AF.2).

There is an explicit positive bounded-polytope formula for every
\(p_{\mu,(n)}^\lambda\) in this entire range. Put
\[
D_k=\sum_{p=0}^{k-1}
\left\{\begin{matrix}k-1\\p\end{matrix}\right\}
2^p(p+1)!.
\tag{AF.3}
\]
The formula has at most
\[
1+D_k\bigl(2(m^2+3m-4)-1\bigr)
\tag{AF.4}
\]
disjoint pieces, each in at most \(m^2+3m-4\) variables.
Every constraint, finite tag and removed point is specified below
and exported by `all_fixed_order_hook_positive.py`.

Exact coefficient evaluation and nonvanishing take
\(f(k)\operatorname{poly}(m+\text{input bit length})\) time.
Generating all positive matrices takes
\[
f(k)(m+k+1)^{2k+O(1)}
\operatorname{poly}(\text{input bit length}).
\tag{AF.5}
\]
Here \(f\) is an explicitly computable function of the ideal
order, supplied by the finite loops in §§3–5. In particular both
are polynomial bounds for every fixed \(k\). For ordinary
binary-part input, the polynomial-size counting interpretation
uses \(t\ge1\), which lists all \(m\) positive output parts,
or an explicit/unary outer-degree parameter. No polynomial-time
assertion in a binary-compressed \(m\), or uniform polynomial
bound in \(k\), is imposed.

The stable range \(n\ge a+t\) is the complete G037 family.
The present statement covers every positive ideal order
\(k=a+t-n\) for the same hook tail. It contains T064–T066,
including every endpoint, by the exact comparisons below.

### 1. The fixed complex and its concentration

Write \(E=\mathfrak h_m\), \(R=m-2\), \(F=\mathbf Q^R\),
and
\[
\alpha=(a^{R-r},(a-1)^r),\qquad
N=|\alpha|=(m-2)a-r\ge mk.
\tag{AF.6}
\]
Use G027's literal frame ideals \(I_i=(\ell_i\otimes F)\)
in \(\operatorname{Sym}(E\otimes F)\), its exact signed
restriction complex FA.4 in degree \(N\), and its actual
balanced-flag map FA.6. Applying the exact \(S_\alpha F\)
multiplicity functor retains every differential and its
\(S_m\)-action. The balanced module is the kernel tensored
by \(\operatorname{sgn}^{a+t}\). T049 gives the actual
diagonal-quotient realization of this kernel, in all degrees.

For a selected subset of size \(q\), the stabilizer is
\(S_q\times S_{m-q}\), and the residual vector space is
\(W=\mathfrak h_{m-q}\), of dimension \(d=m-q-1\).
The normal factor is
\[
T_k(F)^{\otimes q},\qquad
T_k(F)=\bigoplus_{u=0}^{k-1}\operatorname{Sym}^uF.
\tag{AF.7}
\]
Its Schur labels \(\rho\) have at most \(q\) rows and size
at most \(q(k-1)\). The residual factor is
\(S_{\alpha/\rho}W\).

The column argument PB.7 proves that a nonzero residual factor
requires \(\rho_i\ge\alpha_{i+d}\) for \(1\le i\le q-1\).
Consequently
\[
q(k-1)\ge|\rho|\ge(q-1)(a-1),\qquad
q\le Q:=\min\left\{m-2,\left\lfloor\frac{a-1}{a-k}\right\rfloor\right\}
\le k.
\tag{AF.8}
\]
The last inequality follows from \(a\ge k+1\); it also holds
at \(k=1\), when the fraction is one. Thus every term after
the first \(k\) selected-subset terms is zero in the actual
complex. This statement includes the selected-subset orientation;
it is not an unsigned replacement of that complex.

### 2. The exact complementary hook and its two components

Fix the invariant direct sum
\(E=P\oplus W\) of FA.13, where \(P\) has ordered basis
the selected \(\ell_i\)'s and dimension \(q\). Put
\(\beta=(a,1^r)\). The full width-\(a\) exterior-column
pairing is a nondegenerate rational equivariant pairing
\[
S_\alpha E\otimes S_\beta E\longrightarrow(\det E)^a.
\tag{AF.9}
\]
Restrict it to \(GL(P)\times GL(W)\). For a normal partition
\(\rho\subset(a^q)\), padded to length \(q\), the paired
normal partition is
\[
\gamma=(a-\rho_q,\ldots,a-\rho_1).
\tag{AF.10}
\]
This follows from the perfect pairing
\(S_\rho P\otimes S_\gamma P\to(\det P)^a\).
Contract that pairing out of (AF.9). The remaining pairing on
the multiplicity spaces is nondegenerate, since the full pairing
is nondegenerate and distinct normal highest types pair only with
their complementary types. It supplies the actual map
\[
S_{\alpha/\rho}W\simeq
(\det W)^a\otimes S_{\beta/\gamma}W^*.
\tag{AF.11}
\]
The rational normalization is fixed by sending ordered exterior
top wedges to the chosen determinant basis. This construction
commutes with the selected coordinate permutations. Their action
stays entirely in the normal multiplicity space.

Since \(|\rho|\le q(k-1)<qa\), the complement \(\gamma\)
is nonempty. For it to lie in the hook \(\beta\), it must have
the form \((a-A,1^s)\), with
\(0\le s\le\min(q-1,r)\). Its residual skew diagram consists
of one row of length \(A\) and one column of length \(r-s\),
with no common row or column. Row symmetrization and column
antisymmetrization therefore act on disjoint sets of tensor slots.
After ordering the row slots first, their normalized Young maps
give the literal tensor isomorphism
\[
S_{\beta/\gamma}W^*
\simeq\operatorname{Sym}^{A}W^*\otimes\Lambda^{r-s}W^*.
\tag{AF.12}
\]
An empty row or column is the scalar factor. The inverse is the
same slot ordering followed by the normalized symmetric and
exterior projections. No mixed row/column relation remains.

Equations (AF.10)–(AF.12) give exactly the finite list
\[
\rho=\rho(q,s,A):=(a^{q-s-1},(a-1)^s,A),
\tag{AF.13}
\]
where zero parts are omitted, and
\[
\begin{gathered}
0\le s\le\min(q-1,r),\quad r-s\le m-q-1,\\
0\le A\le\min\{a-1,\ q(k-1)-(q-1)a+s\}\le k-q.
\end{gathered}
\tag{AF.14}
\]
A negative upper bound gives an empty list. The leg condition is
exactly the condition that the \(a\)-parts of \(\rho\) fit
inside \(\alpha\), as well as the nonzero exterior-power bound.
The last inequality follows by substituting \(a\ge k+1\) and
\(s\le q-1\). It proves that the entire symmetric decoration
has degree at most \(k-q\). These labels have no repetitions:
\(A\le k-q<a-1\), so their final part cannot merge with an
\((a-1)\)-part.

### 3. Bounded normal representations, with actual maps

Define the genuine \(S_q\)-module
\[
M_{q,k,\rho}=
\operatorname{Hom}_{GL_q}
\left(S_\rho\mathbf Q^q, T_k(\mathbf Q^q)^{\otimes q}\right).
\tag{AF.15}
\]
The first group permutes the \(q\) tensor slots. To specify this
space over \(\mathbf Q\), take monomials in \(q\) blocks of
\(q\) variables, with every block degree below \(k\). Retain
total column weight \(\rho\), and impose the raising equations
\(\sum_i y_{ij}\partial_{y_{i,j+1}}=0\), \(1\le j<q\).
Ordered rational row reduction gives a basis and the actual slot
permutation matrices. This is a finite construction of the
highest multiplicity space, not an unspecified representation
oracle.

Using this space in the original rank \(R\ge q\) changes
nothing. Pad \(\rho\) by zeros. A polynomial of that weight
uses only its first \(q\) column variables; all additional
raising equations vanish, and the previous equations are
unchanged. The inclusion is the actual rank-comparison map and
commutes with every slot permutation.

Write
\(M_{q,k,\rho}=\bigoplus_{\eta\vdash q}
m_{q,k,\rho}^{\eta}[\eta]\). These finitely many nonnegative
integers have the following fully evaluated formula. For a cycle
partition \(\xi\vdash q\), put
\[
P_{q,k,\xi}(X)=\prod_{\ell\in\xi}
\left(\sum_{u=0}^{k-1}h_u(X_1^\ell,\ldots,X_q^\ell)\right),
\quad\delta=(q-1,\ldots,0).
\tag{AF.16}
\]
The cyclic tensor trace, followed by multiplication by the Schur
alternant, gives
\[
\operatorname{tr}(\xi\mid M_{q,k,\rho})=
\sum_{\sigma\in S_q}(-1)^\sigma
[X^{\rho+\delta-\sigma\delta}]P_{q,k,\xi}(X),
\qquad
m_{q,k,\rho}^{\eta}=
\sum_{\xi\vdash q}\frac{\chi^\eta(\xi)}{z_\xi}
\operatorname{tr}(\xi\mid M_{q,k,\rho}).
\tag{AF.17}
\]
The first equality holds because only equal monomials around each
slot cycle contribute to its trace, and the alternating coefficient
selects exactly the dominant Schur label \(\rho\). For completeness,
the small character itself is computed by the same alternating
coefficient applied to
\(\prod_{\ell\in\xi}(X_1^\ell+\cdots+X_q^\ell)\), with
target \(\eta\). This is the explicit Frobenius formula, so
there is no character-table oracle. The second equality is the
finite symmetric-group projector on the already constructed
space (AF.15).

All polynomial degrees here are at most \(q(k-1)\), and
\(q\le k\). Every array, permutation sum and rational kernel
in this step is bounded by a computable function of \(k\) alone.
Even a binary-large \(a\) cannot enlarge a normal calculation:
for \(q\ge2\), a surviving term requires \(a\le2k-1\);
for \(q=1\), its normal label is simply \((A)\), \(A<k\).

### 4. Every stabilizer action and coefficient

The selected-subset orientation is \(\operatorname{sgn}_{S_q}\).
The factor in FA.6 restricts as
\(\operatorname{sgn}_{S_q}^{a+t}
\operatorname{sgn}_{S_{m-q}}^{a+t}\).
Equation (AF.11) contributes
\((\det W)^a=\operatorname{sgn}_{S_{m-q}}^a\).
After removing the common \(\operatorname{sgn}^t\), the
actual \(q\)-th nonambient term is consequently
\[
C_q=\bigoplus_{s,A}\operatorname{Ind}_{S_q\times S_{m-q}}^{S_m}
\left[
\operatorname{sgn}_{S_q}^{a+1}M_{q,k,\rho(q,s,A)}
\otimes\operatorname{Sym}^{A}\mathfrak h_{m-q}
\otimes\Lambda^{r-s}\mathfrak h_{m-q}
\right].
\tag{AF.18}
\]
The invariant rational form is the stated map between each
standard module and its dual. The sum is precisely (AF.14).
Thus a small label \(\eta\) in (AF.17) is replaced by
\(\eta'\) when \(a\) is even, and is unchanged when \(a\)
is odd. This accounts for all selected and complementary signs.

The remaining induced multiplicities have a bounded-cell
evaluation. Put \(L=m-q\), \(B=r-s\), and first replace
\(\operatorname{Sym}^{A}\mathfrak h_L\) by its actual split
sequence
\[
0\longrightarrow u\operatorname{Sym}^{A-1}\mathbf Q^L
\longrightarrow\operatorname{Sym}^{A}\mathbf Q^L
\longrightarrow\operatorname{Sym}^{A}\mathfrak h_L
\longrightarrow0.
\tag{AF.19}
\]
Here \(u=L^{-1}\mathbf1\), the last map is the symmetric power
of coordinate-mean subtraction, and the direct-sum expansion
\(\mathbf Q^L=\mathbf Q u\oplus\mathfrak h_L\) gives its
equivariant splitting. The first term is zero at \(A=0\).
Tensor with \(\Lambda^B\mathfrak h_L\), induce with the
specified \(S_q\)-label, and subtract the two known terms.

For each \(j=A\) or \(A-1\), a monomial orbit in
\(\operatorname{Sym}^j\mathbf Q^L\) is indexed by a partition
\(\zeta\vdash j\) of length \(p\le L\). Its stabilizer
has a zero block of size \(L-p\) and positive-exponent blocks
of the multiplicities of equal parts of \(\zeta\). Subtracting
the coordinate mean on each nonempty block decomposes the
restricted standard module into its block standards and a trivial
space of dimension one less than the number of blocks, exactly
as in FK.9. Exterior powers then give explicit block hooks and
binomial multiplicities as in FK.10. Include the selected label
\(\eta\) or \(\eta'\) as one more induction factor.

When the zero block is nonempty, start with its hook. All remaining
factors together add only \(q+p\le q+A\le k\) cells. When
it is empty, the total size \(m=q+p\le k\) is already bounded.
Successive literal Littlewood–Richardson tableaux of at most
\(k\) cells therefore evaluate every term. The large block leg
is fixed by the requested total exterior degree after choosing
the small block legs and the trivial exterior factor; it is
checked rather than enumerated. These are exactly the finite
maps of tensor induction, block-mean decomposition and Young
branching, with no large-degree representation precomputation.

Let \(c_q(\nu)\) be this explicitly evaluated multiplicity of
\([\nu]\) in (AF.18). The complete coefficient is
\[
\boxed{p_{\mu,(n)}^\lambda
=c_{m,a,r}(\nu)-c(m,k,a,r,\nu),\qquad
c(m,k,a,r,\nu)=\sum_{q=1}^{Q}(-1)^{q+1}c_q(\nu).}
\tag{AF.20}
\]
Equations (AF.13)–(AF.19) evaluate every signed term in (AF.20)
using only the displayed bounded normal calculation and small
ordinary branching.

### 5. The correction is the image of an actual map

For \(q=1\), (AF.13) has \(s=0\), \(\rho=(A)\),
\(0\le A<k\), and its normal representation is the scalar.
Thus \(C_1\) is exactly the jet module (PB.11), and
\(c_1(\nu)=d_{m,k,r}(\nu)\).

This comparison preserves the original map, not only its character.
FA.8 substitutes the selected normal variables by
\(-\sum x_jY_{ja}\). The generic-matrix argument FA.9 proves
injectivity on every lowest normal-degree piece. Since
\(A<k<a\), the complementary Pieri computation (AF.11)–(AF.12)
gives precisely
\(\operatorname{Sym}^A\mathfrak h_{m-1}\otimes
\Lambda^r\mathfrak h_{m-1}\) as that associated jet piece.
The dimensions agree, so the truncated map is a triangular
isomorphism, whose inverse is finite elimination. The horizontal
frames HJ.7 and exterior pairing identify its source with
\(S_{(a,1^r)}\mathfrak h_m\). Hence the first differential
of the transformed complex is the actual hook jet evaluation.

The exact signed complex now proves that the alternating sum
in (AF.20) is the multiplicity of \([\nu]\) in the image of
this first differential. Consequently
\[
0\le c(m,k,a,r,\nu)\le d_{m,k,r}(\nu)\le D_k,
\qquad
c(m,k,a,r,\nu)\le c_{m,a,r}(\nu).
\tag{AF.21}
\]
The last inequality follows from the surjection of the ambient
stable-hook representation onto that image; the kernel is the original balanced
module under the exact flag map. This proves (AF.20) with its
actual maps and every sign.

At \(a\ge2k\), inequality (AF.8) gives \(Q=1\), so this
same complex proves jet surjectivity directly. At \(a=2k-1\),
the only possible higher term is the unique pair term of T066.
Thus the present proof gives precise morphisms to all previously
checked endpoint formulas. T065's primary scalar-regularity proof
remains a separate proof of the same endpoint surjection.

### 6. The positive matrices and their complexity

If \(c=0\), retain G037's single stable-hook polytope. If
\(c>0\), (AF.21) puts \(\nu\) in the support of the jet
module. T064's actual word-orbit injection then proves that
each content diagonal of \(\nu\) has at most \(k+1\)
cells; for \(\nu=(m)\) it proves \(r\le k-1\).

For \(a\ge2k+1\), the correction is exactly the whole jet
multiplicity, so use T064's explicit parity-base points and
injective degree transport. For the remaining \(a\le2k\),
the lowest stable numerator degree is at least \(r+1\).
Hence the total tableau and retained-subset excess is at most
\(a-1\le2k-1\). Enumerate semistandard increments above
the row-minimum filling in that range, standardize with the
proved left-to-right tie rule, and deduplicate. Enumerate the
retained subsets in the bounded content window and the residual
coin partitions, as in FK.14–FK.15. These loops list every
needed point and depend on \(m\) polynomially for fixed \(k\).
For the row label, the total degree is at most \(3k-1\);
enumerate the explicit least-support/star-basis points directly.

Choose the first \(c\) distinct complete points. Inequality
(AF.21) proves that the exhaustive enumeration supplies them.
Delete each from its unique current cell by the first differing
coordinate, with the integral lower and upper inequalities at
that coordinate and equalities on all earlier ones. This is an
explicit disjoint lattice partition. It leaves exactly the stable
coefficient minus \(c\) points and has
\(1+c(2N_{\rm poly}-1)\) pieces. Their boundedness and all
bit-size bounds are inherited from the original matrices and the
listed points. This proves (AF.4) and the positive formula.

There is also a specified rational linear comparison with the
original multiplicity space. Apply a fixed primitive Young
idempotent for \([\nu]\) to the transformed exact complex,
write its first map in ordered rational bases, and take the
ordered reduced-row-echelon nullspace basis. Order the retained
polytope points and send their standard basis vectors to this
kernel basis. Equation (AF.20) proves equal dimensions, and the
specified flag map carries that kernel to the original plethysm
multiplicity. This comparison retains the highest type and Specht
projector. The positive evaluator uses (AF.13)–(AF.20); it does
not construct this input-sized kernel or use it as an oracle.

For the computational bounds, the normal arrays and small
character formulas have sizes depending only on \(k\).
Every later LR shape adds at most \(k\) cells, and each large
leg is determined, so all correction arithmetic takes
\(f(k)\operatorname{poly}(m+\text{input bit length})\).
G037's binary-degree evaluator supplies the ambient coefficient.
For matrix generation, the semistandard increment count is at
most \(\binom{m+2k+1}{2k+1}\), the subset window has
parameter-only size, coin degrees are bounded by \(3k+1\),
and there are at most \(D_k\) deletions. Writing the literal
constraints has polynomial cost in their number and bit lengths.
These explicit loops prove (AF.5), with no unspecified
input-dependent precomputation.

### 7. Source and verification scope

The actual complex, highest-type map and normal-order equality
are G027 FA.1–FA.17 and T049 DP.1–DP.10, whose whole proofs
were reread in the T066 check. The complementary-column maps
are the same rational exterior pairings already fixed there.
The skew branching and ordinary induction convention are
Macdonald, *Symmetric Functions and Hall Polynomials*, I§5
and I§7 (7.1)–(7.3), pp.112–114. The exact small-character
formula used in (AF.17) is I§7 (7.8), p.114, including the
alternant coefficient immediately following it; the complete
proof (7.3)–(7.8) on pp.113–115 was reread for this construction.
The literal LR implementation is I§9 (9.2), p.143, with the
complete proof pp.142–147 already checked. Primary text:
<https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf>.

The full executable is `all_fixed_order_hook_positive.py`.
The author has read all AF.1–AF.21 and all executable code,
checking concentration, the nondegenerate normal pairing,
disconnected skew maps, every subgroup sign, the finite normal
algorithm, all exterior/zero-block endpoints and the full
complexity proof; that reading passed. Root independently read
the complete proof and executable; that review also passed.
Archive's whole-proof and independent normal-space check is
being recorded separately.

The initial executable sweep passed 42,624 valid coefficient
consistency cases for \(k=1,\ldots,4\), \(m=4,\ldots,13\),
all \(a=k+1,\ldots,2k+1\), every physical leg and every
outer label. In that sweep every inner-degree-one case was
also required to equal the literal identity coefficient.
The separate `check_all_fixed_order_hook.py` execution passed
912 degree-one identity/parity comparisons, including actual
nonzero terms with five selected blocks, and 3,307 comparisons
with the previously proved endpoint formulas. In twelve
new-range cases, 3,979 literal cells partitioned twenty original
witnesses into exactly three retained witnesses and the
prescribed points. The receipt is
`ALL_FIXED_ORDER_HOOK_RECEIPT.json`; the script's `--full-scan`
option reproduces the initial sweep.

Rectangular independently passed 1,258 original
cycle-index/Murnaghan–Nakayama plethysm comparisons in the
previously untreated lower ranges, including all outer labels,
both determinant parities and three-/four-selected-block
parameters. Its actual side uses no normal module or
complementary-hook induction. The receipt is
`work/rectangular/ALL_FIXED_ORDER_HOOK_ENDPOINT_MN_CHECK.tsv`.

Source readings, whole-proof reviews and executed comparisons
are recorded as separate events.
