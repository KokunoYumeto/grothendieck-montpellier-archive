# Candidate T6.24: the integral Weil plane has finitely many positive lattice shapes

Status: promoted after author, root and bounds whole-proof reviews all passed; this file retains the candidate history. Date 2026-11-21. Actor: GPT-6 Astra Pro; effort not exposed; /root/rallis_t6. This is a positive counterpart to T6.23 for the actual fixed-imaginary-quadratic Weil plane. It does not construct algebraic cycles of bounded degree.

## Proposed theorem T6.24

Fix an imaginary quadratic field \(K\), its maximal order \(\mathcal O_K\), and an even positive integer \(g=2n\). Write \(\Delta=|\operatorname{disc}K|\). Let \(A\) be any complex abelian variety of dimension \(g\) with an integral \(\mathcal O_K\)-action, of Weil type with signature \((n,n)\). Assume its polarization has Rosati involution restricting to conjugation on \(K\). Put
\[
 W_A=\bigwedge\nolimits_K^g H^1(A,\mathbf Q)
       \ \subset H^g(A,\mathbf Q),\qquad
 \mathscr W_A=W_A\cap H^g(A,\mathbf Z),
 \qquad q_A(u,v)=(-1)^n\int_Au\wedge v.
 \tag{T24.1}
\]
Here the displayed inclusion means the two extreme \(K\)-eigenspaces in the ordinary rational exterior power. The \(K\)-module structure on this plane is the determinant coefficient action. In particular, a geometric scalar endomorphism \([a]^*\) acts on it by \(a^g\), not by \(a\).

### A. Exact maximal-order classification

The form \(q_A\) is positive definite and is the \(L^2\) pairing for every compatible translation-invariant polarization metric. Choose one fractional ideal \(\mathfrak b_j\) from each of the \(h_K\) ideal classes of \(K\), and a \(\mathbf Z\)-basis \(\beta_{j1},\beta_{j2}\) for each. Every lattice \((\mathscr W_A,q_A)\) is isometric to one of the following \(h_K\) positive rank-two lattices:
\[
 \left(\mathfrak b_j,\ 
        (z,w)\longmapsto
        \frac{2\Delta^{\,n-1}}{N(\mathfrak b_j)}
                      \operatorname{Re}(z\bar w)\right).
 \tag{T24.2}
\]
The ideal norm of a fractional ideal is positive. Thus the list depends only on \(K,n\), and not on \(A\), its polarization degree, or a chosen Hecke presentation. Distinct ideal classes need not give distinct unoriented isometry classes, so the assertion is an upper bound of \(h_K\).

In particular,
\[
 \det(\mathscr W_A,q_A)=\Delta^{\,g-1}.
 \tag{T24.3}
\]
For every nonzero \(w\in\mathscr W_A\), the determinant-order submodule \(\mathcal O_Kw\) has exact index
\[
 [\mathscr W_A:\mathcal O_Kw]
       =\frac{q_A(w,w)}{2\Delta^{\,n-1}}\in\mathbf Z_{>0}.
 \tag{T24.4}
\]
In particular \(q_A(w,w)\ge 2\Delta^{n-1}\). Define
\[
 C_{K,n}
   =\max_{j,\ell}
       \left(\frac{2\Delta^{\,n-1}}{N(\mathfrak b_j)}\right)^{1/2}
                       |\beta_{j\ell}|.
 \tag{T24.5}
\]
Every \(\mathscr W_A\) has a \(\mathbf Z\)-basis \(w_1,w_2\) with
\[
 \|w_\ell\|_{q_A}\le C_{K,n},\qquad
 [\mathscr W_A:\mathcal O_Kw_\ell]
        \le \frac{C_{K,n}^2}{2\Delta^{\,n-1}}.
 \tag{T24.6}
\]
Each basis vector is primitive in \(H^g(A,\mathbf Z)\), since \(\mathscr W_A\) is its intersection with a rational subspace.

### B. A fixed smaller order still gives finitely many shapes

Replace the integral maximal-order action by an integral action of a fixed order \(\mathcal O\subset\mathcal O_K\). Let \(f\ge1\) be a fixed integer with \(f\mathcal O_K\subset\mathcal O\). Retain the Weil signature and Rosati assumptions on the rational \(K\)-action. The positive lattices \((\mathscr W_A,q_A)\) then belong to a finite list depending only on \(K,n,f\). Each has a primitive integral basis with
\[
 \|w_\ell\|_{q_A}\le 2f^g C_{K,n}.
 \tag{T24.7}
\]
The precise discriminant in (T24.3) is asserted only under maximal-order integrality.

### C. Scope for the degree and division problem

Part A supplies bounded primitive target vectors, and bounded indices \([\mathscr W_A:\mathcal O_K w]\) for those vectors, without a flat marking or a restriction to one connected family. Part B supplies the corresponding bounded-basis assertion for a fixed order. Together with B8, a uniform effective nonzero Weil-witness degree would therefore give uniform division and signed-degree bounds for such a chosen basis, assuming the fixed polarization type and fixed integral projector data of B8. These lattice facts themselves do not provide the effective witness.

The principal four-factor family in T6.23 does not contradict this theorem. At its sheared split primes, the lattice fails to be stable under a fixed integral imaginary quadratic subfield acting with its two distinct embeddings on the two conjugate coordinates. The full four-CM orbit and the middle \(K\)-Weil plane consequently have different integral constraints.

## Proof

### 1. The pairing is positive and does not depend on the polarization scale

After extending coefficients to \(\mathbf C\), \(H^1\) splits into the two \(K\)-eigenspaces \(V_\sigma,V_{\bar\sigma}\), each of dimension \(g\). The Weil plane is
\[
 W_A\otimes\mathbf C
     =\bigwedge\nolimits^g V_\sigma
        \oplus \bigwedge\nolimits^g V_{\bar\sigma}.
 \tag{T24.8}
\]
The signature assumption makes these lines of Hodge type \((n,n)\). Rosati conjugation makes the polarization form a mixed class in \(V_\sigma\otimes V_{\bar\sigma}\). Wedge multiplication by that form kills each extreme line, so \(W_A\) is primitive. The primitive middle-degree Hodge-star identity gives \(*=(-1)^n\) on \(W_A\); hence its \(L^2\) pairing is exactly (T24.1), and is positive definite. This is the argument of B7, and uses neither a fixed volume nor a lower bound on an injectivity radius.

### 2. An explicit reference lattice and its normalization

Choose a generator \(\tau\) with \(\mathcal O_K=\mathbf Z+\mathbf Z\tau\), embedded in \(\mathbf C\) with \(\operatorname{Im}\tau>0\). Set
\[
 d=\tau-\bar\tau,\qquad d^2=-\Delta.
 \tag{T24.9}
\]
On \(V=K^g\), take the reference homology lattice \(\Lambda_0=\mathcal O_K^g\). Give it a complex structure with \(n\) coordinates using the chosen embedding of \(K\), and \(n\) coordinates using its conjugate. This is the product of the corresponding elliptic curves, so it is an actual polarized abelian variety of the required Weil type. If \(x_j,y_j\) are the real dual coordinates to the ordered homology basis \(1,\tau\) in the \(j\)-th factor, put
\[
 e_j=dx_j+\tau\,dy_j,\qquad
 \zeta=e_1\wedge\cdots\wedge e_g,\qquad
 w_\kappa=\kappa\zeta+\bar\kappa\,\bar\zeta.
 \tag{T24.10}
\]
Every rational vector in the extreme plane has this form, with \(\kappa\in K\).

The expansion in the integral tensor basis has coefficients
\(\operatorname{Tr}_{K/\mathbf Q}(\kappa\tau^s)\), with \(0\le s\le g\). The coefficients for \(s=0,1\) force \(\kappa\) to lie in the trace dual of \(\mathcal O_K\), and this condition makes every other coefficient integral because \(\tau^s\in\mathcal O_K\). The trace dual is exactly \(d^{-1}\mathcal O_K\): its dual basis to \(1,\tau\) is \(-\bar\tau/d,1/d\), and these two elements generate \(d^{-1}\mathcal O_K\) over \(\mathbf Z\). Since the tensor component is a direct summand of integral cohomology, no additional integrality condition or denominator occurs. Consequently
\[
 \mathscr W_0=\{w_{a/d}:a\in\mathcal O_K\}
              =\mathcal O_K w_*,\qquad w_*=w_{1/d},
 \tag{T24.11}
\]
where \(a w_*=w_{a/d}\) is determinant coefficient multiplication, not multiplication of a real vector by a complex scalar.

The complex orientation of the product differs by \((-1)^n\) from the ordered real coordinate orientation
\(dx_1\wedge dy_1\wedge\cdots\wedge dx_g\wedge dy_g\). Reordering \(e_1,\ldots,e_g,\bar e_1,\ldots,\bar e_g\) into coordinate pairs gives
\[
 \zeta\wedge\bar\zeta
   =(-1)^{g(g-1)/2}(-d)^g
              \bigwedge_{j=1}^g(dx_j\wedge dy_j)
   =\Delta^n\bigwedge_{j=1}^g(dx_j\wedge dy_j).
 \tag{T24.12}
\]
Here \(g=2n\), so the two signs cancel. The extreme forms square to zero, while their degree \(g\) is even. Thus
\[
 q_0(w_\kappa,w_\kappa)=2\Delta^n|\kappa|^2,\qquad
 q_0(a w_*,b w_*)=
             2\Delta^{\,n-1}\operatorname{Re}(a\bar b).
 \tag{T24.13}
\]
This computes the constant rather than choosing an unspecified metric on the determinant line.

### 3. Exact transport to an arbitrary maximal-order lattice

Choose a \(K\)-linear rational identification \(H_1(A,\mathbf Q)=K^g\), and let \(\Lambda=H_1(A,\mathbf Z)\) be the resulting \(\mathcal O_K\)-lattice. Its relative determinant ideal and numerical covolume ratio are
\[
 \mathfrak d
       =\det_{\mathcal O_K}\Lambda/
                         \det_{\mathcal O_K}\Lambda_0,\qquad
 \nu=N(\mathfrak d)
       =\frac{\operatorname{covol}_{\mathbf R}\Lambda}
              {\operatorname{covol}_{\mathbf R}\Lambda_0}>0.
 \tag{T24.14}
\]
The covolume identity follows locally from the elementary divisors of a lattice over the discrete valuation rings in \(\mathcal O_K\otimes\mathbf Z_p\). It also holds for fractional lattices, by rescaling.

For completeness, the exact integral determinant rule does not discard primes ramified in \(K\). Over \(\mathbf Z_p\), a maximal-order lattice is free over the product of discrete valuation rings \(\mathcal O_K\otimes\mathbf Z_p\). A change matrix \(T\in\mathrm{GL}_g(K\otimes\mathbf Q_p)\) changes the dual cohomology lattice by the contragredient matrix. Its ordinary \(g\)-th exterior power preserves the rational extreme plane and acts there by determinant coefficient \((\det_KT)^{-1}\). Intersecting with the full integral exterior lattice commutes with this invertible rational change of lattice. The integral standard intersection is an \(\mathcal O_K\otimes\mathbf Z_p\)-module: the integral matrix \(\operatorname{diag}(b,1,\ldots,1)\) acts on the intersection by \(b\), also for nonunits. Therefore these local transformations glue to
\[
 \mathscr W_A=\mathfrak d^{-1}\mathscr W_0
                 =\mathfrak d^{-1}\mathcal O_K w_*.
 \tag{T24.15}
\]
This is the exact intersection-lattice argument of B23, rather than an identification only up to a discriminant denominator.

Top-degree integration of a fixed invariant form scales by the covolume of its homology lattice. The orientation used above remains the correct orientation for every complex structure of \(K\)-signature \((n,n)\). Indeed, relative to the chosen complex structure supplied by \(K\), the actual complex structure has \(n\) positive and \(n\) negative eigendirections; the latter reverse the real two-dimensional orientation \(n\) times. A change of complex basis has positive real determinant. The orientation factor is therefore always \((-1)^n\). It follows that, on the common rational Weil plane,
\[
 q_A=\nu q_0.
 \tag{T24.16}
\]
No requirement that the chosen rational marking preserve a polarization was used.

Set \(\mathfrak b=\mathfrak d^{-1}\), so \(N(\mathfrak b)=\nu^{-1}\). Choose an ideal-class representative \(\mathfrak b_j\) and \(\alpha\in K^\times\) with \(\mathfrak b=\alpha\mathfrak b_j\). Then
\[
 |\alpha|^2=N(\alpha)=\frac{1}{\nu N(\mathfrak b_j)}.
 \tag{T24.17}
\]
The map \(\beta\mapsto\alpha\beta w_*\) is an isomorphism of additive lattices from \(\mathfrak b_j\) to \(\mathscr W_A\). Its metric, by (T24.13) and (T24.16), is precisely (T24.2). Finiteness of the ideal class group proves the asserted finite list and the basis bound (T24.6).

### 4. Discriminant and exact coefficient index

For a fractional ideal \(\mathfrak b\subset K\subset\mathbf C\), its Euclidean covolume is
\[
 \operatorname{covol}_{\mathbf C}(\mathfrak b)
       =\frac{\sqrt\Delta}{2}N(\mathfrak b).
 \tag{T24.18}
\]
Applying this to (T24.2), and recalling that multiplying a real two-dimensional metric by \(c\) multiplies covolume by \(c\), gives
\[
 \operatorname{covol}_{q_A}(\mathscr W_A)
      =\frac{2\Delta^{n-1}}{N(\mathfrak b_j)}
          \frac{\sqrt\Delta}{2}N(\mathfrak b_j)
      =\Delta^{\,n-1/2}.
 \tag{T24.19}
\]
Its square is the Gram determinant (T24.3).

For any nonzero \(w\in\mathscr W_A\), determinant coefficient multiplication identifies \(\mathcal O_Kw\) with \(\mathcal O_K\) carrying metric \(q_A(w,w)\operatorname{Re}(z\bar z')\). Its covolume is \(q_A(w,w)\sqrt\Delta/2\). Dividing by (T24.19) proves (T24.4). The index is a positive integer because the integral Weil lattice is stable under the determinant \(\mathcal O_K\)-action. The positive minimum and bounded index for the chosen basis follow.

### 5. A fixed order and a bounded maximal-order saturation

For an \(\mathcal O\)-stable lattice \(\Lambda\), put \(\Lambda^+=\mathcal O_K\Lambda\). The inclusions
\[
 f\Lambda^+\subseteq\Lambda\subseteq\Lambda^+
 \tag{T24.20}
\]
give
\[
 1\le q=[\Lambda^+:\Lambda]\le f^{2g}.
 \tag{T24.21}
\]
The same universal complex vector space modulo \(\Lambda^+\) is an abelian variety \(A^+\), and the natural isogeny \(u:A\to A^+\) has degree \(q\). To see algebraicity directly, multiply a Riemann form on \(\Lambda\) by \(f^2\); it becomes integral on \(\Lambda^+\), remains positive, and remains compatible with Rosati conjugation. Thus \(A^+\) has a compatible polarization and integral maximal-order action.

Under the common rational marking, pullback \(u^*\) is the identity. Integral cohomological pullback and transfer, with \(u^*u_*=q\), give the exact containments
\[
 L^+:=u^*\mathscr W_{A^+}
      \subseteq\mathscr W_A
      \subseteq q^{-1}L^+.
 \tag{T24.22}
\]
The transfers preserve the rational extreme plane because they are \(K\)-linear. Integration under the degree-\(q\) map gives
\[
 q_A|_{L^+}=q\,q_{A^+}.
 \tag{T24.23}
\]
Thus \(L^+\) has one of the finitely many metrics \(qG_j\), where \(G_j\) is the Gram matrix in (T24.2), and the integer \(q\) belongs to the fixed finite range (T24.21). For each such lattice there are only finitely many intermediate lattices in (T24.22): they correspond to subgroups of the finite group \(q^{-1}L^+/L^+\). This proves the finite-shape assertion.

Here is the stated explicit basis bound. Choose a basis \(e_1,e_2\) of \(L^+\) of lengths at most \(\sqrt q\,C_{K,n}\). The integral sublattice \(S=q\mathscr W_A\) satisfies \(qL^+\subseteq S\subseteq L^+\). A Hermite triangular basis of \(S\), relative to \(e_1,e_2\), can be written
\[
 (a,0),\quad (b,c),\qquad
 1\le a,c\le q,\quad 0\le b<a.
 \tag{T24.24}
\]
The bounds \(a,c\le q\) follow because \(q e_1,q e_2\in S\). Dividing these two basis vectors by \(q\) gives a basis of \(\mathscr W_A\). Each has length at most \(2\sqrt q\,C_{K,n}\), proving (T24.7). Its vectors are primitive in ambient cohomology as before. This argument needs no assumption that \(\Lambda\) is invertible as a module over the smaller order.

### 6. The precise distinction from the full-CM shear family

At a good split prime in T6.23, consider one conjugate coordinate pair with common idempotent basis \(e,f\) and lattice
\[
 L_r=\mathbf Z_p e+\mathbf Z_p(p^{-r}e+f),\qquad r>0.
 \tag{T24.25}
\]
Suppose \(K\subset E\) is an imaginary quadratic subfield. Complex conjugation interchanges the two embeddings of \(K\), so the action of \(a\in\mathcal O_K\) on this pair is \(\operatorname{diag}(a_\sigma,a_{\bar\sigma})\). Since \(p\) is completely split and unramified, choose \(a\in\mathcal O_K\) for which \(a_\sigma-a_{\bar\sigma}\) is a \(p\)-adic unit, by the Chinese remainder theorem at the two primes of \(K\) above \(p\). Applying \(a\) to the second generator of (T24.25) and subtracting \(a_{\bar\sigma}\) times that generator leaves
\[
 p^{-r}(a_\sigma-a_{\bar\sigma})e,
 \tag{T24.26}
\]
which is not in \(L_r\), because a vector supported only on \(e\) belongs to \(L_r\) exactly when its coefficient is integral. Hence the sheared lattice is not \(\mathcal O_K\)-stable. More generally its required order conductor at \(p\) grows with \(r\); no one fixed order containing an element with a bounded nonzero embedding difference stabilizes all these lattices.

The positive lattice theorem therefore removes this particular norm-growth obstruction from the actual fixed-order Weil-family problem. It supplies no control of degrees of effective witnesses, and supplies no comparison between an auxiliary full-CM switch cycle and a generic Weil cycle without their actual correspondence. QED.

## Source and check scope

The new determinant, explicit Gram, orientation, fixed-order, and shear calculations are proved in full above. The exact integral determinant functor and middle Weil positivity are also the previously checked arguments B23 and B7, respectively.

Primary arithmetic background: J.S. Milne, *Algebraic Number Theory*, version 3.08, 19 July 2020, Proposition 4.2, printed pp.69–70 (ideal norm and index); Theorems 4.3–4.4, printed pp.70–71 (class-group finiteness); Proposition 4.26, statement p.79 and complete proof p.80 (ideal covolume). URL: <https://www.jmilne.org/math/CourseNotes/ANT.pdf>. Proposition 4.26 is initially stated for integral ideals; its fractional-ideal version follows by multiplication by a nonzero integer and the real determinant of that scalar.

The trace-dual normalization agrees with Keith Conrad, *The Different Ideal*, Definition 3.2 p.4 and Theorem 3.9 p.8, at <https://kconrad.math.uconn.edu/blurbs/gradnumthy/different.pdf>. The quadratic dual basis actually used here has been computed directly, so no ramification convention is left implicit.

No proof-assistant verification or numerical experiment is claimed.

## Check status

The author, root and bounds each read the complete saved proof and passed it before promotion. The exact quadratic trace-dual lattice, orientation, determinant covariance at ramified primes, norm cancellation, fixed-order saturation and stated scope were checked. Actual source and proof events are recorded separately.
