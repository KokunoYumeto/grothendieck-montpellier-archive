# Candidate T6.26: a fixed source cannot hide core growth in its theta coefficients

Status: candidate awaiting whole-proof review. Date 2026-11-21. Actor: GPT-6 Astra Pro; effort not exposed; /root/rallis_t6. The reduced-image and explicit Rallis-energy consequences below concern a fixed smooth surface and simple abelian fourfold targets. They are not asserted for the product target of every 032 switch.

## Proposed theorem T6.26

Use the fixed maximal \(\mathcal O_K\) target action and notation of T6.25, and set
\[
 c_A=\frac{2^n n!\sqrt V\,\Delta^{(n-1)/2}}{R}.
 \tag{T26.1}
\]

### A. A bounded source order gives the same obstruction

In T6.25, replace integral maximal \(\mathcal O_E\)-action on every source \(B_\ell\) by a rational \(E\)-action and the uniform condition
\[
 b\mathcal O_E H_1(B_\ell,\mathbf Z)
                 \subseteq H_1(B_\ell,\mathbf Z)
 \tag{T26.2}
\]
for one fixed positive integer \(b\). The maps remain \(E\)-linear. For any integral signed target cycle \(\Gamma\) in their proper-push class span,
\[
 b^g P_A[\Gamma]\in\overline{\mathfrak j}\mathscr W_A.
 \tag{T26.3}
\]
If its Weil projection is nonzero, then
\[
 D_{\rm abs}(\Gamma)\ge\frac{c_A}{b^g}\sqrt J.
 \tag{T26.4}
\]
For reduced-image combinations with all generic degrees at most \(S\), the same assertion holds with an additional factor \(L_S\) in the denominator. Thus allowing a fixed nonmaximal source order does not remove the construction-specific growth.

### B. Uniformity for every map from one fixed source

Fix a simple complex CM abelian variety \(A_0\) of dimension \(g=2n\), with
\[
 \operatorname{End}^0(A_0)=E,
 \tag{T26.5}
\]
and fix a smooth connected projective \(n\)-fold \(Y\). Consider all targets \(A\) in the fixed \(E\)-linear isogeny class of \(A_0\), with integral \(\mathcal O_K\)-action, the same Weil signature, and compatible polarizations as in T6.25. There exists a positive integer \(b_Y\), depending only on \(Y\) and the fixed labeled isogeny class, with the following property.

For every morphism \(f:Y\to A\) having \(n\)-dimensional image and nonzero Weil projection,
\[
 \deg_L f_*[Y]\ge\frac{c_A}{b_Y^{2n}}\sqrt J.
 \tag{T26.6}
\]
The same bound with total absolute degree holds for every integral combination of the proper-push classes of such maps, provided the combination has nonzero Weil projection. The maps may vary arbitrarily. No \(E\)-action on \(Y\) itself, and no preselected finite set of homomorphisms, is assumed.

If \(A_0\) has no isotypic factor in \(\operatorname{Alb}(Y)\), there is no such nonconstant map; this is the vacuous alternative.

### C. Reduced images and energy on a fixed surface

Assume \(n=2\), so the targets are simple abelian fourfolds, and \(Y\) is of general type. Put \(K_Y^{\rm vol}=\operatorname{vol}(K_Y)>0\). The generic mapping degree \(\delta_f\) obeys
\[
 \delta_f\le K_Y^{\rm vol},
 \tag{T26.7}
\]
and therefore every reduced surface image \(Z_f=f(Y)_{\rm red}\) with nonzero Weil projection satisfies
\[
 \deg_L Z_f
   \ge\frac{8\sqrt{V\Delta}}{R\,b_Y^4 K_Y^{\rm vol}}\sqrt J.
 \tag{T26.8}
\]
Every integral combination of these reduced-image classes with nonzero Weil projection satisfies the corresponding total absolute degree bound with \(K_Y^{\rm vol}\) replaced by
\(\operatorname{lcm}(1,\ldots,S_Y)\), where \(S_Y=\max(1,\lfloor K_Y^{\rm vol}\rfloor)\). The bound on \(\delta_f\) is a surface statement; no lower bound one for higher-dimensional canonical volumes is used.

Fix a Kähler form \(\omega_Y\) on \(Y\), and let
\[
 V_Y=\int_Y\omega_Y^2>0,\qquad
 E_f=\int_Y f^*c_1(L)\wedge\omega_Y.
 \tag{T26.9}
\]
Then every such actual map has
\[
 E_f\ge
 \frac{\sqrt{8V_Y\sqrt{V\Delta}/R}}{b_Y^2}\,J^{1/4}.
 \tag{T26.10}
\]
For a fixed compact ball-quotient source, this is a lower bound on the exact finite Rallis energy of T6.11 for every actual integral map to these simple fourfold targets. Changing only the theta expansion or its coefficients at that fixed source cannot produce uniformly bounded energy as \(J\) grows.

More explicitly, fix a basis \(\eta_1,\ldots,\eta_m\) of \(H^{1,0}(Y)\) and its positive Gram matrix \(G\), normalized so that
\[
 E_f=\operatorname{tr}(C_f G C_f^*)
 \tag{T26.11}
\]
when the pullbacks of a polarization-orthonormal invariant cotangent frame on \(A\) are the rows of \(C_f\). Then
\[
 \sum_{j,a}|(C_f)_{ja}|^2
    \ge
 \frac{\sqrt{8V_Y\sqrt{V\Delta}/R}}
      {b_Y^2\lambda_{\max}(G)}\,J^{1/4}.
 \tag{T26.12}
\]
If \(Y\) is one of the compact unitary surfaces covered by T6.9, the basis may be chosen as a finite set of actual theta forms. Its fixed Gram matrix is then given by the finite bilinear Rallis identities of T6.11. Equation (T26.12) is invariant under replacing that fixed basis by any other fixed basis. It is an obstruction to a fixed-source coefficient bound, not to a construction using new sources at unbounded level.

## Proof

### 1. Clearing a bounded source order before the core factorization

Let \(h:B\to A\) be \(E\)-linear and satisfy (T26.2). For every \(x\in H_1(B,\mathbf Z)\) and \(a\in\mathcal O_E\),
\[
 a\,(b h_*x)=h_*(b a x)\in\Lambda.
 \tag{T26.13}
\]
Thus \(b h_*H_1(B,\mathbf Z)\subseteq\Lambda^-\). The complex linear universal-cover map of \([b]_A\circ h\) therefore descends to an actual morphism \(B\to A^-\), where \(i:A^-\to A\) is the core isogeny in T6.25. Pushing an integral \(n\)-cycle to \(A^-\), and then applying \(i_*\), gives the same content calculation (T25.13)–(T25.14).

On middle cohomology of a \(g\)-dimensional abelian variety, multiplication by \(b\) has
\[
 [b]_*|_{H^g}=b^g.
 \tag{T26.14}
\]
Indeed \([b]^*=b^g\) in that degree, while \(\deg[b]=b^{2g}\), and pushforward composed with pullback is multiplication by the degree. It follows that the scaled projector class is exactly the vector in (T26.3). Applying the norm-index calculation and the signed calibration bound of T6.25 proves (T26.4). Equivalently, the degree of a proper push of an \(n\)-cycle by \([b]\) is multiplied by \(b^{2n}=b^g\). The reduced-image variant follows by the same least-common-multiple argument as T6.25, retaining actual generic degrees.

### 2. One fixed quotient of the Albanese controls all maps

Choose a base point \(y_0\in Y\), let \(B=\operatorname{Alb}(Y)\), and let \(a_Y:Y\to B\) send \(y_0\) to zero. After translating its target, every \(f\) factors uniquely as a homomorphism \(B\to A\) after \(a_Y\). Translation acts trivially on cohomology and leaves polarized degree unchanged.

By complete reducibility up to isogeny, let \(D\subset B\) be the sum of the simple isotypic factors not isogenous to \(A_0\), and take the actual abelian quotient
\[
 C=B/D.
 \tag{T26.15}
\]
Every homomorphism from \(D\) to \(A\) is zero, since a nonzero homomorphism between simple abelian varieties is an isogeny. Hence every homomorphism \(B\to A\) factors through this one fixed quotient \(C\), without an additional map-dependent denominator. The quotient \(C\) is isogenous to \(A_0^r\) for a fixed \(r\ge0\).

If \(r=0\), the asserted nonconstant maps do not exist. Otherwise choose once and for all an isogeny \(s:A_0^r\to C\). Conjugating the diagonal action of \(E\) through \(s\) gives a central rational \(E\)-action on \(C\). Given any target \(A\), choose an \(E\)-linear rational isogeny \(t:A_0\to A\). For a homomorphism \(u:C\to A\), the rational map
\[
 t^{-1}us:A_0^r\longrightarrow A_0
 \tag{T26.16}
\]
is a row with entries in \(\operatorname{End}^0(A_0)=E\). Since \(E\) is commutative, every such row commutes with the diagonal \(E\)-action. Therefore every \(u\) is automatically \(E\)-linear for the fixed central action on \(C\) and the specified action on \(A\). No uniform bound on its entries is asserted or needed.

Choose a \(\mathbf Z\)-basis of \(\mathcal O_E\). Its finitely many elements act as rational endomorphisms of the fixed \(C\), so one fixed positive integer \(b_Y\) clears their denominators in \(\operatorname{End}(C)\). Then
\[
 b_Y\mathcal O_E H_1(C,\mathbf Z)
                  \subseteq H_1(C,\mathbf Z).
 \tag{T26.17}
\]
Let \(a_C:Y\to C\) be the composite of \(a_Y\) and the quotient. Every translated map is \(f=u\circ a_C\). If its image has dimension \(n\), then \(z_C=(a_C)_*[Y]\) is an integral \(n\)-cycle and
\[
 f_*[Y]=u_*z_C.
 \tag{T26.18}
\]
Part A with the fixed source \(C\), fixed denominator \(b_Y\) and arbitrary \(u\) proves (T26.6), including its integral-span version. This uses only the simple target isogeny class; \(\operatorname{Alb}(Y)\) need not itself be CM.

### 3. The surface image cannot absorb unbounded generic degree

A proper positive-dimensional subvariety of a simple abelian variety is of general type on a smooth birational model. For the surface image in a simple fourfold this applies, including when the image is singular. The canonical-volume inequality for generically finite rational maps gives
\[
 \delta_f\operatorname{vol}(K_{\widetilde Z_f})
                       \le\operatorname{vol}(K_Y).
 \tag{T26.19}
\]
A minimal smooth surface of general type has positive integral canonical square, so its canonical volume is at least one. This proves (T26.7), as in B13. Since \(f_*[Y]=\delta_f[Z_f]\), dividing the raw degree bound by \(\delta_f\) gives (T26.8). For any finite integral combination of reduced-image classes, multiply by \(L_{S_Y}\) to obtain an integral combination of proper pushes, and use Part B. For a compact ball quotient \(K_Y^{\rm vol}=K_Y^2\).

### 4. The corresponding unavoidable growth in actual theta energy

On a surface the Hodge index inequality gives
\[
 \deg_L f_*[Y]=\int_Y(f^*c_1(L))^2
                    \le\frac{E_f^2}{V_Y}.
 \tag{T26.20}
\]
Substituting (T26.6) with \(n=2\) and \(c_A=8\sqrt{V\Delta}/R\), and taking the positive square root, proves (T26.10).

In the convention
\(c_1(L)=\frac i2\sum_j\alpha_j\wedge\bar\alpha_j\)
for a polarization-orthonormal invariant cotangent frame, define
\[
 G_{ab}=\frac i2\int_Y\eta_a\wedge\bar\eta_b\wedge\omega_Y.
 \tag{T26.21}
\]
This is a positive definite Hermitian form on \(H^{1,0}(Y)\), and expansion of \(f^*\alpha_j=\sum_a(C_f)_{ja}\eta_a\) gives (T26.11). Positive-matrix comparison implies
\[
 E_f\le\lambda_{\max}(G)\sum_{j,a}|(C_f)_{ja}|^2.
 \tag{T26.22}
\]
Combining this with (T26.10) proves (T26.12).

T6.9 supplies a finite theta spanning set of this fixed \(H^{1,0}(Y)\) in its stated compact unitary setting; selecting a basis from it gives the same positive matrix. T6.10–T6.11 give its exact scalar/cohomological and Rallis normalization. Nothing in the argument bounds the source denominator \(b_Y\), its canonical volume, or its Gram matrix along a genuinely varying tower of sources. The conclusion therefore requires a fixed source, or a fixed finite collection of sources with common constants. QED.

## Sources and exact scope

The source-order, fixed-quotient, central-action and quantitative calculations are proved above. For complete reducibility and Hom between simple factors, J.S. Milne, *Abelian Varieties*, version 2.00, Chapter I, Proposition10.1 and complete proof, printed p.42, and the subsequent simple-factor Hom and matrix-algebra discussion, p.43, were read directly at <https://www.jmilne.org/math/CourseNotes/AV.pdf>. The Albanese universal property is recalled in Kato–Russell, *Albanese varieties with modulus and Hodge theory*, Section5 opening, printed p.796, with the precise universal statement in Proposition5.1(2), p.798, specialized to modulus zero; <https://www.numdam.org/article/AIF_2012__62_2_783_0.pdf>. This standard background is imported. Supplied032, Lemma2.2 and its full proof, printed p.6, also records its degree-one Albanese use.

For the surface generic-degree bound, the exact imported sources are Ueno, *On Kodaira Dimensions of Certain Algebraic Varieties*, Section3, Corollary after Proposition2, p.158, <https://www.jstage.jst.go.jp/article/pjab1945/47/2/47_2_157/_pdf>; and Guerra–Pirola, *On the finiteness theorem for rational maps on a variety of general type*, Proposition3.2(2), pp.10–11, <https://arxiv.org/pdf/0807.2980>. The entire Ueno announcement and Guerra–Pirola's complete short proof were read; no absent full proof in the announcement is claimed checked.

The constant-source result does not assert simplicity for 032's four-factor product. It applies when one actually asks a fixed source surface to map to a simple Weil-type fourfold in the fixed labeled CM isogeny class. A correspondence that is not realized by such maps, or a source with unbounded isotypic order complexity, is outside this conclusion.
