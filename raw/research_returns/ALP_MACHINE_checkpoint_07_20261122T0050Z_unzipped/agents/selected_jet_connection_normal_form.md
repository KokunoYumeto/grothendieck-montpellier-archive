# AM-K023 — the actual selected jet matrix modulo 11

Author: GPT-6 Astra Pro, ALP_MACHINE /root/kummer_extension, 21 November 2026 UTC. Inherited reasoning effort is not separately exposed.

AM-K022 removes the finite half-orbit saturation loss from a specified finite jet matrix. This note computes the reduction of that jet matrix by a finite polynomial normal form. It also gives actual rectangular selected rows of unexpectedly large degree whose exact 11-content is zero. These are local selected kernel statements; they do not compute a later automorphic class integral.

## 1. Every integral local section, not just the vanishing sigma section

Work over a finite unramified complete extension R of Z₁₁ containing the CM eigenvalues and the needed prime-to-11 torsion. Let k be its residue field. The ordinary Jacobian J, its principal trace-one line L=L₂∞, its q-normalized section, and the canonical source reduced gauge are those of AM-K018 and ALP-LIFT-08. Let F be the normalized nonvanishing even theta germ at D₁₃₅ from AM-K012. Its algebraic section is an integral unit at the origin, by ALP-LIFT-07, and F(0)=1. Its Hurwitz derivatives are integral.

Let κ be any positive integer prime to 11. Write 𝓜κ for the reduced germs of all integral formal local sections of L^κ at zero. The following equality of integral modules is exact:
\[
 \mathcal M_\kappa
   =\{\,h(u)F(u)^\kappa:
            h\text{ is an integral formal function on }\widehat J\,\}.
 \tag{NF1}
\]
Here h(u) means substitution of the characteristic-zero group logarithm into an ordinary integral formal function. It does not mean that F is an integral ordinary power series in logarithmic coordinates.

**Proof.** The difference between L and the line of F is the rigidified two-torsion line \(\mathcal P_T\). Its pullback by [2] has its canonical rigidified trivialization. The [2]-pullback of F is a nonvanishing integral section near zero, so its κ-th power is an integral local frame for [2]*L^κ under this trivialization. Hence any integral formal section S satisfies
\[
 F_S(2u)=r(u)F(2u)^\kappa
\]
for an arbitrary integral formal function r, and every such r occurs. The comparison has no exponential factor: this is the parallel rigidified trivialization of the pulled-back flat two-torsion line, exactly as in AM-K015. Since [2] is an integral formal automorphism at 11, replacing u by u/2 identifies these r with all integral formal functions h. This proves (NF1).

Every iterated invariant derivative of h has integral value at zero, because invariant vector fields preserve the integral formal coordinate ring. Thus h has integral Hurwitz coefficients. Products and inverses of Hurwitz series with integral coefficients and unit constant term are integral, as follows from the binomial product rule and the recursive coefficient equation for an inverse. Therefore every member of 𝓜κ is Hurwitz integral. This statement does not assert ordinary Taylor integrality. ∎

In particular the finite functional matrix B in AM-K022 can be taken integral at 11. Its presentation there as a matrix over Frac(R) was deliberately more general; changing its integral formal frame multiplies its jet columns by an integral invertible matrix and does not change its determinantal ideals.

## 2. Universal restricted-operator relations

For the ordinary coordinates u₁,u₂,u₃, AM-K017 proves both the algebraic restricted powers
\[
 D_1^{11}=0,\qquad D_2^{11}=-D_1,\qquad D_3^{11}=0
\tag{NF2}
\]
on the special fibre, and the full Hurwitz identities for F. The same identities on the completed local ring follow by continuity. For every f in 𝓜κ they imply
\[
 \boxed{
 \partial_1^{11}f=4\kappa u_3f,\qquad
 \partial_2^{11}f=-\partial_1f,\qquad
 \partial_3^{11}f=-\kappa u_2f
 }\quad(\bmod11).
\tag{NF3}
\]

**Proof.** Write H=log F. AM-K017 gives
\[
 \partial_1^{11}H=4u_3,\quad
 \partial_2^{11}H=-\partial_1H,\quad
 \partial_3^{11}H=-u_2.
\]
The Hurwitz augmentation ideal has zero eleventh powers. Since the first derivatives of H have zero constant term, the prime Bell identity applied to κH gives (NF3) for F^κ. For f=hF^κ, the eleventh derivative of a product is a derivation modulo 11. The derivative of h is prescribed by (NF2). Thus the first and third formulas multiply by h; the middle one becomes
\[
 (-D_1h)F^\kappa-h\,\partial_1F^\kappa
              =-\partial_1(hF^\kappa).
\]
This proves (NF3) on the full module. In particular no division by the nonunit initial quadratic of sigma is used. ∎

Apply this to J² with ordinary coordinates u,v. Choose E′=Q(ζ₂₈) coordinates
\[
 z_{i,+}=u_i+i v_i,\qquad z_{i,-}=u_i-i v_i.
\tag{NF4}
\]
This is an integral change of coordinates at 11. The sign is the eigenvalue of the extra CM endomorphism \(I(u,v)=(-v,u)\). Its tangent derivations are
\[
 \partial_{i,+}=(\partial_{u_i}-i\partial_{v_i})/2,\quad
 \partial_{i,-}=(\partial_{u_i}+i\partial_{v_i})/2.
\]
Since \(i^{11}=-i\), the exact identities on every integral local section of the product line are
\[
 \boxed{
 \partial_{1,\epsilon}^{11}f=2\kappa z_{3,\epsilon}f,\qquad
 \partial_{2,\epsilon}^{11}f=-\partial_{1,-\epsilon}f,\qquad
 \partial_{3,\epsilon}^{11}f=-\frac{\kappa}{2}z_{2,\epsilon}f.
 }\tag{NF5}
\]
For example, the first right side is
\((4\kappa/2)(u_3+i v_3)=2\kappa z_{3,+}\).
The middle formula exchanges signs because the coefficient i is conjugated by Frobenius. The same formulas hold entry by entry on the actual Hom variety A^{ab}=J^{2ab}. A simultaneous unit normalization of coordinates gives the conjugate formulas, with unchanged matrix ranks and content.

## 3. A finite normal form computes B modulo 11

For each matrix entry introduce six commuting derivative symbols \(Z_{i,\epsilon}\). Let \(\Lambda_f(P)=[P(\partial)f]_0\). Equation (NF5) gives the following exact evaluation rules over k:
\[
\begin{aligned}
 Z_{1,\epsilon}^{11}Q
     &\longmapsto 2\kappa\,\partial_{Z_{3,\epsilon}}Q,\\
 Z_{2,\epsilon}^{11}Q
     &\longmapsto -Z_{1,-\epsilon}Q,\\
 Z_{3,\epsilon}^{11}Q
     &\longmapsto -(\kappa/2)\partial_{Z_{2,\epsilon}}Q.
\end{aligned}\tag{NF6}
\]
For instance \(Q(\partial)(z_jf)|_0
=(\partial_{Z_j}Q)(\partial)f|_0\). This is the ordinary Leibniz rule, including its exact integer multiplicities.

Apply (NF6) linearly until every individual exponent is less than 11. Each nonzero replacement lowers total degree, by 12, 10, or 12 respectively. Thus the process terminates. Let Tκ(P) denote its output, in the vector space
\[
 \mathcal C=\operatorname{span}_k
   \{Z^\beta:0\leq\beta_j<11\text{ for every individual variable}\}.
\tag{NF7}
\]
The procedure is confluent, and the following matrix statement is exact.

### Proposition NF8

For any finite chosen family P₁,…,Pq of degrees at most D, the rank modulo 11 of its integral source jet matrix B equals the rank of the coefficient vectors
\[
                    T_\kappa(P_1),\ldots,T_\kappa(P_q).
\tag{NF8}
\]
The normalization factors \(M^{-\deg P_j}\) in AM-K022 are units and do not change this rank. For one polynomial P, its derivative image ideal has valuation zero if and only if \(T_\kappa(P)\ne0\). If its normal form is zero, the image is contained in 11R. The latter assertion alone gives no exact higher content.

**Proof.** All replacements preserve the evaluation on every member of 𝓜κ, by (NF6). The evaluation functionals associated with the cube monomials of degree at most D are linearly independent over k. Indeed choose integral algebraic formal parameters with the prescribed tangent basis. The degree-ordered matrix evaluating \(Z^\gamma\), \(0\leq\gamma_j<11\), on \(t^\beta F^\kappa\) has zero entry if \(|\gamma|<|\beta|\); in equal degree its entries are zero except at \(\gamma=\beta\), where they are \(\beta!\). These diagonal entries are units because every βj<11. Thus this square triangular submatrix is invertible.

Any two terminal reductions of P have identical functionals on all integral prefactors. Their difference lies in the cube and is therefore zero, proving confluence. The same independence proves (NF8). All the cube degrees encountered are at most the original degree, so the argument uses precisely the finite D-jet matrix. ∎

For several selected rows this computes exactly the number of Smith factors that are 11-adic units. It does not compute positive valuations of the remaining factors, and it does not iterate a congruence modulo 11 as a divisibility statement modulo higher powers.

Combining (NF8) with AM-K022, J30, gives the identical rank and unit-content criterion for the actual permitted half-orbit tuple matrix. Thus this calculation concerns actual allowed kernels, not an enlarged arbitrary Schwartz span.

## 4. Closed calculation for rectangular selected rows

Take source rank a and target rank b>a. For each of the six labels use the first a columns, and write \(X_{i,\epsilon}\) for that a-by-a matrix of derivative symbols. Define
\[
 P_{\mathbf n}=
 \prod_{\epsilon=\pm}\prod_{i=1}^3
                 \det(X_{i,\epsilon})^{n_{i,\epsilon}}.
\tag{NF9}
\]
It is the primitive highest bideterminant for the rectangular partitions
\((n_{i,\epsilon}^a)\), with determinant twists restored as in AM-DO-025.

Put
\[
 C_a(n)=n(n+1)\cdots(n+a-1).
\tag{NF10}
\]
The classical ordinary Cayley identity, in its integral polynomial specialization, is
\[
 \det(\partial_X)\det(X)^n=C_a(n)\det(X)^{n-1}
 \quad(n\ge1),
\tag{NF11}
\]
with zero on a constant. The primary reference is Caracciolo, Sokal, and Sportiello (2013), Theorem 2.1, equation (2.1); the directly consulted author preprint arXiv:1105.6270v2 gives this on printed p. 7. The short argument below checks the normalization used here; the identity is not a new result.

For completeness, over Q the left side is a relative invariant of the left GLₐ action with character det^{n−1}, so on the dense invertible matrices it is a constant times det^{n−1}. At X=I, the derivative indexed by a permutation π has value
\(\operatorname{sgn}(\pi)n^{c(\pi)}\): each disjoint cycle can be assigned independently to one of the n determinant factors in \(\det(I+T)^n\), and its sign is the cycle sign. The signs in det(∂) cancel these signs. The resulting sum is \(\sum_\pi n^{c(\pi)}\), equal to \(n(n+1)\cdots(n+a-1)\) by inserting the last symbol either as a new cycle or at one of the a−1 positions in the old cycles. This proves (NF11) over Q and hence as an integral polynomial identity.

Since \(\det(X)^{11}=\det(X^{[11]})\) modulo 11, rules (NF6) and (NF11) give the following exact recurrences for the evaluated polynomial:

| Condition | Scalar factor | Exponent change |
|---|---|---|
| \(n_{1,\epsilon}\ge11\) | \((2\kappa)^a C_a(n_{3,\epsilon})\) | \(n_{1,\epsilon}\mapsto n_{1,\epsilon}-11,\ n_{3,\epsilon}\mapsto n_{3,\epsilon}-1\) |
| \(n_{2,\epsilon}\ge11\) | \((-1)^a\) | \(n_{2,\epsilon}\mapsto n_{2,\epsilon}-11,\ n_{1,-\epsilon}\mapsto n_{1,-\epsilon}+1\) |
| \(n_{3,\epsilon}\ge11\) | \((-\kappa/2)^a C_a(n_{2,\epsilon})\) | \(n_{3,\epsilon}\mapsto n_{3,\epsilon}-11,\ n_{2,\epsilon}\mapsto n_{2,\epsilon}-1\) |

A factor Cₐ(0) means that the result is zero. These are finite reduction identities for functionals, not identities of the original symbol polynomials before quotienting by (NF6).

### Corollary NF12. Exact unit-content examples beyond the factorial threshold

Suppose all six exponents equal n=11q+r, where
\[
 1\le q\le r,\qquad r+q\le10,\qquad a+r\le11.
\tag{NF12}
\]
Then the exact 11-content of this selected row is zero. More explicitly its nonzero normal form is
\[
\begin{split}
 T_\kappa(P_{\mathbf n})={}&
 \kappa^{4aq}
 \left(\prod_{\ell=0}^{q-1} C_a(r-\ell)\right)^4\\
 &{}\cdot
 \prod_{\epsilon=\pm}
    \det(X_{1,\epsilon})^{r+q}
    \det(X_{2,\epsilon})^{r-q}
    \det(X_{3,\epsilon})^{r-q}.
\end{split}\tag{NF13}
\]

**Proof.** Reduce the two first-label exponents q times. Each third-label exponent becomes \(10q+r\). Reduce these q times; each middle-label exponent becomes \(10q+r\), and the third exponents become r−q. Reduce the middle exponents q times; they become r−q and each first-label exponent becomes r+q. The scalar factors in the table give (NF13); the signs and powers of 2 cancel. Every factor in every \(C_a(r-\ell)\) has an integer representative between 1 and 10, by (NF12), so the displayed scalar is nonzero modulo 11.

Each remaining determinant power has exponent at most 10. Therefore each individual symbol exponent is less than 11, and its polynomial lies in the cube. Its diagonal monomial has coefficient one, so the result is nonzero. Proposition NF8 proves zero content. ∎

Examples include n=12 for any even a≤10. For a=6, q=r=5 gives n=60 and total degree \(6an=2160\), yet the selected row has a unit value on some actual permitted tuple once M≥6482. The least permitted power is M=29³=24389, and its finite Schwartz vector still has norm one. The simple highest-symbol factorial bound in AM-K022 would only have given
\(6a\,v_{11}(60!)=180\), so the normal form improves that finite bound to the exact value zero.

These rectangles have an explicit source HC specialization at the first edge. For any already admissible rank record with k=a and d=t+1, put H=(d+2)/2 and, at all six embeddings,
\[
 b_j=j(d+2),\qquad e_j=H+j(d+2),\qquad
 u_i=a+n-\tfrac32-i,\qquad v_i=a+n-2-i.
\tag{NF14}
\]
Every interlacing difference is 1/2, the two e,b gaps equal H, and the last u is n−1/2>−b₀=0. The integer/half-integer conditions hold. Since \(w_{0,i}=u_i-\rho_a(i)\), equation DO25.5 gives exactly \(\nu_{0,i}=n\). Thus these are actual selected first-edge partitions, not freely relabelled Schur weights. For example the HC data a=6,d=14,n=60 give the selected edge 6→20. This checks the HC interface; any separate ambient arithmetic field or global size conditions retain their own status.

There is also a basic unbounded-rank family: if all rectangular exponents are at most 10, the highest polynomial already lies in the cube, for every a. Its row has zero content regardless of its total degree, and (NF14) realizes these first-edge HC weights whenever an admissible rank record is supplied. Neither family by itself controls every later stage of one fixed growing chain.

## 5. Scope and sources

The novel step is (NF1)–(NF8): the actual K017 relations extend to every integral local section, giving a rigorous finite normal form for B rather than a congruence for only one theta function. NF12–NF13 are the new selected-row application inside that finite quotient; NF11 is the classical Cayley identity with its integral normalization explicitly checked.

Caracciolo, S., Sokal, A. D., & Sportiello, A. (2013). Algebraic/combinatorial proofs of Cayley-type identities for derivatives of determinants and pfaffians. Advances in Applied Mathematics, 50(4), 474–594. Primary author preprint: https://arxiv.org/pdf/1105.6270, version 2 (31 December 2012), Theorem 2.1 and equation (2.1), printed p. 7. Only the ordinary determinant identity and its normalization are used here.

Carried inputs are AM-K012, AM-K015, AM-K017, AM-K018, ALP-LIFT-07–08, and AM-K022; their exact primary/source locators are in those reports. The actual E′ coordinates and selected Cauchy decomposition are AM-DO-022 and AM-DO-025, especially DO25.3 and DO25.5–9. No extra claim about reduced ordinary Taylor integrality, bounded differential-module saturation, or a later automorphic class matrix is used.

The literal HC check (NF14) uses Formalism/LocalRingCardinality/Params.lean, lines 50–69, and the actual selected-weight identity DO25.5. The finite independent arithmetic certificate is selected_jet_normal_form_certificate.py, with output in selected_jet_normal_form_certificate.json. It checks the integer determinant-two Cayley identity for n=1,…,40; 250 one-entry full normal forms; the complete six-matrix determinant-two expansions at n=12 and n=24 (4096 and 531441 nonzero input monomials modulo 11); a vanishing example at n=23; and the rank-six n=60 level arithmetic. It does not infer any infinite or higher-content conclusion from those finite checks.

The full finite jet matrix is integral and its rank modulo 11 is now computable from finite polynomial operations. Positive Smith valuations, control as every selected weight grows, and the effect of restricting the next class matrix to a previously produced theta image remain separate problems.
