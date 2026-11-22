# Rational high-range restriction in positive characteristic

Research continuation after C.3bl; 19 November 2026, resumed after the checkpoint-17 thaw at 15:35:25 UTC. This is an **unregistered gate clarification**, not a new ordinary-Chow injectivity theorem, counterexample, or movement claim.

## Prior work read before attempting an extension

We read the complete current `agents/real_weil/POSITIVE_HIGH_RESTRICTION_RESEARCH.md`, `notes/ROOT_FINITE_THICKENING_BOUNDARY_RESEARCH.md`, and `notes/ROOT_LEVINE_SUPPORTED_K_SOURCE_AUDIT.md`. The existing distinctions between actual fixed-product families and formal/henselized-product families, and between supported perfect K-theory and coherent exceptional classes, remain in force. The certified C.3bf–C.3bl classes have exact order $p$ and therefore do not give rational kernels.

The present target is the remaining positive-characteristic rational closed-restriction range $N\geq2r+1$, initially $r=2,N=5$. Over $\overline{\mathbf F}_p$ the ordinary algebraically trivial groups are already rationally zero; this does not settle the assertion over an arbitrary algebraically closed field of characteristic $p$.

## One detecting level gives a fixed exponent for the whole-divisor kernel

Let $R$ be an excellent finite-dimensional noetherian local domain of characteristic $p$, and let $Z\to\operatorname{Spec}R$ be a regular projective modification that is an isomorphism away from the closed point. Fix a nonzero $f\in\mathfrak m_R$ and write

\[
D_b=Z\times_R\operatorname{Spec}(R/f^b),\qquad D=D_1.
\]

The enlarged centre $V(f)$ still gives an abstract blow-up square. KST Theorem A and the pro-exact sequence (1.6), together with $K_0(R)=K_0(R/f^b)=\mathbf Z$, identify the quotient by the diagonal graph with the constant group $K_0(Z)$. The level kernels of $K_0(Z)\to K_0(D_b)$ form a decreasing system of subgroups. Its being pro-zero therefore means that **one actual finite level** has zero kernel. This is the same constant-group detection argument already proved and audited in the earlier local K-theory work; we do not replace an inverse limit by a tensor product.

At that fixed level, the closed immersion $D\hookrightarrow D_b$ is nilpotent. Geisser–Hesselholt Theorem A gives bounded $p$-primary exponent for each affine relative K-group in every fixed degree. A finite affine cover of the separated scheme $D_b$, and repeated Mayer–Vietoris for the relative K-theory spectra, use only finitely many groups and degrees to calculate the relevant relative $K_0$. Finite extensions and subquotients of bounded-exponent $p$-groups still have bounded exponent. Consequently, for some integer $e$ depending on this fixed geometry and detecting level,

\[
p^e\ker\bigl(K_0(Z)\longrightarrow K_0(D)\bigr)=0.
\]

This observation does not require a uniform Serre bound for arbitrary Frobenius pullbacks of vector bundles. It gives no uniform bound over all geometries or all infinitesimal levels. In mixed characteristic the same argument requires $p$ to be nilpotent on the chosen thickening; no such hypothesis is silently imposed here.

## The remaining supported-class problem is unchanged

Let $E$ be the exceptional closed subset, $X=Z\setminus E$, and $Y=D\setminus E$. If a class on $X$ restricts to zero on $Y$, a lift to $K_0(Z)$ need not restrict to zero on the **whole** divisor $D$. Its restriction can instead be a nonzero perfect class supported on $E\cap D$. The preceding fixed-exponent statement does not apply to that class.

The relevant unproved comparison remains, schematically,

\[
\frac{
 j^*K_0(Z)_{\mathbf Q}\cap
 \operatorname{im}\bigl(K_0(D\ \mathrm{on}\ E)_{\mathbf Q}\to K_0(D)_{\mathbf Q}\bigr)
}{
 j^*i_*G_0(E)_{\mathbf Q}
}.
\]

Here the denominator is understood through the exceptional coherent boundary on regular $Z$ and its restriction. No identification of the numerator with coherent $G_0(E)$ has been proved. The whole divisor may be singular, and its Cartan map can have a kernel. Levine's supported K-theory theorem retains an extra supported term; it does not authorize deleting it. An alteration that is not an isomorphism away from the centre also changes the constant-local-graph descent argument and does not itself supply a boundary lift.

The current integral Milnor detector likewise does not supply a rational obstruction: its relative sheaf has exponent $p$. Its absolute differential can vanish through the Kodaira–Spencer boundary, so that absolute differential must not be substituted for the relative class.

## Exact nearby formal theorem, freshly reopened

Morrow's published Theorem 6.18, pp.1597–1598, states that for a smooth projective $d$-fold and a smooth ample divisor, the map from the inverse limit of cohomological K-sheaf groups to the divisor group has kernel and cokernel killed by a power of $p$ when $i+n<d-1$. For the diagonal Chow degree this requires $2n<d-1$. Remark 6.19, p.1598, extends the statement to Milnor K-theory over an infinite field. Section 6.5, p.1593, explicitly distinguishes cohomological Chow groups of a nonregular thickening from ordinary cycle Chow groups.

We freshly reopened the full 68-page published primary PDF and read the exact theorem, its proof, and Remark 6.19. This theorem controls an infinitesimal inverse limit; it does not supply the missing ordinary supported-cycle lift on the punctured principal divisor. In particular it is not a proof of the present $r=2,N=5$ assertion.

## Search and source ledger

- Kerz–Strunk–Tamme, pro-cdh descent, Theorem A and equation (1.6), author pp.2–3: the already fully opened and repeatedly audited primary input is reused for the finite detecting level. No fresh full re-proof of pro-cdh descent is claimed.
- Geisser, T., & Hesselholt, L. (2011). *On relative and bi-relative algebraic K-theory of rings of finite characteristic*. Journal of the American Mathematical Society, 24(1), 29–49. Theorem A, p.29, and Theorem C, p.30. Full primary PDF freshly opened and exact introduction/statements read: <https://math.mit.edu/~larsh/papers/025/bounded.pdf>. The bound is stated degree by degree, and the paper expressly uses Bass-completed nonconnective K-theory.
- Morrow, M. (2019). *K-theory and logarithmic Hodge-Witt sheaves of formal schemes in characteristic p*. Annales Scientifiques de l'École Normale Supérieure, 52(6), 1537–1601. Section 6.5, p.1593; Theorem 6.18 and proof, pp.1597–1598; Remark 6.19, p.1598. Full published primary PDF freshly opened and those exact passages read: <https://www.numdam.org/item/ASENS_2019__52_6_1537_0.pdf>.
- Levine (1986), *Modules of finite length and K-groups of surface singularities*, Theorem 2.1, pp.29–32, Proposition 4.1, pp.37–38: exact previously opened source audit reused; no unsupported coherent/perfect dévissage is inferred.

Searches included `"Lefschetz" "algebraically trivial" "codimension two" Chow restriction`, `"positive characteristic" "Chow groups" "weak Lefschetz" injectivity`, `"Chow group" "ample divisor" "codimension 2" injective`, and variants with `"algebraically equivalent"`. Balkan and Schreieder's newly opened 2026 Selecta paper *Cycle conjectures and birational invariants over finite fields*, Section 1.3 after Corollary 1.3 and Remark 7.9, explicitly treats projective Chow hard Lefschetz as a separate conjectural input; those passages were read at <https://link.springer.com/article/10.1007/s00029-026-01142-0>. It supplies no local supported-boundary lifting theorem. Conditional projective Chow-Lefschetz and representability results returned by the searches are not promoted to local restriction theorems. The already rejected Patel–Ravindra Lemma 3.2 route is not reused.

Additional targeted searches after the checkpoint thaw used `"Lefschetz" "algebraic representatives" restriction`, `"local Lefschetz" "K-theory" "Chow" characteristic p`, and the title of Achter–Casalaina-Martin–Vial's diagonal-decomposition monograph. The monograph's primary publisher/author URLs were located; no exact theorem from it has yet been invoked in this note. Search-only results, including broad conditional claims and unrelated automated-looking pages, are not treated as evidence for the desired statement.

## Current assessment

No rational high-range ordinary injectivity theorem or counterexample has been established in this continuation. A fixed exponent for the whole-divisor kernel is justified, but the supported perfect-class lifting comparison remains the concrete obstruction. The finite-exponent clarification alone is **not** counted as main-gate movement.
