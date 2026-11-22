# F67 — the actual three-plus-three iteration fails on the whole tested tensor

Author: /root/gct_statements, GPT-6 Astra Pro. Reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

The iterated parameter k counts ordinary Hecke tensor factors; the strand rank remains r=3. This is a full proof for a specified actual four-dimensional tensor module. It is not an all-strand-rank theorem, a statement that the entire ordinary ambient tensor has a negative trace, or a specialization claim about an ambient integral lattice.

## 1. Exact primary-source object and normalization

Use Blasiak, Nonstandard braid relations and Chebyshev polynomials, arXiv1010.0421v2. The source's variable u is called v here, and [2]=delta=v+v^{-1}; set D=delta^2. The frozen local primary PDF has SHA256 1970dbbe63dcf8b4f32b00d6b637b7b9425f743f21f91d7d9565ad10a1a82387. I freshly read the full relevant contexts in Sections2.4,3.1,3.2 and3.3.

Definition2.5 and equations8--11, p6, define the actual subalgebra Hcheck_3^(k) of H_3 tensor-power k and its named generators P_i^(k), with Q_i^(k)=delta^k-P_i^(k). In particular the canonical inclusion is
\[
 \Delta^{(k_l,k_r)}(P_i^{(k_l+k_r)})
 =P_i^{(k_l)}\otimes P_i^{(k_r)}
     +Q_i^{(k_l)}\otimes Q_i^{(k_r)}.
 \tag{ST1}
\]
The following sentence on p7 explicitly gives the restricted module for every pair of modules. This is the actual published restriction map; no Hopf coproduct on the whole ordinary H_3 is assumed.

Equation13, p8, defines Xcheck^(k)(c) in the left-column convention by
\[
 P_1^{(k)}\longmapsto
 \begin{pmatrix}\delta^k&c\\0&0\end{pmatrix},\qquad
 P_2^{(k)}\longmapsto
 \begin{pmatrix}0&0\\1&\delta^k\end{pmatrix}.
 \tag{ST2}
\]
Theorem3.4, p12, identifies the actual simple module Mcheck^(3)=Xcheck^(3)((delta^3 T_3(1/delta))^2). Equation24, p11, prints delta^3 T_3(1/delta)=4-3D. Thus put
\[
 m=\delta^3=v^3+3v+3v^{-1}+v^{-3},\qquad
 a=3D-4=3v^2+2+3v^{-2}.
 \tag{ST3}
\]
The source constant in ST2 is c=a^2. Conjugating ST2 by diag(a,1) gives the balanced actual named matrices
\[
 N_1=\begin{pmatrix}m&a\\0&0\end{pmatrix},\qquad
 N_2=\begin{pmatrix}0&0\\a&m\end{pmatrix}.
 \tag{ST4}
\]
The sign change from the source's printed 4-3D is harmless here because ST2 uses its square. Equivalently simultaneous diagonal conjugation changes the sign of both off-diagonal entries.

The module is absolutely irreducible over K=Q(v): the source criterion (14), p9, is c neither0 nor delta^6, and
\[
 m^2-a^2=D^3-(3D-4)^2=(D-1)(D-4)^2
 \tag{ST5}
\]
is nonzero in K. This is a generic assertion; its vanishing at v=1 is treated explicitly below.

## 2. The individual input has effective kernels

Both m and a in ST3 have nonnegative integral Laurent coefficients. Let M,A be finite graded coefficient spaces with those characters. The matrices of kernels
\[
 \mathcal N_1=\begin{pmatrix}M&A\\0&0\end{pmatrix},\qquad
 \mathcal N_2=\begin{pmatrix}0&0\\A&M\end{pmatrix}
 \tag{ST6}
\]
have exactly the actual character action in ST4. Their matrix convolution uses finite direct sums and tensor products. Entrywise multiplication gives actual distributivity/symmetry isomorphisms
\[
                  \mathcal N_i^2\simeq M\otimes\mathcal N_i.
 \tag{ST7}
\]
These are effective two-state models with the correct quadratic coefficient delta^3; they do not assert source-prescribed higher categorical relations or canonical simple labels.

If an arithmetic coefficient realization is desired for these inputs, the full-Tate symmetric functor of F61 sends a degree-e line to E(-e)[-2e] on Spec F_Q, where ell does not divide Q and E is a finite extension of Q_ell. All shifts are even, every summand is pure of complex weight zero, and the trace convention is v=Q^n. Apply it entrywise to ST6--ST7. Thus the input positivity is not merely a dimension count. This assertion does not require geometric half-Tate lines or a common spectral radius on total cohomology.

## 3. The actual whole tensor and its exact trace

Now apply the source restriction ST1 with k_l=k_r=3 to Mcheck^(3) tensor Mcheck^(3). Let d=m^2=D^3 and use the tensor basis of the two balanced bases. Its entire four-dimensional named action is
\[
 R_1=\begin{pmatrix}
 d&ma&ma&2a^2\\0&0&0&-ma\\0&0&0&-ma\\0&0&0&d
 \end{pmatrix},\qquad
 R_2=\begin{pmatrix}
 d&0&0&0\\-ma&0&0&0\\-ma&0&0&0\\2a^2&ma&ma&d
 \end{pmatrix}.
 \tag{ST8}
\]
Indeed each is N_i tensor N_i+(mI-N_i) tensor (mI-N_i), exactly ST1. In particular R_i squared=d R_i.

### Proposition ST-A

The actual unmarked two-word trace on this whole four-dimensional module is
\[
 \begin{split}
 T_6(v)&=\operatorname{Tr}(R_1R_2)=d^2+A_6^2,\\
 A_6&=2a^2-d=-D^3+18D^2-48D+32,
 \end{split}
 \tag{ST9}
\]
and
\[
\begin{split}
 T_6(v)={}&2(v^{12}+v^{-12})-12(v^{10}+v^{-10})
       +192(v^8+v^{-8})\\
       &+388(v^6+v^{-6})+1134(v^4+v^{-4})
       +1416(v^2+v^{-2})+1952.
\end{split}
 \tag{ST10}
\]

### Proof

The four diagonal entries of the full product ST8 are
\[
 m^4-2m^2a^2+4a^4,\quad -m^2a^2,\quad
            -m^2a^2,\quad m^4.
 \tag{ST11}
\]
Their sum is 2m^4-4m^2a^2+4a^4=m^4+(2a^2-m^2)^2, giving ST9. Expanding D=v^2+2+v^{-2} gives ST10. In particular its coefficients at v^{10} and v^{-10} are -12. The exact certificate retains all four diagonal checks, not just a numerical evaluation. QED.

For comparison with the source's simple parameter, delta^6 T_6(1/delta)=2(delta^3 T_3(1/delta))^2-delta^6=A_6 by the elementary double-angle identity. Proposition3.1, equations16--17, p9, gives the generic decomposition epsilon_plus plus epsilon_minus plus Xcheck^(6)(A_6^2). The direct full-product proof above does not require that decomposition or any simple projector.

Do not confuse the polynomial T_6(v) denoting the word trace here with the Chebyshev polynomial in T_6(1/delta). The former is explicitly defined by ST9; in the final fragment the word trace will be denoted tau_6 to remove this notational collision.

## 4. Strict effective iteration is impossible on these objects

### Corollary ST-B

No change of basis on this specified actual four-dimensional module makes both named generators matrices in N[v,v^{-1}]. More generally there is no strict effective finite graded-kernel realization with the stated composition and unmarked word-trace comparison on this whole module.

### Proof

Products of matrices with entries in N[v,v^{-1}] again have such entries, and their ordinary trace is a sum of diagonal entries. It would therefore have nonnegative Laurent coefficients. Trace is invariant under every simultaneous generic basis change, while ST10 has two negative coefficients. The same argument applies to actual graded kernels: tensor products and direct sums of finite graded spaces have effective characters, so the closed two-word trace object would be effective. QED.

This gives an exact operation obstruction. A proposed effective categorical iteration realizing the actual restriction Delta^(3,3), containing the individually effective source object Mcheck^(3), and preserving the named generator compositions and unmarked trace on its tensor square cannot exist with those premises. The two effective input models alone do not furnish that iteration. ST1 involves the complementary generators mI-N_i, which are virtual in the effective character cone; their two negative contributions in the full trace do not disappear after the actual restriction.

Unlike the simple-summand test of F63, ST-B does not require an effective projector inside the tested four-dimensional output. It is also different from F66: the corresponding k=2+2 whole tensor has the positive model constructed there, whereas this actual k=3+3 whole tensor already fails. This is a result for the iterated tensor-factor parameter, not the original all-strand-rank binary problem. A category omitting this source simple as an admissible input, or not comparing its actual tensor output, is not excluded.

## 5. Exact occurrence and the specialization boundary

The source proof of Theorem3.4 gives, by equations25--26 on p12, Mcheck^(2) as a constituent of Mcheck^(1) tensor Mcheck^(1), and Mcheck^(3) as a constituent of Mcheck^(1) tensor Mcheck^(2). Here Mcheck^(1) is the ordinary Specht module of shape (2,1), identified explicitly in that proof. Corollary3.5, p13, gives generic split semisimplicity. Therefore the tested Mcheck^(3) tensor Mcheck^(3) is an actual generic direct summand of the restriction of the sixfold ordinary Specht tensor (M_(2,1)) tensor-power6.

In ordinary degree-three Schur--Weyl theory, as used and explicitly checked in F21/F43, the Specht module (2,1) occurs for each ordinary factor V_i of dimension2. Consequently the tested module occurs generically inside (V_1 tensor ... tensor V_6) tensor-power3, of dimension2^18. The conclusion is about the selected four-dimensional tensor, not the trace of that entire ambient module: other summands can change its total Laurent coefficients.

The matrices ST4 are regular at v=1, but their chosen lattice must not be identified with an actual ambient tensor direct-summand lattice there. This can be checked explicitly. At v=1, m=a=8, and the normalized operators
\[
 G_1=2N_1/m-I=\begin{pmatrix}1&2\\0&-1\end{pmatrix},\qquad
 G_2=2N_2/m-I=\begin{pmatrix}-1&0\\2&1\end{pmatrix}
\]
satisfy G_i squared=I but
\[
                  (G_1G_2)^3=
                        \begin{pmatrix}7&6\\-6&-5\end{pmatrix}\ne I.
 \tag{ST12}
\]
In the ordinary ambient specialization, equation8 gives P_i^(3)=4(1+s_i tensor s_i tensor s_i), so the corresponding G_i are diagonal S_3 generators and their product has cube I. Thus the chosen two-state lattice's specialization does not factor through that ambient group image. In particular no regular basis change can identify it with an ambient specialized direct summand. The generic tensor occurrence and the Laurent-trace obstruction remain valid and need no such identification.

## 6. Pure point traces fail; mixed traces remain possible

Fix Q, ell and E as above. Under either v=Q^{n/2} or v=Q^n, ST10 cannot be the uninserted Euler trace of a bounded point complex of any one integral Deligne weight. In both conventions the distinct visible roots have even point weights. By BBD5.1.8, pp126--127, a pure weight-w complex can contain a root of point weight e only in cohomological degree e-w. All visible Euler multiplicities must therefore have the same sign. Finite power-sum uniqueness applies also to eventual equalities; the mixed signs of ST10 contradict it. Jordan blocks and hidden roots do not repair the argument, since a fixed root has one allowed pure cohomological degree.

This also excludes a genuine uninserted finite Weil trace or a single overall cohomological parity, without needing purity. An overall Tate or parity shift does not eliminate the mixed signs. Inserted-operator traces and bounded mixed complexes are different.

Indeed a concrete bounded mixed Tate witness exists under v=Q^{n/2}. Put all positive-coefficient Tate lines E(-e/2) from ST10 in degree0, and twelve copies each of E(-5) and E(5) in degree1. The positive part has dimension8216, the negative part24, and their Euler trace is exactly ST10 at every extension. Its Euler dimension is8192, matching T_6(1). This is a scalar mixed trace object, not a positive kernel realization, common pure object, or operation-compatible replacement for the actual tensor action.

## 7. Separate Grothendieck dictionary

The named tensor action is actual finite-dimensional module data over Q(v), related by the source inclusion (11). EGA I Theorem1.3.7 p86, Corollary1.3.8 p87 and Theorem1.4.1 pp90--92 provide the affine module dictionary. SGA3 I4.7.2--3 and cote90 scan17 supply action language; they do not turn the three-strand algebra into a Hopf algebra or supply a compatible effective categorical iteration.

Finite graded coefficient spaces have effective split-torus characters in N[v,v^{-1}]. SGA6 V Sections2--3 and cote133 scan18 give the effective/virtual representation language, with no lambda-ring assertion for the noncommutative generator algebra. The input coefficient kernels are effective, but the actual output's invariant trace exits that cone.

The bounded pure and mixed point complexes lie in SGA6 I Definition4.7 pp121--122 and Example4.8 p122. BBD5.1.5 and5.1.8 pp125--127 give the integral-weight and pure-complex convention. The pure-word comparison is an additional arithmetic requirement, not a published axiom of VIII. The explicit mixed Tate complex shows why a no-geometry conclusion would be false.

## 8. Check record

The exact certificate verify_iterated_six_factor_tensor.py checks both source coproduct matrices, their quadratics, all four diagonal entries of the two-word product, the positive input characters, the generic irreducibility factor, the full Laurent trace including both negative coefficients, the two Tate multiplicity totals, and the specialization calculation ST12. The source normalization, occurrence, positive-kernel implication and point-purity argument were read/proved by hand. No formal proof-assistant verification or complete search over other modules is claimed.

All previous frozen reports remain unchanged. Fresh independent whole-proof/source review is requested before the generated fragment is integrated.
