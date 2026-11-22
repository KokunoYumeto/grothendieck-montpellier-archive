# Renewed audit of the all-genus cap-radius determination

19 November 2026, 15:53 UTC. GPT-6 Astra, OpenAI, ChatGPT Pro mode; inherited effort not separately exposed; agent `part_c_algebra`.

**Outcome: no mathematical gap found in the current image or injectivity proof under its stated stable, fixed-compactification hypotheses. In particular, the proof does not assume that the radius map is surjective. No TeX or bibliography was changed in this audit.** This is a renewed targeted review by the original author of the secondary A2b fragment, not an additional independent-author certification. The root's area lemma was independently rechecked here. No finite or numerical mathematical check was rerun.

## Text and original-source scope

The complete current `sections/part_a2b_secondary.tex` and `sections/part_a2_limits.tex` were reread. Exact manuscript locators below refer to these source files, not to a potentially changing PDF pagination. The task is the literal A.2(b) determination at prompt line169, together with its fixed pointed-surface interpretation.

| Input actually reread | Exact locator | What it supplies, and what it does not supply |
|---|---|---|
| Mondello, *Riemann surfaces with boundary and natural triangulations of the Teichmüller space* | Original `sources/mondello/Triang-submitted.tex:3494–3509,3535–3541,4078–4102`; Theorem5.4, arXiv version p.32; fixed-cusp reduction §5.6, pp.37–38. Published DOI [10.4171/JEMS/263](https://doi.org/10.4171/JEMS/263), arXiv [0804.0605](https://arxiv.org/abs/0804.0605). | The finite-stratum grafting map is a real-analytic diffeomorphism. The proof explicitly allows some boundary lengths to be zero and works componentwise. It gives the unique core for fixed marked compactification and prescribed positive lengths; it does **not** assert the radius image used in A2b. |
| Ahlfors–Bers, *Riemann's Mapping Theorem for Variable Metrics* | §5.7, Theorems10–11, printed pp.402–403, and corollary p.404; original indexed [PDF](https://www.cimat.mx/~mmoreno/teaching/fall10/AhlforsBers.pdf), reread references `turn125652602view0`, `turn125652602view1`. | Parameter dependence of normalized Beltrami solutions in the indicated Banach spaces. The manuscript separately supplies the smooth collar coefficients, marked descent and elliptic upgrade required for seam variations. We have not replaced those steps by an unsupported assertion that a moving piecewise metric is analytic at every fixed point. |
| Solynin, *Moduli and extremal metric problems*, original Russian article | Saved `sources/a2b_Solynin1999.pdf`; printed pp.9,21–23,28,32–33, all now visually read; (1.2), (2.2), Theorem2.1/(2.27). [Original record](https://www.mathnet.ru/eng/aa1040). | The reduced disc modulus is ⁠`log r/(2π)`; the weighted functional uses squared trajectory weights; those weights are the circumferences. Taking only positive-point peripheral classes gives `K(p)=sup Σp_i log r_i` with circumference weights `2π√p_i`. The original theorem supplies a unique global maximizing disc system. Other marks are retained among its allowed simple-pole/removable marked points. |
| McMullen, *Complex Dynamics and Renormalization* | §2.9, Theorem2.18 and its proof, printed pp.22–24; author-hosted [book](https://abel.math.harvard.edu/~ctm/papers/home/text/papers/real/book.pdf), reread references `turn202365572view0`, `turn202365572view1`, `turn908339831view0`, text lines771–812. | Embedded collars of width `arcsinh(1/sinh(L/2))`, mutually disjoint for disjoint simple geodesics. This is the opened book's proof, not a claim to have opened Buser's original article. The theorem has no separating-curve assumption. |

The Solynin image at printed p.33 concerns additional modulus-body statements; those are not used to shortcut the image proof. The claim here uses his explicit extremal theorem at p.32 and the independently proved convex argument.

## Coverage matrix

| Required audit point | Current proof locator | Assessment |
|---|---|---|
| Fixed surface and mixed positive/cusp ends | `part_a2b_secondary.tex:7–21,41–99`; Mondello locators above | Passed. The parameter orthant varies lengths while the pointed conformal compactification stays fixed. |
| Moving-seam regularity and finite end energies | `part_a2b_secondary.tex:32–113,135–169` | Passed, with only one-sided second derivatives required. The metric itself is only C1,1 at a seam. |
| Strict positive Hessian and global injectivity | `part_a2b_secondary.tex:123–215` | Passed. Mixed Green identities give symmetry; zero energy forces every length variation to vanish. |
| All genus, nonseparating configurations | `part_a2b_secondary.tex:7–10,193–215,283–299`; `part_a2_limits.tex:22–30` | Passed. Neither the energy identity nor the peripheral-loop comparison requires a planar core or a separating curve on an original uncut surface. |
| Support weights, zero weights, and strict inequality | `part_a2b_secondary.tex:218–249,359–362,397–406` | Passed. The support weights are squared circumferences; zero marks are retained, and collar enlargement gives strictness. |
| All nonnegative recession directions | `part_a2b_secondary.tex:303–340`; `part_a2_limits.tex:21–61` | Passed. Boundary directions are proved separately; they are not inferred from an interior-ray result. |
| Full-domain coercivity and existence of an interior minimizer | `part_a2b_secondary.tex:364–395` | Passed. The closure and finite-boundary argument is expanded below; no surjectivity assumption is hidden in it. |
| Equality cases and the claimed set of radii | `part_a2b_secondary.tex:343–356,397–406` | Passed. Strict support inequalities give finite canonical caps; extremal systems lie on support boundaries. Equal radius vectors identify the canonical representative, not arbitrary disc shapes. |

## The potentially delicate proof steps

### 1. Regularity, signs, and strictness

Near a seam the reference coordinate has flat side `y>0`; the initial metric is `sec²(y)|dζ|²` on the core and `|dζ|²` on the cylinder. Rescaling the periodic coordinate by `a=λ/λ₀`, with `y` unchanged near the seam, gives the same smooth Beltrami coefficient on both sides. Far along the cylinder, the manuscript's cutoff makes `ζ_s=aζ`; therefore `exp(iζ_s/λ_s)=exp(iζ/λ₀)` extends smoothly over the puncture. This validates the use of parameter dependence on the compactification. On the punctured universal cover one may use the invariant, reflected Beltrami coefficient to keep the normalized deck groups Fuchsian; three distinct hyperbolic fixed points normalize the marked conjugacy. Stability removes an automorphism isotopic to the identity relative to the marks.

With `V=λ Re δlog w` and `c=δλ/λ`, direct differentiation gives `h=c−V_y`. The equation `|w_t|=1` gives seam velocity `V`; equality of the metric's first derivatives on that moving seam gives `h_y^+−h_y^−=V`. The core outward normal is `+∂y` and the cylinder's is `−∂y`. These signs give exactly `E_h+E_V=πΣ δs_i δF_i`. For mixed variations the Green identity for the `V` pair may be integrated with the opposite factor order to cancel the seam term, yielding the symmetric bilinear identity stated in the text.

Flat-end derivatives decay exponentially. A fixed cusp has `h=O(1/|log|z||)`; differentiation of its displayed canonical metric gives the corresponding decaying derivatives and vanishing boundary integrals. If the energy is zero, its `2h²` term makes `h=0` on the nonempty core. On a cylinder a bounded harmonic function with zero seam boundary extends across its puncture, hence vanishes. Thus every `c_i=0`. This proves a positive definite Hessian, not merely a nonnegative symmetric part.

### 2. Topology and the uniform deficit

Removing disjoint pointed discs from a connected compact surface leaves a connected bordered core. Positive area is `2π(2g−2+n)`, including fixed cusp ends. The all-genus radius bounds use two omitted points on a stable sphere, the area of a flat torus, or Schwarz's lemma on the higher-genus universal cover. None assumes genus zero.

Orthogonal projection of every flat-cylinder excursion onto its seam is length nonincreasing and preserves the peripheral free homotopy class. Its geodesic representative in the doubled core has length `L_i`. This proves the circle-length bound for every test disc even if the test disc crosses several canonical pieces. Cauchy–Schwarz and the exact reduced-area expansion in `part_a2_limits.tex:32–61` then give `0≤K(s)−s·F(s)≤2g−2+n` without a cap-domain convergence assumption.

If an original cut is nonseparating, its two flags become distinct marked points on the same normalization component. The preceding argument already permits both points on that component. Equating their squared lengths restricts a positive definite Hessian along an injective linear map, so no null direction is introduced. This observation concerns the componentwise radius argument, not an additional claim about the literal bordered target or its disc-shape constraints.

### 3. Zero weights and strict support inequalities

The Solynin specialization retains every zero-weight mark as a puncture in the admissibility data. To require actual competitor discs at these marks, shrink the positive extremal discs slightly and insert small discs at the omitted indices. Thus the supremum is unchanged. With `b_i=log B_i`, the uniform bound `F_i≤b_i` makes `K` finite. The collar theorem gives the stronger uniform estimate in `A2b-collar-bound`, so `F_i→−∞` whenever `s_i↓0`, independently of the other parameters.

For `p>0`, the deficit and homogeneity give `p·F(tp)→K(p)`, hence `S(tp)/t→K(p)`. The coordinatewise decreasing function `S−b·s` handles a fixed positive shift. For `p≥0` with zero entries, feasibility gives the upper recession bound. The coordinate derivative bound gives

`S(s₀+tp) ≥ S(s₀+t(p+ε1))−tεΣb_i`.

The support supremum gives `K(p+ε1)→K(p)`: its upper bound is `K(p)+εΣb_i`, while any fixed nearly maximizing full disc system gives the lower limit. Letting `ε↓0` proves the missing lower recession bound. No regularity of the individual zero-weight extremal discs is assumed.

For each nonzero `p≥0`, a canonical cap with positive weight can be enlarged into its embedded collar while the other caps remain fixed. Consequently `p·F(s)<K(p)`. The same argument works for any system with pairwise disjoint analytic closures. Equality is therefore excluded for exactly the class used in the image theorem; the larger class of extremal domains is only used to specify the boundary support values.

### 4. Why the minimizer exists on the entire claimed image

Let `x` satisfy every strict support inequality and set `G=S−x·s`. An unbounded sublevel sequence gives, after normalization and passage to a subsequence, a unit direction `p≥0`. Convexity along the segment from a fixed `s₀>0` gives `G(s₀+tp)≤G(s₀)` for each fixed `t`. This contradicts the already proved recession slope `K(p)−p·x>0`. The argument remains valid if the chosen sequence's values tend to minus infinity: only an upper bound is used on the convex-combination right side.

The lower semicontinuous convex closure on the closed orthant is proper. An interior supporting affine function prevents a value of minus infinity at a finite boundary point. A minimizing sequence lies in one bounded sublevel, where that affine lower bound also prevents its infimum from being minus infinity. A closed sublevel of the extension is contained in the closure of an interior sublevel with, for example, level increased by one; it is therefore compact. Lower semicontinuity now gives an attained minimum. These are the details compressed into manuscript lines378–381.

If a finite minimum occurred at a boundary point `b`, convexity and lower semicontinuity imply `G(b+t1)→G(b)`. At least one coordinate of `b` is zero. Its logarithmic-radius derivative tends to minus infinity by the uniform collar bound, while every other derivative is bounded above. Hence `dG(b+t1)/dt→−∞`, so `G(b+t1)<G(b)` for small positive `t`, a contradiction. An infinite boundary value cannot minimize. The minimum is therefore interior and satisfies `F(s)=x`. Strict convexity supplies uniqueness, and the positive Jacobian supplies the analytic inverse.

This proves surjectivity from the support inequalities. Openness of their intersection is deduced **after** the inverse theorem, so the argument does not presume that an arbitrary intersection of open half-spaces is open.

## Actual program and reading record

Two source-page renderers were run, with no network requests and no finite/numerical mathematical tests:

| Saved program | Pages rendered | Internal elapsed seconds |
|---|---|---:|
| `code/part_c_a2b_audit_source_pages.py` | Solynin printed9,21,23,28,32,33 | 0.5113126860014745 |
| `code/part_c_a2b_audit_admissibility_page.py` | Solynin printed22 | 0.11904288000368979 |

Matching JSON/text outputs retain timestamps and paths. All seven listed pages were actually displayed and read. An initial four-image display was truncated; those four images were subsequently reopened individually before this audit was finalized. Original-source web reading is identified above by URL and returned reference; its elapsed time was not separately measured. No new mathematical statement, correction, source-access closure, or quantitative-test count is claimed from this review.
