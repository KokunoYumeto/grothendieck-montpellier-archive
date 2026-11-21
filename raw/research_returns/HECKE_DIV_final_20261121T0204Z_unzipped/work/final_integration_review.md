# Final independent integration review

Run HECKE_DIV_20261121. Reviewer: `/root/reductions`, GPT-6 Astra Pro; effort setting not exposed. Date: 2026-11-21. This records the actual final proof readings and new independent checks, not a formal proof-assistant certification. Earlier complete reconstructions are in `markman_regularity_independent_check.md` (R28) and `severn_quantitative_independent_check.md` (R29).

## Overall result

The newly supplied quantitative fourfold and eightfold arguments pass under their explicitly retained geometric inputs. The exact new M9/M10 calculations were independently reconstructed and executed. The requested integrated mathematical sections were read, including the mixed-characteristic parameter argument P6. No unresolved mathematical gap was found in the quantitative conclusions under the stated fixed integral polarized data.

The review identified one small overgeneralized proposition statement: M8's dependence-locus proof requires rank r≥3. The author added that hypothesis; its actual rank-96 application is unchanged. The review also requested that R22 explicitly identify H as a connected Q-algebraic subgroup of the ambient Shimura group in its rational H¹ representation, in addition to saying linear. This states the already intended rationality hypothesis needed for the isogeny conclusion. The final R22 statement now explicitly makes H a connected Q-algebraic subgroup of the ambient Shimura group in its fixed rational H¹ representation; this clarification has been checked in the updated TeX.

Transcription fixes in the new eightfold TeX—commas in exponents of N_isog and a carriage-return escape in the mass integral—were sent to the section author. They were corrected and the updated text was reread. No control characters remain in that section. They were typesetting defects, not changes in the mathematical constants. The obsolete statements that the numerical tasks remained open have been removed from the inspected main abstract and closing status. The last part now correctly separates stronger unproved extensions.

## R30. Independent M9 derivation

### R30.1. Input character, GRR, and signs

For one Abel–Jacobi curve on the genus-three Jacobian, GRR gives

`ch(O_C)=θ²/2−θ³/3`.

The first coefficient is the Abel–Jacobi class and the second is χ(O_C)=−2 times the point class θ³/6. For thirteen disjoint translates, multiplying the ideal character by exp(θ) gives exactly

`ch(I_Z(Θ))=1+θ−6θ²−2θ³`.

The same is true for reflected translates.

I independently derived the relative Gaussian identity used in M9. The quadratic matrix on the integration coordinate y and the two base coordinates is the matrix with integration diagonal u+v, mixed entries v and −1, and x diagonal v. Completing the square in each symplectic coordinate pair leaves the base quadratic form

`(uv x+v p−y)/(u+v)`.

There are three symplectic pairs, hence the prefactor `(u+v)^3`. In cohomological degrees 0 through 6 the degree-k expression is the polynomial

`(u+v)^(3−k)(uv x+v p−y)^k/k!`, `0≤k≤3`.

The input polynomial is obtained by applying `Σc_i c_j ∂u^i∂v^j` at zero; there are no missing factorials because differentiation of exp(uθ) returns θ^i. The output is `E=G^∨[−1]`, so its degree-k character is `(-1)^(k+1)` times the derived pushforward character. This agrees with the positive rank 96 and all four displayed character polynomials.

### R30.2. An independent exact numerical certificate

The new checker `work/check_markman_numbers_independent.py` does not use SymPy or the author's polynomial routines. It uses Python Fraction dictionaries and multinomial counting. For each monomial `x^ix p^ip y^iy` it expands the preceding GRR polynomial directly, sums the allowed u/v exponents, and applies the factorial derivative weights. It independently computes κ2, κ3 and all relevant intersections.

The integration functional is independently encoded by the four monomials of `(bc−e²)^3`. Namely

`∫x^i y^j p^k=0`

unless `(i,j,k)=(3−s,3−s,2s)` for `0≤s≤3`, in which case it equals

`(-1)^s binom(3,s) i!j!k!`.

The executed output `work/markman_numbers_independent_check.json` confirms every character coefficient, both normalized character polynomials, and the following exact integers:

| Quantity | Independently verified value |
|---|---:|
| rank | 96 |
| normalized h-regularity | 2,065,542 |
| ∫h⁶ | 906,992,640 |
| Δ_h | 1,259,712 = 108³ |
| ∫h⁴c2(B0) | 30,136,419,515,105,280 |
| ∫h³c3(B0) | 28,288,052,451,512,156,160 |
| negative effective degree | 3,426,088,289,770,686,418,974,855,223,050,240 |
| positive effective degree / D_src | 3,426,088,289,770,714,707,027,306,735,206,400 |
| principal comparison M | 84,537,841,287,168 |

The checker also independently verifies the expanded values of D_6, H_3 and both finite fourfold cap coefficients in the author's JSON. The large least common multiple is intentionally left as an exact finite formula.

### R30.3. The polarization and family interpretation

The calculation gives `κ2(E)=−169(12x+y)²/48`. I checked that the relevant Spin action here is the actual degree-preserving exterior action, which preserves cup products; the source distinguishes it from the twisted Fourier–Mukai action. Thus differentiating invariance is legitimate. Since `h0=12x+y` is ample, the map `h0∧:H²→H⁴` is injective. Invariance of h0² therefore makes the connected group fix h0. The source gives the one-dimensional invariant polarization line, so the choice `h=3h0` is justified.

The numerical matrix of h is diag(36,3), giving polarization type `(3,3,3,36,36,36)`. For c=2 and C=12, the comparison matrices are

`diag(69,3)` and `[[168,48],[48,14]]`.

Their leading principal minors are `(69,207)` and `(168,48)`, respectively. Therefore both are ample. The strengthened vanishing already checked in R28 supplies regularity `112·96²·2+96·12+6`, not merely global generation. The proper nonfree locus remains of codimension at least four on a smaller analytic neighbourhood, so the explicit effective-Chern-cycle construction applies with fixed intersection numbers. Markman's nonzero Weil component is a retained source theorem; it is not inferred merely from a nonzero total Chern character.

The source passages actually checked in this final review include the input and action definitions, main theorem item3, the normalization lemma at lines2406–2478, the invariant-line statement at lines3966–3968, and the eigenspaces at lines1353–1364 of the supplied TeX. I also read the active cyclic-orbit existence argument at lines5200–5318, distinguishing it from the following hidden alternative discussion.

## R31. Principal transfer, sixfold Cramer estimate, and fourfold contraction

### R31.1. Integral order enlargement and the degree factor

The source eigenspaces give the cohomological action of `f=sqrt(−12)` as

`[[0,12θ],[−θ^−1,0]]`.

Because θ is the unimodular principal-polarization contraction, this matrix and its dual are integral. The identity `ω=(f−2)/4` yields the O-stable lattice `Λ_O=Λ+ωΛ⊂(1/4)Λ`. Stability follows directly from `ω²+ω+1=0`. Its index divides `4^12`.

The form 16h is integral on Λ_O and remains positive of type (1,1), giving the quotient polarization h_O. The degree-I quotient satisfies `q_O^*h_O=16h`; volume comparison gives `Δ_O=16^6Δ_h/I`, an integer divisor of `16^6Δ_h`.

The hyperbolic-basis calculation previously checked in R29 works in rank six with the absolute Hermitian determinant. For a block matrix `[[0,B],[B*,D]]`, the determinant has sign −, while its absolute value is `Norm(detB)`. The transformations `X=(B*)^−1D/2`, `w'=w−vX`, and `u=w'B^−1` have denominators dividing 2Δ in both directions. Comparing with a principal split target therefore has denominator dividing 4Δ_O, and `M=4·16^6·Δ_h` clears it uniformly.

The resulting composition has polarization pullback `16M²h`. A cycle of dimension three therefore acquires precisely the factor `16³M⁶`, by the projection formula. The rational isometry identifies the marked period domains, preserving a nonempty analytic open image and the nonzero Weil projection. Thus the degree `D_6=16³M⁶D_src` is valid.

### R31.2. Independent sixfold projector certificate

The new script `work/check_projector_n3_independent.py` reconstructs all seven eigenvalues by ordinary integer-pair multiplication in `Z[ω]`, rather than trusting the listed eigenvalues. It evaluates the numerator by independently coded Horner evaluation and checks the weighted degree sum. Its executed output is `work/projector_n3_independent_check.json`.

All seven values agree exactly: the two extremes give

`δ3=1,701,760,099,946,011,389,900`,

and the other five give zero. The weighted sum is

`B3=6,493,952,361,560,098,735,300`.

The reconstructed eigenvalue is `a^6=37+360ω`. The original n=2,4 independent certificate was not rerun or counted twice.

### R31.3. Cramer coefficients and uniformity

The exterior-coordinate argument for the saturated integral Weil lattice applies equally with n=3, giving `G3=9[[2,1],[1,2]]`. For `z=δ3P[Z]=xu3+yv3`, the norm bound is

`18(x²+xy+y²)=||z||²≤δ3²D_6²/36`.

Thus `h_z=x²+xy+y²` lies between one and `H3=max(1,floor(δ3²D_6²/648))`. The exact action matrix is

`T=[[37,360],[−360,−323]]`,

and `det(z,Tz)=−360h_z`. Cramer's coefficients for `360h_z u3` have absolute values `|360x+323y|` and `|y|`. Applying T to a cycle multiplies degree by343. Since `|x|,|y|≤h_z`, the weighted coefficient cost is at most1026h_z, strictly below `3·360h_z`. This proves the separate-sign degree bound in M10b.

For the finite cap, the union over `1≤h_z≤H3` of the closed loci with multiplier `360h_z` and corresponding degree `3·360h_zB3D_6` contains an analytic open. It is therefore the whole irreducible component. This preserves the relation between the multiplier and its degree bound. For an explicit common multiplier, `360·lcm(1,…,H3)` is divisible by every possible multiplier; scale before applying the closed fixed-multiplier locus. Both versions are correct and distinct.

### R31.4. Compensation with separate sign bounds

On `A4×B`, `B=E_x×E_y`, the marked determinant forms satisfy `Ω3=Ω2Ω1` without an extra sign, since moving the third x-form past two y-forms contributes +1. Therefore

`u3=u2 U−v2 V`.

The pairwise divisor intersections are `U²=V²=−2`, `UV=−1`. The two contractions are consequently

`pr_*(u3(−2U+V))=3u2`, `pr_*(u3(−U+2V))=3v2`.

Their actual signed divisors are

`−2U+V=3(Fx+Fy)−2Γω−Γ1`, `−U+2V=Γ1−Γω`.

Each graph is nef and at most `2θ_B`. Thus the first pair of signs is bounded separately by `3θ_B` and `6θ_B`, and the second by `2θ_B` and `2θ_B`. Generic translations on B give proper intersections with every component; a component with point image can be avoided, which contributes zero. These translations preserve the cohomology and nef estimates.

For an effective three-cycle Z,

`3∫_Z θ4²θ_B≤∫_Z(θ4+θ_B)³`.

If its two signs have degrees at most D', either signed contraction therefore has each sign of degree at most3D'. This uses `(3+6)/3=3` for the first contraction and `4/3≤3` for the second; no signed-degree cancellation is used.

The same sixfold multiplier gives both fourfold basis classes, so taking an integral combination adds only `|a|+|b|` to the degree. For `t=(a u2+b v2)/q`, the verified cap is

`N≤1080qH3`, `deg Z±≤3240H3B3D_6(|a|+|b|)`.

The explicit common version uses `L3=lcm(1,…,H3)` in place of H3. No extra multiplier is introduced by combining the two contractions.

## R32. Integrated proof readings and exact scope

The following current files were read in full for their mathematical arguments: `deliverables/HECKE_DIV.tex`, `sections_remaining.tex`, `regularity_section.tex`, `integral_seeds.tex`, `prime_section.tex`, `markman_quantitative.tex`, and `eightfold_quantitative.tex`. The unproved-extensions part of `open_and_bibliography.tex` was also read. The earlier detailed archive source audit remains the record for `archive_section.tex`; the parent owns the final bibliography and rendering checks.

### R32.1. Mixed-characteristic P6

The finite-type parameter justification is valid in its stated relative-cycle formulation. One takes the finite union of bounded-degree Chow parameter spaces, then a finite-type h-cover on which both universal effective relative cycles are represented. Quasicompactness permits finitely many cover pieces. On each reduced irreducible piece, simultaneous flattening of the closures of finitely many generic supports gives proper surjective modifications with genuine flat projective cycle families. Equality with the pulled-back relative cycle follows from equality at generic points, because relative cycles of the indicated type are determined by those generic values. The flattening process is not being mistaken for a flat universal subscheme on the coarse Chow scheme.

The resulting parameter scheme has finitely many irreducible components. Vertical components account for only finitely many residue places. A point above any other place lies on a horizontal component; a trait from its generic point to that point carries the flat cycles. Smooth proper base change and cycle-class specialization injectivity transport the equality with its actual positive integer N_v to characteristic zero. The trait's fraction field is finitely generated over the number field and embeds in C. Betti comparison then yields equality of rational Betti classes. Characteristic-zero parameter specialization descends the pair to Qbar without altering degree. Conversely, a rational algebraic class can be descended and spread with fixed cleared coefficients. This proves all the stated equivalences, including varying unbounded initial N_v.

The theorem still requires a fixed nonzero global realization and a common bound for the integral effective degrees. It does not turn pointwise algebraicity in finite characteristic into lifting without that bound. The exact application of 032 Remark8.5 is stated with this missing uniform-degree condition retained.

### R32.2. Core reductions and new quantitative sections

R21 uses proper bounded-degree Chow spaces and constancy of the cycle class, rather than a bound on Hilbert polynomials for arbitrary schemes. Its Baire uses are qualitative; its final analytic-open closedness uses with explicit bounds do not introduce unknown constants. The fixed-multiplier variants are applied correctly in M10 and SQ9.

R22 requires a connected linear Q-subgroup acting through the fixed rational H¹ datum of the Shimura variety. With that explicit qualification, rational density and rational Hodge isomorphisms give precisely the stated tensor-compatible isogeny orbit. The special-unitary application fixes the chosen Weil class. R23 retains the necessary eventual avoidance of every proper special subvariety, rather than the weaker assertion of not being contained in one.

The corrected divisor and endomorphism counterexamples, graph-degree formula, P1/P2 denominator and raw-growth assertions, P3 finite positive lattice argument, and integral seed formulas remain consistent. The n=3 basis used in M10 is the same exterior proof applied at n=3; its separate statement makes this extension explicit.

The quantitative eightfold TeX matches the independently audited SQ proof. Its principal refinement also checks: `31104=54(4!)²`; the action matrix is `[[−1504,1265],[−1265,−2769]]`; the determinant is `−1265(x²+xy+y²)`; the scale factor is2401 and the sine of the rotation angle has absolute value `1265sqrt(3)/(2·2401)`. The two-dimensional coefficient cost is at most `4·2401/(1265sqrt(3))<5`. This yields the stated factors1265 and6325, or the explicit common multiplier1265·lcm. The two targets can use the same multiplier from the same seed before forming their integral combination.

The final SQ9 norm estimate can be stated most directly by pairing the signed representatives with unit Weil classes, using the same comass/Wirtinger proof as P3. This avoids an unnecessary assertion about all strongly positive forms. Both approaches give the required bound `||y_i||≤B`; the parent requested the shorter direct version.

### R32.3. Limits of this review

The source theorems remain cited inputs with their actual status. In particular, I did not independently reprove Severn's entire dominance theorem or Markman's semiregular deformation theorem in this final integration pass. Their prior team audits and exact reconstruction records are retained. Reading those scope statements in the integrated paper is not recorded as a new complete source-theorem verification.

The new explicit constants are sufficient bounds for fixed data. They do not assert optimality, explicit equations for every fibrewise cycle, uniformity over changing rational targets or unbounded integral orders, a general Hodge theorem in all dimensions, or formal Lean verification. The final unproved-extensions part correctly identifies these stronger assertions separately from the completed fixed-family quantitative work.


## Final correction closure

The updated M8 statement explicitly assumes r≥3. The updated R22 statement has the required ambient Q-subgroup and rational H¹ action. All SQ exponent and control-character transcription defects were corrected. The final SQ9 proof now uses unit Weil classes, invariant harmonic forms, Wirtinger volume and comass exactly as in P3; its norm bound and subsequent Gram estimate pass. The complete M10a/M10b/M10 theorem and proof in the final TeX, including the shared multiplier for both contractions, were read and agree with R31. No mathematical correction remains outstanding from this review.

### Inspected integrated source hashes

These hashes record the versions actually inspected at the completion of this review; later purely editorial or rendering changes belong to the parent’s build record.

- `HECKE_DIV.tex`: `25cb47b5c27782ea48009a5336547328ebfc267a06dc129a2b4eb8986426516a`
- `sections_remaining.tex`: `6930842243851362d860c7add8720e69524e23f667b9bf702f2cdce062e8a2ba`
- `regularity_section.tex`: `a5441046794fd3c21f592fb4423581e17d84893f20b7e8a3cdf9a28d3e7d5e9f`
- `integral_seeds.tex`: `7a5fa8695718eb70af598949bbdea6e235ddbe7df97d786c519aa9b664d603cf`
- `prime_section.tex`: `07a163259e510668c121047041ab3c493881664adb40441aa2480e6ff3bfe220`
- `markman_quantitative.tex`: `e8446bf4d69369a5d1ff9c3df79244c5bad8ef075db792c0a8983cc9d81686e4`
- `eightfold_quantitative.tex`: `6ba9ecbaf3b6d16f7eefe248e61ffaa28cb78fa6946ac8389a6278a25a2b255b`
- `open_and_bibliography.tex`: `923aaaccedfd013f627e2a4bb3bf97180f5c083425d4112b28b551f4b2babca0`
