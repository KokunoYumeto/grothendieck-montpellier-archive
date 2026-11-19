# A.2(b): secondary investigation of the canonical-cap radius map

Owner: part_c_algebra. Started 2026-11-19 after completing Part C.

## Exact question and current gate

For a fixed marked compact Riemann surface with chosen tangent coordinates at its marked points, the canonical infinite grafting construction gives a real-analytic family of capped hyperbolic surfaces indexed by positive boundary lengths. The outstanding question is whether the vector of canonical cap conformal radii determines those lengths, and what its exact image is. A theorem about fixed lengths is not by itself a theorem about this radius map.

The general injectivity and exact image theorem are now proved in `sections/part_a2b_secondary.tex`, using the root's explicit area comparison `A2-strebel-deficit` in `sections/part_a2_limits.tex`. This note retains the initial routes below as a record of how the proof was found; they are superseded by the moving-seam proof.

## Sources actually inspected

1. G. Mondello, source `sources/mondello/Triang-submitted.tex`, subsection “The grafting map,” theorem labelled `thm:grafting` (published Theorem 5.4), and the proof at lines 4080–4307. The map consisting of infinite grafting and the boundary length vector is a homeomorphism and a real-analytic diffeomorphism on each finite topological stratum. The injectivity proof fixes the boundary lengths; its reduced-energy argument cannot immediately be reused when lengths vary.
2. A. H. Fırat, source `sources/firat_bootstrap/WKB-short.tex`, Appendix B, equation labelled `eq:connection` (B.1): partial derivative of the on-shell Hadasz–Jaskólski action in a length parameter is `2 lambda_i log r_i`. Formula by itself does not establish convexity in squared lengths or global injectivity of its gradient.
3. Root reports a convention inconsistency in the 2021 paper: gamma is defined as Gamma(1-x)/Gamma(x) near the introduction and its reciprocal in the body. Use the body and corrected 2023 formulation only after checking branches.

## Routes under investigation

Let `s_i=lambda_i^2`. Formally, B.1 gives `dS/ds_i=log r_i`. Strict convexity in `s` would imply injectivity. Its asymptotic relation to the extremal product of conformal radii might then identify the image as an interior of a logarithmic radius body. Neither the strict convexity nor the required global boundary/properness statement has been established; these are separate gates.

An alternative is a direct comparison of the hyperbolic/flat grafted metrics, with a monotonicity identity pairing changes in squared boundary lengths against changes in logarithmic radii. Such an identity needs a proof with interface terms and cannot be inferred from fixed-length grafting rigidity.

## Completed proof, independently checked with root

Write `g_t=exp(2u_t)|dz|^2`, `h=dot u`, `lambda_i=L_i/(2pi)`, and `s_i=lambda_i^2`. A conformal seam coordinate is `zeta=x+iy`, with the core at `y<0`, metric `sec(y)^2 |dzeta|^2`, and flat cylinder at `y>0`. For the varying normalized cap coordinate let `V_i=lambda_i Re(d/dt log w_i)` and `c_i=dot lambda_i/lambda_i`. Then:

- `(Delta-2)h=0` on the core; `Delta h=0` on the cylinders.
- `V_i` is harmonic, `h=c_i-(V_i)_y`, and `V_i(infinity)=-lambda_i dot(log r_i)`.
- The seam's normal velocity is `V_i`; differentiation of matching first derivatives gives `(h_y)_flat-(h_y)_core=V_i`.
- Green's formula gives `E_h=-sum integral hV`, and `E_V=sum integral hV-sum c_i integral V_i`.
- The circular mean identity is `integral V_i=-2pi lambda_i^2 dot(log r_i)`.
- Therefore `pi sum dot s_i dot(log r_i)=E_h+E_V>0` for any nonzero variation. Polarization proves symmetry of the Jacobian.

The positive Jacobian is thus a proved energy identity, not a numerical inference or an assumed convexity property of the Hadasz–Jaskolski action. Zero energy forces `h=0` on the nonempty core, and then on each cylinder, so every length variation is zero. Fixed cusp ends contribute no boundary terms: `h=O(1/|log|z||)` there.

The required real-analytic family regularity follows from Mondello's finite-stratum inverse, analytic collar charts, and Ahlfors–Bers parameter dependence. On the universal cover, normalize the conjugating deck-group Möbius map by three distinct boundary fixed points; smooth Beltrami coefficients permit elliptic bootstrap across the seam charts. The metric itself is only C^{1,1}, which is sufficient because the second derivatives used in the jump computation are one-sided.

Let `K(p)=sum p_i log R_i(p)` for the Jenkins–Strebel discs with circumferences `2pi sqrt(p_i)` and zero-weight remaining marks. Solynin's weighted reduced-modulus theorem identifies K with the supremum over disjoint pointed disc systems. Root's area comparison proves `0 <= K(s)-s·log r(s) <= 2g-2+n`; this gives the recession function of the strictly convex potential S. A collar estimate gives
`r_i <= B_i exp[-arctan(csch(pi sqrt(s_i)))/sqrt(s_i)]`,
so the inward derivative at every finite boundary point of the nonnegative orthant is negative infinite. Minimizing `S(s)-x·s` now proves that the exact log-radius image is
`{x : p·x < K(p) for every nonzero p>=0}`.
The complete bounded-sublevel and boundary-exclusion arguments are in the TeX fragment. No compactness/convergence assertion about abstract Teichmuller points is needed for this image proof.

## Primary sources checked for the completed proof

- Ahlfors–Bers, *Riemann's Mapping Theorem for Variable Metrics*, Annals72(1960),385–404. Full indexed PDF opened at https://www.cimat.mx/~mmoreno/teaching/fall10/AhlforsBers.pdf ; tool `turn937810368view0`. Section5.7, Theorems10–11, pp402–403 explicitly read. Direct local fetch403, recorded in the source-fetch output; the indexed full text is accessible.
- Solynin, *Moduli and extremal metric problems*, Algebra i Analiz11(1999),3–86. Original Russian PDF opened: https://www.mathnet.ru/php/getFT.phtml?jrnid=aa&option_lang=eng&paperid=1040&what=fullt ; tool `turn899768493view0`. Exact specialization: reduced disc modulus (1.2), printedp9, `turn152856588view0`; circle homotopy classes §2.1 p21 and weighted functional (2.2) p23, `turn152856588view1/2`; Theorem2.1 and (2.27), printedp32, `turn860097884view0`. The general Theorems3.1–3.2 were also visually inspected on pp36–37, screenshot refs `turn860097884view1/2`, but are unnecessary for this specialization. The English translation was not opened.

## Numerical diagnostic actually run

`code/part_a2b_checks.py` with seed22021119, float64 scipy continuous loggamma and digamma. All1209 tested pants Hessians had positive eigenvalues after diagonal normalization; the smallest normalized eigenvalue was8.3969789919e-6. All600 random strict-monotonicity pairings were positive. Maximum normalized symmetry residual1.8152e-14; finite-difference derivative residual1.7240e-9. Output is in `code/part_a2b_checks_output.json/txt`. These diagnostics are not proofs. The continuous loggamma branch is essential; taking the principal logarithm of a Gamma quotient changes the cap scale.

## Independent review of root's limit proof

Read `sections/part_a2_limits.tex` in full. Checked the test-annulus area inequality, the signs of its reduced-area terms, the removal of zero-weight terms by their upper bounds, the lower bound for each positive-weight radius, the disjointness of nonconstant limit maps, and uniqueness of the weighted maximizer. The zero-weight collapse argument is valid because the positive-weight discs fill the complement of a critical graph with empty interior.

Directly checked `k(u)=4u/(1+u)^2`: derivative4 at0 and pullback of `-dz^2/[z^2(1-z)]` equal to `-du^2/u^2`. For the orange domain, `m(0)=exp(2pi i/3)`, the chosen power sends0 to i, and `|U'(0)|=3sqrt(3)/4`, so the radius is `4/(3sqrt(3))`. The third critical arc is the long arc of `|z-1|=1`, supplementing the explicitly named long unit-circle arc and vertical segment. Root was informed of this small prose clarification.

