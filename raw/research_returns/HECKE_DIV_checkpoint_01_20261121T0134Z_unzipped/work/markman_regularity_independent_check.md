# R28. Independent audit of the explicit Markman output bound

Run HECKE_DIV_20261121. Check date: 2026-11-21. Checker: `/root/reductions`, GPT-6 Astra Pro; effort setting not exposed. This note records an independent reconstruction and a subsequent complete proof reading of M7.1–M7.5 and M8 in `work/markman_output_regularity.md`. It is not a formal proof-assistant verification. The numerical bound is a new derivation by the arithmetic agent, not a theorem attributed to Markman.

## Result and scope

The bound `reg_H(E) ≤ 112` is correct under the exact seed hypotheses in M7: a smooth nonhyperelliptic genus-three Jacobian, thirteen disjoint translates in each family, and the stated vanishing of all Picard twists of `I_Z1(2Θ)`. The stronger estimate

`H^i(A,[m]^*E ⊗ L)=0` for `i>0` whenever `c1(L)−112m²H` is nef

also passes. Consequently, for a determinant-normalized rank-96 seed and a relatively very ample deformation polarization h, the explicitly certified bound

`R_safe = 112·96²·c + 96·C + 6`,

where `c h−H` and `C h−c1(det E)` are ample, supplies the six regularity vanishings needed for persistence on an analytic neighbourhood. The conclusions about the deformation family remain conditional on the particular flat twisted deformation provided by Markman's construction and on a specified deformation polarization. No unexamined assertion that seed global generation is automatically open is used.

## R28.1. Total-space complex and duality

Write the integration variable as y, the translation parameter as x, and the dual parameter as α. The coordinate change `(y,x)↦(y,z=y+x)` identifies the two curve supports with pullbacks under independent projections. Over C these are Tor independent: locally the relevant quotients are tensor products over the ground field. Thus the ordinary product of their ideals is their intersection, and tensoring the inclusion–exclusion sequence by the line bundle ℒ gives an exact length-two resolution of the input M.

The line bundle on the abelian-threefold integration fibre has class `2Θ`; Kodaira vanishing and Riemann–Roch give a rank-8 bundle W in degree zero. Each of the 26 curve restrictions has degree 6 on a curve of genus 3. Its first cohomology vanishes because its Serre-dual degree is −2, and Riemann–Roch gives rank 4. Hence U has rank 104. The pairwise intersection is the disjoint union of 169 copies of `C×C×Xhat`. Each maps finitely to a divisor in `X×Xhat`: the curve map is the degree-two quotient `C×C→Sym²C`, followed by the isomorphism `Sym²C≅Θ`. The last is an isomorphism because C is nonhyperelliptic of genus 3; its theta divisor is smooth. There are no positive direct images of these finite maps. Consequently the derived pushforward is the complex `[W→U→Tcal]` in degrees 0,1,2.

The Picard-uniform vanishing assumption makes `W→U` injective on every fibre already by its first thirteen curve components. Constant fibre rank therefore makes its quotient Q a locally free rank-96 bundle. The complex becomes `[Q→Tcal]` in degrees 1,2.

Each summand of Tcal is a finite-flat direct image of a line bundle to a smooth divisor, then a divisor embedding into the smooth sixfold. It is Cohen–Macaulay of codimension one. Hence its only sheaf Ext against the structure sheaf is Ext¹. Finite duality gives

`Tcal^D = ⊕ f_*(ω_T ⊗ ℒ_T^−1)`.

The triangle `Tcal[−2]→G→Q[−1]→`, after derived duality and shift by −1, gives the short exact sequence

`0→Q*→E→Tcal^D→0`.

I checked the shifts independently: `RHom(Tcal,O)=Tcal^D[−1]`, so both outside terms of the resulting triangle are in degree zero. There is no hidden exactness assumption on the singular locus.

## R28.2. The cohomology of W* and U*

For positive q, relative duality along the integration variety followed by absolute Serre duality reduces the p-th cohomology of each dual bundle twisted by qH to total cohomology in degree `6−p` of its original integration space with the line bundle twisted by `−qH`. Project instead to the integration variable, keeping the base sixfold as the fibre. On that fibre the numerical matrices are

`diag(1−3q,−3q)`

and, for the second curve family after writing `z=y+x`,

`[[1−3q,1],[1,−3q]]`.

Both are negative definite for q≥1: the largest eigenvalue before subtracting `3q I` in the second case is `(1+sqrt(5))/2<3`. Thus all direct images except degree six vanish, by Serre duality and Kodaira vanishing on the abelian fibre. Total cohomology below degree six is zero. This proves the complete higher-cohomology vanishing used in M7.2 and hence 7-regularity. The argument is unchanged by translations and arbitrary Picard-zero factors.

## R28.3. Evaluation kernels and Buchsbaum–Rim indexing

Evaluation of `U*(7H)` gives a kernel K_U. For `i≥2`, the long exact sequence shows vanishing at twist `(14−i)H`: the free middle term has positive exponent `7−i`, and the U* group is one of the vanishings just proved. For i=1, multiplication surjectivity for a 7-regular sheaf, not merely the higher-cohomology argument, is needed and is available. Thus K_U is 14-regular.

Composing evaluation with the bundle surjection `U*→W*` gives a surjection from `O(−7H)^N` to W*, with kernel J, and the exact sequence

`0→K_U→J→Q*→0`.

For a rank-8 quotient bundle W*, the terms of the Buchsbaum–Rim resolution of J are exactly

`C_k = wedge^(8+k)(O(−7H)^N) ⊗ Sym^(k−1)W ⊗ det W`, for k≥1.

The determinant factor has the indicated sign. I reconstructed its exactness in the locally split case rather than relying on a depth criterion. Splitting the source as `K⊕V` with V the rank-8 target, the part with a exterior factors from K identifies with

`wedge^(a−k)V* ⊗ Sym^(k−1)V*`.

The differential is the homogeneous polynomial de Rham differential, of total degree a−1. Euler contraction proves exactness when a≥2 in characteristic zero; the a=1 term maps isomorphically to K. This is the required augmented resolution locally, and therefore globally.

The standard polarization-isogeny pullback formula, also directly obtained by translating the integration variable, gives `[2]^*W=Q0^⊕8` up to numerically trivial factors. The numerical class of Q0 has matrix

`[[2,2],[2,−2]]`.

Its eigenvalues are `±2sqrt(2)`, whereas `[2]^*H` has matrix `12I`. Pulling back `Sym^(k−1)W⊗det W` therefore produces copies of `Q0^(k+7)`. For every q≥k+7, its qH twist is ample upstairs. Trace splitting descends the higher-cohomology vanishing. This yields regularity at most k+13 for that factor and at most `69+8k` for C_k.

The six-term truncation is correct. At cohomological degree i, successive long exact sequences require the groups of C_k in degree `i+k−1`. The last potentially relevant k is `7−i`, whose degree is six; the following kernel group has degree seven and vanishes on a sixfold. To deduce R-regularity of J it suffices that `R≥reg(C_k)−k+1` for `1≤k≤6`. The maximum is

`max_(1≤k≤6)(70+7k)=112`.

The exact sequence with K_U then gives 112-regularity of Q*. This check does not depend on a bound for N. If a complex terminates before its sixth term, the omitted terms are zero and the argument only shortens.

## R28.4. Positivity for the torsion dual

On `C×C`, put `S=F1+F2`. The theta class under addition is `4S−Δ`, since the theta restriction to either Abel–Jacobi curve has degree 3 and the mixed Poincaré class is `S−Δ`. Its intersection with the diagonal is 12, independently checking the sign.

The class `R=3S−Δ` is nef. A degree-three map to P¹ exists by projecting the canonical plane quartic from a point of the curve. The residual fibre-product divisor has class R. Its transitive degree-three monodromy is S3 or A3. In the S3 case the action on ordered pairs of distinct sheets is transitive, so the residual divisor is irreducible, and its self-intersection is `18−12−4=2`; it therefore has nonnegative intersection with every curve. In the cyclic A3 case it is the sum of the two nonidentity automorphism graphs. Each graph has self-intersection −4. Riemann–Hurwitz gives five fixed points, and the distinct order-three tangent eigenvalues make these intersections transverse. Each graph therefore has intersection 1 with their sum; all other curves have nonnegative intersection. This proves nefness in both cases, without a generic-branching assumption.

For q≥3, the class `q f*H−c1(ℒ_T)` decomposes as

`[3qR+(3q−6)F1+(3q−3)F2] + (3q−1)Θ_α + [3F1+Θ_α+P_(c1,α)]`.

The first bracket is ample on `C×C`, the second is ample on Xhat, and the final bracket is a theta pullback and therefore nef. Their sum is ample. Kodaira vanishing on the smooth fivefold gives the desired vanishing for `ω_T⊗ℒ_T^−1⊗f*O(qH)`. Since the torsion dual has support dimension five, twists `q=8−i` for `1≤i≤5` suffice for 8-regularity. The extension then proves the stated 112 bound for E.

## R28.5. The strengthened vanishing and family passage

I independently checked the addition M7.5. Pullback by [m] preserves all exact sequences. In the duality argument the fixed base-fibre numerical matrices scale by m². If `c1(L)−112m²H` is nef, subtraction of L makes these classes antiample, so `[m]^*W*⊗L` and `[m]^*U*⊗L` have no positive cohomology. The evaluation kernel consequently has vanishing in degrees at least two; degree one is not used in the passage to Q*.

For the first six Buchsbaum–Rim terms, after a further pullback by [2], the relevant positive-definite matrix is

`12[112−7(8+k)]I + (k+7)[[2,2],[2,−2]]`.

Its smallest eigenvalue is at least `168−26sqrt(2)>0` for 1≤k≤6. Addition of the assumed nef form preserves ampleness. All positive cohomology of these terms vanishes, and the same dimension-six truncation gives the assertion for J and then Q*.

For the torsion term form the finite étale base change `g:T'→T` and the finite map `f':T'→A`. Its dual is `f'_*(ω_T'⊗g*ℒ_T^−1)`. The line bundle needed for Kodaira vanishing has numerical class

`g*(3f*H−c1(ℒ_T)) + f'*(c1(L)−3m²H)`.

The first summand is ample by R28.4 and finiteness of g. The second is nef (indeed ample on its finite image) by the hypothesis. This proves all positive-degree vanishings and establishes M7.8.

For `B0=[r]^*E⊗(det E)^−r`, `r=96`, substituting `L_i=(det E)^−r⊗h^(R_safe−i)` gives

`c1(L_i)−112r²H = 112r²(c h−H)+r(C h−c1(det E))+(6−i)h`,

which is ample for 1≤i≤6. This is a direct proof of the six regularity vanishings; it closes the earlier openness gap. Finite-coefficient twisting is killed by [r] on a torus family, since [r] acts by r² on H² with μ_r coefficients. On a contractible analytic base this allows the stated local untwisting. Any flat-line ambiguity does not affect the numerical vanishing argument. Upper semicontinuity then preserves regularity, and properness preserves the codimension-at-least-four condition on the nonfree locus after shrinking.

## R28.6. Effective Chern cycles

For a globally generated normalized sheaf B(Rh), locally free off codimension at least four, general dependence loci of `r−p+1` sections give effective representatives of c_p for p=2,3 on the locally free open. Localization identifies CH^p of that open with CH^p of the sixfold for p≤3, because the complement has dimension at most two. Closing the loci therefore gives the required classes without contributions of the wrong codimension.

I checked the twist elimination:

`c3(B)=C3−(r−2)R h C2 + [r(r−1)(r−2)/3]R³h³`.

The integer coefficient and the two degree formulas in M8 follow. With only cohomological c1-triviality these are asserted as cohomology-class identities; literal Chow identities require the extra Chow normalization expressly stated in M8. This distinction is correctly retained. At least one effective part has nonzero Weil projection whenever c3(B) does. The subsequent global bounded-cycle argument is a separate input, not a consequence of the Chern-character calculation alone.

## Sources actually used and checks

- Markman (2025), supplied TeX source `250531.tex`: source paragraphs at lines 5110–5195 and 5370–5475 were read directly in this turn; earlier source proof locators were read in the preceding audit. This verifies the precise assumptions and identification of E. No numerical regularity theorem is attributed to this source.
- The entire M7.1–M7.5 and M8 text in `work/markman_output_regularity.md` was read. The proofs above were reconstructed from the geometric and linear-algebra definitions. In particular the Buchsbaum–Rim indexing was independently reproved; this note does not claim an independent reading of the Raicu–Sam PDF.
- Check status: all displayed assertions pass under their stated hypotheses. No numerical computation or proof-assistant run was used in this check. The unused possibility of a smaller torsion-dual regularity bound was not needed and is not part of the certified estimate.
