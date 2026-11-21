# DP49 — actual polarized theta germs on the genus-three Jacobian at 11

Date: 2026-11-21 UTC. Researcher: GPT-6 Astra Pro; effort is not exposed. This is a concrete local geometric application of DP46–DP48, together with an elementary nonvanishing result. It does not construct a shorter global theta-lift chain or prove nonvanishing of a path fixed by that global construction.

## 1. Concrete geometric data

Put \(p=11\), \(R=W(\mathbf F_{11^3})\), \(K=\operatorname{Frac}R\), and let

\[
C:y^2=x^7-1,\qquad J=\operatorname{Jac}(C)
\]

with the good integral model of DP22. Choose \(\zeta=\zeta_7\in R\), and let \(a\) be the covariant Jacobian automorphism induced by

\[
(x,y)\longmapsto(\zeta x,y),\qquad
a[P-\infty]=[\sigma(P)-\infty].
\]

Let \(\lambda\) be the canonical principal polarization. The CM action is integral, and \(a\) preserves \(\lambda\). Its Rosati involution is therefore

\[
a^\dagger=a^{-1}.
\tag{JT1}
\]

Set

\[
\eta=a+a^2+a^4,\qquad
w_0=-\eta.
\tag{JT2}
\]

Then \(w_0\) is an integral endomorphism and

\[
w_0+w_0^\dagger=1,\qquad w_0w_0^\dagger=2.
\tag{JT3}
\]

Equivalently, if \(\delta=1+2\eta\), then \(\delta^2=-7\) and \(w_0=(1-\delta)/2\). The polynomial expression in (JT2), rather than division by two, already proves integrality.

The two \(11\)-adic CM factors have character orbits

\[
\{1,2,4\},\qquad \{3,5,6\}.
\]

The first factor has dimension two, the second dimension one; each has height three. Write the latter as \(G\) and the former as \(H\). Both are connected, and the principal polarization identifies \(H\) integrally with the actual Cartier dual \(G^D\). Consequently

\[
\widehat J=G\times H
\tag{JT4}
\]

as an integral formal group with its polarized cross pairing.

In the Frobenius order

\[
(3,5,6)
\tag{JT5}
\]

the integral display of \(G\) has singleton type \(\{0\}\), with arbitrary unit arrows. Its actual dual has complementary type. Thus the exact primitive-kernel theorem DP46 applies to the actual formal factors of this Jacobian, without requiring its unit arrows to become one.

## 2. The polarized theta-germ conclusion

Let \(\mathcal P_\lambda\) be the integral symmetric polarization biextension on \(J\times J\), and put

\[
\mathcal L_{w_0}=(1,w_0)^*\mathcal P_\lambda.
\tag{JT6}
\]

This is the trace-one theta line. Its associated symmetric biextension is \(\mathcal P_\lambda\), as proved below. Fix an integer tensor power \(\kappa>0\) with \(11\nmid\kappa\), and any nonzero integral section germ \(f\) of \(\mathcal L_{w_0}^{\otimes\kappa}\), written in an integral formal frame at the origin. In particular, one may take the germ of any nonzero algebraic theta section that has been extended integrally to this model. No assumption that \(f(0)\) is a unit, or even nonzero, is made.

Use the actual unit-arrow Teichmüller coordinates and their normalized logarithms. Write \(X\) for the line coordinate and \(Y_1,Y_2\) for the dual logarithm coordinates. In the original covariant Jacobian character convention, the corresponding tangent directions have characters

\[
G:\ 3,\qquad Y_1:\ 2,\qquad Y_2:\ 1.
\tag{JT7}
\]

Choose \(u\in R^\times\) and a primitive vector \(v=(v_1,v_2)\in R^2\), and restrict the normalized theta germ to the additive-logarithm line

\[
X=ut,\qquad (Y_1,Y_2)=(v_1t,v_2t).
\tag{JT8}
\]

Require that the restricted integral algebraic prefactor be nonzero. There are two possibilities:

\[
\begin{array}{c|c|c|c}
\text{dual direction}&k& w_k& c_k=1/10-w_k\\ \hline
v_1\in R^\times&2&121/1220&1/1220\\
v_1\in11R,\ v_2\in R^\times&1&11/120&1/120
\end{array}
\tag{JT9}
\]

Here \(k\) is the intrinsic nilpotency length of the reduced dual tangent vector under the restricted \(11\)-power operation.

In the invariant product canonical gauge, write the restricted normalized theta germ as \(\sum_{n\ge0}A_nt^n\). Then

\[
v_{11}(n!A_n)\ge c_kn-\frac{s_{11}(n)}{10},
\qquad
\liminf_{n\to\infty}\frac{v_{11}(n!A_n)}n=c_k.
\tag{JT10}
\]

Here \(s_{11}(n)\) is the sum of the base-11 digits of \(n\). The same conclusion holds in any canonical gauge whose quadratic coefficient on that line is integral. For a completely arbitrary rational canonical gauge, let \(c t^2\) be its remaining quadratic correction after DP47's integral-frame adjustment. If \(c=0\), set \(r_c=-\infty\); otherwise put

\[
r_c=\frac{1/10-v_{11}(c)}2,\qquad R_c=\max(w_k,r_c).
\]

The exact weighted coefficient threshold is \(R_c\), and the exact factorial-slope limit is \(1/10-R_c\). If \(v_{11}(c)=-M<0\), it equals

\[
\frac{1/10-M}{2}<0.
\tag{JT11}
\]

Thus no rational canonical quadratic gauge improves the ordinary primitive mixed-line slope in (JT9). The best value in this family is the height-two primitive-pair value \(1/(11^2-1)=1/120\).

## 3. Nonzero restrictions exist in every primitive residue class

Fix any \(\bar u\in(R/11R)^\times\) and any nonzero \(\bar v\in(R/11R)^2\). There exist lifts \(u,v\) of these exact residues for which the restriction of the nonzero integral germ \(f\), including any integral unit frame factor, is not identically zero.

Consequently the nonvanishing hypothesis is attained in both rows of (JT9), and indeed in every prescribed primitive residue class. This does **not** imply that an individual path prescribed before inspecting \(f\) has nonzero restriction.

## 4. Proof of the actual CM display and polarized block

The smooth two-chart genus-three model, its Jacobian abelian scheme, and its integral cyclotomic action were proved in DP22. The differentials

\[
dx/y,\quad x\,dx/y,\quad x^2dx/y
\]

have pullback characters \(1,2,3\). Under the displayed covariant Abel–Jacobi convention these are also the characters on the tangent space of \(J\). The ordinary transpose of a scalar retains its value. Since \(\sigma\) fixes infinity and preserves effective divisors, it preserves the canonical theta polarization. This gives \(a^\vee\lambda a=\lambda\), hence (JT1).

Because \(11\equiv4\pmod7\), its multiplicative order modulo seven is three and its two nonzero-character orbits are exactly those in §1. The integral \(11\)-adic cyclotomic order is unramified, and its two Henselian factors give integral idempotents on \(J[11^\infty]\).

Here is a direct integral normal-form verification, adapting DP45 to these two orbits. Over \(R_n=R/11^n\), use the display of the connected group, or separately the connected factors established in DP22. Its Witt module \(P_n\) has total rank six. The operators

\[
e_b=\frac17\sum_{r=0}^{6}[\zeta]^{-br}a^r,
\qquad 1\le b\le6,
\tag{JT12}
\]

split it into free eigenspaces \(P_{b,n}\). The zeroth eigenspace is zero because \(\Phi_7(a)=0\). The semilinear Frobenius sends character \(b\) to character \(11b\); its linearization is invertible after inverting \(11\), so the free ranks are constant along each of the two length-three orbits.

Both orbit ranks are positive: the tangent quotient has a nonzero character \(1\) summand and a nonzero character \(3\) summand. If the common ranks on the two orbits are \(r_1,r_2\), then

\[
3r_1+3r_2=6,\qquad r_1,r_2\ge1,
\]

so \(r_1=r_2=1\). The exact Hodge quotient \(P_n/Q_n=\operatorname{Lie}J\) therefore forces \(Q_n\cap P_{b,n}=I_nP_{b,n}\) for \(b=1,2,3\), and \(Q_n\cap P_{b,n}=P_{b,n}\) for \(b=4,5,6\). In particular the orbit \((3,5,6)\) has exactly one selected line.

Choose generators in Frobenius order. The linearized normal-decomposition map \(V^{-1}\oplus F\) is an isomorphism and becomes a monomial matrix on these lines. Every arrow coefficient is therefore a Witt unit. The arrows of the singleton orbit have the form

\[
Fe_0=u_0e_1,\qquad
Fe_1=11u_1e_2,\qquad
Fe_2=11u_2e_0,\qquad u_i\in W(R)^\times.
\tag{JT13}
\]

Generators and units can be chosen compatibly as \(n\) increases, by lifting generators of each free rank-one summand; the Witt reductions are surjective and detect units. Passing to the inverse limit gives the actual integral unit-arrow model. This is an isomorphism of formal groups, not merely an isogeny with a potentially nonunit tangent map.

For completeness, connectedness also follows directly from the local field action. Each height-three factor has an action of the unramified cubic field up to isogeny. A nonzero étale quotient would have a rational Tate module of dimension a positive multiple of three. It would therefore have height three, making the entire factor étale and of dimension zero. Its actual dimension is one or two, a contradiction. This reasoning applies to both factors and their actual duals. It is also the connectedness argument used in DP22/DP45.

Rosati conjugation exchanges the two integral idempotents. The principal polarization is an isomorphism on \(11\)-divisible groups. DP47's direct idempotent argument therefore makes each same-factor biextension trivial and the cross pairing perfect. It identifies \(H\) with \(G^D\) integrally and the polarized formal biextension with the hyperbolic product of its two cross pairings. The dual of the singleton display is its actual complementary reciprocal-unit display. This proves (JT4)–(JT5) and the hypotheses needed for DP46–DP47.

The ordinary dual action \(a_G^D\) on this dual display retains the characters \(5,6\) in its two tangent positions. Under the polarization, the original Jacobian action on \(H\) is \((a_G^{-1})^D\), by Rosati. These become characters \(-5=2\) and \(-6=1\) modulo seven, proving (JT7). The restricted-power chain goes from character 2 to character 1 with a unit coefficient and then to zero, as DP46's ordinary dual arrows show. This also checks the intrinsic interpretation of the two rows of (JT9).

## 5. Proof of trace one and the actual theta pullback

The identity \(\Phi_7(a)=0\) gives

\[
\eta+\eta^\dagger=\sum_{r=1}^{6}a^r=-1.
\]

Direct multiplication gives

\[
\eta\eta^\dagger=3+\sum_{r=1}^{6}a^r=2.
\]

Therefore (JT3) holds and

\[
(1+2\eta)^2
=1+4\eta+4(-\eta-2)=-7,
\]

since \(\eta^2+\eta+2=0\). Both \(w_0\) and its adjoint are units at 11, though their individual invertibility is not needed for the trace-one argument.

To verify the theta-line identity in (JT6), use the two biextension addition laws. The associated symmetric biextension of \(\mathcal L_{w_0}\) at \(z,z'\) is

\[
\mathcal P_\lambda(z,w_0z')
\otimes\mathcal P_\lambda(z',w_0z).
\]

Symmetry and adjunction turn its second factor into
\(\mathcal P_\lambda(z,w_0^\dagger z')\). Adding in the second argument and using \(w_0+w_0^\dagger=1\) gives exactly \(\mathcal P_\lambda(z,z')\). Thus this trace-one line induces the actual principal polarization; the calculation has not substituted a guessed scalar exponential for the geometric line.

Apply the generalized DP47 to the actual unit-arrow polarized block. In an integral formal frame, its canonical normalized section is

\[
\widetilde f(S,Y)\,B(S,Y)^{-\kappa}
\exp Q_\kappa(\log_GS,\log_HY),
\tag{JT14}
\]

where \(\widetilde f\) is the original integral germ times an integral unit, \(B\) is the actual primitive display Poincaré splitting, and \(Q_\kappa\) is homogeneous quadratic. The source convention fixes the minus sign; the inverse convention changes it coherently and does not change its unit valuation. Since \(11\nmid\kappa\), the primitive coefficient is a unit.

On (JT8), the quadratic becomes \(ct^2\). DP46 gives the exact threshold \(w_k\) and factorial slope \(c_k\) for the actual arbitrary-unit primitive part. The proof of DP48 applies unchanged: it uses only that exact threshold, bounded nonzero restricted prefactors, and the bounded-multiplier exponential lemma, all supplied by DP46. Hence the threshold is \(\max(w_k,r_c)\) and (JT10)–(JT11) follow. In the invariant product gauge \(Q_\kappa=0\), so both rows of (JT10) are exact.

## 6. Proof of nonvanishing in every primitive residue class

Let \(f_1\in R[[S,Y_1,Y_2]]\) be a nonzero integral germ, possibly multiplied by an integral unit. Substitution by the inverse normalized logarithms is an automorphism of \(K[[X,Y_1,Y_2]]\). Thus

\[
F(X,Y)=f_1(E_G(X),E_H(Y))
\]

is nonzero. Let \(P_d\) be its first nonzero homogeneous component. It is a nonzero polynomial over \(K\). The inverse logarithms have identity tangent map, so this leading homogeneous component is also the corresponding leading component of \(f_1\); no denominator issue is needed for the nonvanishing argument.

The lifts of fixed residues \((\bar u,\bar v)\), with \(\bar u\ne0\) and \(\bar v\ne0\), form a nonempty full open box in \(K^3\). A nonzero polynomial over the infinite field \(K\) cannot vanish on such a box. One proves this by induction on the number of variables: a nonzero one-variable polynomial has finitely many roots, whereas every \(11\)-adic open ball is infinite; then view a multivariable polynomial as a polynomial in its last variable and apply the same fact to its coefficients.

Choose a lift in this box with \(P_d(u,v)\ne0\). The coefficient of \(t^d\) in \(F(ut,vt)\) is exactly \(P_d(u,v)\), so the restriction is nonzero. The fixed residue determines the same intrinsic length \(k\) throughout the box. This proves the assertion for every primitive residue class, including both \(k=1,2\).

If \(f_1\) comes from a nonzero algebraic section of an invertible sheaf on the integral Jacobian model, its local germ at the origin is nonzero: a section vanishing on a nonempty open set would vanish at the generic point and hence everywhere. Its image in the formal completion remains nonzero. Indeed the noetherian local ring is a domain, and the intersection of all powers of the completion ideal is zero by the local Krull intersection theorem (Stacks Project, Lemma 10.51.4, Tag 00IP, https://stacks.math.columbia.edu/tag/00IP); the formal completion therefore injects on that germ. This supplies the asserted algebraic-section application without a basepoint-free or primitive-leading-coefficient assumption. \(\square\)

## 7. Sources, dependency boundary, and interpretation

The curve and Jacobian inputs are DP22's actual two-chart construction and the FGA Picard representability/smoothness/properness locators already checked there. The exact display inputs are Zink, Astérisque 278 (2002), Theorem 5, p.131; Theorem 9, p.132; normal decomposition and dual display, Definition 19/(22), p.143. The integral idempotent and inverse-limit argument is the same proved argument as DP45, with the two length-three orbits and rank equation written explicitly above. Connectedness uses Tate 1967 §2.2, sequence (4), and the abelian-scheme and dual-height/dimension statements cited in DP22/DP45. These accepted primary inputs are not an RH audit.

The numerical kernel is DP46, the actual polarized trace-one identification is DP47, and the quadratic-gauge comparison is DP48. The recovered source's actual trace-one assumption is ExpConjConnectionIntegral.lean:40; its gauge and derivative conventions are CocycleRightZeroThd.lean:174–189.

The result now gives genuine normalized theta-germ derivative rates for an explicit higher-height polarized Jacobian block. It does not identify any prescribed global path with the directions constructed by the polynomial nonvanishing argument, nor identify a selected harmonic polynomial or minor with a single ordinary mixed-line derivative. It also does not satisfy the old induced-type Host of DP25. Those distinctions are the remaining scope limits; the local primitive Poincaré pullback is no longer an unspecified identity in this example.
