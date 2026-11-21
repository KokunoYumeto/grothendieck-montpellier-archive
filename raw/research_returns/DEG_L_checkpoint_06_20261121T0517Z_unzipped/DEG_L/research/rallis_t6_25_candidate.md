# Candidate T6.25: arbitrary maximal-order sources retain square-root core degree

Status: promoted after author, root and bounds whole-proof reviews all passed; this file retains the candidate history. Date 2026-11-21. Actor: GPT-6 Astra Pro; effort not exposed; /root/rallis_t6. This is a quantitative obstruction for the specified transport construction. It is not a lower bound for the least degree of all intrinsic target Weil witnesses.

## Proposed theorem T6.25

Let \(K\subset E\) be an imaginary quadratic subfield of a CM field, with \([E:K]=g=2n\), \(n\ge2\). Let \(A\) have dimension \(g\), rational homology of rank one over \(E\), and integral \(\mathcal O_K\)-action of Weil signature \((n,n)\). Its polarization \(L\) has Rosati conjugation on \(K\). Put
\[
 \Delta=|\operatorname{disc}K|,\qquad
 V=\chi(L)=\int_A\frac{c_1(L)^g}{g!}.
 \tag{T25.1}
\]
In the common CM analytic model let its integral homology be \(\Lambda\), let
\[
 \Lambda^-=\{x\in\Lambda:\mathcal O_E x\subseteq\Lambda\},\quad
 J=[\Lambda:\Lambda^-],\quad
 \mathfrak j=\det_{\mathcal O_K}\Lambda^-/
                        \det_{\mathcal O_K}\Lambda.
 \tag{T25.2}
\]
Thus \(\mathfrak j\) is an integral ideal with \(N_{K/\mathbf Q}\mathfrak j=J\).

Write \(e_A\) for the canonical rational projector onto the middle \(K\)-Weil plane. Fix \(R\ge1\) such that the polynomial projector \(P_A=Re_A\) of B6 preserves integral cohomology on every \(g\)-dimensional abelian variety with the indicated integral \(\mathcal O_K\)-action. Such an \(R\) depends only on the fixed \(K,g\) and the chosen integral generic-field element.

Let \(\Gamma\) be any integral signed \(n\)-cycle whose cycle class is an integral linear combination of classes
\[
 (h_\ell)_*[Z_\ell],
 \tag{T25.3}
\]
where \(h_\ell:B_\ell\to A\) is an \(E\)-linear homomorphism of abelian varieties, \(B_\ell\) has integral maximal \(\mathcal O_E\)-action, and \(Z_\ell\) is an integral \(n\)-cycle on \(B_\ell\). The sources, their dimensions, their cycles and the number of summands may all vary. Proper pushforward in (T25.3) retains every generic multiplicity. A source cycle whose image has smaller dimension contributes zero.

For a signed cycle write \(D_{\rm abs}(\Gamma)\) for the sum of the absolute coefficients times the \(L\)-degrees of its irreducible components.

### A. Exact common core content and degree growth

One has
\[
 v=P_A[\Gamma]\in\overline{\mathfrak j}\,\mathscr W_A,
 \qquad \mathscr W_A=W_A\cap H^g(A,\mathbf Z).
 \tag{T25.4}
\]
If \(e_A[\Gamma]\ne0\), then \(v\) is a nonzero integral vector, and
\[
 \frac{q_A(v,v)}{2\Delta^{\,n-1}}\in J\mathbf Z_{>0},
 \qquad
 D_{\rm abs}(\Gamma)
   \ge
    \frac{2^n n!\sqrt V\,\Delta^{(n-1)/2}}{R}\sqrt J.
 \tag{T25.5}
\]
Thus the degree assertion requires only a nonzero rational Weil projection of the integral cycle; it does not require that the unscaled projection \(e_A[\Gamma]\) itself be integral, or aligned with any previously fixed target vector. Integral combinations of arbitrarily many such transports cannot remove the bound.

The inequality also applies to any other integral cycle representative with the same projected class, even if that representative is constructed differently. It does not constrain arbitrary integral target cycles whose projections lie outside the subgroup (T25.4).

### B. Bounded division by image multiplicities

Suppose instead that \(\Gamma\) is an integral linear combination of reduced image cycles, each arising from such a map and integral \(n\)-dimensional source subvariety, and the corresponding finite generic degrees are at most a fixed positive integer \(S\). Put
\[
 L_S=\operatorname{lcm}(1,2,\ldots,S).
 \tag{T25.6}
\]
If the projection of \(\Gamma\) is nonzero, then
\[
 D_{\rm abs}(\Gamma)
   \ge
    \frac{2^n n!\sqrt V\,\Delta^{(n-1)/2}}{R L_S}\sqrt J.
 \tag{T25.7}
\]
This condition on generic degrees is substantive. For a fixed simple maximal-order source of dimension \(g\), bounded-degree middle subvarieties have such a bound by B22/B22a; the precise bound and the multiplicity formula are recorded in B23. No bound on generic degrees is asserted for arbitrary higher-dimensional sources.

### C. The exponent is exact for this class of constructions

Assume in addition that \(E\), the CM type and the target polarization volume \(V\) are fixed; that the polarization has Rosati conjugation on \(E\); and that one fixed maximal-order source
\(A_0=\mathbf C^g/\Phi(I_0)\), with polarization volume \(V_0\), has an effective integral middle cycle \(Z_0\) of degree \(D_0\) and nonzero \(K\)-Weil projection. Let \(D_{\rm tr}(A)\) be the least total absolute degree of an integral cycle with nonzero Weil projection whose class belongs to the transport group described in (T25.3). Then
\[
 \begin{aligned}
 \frac{2^n n!\sqrt V\,\Delta^{(n-1)/2}}{R}\sqrt J
 &\le D_{\rm tr}(A)\\
 &\le D_0 K_E^n\left(\frac V{V_0}\right)^{1/2}\sqrt J,
 \qquad
 K_E=\frac2\pi\bigl(g!\sqrt{|D_E|}\bigr)^{1/g}.
 \end{aligned}
 \tag{T25.8}
\]
Here \(D_E\) is the discriminant of \(E\). The upper bound is achieved by one effective pushforward with its actual multiplicity. Thus allowing all maximal-order sources and all integral combinations changes neither the square-root exponent nor the need for core growth in this construction. The source existence in Part C is an explicit hypothesis, already available once a fixed CM witness has been constructed.

## Proof

### 1. Every maximal-order source map factors through the target core

Let
\[
 A^-=\mathbf C^g/\Phi(\Lambda^-),\qquad
 i:A^-\longrightarrow A.
 \tag{T25.9}
\]
This is an isogeny of degree \(J\); \(A^-\) has integral maximal \(\mathcal O_E\)-action and is polarized, for example, by \(i^*L\). For an \(E\)-linear \(h:B\to A\) as in the statement, its integral homology image is \(\mathcal O_E\)-stable:
\[
 a\,h_*x=h_*(a x)\in h_*H_1(B,\mathbf Z)
 \quad(a\in\mathcal O_E,\ x\in H_1(B,\mathbf Z)).
 \tag{T25.10}
\]
It is a subgroup of \(\Lambda\), and is therefore contained in \(\Lambda^-\). The complex linear universal-cover map defining \(h\) consequently descends through the core lattice, giving an actual homomorphism
\[
 h^-:B\longrightarrow A^-,\qquad h=i\circ h^-.
 \tag{T25.11}
\]
No dimension or surjectivity argument is needed for this factorization. The proper pushforward \(\zeta=h^-_*Z\) is an integral \(n\)-cycle on \(A^-\), possibly zero, and \(h_*Z=i_*\zeta\).

### 2. Its exact action on the actual integral Weil plane

The determinant-lattice formula of B23 or T6.24 gives, in the common rational cohomology,
\[
 \mathscr W_{A^-}=\mathfrak j^{-1}\mathscr W_A.
 \tag{T25.12}
\]
The isogeny \(i\) is induced by the identity of universal vector spaces. Hence \(i^*\) is the identity on the common rational cohomology, and \(i_*=J\) there. For ideals of an imaginary quadratic field,
\(\mathfrak j\overline{\mathfrak j}=(J)\). It follows exactly that
\[
 i_*\mathscr W_{A^-}
       =J\mathfrak j^{-1}\mathscr W_A
       =\overline{\mathfrak j}\,\mathscr W_A.
 \tag{T25.13}
\]
The degree-\(g\) polynomial projector is integral on \(A^-\) with the same \(R\). Since \(i\) is a same-dimensional \(K\)-linear isogeny, it commutes with the rational extreme projector:
\[
 P_A i_*[\zeta]=i_* P_{A^-}[\zeta]
       \in i_*\mathscr W_{A^-}.
 \tag{T25.14}
\]
This proves (T25.4) on every summand and hence on their integral span. It does not assert that a fixed-degree polynomial projector commutes with pushforward through the possibly different-dimensional map \(h^-\); the projection is applied after that pushforward, on the \(g\)-dimensional variety \(A^-\).

### 3. Exact ideal content gives a nonzero norm bound

For nonzero \(v\in\overline{\mathfrak j}\mathscr W_A\), its determinant-order envelope satisfies
\[
 \mathcal O_K v\subseteq\overline{\mathfrak j}\mathscr W_A
                         \subseteq\mathscr W_A.
 \tag{T25.15}
\]
The second inclusion has index \(J\). T6.24's exact norm-index formula therefore gives
\[
 \frac{q_A(v,v)}{2\Delta^{n-1}}
     =[\mathscr W_A:\mathcal O_Kv]
     =J[\overline{\mathfrak j}\mathscr W_A:\mathcal O_Kv]
     \in J\mathbf Z_{>0}.
 \tag{T25.16}
\]
This is stronger than an estimate using an arbitrary chosen coefficient vector, and is independent of any target generator or ideal-class representative.

By B26, every effective middle cycle \(Z\) satisfies
\[
 \|e_A[Z]\|_{q_A}
    \le\frac{\deg_LZ}{2^{n-1/2}n!\sqrt V}.
 \tag{T25.17}
\]
Applying the triangle inequality to the irreducible signed decomposition gives the same bound with \(D_{\rm abs}(\Gamma)\) for any integral signed \(\Gamma\). Since \(v=R e_A[\Gamma]\), (T25.16) gives
\[
 \sqrt{2\Delta^{n-1}J}
 \le\|v\|_{q_A}
 \le\frac{R D_{\rm abs}(\Gamma)}
                {2^{n-1/2}n!\sqrt V}.
 \tag{T25.18}
\]
Rearranging proves (T25.5). The estimate uses only the projected cycle class and the mass of the chosen representative, which proves its stated invariance under replacing that representative.

### 4. Reduced-image denominators and the upper construction

For an individual reduced image of finite generic degree \(\delta\le S\), proper pushforward gives
\[
 h_*[Z]=\delta[h(Z)_{\rm red}].
 \tag{T25.19}
\]
Since \(\delta\mid L_S\), multiplying an integral sum of such reduced images by \(L_S\) expresses it as an integral sum of the proper pushes in Part A. Its Weil projection remains nonzero, and its total absolute degree is multiplied by \(L_S\). Applying (T25.5) proves (T25.7). If different summands have common components, first combine their coefficients; the argument still applies to the resulting cycle class and its absolute degree.

For Part C, B19.2, in the rank-one homology extension checked in T6.17, supplies an actual \(E\)-linear isogeny \(h:A_0\to A\) whose squared Hom norm satisfies
\[
 Q_A(h)\le K_E\left(\frac V{V_0}J\right)^{1/g}.
 \tag{T25.20}
\]
That ideal-lattice proof requires only rank-one \(E\)-homology and Rosati conjugation on \(E\); it does not require primitivity of the CM type. The invariant positive forms obey \(h^*\omega\le Q_A(h)\omega_0\). Integrating their \(n\)-th powers on \(Z_0\), as in B19.3, gives
\[
 \deg_L(h_*Z_0)
    \le D_0Q_A(h)^n
    \le D_0K_E^n\left(\frac V{V_0}\right)^{1/2}\sqrt J.
 \tag{T25.21}
\]
Its Weil projection is nonzero because an isogeny induces an isomorphism on the rational Weil plane and commutes with its projector. This provides an admissible effective integral cycle for the minimum defining \(D_{\rm tr}\). Positive absolute degrees are positive integers, so the nonempty minimum exists. The lower bound is Part A. This proves (T25.8). QED.

## Sources and scope

The core factorization, arbitrary-source extension and norm/index consequence are proved above. B23 provides the exact determinant conventions; T6.24 provides the actual maximal-order Weil lattice and its exact positive norm. B19.2–B19.3 provide the small-isogeny upper bound and its full proper-multiplicity degree comparison. Their displayed proofs were reread for this corollary.

B26 is the checked exact polarization normalization of the calibration inequality. Its principal-angle input is rStation paper4/v1 by gabrielov_cell, *Calibrated Geometry of Weil Classes...*, 16 October2026, Theorem1(b), Section2, with the differential-form conversion in Theorem3(c), Section4, <https://rstation.ai/problems/hodge_conjecture/papers/4/v1>. Only that calibration bound is used here; no other claims of that paper are imported.

For the qualitative unboundedness of \(J\), B24 proves that any infinite set of distinct fixed-field, fixed-type, fixed-volume polarized targets has unbounded core index. Consequently (T25.8) excludes uniformly bounded transport witness degrees on such a set. It does not prove that the least degree of unrestricted intrinsic target witnesses grows: cycles from sources of increasing nonmaximal order, reduced images with unbounded generic multiplicity, or genuinely different target constructions remain outside the hypothesis.

No proof-assistant verification is claimed.

## Check status

The author, root and bounds read the complete saved proof and passed it before promotion. The positive-integer multiplicity bound and the already checked rank-one version of the small-isogeny theorem were made explicit after review. Actual source and proof checks are recorded separately.
