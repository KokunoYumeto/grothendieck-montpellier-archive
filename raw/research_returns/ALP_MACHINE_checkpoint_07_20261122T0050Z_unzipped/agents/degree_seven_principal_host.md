# AM-K030 — an explicit principal product host for the degree-seven character repair

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/kummer_extension`, 21 November 2026 UTC. Inherited reasoning effort is not separately exposed.

AM-K029 supplies the literal unramified `IsEtaT` character on an induced-type degree-84 CM field. This finding supplies its actual integral principally polarized ordinary-Jacobian host. The identification is an isomorphism of principally polarized complex abelian varieties, with a full integral CM action. It is stronger than an isogeny or a rational trace-form comparison.

Keep
\[
 E_0=\mathbb Q(\zeta_{28}),\quad F_0=E_0^+,\quad
 \Phi_0=\{1,3,9,15,17,23\},\quad A=J^2,
\]
where \(J:y^2=x^7-1\) has its actual principal polarization. Let B be the unique degree-seven subfield of \(\mathbb Q(\zeta_{29})\), let \(K=E_0B\), and let \(F=F_0B\). The induced type \(\Psi\) consists of all seven lifts of every embedding in \(\Phi_0\).

Accepted DP57 and AM-DO-022 identify A with the type-\(\Phi_0\) CM torus whose lattice is \(\mathcal O_{E_0}\) and whose exact principal trace coefficient is
\[
 \xi_0=\frac{\zeta_7-\zeta_7^{-1}}{14}.
\tag{PH1}
\]
All sign conventions below use that same alternating form. Nothing changes its source/target Hom convention.

## 1. An explicit selfdual normal basis

Set \(\zeta=\zeta_{29}\),
\[
 H=\{1,12,17,28\}\subset(\mathbb Z/29\mathbb Z)^\times,
 \qquad C_i=2^iH\quad(i\in\mathbb Z/7\mathbb Z),
\]
and define the Gaussian periods
\[
             \eta_i=\sum_{h\in H}\zeta^{2^ih}.
\tag{PH2}
\]
The integer 2 has order 28 modulo 29, and H is its subgroup of order four. In particular H contains \(-1\), so the periods and B are real. Let \(\sigma\) be the generator of \(\operatorname{Gal}(B/\mathbb Q)\) induced by \(\zeta\mapsto\zeta^2\). Then \(\sigma\eta_i=\eta_{i+1}\).

The following seven elements are completely explicit:
\[
 \begin{split}
  a&=(-8,-4,-2,-5,-2,-4,-4),\\
  e_0&=\frac1{29}\sum_{i=0}^6a_i\eta_i,\qquad
  e_j=\sigma^j(e_0)\quad(0\le j\le6).
 \end{split}
\tag{PH3}
\]

### Theorem PH4

Let \(\mathfrak p\) be the unique prime of B above 29. Then
\[
 \mathfrak D_{B/\mathbb Q}=\mathfrak p^6,
 \qquad \mathcal A_B:=\mathfrak p^{-3},
 \qquad
 \mathcal A_B=\bigoplus_{j=0}^6\mathbb Z e_j,
 \qquad \operatorname{Tr}_{B/\mathbb Q}(e_je_k)=\delta_{jk}.
\tag{PH4}
\]
Every \(e_j\) has \(\mathfrak p\)-valuation exactly \(-3\), and
\(\operatorname{Tr}_{B/\mathbb Q}e_j=1\).

**Proof of the ramification and trace identities.** The prime 29 is totally ramified in \(\mathbb Q(\zeta)\), and hence is totally ramified in its degree-seven subfield B. There are no other ramified primes. This extension is tame because \(29\nmid7\); the different exponent is \(7-1=6\). These are the standard cyclotomic and tame-different facts; precise references appear below.

The sum of the seven periods is \(-1\). Therefore
\(\operatorname{Tr}\eta_i=-1\). To compute \(\operatorname{Tr}(\eta_i\eta_j)\), sum the products over the seven simultaneous translates of the two cosets. The coefficient of \(\zeta^t\) is constant for nonzero residues t, since multiplication by any nonzero residue permutes all terms. If \(i=j\), there are 28 terms with exponent zero: for each of the seven cosets, there are four ordered pairs \((x,-x)\). The remaining 84 terms distribute three to every nonzero residue. If \(i\ne j\), there is no exponent-zero term and all 112 terms distribute four to every nonzero residue. Hence
\[
                  \operatorname{Tr}(\eta_i\eta_j)=29\delta_{ij}-4.
\tag{PH5}
\]
In particular the periods are linearly independent, their trace determinant is \(29^6\), and, by the different calculation, they are an integral basis of \(\mathcal O_B\).

For the vector a in (PH3), direct integer multiplication gives
\[
 \sum_i a_i=-29,\qquad
 \sum_i a_i a_{i+k}=\begin{cases}145&k=0,\\116&k\ne0.\end{cases}
\tag{PH6}
\]
One may check the shorter equivalent computation with
\(b=a+4(1,\ldots,1)=(-4,0,2,-1,2,0,0)\): its sum is \(-1\), and its cyclic correlations are 25 at zero and \(-4\) elsewhere. Combining (PH5) and (PH6) yields
\[
 \operatorname{Tr}(e_0e_k)
 =\frac{29\sum_i a_i a_{i-k}-4(\sum_i a_i)^2}{29^2}
 =\delta_{0k}.
\tag{PH7}
\]
The trace-one assertion follows from \(\operatorname{Tr}\eta_i=-1\). Galois invariance gives all entries in (PH4).

**Proof of membership in the square-root inverse different.** Write
\[
             P(X)=\sum_i a_i\sum_{h\in H}X^{(2^ih\bmod29)},
\]
using representatives in \(\{1,\ldots,28\}\). The exact polynomial identity needed for the local check is
\[
\begin{split}
 P(1+T)\equiv T^{16}\bigl(&1-8T-13T^2+2T^3+7T^4-14T^5
 +14T^6-5T^7\\
 &-12T^8+6T^9-4T^{10}+4T^{11}-8T^{12}\bigr)\pmod{29}.
\end{split}
\tag{PH8}
\]
This is a 29-term binomial computation; the accompanying certificate verifies every coefficient, not just the first nonzero one. In the completion of \(\mathbb Q(\zeta)\) at 29, \(t=\zeta-1\) has valuation one and 29 has valuation 28. Equation (PH8) shows that \(P(\zeta)\) has valuation exactly 16: all terms of lower degree have valuation at least 28, its degree-16 coefficient is a unit, and all higher-degree terms have strictly larger valuation. The extension \(\mathbb Q(\zeta)/B\) has ramification degree four, so
\[
                    v_{\mathfrak p}(P(\zeta))=4,
                    \qquad v_{\mathfrak p}(e_0)=4-7=-3.
\tag{PH9}
\]
At every other finite prime, e₀ is integral because its only rational denominator is 29. The same statements hold for all its conjugates. Thus
\(L:=\sum\mathbb Z e_j\subset\mathcal A_B\).

The trace-dual of a fractional ideal I is
\(I^*=\mathfrak D_{B/\mathbb Q}^{-1}I^{-1}\). Consequently
\(\mathcal A_B^*=\mathcal A_B\). Equation (PH7) says \(L^*=L\). Taking duals of \(L\subset\mathcal A_B\) gives
\(\mathcal A_B\subset L\), proving equality. This finishes the proof. No classification of positive unimodular lattices, approximate lattice search, or unproved integral-normal-basis assertion is needed. ∎

## 2. A positive generator and an actual integral CM action

Define
\[
 \pi_B=N_{\mathbb Q(\zeta)/B}(1-\zeta)
       =\prod_{h\in H}(1-\zeta^h)
       =4-2\eta_0+\eta_4.
\tag{PH10}
\]
The last identity is obtained by multiplication and the relation
\(\sum_i\eta_i=-1\); the certificate checks it exactly in the cyclotomic algebra.

The factors with exponents \(h\) and \(-h\) multiply to
\(|1-\zeta^h|^2>0\). This remains true at every real embedding of B. Thus \(\pi_B\) is totally positive. Norm transitivity and
\(N_{\mathbb Q(\zeta)/\mathbb Q}(1-\zeta)=29\) give
\[
              N_{B/\mathbb Q}\pi_B=29,
              \quad \mathfrak p=(\pi_B),
              \quad \mathcal A_B=\pi_B^{-3}\mathcal O_B.
\tag{PH11}
\]

Multiplication by any \(\beta\in\mathcal O_B\) on the basis e gives an integral matrix: \(\mathcal A_B\) is an \(\mathcal O_B\)-ideal. Its entries are explicitly
\[
                 (M_\beta)_{jk}=\operatorname{Tr}(\beta e_k e_j),
\tag{PH12}
\]
and are symmetric. The matrices give a faithful ring embedding
\(\mathcal O_B\hookrightarrow M_7(\mathbb Z)\), with every B-element self-adjoint for the standard Euclidean form. As an optional directly usable generator check, multiplication by \(\eta_0\) is
\[
 M_{\eta_0}=\begin{pmatrix}
 -2&0&-1&0&0&0&-1\\
 0&0&0&-1&0&0&1\\
 -1&0&0&1&0&1&-1\\
 0&-1&1&1&0&1&0\\
 0&0&0&0&0&-1&0\\
 0&0&1&1&-1&0&1\\
 -1&1&-1&0&0&1&0
 \end{pmatrix}.
\tag{PH13}
\]
The conjugate-period matrices are obtained by conjugating this matrix by the cyclic permutation \(e_j\mapsto e_{j+1}\). Since the periods form an integral basis, these matrices specify the full \(\mathcal O_B\)-action. The characteristic polynomial is
\[
 X^7+X^6-12X^5-7X^4+28X^3+14X^2-9X+1.
\tag{PH14}
\]
Neither the characteristic polynomial nor a numerical eigenvalue computation is being used to infer the integral-lattice theorem; it was proved above.

## 3. The actual product principal polarization

The discriminants of E₀ and B are coprime, and the degrees 12 and 7 are coprime. The integral-compositum theorem therefore gives
\[
            \mathcal O_K=\mathcal O_{E_0}\otimes_{\mathbb Z}\mathcal O_B,
 \qquad |d_K|=|d_{E_0}|^7 |d_B|^{12}
                  =2^{84}7^{70}29^{72}.
\tag{PH15}
\]
Consider the full lattice
\[
       \Lambda=\mathcal O_{E_0}\otimes_{\mathbb Z}\mathcal A_B
               =\pi_B^{-3}\mathcal O_K\subset K.
\tag{PH16}
\]
It is stable under \(\mathcal O_K\). On pure tensors define the alternating form by the product of the old principal alternating form and the real trace pairing of B. Equivalently, in K it is the trace form with coefficient \(\xi_0\). For arbitrary \(x_j,y_j\in E_0\), the exact identity is
\[
 \operatorname{Tr}_{K/\mathbb Q}
  \left(\xi_0\Bigl(\sum_jx_je_j\Bigr)
                    \overline{\Bigl(\sum_ky_ke_k\Bigr)}\right)
       =\sum_{j=0}^6\operatorname{Tr}_{E_0/\mathbb Q}
                           (\xi_0x_j\bar y_j).
\tag{PH17}
\]
It follows directly from (PH4), because conjugation fixes B. Thus the tensor alternating form is integral and unimodular on \(\Lambda\). Its positivity follows from the positivity of the old Hermitian form and of the real trace form. With the induced complex structure of \(\Psi\), the map
\[
         (x_0,\ldots,x_6)\longmapsto\sum_jx_je_j
\tag{PH18}
\]
is an isomorphism of polarized complex tori
\[
      (A^7,\lambda_A^{\boxtimes7})
           \simeq (K\otimes\mathbb R/\Lambda,\lambda_\Lambda)
           \simeq (J^{14},\lambda_J^{\boxtimes14}).
\tag{PH19}
\]
For the complex-linearity assertion, B acts through its regular real representation on the seven copies; E₀ supplies the same complex structure on each copy. Diagonalizing that real representation gives exactly all seven lifts of every old selected embedding. This is the stated induced type, not a change to conjugate Jacobian factors.

The commuting integral actions of \(\mathcal O_{E_0}\) and \(\mathcal O_B\), together with (PH15), supply the full integral \(\mathcal O_K\)-action on the actual product. Rosati acts as conjugation on E₀ by DP57 and as the identity on B by (PH12); it is therefore complex conjugation on K. The field degree is \(84=2\dim J^{14}\), so this is a full CM action.

If the source uses the standard lattice \(\mathcal O_K\), transport (PH16) by multiplication by \(\pi_B^{-3}\). The exact coefficient then becomes
\[
             \boxed{\xi_K=\xi_0\pi_B^{-6}.}
\tag{PH20}
\]
Since \(\pi_B\) is totally positive, this has the same selected positivity signs. Moreover
\[
        \xi_K\mathcal O_K=\mathfrak D_{K/\mathbb Q}^{-1},
       \qquad |N_{K/\mathbb Q}\xi_K|
                      =2^{-84}7^{-70}29^{-72}.
\tag{PH21}
\]
The ideal equality also follows from the established perfect trace pairing, so it is stronger than a mere equality of absolute norms. The factor \(\pi_B^{-6}\) is part of the new host data. Keeping the old \(\xi_0\) while silently replacing \(\Lambda\) by \(\mathcal O_K\) would give the wrong principal lattice.

## 4. The theta line and the CM coordinate comparison

Use the same trace-one element
\[
                      w_0=-(\zeta_7+\zeta_7^2+\zeta_7^4)
                      \quad(w_0+\bar w_0=1).
\]
It acts diagonally in (PH18). Equation (PH17) splits its actual trace-one semicharacter into the product of the old semicharacters. Thus the rigidified symmetric principal line is exactly the external product of the fourteen ordinary Jacobian trace-one lines. With the normalization of AM-R-006 and AM-LIFT-08, transport the already fixed product section through (PH18). Its actual reduced germ in product coordinates is
\[
        \prod_{r=1}^{14}\Sigma_{\mathrm{tr}}(u^{(r)})
            =c^{14}\prod_{r=1}^{14}\sigma_q(u^{(r)}).
\tag{PH22}
\]
Here \(\sigma_q=u_1u_3-u_2^2+\cdots\), and c is the already fixed algebraic scalar. In particular its order of vanishing at the origin is 28. No theta-null unit is asserted. This is the line at the invariant characteristic \(2\infty\), not the distinct non-effective translated characteristic.

Let \(\tau_0,\ldots,\tau_6\) be the seven real embeddings of B and put
\[
                        U_{kj}=\tau_k(e_j).
\tag{PH23}
\]
Equation (PH4) says \(U^tU=I_7\). Hence U is a real orthogonal matrix, \(U^{-1}=U^t\), and \(\det U=\pm1\). Write the seven A-copy coordinates as \((u_{i,j},v_{i,j})\), \(i=1,2,3\), \(j=0,\ldots,6\), and define
\[
 w_{i,\pm,j}=u_{i,j}\pm i v_{i,j},\qquad
 z_{i,\pm,k}=\sum_{j=0}^6U_{kj}w_{i,\pm,j}.
\tag{PH24}
\]
These are full K-eigenvectors for the actual induced CM action. The Hermitian metric is exactly
\[
 H=\sum_{i,j}\frac{|u_{i,j}|^2+|v_{i,j}|^2}{G_i}
   =\sum_{i,\pm,k}\frac{|z_{i,\pm,k}|^2}{2G_i}.
\tag{PH25}
\]
Thus the B-diagonalization itself has no archimedean operator-norm loss.

At every prime away from 29, all entries of U and \(U^{-1}\) are integral. At 11, (PH24) is consequently an integral invertible change of the primitive Hodge eigenbasis, including its old \(\pm i\) blocks, since 2 is a unit. This proves a precise integral comparison at 11, not merely an algebraic splitting of de Rham cohomology. AM-K018 then applies to this ordinary \(J^{14}\) product: the central \(\zeta_7\)-action has no invariant holomorphic quadratic form, and its full-CM Chern/reduced-gauge comparison is unchanged. No claim is made for the conjugate-factor products outside that lemma's scope.

At 29, every entry of U has normalized valuation \(-3/7\), by (PH9); its inverse has the same bound. A homogeneous derivative of degree D transported by this matrix therefore has coefficient valuations at least \(-3D/7\). This is an upper bound on the possible denominator, not a claim that every derivative attains it. The old \(\pm i\) coordinate change retains its dyadic denominator bound \(2^D\). The additional standard-lattice rescaling in (PH20), if used to choose logarithmic coordinates, must also be included explicitly; it is a diagonal multiplication by the displayed conjugates of \(\pi_B^{\pm3}\). All these diagonal factors are units at 11.

This section identifies the line, product section, metric, and local coordinate change. It does not assert that the old selected-Schur upper-bound witnesses retain their old individual CM weight after the seven-copy change. The common joint integral lower estimate can be transported through an integral invertible 11-coordinate change; a new selected upper witness needs its own weight calculation.

## 5. Finite-level costs that change under the repair

The relative CM extension K/F remains unramified at every finite place by AM-K029. At 29 it is split, because 29 splits completely in E₀. Nevertheless the absolute real field F has six primes above 29, each with residue field \(\mathbb F_{29}\) and absolute ramification index seven. Rational 29 is therefore **not** a uniformizer of these local real fields.

For example, for the standard split rank-a compact group at all six places, a principal congruence subgroup defined by the rational ideal \((M)\), with \(M=29^e\) and \(e\ge1\), has the exact index
\[
     I_a^{\mathrm{new}}(M)
        =M^{42a^2}\prod_{i=1}^a(1-29^{-i})^6.
\tag{PH26}
\]
Indeed the local residue length is \(7e\), so each local index is
\(29^{7ea^2}\prod_{i=1}^a(1-29^{-i})\), by reduction to
\(\operatorname{GL}_a(\mathbb F_{29})\) and the successive additive matrix kernels. Multiplying six places gives (PH26). This statement concerns that precisely defined principal subgroup; it is not an automatic identification of every source level symbol with rational M.

The old 29 half-orbit construction still has to be instantiated with the new actual lattice and its exact \(\alpha\bar\alpha=M\) data. The good-prime jet-surjectivity argument of AM-K022 applies at 11 once those data are specified, but the former absolute-uniformizer and degree-six mass formulas cannot simply be copied. Terminal `qOf` depths must likewise retain their actual local valuations.

Combining this theorem with AM-K029 gives an actual product principal CM host and its literal auxiliary character. It does not settle the independent original `IsTen`, full real/rank/size records, prescribed finite Xi equality, or the later selected-image arithmetic window. The degree-seven repair is one concrete part of that adapter, with its new finite costs exposed.

## 6. Sources, novelty, and certificate scope

- Milne, J. S. (2020). *Algebraic number theory* (Version 3.08, 19 July 2020). Proposition 6.2 and Theorem 6.4, printed pp.96–99, for prime cyclotomic ramification; Lemma 6.5, printed p.100, and Remark 6.6(c), printed p.101, for the integral compositum and its discriminant. Primary author PDF: https://www.jmilne.org/math/CourseNotes/ANT.pdf. The exact compositum statements were read in the source.
- Erez, B. (1991). A survey of recent work on the square root of the inverse different. *Astérisque, 198–200*, 133–152. Section 1, equations (1.1)–(1.2), printed p.134, for the tame different and trace-dual ideal; Theorem 2.9, printed p.139, records the general selfdual-normal-basis theorem in this tame abelian setting. Primary author paper: https://smf.emath.fr/system/files/filepdf/AST_1991__198-199-200__133_0.pdf. The general theorem is background only: (PH3)–(PH9) verify the particular basis directly.
- Accepted DP57; AM-DO-022, §§1–2; AM-R-004/006 and AM-LIFT-08: the original Jacobian, product lattice and exact theta normalization. AM-K018: the full-CM gauge comparison for ordinary powers. AM-K029: the enlarged field, induced type and literal unramified-character construction.

The general square-root-inverse-different and selfdual-normal-basis facts are classical, not claimed as new. The concrete contributions here are the displayed basis and its exact local certificate for conductor 29, the integral product-polarization transport, the exact coefficient (PH20), and the finite coordinate/cost comparison for this host. The certificate checks rational/cyclotomic algebra, matrix identities, all coefficients in (PH8), and the displayed norm/index formulas. No Lean build, unbounded analytic derivative computation, or full source-host instance is claimed.
