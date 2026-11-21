# Independent reviews of the five-point higher-power formulas

Statements **A-042–A-045**. Checked on 21 November 2026 by GPT-6 Astra
Pro, run /root/archive_audit; effort setting not exposed. This report
records complete proof readings, the actual maps checked, and the
separate scope of executed calculations. The six-category event ledger
is CHECK_EVENTS.tsv.

## A-042. The all-power hook formula T043

**Result: complete proof PASS; all 403,200 fixed constants independently
reconstructed.** The source read in full is
work/theta/outer5/hook_all_powers_report.md. Put
\(E=\mathbf Q^5/\mathbf Q(1,\ldots,1)\), let \(Q\) be the rank-three
tautological quotient on \(\mathbf P(E)\), and let \(I\) be the ideal
of the five projective-frame points. The module under review is
\[
H^0\!\left(I^k(2k)S_{(a,1)}Q\right),\qquad a\ge1,\quad k\ge0.
\]
The actual flag pairing gives the stated sign twist
\(\varepsilon^{d+a}\) and the partition
\[
(d+2a+3k+1,d+a+2k,d+a,d+a-1,d).
\]
Its total size is \(5(d+a+k)\); all endpoint inequalities agree with
the partition convention.

The hook resolution is the image of the actual tensor-complex
projector. Its maps, before the indicated Schur projections, are
\[
l^2v\longmapsto l\otimes l\otimes v,\qquad
l\otimes e\otimes v\longmapsto e\otimes lv-l\otimes ev.
\]
Their composite is zero. On a local splitting \(E=L\oplus Q\), the
ordinary tensor contraction gives the asserted exact sequence.
After tensoring by \(I^k(2k)\), its three terms are
\[
\begin{aligned}
F_2&=I^k(2k-2)\operatorname{Sym}^{a-1}E,\\
F_1&=I^k(2k-1)E\otimes\operatorname{Sym}^{a-1}E,\\
F_0&=I^k(2k)S_{(a,1)}E .
\end{aligned}
\]
The exactness survives this tensoring because the original sequence
is locally split. For \(k\ge2\), A-029 gives \(H^1(F_0)=H^1(F_1)=0\),
and the scalar ideal sheaves have no \(H^2,H^3\) in the displayed
range. Resolving the image of \(F_1\to F_0\) by \(F_2\to F_1\) proves
vanishing of all higher cohomology of the quotient. The potentially
nonzero \(H^1(F_2)\) affects the section sequence, not the asserted
higher-cohomology vanishing. The proof treats \(k=1\) by the actual
Čech map from T041 and \(k=0\) by the acyclicity of the twists
\(-1,-2\); these endpoints were checked separately.

The resulting Euler identity, its dimension polynomial, the
bivariate rational character, the parity twist, and all fifteen
active Newton orders were checked. In particular, the missing
order \((3,3)\) follows from the actual phase polynomial degrees.
The product of binomial coefficients counts exactly the ordered
subset coordinates used in the displayed bounded polytopes. The
support argument uses actual invariant quadratic multiplication:
the quadratic in \(Q\) preserves the kernel realization of the
hook functor, and the scalar quadratic in the ideal-power direction
is nonzero in the coordinate domain. Thus the parity-direction
injections used in the support proof are genuine module maps.

The independent script
check_hook_all_powers_by_ambient.py reconstructs the character as an
ambient \(3\times3\) Jacobi–Trudi determinant minus the actual
five-point jets, without using the hook Euler-resolution formula.
It uses the seven elementary closed symmetric-power trace formulas,
checks twenty-eight proper rational denominators, and applies
literal finite differences. All 403,200 constants agree, as do all
seven serialized table hashes and all seventeen zero pairs. The
smallest positive-order constant is \(941\), the largest constant
is \(1,213,066,800\), and the proved bound on every signed-64
intermediate is \(360,556,473,799,296\). The receipt is
HOOK_ALL_POWERS_AMBIENT_RECEIPT.json.

## A-043. The two-row boundary ray T044

**Result: complete proof PASS.** The complete report
work/theta/outer5/two_row_ray_report.md and its certificate program
were read. This is the \(t=0\) specialization of the actual
two-row complex checked in A-038 and of G021 checked in A-039.
For \(a=b+x\), its trace is the three-term expression
\[
A(h_{2k}-J)-B(h_{2k-1}-J)+C(h_{2k-2}-J),
\]
where
\[
A=s_{(a,b)}(E),\quad
B=s_{(a-1,b)}(E)+s_{(a,b-1)}(E),\quad
C=s_{(a-1,b-1)}(E).
\]
Invalid partitions mean zero. The identity
\[
B=h_{a-1}h_b-h_{a+1}h_{b-2}
\]
follows by adding the two \(2\times2\) Jacobi–Trudi determinants
and remains valid at \(a=b\) and \(b=0\) with the stated zero
convention. These boundary conventions match the projected
tensor complex.

The degrees \((3,4,3)\), the fifty-five active orders, the
twenty-five absent orders, and the ten-variable lattice bijection
were checked against the exact rational expression. The
coefficientwise domination independently reconstructed in A-039
also proves positivity of every positive order on this ray. The
reported support list has seventy entries, distributed
\((9,3,3,6,6,12,31)\) among the seven labels; the list and its
injection argument were read and checked.

The author's complete 120,960,000-entry certificate, its overflow
bound, its coefficient construction and its receipts were reviewed.
That complete stream was **not independently rerun in A-043**.
The earlier independent G021 phase calculation and evaluator
specializations remain separately identified in A-039.

## A-044. One degree below the boundary T045

**Result: complete proof PASS.** The full source read is
work/theta/outer5/two_row_below_ray_report.md. The module is
\[
H^0\!\left(I^k(2k-1)S_{(b+x,b)}Q\right).
\]
For \(k\ge2\), A-029 supplies \(H^1(I^k(2k-1))=0\).
The other terms of the locally split Schur complex have no
\(H^2,H^3\). Its two short exact sequences therefore prove the
claimed higher-cohomology vanishing.

The new endpoint \(k=1\) was checked at the level of actual maps.
Write \(P=\mathbf Q^5\), with basis indexed by the five points
represented by vectors \(\ell_i\in E\), satisfying
\(\sum_i\ell_i=0\). The maps in the report are
\[
H^1(I)=P/\mathbf Q(1,\ldots,1)\ \longrightarrow E,
\qquad [c]\longmapsto\sum_i c_i\ell_i,
\]
and
\[
H^1(I(1))=P/\operatorname{ev}(E^*)\ \longrightarrow\mathbf Q,
\qquad [c]\longmapsto\frac15\sum_i c_i .
\]
The five-point frame makes the first map an isomorphism.
Multiplication by a linear form \(\phi\in E^*\) becomes
\(v\mapsto\phi(v)/5\) under these identifications. Hence the last
map in the cohomology row is exactly one fifth of the Schur
insertion map. Marking each of the \(a+b\) tensor positions and
then applying the same primitive idempotent gives its explicit
reverse map \(\delta\), with
\[
D\delta=(a+b)\operatorname{id}.
\]
Thus \(5\delta/(a+b)\) is a right inverse for every nonempty
shape. The empty shape is excluded by the stated validity
inequality. At \(b=0\), the remaining actual kernel is
\(S_{(x-1,1)}E\), as stated.

The conversion \(K=k-2\) for the \(k\ge2\) range, the separate
first-power formula, all sign twists, partition endpoints and
the bounded-polytope bijections were checked. The report's
120,960,000-entry certificate and its separate 504,000-entry
first-power certificate were read, including their exact
integer bounds and finite recurrences. Those two streams were
**not independently rerun in A-044**.

## A-045. The pair-line correction T046

**Result: complete proof PASS.** The full source read is
work/theta/outer5/two_row_line_correction_report.md. For every
\(k\ge5\) and \(a\ge b\ge0\), the actual higher-cohomology module is
\[
H^1\!\left(I^k(2k-2)S_{(a,b)}Q\right)
\simeq
\operatorname{Ind}_{S_2\times S_3}^{S_5}
\left(\operatorname{sgn}_{S_2}\otimes S_{(a,b)}h_3\right).
\tag{AR1}
\]
Here \(h_3\) denotes the two-dimensional sum-zero representation
on the remaining three points. All higher groups of index at
least two vanish.

For a pair \(e=\{i,j\}\), put \(P_e=\langle\ell_i,\ell_j\rangle\)
and \(L_e=\mathbf P(P_e)\). The actual restriction morphism is
\[
I^k(r)\longrightarrow
(i_e)_*\mathcal O_{L_e}(r)(-kp_i-kp_j).
\]
The target is \((XY)^k\mathcal O_{L_e}(r-2k)\).
The factor \((XY)^k\) is invariant under interchange of the
endpoints. At \(r=2k-2\), its first cohomology is \(\det P_e\);
at \(r=2k-3\), it is \(P_e\otimes\det P_e\).
The actual linear-form map on these groups is contraction
\[
v\otimes\omega\longmapsto \phi(v)\omega.
\]
This follows either from the displayed Čech representatives or
from the same Serre-duality pairing; both twists and the
determinant action agree.

The target overlap functional is the difference of the two
endpoint coefficients of order \(k-1\). In the preceding
degree there are two directed functionals, using endpoint
orders \((k-1,k-2)\) and \((k-2,k-1)\). At any fixed point the
four tangent directions to the other points form a projective
frame in \(\mathbf P^2\). In frame coordinates, the four
quadratics
\[
z_1^2-z_1z_2,\quad z_2^2-z_1z_2,\quad
z_3^2-z_1z_2,\quad z_1z_2
\]
give four independent evaluations. Multiplication by
\((z_1+z_2+z_3)^{s-2}\), with the explicit nonzero
normalizing evaluations, proves independence in every degree
\(s\ge2\). The top jets therefore isolate the ten target
functionals and the twenty directed source functionals for
the required range. Lower-order changes of local coordinates
do not alter this triangular argument. The resulting
restriction maps on the scalar first cohomology are onto.

The Cox comparison from A-028 was rechecked with its actual
grading:
\[
cH-k\sum_iE_i\longleftrightarrow
((c-k)^5,\,3c-5k).
\]
At \(c=2k-2\), the coefficient formula gives
\[
h^0(I^k(c))
=\binom{2k+1}{3}-5\binom{k+2}{3}+10
\]
for \(k\ge6\). At \(k=5\), the last Cox weight is \(-1\),
so the section space is zero, and the same displayed
expression is \(165-175+10=0\). Comparing with the fat-point
length \(5\binom{k+2}{3}\) proves that the scalar first
cohomology has dimension ten throughout \(k\ge5\). Its
surjection onto the ten line groups is therefore an
isomorphism, including the endpoint.

Finally, the locally split Schur complex yields
\[
H^1(I^k(c)S_{(a,b)}Q)
=\operatorname{coker}\bigl(H^1(F_1)\to H^1(F_0)\bigr).
\]
The source restriction is onto the sum of
\(P_e\otimes\det P_e\) tensored with the removed-shape
representations, and the target restriction is the scalar
isomorphism just proved. The diagram commutes by the actual
linear-form contraction. The image on each pair is precisely
the Schur-insertion image of \(P_e\). Indeed, the kernel of
\(E^{\otimes(a+b)}\to(E/P_e)^{\otimes(a+b)}\) is generated by
tensors with one entry in \(P_e\); applying the primitive
idempotent and the explicit branching projections gives
exactly those insertion maps. Its quotient is
\(S_{(a,b)}(E/P_e)\). The endpoint transposition acts trivially
on \(E/P_e\) and by sign on \(\det P_e\); the remaining
three-point action is \(h_3\). Summing over the ten pairs
proves the equivariant isomorphism (AR1).

The seven correction characters were independently checked
by counting fixed two-element subsets:
\[
\bigl(10(x+1),\
3(-1)^b{\bf1}_{2\mid x}-(x+1),\
-2(-1)^b{\bf1}_{2\mid x},\
\tau(x),-\tau(x),0,0\bigr),
\]
where \(\tau\) has period three and values \(1,-1,0\).
The family, the sign \(\varepsilon^{d+b+x}\), the validity
inequality \(2b+x+k\ge6\), the exceptional invalid origin
at \(k=5\), and the six valid support exceptions were checked.
The author's 120,960,000-entry Newton certificate, its
integer bound, and its ten-variable polytope conversion
were read. That complete numerical stream was **not
independently rerun in A-045**. This limitation concerns
that executed certificate; the whole cohomological proof
and every morphism establishing (AR1) were checked.
