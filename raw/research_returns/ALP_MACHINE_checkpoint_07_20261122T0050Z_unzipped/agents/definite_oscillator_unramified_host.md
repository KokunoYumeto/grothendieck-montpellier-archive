# AM-DO-022: the full finite moved-vacuum identity on the repaired CM host

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`;
inherited reasoning effort not separately exposed; 21 November 2026 UTC.

This finding carries DP57's field and integral-action assertions at their
accepted status. It supplies a new finite Weil-phase comparison for the
explicit mixed CM theta construction of AM-DO-017–020. The comparison is
with the standard unitary splitting attached to the displayed characters,
not with an arbitrary representation having only some of the source's
axioms. The unchanged elliptic `VacIn` is not an input to this proof.

## 1. Statement with the exact product trace form

Put

\[
 E=\mathbf Q(\zeta_7),\quad \xi=(\zeta_7-\zeta_7^{-1})/7,
 \quad E'=E(i)=\mathbf Q(\zeta_{28}),\quad F'=(E')^+,
 \quad A=J\times J.
 \tag{DO22.1}
\]

DP57 proves that \(E'/F'\) is unramified at every finite place,
\(\mathcal O_{E'}=\mathcal O_E[i]\), and that the matrix
\(I=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\)
gives the integral action of \(i\) on \(A\). Its product principal
polarization has Rosati involution equal to conjugation on \(E'\).
Its CM type is

\[
                         \Phi'=\{1,3,9,15,17,23\}\pmod{28}.
 \tag{DO22.2}
\]

The trace coefficient for this exact lattice and polarization is

\[
                                  \boxed{\xi'=\xi/2.}
 \tag{DO22.3}
\]

For positive even ranks \(a,b\), let \(S=E'^a\), \(T=E'^b\)
have their identity Hermitian forms, and put

\[
 \Lambda_{00}=\operatorname{Hom}_{\mathcal O_{E'}}
                    (\mathcal O_{E'}^a,\mathcal O_{E'}^b).
 \tag{DO22.4}
\]

Its rational alternating form is
\(E_H(X,Y)=-\operatorname{Tr}_{E'/\mathbf Q}
  (\xi'\operatorname{tr}(Y^*X))\), with the convention
\(H\) linear in the first argument and \(E_H=\operatorname{Im}H\).
Use \(\psi_\infty(t)=e^{2\pi it}\), and the product-compatible
finite character \(\psi_f\). Let \(\omega_\chi\) be the standard
unitary Weil representation in this realized Heisenberg model. Its two
splitting characters satisfy

\[
 \chi_S|_{\mathbb A_{F'}^\times}=1,
 \qquad\chi_T|_{\mathbb A_{F'}^\times}=1,
 \tag{DO22.5}
\]

because \(a,b\) are even. In particular the globally trivial characters
are permitted. The unitary Hom action is \(X\mapsto hXg^{-1}\).
Character labels here use the recovered source convention
`LocalNewformFunction.splitFacO`: the source factor is the inverse
of \(\chi_T\) evaluated at a determinant root. In the conventional
Harris–Kudla–Sweet tensor labels used by Konno and Konno (2007),
§3.3 and Lemma 3.1, this is the pair
\((\xi,\xi')=(\chi_S,\chi_T^{-1})\), after the group and
Heisenberg conventions are identified as in corrected AM-DO-023.
This explicit labeling matters for nontrivial characters; it has no
effect on the trivial-character comparison proved below.

Use the trace-one element
\(w_0=-(\zeta_7+\zeta_7^2+\zeta_7^4)\), so
\(w_0+\bar w_0=1\). Let \(\phi_{00}\) be the actual finite
Schwartz input constructed in AM-DO-016 and AM-DO-018, with two copies
of the Jacobian input for each of the \(ab\) entries. For finite adelic
unitary elements \(g,h\), write

\[
 N=g\widehat{\mathcal O}_{E'}^a\cap E'^a,\qquad
 N'=h\widehat{\mathcal O}_{E'}^b\cap E'^b,
 \quad \Lambda_{N,N'}=\operatorname{Hom}_{\mathcal O_{E'}}(N,N').
 \tag{DO22.6}
\]

Let \(\phi_{N,N'}\) be the prescribed two normalized finite averages,
first moving the source lattice and then the target lattice, exactly
as in (DO18.3)–(DO18.7). Define the positive indices

\[
\begin{split}
 q_1&=[\Lambda_{N,0}:\Lambda_{N,0}\cap\Lambda_{00}],\\
 q_2&=[\Lambda_{N,N'}:\Lambda_{N,N'}\cap\Lambda_{N,0}].
\end{split}
 \tag{DO22.7}
\]

For determinant roots \(x/\bar x=\det g\),
\(y/\bar y=\det h\), the exact equality at **all finite places** is

\[
 \boxed{\omega_\chi(g,h)\phi_{00}
            =\chi_T(x)^{-1}\chi_S(y)\phi_{N,N'}.}
 \tag{DO22.8}
\]

The reversed order of the two prescribed averages gives the same vector.
The characters in (DO22.8) are evaluated at the roots, not at the
determinants. Changing a root by an idele of \(F'\) leaves the factor
unchanged by (DO22.5).

In particular, the ramified character of AM-DO-021 disappears after this
specified repair. It is not discarded: no finite place of the new relative
CM extension is ramified. At the places over 7 the extension is now
unramified quadratic, and the argument below computes the phase there.

## 2. Proof of the product lattice, polarization, and dyadic index

The \(\mathcal O_E\)-linear map

\[
          \mathcal O_E[i]\longrightarrow\mathcal O_E^2,
                       x+iy\longmapsto(x,y)
 \tag{DO22.9}
\]

is an isomorphism of free modules and intertwines multiplication by
\(i\) with \(I\). For arbitrary \(x,y,x',y'\in E\), taking
the relative trace gives

\[
\begin{split}
 &\operatorname{Tr}_{E'/\mathbf Q}
  \left[\frac{\xi}{2}(x+iy)(\bar x'-i\bar y')\right]\\
 &\hspace{15mm}=
      \operatorname{Tr}_{E/\mathbf Q}
             \left[\xi(x\bar x'+y\bar y')\right].
\end{split}
 \tag{DO22.10}
\]

Indeed the terms linear in \(i\) have relative trace zero and the
remaining terms have relative trace twice themselves. AM-R-004 proves
that the right side is the integral unimodular Riemann form of the
product Jacobian. Thus (DO22.10) proves perfection of the actual integral
trace pairing on \(\mathcal O_{E'}\), not merely a discriminant equality.
Equivalently \(\xi'\mathcal O_{E'}=\mathfrak D_{E'/\mathbf Q}^{-1}\).
The numerical check is

\[
 |N_{E'/\mathbf Q}(\xi')|=7^{-10}2^{-12}
                   =|d_{E'}|^{-1}.
 \tag{DO22.11}
\]

Here \(|N_E(\xi)|=7^{-5}\), the norm of \(\xi\) from
\(E'\) is its square, and \([E':\mathbf Q]=12\).
The cyclotomic discriminant is \(|d_{E'}|=7^{10}2^{12}\),
consistent with (DO22.10).

In the actual differential coordinates of AM-R-004 write
\(u=(u_1,u_2,u_3)\), \(v=(v_1,v_2,v_3)\), and

\[
                w_{i,+}=u_i+iv_i,\qquad w_{i,-}=u_i-iv_i.
 \tag{DO22.12}
\]

These are the two selected \(E'\)-eigencharacters over each old selected
\(E\)-embedding. Since
\(|u_i|^2+|v_i|^2=(|w_{i,+}|^2+|w_{i,-}|^2)/2\), the actual
positive Hermitian form is

\[
 H_A=\sum_{i=1}^3\frac{|u_i|^2+|v_i|^2}{G_i}
          =\sum_{i=1}^3\frac{|w_{i,+}|^2+|w_{i,-}|^2}{2G_i}.
 \tag{DO22.13}
\]

The eigenbasis change on each pair of differentials is
\(\left(\begin{smallmatrix}1&i\\1&-i\end{smallmatrix}\right)\),
whose determinant is \(-2i\). Across the three pairs its determinant
has normalized dyadic valuation 3. The eigenbasis is therefore not a
primitive dyadic basis of the product Hodge lattice. In particular

\[
 \partial_{w_{i,+}}=\tfrac12(\partial_{u_i}-i\partial_{v_i}),
 \qquad
 \partial_{w_{i,-}}=\tfrac12(\partial_{u_i}+i\partial_{v_i}).
 \tag{DO22.14}
\]

A total degree \(D\) change of derivative coordinates has the explicit
upper denominator bound \(2^D\); it need not attain that bound for a
particular polynomial. At 11 this change is integral and invertible.
No dyadic index or derivative denominator is removed by the field repair.

The trace-one semicharacter on the lattice in (DO22.9) is the product
of the two old trace-one semicharacters, by (DO22.10) and because \(w_0\)
acts diagonally. Thus its rigidified line is exactly
\(L_{w_0}\boxtimes L_{w_0}\). Its reduced seed is
\(\Sigma_{\rm tr}(u)\Sigma_{\rm tr}(v)\), or equivalently
\(c^2\sigma_q(u)\sigma_q(v)\), with the exact \(c\) of AM-R-006.

## 3. The local unramified comparison, including the splitting

We prove the part of (DO22.8) not supplied by AM-DO-020. Let \(k\)
be a finite completion of \(F'\) of odd residue characteristic, and
let \(L/k\) be its unramified quadratic extension in \(E'\). Let
\(\mathcal O,\mathcal O_L\) denote their integers.

### 3.1. Integral hyperbolic polarizations exist

The norm \(\mathcal O_L^\times\to\mathcal O^\times\) is
surjective. One elementary verification starts with the surjective norm
\(\mathbf F_{q^2}^\times\to\mathbf F_q^\times\). After a lift,
correcting by \(1+\pi^r z\) changes its norm modulo \(\pi^{r+1}\)
by \(1+\pi^r\operatorname{Tr}(z)\); the residue trace is
surjective. Successive correction and completeness give the claim.
Choose a unit \(z\) of norm \(-1\). Then \((z,1)\) is a
primitive isotropic vector of the identity Hermitian lattice of rank 2.
Unimodularity supplies a vector pairing to 1 with it. Subtracting one
half of that vector's norm times the isotropic vector makes the second
vector isotropic. Their pairing is a unit and their Gram determinant
is a unit, so they form an integral basis. Hence

\[
       (\mathcal O_L^{2m},I_{2m})\simeq H^{\perp m}
                 \quad\text{integrally.}
 \tag{DO22.15}
\]

Scaling a Hermitian form by a fixed nonzero skew scalar gives the same
integral isotropic direct-sum decomposition. Thus both even-rank factors
in our dual pair possess polarizations with integral direct summands.

The trace-lattice conductor hypotheses used in Pan's comparison are
satisfied. Let \(\lambda_k\) be the conductor exponent of
\(\psi_k=\psi_{\mathbf Q_p}\circ\operatorname{Tr}_{k/\mathbf Q_p}\).
Because \(L/k\) is unramified and \(\xi'\) generates the absolute
codifferent, \(v_L(\xi')=\lambda_k\). Pan's half-trace convention is
realized using the opposite skew form with coefficient \(-2\xi'\),
and duality exponents \(0,\lambda_k\). Since 2 is a unit, their sum
is exactly the unramified compatibility exponent in Pan (2001),
§3.1, (3.1.b). His lattice (3.2.c) is the actual selfdual Hom lattice.
Replacing both the symplectic form and the additive character by their
negatives, if needed to pass between his Heisenberg convention and
(DO18.5), transports the same representation. The scalar formulas
used below are independent of this simultaneous sign transport.

At these odd places the trace-one semicharacter is trivial on every
integral selfdual lattice under discussion: its defining half-pairing
is integral in the additive-character conductor convention and 2 is a
unit. Consequently the usual selfdual-lattice vacuum is the actual
trace-one vacuum.

### 3.2. Pure pullback agrees with the prescribed trivial-character splitting

First set \(\chi_S=\chi_T=1\). Polarize the target hyperbolic space
as \(T=X_T\oplus Y_T\), with its integral lattice decomposed in
the same way. The Hom symplectic space is polarized by

\[
 X=\operatorname{Hom}_L(S,X_T),\qquad
 Y=\operatorname{Hom}_L(S,Y_T).
 \tag{DO22.16}
\]

The whole source group preserves this polarization. In the Schrödinger
model on \(X\), it has the natural unitary action

\[
                 T_g\phi(x)=\phi(xg).
 \tag{DO22.17}
\]

There is no absolute-determinant factor in (DO22.17):
\(\det_k(X\mapsto Xg^{-1})
 =N_{L/k}(\det g)^{-b/2}=1\).
The associated lift to the metaplectic circle extension is the natural
Siegel-Levi splitting. The same assertion for a hyperbolic opposite
unitary space is stated in Hanzer (2011), Corollary 2.4, printed p.128;
its mixed-model form is equation (3.3), printed p.131.

We must identify (DO22.17) with the **fixed standard** splitting rather
than choosing it independently. Here is that identification. On the
standard compact source group, Pan (2001), Lemma 6.2, printed p.197,
gives \(\alpha\beta^Y=1\) for each determinant-section element
against a hyperbolic plane when its splitting character is trivial.
Tensor multiplicativity, §3.6, equation (3.6.e), gives the same result
against the whole even hyperbolic opposite space. Proposition 3.3 says
that \(\alpha\beta^Y\) is trivial on the compact special unitary
subgroup when the opposite dimension is even. The determinant map from
the standard compact unitary group onto \(L^1\) is surjective:
\(t\mapsto\operatorname{diag}(t,1,\ldots,1)\) is a section and
every norm-one \(t\) is a unit. These statements show that the fixed
standard splitting fixes the compact vacuum exactly, just as (DO22.17)
does.

The ratio of two splittings of the same metaplectic extension is a
continuous character of the source unitary group. This follows directly
by multiplying their group-law identities; both cover the same
symplectic action, so their ratio is central. The moving space is
isotropic by (DO22.15), and for these local unitary groups

\[
                        [U(S),U(S)]=SU(S).
 \tag{DO22.18}
\]

Thus the ratio factors through the determinant. The abelianization
assertion and the resulting uniqueness from the compact restriction
are exactly the unitary case of the proof of Pan's Theorem 3.4,
printed p.181. Its ramified exceptional determinant-index-two case is
excluded here because \(L/k\) is unramified. Since the ratio is 1 on
the compact subgroup and the latter surjects onto \(L^1\), it is
1 everywhere. This proves that (DO22.17) is the prescribed standard
trivial-character action on the entire source group. The same proof,
using a source hyperbolic polarization, identifies the target action.

This argument uses the published abelianization and splitting results
with their hypotheses stated. It does not derive equality from scalar
uniqueness alone: compact scalar calculation and determinant surjectivity
are the two additional steps that fix the scalar.

### 3.3. The one-factor average is exactly the Weil move

In (DO22.16) the original Hom lattice has the form \(P_0\oplus P_0^*\),
where star denotes the \(\psi_k\)-annihilator. After an arbitrary
source move \(g\), it has the form \(P_g\oplus P_g^*\), with
\(P_g=\{xg^{-1}:x\in P_0\}\). This follows either from the
perfect tensor pairing, or directly because the move is symplectic and
preserves each of the two polarized subspaces. The positive normalized
vacuum is

\[
                         v_P=\operatorname{vol}(P)^{-1/2}1_P.
 \tag{DO22.19}
\]

The proof of (DO20.6) is a calculation for *arbitrary dual position
lattices*. It does not require that the relative CM algebra be split
once a polarization of this form is supplied. For clarity, with
\(M=P\cap P_0\), \(u=[P:M]\), \(v=[P_0:M]\), the full
symplectic index is \(q=uv\). The position and momentum finite sums
send \(1_{P_0}\) to \(\sqrt{v/u}\,1_P\): the momentum sum is
\(v\) on \(P\) and zero elsewhere in \(P+P_0\), and exactly
one position class contributes there. Since
\(\operatorname{vol}(P)/\operatorname{vol}(P_0)=u/v\), the
normalized average sends \(v_{P_0}\) exactly to \(v_P\).
At odd residue characteristic all half-pairings on either integral
lattice are killed by \(\psi_k\), so this is precisely the prescribed
trace-one average.

Equation (DO22.17) has the same effect, with the same positive value on
the zero position. Therefore, in the original realized model as well,

\[
 I_{\Lambda_{N,0},\Lambda_{00}}\phi_{00}
                       =\omega_1(g,1)\phi_{00}.
 \tag{DO22.20}
\]

An arbitrary scalar used to identify the Schrödinger model cancels from
this vector equality. Reversing source and target and using the other
hyperbolic polarization proves

\[
 I_{\Lambda_{0,N'},\Lambda_{00}}\phi_{00}
                       =\omega_1(1,h)\phi_{00}.
 \tag{DO22.21}
\]

### 3.4. Covariance fixes the two-factor phase and the order

Let \(A_g\) denote the symplectic Hom action of \(g\) and let
\(A_h\) be that of \(h\). They commute, preserve the alternating
form, and commute with \(w_0\). Hence they preserve the defining
trace-one semicharacters. They send finite quotient representatives
bijectively to the corresponding moved quotient representatives and
preserve the indices. Heisenberg covariance therefore gives the exact
operator identity on the appropriate vacuum line

\[
 I_{\Lambda_{N,N'},\Lambda_{N,0}}
  =\omega_1(g,1)\,
       I_{\Lambda_{0,N'},\Lambda_{00}}\,
            \omega_1(g,1)^{-1}.
 \tag{DO22.22}
\]

There is no scalar in (DO22.22): substitute the actual finite sums term
by term, using \(\omega W_x\omega^{-1}=W_{A_gx}\), equality of
the \(\alpha\)'s, and the unchanged positive square root of the index.
Combining (DO22.20)–(DO22.22) yields

\[
\begin{split}
 \phi_{N,N'}
 &=I_{\Lambda_{N,N'},\Lambda_{N,0}}
                   I_{\Lambda_{N,0},\Lambda_{00}}\phi_{00}\\
 &=\omega_1(g,1)\omega_1(1,h)\phi_{00}
   =\omega_1(g,h)\phi_{00}.
\end{split}
 \tag{DO22.23}
\]

The reversed order gives \(\omega_1(1,h)\omega_1(g,1)\phi_{00}\),
the same vector because the unitary splittings commute. This proves the
required order equality without assuming that every triple of unrelated
selfdual lattices has trivial metaplectic triangle phase.

### 3.5. Restore the specified characters and determinant roots

At even ranks, a character \(\chi\) with \(\chi|_{k^\times}=1\)
defines a character \(\nu_\chi\) of \(L^1\) by

\[
           \nu_\chi(t)=\chi(z),\qquad z/\bar z=t.
 \tag{DO22.24}
\]

Existence of the root is Hilbert 90; independence follows because two
roots have quotient in \(k^\times\). Multiplicativity follows by
multiplying roots. In particular Pan's Lemma 6.2 evaluates the compact
splitting change at \((t-1)\delta\), whose quotient by its conjugate
is \(t\), where \(\bar\delta=-\delta\).

The ratio between the \(\chi\)-splitting and the trivial-character
splitting is a character of the moving group. The same compact
calculation, followed by (DO22.18) and determinant surjectivity, shows
that this character is exactly \(\nu_\chi\circ\det\) on the
whole group. On the source member our convention uses the
character \(\chi_T^{-1}\), equivalently the character on the
contragredient source determinant. Thus its factor is
\(\chi_T(x)^{-1}\). On the target it uses \(\chi_S\), giving
\(\chi_S(y)\). Applying these factors to (DO22.23) proves the
local assertion (DO22.8) with its exact root convention.

## 4. The relative split places, including residue characteristic two

AM-DO-020 proves (DO22.8) at every relative split place, using the
prescribed split normalization, the positive indicator value, and the
exact trace-one cancellation. Its proof includes residue characteristic
two and does not replace the half-pairing by zero there.

All places of \(F'\) above 2 are relative split. One direct check is
that the decomposition group of 2 in \(E/\mathbf Q\) is generated
by \(2\pmod7\), namely \(\{1,2,4\}\); it excludes conjugation
\(-1\pmod7\). Conjugation thus swaps the two primes of \(E\)
over 2. Any prime of \(E'\) above one of them is swapped to a prime
above the other. Consequently no prime above 2 is fixed by relative
conjugation. For a quadratic extension this is exactly splitting of
the prime in \(E'/F'\). This argument only identifies the local
splitting type; it does not repeat DP57's proof of unramifiedness.

Every remaining finite place is either relative split, covered by
AM-DO-020, or unramified quadratic of odd residue characteristic,
covered by §3. The local finite averages factor as products of their
primary components. Their indices multiply, their positive square
roots multiply, and the character factors multiply. The original
finite Schwartz vector factors as well. This proves the global finite
identity (DO22.8) and its reversed-order counterpart. ∎

## 5. Actual period, normalization, and arithmetic cost retained

Write \(\theta_0=\theta[0;0](0;\tau)\). In the actual product
coordinates of §2, apply the reading map of AM-DO-018 entry by entry.
Let \(F_{N,N'}\) be the two-average theta germ with initial seed
\((\Sigma_{\rm tr}\boxtimes\Sigma_{\rm tr})^{\boxtimes ab}\).
The exact whole-family identity is

\[
\begin{split}
 R\phi_{N,N'}&=\theta_0^{2ab}F_{N,N'},\\
 R(\omega_\chi(g,h)\phi_{00})
   &=\chi_T(x)^{-1}\chi_S(y)\theta_0^{2ab}F_{N,N'}.
\end{split}
 \tag{DO22.25}
\]

The equality is of entire holomorphic functions in the common reduced
gauge, so it holds after every fixed polynomial differential operator.
It is stronger than a nonzero value at a single adelic point.

All analytic norms below use the probability Haar measure on the
corresponding complex torus, as fixed and justified in AM-DO-017. They
are not automatically the automorphic quotient measure in a terminal
period. With that convention,

\[
 \|F_{N,N'}\|^2
          =\det(2Y)^{-ab}|\theta_0|^{-4ab},
 \qquad c_{\rm unit}=\theta_0^{2ab}\det(2Y)^{ab/2}.
 \tag{DO22.26}
\]

The finite Schwartz vector has norm one for the product rational
position measure; both normalized averages are isometries on their
vacuum lines. At a normalized nonarchimedean valuation \(v_p(p)=1\),
its values satisfy

\[
           v_p(\phi_{N,N'}(q_f))\ge-\tfrac12v_p(q_1q_2).
 \tag{DO22.27}
\]

This follows from the \((q_1q_2)^{-1/2}\) coefficient, because the
initial nonzero values and all translation/semicharacter values are
roots of unity and the remaining finite sum is integral. It is an
elementary bound, not an assertion that each coefficient attains it.

The fixed-embedding Gaussian envelope inherited from AM-R-004 and
AM-DO-018 is

\[
 |F_{N,N'}(U)|
    <49^{2ab}\sqrt{q_1q_2}\,
                         e^{\pi H_{\rm Hom}(U,U)/2}.
 \tag{DO22.28}
\]

For the alternative seed \((\sigma_q\boxtimes\sigma_q)^{\boxtimes ab}\),
replace the period \(\theta_0^{2ab}\) by
\((\theta_0c)^{2ab}\), divide the squared norm by \(|c|^{4ab}\),
and replace \(49^{2ab}\) by \((6125/16)^{2ab}\), using the
proved AM-R-006 bound. The dyadic eigenbasis cost (DO22.14) remains
additional if derivatives are expressed in \(E'\)-eigenforms.

To match the recovered source's opposite real additive-character sign,
transport the form and character together: use
\(\psi_{F'}=\psi_{\mathbf Q}^{-1}\circ\operatorname{Tr}_{F'/\mathbf Q}\)
and the corresponding opposite trace coefficient. Their composition
on the Heisenberg center is unchanged. This changes the old fixed
quadratic coefficient pin; it is part of the new mixed constructor,
not evidence that the old `StdPair.xi` or elliptic `VacIn` is satisfied.

## 6. Precisely which gate this closes

The result supplies one actual common-period moved family, both
prescribed finite averages with their exact covolume indices, its
standard unitary Weil realization for every finite adelic move, and
the equality of the two orders. It resolves the finite phase in
(DO19.1) on this explicitly repaired host at all even ranks.

The recovered theorem `thetaKernel_eq_jet_thC` in
`Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaKernelSplitPlacesEqJetClassicalTheta.lean`
transports a vacuum identity to
polynomial jets; its key hypothesis is an actual equality, rather
than mere nonvanishing. Equation (DO22.25) provides the mathematical
analogue of that hypothesis for this new mixed seed. No Lean build or
formal instantiation is claimed.

AM-K018 subsequently proves the full-cyclotomic Chern/source formal
gauge comparison for this underlying ordinary product of copies of
\(J\), including the actual primitive kernel at 11. This comparison
is used at its separately recorded proof-check status. It removes
the previously listed gauge gate for these ordinary products; it does
not assert that a reduced frame is integral or cover products with
conjugated \(E\)-actions.

The following requirements are still separate: the old elliptic
`VacIn`/fourth-tensor seed pin; the actual integral row module with its
specified coefficient type; the whole set of `AdmS` covolume equations;
membership of an arbitrarily selected row in the prescribed iterated
theta image; and the terminal-mass equation in THETA3 Part II G1.
Finite Weil equivariance is a concrete constructor result and cannot
substitute for any of those arithmetic equations. AM-DO-026 records
the more precise operator and class-kernel consequences.

## References and exact source use

Pan, S.-Y. (2001). Splittings of the metaplectic covers of some reductive
dual pairs. *Pacific Journal of Mathematics, 199*(1), 163–226.
https://msp.org/pjm/2001/199-1/pjm-v199-n1-p10-p.pdf
Used locators: §3.1, (3.1.a)–(3.1.b), printed pp.177–178;
§3.2, (3.2.c); Proposition 3.3, pp.179–180; Theorem 3.4 and especially
its unitary abelianization/uniqueness argument, p.181; §3.6, (3.6.e),
p.183; Lemma 6.2, p.197. The published abelianization and splitting
theorems are used, not claimed as newly reproved here.

Hanzer, M. (2011). Rank one reducibility for unitary groups.
*Glasnik Matematički, 46*(66), 121–148.
https://web.math.pmf.unizg.hr/glasnik/46.1/46(1)-12.pdf
Used locators: Theorem 2.3 and Corollary 2.4, printed pp.127–128;
equation (3.3), printed p.131. These give the natural polarized
pullback action. Its identification with the fixed standard splitting
is separately proved in §3.2 above.

Carried supplied result: `DP_MULT.tex`, Proposition DP57, accepted
unramified CM repair and endpoint realization, especially parts (a),
(b), and (d), and the proof of the integral \(\mathcal O_{E'}\)-action.
Local exact file: `sources/RETURN_DP_MULT_checkpoint_06_20261121T0420Z/DP_MULT.tex`.
Other carried results: AM-R-004, AM-R-006, AM-DO-017–020, ALP-LIFT-07–08,
at their separately recorded proof-check status.
