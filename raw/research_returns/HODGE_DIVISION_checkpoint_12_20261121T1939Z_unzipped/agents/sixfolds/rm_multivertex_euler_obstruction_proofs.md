# SF-E815: a concrete balanced character and the finite-action obstruction for its line-class cone model

Author: GPT-6 Astra Pro; inherited effort not exposed; HODGE_DIVISION /root/sixfolds. Date: 2026-11-21. The explicit rank-32 character was supplied by /root; its complete calculation and the new categorical obstruction are given below.

**Status:** Whole-proof mathematical PASS reviews of the complete base argument were received from /root and /root/imprimitive on 2026-11-21 (GPT-6 Astra Pro; inherited effort not exposed). Both independently reran the exact seven-character certificate and obtained PASS. The explicit equivariant Grothendieck-group identity requested by root is incorporated. Both reviewers also approved the projectively flat factor extension in §6; its full written adaptation is included below. The separately written SF-E815R refinement was whole-proof checked by root and replaces the former numerical bound31 by63; the extended exact certificate was freshly rerun by both author and root. The categorical assertions are proved here, not inferred from the computation. The result concerns the stated cohomology models and does not exclude all perfect complexes or all nonsimple equivariant objects.

## 1. The explicit actual polystable bundle

Let \(X=E_{\mathrm i}^{\,4}\), with its product principal polarization \(\theta\). Identify integral symmetric real matrices with the corresponding algebraic divisor classes on this CM product. Put

\[
 U=\operatorname{diag}\left(
     \begin{pmatrix}1&1\\1&-1\end{pmatrix},
     \begin{pmatrix}1&1\\1&-1\end{pmatrix}\right),
 \qquad S=\operatorname{diag}(1,1,-1,-1).
 \tag{E815.1}
\]

Then \(U^2=2I\), \(US=SU\), and \(U\) is self-adjoint for \(\theta\). It defines genuine real multiplication by \(\mathbf Q(\sqrt2)\), of type \((2,2)\). Write \(\theta=\theta_++\theta_-\) along its two complex eigenspaces, and let

\[
 X_0=\theta_S=x+y,\qquad Y=\theta_{US}=\sqrt2x-\sqrt2y,
 \qquad Z_+=X_0+Y,\quad Z_-=X_0-Y.
 \tag{E815.2}
\]

Here \(x,y\) are the restrictions of \(X_0\) to the two eigenspaces. The notation \(X_0\) distinguishes this divisor from the abelian variety \(X\). On each complex eigenspace the matrix \(S\) has eigenvalues \(1,-1\). Consequently

\[
 x^2=-\theta_+^2,\qquad y^2=-\theta_-^2,
 \qquad x^3=y^3=0,
 \qquad \int_Xx^2y^2=4.
 \tag{E815.3}
\]

Both \(x\) and \(y\) are primitive on their respective planes. All rational combinations of \(X_0,Y\) therefore have zero \(\theta\)-slope. Choose line bundles \(L_\beta\) with the indicated integral divisor classes and form the actual bundle

\[
 \begin{split}
 E_{\mathrm{poly}}={}&\mathcal O_X^{\oplus24}
 \oplus L_{X_0}^{\oplus2}\oplus L_{-X_0}^{\oplus2}\\
 &\oplus L_{Z_+}\oplus L_{-Z_+}
 \oplus L_{Z_-}\oplus L_{-Z_-}.
 \end{split}
 \tag{E815.4}
\]

Every line summand is stable of slope zero, so this is a polystable bundle. Its rank is 32; symmetry of the signs makes its odd Chern-character components zero. Its degree-four cohomology component is

\[
 \operatorname{ch}_2(E_{\mathrm{poly}})
 =2X_0^2+Z_+^2+Z_-^2
 =4X_0^2+2Y^2
 =-8(\theta_+^2+\theta_-^2).
 \tag{E815.5}
\]

For the top component, if \(\beta=ax+by\), then \(\beta^4=6a^2b^2x^2y^2\). The two coefficients of \(X_0\) have product one, whereas the two coefficients of either \(Z_+\) or \(Z_-\) have product \(-1\). Hence

\[
 \begin{split}
 \operatorname{ch}_4(E_{\mathrm{poly}})
 &=\frac{2X_0^4+Z_+^4+Z_-^4}{12}\\
 &=2x^2y^2=2\theta_+^2\theta_-^2.
 \end{split}
 \tag{E815.6}
\]

Thus the **entire** Chern character is

\[
 C=\operatorname{ch}(E_{\mathrm{poly}})
   =32\left(1-\frac14\theta_+^2\right)
       \left(1-\frac14\theta_-^2\right).
 \tag{E815.7}
\]

This is the balanced character with parameter \(q=1/2\). It is an actual algebraic realization, not merely a formal class in rational cohomology. SF-E812 already excludes weak equivariant semiregularity of this polystable bundle. The question addressed next is whether genuinely derived gluing within its line-class model can repair that defect.

## 2. Exact independence of the seven exponential characters

Let

\[
 \mathcal B=\{0,X_0,-X_0,Z_+,-Z_+,Z_-,-Z_-\}.
\]

The seven classes \(e^\beta\), \(\beta\in\mathcal B\), are linearly independent over \(\mathbf Q\). Here is an exact determinant certificate. Work over \(\mathbf Q(u)\), \(u^2=2\), in the nine-dimensional exterior subalgebra

\[
 \mathbf Q(u)[x,y]/(x^3,y^3).
\]

The nine monomials are independent: their \((\deg_x,\deg_y)\) components are distinct and each nonzero factor \(x^a,y^b\), for \(0\le a,b\le2\), lies on its own complex two-plane. For \(\beta=aX_0+bY\), the coefficient of \(x^py^q\) in its exponential is

\[
 \frac{(a+bu)^p(a-bu)^q}{p!q!}.
 \tag{E815.8}
\]

Take the seven columns corresponding, in order, to

\[
 (a,b)=(0,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)
\]

and the seven rows

\[
 (p,q)=(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0).
\]

The determinant of the matrix (E815.8) is exactly \(-512\). This gives independence even over \(\mathbf Q(u)\), hence over \(\mathbf Q\). The entries, determinant, full character (E815.7), and Euler numbers below are supplied in the exact script and JSON certificate.

## 3. The permitted cone model and its actual equivariant class blocks

Fix an integer \(k\ge1\). Let \(E\) be a perfect complex with

\[
 \operatorname{ch}(E)=kC.
 \tag{E815.9}
\]

Assume that every cohomology sheaf \(\mathcal H^j(E)\) is a vector bundle admitting a finite filtration by line bundles of the form

\[
 L_\beta\otimes P,\qquad\beta\in\mathcal B,
 \quad P\in\operatorname{Pic}^0(X).
 \tag{E815.10}
\]

This permits arbitrary cohomological degrees, arbitrary extra cancelling terms, arbitrary multiplicities, and arbitrary extensions within each class. In particular the aggregate virtual multiplicities need not be read from the number of vertices of a chosen complex. They will be determined from its full character.

Let \(G\subset X\times\widehat X\) be any effective finite subgroup with a specified coherent translation/tensor action, and suppose \(E\) has an equivariant lift. Individual line factors in (E815.10) are **not** assumed to admit linearizations. Nontrivial projective multiplicity representations are allowed.

For distinct \(\beta,\gamma\in\mathcal B\), their difference is a nonzero rational combination of \(X_0,Y\), block diagonal and primitive on both genuine real-multiplication planes. The rationality proof in SF-E813 shows that both blocks are nonzero and the complete Hermitian form has signature \((2,2)\). Therefore

\[
 \operatorname{Hom}(L_\beta\otimes P,L_\gamma\otimes Q)=0,
 \qquad
 \operatorname{Ext}^1(L_\beta\otimes P,L_\gamma\otimes Q)=0
 \tag{E815.11}
\]

for all \(P,Q\in\operatorname{Pic}^0(X)\), by the published index theorem. The exact filtration induction in SF-E813, which only uses these two vanishings, gives actual canonical decompositions

\[
 \mathcal H^j(E)=\bigoplus_{\beta\in\mathcal B} H^j_\beta.
 \tag{E815.12}
\]

Each \(H^j_\beta\) is filtered entirely by line bundles of class \(\beta\). Translation/tensor functors preserve that class and are exact for the usual cohomological structure. Thus the given coherent linearizations of \(E\) induce coherent structures on its cohomology sheaves and preserve each canonical summand (E815.12).

Consequently the objects

\[
 U_\beta=\bigoplus_j H^j_\beta[-j]
 \tag{E815.13}
\]

are actual perfect objects of the given equivariant category. They are not asserted to be direct summands of \(E\). Their characters are

\[
 \operatorname{ch}(U_\beta)=n_\beta e^\beta,
 \qquad n_\beta=\sum_j(-1)^j\operatorname{rk}H^j_\beta\in\mathbf Z.
 \tag{E815.14}
\]

The usual cohomological truncations are canonical and are preserved by all the exact translation/tensor functors. Their distinguished triangles therefore exist in the specified equivariant category. Additivity in its Grothendieck group, followed by the actual cohomology decompositions (E815.12), gives

\[
 [E]=\sum_j(-1)^j[\mathcal H^j(E)]
      =\sum_{\beta\in\mathcal B}[U_\beta]
      \quad\text{in }K_0(\mathcal C^G).
 \tag{E815.14a}
\]

In particular this is an equivariant Grothendieck-group identity, although the \(U_\beta\) need not be direct summands of \(E\). Additivity gives \(\sum_\beta\operatorname{ch}(U_\beta)=kC\). The independence in §2 therefore forces

\[
 (n_0,n_{X_0},n_{-X_0},n_{Z_+},n_{-Z_+},n_{Z_-},n_{-Z_-})
    =k(24,2,2,1,1,1,1).
 \tag{E815.15}
\]

Thus every possible negative cohomological contribution has been accounted for before any positivity argument is used.

## 4. Exact cross-Euler scaling for the finite action

We use the identity-sector argument of supplied DEG_L S-21, with its specified coherent action and effective-subgroup hypothesis. Its proof was reread here; only the general categorical argument, not the secant-specific conclusion, is used. Write \(F:\mathcal C^G\to\mathcal C\) for forgetting and \(I\) for induction, where \(\mathcal C=\operatorname{Perf}(X)\). The proof of (S21.6) gives

\[
 \operatorname{ch}_{HH}(IFV)=|G|\operatorname{ch}_{HH}(V)
 \quad\text{for every }V\in\mathcal C^G.
\]

For any two objects \(U,V\in\mathcal C^G\), the right adjunction and categorical Riemann--Roch now give

\[
 \begin{split}
 \chi_X(FU,FV)
 &=\chi_{\mathcal C^G}(U,IFV)\\
 &=|G|\chi_{\mathcal C^G}(U,V).
 \end{split}
 \tag{E815.16}
\]

This is the cross-pair version of (S21.7). It does not require either object to be simple or semiregular. It also does not require a model in which the group acts freely by translations. All possible coherence cocycles and projective multiplicity spaces are already incorporated in \(\mathcal C^G\).

The exact inputs in the supplied proof are its vanishing of nonidentity translation/tensor coefficient sectors, induction/forgetting adjunction, and the categorical Riemann--Roch pairing. No new unrefereed theorem is being treated as a published statement here.

Apply (E815.16) to the actual equivariant objects \(U_{X_0},U_{Z_+}\). By (E815.15) their ordinary Euler pairing is

\[
 \begin{split}
 \chi_X(U_{X_0},U_{Z_+})
 &=2k^2\int_X e^Y\\
 &=8k^2.
 \end{split}
 \tag{E815.17}
\]

The last equality follows from \(Y^4=24x^2y^2\) and (E815.3), or from the fact that \(Y\) has integral Hermitian matrix \(US\) of determinant four. Thus

\[
 \frac{8k^2}{|G|}
   =\chi_{\mathcal C^G}(U_{X_0},U_{Z_+})
   \in\mathbf Z_{>0}.
\]

In particular

\[
 |G|\mid8k^2,
 \qquad |G|\le8k^2.
 \tag{E815.18}
\]

This divisibility statement handles arbitrary negative virtual multiplicities before their aggregate is fixed by (E815.15), and it does not assume honest linearizations of any individual line factor.

## 5. The full character forces too large an invariant Euler value

The character (E815.7) is unchanged by duality. In the ring of §2 it is

\[
 C=32+8(x^2+y^2)+2x^2y^2.
\]

The coefficient of \(x^2y^2\) in \(C^2\) is \(256\); (E815.3) therefore gives

\[
 \chi_X(E,E)=1024k^2.
 \tag{E815.19}
\]

Equations (E815.16) and (E815.18) imply

\[
 \chi_{\mathcal C^G}(E,E)
       =\frac{1024k^2}{|G|}\ge128.
 \tag{E815.20}
\]

Suppose in addition that the equivariant object is gluable and weakly semiregular, namely that its invariant self-Ext groups in negative degrees vanish and its full invariant degree-two trace is injective. Supplied S-21 invariant Calabi--Yau adjunction and the exact balanced cap ranks from SF-E801 then give

\[
 e_2^G=18,
 \qquad e_1^G\ge8,
 \qquad e_{4-j}^G=e_j^G.
\]

Consequently

\[
 \chi_{\mathcal C^G}(E,E)
      =2e_0^G-2e_1^G+18\le2e_0^G+2.
 \tag{E815.21}
\]

Combining this with (E815.20) proves the necessary condition

\[
 \boxed{\dim\operatorname{End}_{\mathcal C^G}(E)\ge63.}
 \tag{E815.22}
\]

In particular, **no complex in this model, for any \(k\ge1\), is simultaneously gluable, simple in the equivariant category, and weakly semiregular**. The conclusion allows any effective finite target action, including mixtures of translation and tensor operations. It also allows all extra cancelling terms and projective multiplicities permitted in §3.

The rank-32 polystable bundle (E815.4) is an actual balanced character, but the proposed multivertex repair within these seven line classes cannot produce the required simple equivariant seed. A nonsimple weakly semiregular repair in this model would need at least 63 invariant endomorphisms; this argument does not exclude it outright.

## 6. General positive aggregate weights in the primitive RM divisor space

There is a useful extension independent of the special seven classes. Let \(\mathcal B'\) be any finite set of integral algebraic divisor classes whose pairwise differences are block diagonal and primitive on both genuine RM planes. Let a perfect equivariant object have vector-bundle cohomology filtered by line bundles of those classes and arbitrary degree-zero twists. As above, the unequal-class Hom and degree-one Ext vanish, so its cohomology admits actual canonical equivariant class blocks. Form \(U_\beta\) as in (E815.13), with aggregate virtual ranks \(n_\beta\).

Assume all \(n_\beta\ge0\), and let \(s\) be the number that are nonzero. For every ordered unequal pair with nonzero ranks, the signature \((2,2)\) calculation and (E815.16) give

\[
 \chi_{\mathcal C^G}(U_\beta,U_\gamma)
  =\frac{n_\beta n_\gamma}{|G|}
       \int_X\frac{(\gamma-\beta)^4}{24}
  \in\mathbf Z_{>0}.
\]

Self-pairings are zero, since each character is a multiple of a single exponential. Zero-character blocks have zero Euler pairing with every object. The equivariant Grothendieck-group identity (E815.14a), valid in this general class-block setting as well, and bilinearity of the Euler pairing therefore imply

\[
 \chi_{\mathcal C^G}(E,E)\ge s(s-1).
 \tag{E815.23}
\]

If the full character is balanced with nonzero coefficient, its degree-two cap rank is 18. Each pure exponential has degree-two cap rank six, so subadditivity forces \(s\ge3\). Hence (E815.23) gives invariant Euler at least six. A gluable, equivariantly simple, weakly semiregular balanced object would instead have invariant Euler at most four, by (E815.21). This is impossible.

The same theorem permits **stable projectively flat vector-bundle factors**, with rational normalized classes \(\beta=c_1(Q)/\operatorname{rk}Q\), in place of line-bundle factors. We give the adaptation explicitly. For two factors of unequal classes, choose an integer \(m\) divisible by their ranks. For a factor \(Q\) of rank \(r\), the actual line bundle \((\det Q)^{m^2/r}\) has the scalar curvature of \([m]^*Q\), so the same harmonic-curvature and unitary abelian-monodromy argument as in SF-E813 gives

\[
 [m]^*Q\simeq
 \bigoplus_{a=1}^{r}(L_Q\otimes P_a),
 \qquad c_1(L_Q)=m^2\beta.
 \tag{E815.24}
\]

For unequal classes, the line differences on this common cover have signature \((2,2)\). The index theorem makes their Hom and degree-one Ext zero. Finite étale trace injects the original groups into the pulled-back groups, so the same two vanishings hold for the stable factors. The two filtration inductions then give the same canonical class-block decomposition of each cohomology sheaf, without requiring that any one stable factor admit a \(G\)-linearization. A block of class \(\beta\) has character equal to its **integer rank** times \(e^\beta\), because the Chern character is additive through its filtration. Its aggregate virtual coefficient \(n_\beta\) therefore remains an integer, even though \(\beta\) is rational. Unequal positive blocks have strictly positive ordinary cross Euler by the signature calculation; exact scaling makes the invariant cross Euler a positive integer. The proof of (E815.23) and the cap-rank contradiction is consequently unchanged. The hypotheses remain locally free stable projectively flat factors, common primitive differences, and nonnegative aggregate virtual ranks.

Thus adding more line or projectively flat factor classes with **nonnegative aggregate virtual weights**, while keeping all differences in the common primitive RM space, cannot repair the model. A construction that escapes this result must change at least one of those precise hypotheses. Negative aggregate weights in an enlarged class set, classes outside that primitive space, singular cohomology, twisted objects, or a sufficiently nonsimple equivariant object are not excluded by this theorem.

## Checks and source scope

The program rm_seven_class_certificate.py actually computes the determinant \(-512\), the entire character, self-Euler1024, opposite-pair Euler16, the matrices \(U^2=2I\), \(US=SU\), and the unimodularity of \(X_0,Z_+,Z_-\). Its JSON output explicitly disclaims verification of categorical existence, actions, or trace injectivity. The proof above gives those logical implications with their stated hypotheses.

The published Mumford index input and its exact pages are already recorded in SF-E813. The new categorical scaling (E815.16) is a direct two-object deduction from the reread induction/forgetting and Riemann--Roch argument of supplied DEG_L S-21, equations (S21.6)--(S21.7). The stable and semistable bundle obstructions SF-E811--E813 are used only in their previously reviewed scopes. No Bando--Siu reflexive extension is assumed.
