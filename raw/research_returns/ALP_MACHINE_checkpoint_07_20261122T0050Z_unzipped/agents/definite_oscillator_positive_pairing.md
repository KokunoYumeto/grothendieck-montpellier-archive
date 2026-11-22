# AM-DO-024: the direct-average sign, an exact vacuum pairing, and adjoints

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`;
inherited reasoning effort not separately exposed; 21 November 2026 UTC.

This result uses the repaired host and the **standard unitary splitting**
proved in AM-DO-022. It computes a theta-line pairing with its measure
normalization. It does not identify that pairing with the terminal
automorphic mass in THETA3 G1.

## 1. Statement with all normalizations

Put \(E'=\mathbf Q(\zeta_{28})\), \(F'=E'^{+}\), and use the
principally polarized CM abelian variety \(A=J^2\), with integral
trace coefficient \(\xi'=\xi/2\), constructed in DP57 and
AM-DO-022. Fix positive even integers \(a,b\). Let
\(S=E'^a\) and \(T=E'^b\) have positive identity Hermitian
forms. The underlying Hom symplectic space, its character, the
trace-one semicharacters, and its finite Schwartz vacuum \(\phi_{00}\)
are exactly those of AM-DO-022; normalize \(\|\phi_{00}\|=1\).

For \(g\in U(S)(\mathbf A_{F',f})\) and
\(h\in U(T)(\mathbf A_{F',f})\), write \(\Lambda_{00}\),
\(\Lambda_{10}\), \(\Lambda_{11}\) for the standard,
source-moved, and both-moved rational period lattices. Their actual
action is \(X\mapsto hXg^{-1}\). All lattices carry the same
trace-one rule \(\alpha(x)\), and its restrictions agree on
intersections. Write

\[
 q_0=[\Lambda_{11}:\Lambda_{11}\cap\Lambda_{00}],\qquad
 I_{ji}=q_{ji}^{-1/2}
       \sum_{x\in\Lambda_j/(\Lambda_i\cap\Lambda_j)}
                         \alpha(x)^{-1}W_x,
 \tag{DO24.1}
\]

where \(q_{ji}=[\Lambda_j:\Lambda_i\cap\Lambda_j]\) and the
square root is positive. On holomorphic theta functions replace
\(W_x\) by the reduced translation \(U_x\) of AM-DO-017.
For sign-valued \(\alpha\), the inverse in (DO24.1) equals
\(\alpha\), as in the source definition.

Let \(\omega_1\) be the standard splitting with both unitary
characters trivial. Then

\[
 \boxed{
 \omega_1(g,h)\phi_{00}
   =I_{11,00}\phi_{00}
   =I_{11,10}I_{10,00}\phi_{00}
   =I_{11,01}I_{01,00}\phi_{00}.}
 \tag{DO24.2}
\]

In particular the direct-average comparison has sign \(+1\).
Its finite Schwartz pairing is

\[
 \boxed{\langle\phi_{00},\phi_{11}\rangle=q_0^{-1/2},
        \qquad \|\phi_{11}\|=1.}
 \tag{DO24.3}
\]

The inner product is conjugate-linear in the first argument. For
general splitting characters \(\chi_S,\chi_T\), trivial on
\(\mathbf A_{F'}^\times\), and determinant roots
\(x/\bar x=\det g\), \(y/\bar y=\det h\), the formula is

\[
 \omega_\chi(g,h)\phi_{00}
       =\chi_T(x)^{-1}\chi_S(y)I_{11,00}\phi_{00}.
 \tag{DO24.4}
\]

The dependence is on these roots, not on evaluating the characters
at \(\det g,\det h\) themselves. This is the root convention
already fixed in AM-DO-009 and AM-DO-022.

Let \(F_{00}\) have initial seed
\((\Sigma_{\mathrm{tr}}\boxtimes\Sigma_{\mathrm{tr}})^{\boxtimes ab}\)
and put \(F_{11}=I_{11,00}F_{00}\). On the common complex torus
quotient by \(\Lambda_{00}\cap\Lambda_{11}\), integrate its
Hermitian norm density against **probability Haar measure**. With
\(Y=\operatorname{Im}\tau\) and
\(\theta_0=\theta[0;0](0;\tau)\),

\[
 \boxed{\langle F_{00},F_{11}\rangle
      =q_0^{-1/2}\det(2Y)^{-ab}|\theta_0|^{-4ab}.}
 \tag{DO24.5}
\]

Both norms squared are \(\det(2Y)^{-ab}|\theta_0|^{-4ab}\).
For the alternative seed
\((\sigma_q\boxtimes\sigma_q)^{\boxtimes ab}\), divide the
right-hand side and both squared norms by \(|c|^{4ab}\), where
the exact scalar \(\Sigma_{\mathrm{tr}}=c\sigma_q\) was
computed in AM-R-006. The period connecting the finite Schwartz
vacuum to that alternative seed is \((\theta_0c)^{2ab}\).

## 2. Positivity of the actual local matrix coefficient

We first prove

\[
                 \langle\phi_{00},\omega_1(g,h)\phi_{00}\rangle>0
 \tag{DO24.6}
\]

at every finite place. This is a statement about the fixed standard
splitting, rather than an arbitrary choice of a unit vector on each
vacuum line.

### 2.1. Relative split places

At a relative split place, AM-DO-020 identifies both group actions
with the normalized change of variables in a single Schrödinger
position space. It includes residue characteristic two and retains
the trace-one half-pairing there. In the model used in that proof,
the initial and moved normalized vectors are, up to the same
irrelevant unit scalar,

\[
 v_{P_0}=\operatorname{vol}(P_0)^{-1/2}\mathbf1_{P_0},\qquad
 v_P=\operatorname{vol}(P)^{-1/2}\mathbf1_P,
 \tag{DO24.7}
\]

for full position lattices. Their pairing is

\[
 \langle v_{P_0},v_P\rangle
   =\frac{\operatorname{vol}(P_0\cap P)}
          {\sqrt{\operatorname{vol}(P_0)\operatorname{vol}(P)}}>0.
 \tag{DO24.8}
\]

The quotient is independent of rescaling the position Haar measure.

### 2.2. Odd unramified quadratic places

Let \(L/k\) be the local unramified quadratic extension. The
positive identity lattices of even ranks \(a,b\) are integrally
hyperbolic, by the explicit norm-unit and half-adjustment argument in
AM-DO-022 §3.1. Choose those integral hyperbolic bases. Their lattice
stabilizers \(K_S,K_T\) are hyperspecial maximal compact subgroups.
The **standard trivial-character splitting fixes the initial vacuum**
under \(K_S\times K_T\), by AM-DO-022 §3.2, including its Pan
comparison and abelianization argument.

The Cartan decomposition for the split unramified unitary group gives

\[
 g=k_1a_\nu k_2,\qquad h=l_1b_\mu l_2,
 \tag{DO24.9}
\]

where \(k_i\in K_S\), \(l_i\in K_T\), and the middle
terms are diagonal in the selected hyperbolic bases, with entries
\(\varpi^{\nu_j},\varpi^{-\nu_j}\) and
\(\varpi^{\mu_j},\varpi^{-\mu_j}\). The local hypotheses and
these exact standard lattices/maximal split tori are recalled in Li,
Rapoport, and Zhang (2024), §§1 and 3.4; §4.1 explicitly invokes the
Cartan decomposition for \(K\backslash U(W_0)/K\). We use this
published decomposition, without claiming a new proof of it.

Since the source and target splittings commute, (DO24.9) and compact
invariance imply

\[
 \langle\phi_{00},\omega_1(g,h)\phi_{00}\rangle
       =\langle\phi_{00},\omega_1(a_\nu,b_\mu)\phi_{00}\rangle.
 \tag{DO24.10}
\]

Polarize the target as \(T=X_T\oplus Y_T\) in the same
hyperbolic basis. The associated position space is
\(\operatorname{Hom}_L(S,X_T)\). The whole source action
preserves this polarization and is the pure normalized pullback
identified with the standard splitting in AM-DO-022 §3.2. The target
element \(b_\mu\) is in the Siegel Levi for this polarization.
Its standard Weil operator is also a positive normalized pullback:
in the standard splitting formula its Bruhat index is zero and its
character factor is \(\chi_S=1\). The usual factor
\(|\det A|^{1/2}\), or its reciprocal when writing the inverse
change of variables, is positive. This is the polarized formula in
Hanzer (2011), Theorem 2.3 and Corollary 2.4, together with the mixed
model equation (3.3); the identification with the fixed splitting is
the separate argument in AM-DO-022, not a new normalization choice.

The initial lattice splits as the position lattice and its exact
dual because the trace coefficient is a codifferent generator. The
initial vacuum is therefore a normalized indicator as in (DO24.7).
The combined diagonal action sends it to another such normalized
indicator. Its coefficient is (DO24.8), which is strictly positive.
This proves (DO24.6) at an odd unramified quadratic place.

All relative dyadic places in this host are split, as proved in
AM-DO-022 §4. The preceding two cases thus cover every finite place.
The global matrix coefficient is a finite product of these positive
local coefficients: outside finitely many places the move is compact
and the coefficient is one. Consequently (DO24.6) holds globally.

## 3. The positive coefficient fixes the direct-average phase

By the covariance of the actual Weil representation and the
invariance of the trace-one rule under \(E'\)-linear isometries,
\(\omega_1(g,h)\phi_{00}\) belongs to the vacuum line of
\(\Lambda_{11}\). The vector \(I_{11,00}\phi_{00}\)
belongs to that same one-dimensional line. Both have norm one:
the former by unitarity and the latter by AM-DO-017. Thus they differ
by a unique scalar \(\lambda\) of absolute value one.

The direct-average coefficient is exactly

\[
 \langle\phi_{00},I_{11,00}\phi_{00}\rangle=q_0^{-1/2}.
 \tag{DO24.11}
\]

Indeed choose zero as the representative of the zero coset in
(DO24.1). That term contributes \(q_0^{-1/2}\). Every other
term is orthogonal to \(\phi_{00}\): if
\(x\notin\Lambda_{00}\), selfduality supplies
\(\lambda_0\in\Lambda_{00}\) with a nontrivial commutator
\(e^{2\pi i E_H(\lambda_0,x)}\). The two vectors are then
eigenvectors of the same unitary Heisenberg operator with distinct
eigenvalues. This is exactly the finite-pairing argument in
AM-DO-017; the common semicharacter on the intersection ensures that
there is no representative-dependent phase.

Both (DO24.6) and (DO24.11) are positive real numbers. Pairing
\(\omega_1(g,h)\phi_{00}=\lambda I_{11,00}\phi_{00}\)
with \(\phi_{00}\) therefore makes \(\lambda\) positive
real. Since \(|\lambda|=1\), it follows that \(\lambda=1\).
AM-DO-022 already proved that the actual Weil translate equals each
two-step average. This proves (DO24.2) and (DO24.3). Its exact
splitting-change formula proves (DO24.4).

The same finite orthogonality calculation on the common holomorphic
theta space gives
\(\langle F_{00},I_{11,00}F_{00}\rangle
 =q_0^{-1/2}\|F_{00}\|^2\).
AM-DO-017 proves that the probability-Haar norms on the two principal
quotients agree with their norms on the common finite cover. Inserting
the explicit seed norm from (DO22.26) proves (DO24.5). The
\(\sigma_q\) statement follows by multiplying both vectors by
\(c^{-2ab}\), whose contribution to a Hermitian pairing is
\(|c|^{-4ab}\). This completes the proof of all the stated
pairing and sign assertions. \(\square\)

This argument applies to these actual dual-pair orbit lattices. It
does not assert that the metaplectic triangle phase is one for three
arbitrary selfdual lattices. Neither does it cover the original
ramified \(\mathbf Q(\zeta_7)\) host with unchanged trivial
characters: AM-DO-021 computes a nontrivial compact sign there.

### A concrete rank-two to rank-four value on the repaired host

Take \(a=2,b=4\), \(\pi=2-\zeta_7\),
\(r=\pi/\bar\pi\),
\(N=r\mathcal O_{E'}\oplus\mathcal O_{E'}\), and
\(N'=\mathcal O_{E'}^4\). The two conjugate ideals generated by
\(\pi\) and \(\bar\pi\) remain coprime after the integral
extension from \(E\) to \(E'\). Their absolute norms are
\(127^2\), because \(N_{E/\mathbf Q}(\pi)=127\) and
\([E':E]=2\). For each of the four changed Hom entries,

\[
 \mathcal O_{E'}\cap r^{-1}\mathcal O_{E'}
       =\bar\pi\mathcal O_{E'},\qquad
 [\mathcal O_{E'}:\bar\pi\mathcal O_{E'}]
       =[r^{-1}\mathcal O_{E'}:\bar\pi\mathcal O_{E'}]=127^2.
 \tag{DO24.16}
\]

The remaining four entries are unchanged. Thus \(q_0=127^8\),
and (DO24.3)–(DO24.5) become

\[
 \langle\phi_{00},\phi_{N,N'}\rangle=127^{-4},\qquad
 \langle F_{00},F_{N,N'}\rangle
        =127^{-4}\det(2Y)^{-8}|\theta_0|^{-32}.
 \tag{DO24.17}
\]

The common analytic period is \(\theta_0^{16}\), and the
direct finite average has coefficient \(127^{-4}\) before its
root-of-unity summands. This example retains the two Jacobian factors
of the repaired host; omitting that doubling would give the different
\(127^{-2}\) coefficient of AM-DO-020 over the original host.

## 4. Exact adjoints of the finite operators

There is an additional operator identity that does not require the
special host. Let \(\Lambda_1,\Lambda_2\), their common
semicharacters, and their normalized theta lines satisfy AM-DO-017.
Then

\[
                       I_{21}^{*}=I_{12},\qquad
                       I_{12}I_{21}=1,\qquad I_{21}I_{12}=1.
 \tag{DO24.12}
\]

The adjoints use the actual normalized Hermitian forms on the two
lines, and the same identity holds in their finite Schwartz models.

**Proof.** Put \(\Gamma=\Lambda_1\cap\Lambda_2\),
\(q=[\Lambda_i:\Gamma]\), and realize both principal theta
lines inside the common space of sections for \(\Gamma\), with
its probability-Haar norm. The operators
\(\alpha_i(x)^{-1}U_x\), for \(x\in\Lambda_i/\Gamma\),
form a unitary representation of that finite group on this common
space. Its invariant subspace is exactly the principal theta line
\(H_i\). Therefore

\[
 P_i=\frac1q\sum_{x\in\Lambda_i/\Gamma}\alpha_i(x)^{-1}U_x
 \tag{DO24.13}
\]

is its orthogonal projection. In particular \(P_i=P_i^*\).
Equation (DO24.1) says \(I_{21}=\sqrt q\,P_2|_{H_1}\).
For \(f\in H_1\), \(g\in H_2\),

\[
 \langle I_{21}f,g\rangle
 =\sqrt q\langle P_2f,g\rangle
 =\sqrt q\langle f,g\rangle
 =\sqrt q\langle f,P_1g\rangle
 =\langle f,I_{12}g\rangle.
 \tag{DO24.14}
\]

This proves the adjoint identity. Both operators are nonzero
isometries between one-dimensional spaces by AM-DO-017, so they are
unitary inverses. The finite Schwartz proof is identical, using the
finite Heisenberg eigenrelations in place of the holomorphic
periodicity. \(\square\)

For the two-step moved family this gives the **actual reversed
operator**, with no unspecified constant:

\[
 (I_{11,10}I_{10,00})^*=I_{00,10}I_{10,11}.
 \tag{DO24.15}
\]

Together with (DO24.2), this is the finite-vacuum adjoint of the
standard Weil action. A general determinant-character factor in
(DO24.4) is conjugated, exactly as required by a unitary adjoint.
No automorphic quotient volume has been replaced by a theta-line
norm in this assertion.

## 5. Literal source obligations supplied

The recovered `Formalism/LocalToGlobal/KernelLattices/LateralTheory.lean`
defines `SignP` at lines 230–233 and `OrderP` at lines 235–238.
Equation (DO24.2) proves their mathematical analogues for the new
mixed-CM seed, with the stronger positive sign. The period and every
polynomial jet remain those in (DO22.25), so the comparison uses one
common seed scalar throughout.

The exact operator and pairing formulas are concrete inputs towards
`VacT`/`ClsK.Core`. They do not instantiate the old elliptic `VacIn`,
do not choose the prescribed arithmetic row lattice, and do not
identify the source `Btop` terminal functional with (DO24.5). In
particular a computed positive vacuum coefficient does not prove
the terminal-mass equation or all six `AdmS` predicates.

## References

Hanzer, M. (2011). Rank one reducibility for unitary groups.
*Glasnik Matematički, 46*(66), 121–148.
https://web.math.pmf.unizg.hr/glasnik/46.1/46(1)-12.pdf
Exact locators: Theorem 2.3 and Corollary 2.4, pp.127–128; equation
(3.3), p.131. Used through the standard-splitting comparison proved
in AM-DO-022.

Li, C., Rapoport, M., & Zhang, W. (2024). Arithmetic fundamental lemma
for the spherical Hecke algebra. *Manuscripta Mathematica, 175*, 1–51.
https://doi.org/10.1007/s00229-024-01572-0
Exact locators: §1 (odd residue characteristic and unramified
quadratic extension); §3.4 (split Hermitian form, standard selfdual
lattice, hyperspecial subgroup, and diagonal maximal split torus);
§4.1 (the Cartan decomposition on the corresponding double-coset
space). No arithmetic fundamental lemma from this paper is used.

Carried and separately checked: AM-DO-017, AM-DO-020, AM-DO-022,
AM-R-006, and the accepted DP57 host construction.
