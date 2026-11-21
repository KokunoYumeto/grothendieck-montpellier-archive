# Explicit regularity and an effective detector from the CM construction

Author/checker: GPT-6 Astra Pro, inherited effort not exposed, HODGE_DIVISION /root/sixfolds. Date: 2026-11-21.

This note develops a positive-rank variant of D-SR-01--05. The regularity argument was suggested by the supplied HECKE_DIV M7 calculation, but that statement, Markman's output-sheaf theorem, and Markman's generic-position hypotheses are not premises. All geometry and regularity needed here are proved below. The deformation step uses the authorized DEG_L S-14 input, specifically Perry arXiv:2604.00511v2, Theorem 1.2 and its proof. Perry remains a preprint in the source-status convention of this project.

The finite construction below is explicit but has not been executed for its astronomical torsion order. Its termination follows from the displayed counting inequalities. Numerical certificates in the accompanying script concern the symbolic character, matrices, regularity inequalities, and final integer formula, not an enumeration of the torsion group.

## SF-QC01. A strengthened torsion orbit

Let C be the Fermat plane quartic, J=J(C), and Θ its principal polarization. Let E_i be the Gaussian CM elliptic curve. The three elliptic quotient maps give an isogeny j:E_i^3→J with j*Θ=2θ_product and degree eight, as proved in D-SR-04. Fix a positive squarefree integer m. Put

\[
 P=2^{2048+\lceil\log_2(m+1)\rceil},\quad
 L=\operatorname{lcm}(1,\ldots,P),\quad
 N=4mL^2+1,\quad d=N-1=4mL^2.
\]

For the nine class-number-one radicands m≤163 one can instead use the common P=2^2048, as checked in D-SR-01. Every prime divisor of N exceeds P. In particular N is odd, and j induces an isomorphism E_i^3[N]→J[N]. There exists a cyclic subgroup H⊂J[N] of order N satisfying both:

1. The translates C+h, h∈H, are pairwise disjoint.
2. For every P₀∈Pic⁰(J),
   \[
   H^0(J,I_{Z_H}(2\Theta)\otimes P_0)=0,
   \qquad Z_H=\coprod_{h\in H}(C+h).
   \tag{QC1.1}
   \]

**Proof.** Sample uniformly from exact-order-N vectors v′∈E_i^3[N], and let v=j(v′). D-SR-01 proves that failure of the first condition has probability less than 216/499. Its proof uses the bound #(C−C)∩J[q]≤108q⁴, the lower bound J₆(q)>q⁶/2 for exact-order-q points, and Σ_{p|N}1/p<1/500. These estimates apply unchanged to the present m-dependent P.

Identify NS(E_i³) with integral Hermitian three-by-three Gaussian matrices using the product principal polarization. Consider all nonzero such matrices M with 0≤M≤4I. There are at most

\[
 B=5^3\,81^3=66\,430\,125
\]

matrices: each diagonal entry is one of 0,1,2,3,4; each off-diagonal Gaussian entry has real and imaginary parts between −4 and 4. Positive semidefiniteness actually gives its norm at most 16, so every nonzero entry is a unit modulo N, because all prime divisors of N exceed 16. A row containing such an entry defines a surjective map (Z[i]/N)^3→Z[i]/N. Consequently ker(M) contains at most N⁴ points of E_i³[N], and the probability that an exact-order-N v′ lies in it is less than 2/N². The probability of lying in any of these kernels is therefore at most 2B/N²<1/4. The combined failure probability is below 216/499+1/4<1. Choose v′ outside both bad sets, and set H=⟨j(v′)⟩.

Suppose that (QC1.1) fails. Then an effective divisor D numerically equivalent to 2Θ contains every curve C+h. Write its distinct irreducible components as D₁,…,D_k. Since Θ²D=12 and Θ²D_i is a positive integer, k≤12. For every h∈H, both D and D+h contain all the N curves. If these divisors had no common component, their proper intersection would be an effective curve of Θ-degree 24. Each curve C+h has Θ-degree three, so 3N≤24, a contradiction. Thus every h belongs to at least one set

\[
 S_{ij}=\{h\in H:D_i+h=D_j\}.
\]

Each nonempty S_ij is a coset of H∩Stab(D_i). If all these subgroups were proper, each coset would have at most N/p_min points, where p_min>P is the smallest prime divisor of N. The at most k²≤144 cosets could not cover H. Therefore some D_i is H-stable.

Effective divisors on an abelian variety are nef: for a curve, translate the divisor to meet it properly and compute the nonnegative intersection. Hence D_i and 2Θ−D_i are nef. The matrix M corresponding to j*D_i is a nonzero integral Gaussian Hermitian matrix with 0≤M≤4I. Since D_i is invariant under v=j(v′), its polarization homomorphism kills v. Pullback gives Mv′=0, contrary to the choice of v′. This proves (QC1.1).

The construction is finite: enumerate exact-order-N torsion vectors, test avoidance of C−C and the finite displayed matrix kernels, and take the first successful vector. No test over the continuum Pic⁰(J) is needed, because the divisor argument proves its vanishing consequence uniformly.

## SF-QC02. The coherent output and its complete character

Let A=J_x×Ĵ_α, identify Ĵ with J by Θ when writing matrices, and put

\[
 x=\Theta_x,\qquad y=\Theta_\alpha,\qquad
 \gamma=c_1(\mathcal P_{x,\alpha}),\qquad
 H_d=dx+y,\qquad H_b=3(x+y),\qquad h=3H_d.
\]

Both H_b and h are very ample: the third power of an ample line bundle on an abelian variety is very ample. Let Y=J_y×A and π:Y→A. Write a(y,x)=y+x. On Y set

\[
 \mathcal L=\mathcal O(\Theta_y)\otimes a^*\mathcal O(\Theta)
                       \otimes\mathcal P_{y,\alpha}^{-1},
 \qquad D_1=\{y\in Z_H\},\quad D_2=\{y+x\in-Z_H\}.
\]

Define

\[
 \mathcal M=\mathcal L\otimes I_{D_1}I_{D_2},\qquad
 \mathcal G=R\pi_*\mathcal M,\qquad
 E=\mathcal G^\vee[-1].
 \tag{QC2.1}
\]

Then E is a coherent sheaf of rank r=8d, locally of projective dimension at most one. It is strongly equivariantly semiregular for a coherent action of a finite subgroup of A[N]×Â[N].

To prove the sheaf assertion, the change of variables (y,x)↦(y,z=y+x) makes D₁,D₂ pullbacks from independent factors. Their ideals are Tor-independent and their intersection equals their product. There is therefore an exact sequence on the total space

\[
 0\longrightarrow\mathcal M\longrightarrow\mathcal L
 \longrightarrow\mathcal L|_{D_1}\oplus\mathcal L|_{D_2}
 \longrightarrow\mathcal L|_T\longrightarrow0,
 \quad T=D_1\cap D_2.
 \tag{QC2.2}
\]

There are N² disjoint components of T, each isomorphic to C×C×Ĵ. Its map f:T→A is finite: after translations and signs, its first-factor map is the addition C×C→C^(2)≅Θ⊂J. For a nonhyperelliptic genus-three curve the Abel map C^(2)→Θ is an embedding, since an effective divisor of degree two has a unique section, and the differential criterion gives an immersion. The quotient C×C→C^(2) is finite flat of degree two. Thus Θ is smooth and each component of f factors as a finite flat degree-two cover of a smooth divisor in A.

Set

\[
 W=\pi_*\mathcal L,\quad
 U=\pi_*(\mathcal L|_{D_1}\oplus\mathcal L|_{D_2}),\quad
 \mathcal T=f_*(\mathcal L|_T).
\]

On every π-fibre, L has class 2Θ and no higher cohomology; W is locally free of rank eight. Each curve restriction has degree six, and genus three implies H¹=0 and h⁰=4. Hence U is locally free of rank 8N. Since f is finite, T has no higher direct image. Sequence (QC2.2) represents G by [W→U→T] in degrees 0,1,2. By (QC1.1), W→U is fibrewise injective, so Q=U/W is a vector bundle of rank 8N−8=r and G=[Q→T] in degrees 1,2.

Each summand of T is the pushforward of a vector bundle on a smooth divisor; hence it has local projective dimension one and only its first sheaf Ext into O_A is nonzero. Finite duality identifies

\[
 \mathcal T^D:=\mathcal E xt_A^1(\mathcal T,\mathcal O_A)
 =\bigoplus_{i,j} f_{ij,*}
       ((\mathcal L|_{T_{ij}})^{-1}\otimes\omega_{T_{ij}}).
\]

Dualizing [Q→T] gives a coherent sheaf E and an exact sequence

\[
 0\longrightarrow Q^*\longrightarrow E\longrightarrow\mathcal T^D
 \longrightarrow0.
 \tag{QC2.3}
\]

This also proves pd(E)≤1. No statement about a codimension-four nonfree locus is used.

For semiregularity, let q:J→Z=J/H and F=I_{q(C)}. D-SR-02 proves injectivity of the trace in degrees zero, one and two for F and its transforms by inversion. Thus F⊠(−1)*F is fully semiregular by the three Hochschild Künneth summands. Pullback under q×q gives I_ZH⊠I_−ZH with its honest H×H descent action. Its invariant Ext² is the original Ext², and trace pullback is injective. Tensor by O(Θ)⊠O(Θ), make the linear change of variables, apply Fourier–Mukai on one factor, and finally derived-dual and shift as in (QC2.1). These equivalences or anti-equivalences preserve trace injectivity and transport the whole coherent action. Translation and degree-zero tensor functors are taken to functors of the same kind under these operations. Their action on isomorphism classes is an automorphism of the abelian variety of such functors, so the resulting group remains an injective finite subgroup of A×Â of exponent N. Coherence is transported from the honest original descent action, not inferred from invariance of a K-class. Since the output is a coherent sheaf, its ordinary negative self-Ext groups vanish.

Here is the full character, independently calculated by exterior integration. Put u²=−d, a=(1+1/u)/2 and b=(1−1/u)/2. Then

\[
 \operatorname{ch}(I_{Z_H}(\Theta))
 =1+\Theta-\frac d2\Theta^2-\frac d6\Theta^3
 =a e^{u\Theta}+b e^{-u\Theta}.
\]

In Darboux coordinates define

\[
 Q_u=\prod_{j=1}^3(u a_j-U_j)(u b_j-V_j),\qquad
 t=-ab(Q_u+Q_{-u}).
\]

With the sign convention of (QC2.1),

\[
 e^{\gamma/2}\operatorname{ch}(E)=t+P_d(H_d),
 \tag{QC2.4}
\]

where

\[
 P_d(z)=8d+2(d-1)z-z^2-\frac{d-1}{12d}z^3
     +\frac1{48d}z^4+\frac{d-1}{960d^2}z^5
     -\frac1{5760d^2}z^6.
 \tag{QC2.5}
\]

For completeness, in one symplectic plane, integrating the middle coordinates c,e gives

\[
 \int_{c,e}\exp(s(a+c)(b+e)+tce-cV+eU)
  =(s+t)+st\,ab+s(aV-bU)-UV-s\,abUV.
\]

For opposite roots s=−t this is −e^{γ_j/2}(sa−U)(sb−V), producing the two Weil determinant terms. For equal roots s=t it equals

\[
 2s\exp\left(\frac{\gamma_j}{2}+\frac{s}{2d}(d a b+UV)\right).
\]

Multiplying the three planes, then dualizing and multiplying by −1 for the shift, gives the unequal-root term −ab(Q_u+Q_−u) and the equal-root polynomial

\[
 -8u^3\left(a^2e^{-uH_d/(2d)}-b^2e^{uH_d/(2d)}\right).
\]

Expanding through degree six proves (QC2.5). There is no additional volume factor because Θ on J is principal.

The Weil operator on H₁(J)⊕H₁(J) is

\[
 J_K=\begin{pmatrix}0&-1\\d&0\end{pmatrix},\qquad J_K^2=-d.
\]

Its two eigenspaces on H¹ have generators ua_j−U_j, ub_j−V_j and their conjugates, each of Hodge signature (3,3). It is Rosati-skew for the polarization matrix diag(d,1); that product is [[0,−d],[d,0]]. If L₀⊂H₁(J,Q) is a rational symplectic Lagrangian, L₀⊕L₀ is J_K-stable and totally isotropic for the associated K-Hermitian form. Thus the Hermitian space is split with determinant class [−1]. The two determinant terms Q_u,Q_−u are independent and ab=N/(4d) is nonzero. Therefore t is a nonzero rational primitive Weil class. In particular H_dt=0.

Writing

\[
 a_d=\frac{d-1}{4d},\qquad
 D=\det E,\qquad c_1(D)=2(d-1)H_d-4d\gamma,
\]

the normalized entire character is

\[
 \kappa(E):=e^{-c_1(E)/r}\operatorname{ch}(E)
 =t+e^{-a_dH_d}P_d(H_d).
 \tag{QC2.6}
\]

All terms other than t are polarization powers. The coefficients c_k of e^(−a_dz)P_d(z), through degree six, are

\[
\begin{array}{c|l}
0&8d\\
1&0\\
2&-(d+1)^2/(4d)\\
3&(d-1)(d+1)^2/(24d^2)\\
4&-(d-3)(d+1)^2(3d-1)/(768d^3)\\
5&(d-1)(d+1)^2(d^2-6d+1)/(3840d^4)\\
6&-(d+1)^2(d^2-10d+5)(5d^2-10d+1)/(368640d^5).
\end{array}
\tag{QC2.7}
\]

## SF-QC03. A complete explicit regularity proof

The sheaf E is 112-regular with respect to H_b. More strongly, for any integer s≥1 and any line bundle M on A satisfying

\[
 c_1(M)-112s^2H_b\quad\hbox{is nef},
 \tag{QC3.1}
\]

one has H^i(A,[s]*E⊗M)=0 for all i>0. Arbitrary flat factors of M are allowed.

The regularity convention is H^i(A,F((q−i)H_b))=0 for every i>0. The standard Castelnuovo–Mumford lemma is applied to the pushforward under the embedding defined by H_b: a zero-regular sheaf is globally generated, remains regular under nonnegative twists, and its section multiplication maps are surjective. An inspected published locator is Pareschi–Popa, M-regularity and the Fourier–Mukai transform, Theorem 1.2 (author version p.2); the publisher version is Pure Appl. Math. Q.4(3),587–611 (2008). The relevant Buchsbaum–Rim terms are in Raicu–Sam, Compositio158(2022), pp.41–42; their exactness in the locally split case used here is also proved below.

**Step 1: the dual bundles.** For every integer q≥1,

\[
 H^i(A,W^*(qH_b))=H^i(A,U^*(qH_b))=0\quad(i>0).
 \tag{QC3.2}
\]

For W, relative duality identifies W* with R³π_*L^−1. Leray and Serre duality on the ninefold Y identify the dual of H^i(A,W*(qH_b)) with H^(6−i)(Y,L(−qH_b)). Project Y onto J_y. On an A-fibre the line bundle has matrix diag(1−3q,−3q), hence is antiample. Its cohomology is concentrated in degree six, so total cohomology below six vanishes.

For a summand of U supported on C×A, relative duality first introduces the relative canonical bundle; Serre duality on the sevenfold cancels it and again gives H^(6−i)(C×A,L_C(−qH_b)). Project onto C. The first curve type has the same fibre matrix. For the second type use z=y+x as the fixed curve coordinate; its matrix is

\[
 \begin{pmatrix}1-3q&1\\1&-3q\end{pmatrix}.
\]

The largest eigenvalue of the matrix before subtracting 3qI is (1+√5)/2<3, proving antiampleness for q≥1. Flat twists and translations do not change this calculation. Thus W*,U* are 7-regular.

**Step 2: a kernel estimate.** Let e=h⁰(U*(7H_b)). Evaluation gives

\[
 0\to K_U\to O_A(-7H_b)^e\to U^*\to0.
\]

The kernel is a vector bundle and is 14-regular. For i=2,…,6, twist by (14−i)H_b and use (QC3.2) and the positivity of (7−i)H_b. For i=1, section multiplication from 7-regularity gives surjectivity at twist 13H_b; the multiplication by degree-six ambient polynomials factors through H⁰(A,6H_b), which is enough for this evaluation map.

Compose evaluation with U*→W*, and let J₀ be the resulting kernel. There is an exact sequence

\[
 0\to K_U\to J_0\to Q^*\to0.
 \tag{QC3.3}
\]

The Buchsbaum–Rim complex resolving J₀ has terms, beginning with a surjection C₁→J₀,

\[
 C_k=\bigwedge^{8+k}(O_A(-7H_b)^e)
       \otimes\operatorname{Sym}^{k-1}W\otimes\det W,
 \qquad 1\le k\le e-8.
 \tag{QC3.4}
\]

Its determinant factor is required globally. To verify exactness in this case, locally split the surjection as K⊕V→V, with dim V=8. Splitting each wedge by the number a of factors from K identifies the residual strands, after the determinant pairing, with the polynomial de Rham complex of total degree a−1 on V*. For a≥2 the Euler contraction divides by the nonzero integer a−1 and gives a contracting homotopy. The a=1 strand maps isomorphically to K, and the remaining V maps isomorphically to the target. This proves the needed local exactness in characteristic zero.

The theorem of the square gives W=O_A(Θ_x)⊗b*FM(O_J(2Θ)), where b(x,α)=x−α. Pulling the Poincaré family back by the polarization isogeny [2] identifies it with a*O(2Θ)⊗p₂*O(−2Θ). Taking direct image gives H⁰(O(2Θ))⊗O(−2Θ). Consequently

\[
 [2]^*W\simeq Q_0^{\oplus8},\qquad
 c_1(Q_0)=4\Theta_x-2\Theta_{x-\alpha}.
 \tag{QC3.5}
\]

A different symmetric normalization adds a flat factor and affects no vanishing assertion. The matrix of Q₀ is [[2,2],[2,−2]], with eigenvalues ±2√2, while [2]*H_b has matrix 12I. Thus q[2]*H_b+(k+7)c₁(Q₀) is ample for q≥k+7. Kodaira vanishing on A, and trace splitting for the finite étale map [2], prove

\[
 \operatorname{reg}_{H_b}(\operatorname{Sym}^{k-1}W\otimes\det W)
 \le k+13.
\]

Hence reg C_k≤7(8+k)+k+13=69+8k. Only the first six terms of (QC3.4) are needed. Successive cohomology sequences show the vanishings required for R-regularity of J₀ whenever

\[
 R\ge\max_{1\le k\le6}(\operatorname{reg} C_k-k+1)
 \le\max_{1\le k\le6}(70+7k)=112.
\]

The final possible cohomology is in degree seven and vanishes on the sixfold. Sequence (QC3.3), together with 14-regularity of K_U, gives 112-regularity of Q*. This bound is independent of the number N of curves and of the number e of evaluation sections.

**Step 3: the torsion dual.** On one component C×C×Ĵ, put F₁={p}×C, F₂=C×{p}, S=F₁+F₂, and let Δ_C be the diagonal. The sum map C×C→J pulls Θ back to

\[
 A_C=4S-\Delta_C.
\]

Indeed Θ|C has degree three and its mixed Poincaré class is S−Δ_C. Restriction to the diagonal gives degree twelve, agreeing with [2]*Θ|C.

The divisor R_C=3S−Δ_C is nef. Projection of the plane quartic from a point of C gives a degree-three morphism to P¹. The residual to the diagonal in its fibre correspondence is effective of class R_C. If its monodromy is S₃, this residual divisor is irreducible, and its self-intersection is 18−12−4=2. An effective irreducible divisor of nonnegative square on a smooth surface is nef. If the transitive monodromy is A₃, the cover is cyclic, and the residual divisor is the sum of the two nonidentity automorphism graphs. Each graph has square −4. Riemann–Hurwitz gives five fixed points; the two graphs meet transversely there because the two nontrivial eigenvalues of the order-three local action differ. Their sum has intersection one with each graph and nonnegative intersection with any other irreducible curve. It is again nef.

Numerically on this component,

\[
 c_1(\mathcal L_T)=3F_1+3F_2-\mathcal P_{c_1,\alpha},\qquad
 f^*H_b=3A_C+3\Theta_\alpha.
\]

For q≥3 decompose

\[
\begin{split}
 qf^*H_b-c_1(\mathcal L_T)
 ={}&[3qA_C-6F_1-3F_2]+(3q-1)\Theta_\alpha\\
 &+[3F_1+\Theta_\alpha+\mathcal P_{c_1,\alpha}].
\end{split}
\]

The last bracket is a pullback of Θ, hence nef. The first is 3qR_C+(3q−6)F₁+(3q−3)F₂, ample on C×C. Together with the strictly positive theta class on Ĵ it is ample on the product. Thus the entire class is ample. Kodaira vanishing on the smooth fivefold gives H^i(T,ω_T⊗L_T^−1⊗f*O(qH_b))=0 for i>0,q≥3. Therefore T^D is 8-regular. Extension (QC2.3) proves the asserted 112-regularity of E.

**Step 4: the stronger bound (QC3.1).** Pull all exact complexes back by [s] and tensor with M. In Step 1 the two output fibre matrices are multiplied by s²; subtracting c₁(M) makes them negative definite under (QC3.1). Thus [s]*U*⊗M and [s]*W*⊗M have no higher cohomology. In the pulled-back evaluation sequence the middle term is a sum of ample line bundles M(−7s²H_b), so H^j([s]*K_U⊗M)=0 for j≥2. No claim about H¹ of this kernel is needed.

For k≤6 pull [s]*C_k⊗M back once more by [2]. Its summands have class

\[
 [2]^*c_1(M)-7s^2(8+k)[2]^*H_b+s^2(k+7)c_1(Q_0).
\]

After removing a nef class the matrix is s² times

\[
 12[112-7(8+k)]I+(k+7)\begin{pmatrix}2&2\\2&-2\end{pmatrix}.
\]

Its least eigenvalue is positive for 1≤k≤6; the worst displayed lower bound is 168−26√2>0. Kodaira vanishing, trace splitting, the six-term truncation and (QC3.3) give the required vanishings for [s]*Q*⊗M.

For T^D, form the finite étale base change T′=T×_{A,[s]}A with g:T′→T and f′:T′→A. The relevant line class is

\[
 f'^*c_1(M)-g^*c_1(\mathcal L_T)
 =g^*(3f^*H_b-c_1(\mathcal L_T))
       +f'^*(c_1(M)-3s^2H_b).
\]

The first summand is ample by Step 3 and the second is nef. Kodaira vanishing on T′, finite base change, and (QC2.3) prove (QC3.1) for E.

## SF-QC04. Ordinary normalization and coherent equivariance

Let r=8d and define the coherent sheaf

\[
 B_0=[r]^*E\otimes D^{-r},\qquad D=\det E.
 \tag{QC4.1}
\]

It has rank r, projective dimension at most one, c₁(B₀)=0, and complete character

\[
 \operatorname{ch}(B_0)=[r]^*\kappa(E)
       =r^6t+\sum_{k=0}^6 r^{2k}c_k H_d^k.
 \tag{QC4.2}
\]

Here r⁶ is the degree-six cohomological scaling, not the isogeny degree. Since gcd(r,N)=1, this normalization preserves a strong equivariant semiregularity structure for an actual finite subgroup of A×Â, as follows.

Write the original group action as T_g=t_{a_g}*⊗P_g, with a_g∈A[N], P_g∈Â[N], and all associativity constraints transported from descent. Let a′_g be the unique N-torsion point with r a′_g=a_g. Define T′_g=t_{a′_g}*⊗[r]*P_g. Its coherent composition maps are the pullbacks of those for T_g, since t_{a′_g}*[r]*=[r]*t_{a_g}*. The deck group A[r] acts on [r]*E in the canonical way; each pulled-back P_g has a canonical deck linearization. Thus these actions commute coherently and give an action of A[r]×G. The map to A×Â is

\[
 (b,g)\longmapsto(b+a'_g,\,[r]^*P_g).
\]

It is injective: the first summands have coprime r- and N-torsion orders, and multiplication by r is injective on N-torsion in the dual. There is no invisible central kernel. Descent for the deck group identifies the invariant Ext² with Ext²(E,E), and then taking G-invariants gives the original semiregular invariant space. Trace pullback is injective under the isogeny. Tensor by D^−r conjugates this honest action by an autoequivalence, hence preserves coherence and injectivity of its underlying subgroup. This proves strong, and therefore weak, equivariant semiregularity of B₀. Ordinary negative Ext vanishes because B₀ is a coherent sheaf.

The full character (QC4.2) stays Hodge on the split Weil period family with polarization h=3H_d. On a suitable finite level cover the rational Weil plane is constant, and r⁶t extends as a flat Hodge class. Apply Perry Theorem 1.2 with B-field zero. Its proof gives an ordinary perfect deformation, not merely a twisted one: in §6.2 choose b₀=0,n=1 and the zero gerbe class. Corollary 5.17 may replace its band by μ_q, but pushing out the zero class keeps the Brauer class zero. Theorem 6.3 returns the object in the ambient category Perf(A_U,0). Any gerbe on an auxiliary quotient used to geometrize the invariant category does not change this ambient conclusion.

After shrinking the étale neighbourhood, the ordinary perfect deformation is a flat coherent sheaf B and has fibrewise projective dimension at most one. Here are precise algebraic details of the openness step. At every point of the special fibre the derived residue-field complex has amplitude in [−1,0], because B₀ has projective dimension at most one. Openness of the Betti-number vanishings for a perfect complex (Stacks Lemma36.31.1, Tag0BDI) therefore gives a two-term vector-bundle presentation in degrees −1,0 on a neighbourhood of that point. On the special fibre its differential is injective as a map of sheaves, since B₀ is a sheaf. The local criterion in Stacks Lemma10.99.1, Tag00ME, applied to the local rings of the base and total space, proves that the differential is injective near this point and that its cokernel is flat over the base there. Openness of the flat locus (Theorem37.15.1, Tag0399, citing EGAIV₃11.3.1) extends this to an open neighbourhood of the entire special fibre. Properness permits shrinking the base so that every point of the new total space lies in this neighbourhood. The two-term presentation gives pd≤1 on every fibre, and the cokernel gives the desired ordinary flat coherent family. No global boundedness of all sheaves with this Chern character is asserted.

Put

\[
 R=224r^2+r(d+2)+6=14344d^2+16d+6.
 \tag{QC4.3}
\]

Then B₀ is R-regular with respect to h. Indeed 2h−H_b=3((2d−1)x+y) is ample. The matrix of (d+2)h−c₁(D) is

\[
 \begin{pmatrix}d(d+8)&4d\\4d&d+8\end{pmatrix},
\]

whose determinant is d((d+8)²−16d)=d(d²+64)>0. For i=1,…,6, the line bundle M_i=D^−r⊗h^(R−i) satisfies

\[
 c_1(M_i)-112r^2H_b
 =112r^2(2h-H_b)+r((d+2)h-c_1(D))+(6-i)h,
\]

which is ample. SF-QC03 supplies all six vanishings. Upper semicontinuity in the ordinary flat coherent family preserves them after shrinking. Thus every B_s on this open is R-regular, of rank r, c₁=0 and pd≤1, with the same full character.

## SF-QC05. A numerical effective detector

Define the explicit integers

\[
 \begin{split}
 r&=8d,\qquad R=14344d^2+16d+6,\\
 V&=\int_A h^6=524880d^3,\\
 M&=729d^3r(R+r^2)^6,\\
 A_2&=\frac{1024}{9}d^3(d+1)^2.
 \end{split}
 \tag{QC5.1}
\]

A₂ is an integer because d=4mL² is divisible by nine. Set

\[
 D_{\rm CM}(m)=V\left((r+2)R A_2
       +7M\binom{r+1}{2}R^2+343\binom M3\right).
 \tag{QC5.2}
\]

This is a numerical formula involving only m, powers, binomial coefficients and the explicit finite lcm defining L. On the entire fixed split Weil family containing (A,h,K), there is an effective integral three-cycle with nonzero Weil projection and h-degree at most D_CM(m), using the authorized detector closedness input to pass from the open obtained above to its component. No Chow denominator occurs in the detecting cycle.

In particular the simpler safe integer

\[
 \boxed{D_{\rm CM}(m)\le 2^{318}d^{51}
                  =2^{420}m^{51}L^{102}}
 \tag{QC5.2a}
\]

may be used instead. Indeed r+2≤2⁴d, R<2¹⁴d², A₂<2⁹d⁵, V<2²⁰d³ and binom(r+1,2)≤2⁶d². Also R+r²≤14430d²<2¹⁴d², so M<2⁹⁷d¹⁶. The three summands in (QC5.2) are respectively bounded by 2⁴⁷d¹¹, 2¹⁵⁴d²⁵, and 2³¹⁷d⁵¹; for the last use 343 binom(M,3)<64M³. Since d≥1, their sum is below 2³¹⁸d⁵¹.

**Proof.** On the deformation open, F_s=B_s(Rh) is zero-regular and globally generated. Its higher cohomology vanishes and v=h⁰(F_s)=χ(F_s) is constant. The evaluation sequence

\[
 0\to K_s\to O_{A_s}^{v}\to F_s\to0
\]

has a vector-bundle kernel because pd(F_s)≤1. Put k=v−r. The same section multiplication argument used above shows that K_s is 7-regular: for cohomological degrees at least two use the positivity of (7−i)h and zero-regularity of F_s, and in degree one use surjectivity of H⁰(F_s)⊗H⁰(O(6h))→H⁰(F_s(6h)). Hence G_s=K_s(7h) is a globally generated vector bundle.

Let

\[
 A_3=\frac{65536}{81}d^4(d-1)(d+1)^2.
\]

From (QC2.7) and c₁(B_s)=0,

\[
 c_2(B_s)=A_2h^2,\qquad
 c_3(B_s)=A_3h^3+2r^6t_s.
 \tag{QC5.3}
\]

The sign and all coefficients here follow from ch₂=−c₂ and ch₃=c₃/2 when c₁=0. Inverting c(F_s) in the evaluation sequence and then twisting by 7h gives

\[
\begin{split}
 c_3(G_s)= {}&-2r^6t_s+ S_kh^3,\\
 S_k={}&-A_3+(r+2)R A_2-\binom{r+2}{3}R^3\\
 &+7(k-2)\left(\binom{r+1}{2}R^2-A_2\right)
   -49rR\binom{k-1}{2}+343\binom k3.
\end{split}
\tag{QC5.4}
\]

Thus c₃(G_s) has nonzero Weil projection. In particular k≥3. Choose k−2 general global sections of G_s. Their first rank-drop locus has expected codimension three, or is empty, because the bundle is globally generated and the universal evaluation is transverse to the matrix-rank strata. The Thom–Porteous formula gives its class c₃(G_s). Nonzero Weil projection excludes the empty case. It is therefore an integral effective detecting cycle.

It remains to bound k. Write c_j for (QC2.7). Since H_dt=0 and td(A)=1, Riemann–Roch gives

\[
 v=V\sum_{j=0}^6\frac{r^{2j}c_j}{3^j}
                      \frac{R^{6-j}}{(6-j)!}.
\]

For d≥1 each coefficient of P_d has absolute value at most r/j!. Since 0≤a_d<1/4, multiplying by exp(−a_dz) gives |c_j|≤r(5/4)^j/j!. Consequently

\[
 v\le\frac{Vr}{6!}(R+5r^2/12)^6
    \le729d^3r(R+r^2)^6=M.
\]

Thus 3≤k≤M. Since d>1, both A₂,A₃ are positive. Discarding the negative terms in (QC5.4) and replacing k by M in the remaining positive terms gives S_k≤(r+2)RA₂+7M binom(r+1,2)R²+343 binom(M,3). Finally h³t_s=0, so the degree is VS_k≤D_CM(m), proving (QC5.2).

The source polarization is specified: h=3(dx+y) has type (3,3,3,3d,3d,3d), product 729d³. This result must not be described as a principal-polarization bound without an additional lattice/isogeny calculation. For any fixed target split polarized K-lattice, a chosen rational polarization isometry whose denominators are cleared by q gives a fixed isogeny with pullback target polarization q²h; pushforward transports the detector bound with cost q⁶. A numerical bound uniform over all target polarization products requires bounding that q, separately.

For class normalization, the exterior pairing gives ∫t²=−8dN²: each symplectic plane contributes Q_uQ_−u=−4d times its oriented volume, and 2(ab)²=2N²/(16d²). Therefore, for t_B=r⁶t,

\[
 -\int t_B^2=8dN^2r^{12}=2^{39}d^{13}N^2.
\]

Moreover A₃ is an integer for the chosen d, since 9 divides d. Formula (QC5.3) then expresses 2t_B as the difference of integral algebraic cycle classes. Thus the lattice denominator δ=2 is valid for this explicit flat Weil class. This does not assert that an arbitrary rational Weil vector has denominator two.

## Source and status notes

- The finite torsion avoidance and the denominator-free effective Chern construction are new arguments in this run. The proof does not invoke an unverified generic-rank or generic-position statement.
- Pareschi–Popa, M-regularity and the Fourier–Mukai transform, Pure Appl. Math. Q.4(3),587–611 (2008), Theorem1.2; exact basic regularity statement inspected in the author PDF p.2. Publisher DOI10.4310/PAMQ.2008.v4.n3.a1.
- Raicu–Sam, Bi-graded Koszul modules, K3 carpets, and Green's conjecture, Compositio158(2022),33–56, pp.41–42 immediately before Theorem3.2. The globally correct Buchsbaum–Rim determinant factor was inspected in the published PDF, and the locally split exactness is proved here.
- Bauer–Szemberg, On tensor products of ample line bundles on abelian varieties, Math.Z.223(1996),79–85, Theorem1.1(a),(b), author version p.1. The proof and publication header were inspected.
- Fulton, Intersection Theory, second edition (1998), Theorem14.4, pp.254–255. The Thom–Porteous statement used here was checked against the publisher's chapter abstract and the indexed primary book text; a full independent audit of the entire chapter proof is not claimed.
- Mukai1981, Theorem2.2 and equation3.1, and Buchweitz–Flenner2003 Proposition4.2, remain the published Fourier–Mukai and trace inputs already checked in D-SR-01--04.
- Perry2604.00511v2 remains an authorized preprint input. The zero-B ordinary conclusion is an inference from the full proofs of Corollary5.17, Theorems6.1/6.3 and Theorem1.2 in §6.2, not an extra theorem quoted without checking.
- Exact Perry page locators for this inference: Corollary5.17 pp.20--21; Theorems6.1/6.3 pp.25--26; §6.2 and the proof of Theorem1.2 pp.26--28. All were inspected in the official versioned PDF.
- Stacks Project Tags0BDI,00ME,0399 and07VK were opened and checked for, respectively, openness of perfect-complex Betti vanishings, the injectivity/flat-cokernel criterion, openness of the flat locus, and perfect cohomology with arbitrary base change. The last two provide the precise family hypotheses used for upper semicontinuity.
- All regularity constants used for the numerical estimate have been proved above. HECKE_DIV M7 is provenance for the architecture of that argument, not a premise, and Markman's output sheaf and general-position assertions are unnecessary here.
