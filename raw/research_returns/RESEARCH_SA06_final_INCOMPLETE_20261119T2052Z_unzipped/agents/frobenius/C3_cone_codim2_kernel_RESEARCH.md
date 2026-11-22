# A precise projective subproblem inside rational local injectivity

19 November 2026. This is an unregistered research reduction, not a solution of the remaining universal rational restriction assertion and not a movement claim. It uses the already certified C.3ax and C.4a.

Let $k$ be algebraically closed of characteristic $p>0$. Let $V/k$ be a smooth projective connected fourfold, let $L$ be very ample with normal degree-one-generated full section ring, and let $H\in|L|$ be smooth connected. Form the strict local cone puncture $X$ over $(V,L)$ and its principal punctured hyperplane $Y$. Write $J^r$ for ordinary algebraically trivial cycles modulo rational equivalence, using actual proper parameter curves.

The following comparison is the exact obstruction already present in this restricted family:

\[
\ker\bigl(J^2(V)_{\mathbf Q}\longrightarrow J^2(H)_{\mathbf Q}\bigr)
\simeq
\ker\bigl(J^2(X)_{\mathbf Q}\longrightarrow J^2(Y)_{\mathbf Q}\bigr).
\]

We give the argument to distinguish this projective cycle problem from an infinitesimal nilpotent problem. We do not assert that either kernel vanishes.

## Cone and ordinary-family identifications

C.3ax identifies both rational Chow and ordinary-algebraic quotients of the strict local cone with their projective quotients. Its proof applies also to the standard graded quotient ring $S/(s)$ defining the hyperplane cone, even if that quotient ring is not the full normal section ring of $H$. Indeed, its degree-one blow-up charts are the total line bundle $L_H^{-1}$, the puncture is regular, the exceptional zero section is $H$, and there is still an actual retraction to $H$. KST finite detection, nilpotent invariance after inverting $p$, Chern pullback, and ordinary-family localization use precisely these properties; normality of this quotient cone is not an extra premise.

For either $W=V$ or $W=H$, these identifications and the defining kernel $J^2=\ker(\mathrm{CH}^2\to B^2)$ give

\[
J^2(X_W)_{\mathbf Q}
\simeq
\frac{J^2(W)_{\mathbf Q}}
 {J^2(W)_{\mathbf Q}\cap c_1(L_W)\operatorname{Pic}(W)_{\mathbf Q}}.
\]

To see surjectivity directly, if a projective lift of an ordinary-trivial punctured cycle has class $c_1(L_W)b$ in $B^2(W)$, choose an actual divisor representative of $b$ and subtract its $L_W$-multiple. The resulting projective lift is ordinary algebraically trivial. This uses the already proved actual-family localization, not a family on a varying étale neighbourhood.

The denominator is exactly $c_1(L_W)\operatorname{Pic}^0(W)(k)_{\mathbf Q}$. One inclusion is immediate. For the reverse inclusion, if $L_WD$ is algebraically trivial, its prime-to-$p$ cycle class is zero. Hard Lefschetz makes multiplication by $L_W$ injective on $H^2(W,\mathbf Q_\ell(1))$ in dimensions three and four. The Kummer sequence and the finite-generation theorem for Néron–Severi groups then imply $D\in\operatorname{Pic}^0(W)(k)_{\mathbf Q}$. Possible torsion Néron–Severi classes disappear after tensoring with $\mathbf Q$.

## The two divisor columns are isomorphic

Weak Lefschetz on $H^1(-,\mathbf Q_\ell)$ shows that the pullback of reduced Picard varieties $\operatorname{Pic}^0(V)\to\operatorname{Pic}^0(H)$ is an isogeny. Its map on $k$-points therefore becomes an isomorphism after tensoring with $\mathbf Q$; this conclusion allows a finite inseparable kernel and needs no stronger integral Picard assertion.

For a smooth projective variety $W$ of dimension at least two, multiplication by $L_W$ is injective on $\operatorname{Pic}^0(W)(k)_{\mathbf Q}$ as a map to $J^2(W)_{\mathbf Q}$. If $L_WD=0$, multiply by $L_W^{\dim W-2}$ and apply the Albanese map. The resulting map from the Picard variety to the Albanese is the degree-one Lefschetz isogeny of C.4a. Its kernel is finite, so $D=0$ rationally. This is an actual zero-cycle/Albanese argument, not an assertion that a Picard-zero divisor has nonzero ordinary cohomology.

We consequently have a commutative diagram with exact rows

\[
0\to L\operatorname{Pic}^0(V)_{\mathbf Q}
\to J^2(V)_{\mathbf Q}\to J^2(X)_{\mathbf Q}\to0,
\]

\[
0\to L_H\operatorname{Pic}^0(H)_{\mathbf Q}
\to J^2(H)_{\mathbf Q}\to J^2(Y)_{\mathbf Q}\to0,
\]

whose first vertical arrow is an isomorphism. The snake lemma gives the claimed kernel isomorphism.

## Scope and implication

The local ring has dimension five and the cycles have codimension two. Thus the first high-range rational local problem already contains an ordinary projective restriction problem for fourfolds. The argument does not prove that every arbitrary local germ reduces to a cone, does not identify a conjecture with the full universal local assertion, and does not prove projective Chow weak Lefschetz. It only shows explicitly where the previously proved cone rigidity stops.

Source dependencies are C.3ax's completely opened KST/GH/TT/Fulton/actual-family inputs and C.4a's opened Kleiman Appendix Theorem2A9(5)–(6), together with the classical prime-to-characteristic cohomological weak/hard Lefschetz and Kummer inputs already used throughout the master. No newly searched theorem is used as an unverified replacement for a cycle-level assertion.

## The ordinary incidence test excludes every cycle, not only divisor products

There is a particularly concrete limitation on the proposed supersingular-surface variant. Let $W$ be **any** smooth projective threefold, let $B$ be very ample, and choose two sections whose common zero locus $B_0$ is a smooth connected curve. The smooth incidence divisor

\[
H=\{x_0s_0+x_1s_1=0\}\subset V=\mathbf P^1\times W
\]

is $\pi:H=\operatorname{Bl}_{B_0}W\to W$. If $E$ is its exceptional divisor, then the pullback of the hyperplane class from $\mathbf P^1$ is $h=\pi^*c_1(B)-E$.

The integral projective-bundle and codimension-two blow-up formulas identify the ordinary-trivial groups, after tensoring with $\mathbf Q$, as

\[
J^2(V)_{\mathbf Q}=J^2(W)_{\mathbf Q}\oplus h\operatorname{Pic}^0(W)_{\mathbf Q},
\qquad
J^2(H)_{\mathbf Q}=J^2(W)_{\mathbf Q}\oplus\operatorname{Pic}^0(B_0)_{\mathbf Q}.
\]

These decompositions preserve ordinary algebraic equivalence in both directions because the projective-bundle/blow-up maps and their inverses are actual pullback, pushforward, and divisor-intersection operations on the fixed products with a proper parameter curve. With the exceptional summand normalized by $j_*q^*$, restriction sends

\[
\alpha+hD\longmapsto\bigl(\alpha+c_1(B)D,-D|_{B_0}\bigr).
\]

Repeated cohomological weak Lefschetz shows that $\operatorname{Pic}^0(W)\to\operatorname{Pic}^0(B_0)$ has finite kernel. Consequently, if this ordered pair vanishes rationally, then $D=0$ and then $\alpha=0$. Restriction is therefore injective on **all** ordinary algebraically trivial codimension-two cycles in this incidence test. A nondivisorial class in $J^2(W)$ is not lost by the calculation; it is the first component and is detected directly.

Together with the cone kernel comparison, this excludes a rational kernel from the corresponding split-cone incidence construction, including the case $W$ is a product of a supersingular surface and a curve. It does not exclude other ample hypersurfaces, a singular leading divisor, or a general nonconical modification. The exact integral blow-up/projective-bundle inputs are the already opened Jiang Theorems2.4/2.8(3) and Stacks Tag02TX used throughout the certified cubic arguments. No new main-gate movement is inferred from this construction limitation.
