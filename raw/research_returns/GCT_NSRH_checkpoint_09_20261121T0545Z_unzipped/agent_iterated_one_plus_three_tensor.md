# F67 supplement: the actual one-plus-three whole tensor

Author: /root/gct_statements, GPT-6 Astra Pro; reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

The frozen three-plus-three report and fragment remain unchanged. This supplement proves a smaller specified tensor operation failure, without claiming a minimal threshold among all possible earlier cases.

## 1. Exact source and effective inputs

Retain the primary source, conventions and full contexts read for F67: Blasiak, arXiv1010.0421v2, Definition2.5 and equations8--11 p6 (actual restriction), equation13 p8 and criterion14 p9 (simple matrices), Theorem3.4 and equations25--26 p12 (source simples and occurrence), Corollary3.5 p13 (generic split semisimplicity and specialization warning). The local PDF SHA256 is `1970dbbe63dcf8b4f32b00d6b637b7b9425f743f21f91d7d9565ad10a1a82387`. The variable u is renamed v, delta=v+v^{-1}, D=delta². The strand rank is r=3 throughout.

The balanced source matrices for two factors with parameters (m,a) and (n,b) are

\[
 N_1=\begin{pmatrix}m&a\\0&0\end{pmatrix},\quad
 N_2=\begin{pmatrix}0&0\\a&m\end{pmatrix},\qquad
 L_1=\begin{pmatrix}n&b\\0&0\end{pmatrix},\quad
 L_2=\begin{pmatrix}0&0\\b&n\end{pmatrix}.
 \tag{OT1}
\]

For the actual source modules Mcheck^(1) and Mcheck^(3), put

\[
 m=\delta,\quad a=1,\quad n=\delta^3,\quad b=3D-4.
 \tag{OT2}
\]

The first source parameter is (delta T1(1/delta))²=1. The second is (delta³T3(1/delta))²=(4-3D)²=b², exactly as in F67. The first pair already has the balanced form; the second is obtained by diag(b,1) conjugation as proved there. Both are genuine generic source simples, because m²-a²=D-1 and n²-b²=(D-1)(D-4)² are nonzero in Q(v).

All four input characters m,a,n,b are in N[v,v^{-1}]. Actual two-state graded coefficient kernels with the stated named matrices and quadratic coefficients m and n are obtained by finite graded spaces of these characters. Their quadratic maps are the entrywise distributivity/symmetry identifications. The full-Tate functor of F61 supplies pure weight-zero derived point kernels with v=Q^s for their individual actions, where s is the extension degree. This supplies effective inputs, not a categorical restriction map.

## 2. Full direct matrix certificate for the actual restriction

The source Delta^(1,3) gives, on the entire four-dimensional tensor,

\[
 R_i=N_i\otimes L_i+(mI-N_i)\otimes(nI-L_i).
\]

With h=mn, its actual matrices are

\[
 R_1=\begin{pmatrix}
 h&mb&an&2ab\\0&0&0&-an\\0&0&0&-mb\\0&0&0&h
 \end{pmatrix},\qquad
 R_2=\begin{pmatrix}
 h&0&0&0\\-mb&0&0&0\\-an&0&0&0\\2ab&an&mb&h
 \end{pmatrix}.
 \tag{OT3}
\]

They satisfy R_i²=hR_i. The full product diagonal is

\[
 m^2n^2-a^2n^2-m^2b^2+4a^2b^2,
 \quad-a^2n^2,\quad-m^2b^2,\quad m^2n^2.
 \tag{OT4}
\]

Thus, before any specialization of m,a,n,b,

\[
 \operatorname{Tr}(R_1R_2)
 =2m^2n^2-2a^2n^2-2m^2b^2+4a^2b^2.
 \tag{OT5}
\]

Substitute OT2 and set A4=D²-8D+8. Elementary expansion gives

\[
 \begin{split}
 \tau_{1,3}(v)
 &=2D^4-20D^3+84D^2-128D+64\\
 &=D^2(D-2)^2+A_4^2\\
 &=2(v^8+v^{-8})-4(v^6+v^{-6})
       +20(v^4+v^{-4})+20(v^2+v^{-2})+52.
 \end{split}
 \tag{OT6}
\]

This directly proves negative Laurent coefficients -4 at v^6 and v^{-6} on the whole output. It agrees with the source decomposition into the j=2 and j=4 simple constituents, but uses neither that decomposition nor a projector.

For comparison, F66's whole two-plus-two tensor at the same total k=4 has trace D^4+A4² and admits a positive basis. The two operations have different input modules and different lower-simple/scalar contributions. A failure of the one-plus-three operation does not contradict the positive two-plus-two model.

## 3. Exact implications and boundaries

If both actual R_i could be simultaneous matrices in N[v,v^{-1}], then their product and trace would have nonnegative Laurent coefficients. OT6 contradicts this basis-independent invariant. The same proof excludes an effective finite graded-kernel construction of the actual restriction on this full four-state tensor when actual composition and the unmarked closed-word trace are retained. No effective output simple projector is assumed.

The whole tensor occurs generically in the restriction of M_(2,1)^{tensor4}: the source proof realizes Mcheck^(3) in the third tensor power of Mcheck^(1), and generic semisimplicity turns that inclusion into a summand. It consequently occurs generically in (V1 tensor V2 tensor V3 tensor V4)^{tensor3} with all dimVi=2, the 4096-dimensional ambient tensor. Its full ambient trace has not been computed here.

The Mcheck^(3) input uses the same regular two-state lattice as F67. At v=1 its normalized involutions have product cube [[7,6],[-6,-5]], rather than I. Hence that lattice is not asserted to be an ambient specialized direct summand. The generic occurrence and OT3--OT6 are valid without this false specialization identification. No claim of a minimal tensor-factor threshold is made.

Under either v=Q^{s/2} or v=Q^s, every visible root of OT6 has even point weight and its Euler coefficients have mixed signs. The F57 pure-point proof (BBD5.1.8, pp126--127, and eventual Vandermonde uniqueness) excludes any bounded pure point complex of one integral weight realizing this uninserted trace. A fixed root in a pure complex has only one allowed degree, so hidden eigenvalues and Jordan blocks cannot repair it. A single overall cohomological parity is likewise impossible, and neither a Tate nor parity shift repairs the signs. Inserted traces are outside this claim.

An actual bounded mixed Tate witness does exist under v=Q^{s/2}: use the 136 positive-coefficient Tate lines of OT6 in degree zero and four copies each of E(-3), E(3) in degree one. Its Euler dimension is136-8=128=tau_(1,3)(1). This is a scalar mixed realization, not an effective operation model. Numerically OT6 is positive for real v>0, being D²(D-2)²+A4²; no negative numerical-trace claim is made.

## 4. Separate Grothendieck dictionary

The exact source inclusion and named module action fit the EGA I affine module dictionary, Theorem1.3.7 p86, Corollary1.3.8 p87 and Theorem1.4.1 pp90--92. SGA3 I4.7.2--3/cote90 scan17 provide action language, not a Hopf structure or an effective iteration. The N[v,v^{-1}] obstruction is in the actual coefficient representation cone; SGA6 V Sections2--3/cote133 scan18 provide effective/virtual language, not a lambda-ring structure on the noncommutative algebra. The mixed Tate witness is a perfect point complex in SGA6 I Definition4.7 pp121--122 and Example4.8 p122. BBD5.1.5/5.1.8 pp125--127 specify the integral-weight pure-complex comparison. Neither effective nor pure operation comparison is inferred as an axiom of the GCT canonical-basis conjectures.

## 5. Actual verification

The exact script `verify_iterated_one_plus_three_tensor.py` reconstructs OT3 directly from the source formula, checks both quadratics, all four diagonal entries OT4, all formulas OT5--OT6 and the positive/mixed multiplicity totals. The source object, generic occurrence, specialization scope and mathematical implications were proved above, not inferred from a finite numerical search. Fresh independent whole-proof and final-fragment review is requested. Frozen F67 and root master files remain unchanged.
