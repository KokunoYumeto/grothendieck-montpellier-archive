# F63 extension: exact strict effectivity classification for the iterated three-strand simples

Author: /root/gct_statements, GPT-6 Astra Pro; reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

This is a classification of individual generic simple modules for the published iterated three-strand algebras. It is not a classification of arbitrary direct sums, a regular integral-lattice assertion at v=1, or a refutation of the sources' signed/factored positivity. The factor count k and strand rank r=3 remain distinct.

## 1. Exact source modules

Use Blasiak, *Nonstandard braid relations and Chebyshev polynomials*, arXiv1010.0421v2. The frozen local PDF has SHA256 `1970dbbe63dcf8b4f32b00d6b637b7b9425f743f21f91d7d9565ad10a1a82387`. I freshly reread the full primary contexts of Section2.4 pp6--7, equation13 and criterion14 pp8--9, and Theorem3.4 with its proof and Corollary3.5 pp12--13.

Set K=Q(v), delta=v+v^{-1}, D=delta². The source variable u is renamed v. For k≥1, Theorem3.4 and Corollary3.5 give the two one-dimensional simples epsilon_check± and, for1≤j≤k,

\[
 M_{k,j}=epsilon_+^{\otimes(k-j)}\otimes\check M^{(j)}
 \simeq\check X^{(k)}\bigl((\delta^k T_j(1/\delta))^2\bigr).
 \tag{SE1}
\]

This is an actual published classification, not a new result. Equation13, p8, gives the actual left-column generator matrices of Xcheck^(k)(c):

\[
 P_1\mapsto\begin{pmatrix}\delta^k&c\\0&0\end{pmatrix},
 \qquad P_2\mapsto\begin{pmatrix}0&0\\1&\delta^k\end{pmatrix}.
 \tag{SE2}
\]

The one-dimensional actions, stated in Section2.4 p7, are P_i↦delta^k for epsilon_check+ and P_i↦0 for epsilon_check−.

Define

\[
 A_j=\delta^jT_j(1/\delta),\qquad
 c_{k,j}=\delta^{2(k-j)}A_j^2.
 \tag{SE3}
\]

The elementary Chebyshev recurrence gives

\[
 A_0=A_1=1,\qquad A_j=2A_{j-1}-DA_{j-2}.
 \tag{SE4}
\]

In particular each A_j is in Z[D] and is bar-invariant. The source's c in SE2 is exactly c_(k,j), with no additional scalar normalization.

## 2. Complete strict named-generator classification

Call a generic module strictly effective here if it has a K-basis in which both specified P_1,P_2 have entries in N[v,v^{-1}]. This is only a property of the named action. It does not mean a source-designated canonical basis or a categorical simple has been constructed.

### Proposition SE-A

For every k≥1, the two one-dimensional simples are strictly effective. Among the two-dimensional simples M_(k,j), strict effectivity holds exactly for

\[
                    j\in\{1,2,3,5\}\cap[1,k].
 \tag{SE5}
\]

For every other j, no simultaneous basis even gives nonnegative-real Laurent matrices for both named generators.

### Proof: the four effective indices

The exact first values of SE4 give

\[
\begin{array}{c|c|c}
j&A_j&\text{a choice of }B_j=\pm A_j\text{ in }\mathbb N[v,v^{-1}]\\\hline
1&1&1\\
2&2-D&v^2+v^{-2}\\
3&4-3D&3v^2+2+3v^{-2}\\
5&5D^2-20D+16&5v^4+6+5v^{-4}.
\end{array}
 \tag{SE6}
\]

Put m=delta^k and b=delta^(k-j) B_j. Since k-j≥0, b is a nonzero effective Laurent polynomial, and b²=c_(k,j). Conjugating SE2 by S=diag(b,1), specifically S^{-1}P_iS, gives

\[
             P_1=\begin{pmatrix}m&b\\0&0\end{pmatrix},
             \qquad P_2=\begin{pmatrix}0&0\\b&m\end{pmatrix}.
 \tag{SE7}
\]

These are actual named matrices, with entries in N[v,v^{-1}]. The one-dimensional source matrices are already effective. This proves existence in every case in SE5.

### Proof: every other index has a positive real zero

The remaining indices are precisely the even j≥4 and the odd j≥7. Choose the odd integer

\[
 \ell=j-1\quad(j\text{ even}),\qquad
 \ell=j-2\quad(j\text{ odd}).
\]

In the even case j>3 and in the odd case j>6, so

\[
      \frac{\pi}{3}<\theta=\frac{\ell\pi}{2j}
                       <\frac{\pi}{2}.
 \tag{SE8}
\]

Thus x0=cos(theta) lies strictly between0 and1/2, and T_j(x0)=cos(j theta)=cos(ell pi/2)=0. Set delta0=1/x0>2 and

\[
           v_0=\frac{\delta_0+\sqrt{\delta_0^2-4}}2>1.
 \tag{SE9}
\]

Then v0+v0^{-1}=delta0, so A_j(v0)=0 and c_(k,j)(v0)=0 for every k≥j. The polynomial c_(k,j) is nonzero: at v=1, delta=2 and

\[
       c_{k,j}(1)=2^{2k}\cos^2(j\pi/3)>0,
 \tag{SE10}
\]

because an integer j never makes cos(j pi/3) vanish.

Direct multiplication of the source matrices SE2 gives

\[
                     \operatorname{Tr}(P_1P_2)=c_{k,j}.
 \tag{SE11}
\]

A nonzero Laurent polynomial with nonnegative real coefficients is strictly positive at every positive real argument. If both named matrices were nonnegative Laurent in any simultaneous basis, their product trace would be such a polynomial. SE9--SE11 contradict this basis-independent trace. This proves nonexistence for every remaining j and completes the classification. QED.

The factor delta^(2(k-j)) does not spoil this particular obstruction: it is strictly positive at v0, so the zero remains. This is a proved statement about the simple trace SE11. It does not assert that multiplying an arbitrary mixed-sign whole-tensor trace by a positive polynomial preserves its negative coefficients.

## 3. Exact arithmetic and categorical boundaries

For every excluded index, c_(k,j) belongs to Z[v²,v^{-2}], since A_j is a polynomial in D and the prefactor is an even power of delta. It has coefficients of both signs: it is nonzero and zero at a positive v0, excluding all coefficients of one nonnegative sign; it is positive at v=1 by SE10, excluding all coefficients nonpositive. Consequently under either v=Q^{n/2} or v=Q^n its distinct visible roots all have even point weight and its Euler multiplicities have mixed signs.

The F57 pure-point criterion therefore excludes any bounded uninserted point complex of one integral Deligne weight with this trace at all sufficiently large extension degrees. In detail, BBD5.1.8 permits a root of point weight e in a pure weight-w complex only in degree e-w. All visible Euler signs would be (-1)^w. Eventual finite power-sum uniqueness contradicts the mixed signs. A fixed root cannot be hidden by cancellation in another pure degree. Jordan blocks do not change multiplicities. Overall Tate and parity shifts do not repair this, while arbitrary mixed complexes or inserted traces are not excluded.

For the positive cases, actual effective two-state graded kernels can be made from the coefficient spaces of m,b in SE7. Their quadratic maps K_i²≅M⊗K_i, with char M=m, are the actual coefficient associativity/distributivity/symmetry identifications. Applying the full-Tate F61 functor grade e→E(-e)[-2e] supplies individual pure weight-zero derived kernels under v=Q^n, for ell not dividing Q and E finite/Q_ell. This retains the named action and quadratic only. It is not a categorical implementation of every source relation, a compatible iteration, or a canonical-simple classification.

Crucially, this is a simple-module theorem. It does not classify arbitrary semisimple direct sums or forbid a positive model containing a non-effective generic summand. F66 is an actual counterexample to that stronger inference: its positive four-dimensional module contains the j=4 simple, whose designated projector cannot be effective. F67 separately tests specified entire tensor outputs and proves failures of the effective iteration; that is a different assertion.

Nor does the displayed generic balanced basis identify the actual ambient tensor lattice at v=1. In particular the j=3 example has exactly F67's non-S3 specialization in this chosen lattice. No new regular specialization, quantum-group comodule tensor compatibility, canonical basis label or published positivity refutation is claimed. The source's signed/factored positivity remains a distinct requirement.

## 4. Separate F63 Grothendieck dictionary

The source modules and explicit conjugations are affine finite-dimensional module/action data over Q(v), in the EGA I Theorem1.3.7 p86, Corollary1.3.8 p87 and Theorem1.4.1 pp90--92 dictionary. SGA3 I4.7.2--3 and cote90 scan17 supply action and split-torus language; they do not identify an auxiliary positive basis with the designated canonical one.

The effective coefficient cone N[v,v^{-1}] consists of actual finite graded representation characters. SGA6 V Sections2--3 and cote133 scan18 provide effective/virtual language, not a lambda-ring structure on the noncommutative simple-action algebra. The positive-real-zero argument concerns this exact effective cone.

The optional derived point kernels fit SGA6 I Definition4.7 pp121--122 and Example4.8 p122, and BBD5.1.5/5.1.8 pp125--127 fix the integral-weight pure-complex convention. The pure-word comparison is an extra arithmetic axiom; the source classification itself supplies no such sheaf realization or all-rank NSRH statement.

## 5. Verification and requested fresh review

The proof for every j is the explicit angle and positive-real-zero argument SE8--SE11, not a bounded computation over sample indices. The short exact script `verify_iterated_simple_effectivity.py` checks the source balancing identity, trace normalization and the four positive Laurent formulas from the Chebyshev recurrence; it does not purport to establish the universal root argument by testing finitely many j.

Frozen prior reports and root master artifacts remain unchanged. Fresh independent whole-proof and source-scope review is requested before generating the final integration fragment.
