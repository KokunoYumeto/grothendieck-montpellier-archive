# A varying-outer-degree first-hook formula and its actual kernel module

## T-060. Stable first-hook tails, positive polytopes and exact support

Let \(m\ge4\), \(a\ge1\), \(t\ge0\), \(n\ge a+t\), and
\(\mu\vdash m\). Put
\[
\begin{gathered}
\lambda=(A,a+t,t+1,t^{m-3}),\\
A=mn-a-(m-1)t-1,\qquad D=a+1.
\end{gathered}
\tag{FH.1}
\]
Set \(\nu=\mu\) for even \(t\), and \(\nu=\mu'\) for odd
\(t\). For a cell \(z=(i,j)\), write \(c(z)=j-i\), and define
\[
\mathcal C_\nu=\nu\setminus\{(1,1),(2,1)\}
\quad\text{when }\nu\ne(m).
\]
Let
\[
f_\nu(q)=\sum_{T\in\operatorname{SYT}(\nu)}q^{\operatorname{comaj}(T)}
=q^{n(\nu)}\frac{\prod_{i=1}^m(1-q^i)}
 {\prod_{z\in\nu}(1-q^{h(z)})},
\qquad n(\nu)=\sum_i(i-1)\nu_i.
\tag{FH.2}
\]
The comajor convention and its complete standardization bijection are
T027/S.3 and S.13–S.16. The hook specialization is Macdonald,
*Symmetric Functions and Hall Polynomials*, second edition,
I§3 Example2, printed p45.

For \(\nu\ne(m)\), put
\[
N_\nu(q)=f_\nu(q)\sum_{z\in\mathcal C_\nu}q^{c(z)+1}
=\sum_{s=0}^{\binom m2+1}N_{\nu,s}q^s.
\tag{FH.3}
\]
All its coefficients are nonnegative integers. The exact positive formula is
\[
\boxed{
p_{\mu,(n)}^\lambda
=\sum_sN_{\nu,s}\,
\#\{(u_2,\ldots,u_m)\in\mathbb Z_{\ge0}^{m-1}:
\textstyle\sum_{i=2}^m i u_i=D-s\}.}
\tag{FH.4}
\]
For the trivial effective label \(\nu=(m)\), it is
\[
\boxed{
p_{\mu,(n)}^\lambda
=\sum_{2\le i<j\le m}
\#\{(u_i,\ldots,u_m)\in\mathbb Z_{\ge0}^{m-i+1}:
\textstyle\sum_{l=i}^m l u_l=D-i-j\}.}
\tag{FH.5}
\]
Negative right sides give empty polytopes. Formula (FH.4) uses at most
\(\binom m2+2\) selected bounded polytopes with at most \(m\)
variables; (FH.5) uses \(\binom{m-1}{2}\) with at most \(m-1\)
variables. Every matrix is explicit in §5.

There is also a closed nonvanishing test. For \(\nu\ne(m)\), let
\[
L_\nu=n(\nu)+\min_{z\in\mathcal C_\nu}(c(z)+1).
\tag{FH.6}
\]
Then
\[
\boxed{
p_{\mu,(n)}^\lambda>0
\iff
\begin{cases}
D\ge L_\nu,&\nu\ne(m),\\
D\ge5,&\nu=(m).
\end{cases}}
\tag{FH.7}
\]
The result concerns the stated varying-\(m\) family. It is an explicit
coinvariant/kernel realization, with its classical ingredients cited
below; no assertion of global priority is made.

## 1. Exact stable-chart and hook maps

Write \(E=\mathfrak h_m=\mathbb Q^m/\mathbb Q(1,\ldots,1)\),
with its permutation action. The first gap in (FH.1) is
\[
A-(a+t)=mn-2a-mt-1\ge(m-2)a-1\ge0.
\]
Thus the output is a partition of \(mn\). Since \(n\ge\lambda_2\),
the exact flag-chart map T032 gives
\[
(S_\lambda\mathbb Q^m)_{(n^m)}
\simeq S_{(a+t,t+1,t^{m-3})}E
\simeq\operatorname{sgn}^{t}\otimes S_{(a,1)}E.
\tag{FH.8}
\]
The first map uses the balanced flag generators and multiplication by
\(u^{n-\lambda_2}\), with the polynomial inverse proved in T032.
The second removes \(t\) full exterior columns through the perfect
determinant pairing. The actual determinant of the permutation quotient
\(E\) is the permutation sign. Together with the Cauchy/Young map of
T003, this proves that the desired multiplicity is
\([\,[\nu]:S_{(a,1)}E\,]\), including its exact sign.

Let \(P=\operatorname{Sym}E\), grade \(P\otimes E\) by polynomial
degree plus one, and let
\[
\delta:P\otimes E\longrightarrow P,
\qquad \delta(f\otimes v)=fv,\qquad K=\ker\delta.
\tag{FH.9}
\]
This is an actual \(S_m\)-equivariant module map with image \(P_+\).
Its degree-\(D=a+1\) kernel is \(S_{(a,1)}E\). More explicitly,
the map
\[
q\otimes(u\wedge v)\longmapsto qu\otimes v-qv\otimes u
\]
from \(\operatorname{Sym}^{a-1}E\otimes\Lambda^2E\) has this
image. The one-box Pieri decomposition and the nonzero hook highest
vector identify its image with the hook Young summand. A concrete
projection onto that image is
\[
1-\frac1D\nabla\delta,
\qquad \nabla p=\sum_j\frac{\partial p}{\partial z_j}\otimes z_j;
\quad\delta\nabla p=Dp
\tag{FH.10}
\]
on degree \(D\). The expression is independent of the basis used
to write the natural polarization map. This proves the comparison with
the actual kernel, including its rational inverse on the complementary
symmetric summand.

## 2. Coinvariants, a free nontrivial multiplicity module and its numerator

Let \(e_i\) be the elementary symmetric functions on the centered
coordinates of \(E\), and put
\[
I=P^{S_m}=\mathbb Q[e_2,\ldots,e_m],\qquad
H=P/(e_2,\ldots,e_m),\qquad M=\binom m2.
\]
The usual coinvariant freeness gives a graded equivariant isomorphism
\(I\otimes H\to P\): choose a homogeneous section of the quotient,
average it over \(S_m\), and multiply. The homogeneous-basis criterion
that this is an isomorphism is Stanley, *Invariants of finite groups
and their applications to combinatorics*, Proposition3.1, p482, and
Theorem3.10, p485. The invariant-polynomial assertion is its §4,
pp486–489. The quotient is concentrated in degrees \(0,\ldots,M\).
These statements hold over \(\mathbb Q\); the section and every
matrix just specified have rational coefficients.

For a nontrivial irreducible \([\nu]\), every element in its
isotypic component of \(P\) has positive degree. Taking
\(\operatorname{Hom}_{S_m}([\nu],-)\) in (FH.9) therefore gives
a surjection onto the free \(I\)-module \(P_\nu\). Choose its
homogeneous \(I\)-basis from \(H_\nu\); lift each basis map of
degree \(D\) by \(\nabla/D\), and extend \(I\)-linearly. This
is an explicit rational \(I\)-linear section. Hence \(K_\nu\)
is a graded direct summand of a finite free \(I\)-module.

For completeness, its graded freeness needs no unspecified basis
theorem. Choose homogeneous lifts of a vector-space basis of
\(K_\nu/I_+K_\nu\); multiplication gives a map from the corresponding
graded free module. Graded Nakayama proves surjectivity. Projectivity
splits the map, and its kernel has zero quotient by \(I_+\), so graded
Nakayama again proves that kernel zero. These steps specify the free
isomorphism: in finite degree the lifts can be chosen by rational row
reduction of the actual kernels and invariant multiples. The resulting
free generators have degrees at most \(M+1\), by (FH.11) below.
The coefficient formula does not require this basis computation.

The finite numerator is
\[
\operatorname{Hilb}(K_\nu;q)
=\frac{q f_{\nu\otimes E}(q)-f_\nu(q)}
 {\prod_{i=2}^m(1-q^i)}.
\tag{FH.11}
\]
The degree of its numerator is at most \(M+1\), since both
fake-degree polynomials refer to \(H\). Here the denominator refers
to the displayed algebra \(I\), so it retains its actual free-module
meaning.

We compute the numerator explicitly. On a cycle of length \(l\),
the polynomial/exterior trace on the permutation representation is
\((1-(-z)^l)/(1-q^l)\). Removing its trivial line and applying the
Frobenius formula gives
\[
\sum_{j\ge0}\operatorname{Hilb}((P\otimes\Lambda^jE)_\nu;q)z^j
=\frac{1-q}{1+z}\,
s_\nu\left[\frac{1-(-z)}{1-q}\right].
\tag{FH.12}
\]
Macdonald I§3 Example3, p45, evaluates the right side. Multiplying
by \(\prod_{i=2}^m(1-q^i)\) gives exactly
\[
\sum_j f_{\nu\otimes\Lambda^jE}(q)z^j
=f_\nu(q)\prod_{v\in\nu\setminus\{(1,1)\}}
(1+zq^{c(v)}).
\tag{FH.13}
\]
The one removed factor is the literal \(1+z\) at cell \((1,1)\).
For non-row \(\nu\), cell \((2,1)\) contributes \(q^{-1}\)
to the coefficient of \(z\). Thus
\(qf_{\nu\otimes E}-f_\nu\) is exactly (FH.3): its subtraction
cancels this one specified term. Every remaining summand is a
nonnegative shifted fake-degree polynomial. The shifts may be
negative, but the resulting exponents are nonnegative: the lowest
possible exponent is at least
\(n(\nu)+2-\ell(\nu)\ge1\). This proves (FH.3)–(FH.4)
with no positivity inferred from a virtual expression alone.

## 3. Trivial multiplicity: actual differential forms and positive cells

The missing trivial component in the surjection onto \(P_+\)
matters. Its exact replacement is Solomon's invariant-form theorem:
*Invariants of finite reflection groups*, Nagoya Math.J.22(1963),
§3 unnumbered Theorem, p59, complete proof pp59–61. In degree one
it identifies
\[
(P\otimes E)^{S_m}=\bigoplus_{i=2}^m I\xi_i,
\qquad \xi_i=\frac1i\,de_i,\qquad\delta\xi_i=e_i.
\tag{FH.14}
\]
The invariant dot form identifies \(E\) with its dual so that these
are the same polynomial differential forms as (FH.9). Euler's formula
proves the last equality, including its scalar. Thus \(K^{S_m}\)
is the actual first cycle module of the sequence \((e_2,\ldots,e_m)\).

Fix a nonconstant monomial \(e^\beta\) in \(I\), let
\(J=\{l:\beta_l>0\}\), and put \(i=\min J\). In multidegree
\(\beta\), the domain of (FH.14) has basis
\(e^\beta\xi_l/e_l\), \(l\in J\), all of which map to
\(e^\beta\). Consequently its kernel has the exact basis
\[
e^\beta\left(\frac{\xi_j}{e_j}-\frac{\xi_i}{e_i}\right),
\qquad j\in J\setminus\{i\}.
\tag{FH.15}
\]
Both denominators cancel because \(\beta_i,\beta_j\ge1\).
Grouping these basis vectors by \((i,j)\) gives
\[
\operatorname{Hilb}(K^{S_m};q)
=\sum_{2\le i<j\le m}
\frac{q^{i+j}}{\prod_{l=i}^m(1-q^l)}.
\tag{FH.16}
\]
This is an actual disjoint basis decomposition: a monomial and its
least support index are unique, and the displayed differences are a
basis in each multidegree. It proves (FH.5).

The nontrivial-label freeness cannot be extended to the trivial label.
Already for \(m=4\), multiplying (FH.16) by
\((1-q^2)(1-q^3)(1-q^4)\) gives
\[
q^5+q^6+q^7-q^9.
\tag{FH.17}
\]
A finite graded free module over this specific invariant algebra has
a numerator with nonnegative coefficients, namely its basis degrees.
The coefficient \(-1\) therefore proves that this trivial cycle module
is not graded free over \(I\). The positive cells (FH.15) retain the
actual module in this case.

## 4. Exact nonvanishing thresholds

The hook product in (FH.2) has lowest coefficient one, in degree
\(n(\nu)\). The coefficient one degree later is the number of
removable corners minus one: each hook of length one contributes
\(1+q+O(q^2)\), while \(\prod_{i=1}^m(1-q^i)=1-q+O(q^2)\).
Therefore (FH.3) has a positive coefficient at degree \(L_\nu\).

It also has a positive coefficient at \(L_\nu+1\) for every
non-row \(\nu\vdash m\) with \(m\ge4\). For a nonrectangle,
there are at least two corners, so the preceding fake-degree
coefficient supplies it. For a rectangle with at least two rows,
the retained cell weights \(c(v)+1\) contain their minimum and
the next integer. For a column these are \(2-m,3-m\). For width
at least two and height two they are \(1,2\). For width at least
two and height at least three they are \(2-\ell,3-\ell\), given
by the bottom first and second cells or the adjacent first-column
cell. The two retained cells exist since \(m\ge4\).

The coin weights include two and three, which generate exactly zero
and every integer at least two. Hence the coefficients at
\(L_\nu\) and \(L_\nu+1\), followed by these coin increments,
prove positivity in every degree at least \(L_\nu\). All smaller
degrees are absent by minimality. For (FH.16), the smallest degree
is five, from \((i,j)=(2,3)\), and degree six occurs from \((2,4)\).
The former cell again supplies every increment generated by two and
three. This proves (FH.7), including every endpoint.

## 5. Literal polytopes, effective computation and encoding

For each nonzero \(N_{\nu,s}\), use variables
\(u_2,\ldots,u_m,y\) and constraints
\[
u_i\ge0,\qquad0\le y\le N_{\nu,s}-1,\qquad
\sum_{i=2}^m i u_i=D-s.
\tag{FH.18}
\]
The selector can be deleted when \(N_{\nu,s}=1\). The integer
points are in bijection with a coin solution and one basis label of
that numerator degree. For (FH.5), omit the selector and use exactly
the displayed weighted equality. All these polytopes are bounded
because every coin weight is positive. The program
`first_hook_positive.py` exports their integer equality and inequality
matrices and the precise tag of each selected piece.

The numerator is computed without a character table: truncate the
hook product at degree \(M\), expand each factor
\((1-q^h)^{-1}\) by the coefficient recurrence, multiply by
\(\prod_{i=1}^m(1-q^i)\), shift by \(n(\nu)\), and add the
\(m-2\) content shifts. This uses polynomially many integer
operations in \(m\). The intermediate coefficient bit lengths are
\(O(m\log(m+1))\): the truncated denominator coefficients count
at most \((M+1)^m\) tuples, and the numerator has at most \(2^m\)
signed terms. Thus (FH.18) has a polynomial-size effective description.

The coefficient itself can also be evaluated in polynomial bit
complexity in \(m+\log(a+1)\). For \(P(q)/Q(q)\), with
\(Q(0)=1\), multiply numerator and denominator by \(Q(-q)\).
The denominator is even. To extract degree \(D\), retain the parity
\(D\bmod2\) of the new numerator, replace \(q^2\) by \(q\),
and replace \(D\) by \(\lfloor D/2\rfloor\). Repeating gives
the constant coefficient. This is Bostan–Mori's Algorithm1
(OneCoeff), §2.1, in *A simple and fast algorithm for computing the
N-th term of a linearly recurrent sequence*, SOSA2021, pp121–122
(author PDF pp4–5). The displayed identity records its exact
coefficient comparison in the present ring.
All denominator degrees are \(O(m^2)\). Their roots remain roots
of unity after squaring, so their coefficients have bit length
\(O(m^2)\). The numerator coefficients are bounded by a fixed
degree-\(O(m)\) polynomial in the accessed coefficient index times
\(2^{O(m^2)}m!\), using (FH.4) or (FH.5); hence their bit lengths
are polynomial in \(m+\log(a+1)\). There are only
\(O(\log(a+1))\) iterations, and naive polynomial multiplication
already gives the stated complexity. The script implements this exact
integer parity reduction, not an input-degree dynamic program.

The encoding statement is explicit. The bounds are polynomial in
\(m\) plus the binary lengths of the parameters. For \(t\ge1\),
the original output has \(m\) positive parts, so this is also
polynomial in its usual explicitly listed binary-part encoding.
For \(t=0\), a binary outer partition can encode large \(m\) in
few parts; the same ordinary-input assertion is made only when
\(m\) is explicitly/unarily encoded. No compressed-encoding claim
is made. Complementary outputs inherit the exact formula through
the exterior-column pairing and sign rule of T004/G015.

## 6. Grothendieck dictionary and checked sources

The original Schur-operation class is transported by the exact
balanced Cauchy, Young and stable-flag maps in (FH.8). The kernel
(FH.9) is an equivariant coherent module on the affine scheme
\(\operatorname{Spec}P\); over \(\operatorname{Spec}I\), its
nontrivial multiplicity components have the specified free
isomorphisms, while the trivial component has the exact cycle
presentation and basis (FH.14)–(FH.15). The gradient and Euler maps
are algebraic morphisms of these modules. Their associated sheaf
and representation-\(K_0\) classes are carried by the same
SGA3 I4.5/4.7.2–4.7.3 and SGA6 VI3.3 dictionaries already verified
in G015/T032. The Schur and \(\lambda\) operations use SGA6
V4.2,4.4,4.8–4.9 and the exact archive-cote133 tensor/Young maps
recorded in A012. The rational finite matrices spread over a
localization of \(\mathbb Z\) clearing their denominators; the
coefficient theorem is on the characteristic-zero generic fiber.

Primary sources read for the steps newly used here:

* Macdonald, second edition, I§3 Examples2–3, p45: ordinary and
  super principal specialization, including the full interpolation
  proof. PDF: <https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf>.
* Stanley, *Invariants of finite groups and their applications to
  combinatorics*, Bull.AMS1(1979), Proposition3.1 p482,
  Theorem3.10 p485, and §4 pp486–490: homogeneous-basis freeness,
  invariant polynomials and the coinvariant representation.
  PDF: <https://sites.math.washington.edu/~billey/classes/reflection.groups/presentations/archive/stanley.1979.pdf>.
* Solomon, *Invariants of finite reflection groups*, Nagoya
  Math.J.22(1963), §3 Theorem p59, complete proof pp59–61,
  formula(4)p62: actual invariant differential-form basis.
  DOI: <https://doi.org/10.1017/S0027763000011028>.
* Bostan–Mori, SOSA2021, §2.1, proof of Theorem1 and Algorithm1,
  pp121–122 (author PDF pp4–5): parity reduction of a rational series.
  PDF: <https://specfun.inria.fr/bostan/BoMo21.pdf>.

## 7. Executed checks and proof status

The full proof has been read by its author. The separate script
`check_first_hook.py` computes the comparison characters directly from
the permutation-cycle determinant of \(\mathfrak h_m\) and the
previously independently written Murnaghan–Nakayama primitive. It uses
no fake-degree or content expression on that side. All8380 coefficient
and parity comparisons passed, covering every label for \(m=4,\ldots,10\)
and \(a=1,\ldots,60\), with the additional literal parity cases.
All7920 support comparisons passed. The actual matrices yielded1536
checked polytopes and3818 integer witnesses, each checked directly
against every equality and inequality.

For \(m=4\), the exact rational denominators prove a period12
quasipolynomial of degree at most two in every positive degree.
Three small original-cycle values per residue therefore supply an
independent large-index comparison: all60 cases at indices of size
\(10^{30}\) passed the parity evaluator. The negative coefficient in
(FH.17) was also reconstructed directly. The full receipt is
`FIRST_HOOK_RECEIPT.json`. These scopes are distinct from any subsequent
independent whole-proof reading; none is inferred from a citation.

Independent full-proof reviews are now complete: the root author read
all of T060, and the archive agent recorded A087 in
`work/archive/FIRST_HOOK_KERNEL_REVIEW.md`, including fresh readings
of all four primary inputs and the actual invariant-algebra section.
The rectangular agent also independently compared 312 literal
Murnaghan–Nakayama plethysm coefficients in
`work/rectangular/VARYING_FIRST_HOOK_MN_CHECK.tsv`. Of these, 276
lie in the stated range \(m\ge4\); the other 36 check the same module
identity at \(m=3\), without extending the support theorem to that rank.
