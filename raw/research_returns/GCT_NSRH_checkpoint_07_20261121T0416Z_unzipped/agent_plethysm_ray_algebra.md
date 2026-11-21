# Actual polynomial highest-weight algebra for the F34 ray

Author: /root/rectangular_and_theta. Date: 2026-11-21 UTC.

This is a constructive supplement to agent_plethysm_dimension_gate.md. It identifies an actual ordinary highest-weight algebra behind its coin-count formula. It does not claim a new general plethysm rule, a nonstandard canonical basis, or priority for the classical slice calculation used below.

## 1. The algebra and its grading

Fix k≥2 and put \(V=\operatorname{Sym}^k\mathbf C^2\). Choose the divided basis
\[
v_i=x^{k-i}y^i/i!,\qquad 0\le i\le k.
\]
The raising operator \(E=x\partial_y\) satisfies \(Ev_i=v_{i-1}\) for i≥1 and \(Ev_0=0\).
The divided basis and every factorial denominator below are valid in characteristic zero. The construction is defined over the rational numbers and may then be base changed to the complex numbers.

In this note
\[
A=\operatorname{Sym}(V)=\mathbf C[v_0,\ldots,v_k]
\]
is the free symmetric algebra on these basis vectors. The symbols v_i are algebraically independent generators of A; the displayed binary forms only specify their basis and GL2 action. They must not be identified with their products in \(\mathbf C[x,y]\).

Extend E as the derivation D of A:
\[
D(v_0)=0,\qquad D(v_i)=v_{i-1}.
\]
Give A the bigrading
\[
\deg(v_i)=1,\qquad \operatorname{ind}(v_i)=i.
\]
An element of degree N and index r has diagonal GL2 weight \((kN-r,r)\). Its highest-weight subspace is its kernel under D. Define the ray algebra
\[
B=\bigoplus_{N\ge0}
  \{f\in A:\deg f=N,\ \operatorname{ind}f=N,\ Df=0\}.
\tag{S1}
\]
Multiplication preserves this condition, so B is a graded subalgebra. Ordinary characteristic-zero highest-weight theory identifies
\[
\dim B_N=
[\operatorname{Sym}^N(\operatorname{Sym}^k\mathbf C^2):
S_{((k-1)N,N)}\mathbf C^2]
=c_k(N).
\tag{S2}
\]
Here the highest-weight inequality holds because k≥2. This is the same classical multiplicity family in F34.

## 2. Explicit polynomial generators

In \(A[v_0^{-1}]\) put \(t=v_1/v_0\), so \(D(t)=1\). For \(2\le i\le k\) define
\[
f_i=v_0^{i-1}
       \sum_{j=0}^{i}\frac{(-t)^j}{j!}\,v_{i-j}.
\tag{S3}
\]
Every f_i actually belongs to A. For j≤i-1 its summand is
\[
\frac{(-1)^j}{j!}\,
v_0^{\,i-1-j}v_1^jv_{i-j},
\]
and the j=i summand is \((-1)^iv_1^i/i!\). All exponents are nonnegative.

Each term has degree i and index i. Differentiating the sum in (S3), the derivative of \((-t)^j/j!\) cancels the term obtained by differentiating \(v_{i-j+1}\) in the preceding index; the final derivative \(D(v_0)\) vanishes. Since D fixes v_0, this proves
\[
D(f_i)=0,\qquad
\deg(f_i)=\operatorname{ind}(f_i)=i.
\tag{S4}
\]
For example
\[
f_2=v_0v_2-\tfrac12v_1^2,\qquad
f_3=v_0^2v_3-v_0v_1v_2+\tfrac13v_1^3.
\]
Thus every f_i is an actual highest-weight vector on the required ray.

## 3. Exact localized coordinate calculation

The formula is triangular:
\[
f_i=v_0^{i-1}v_i+
       \text{a polynomial in }v_0,\ldots,v_{i-1}.
\]
Since v_0 is invertible in the localization, successive substitution gives an algebra isomorphism
\[
A[v_0^{-1}]
=\mathbf C[v_0,v_0^{-1},t,f_2,\ldots,f_k].
\tag{S5}
\]
More formally, \(v_0,t,f_2,\ldots,f_k\) are obtained from the free localized coordinates \(v_0,v_0^{-1},v_1,\ldots,v_k\) by an invertible triangular change: \(v_1=t v_0\), and each successive v_i is uniquely solved from its displayed formula with unit leading coefficient \(v_0^{i-1}\). In particular these new coordinates have no algebraic relation except \(v_0v_0^{-1}=1\).

In these coordinates D fixes \(v_0,f_2,\ldots,f_k\) and sends t to one. Hence D is the ordinary partial derivative in t, and in characteristic zero
\[
A[v_0^{-1}]^D
=\mathbf C[v_0,v_0^{-1},f_2,\ldots,f_k].
\tag{S6}
\]
This calculation is explicit; no unverified assertion about the global invariant ring \(A^D\) is needed.

## 4. The ray algebra is genuinely polynomial

The monomial
\[
v_0^a f_2^{x_2}\cdots f_k^{x_k},
\qquad a\in\mathbf Z,\ x_i\in\mathbf Z_{\ge0},
\]
has
\[
\deg-\operatorname{ind}=a.
\]
The coordinates in (S6) are algebraically independent and homogeneous. Therefore its homogeneous component with degree equal to index has a=0. It follows that the localized invariant algebra on this ray is exactly \(\mathbf C[f_2,\ldots,f_k]\).

Every f_i is already polynomial in A, so intersecting with the original unlocalized algebra loses nothing. Thus
\[
\boxed{B=\mathbf C[f_2,\ldots,f_k],\qquad \deg f_i=i.}
\tag{S7}
\]
Its actual monomial basis consists of products \(\prod f_i^{x_i}\), and the degree-N basis is parametrized by
\[
2x_2+\cdots+kx_k=N.
\]
This constructs the counting basis in the actual highest-weight multiplicity algebra. It is not an arbitrary set of the same cardinality and does not evaluate c_k(N) first.

This is compatible with the cited classical two-row identity in PPS, Lemma 1.3, p.2; that identity and F34's coefficient formula remain known source applications. The construction here explains an ordinary algebra realizing the specialized rule.

## 5. What this supplies, and what it does not

As a scheme, \(\operatorname{Spec}B\) is affine \((k-1)\)-space with the specified positive grading \(2,\ldots,k\); \(\operatorname{Proj}B\) is the corresponding weighted projective scheme. The degree-N part of the affine scheme's graded coordinate ring has exactly the required highest-weight multiplicity. No unproved identification of arbitrary coherent and constructible cohomology is used. The graded Hilbert series is
\[
\prod_{i=2}^k(1-z^i)^{-1}.
\]
The exponent simplex is the one in F34 and has dimension k-2. Thus the positive algebra and the necessary dimension lower bound concern the very same actual multiplicities.

The monomial multiplication constants in this particular algebra are one. This is not the specified VIII nonstandard multiplication/comultiplication basis. The choice of raising operator and coordinates fixes an ordinary highest-weight convention, and no theta functor or arithmetic Frobenius comparison is asserted.

There are k−1 generators, and their elementary explicit formulas have total size polynomial in the numerical k. This does not make them polynomial in log k. The coherent construction therefore does not evade either the succinct dimension obstruction or the fully binary output-length obstruction proved in F34.

All calculations in (S1)–(S7) are proved here directly. A fresh independent review remains to be recorded before treating this supplement as checked beyond the author.

