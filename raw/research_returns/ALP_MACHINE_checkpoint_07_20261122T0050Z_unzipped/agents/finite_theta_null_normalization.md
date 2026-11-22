# ALP-LIFT-07: the actual theta characteristic, its finite normalization, and the source line

Run ALP_MACHINE. Author: `/root/lift_accounting`, GPT-6 Astra Pro; reasoning
effort is not separately exposed. The good models and Hodge bases are the
proved ALP-LIFT-05 inputs. The homology basis is AM-R-004. The branch
half-period table also occurs independently in AM-DO-012; credit it once
in a final synthesis. The new finite calculation uses the determinant of
cohomology, so no unspecified Thomae scalar enters it.

## Statement and normalization

Put
\[
 C:y^2=x^7-1,\quad J=\operatorname{Jac}(C),\quad
 P_a=(\zeta_7^a,0)\ (0\leq a\leq6),\quad P_\infty=\infty.
 \tag{T1}
\]
For a three-element subset \(S\subset\{0,\ldots,6\}\), set
\[
 E_S=\sum_{a\in S}P_a,\qquad D_S=E_S-P_\infty.
 \tag{T2}
\]
At each finite place work over a complete DVR \(R\), after a finite
extension large enough for ALP-LIFT-05's good curve model and these
sections. Write \(v_p(p)=1\). On the relative degree-two Picard scheme
take its canonical determinant theta divisor, pull it back to
\(\mathcal J\) by \(x\mapsto\mathcal O(D_S)\otimes x\), and
denote the resulting line and canonical section by
\((\mathcal L_S,s_S)\). The section has no vertical divisor: on each
geometric fibre it is the ordinary nonzero theta section. This is the
primitive integral theta model meant here. The valuation of its nonzero
origin value means its valuation relative to any primitive generator of
the free rank-one module \(e^*\mathcal L_S\); this is independent of
the generator's integral-unit ambiguity.

**(a) Exact finite value.** All 35 choices have \(s_S(0)\ne0\) on the
generic fibre, and
\[
 \boxed{v_p(s_S(0))=
 \begin{cases}6/7,&p=2,\\0,&p\text{ odd}.\end{cases}}
 \tag{T3}
\]
The entry at 7 is zero on the good model after extension. Normalization
of the value to 1 therefore contributes the fixed scalar valuation
\(-6/7\) at 2 and zero at every odd prime, in these local integral
origin frames.

**(b) Characteristic of the explicit analytic germ.** In AM-R-004's
symplectic basis
\[
 a_j=\gamma_{2j},\qquad b_j=\sum_{k=j}^2\gamma_{2k+1}
 \quad(0\leq j\leq2),
 \tag{T4}
\]
write a half-period as \((m+\tau n)/2\), with
\(m,n\in\mathbb F_2^3\). The Riemann constant for infinity is
\[
 K_\infty=\frac{(1,0,1)^t+\tau(1,1,1)^t}{2}
 =\operatorname{AJ}(P_1+P_3+P_5-3P_\infty).
 \tag{T5}
\]
Thus \(D_{135}=P_1+P_3+P_5-P_\infty\) corresponds to the **zero
analytic characteristic**. Its theta divisor is the zero locus of
\(\theta(z,\tau)\), and AM-R-004's value-one germ
\[
 F_1(u)=\exp\!\left(\frac\pi2z^t(\operatorname{Im}\tau)^{-1}z\right)
 \frac{\theta(z,\tau)}{\theta(0,\tau)},\qquad u=Pz,
 \tag{T6}
\]
belongs to this precise principal line. AM-DO-011 identifies it as the
reduced theta in the specified CM differential coordinates and applies
Bannai--Kobayashi's algebraicity theorem. Those are separate carried
findings; (T3) is an additional integral origin calculation.

**(c) The trace-one line is a different principal line.** Let \(a\)
be induced by \(x\mapsto\zeta_7x\), let \(w_0=-(a+a^2+a^4)\),
and put \(L_{w_0}=(1,w_0)^*\mathcal P_\lambda\), as in accepted
DP49. Let \(L_\infty\) be the theta line obtained from
\(2P_\infty\). Superscript \(\mathrm{rig}\) means tensoring a
line with the inverse of its origin fibre, giving a rigidified line.
On the good models as well as generically,
\[
 L_{w_0}\simeq L_\infty^{\mathrm{rig}}.
 \tag{T7}
\]
Its unique principal theta section vanishes to order **two** at zero.
In contrast,
\[
 L_{135}^{\mathrm{rig}}\simeq L_{w_0}\otimes\mathcal P_T,
 \qquad T=K_\infty\in J[2]\setminus\{0\},
 \tag{T8}
\]
using the canonical polarization to identify \(J\) with its dual.
For every positive even integer \(M\) there is an integral rigidified
isomorphism
\[
 [M]^*L_{135}^{\mathrm{rig}}\simeq L_{w_0}^{\otimes M^2}.
 \tag{T9}
\]
The pulled-back primitive section retains (T3). Its normalized reduced
germ is \(F_1(Mu)\), and
\[
 M^{-|\alpha|}\partial_u^\alpha F_1(Mu)|_{u=0}
       =\partial_u^\alpha F_1(u)|_{u=0}.
 \tag{T10}
\]
This construction is **outside the present source `Level` record**,
which requires `Odd M`. For odd \(M\) the nonzero two-torsion twist
survives pullback. An odd-order theta-group translation within
\(H^0(J,L_{w_0}^{M^2})\) cannot change its underlying line into that
of \([M]^*s_{135}\). This is a line distinction, not a claim that
allowed odd-order translates have zero origin value.

## Proof of the determinant normalization

### 1. The determinant theta model and its dual complex

The degree \(g-1\) theta divisor has its standard determinant-of-
cohomology description: a perfect two-term complex of equal-rank vector
bundles computes the universal degree \(g-1\) line's cohomology, and
the determinant of its differential is the theta section. See
Casalaina-Martin and Kass (2010, Definition 3.1 and the ensuing
paragraphs, printed pp. 9--10). Invariance of this determinant element
under a change of perfect representative is the determinant functor
formalism (Stacks Project, Tag 0FJI). We use this construction over the
DVR; no equal-characteristic arc theorem is asserted to cover the
present mixed-characteristic family.

Write \(\omega=\Omega^1_{\mathcal C/R}\). The exact sequence
\[
 0\to\omega(P_\infty-E_S)\to\omega(P_\infty)
   \to\omega(P_\infty)|_{E_S}\to0
 \tag{T11}
\]
gives a simple complex. On every geometric fibre,
\(H^1(\omega(P_\infty))=0\) by Serre duality and
\(h^0(\omega(P_\infty))=3\) by Riemann--Roch. The inclusion
\(H^0(\omega)\to H^0(\omega(P_\infty))\) is an isomorphism
on each fibre: both have dimension three, or a differential cannot have
a single nonzero simple-pole residue. Cohomology and base change and
Nakayama therefore identify these integral rank-three modules. Since
\(E_S\) is finite flat of degree three, its restricted invertible
sheaf has free rank three over \(R\). Hence
\[
 r_S:H^0(\omega(P_\infty))\longrightarrow
 H^0(E_S,\omega(P_\infty)|_{E_S})
 \tag{T12}
\]
is a map between free rank-three modules. Its complex in degrees zero
and one computes \(R\Gamma(\omega\otimes\mathcal O(-D_S))\).

Relative Serre duality identifies this with the dual shifted complex
of \(R\Gamma(\mathcal O(D_S))\); see Stacks Project, Tag 0E6N.
For a free complex \([A\xrightarrow d B]\) in degrees zero and one,
the dual shifted complex is \([B^*\xrightarrow{\pm d^t}A^*]\),
which has the same determinant valuation. Thus the theta section at
\(D_S\) has valuation \(v_p(\det r_S)\). Equivalently, Smith
normal form says that the determinant order of this generically
acyclic complex is the sum of its elementary-divisor orders, the length
of its torsion cokernel. This elementary argument works over every
DVR. We have not used an unverified integral identification of
\(\omega(-D_S)\) with \(\mathcal O(D_S)\).

The canonical relative theta section is primitive because its
restriction to every geometric Picard fibre is a proper effective
theta divisor, not that entire fibre. The translated pullback is
primitive for the same reason. The determinant in (T12) therefore
computes the stated model, with no arbitrary vertical scalar.

### 2. Every odd-prime value is a unit

For \(p\nmid14\), the original good model has seven distinct finite
branch points, separate from infinity. At 7 use ALP-LIFT-05's good model
\[
 Y^2=\frac{(1+\lambda X)^7-1}{\lambda^7},\qquad
 \lambda=\zeta_7-1,
 \tag{T13}
\]
whose special fibre is \(Y^2=X^7-X\). The branch coordinates are
\[
 X_a=(\zeta_7^a-1)/\lambda\equiv a\pmod\lambda,
 \tag{T14}
\]
so they are again distinct. On each smooth odd-characteristic fibre,
\(K_C\sim4P_\infty\) and
\(H^0(\mathcal O(5P_\infty))=\langle1,X,X^2\rangle\).
Riemann--Roch and evaluation at three distinct coordinates give
\[
 h^0(D_S)=h^0(5P_\infty-E_S)=0:
 \tag{T15}
\]
the quadratic-polynomial evaluation matrix is an invertible
Vandermonde. This also proves the generic nonvanishing. Since the
degree is \(g-1\), first cohomology vanishes as well. The matrix
(T12) is therefore invertible after reduction, proving all the odd
entries of (T3). No parity assertion in characteristic 2 was used.

### 3. The dyadic collision algebra

Use the good model and integral Hodge basis from ALP-LIFT-05:
\[
 Y^2+Y=X^7,\quad x=\alpha X,\quad y=\iota(2Y+1),\quad
 \alpha^7=-4,\quad\iota^2=-1,\qquad
 \eta_i=X^{i-1}\frac{dX}{2Y+1}\ (1\leq i\leq3).
 \tag{T16}
\]
On the infinity chart \(U=1/X\), \(V=YU^4\), the equation is
\(V^2+U^4V=U\). The rational function
\[
 t=X^3/Y=U/V=V+U^4
 \tag{T17}
\]
is a uniformizer at the infinity section. Indeed \(U\) is a formal
power series in \(V\) beginning with \(V^2\), so
\(t=V+O(V^8)\). The completed ring is \(R[[t]]\), and \(dt/t\)
is an integral generator of \(\omega(P_\infty)\) on this disk.
At \(P_a\),
\[
 X_a=\zeta_7^a/\alpha,\quad Y_a=-1/2,\quad
 t_a=-2\alpha^{-3}\zeta_7^{3a}.
 \tag{T18}
\]
All seven sections specialize to infinity. Since
\(v_2(\alpha)=2/7\),
\[
 v_2(t_a)=1/7,\qquad v_2(t_a-t_b)=1/7\quad(a\ne b).
 \tag{T19}
\]
The differences of distinct seventh roots of unity are dyadic units:
their reductions are distinct since \(X^7-1\) is separable in
characteristic 2. The actual finite flat collision algebra is thus
\[
 H^0(E_S,\mathcal O_{E_S})
   =R[[t]]\big/\!\prod_{a\in S}(t-t_a).
 \tag{T20}
\]
The product is a distinguished monic cubic, so Weierstrass division
gives the integral basis \(1,t,t^2\). Inverting the uniformizer
splits the algebra into the three point evaluations. That split
evaluation basis is not integral: its determinant relative to
\(1,t,t^2\) is a Vandermonde of valuation \(3/7\).

Write \(\eta_i=f_i(t)dt/t\). Differentiating (T17) and using
\(X^7=Y^2+Y\) yields the exact identity
\[
 dt=-\frac{X^2(Y+4)}{Y(2Y+1)}dX,\qquad
 \frac{\eta_i}{dt}=-\frac{YX^{i-3}}{Y+4}.
 \tag{T21}
\]
The ratio extends at every \(P_a\). Substitution gives
\[
 f_i(t_a)=t_a\frac{\eta_i}{dt}(P_a)=-\frac27X_a^i.
 \tag{T22}
\]
Up to the ordering sign, this split evaluation determinant is
\[
 \det(f_i(t_a))=
 \left(-\frac27\right)^3
 \left(\prod_{a\in S}X_a\right)
 \prod_{a<b\text{ in }S}(X_b-X_a).
 \tag{T23}
\]
Each \(X_a\) and each pairwise difference has valuation \(-2/7\).
Thus (T23) has valuation
\[
 3-6/7-6/7=9/7.
 \tag{T24}
\]
The conversion matrix from the integral target basis
\((1,t,t^2)dt/t\) to split evaluation has determinant
\(\prod_{a<b}(t_b-t_a)\), of valuation \(3/7\). Consequently
the actual integral restriction map in (T12) has
\[
 v_2(\det r_S)=9/7-3/7=6/7.
 \tag{T25}
\]
This proves the dyadic entry of (T3) for every triple. It also explains
why using only split point values would give the incorrect answer
\(9/7\). The special-fibre class \(D_S\) is \(2P_\infty\),
whose space of sections has dimension two, consistent with the nonunit
theta value.

## Proof of the characteristic and source-line assertions

### 4. Half-periods and the Riemann constant

In this subsection only, write
\(t_a=\operatorname{AJ}(P_a-P_\infty)\); this is distinct from
the parameter values in (T18). Each \(t_a\) is two-torsion because
\(\operatorname{div}(x-\zeta_7^a)=2P_a-2P_\infty\). The
adjacent-arc relation for the paths of AM-R-004 is
\[
 t_a-t_0=\frac12\sum_{j=0}^{a-1}\gamma_j
                    \pmod{H_1(C,\mathbb Z)}.
 \tag{T26}
\]
This is the hyperelliptic doubled-arc calculation: the two sheets give
opposite integrals between the ramification endpoints, so the closed
cycle is twice the Abel integral. It also follows from AM-DO-012's
independently evaluated branch half-periods. Since
\(\operatorname{div}(y)=\sum_aP_a-7P_\infty\), one has
\(\sum_at_a=0\). Summing (T26), using two-torsion, and reducing
cycle coefficients modulo two gives
\[
 t_0=(\gamma_1+\gamma_3+\gamma_5)/2=b_0/2.
 \tag{T27}
\]
Substitution of \(\gamma_{2j}=a_j\),
\(\gamma_1=b_0-b_1\), \(\gamma_3=b_1-b_2\),
and \(\gamma_5=b_2\) now gives

| \(a\) | \(m_a\) | \(n_a\) in \(t_a=(m_a+\tau n_a)/2\) |
|---:|:---:|:---:|
| 0 | 000 | 100 |
| 1 | 100 | 100 |
| 2 | 100 | 010 |
| 3 | 110 | 010 |
| 4 | 110 | 001 |
| 5 | 111 | 001 |
| 6 | 111 | 000 |

The Riemann constant is determined from this table and parity, rather
than assumed from the labels. The theta characteristic \(2P_\infty\)
has \(h^0=2\). Its twist by any \(t_a\) is \(P_\infty+P_a\),
with \(h^0=1\): Riemann--Roch identifies this dimension with the
space of sections of \(3P_\infty-P_a\), a codimension-one
subspace of \(\langle1,x\rangle\). The standard Riemann theta
correspondence identifies algebraic and analytic characteristic
parity; equivalently use Riemann singularity and analytic theta
parity. These classical inputs are recalled by Mumford (1971,
pp. 181--182) and Casalaina-Martin and Kass (2010, p. 1).

In the convention of DLMF 21.2.5--21.2.7, the analytic characteristic
of \((m+\tau n)/2\) is \([n/2;m/2]\) and has parity
\(n\cdot m\). This follows directly by replacing the theta
summation index by \(-k-n\). If \((m_K,n_K)\) is the
characteristic of \(2P_\infty\), its parity is even and all seven
twists above are odd. Therefore
\[
 n_a\cdot m_a+n_K\cdot m_a+m_K\cdot n_a=1
                         \quad\text{in }\mathbb F_2.
 \tag{T28}
\]
The rows \(a=0,1,2,3,4,5\), in succession, force
\[
 m_K=(1,0,1),\qquad n_K=(1,1,1).
 \tag{T29}
\]
The last row is consistent and this characteristic is even. The table
also gives \(t_1+t_3+t_5=K_\infty\). The divisor for
\(2P_\infty\) is analytically \(\theta(z+K_\infty,\tau)=0\)
up to a nowhere-vanishing factor. Translating its degree-two class by
\(t_1+t_3+t_5=K_\infty\) changes it to \(D_{135}\) and adds
another \(K_\infty\) to the theta argument. Since \(2K_\infty\)
is a period, the divisor becomes \(\theta(z,\tau)=0\). This proves
(T5)--(T6). All parity arguments here take place over \(\mathbb C\),
not in residue characteristic 2.

### 5. Identification of the invariant principal line

Use the accepted DP49 identities \(a^\dagger=a^{-1}\),
\(w_0+w_0^\dagger=1\), \(w_0w_0^\dagger=2\), and its
principal polarization conclusion for \(L_{w_0}\). Symmetry and
multiplication isomorphisms are also in accepted DP59, proof of
(TS7)--(TS8). The same Poincaré functoriality applies to each good
abelian scheme in ALP-LIFT-05. In particular
\[
 a^*L_{w_0}\simeq(1,a^\dagger w_0a)^*\mathcal P_\lambda
                 \simeq L_{w_0}.
 \tag{T30}
\]
The theta line \(L_\infty\) is symmetric as well: relative duality
sends \(2P_\infty\otimes x\) to \(2P_\infty\otimes x^{-1}\),
since \(\omega\simeq\mathcal O(4P_\infty)\). This canonical-
divisor identity holds on the good models, where the first integral
differential has divisor exactly \(4P_\infty\). The automorphism
fixes infinity and preserves effectivity, so it preserves this theta
divisor.

Two rigidified principal theta lines with the same polarization differ
by a rigidified line in \(\operatorname{Pic}^0\). Because both are
symmetric, that difference is two-torsion; because both are
\(a\)-invariant, it is fixed by the dual \(a\)-action. But
\(a-1\) is invertible on two-torsion. Indeed \(\Phi_7(a)=0\), and
\[
 (T-1)(T^5+2T^4+3T^3+4T^2+5T+6)=\Phi_7(T)-7
 \tag{T31}
\]
shows that \(a^5+a^3+a\) is an inverse to \(a-1\) on \(J[2]\).
The dual action has the same property. This is a group-scheme
endomorphism identity, so it remains valid on two-torsion in residue
characteristic 2. The invariant difference is therefore trivial,
proving (T7) integrally with rigidifications.

The space of sections of \(2P_\infty\) is exactly
\(\langle1,x\rangle\), so Riemann singularity gives theta
multiplicity two at zero. Translation by \(T=K_\infty\) and the
definition of the polarization homomorphism give (T8). The explicit
table shows \(T\ne0\).

### 6. Pullbacks and the exact source limitation

For a rigidified symmetric line, \([M]^*L\simeq L^{M^2}\); for
a rigidified degree-zero line,
\([M]^*\mathcal P_T\simeq\mathcal P_{MT}\). These are the
theorem-of-the-cube identities; for \(L_{w_0}\) the first is exactly
the integral Poincaré identity in DP59 (TS7). Applied to (T8), they
prove (T9) when \(M\) is even.

Choose a primitive local generator of \(e^*\mathcal L_{135}\) to
transfer its canonical section to the rigidified line. Pullback by
\([M]\) retains the origin value. It retains primitivity as well:
multiplication on an abelian scheme is finite faithfully flat, so a
nonzero section on the special fibre cannot pull back to zero. The
isomorphism (T9) is integral and rigidified and introduces no nonunit
origin scalar. This proves its claimed origin valuation. In reduced
analytic frames the pullback is composition with \(u\mapsto Mu\);
normalization gives \(F_1(Mu)\). The chain rule proves (T10),
including the exact factor \(M^{-|\alpha|}\).

For odd \(M\), instead \(MT=T\ne0\), and hence
\[
 [M]^*L_{135}^{\mathrm{rig}}
 \simeq L_{w_0}^{M^2}\otimes\mathcal P_T
       \not\simeq L_{w_0}^{M^2}.
 \tag{T32}
\]
The directly recovered source file
`ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ToroidalCompactification/TwoWeightEqOneAddRoot.lean`,
lines 53--60, defines `Level` with `odd : Odd M` at line 56.
Accepted DP59/DP62 likewise use odd levels with theta translations in
the specified subgroup of \(J[M^2]\). A theta-group translation
acts within the section space of its given line, so it cannot erase
the nontrivial difference in (T32). This is the stated limitation. It
does not imply that allowed odd torsion translates of the singular
principal section have zero origin value; they can have nonzero value,
and DP59 already supplies jet-spanning results for their prescribed span.

## What this closes, and what remains

This identifies the exact algebraic principal line for AM-R-004's
nonvanishing analytic germ, computes its entire finite origin
normalization on the stable good models, and identifies the different
principal line specified by the trace-one construction. Thus this
explicit analytic model has neither an unspecified characteristic nor
an unspecified finite theta-null scalar.

It does not make the value-one Chern/reduced formal frame integral at
nonordinary primes. A unit value at 11 does not imply integral Taylor
coefficients or identify the selected gain. Conversion from an
integral algebraic frame to the reduced CM frame remains a separate
local problem, as AM-DO-013--014 explain. At 2 the norm
\(w_0w_0^\dagger=2\) is a nonunit: neither (T3) nor (T7) verifies
DP49's unit-parameter primitive-kernel hypotheses. The even-level
construction (T9) is outside `Level.odd`. Finally \(F_1(Mu)\) is a
pullback theta, distinct from AM-R-004's other family
\(\theta(M^2z,M^2\tau)\). No all-polynomial arithmetic/automorphic
kernel identity, full `MainX`, selected \(g_j,e_j\), source period
\(H\), or shorter lift chain is asserted.

## References and exact source locators

Casalaina-Martin, S., & Kass, J. L. (2010). *A Riemann singularity
theorem for integral curves* (arXiv:0907.0212v2, 1 June 2010).
https://arxiv.org/pdf/0907.0212 . The smooth Riemann singularity
statement is recalled on printed p. 1. The determinant/Fitting
construction is Definition 3.1 and the ensuing paragraphs, pp. 9--10.
Proposition 3.3, p. 11, concerns an equal-characteristic test arc; its
elementary determinant idea is extended here by the written DVR
argument. No mixed-characteristic scope is attributed to that result.

Mumford, D. (1971). Theta characteristics of an algebraic curve.
*Annales scientifiques de l'École Normale Supérieure*, 4(2), 181--192.
https://www.numdam.org/article/ASENS_1971_4_4_2_181_0.pdf . Parity and
its quadratic law are on pp. 181--182, formula (*); the proof is in
§3, pp. 188--190. Only complex/characteristic-not-two parity is used.

National Institute of Standards and Technology. (n.d.). *Digital
Library of Mathematical Functions*, §21.2(ii), equations
21.2.5--21.2.7. https://dlmf.nist.gov/21.2 . These fix characteristic
and translation conventions. The parity identity follows directly
from the displayed defining series.

The Stacks Project Authors. (n.d.). *Determinants of complexes*,
Tag 0FJI. https://stacks.math.columbia.edu/tag/0FJI . The rank-zero
two-term determinant element and its quasi-isomorphism invariance are
used. *The relative dualizing sheaf*, Tag 0E6N.
https://stacks.math.columbia.edu/tag/0E6N . Relative duality and its
base-change compatibility are used.

Accepted intake: `RETURN_DP_MULT_checkpoint_06_20261121T0420Z/DP_MULT.tex`,
DP49 statement and trace-one polarization proof; DP59 proof (TS7)--(TS8),
symmetry and rigidified multiplication; DP62, odd-level canonical
translates. These are carried at their accepted status, not newly
proved. `Level.odd` was read directly in the recovered pinned source
module named above; no Lean execution is claimed.
