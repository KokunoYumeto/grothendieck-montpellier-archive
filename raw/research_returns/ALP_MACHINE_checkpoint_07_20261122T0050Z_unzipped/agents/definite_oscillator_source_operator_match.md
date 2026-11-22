# AM-DO-026: actual mixed-kernel operators and the remaining source equations

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/definite_oscillator`;
inherited reasoning effort not separately exposed; 21 November 2026 UTC.

This finding combines the proved mixed-CM construction with the literal
recovered source interfaces. It proves an all-polynomial geometric kernel
identity, its compact covariance, a concrete finite stabilizer, and the
exact adjoint and class-mass formulas for the resulting actual operators.
It then identifies the additional equations needed to obtain the source
`PinColT`, `TieIo`, and terminal identities. These last equations are
not inferred from one nonzero theta value.

The carried inputs are AM-DO-017–020 and AM-DO-022–025, AM-R-004–006,
AM-K018, and the accepted DP57 host. Their conclusions are used at their
recorded checked status. In particular the finite direct-average phase
and pairing are already proved in AM-DO-024; they are not re-proved here.

## 1. A geometric kernel identity for every polynomial and finite translate

Use
\[
 E'=\mathbf Q(\zeta_{28}),\quad F'=E'^+,
 \quad A=J^2,\quad \xi'=\xi/2,
 \quad C=\theta_0c.
 \tag{DO26.1}
\]
For positive even ranks \(a,b\), let \(S=E'^a,T=E'^b\) have
the positive identity Hermitian forms. All Heisenberg signs, measures,
and splitting labels are those of AM-DO-022. Let
\(\Lambda=\operatorname{Hom}_{\mathcal O_{E'}}
(\mathcal O_{E'}^a,\mathcal O_{E'}^b)\), with its actual perfect
trace pairing, and let \(\phi_0\) be its finite trace-one vacuum.

For moved lattices \(N,N'\), define \(F_{N,N'}\) **geometrically**
by the two normalized finite Mumford averages from the seed
\((\sigma_q\boxtimes\sigma_q)^{\boxtimes ab}\). Thus each average
uses the actual finite quotient, its trace-one theta-group multiplier,
and the positive factor \(q^{-1/2}\). This definition precedes the
analytic theta comparison. For finite \(g,h\) moving the standard
lattices to \(N,N'\), write
\[
 A_{g,h}X=hXg^{-1},\qquad
 \epsilon_\chi(g,h)=\chi_T(x)^{-1}\chi_S(y),
 \quad x/\bar x=\det g,\quad y/\bar y=\det h.
 \tag{DO26.2}
\]
The independence from the determinant roots is the even-rank
restriction \(\chi_S|_{\mathbb A_{F'}^\times}
=\chi_T|_{\mathbb A_{F'}^\times}=1\).

For clarity, a finite adelic translation parameter does not itself
define a complex tangent vector. If \(y\) is such a parameter and
\(\Lambda'\) is the rational period lattice of \(F_{N,N'}\),
choose \(r\in\Lambda'\otimes\mathbf Q\) with
\(\delta=y-r\in\widehat\Lambda'\). Additive approximation supplies
such \(r\). Define the actual adelic translation on this theta line by
\[
 \mathcal U_y^{\Lambda'}F
   =\psi_f(-b(r,\delta)/2)\alpha_{\Lambda'}(\delta)\,U_rF.
 \tag{DO26.2a}
\]
The finite semicharacter is the continuous extension of the actual
trace-one lattice character. The Weyl law
\(W_rW_\delta=\psi_f(b(r,\delta)/2)W_y\), together with
\(W_\delta\phi_{N,N'}=\alpha_{\Lambda'}(\delta)\phi_{N,N'}\),
proves that (DO26.2a) is independent of the chosen rational
representative and that
\(\mathcal R W_y\phi_{N,N'}=C^{2ab}
\mathcal U_y^{\Lambda'}F_{N,N'}\). Equivalently, independence
follows from the reduced-translation group law and the rational
product formula. All displayed central factors are retained.

Choose a finite collection of rational Heisenberg parameters \(x\)
and coefficients \(d_x\), and set
\[
 \phi_d=\sum_x d_xW_x\phi_0,\qquad
 F_{d;g,h}=\sum_x d_x\mathcal U_{A_{g,h}x}^{\Lambda'}F_{N,N'}.
 \tag{DO26.3}
\]
Here \(W_x\) and \(\mathcal U_y^{\Lambda'}\) are the actual
Schrödinger and reduced Mumford translations, with their central
phase retained. In particular no finite adele has been silently
treated as a complex translation vector. For a
polynomial \(P\) in the actual invariant tangent coordinates, let
\(r_P\) be its corresponding Chern creation operator. Then
\[
 \boxed{\vartheta_{r_P\phi_d}(g,h)
   =C^{2ab}\epsilon_\chi(g,h)
                  \,[P(\partial)F_{d;g,h}]_{0}.}
 \tag{DO26.4}
\]
This is one common period for the entire moved family and all
polynomial degrees, not a separate scalar selected at each value.

**Proof.** Exact Heisenberg covariance gives
\[
 \omega(g,h)\phi_d
 =\epsilon_\chi(g,h)\sum_xd_xW_{A_{g,h}x}\phi_{N,N'}.
\]
AM-DO-022 gives the vacuum identity with period \(C^{2ab}\),
and AM-DO-018 identifies the actual translations under the reading
map. Therefore
\(\mathcal R(\omega(g,h)\phi_d)
=C^{2ab}\epsilon_\chi(g,h)F_{d;g,h}\) as entire functions.
The finite action commutes with every archimedean creation operator,
because they act on different factors of the restricted tensor
product. The explicit identity
\(\mathcal Rr_P=P(\partial)\mathcal R\), checked in
ALP-LIFT-09, then gives (DO26.4) by evaluation at zero. All sums in
(DO26.3) are finite. The theta sum and its fixed-order derivatives
converge normally by the Gaussian estimate already proved for the
reading map. Hence no interchange of divergent expressions is used.
\(\square\)

AM-K018 identifies the starting Chern-reduced formal gauge with the
actual source primitive gauge for the underlying ordinary product
of copies of \(J\), including the integral block at 11. The extra
\(E'\)-action does not replace that product by a product with
conjugated \(E\)-actions. Its complete generic gauge comparison
also transports through the actual CM isogenies and torsion
translations in these finite averages: these preserve the same
holomorphic character set, so the same no-opposite-characters
uniqueness argument applies. This does not supply an integral
11-adic frame after an arbitrary isogeny of 11-power degree. The
accepted original integral frame transports directly only when
that isogeny is prime to 11, or when an additional integral
comparison is proved. No reduced theta frame is asserted integral.
The product trace remains \(\xi/2\), and the eigenbasis change has
dyadic determinant valuation 3 per \(A\), as in AM-DO-022.

For specified finite class representatives \(g_i,h_j\), define the
geometric jet functionals
\[
 \mathcal A_{ji}(P)=\epsilon_\chi(g_i,h_j)
                    [P(\partial)F_{d;g_i,h_j}]_0.
 \tag{DO26.5}
\]
They are defined from actual line-bundle translations and averages,
not by dividing an analytic theta value by a desired constant. For
algebraic finite characters and coefficients they have algebraic
values, by AM-K018 and algebraicity of the fixed torsion translations.
For any chosen source level volume \(v_S\), (DO26.4) gives the
concrete all-polynomial class-kernel equation
\[
 v_S\vartheta_{r_P\phi_d}(g_i,h_j)
                   =v_SC^{2ab}\mathcal A_{ji}(P).
 \tag{DO26.6}
\]
This is the exact mixed-family analogue of `ClsK.Core`. Identification
with its independently specified `abelian₂`, frame scale, and chart
characters is an additional comparison, detailed in section 5.

## 2. The actual compact covariance and an explicit finite stabilizer

For the selected common-character edge of AM-DO-025, put
\(a=N_j,b=N_{j+1}\) and
\(\chi_S=\chi_T=\mu_{j+1}\), with infinity exponent \(-e_j\).
The corrected source splitting formula gives
\[
 \omega_\infty(g,h)r_P\phi_\infty
 =\prod_\tau\det(g_\tau)^{e_{j,\tau}-b/2}
                    \det(h_\tau)^{-e_{j,\tau}+a/2}
      r_{\operatorname{mvZ}(g^{-1},h)P}\phi_\infty.
 \tag{DO26.7}
\]
The polynomial action is expressed in the source's creation-label
convention `mvZ`; it is the tensor action on \(T\otimes S^*\).
Equation (DO26.7) is AM-DO-023's honest-splitting formula applied to
all creation polynomials, not merely to a lowest-weight line.

The exact recovered definitions give
\[
 s_S=e_j-b/2=\texttt{sSharpC},\qquad
 s_D=e_j-a/2=\texttt{sDivC}.
 \tag{DO26.8}
\]
Indeed `Params.sExp'` and `sExp` have these values at \(j+1\);
their integer floors in `Columns/Record.lean`, lines 1083–1087,
are unchanged because \(e_j\) is integral and both ranks are even.
Thus (DO26.7) is exactly the determinant and polynomial covariance
required by `ClsK.Real`, after matching the actual tangent frames.
AM-DO-025 proves that the source partition `nuW` selects the
contragredient of `lamTrue` on the source and the next `lamTrue`
on the target. The real covariance and the local type match are
therefore established for this constructed compact family.

Here is also a definite finite-level assertion. Suppose every
parameter in (DO26.3) belongs to \(M^{-1}\Lambda\), where
\(M\) is a positive integer. Let \(K_S,K_T\) be the standard
integral unitary compacts, refined by the principal congruence
condition \(1\pmod{2M^2}\). For trivial characters, both groups
fix \(\phi_d\) exactly:
\[
                     \omega(K_S,K_T)\phi_d=\phi_d.
 \tag{DO26.9}
\]
For nontrivial even-rank characters the same assertion holds after
intersecting with the kernels of the two determinant characters
\(\nu_{\chi_T}^{-1}\circ\det\) and
\(\nu_{\chi_S}\circ\det\). These are open subgroups of the
compacts, so the refinement is finite.

**Proof.** AM-DO-022 proves that the trivial-character standard
compacts fix \(\phi_0\). The induced Hom action is congruent to
the identity modulo \(2M^2\), including after inversion on the
source. For \(x\in M^{-1}\Lambda\), write
\(\delta=A_{g,h}x-x\in2M\widehat\Lambda\). Perfection and
integrality of the actual trace pairing give
\[
 \psi_f(b(x,\delta)/2)=1,\qquad
 \alpha_{\rm tr}(\delta)
      =\psi_f(b(\delta,w_0\delta)/2)=1.
\]
For the first equality write \(x=\lambda/M,\delta=2M\eta\);
the half-pairing is \(b(\lambda,\eta)\), which is integral.
For the second it is \(2M^2b(\eta,w_0\eta)\), also integral.
The exact Weyl group law therefore yields
\(W_{x+\delta}\phi_0=W_x\phi_0\). Covariance fixes each
summand in (DO26.3), proving (DO26.9). For the specified nontrivial
characters the only remaining compact scalar is the displayed
determinant factor from AM-DO-022; killing it gives the assertion.
\(\square\)

This bound is deliberately uniform for the named finite span. It is
not asserted to be the least level; ALP-LIFT-10 obtains a smaller one
for its special isotropic half-orbit. Nor does (DO26.9) prove that an
independently pinned source level already lies in this stabilizer.
The index of the needed refinement remains an arithmetic cost.

## 3. Exact adjoint and conjugation identities for the compact kernel

Let \(X=[U(S)]\) and \(Y=[U(T)]\), with specified compatible
quotient Haar measures. Both are compact because the groups are
definite. Let \(K(x,y)\) be one of the actual polynomial theta
kernels from section 1. Define the source-style **bilinear** operators
\[
 (T_Kf)(y)=\int_XK(x,y)f(x)\,dx,
 \qquad
 (S_Kg)(x)=\int_YK(x,y)g(y)\,dy.
 \tag{DO26.10}
\]
Use the inner product conjugate-linear in its first argument, and
write \(C_Xf=\bar f\), \(C_Yg=\bar g\). Then the exact identities
are
\[
 \boxed{T_K^*=C_XS_KC_Y,\qquad
        C_YT_KC_X=T_{\bar K}.}
 \tag{DO26.11}
\]
The second equation keeps the same source-to-target orientation;
in the first, \(S_K\) reverses it. In particular `liftS` with the
same kernel is not the Hermitian adjoint of `liftT` until these
pointwise conjugations are inserted.

**Proof.** At fixed level the quotient is a finite union of compact
real-group pieces. The finite support is fixed on each piece, and the
positive Gaussian quadratic form has a uniform positive lower bound
as the real group varies over its compact set. Its polynomial theta
series therefore converges normally and gives a continuous bounded
kernel. It is square integrable, and Fubini applies to the displayed
operators, first for continuous functions and then to all \(L^2\)
functions by the bounded integral-operator estimate. Directly,
\[
 \begin{aligned}
 \langle T_Kf,g\rangle_Y
  &=\int_X\bar f(x)
       \left(\int_Y\overline{K(x,y)}g(y)\,dy\right)dx\\
  &=\langle f,C_XS_KC_Yg\rangle_X.
 \end{aligned}
\]
Conjugating (DO26.10) term by term gives the second equality.
This proves (DO26.11). \(\square\)

The corresponding bilinear pairing \(B_X(f_1,f_2)=\int_Xf_1f_2\)
satisfies
\[
                  B_Y(T_Kf,g)=B_X(f,S_Kg).
 \tag{DO26.12}
\]
Consequently
\[
             \langle f,T_K^*T_Kf\rangle_X=\|T_Kf\|_Y^2.
 \tag{DO26.13}
\]
This is strictly positive for an actual nonzero first image. It
constructs an actual detecting Gram operator; it does not identify
that operator with a separately prescribed positive-rank next theta
edge. Complex conjugating the theta series also gives a concrete
kernel in the conjugate Weil representation, with the additive
character and splitting scalars conjugated. This supplies the
conjugations in (DO26.11) without guessing a source-target swapping
character formula.

The scalar bookkeeping is exact. If \(K=c_0\mathcal K\), then
\[
 T_K=c_0T_{\mathcal K},\qquad
 T_K^*=\bar c_0T_{\mathcal K}^*,\qquad
 T_K^*T_K=|c_0|^2T_{\mathcal K}^*T_{\mathcal K}.
 \tag{DO26.14}
\]
Here \(c_0=C^{2ab}\), with any explicitly chosen creation-frame
scaling retained. Neither the complex-torus probability measure of
AM-DO-024 nor a Gaussian unit normalization silently substitutes for
the automorphic quotient measure in these formulas.

For a compact subgroup embedding \(\iota:H\to G\), the actual
restriction period
\(B_{\rm top}(F,G)=\int_{[H]}\overline{F(\iota h)}G(h)\,dh\)
obeys
\[
 B_{\rm top}(C F,G)=\int_{[H]}F(\iota h)G(h)\,dh.
 \tag{DO26.15}
\]
Thus the source's `conjAF` in `TieBm` has a concrete role: it
converts its conjugate-linear first argument into the bilinear
terminal pairing. Equation (DO26.15) does not specify the arithmetic
terminal row or its scalar.

## 4. Actual finite class masses and the operator matrix

Fix an open compact \(K_f\subset G(\mathbb A_f)\), and write
\(g_i\) for the finitely many double-class representatives. Put
\[
 \Gamma_i=G(F)\cap g_iK_fg_i^{-1},\qquad
       v_K=\operatorname{vol}(K_f),\qquad w_i=v_K/|\Gamma_i|.
 \tag{DO26.16}
\]
The real compact group has Haar volume one. The rational intersection
is finite: it is discrete in the compact product of the real group
and the finite compact, hence finite. Quotient integration gives
\[
 \int_{[G]}F(g)\,dg
       =v_K\sum_i\frac1{|\Gamma_i|}
                    \int_{G_\infty}F(g_ik)\,dk.
 \tag{DO26.17}
\]
Indeed the piece is the diagonal quotient of
\(G_\infty\times K_f\) by the finite group \(\Gamma_i\).
Pushing forward Haar measure divides by its order; then integrating
the right \(K_f\)-invariant function contributes \(v_K\).
This proves (DO26.17) with the chosen compatible quotient measure.

If \(\rho\) is an irreducible unitary real coefficient type of
dimension \(d_\rho\), and a unit functional \(\ell\) is used
to realize its vectors as \(k\mapsto\ell(\rho(k)v)\), then
\[
 \int_{G_\infty}|\ell(\rho(k)v)|^2\,dk
                          =\frac{\|v\|^2}{d_\rho}.
 \tag{DO26.18}
\]
For completeness, the averaged positive rank-one operator
\(\int\rho(k)^*\ell^*\ell\rho(k)\,dk\) commutes with
\(\rho\), hence is scalar by irreducibility; its trace is one,
so its scalar is \(1/d_\rho\). This proves (DO26.18).
Multiplication of this realization by \(\sqrt{d_\rho}\) makes
it isometric. Without that normalization, the factor in (DO26.18)
must remain in every class metric.

Choose orthonormal real compact coefficient bases in each class
piece, using that normalization and its actual invariant subspaces.
Then the metric on the class coefficient vector is
\(G_X=\operatorname{diag}(w_i I_i)\). Do the same on the
target, with metric \(G_Y\). Expand the relevant finite-type
kernel as
\[
 K((i,k),(j,l))
       =\sum_{r,s}A_{ji,sr}\overline{u_{i,r}(k)}v_{j,s}(l).
 \tag{DO26.19}
\]
Such an expansion is finite for a fixed polynomial input: its
compact-group orbit is finite dimensional. Orthogonality and
(DO26.17) now give the **actual operator matrices**
\[
 \boxed{T=A G_X,\qquad
        T^{\dagger}=G_X^{-1}\bar T^{\,t}G_Y
                         =\bar A^{\,t}G_Y.}
 \tag{DO26.20}
\]
The formulas hold blockwise on the invariant coefficient subspaces;
empty blocks are omitted. They follow simply by integrating
\(\bar u_{i,r}u_{i,r'}\) and then evaluating the defining
Hermitian-adjoint equality. Thus the stabilizer denominators, level
volume, real Schur factor, and conjugation are all explicit.

This construction proves a class-mass formula for the actual
automorphic operator. An independently given integral polynomial or
Weyl-module basis need not be this orthonormal basis. Changing to it
requires its actual Gram matrix and lattice determinant; those
quantities are not removed by (DO26.20). In particular an arbitrary
choice of the source's `rowAF` cannot be made isometric by assertion.

## 5. Exact comparison with the recovered arithmetic pins

The definitions in `LevChiEqOne.lean` give the following nonoptional
equations. The symbols on their right sides are independently
specified source data.

First, `VacT` requires (DO26.4) at degree zero with the source
`xiS`, `I.J.V.thMoved`, and determinant-root factor
\(\mu(x)^{-1}\mu(y)\), uniformly in every finite move. AM-DO-022
proves that mathematical statement for the new mixed geometric
family and the standard Weil representation. `PinX.mv` additionally
quantifies over every `om` satisfying `IsWeilDatumO`; identifying
all such axiomatic data with this fixed standard realization requires
its uniqueness statement. The old elliptic `VacIn` is not the new
seed merely because both are vacua.

Second, `PinColT.cst` is, literally,
\[
 c_{K,j}=v_{j,\alpha}\,w_{j,\alpha\gamma}\,c_{0,j}
       \mu_{j+1}(x_{j,\alpha})
       \mu_{j+1}(x_{j+1,\gamma})^{-1}
                 \quad\text{for every }\alpha,\gamma.
 \tag{DO26.21}
\]
The volume is that of the source chart level, not a theta-line
norm. If every factor is nonzero, independence of the chart is
equivalent to all pairwise ratio equations
\[
 \frac{v_{j,\alpha}w_{j,\alpha\gamma}}
      {v_{j,\alpha'}w_{j,\alpha'\gamma'}}
 \frac{\mu(x_{j,\alpha})}{\mu(x_{j,\alpha'})}
 \frac{\mu(x_{j+1,\gamma'})}{\mu(x_{j+1,\gamma})}=1.
 \tag{DO26.22}
\]
This equivalence follows by dividing two instances of (DO26.21);
conversely fix one chart to define \(c_{K,j}\) and use all
ratios. It is a finite concrete compatibility test. The geometric
period \(c_{0,j}=C^{2N_jN_{j+1}}\) is now known; the source
chart factors and their arithmetic meanings cannot be replaced by
freely chosen scalars just to force (DO26.22).

Third, `ClsK.Core` requires for **every** polynomial
\[
 v_{j,\alpha}\Theta_{j,\alpha\gamma}(h_a,h_{a'};P)
  =c_{K,j}\,\operatorname{abelian}_2
       \bigl(\operatorname{mvZ}(1,\operatorname{sc}_j I)
                            \operatorname{castP}(P)\bigr).
 \tag{DO26.23}
\]
Our equation (DO26.6) supplies its analytic-to-geometric kernel
comparison. The actual source functional is
\(\rho_i(c)\rho_i'(c')\operatorname{jetL}
  (I.\mathrm{th}(\operatorname{rep}c,\operatorname{rep}c'))\),
as defined at lines 73–77 of `LevChiEqOne.lean`. Its frame scale,
finite arithmetic datum, and these two character scalars must be
matched to (DO26.5). The finite-level statement in section 2 and the
real statement (DO26.7) supply corresponding `Lev` and `Real`
identities for the newly constructed datum. They do not identify
an independently fixed datum without this comparison.

Fourth, `ClsK.Kval` says that the prescribed arithmetic row map
\(K_j\), evaluated in its specified frames, is exactly the
stabilizer-weighted geometric kernel sum, including the target
factor \(\det(y')^{-s_D}\). Equation (DO26.20) proves the
class integral formula for the actual operator. To deduce that
particular `Kval`, one must exhibit the same coefficient-lattice
realization and its compact projection normalization. Local type
occurrence from AM-DO-025 does not choose that realization.

The abstract `ThetaX` ties are equally precise. With
\(\operatorname{petY}_j=m_{Y,j}\operatorname{pet}_j\) and
\(\operatorname{dnY}_j=m_{Y,j+1}\Theta_j\), they require
\[
 \begin{aligned}
 m_{Y,j}&=\prod_v\operatorname{parIdx}(q_v,r,jt),\\
 \operatorname{petY}_j(\operatorname{rowAF}_j x,
                      \operatorname{rowAF}_j y)&=\langle x,y\rangle,\\
 \operatorname{petY}_j(\operatorname{dnY}_j
           \operatorname{rowAF}_{j+1}y,\operatorname{rowAF}_j x)
                &=\langle\operatorname{io}_j y,x\rangle.
 \end{aligned}
 \tag{DO26.24}
\]
Equations (DO26.11) and (DO26.20) give the exact analytic adjoint
and its actual matrix. They establish (DO26.24) only when the
preassigned `rowAF`, `io`, metrics, and parahoric factors are
identified with those matrices. Choosing a new abstract map equal
to an adjoint would prove a different statement.

## 6. Terminal mass and the literal two-step MainX equation

The source terminal equation `ClsT.tail` is
\[
 v_T\sum_{\beta,a}\frac{1}{|\Gamma_{T,a}|}
    \ell_{\beta,a,G}\!\left(
      \operatorname{low}\bigl(\operatorname{rd}_{m,\beta}
                    \psi\circ\iota(h_a,1)\bigr)\right)
                 =c_P\,\operatorname{tail}(\psi,G).
 \tag{DO26.25}
\]
It holds for every allowed arithmetic row \(\psi\) and every
terminal coefficient vector \(G\), with the same \(c_P\).
The actual finite theta-line overlap
\(q_0^{-1/2}\), and the holomorphic overlap with period and
metric factors in AM-DO-024, are completely determined. They are
not (DO26.25): the latter contains a different quotient measure,
an actual restriction embedding, coefficient projections, and a
prescribed arithmetic terminal functional.

For fixed finite-dimensional row and terminal spaces, (DO26.25)
is a finite matrix test. Choose their actual bases, let \(B\)
be the matrix of the left side computed with its masses, and let
\(T\) be the matrix of `tail`. The requirement is
\[
                              B=c_PT.
 \tag{DO26.26}
\]
If \(T\ne0\), choose one nonzero entry \(T_{rs}\). Then
there is such a scalar if and only if
\(B_{ij}T_{rs}=B_{rs}T_{ij}\) for all entries. This condition
also forces \(B_{ij}=0\) whenever \(T_{ij}=0\). The proof is
division by the chosen entry, followed by bilinearity on the two
bases. Thus one nonzero period fixes a candidate scalar but does
not verify its uniformity. The source also requires \(c_P\ne0\)
where its later nonvanishing arguments use it.

For the literal two-step case \(m=2\), `MainX` uses the implication
\[
 \begin{split}
 &\sum_i\alpha_i
   c_{V,0}^{(i)}c_{K,0}^{(i)}c_{K,1}^{(i)}c_P^{(i)}
   \operatorname{tail}^{(i)}
      (K_1^{(i)}K_0^{(i)}S_0^{(i)}\psi_i,F_i)=0\\
 &\quad\Longrightarrow\quad
 \sum_i\alpha_i c_{I,0}^{(i)}c_{I,1}^{(i)}
   \operatorname{per}_0^{(i)}
      (\psi_i,\operatorname{io}_0^{(i)}
                       \operatorname{ioT}_0^{(i)}F_i;y,v)=0
                         \quad\text{for all }y,v.
 \end{split}
 \tag{DO26.27}
\]
The quantifier over all finite linear relations and common frames
is essential. In the general even chain the factors are exactly
\[
 c_{\rm Top}=\prod_i(c_{V,2i}c_{K,2i}c_{K,2i+1})c_P,
               \qquad c_{\rm Bot}=\prod_jc_{I,j}.
 \tag{DO26.28}
\]
These are `Tup.cTop`, `cBot`, and `MainX` in `ValLastX.lean`.
The new compact kernels prove substantive components that enter
this system. They do not replace its Bessel/Jacobi two-step
unfolding, its fixed row maps, or (DO26.25).

## 7. The six actual analytic predicates and exact source scope

The source's `AdmS` is a conjunction of the following six predicates,
not a name for the elementary compact kernel identities alone.

| Actual predicate | What the new construction proves | Obligation still present in the literal source |
|---|---|---|
| `RallisSiegelWeilFormula` | Actual compact kernels, exact prescribed local coefficient types, and separate concrete nonzero first lifts | For every `Hyp3` parameter, a nonzero irreducible global chain in the specified types, with every upper vector a finite sum of prescribed theta lifts |
| `LiftParameterConditions` | Actual compact restriction pairings and their conjugation convention | A nonzero terminal period against the specified noncompact discrete-series family for every allowed top irreducible representation |
| `ThetaUnfoldingFreeData` | Exact compact Fubini/adjoint identities (DO26.11)–(DO26.12) | The source's Bessel/Jacobi period transfer with factorizable, real-finite downward Schwartz data and its universal nonzero-period implication |
| `ThetaStablePeriodVanishing` | No cuspidality problem for the constructed anisotropic compact groups themselves | The stated lower-Witt-tower vanishing implication for the noncompact `Y` chain |
| `RealThetaLiftDiscreteSeries` | Exact compact real formula and the selected compact Schur correspondence | The specified noncompact discrete-series preservation and lower-signature vanishing statements |
| `RealConstantNonvanishing` | Translation preserves the actual compact representation and its fixed local type | Stability of the source's particular noncompact `IsDv` condition under all displayed finite and real actions |

Consequently the correct progression is: an actual mixed theta seed;
its exact all-finite moved family and direct pairing; its all-degree
geometric class kernel; the selected real covariance; then the
independently pinned arithmetic row and terminal equations. The first
four now have explicit formulas. The remaining source comparisons
are concrete algebraic and automorphic obligations, not evidence
that no other map or construction can exist.

### Exact recovered-source locators

All paths below are relative to `work/research/alpoge_source`.

| Interface | Source locator |
|---|---|
| Bilinear `liftS`/`liftT` | `Development/AbelianVarietyTheory/Definitions/TwistedInnerProducts/WittSmallGroupEmbeddingMemPointwiseStabilizerIso.lean`, lines 157–167 |
| Finite-combination kernel and lift | `Development/AbelianVarietyTheory/Definitions/LatticeFrames/JointSmooth.lean`, `KerDat.pt`, `lift`, lines 74–82 |
| Actual vacuum, character roots, chart constant | `Development/AbelianVarietyTheory/Definitions/LatticeFrames/LevChiEqOne.lean`, `abelian₂`, lines 73–77; `VacT`, 87–93; `PinX`, 95–101; `PinColT`, 103–119 |
| Real, level, kernel and arithmetic row identities | `Development/AbelianVarietyTheory/Definitions/LatticeFrames/OnFramesRdApply.lean`, `ClsK.Real`, 93–102; `Lev`, 103–107; `Core`, 108–113; `Kval`, 115–121 |
| Terminal class mass | Same file, `ClsT.Is.top` and `tail`, lines 143–150 |
| Exact determinant exponents | `Formalism/LocalRingCardinality/Params.lean`, `sExp`, `sExp'`, lines 71–73; `Formalism/LocalToGlobal/Columns/Record.lean`, `sSharpC`, `sDivC`, lines 1083–1087 |
| Conjugation, periods and row ties | `Formalism/LocalRingCardinality/DataTheta.lean`, `conjAF`, 645–649; `Bper` and `Btop`, 657–670; `petY`, `dnY`, `TieMY`, `TieRowIsom`, `TieIo`, `TieBm`, 730–752 |
| Two-step and terminal relation laws | `Development/AbelianVarietyTheory/Definitions/LatticeFrames/ValLastX.lean`, `ValX`, `ValLastX`, `KerX`, `PerX`, `LawsX`, `LastX`, `MainX`; `Tup.cTop` and `cBot` |
| Six analytic assumptions | `Formalism/SharpRestriction/CuspSpanNormBounds/CayleySignature.lean`, lines 154–202 |
| Existing vacuum-to-polynomial comparison | `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaKernelSplitPlacesEqJetClassicalTheta.lean`, complete theorem `thetaKernel_eq_jet_thC` |

No Lean build or formal instantiation of a source record is claimed.
The cited interfaces and theorem bodies were directly read. The new
operator proofs above state exactly which representation, period,
measure, and coefficient normalization they use.
