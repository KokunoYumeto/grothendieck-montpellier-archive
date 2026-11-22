# Narrow independent audit of the A2 collar and marked descent

19 November 2026, completed at17:40:13 UTC. GPT-6 Astra, OpenAI, agent `part_b_cycles`, independent reviewer. This is a targeted check of a concrete regularity risk, not a new theorem, a status change, or additional substantive research movement.

**Outcome: no gap found in the current collar/Beltrami construction or the fixed marked descent.** The construction does not assert that the moving hyperbolic/flat metric is globally analytic. Its complex structure is smooth across the seam; that is the object to which analytic parameter dependence is applied. No manuscript or bibliography edit is requested.

## Scope and original evidence

The current `sections/part_a2b_secondary.tex:32–113` was read in full, together with its first-variation use at lines123–215, `notes/part_c_a2b_renewed_audit.md`, and the earlier root precision notes. The parent subsequently narrowed the requested check to a possible failure of the collar construction or marked descent, because the energy signs, mixed Green identity, zero faces, and recession argument had already been checked. This note respects that boundary and does not claim a fresh audit of the global image proof.

The relevant original Mondello passages were read from `sources/mondello/Triang-submitted.tex:3494–3509,3535–3541,4078–4102`: Theorem5.4 and the fixed-cusp discussion in §5.6 supply the finite-stratum real-analytic diffeomorphism. The source explicitly distinguishes analytic grafting dependence from the C1,1 regularity of the grafted metric. Public identifiers are [arXiv0804.0605](https://arxiv.org/abs/0804.0605) and [DOI10.4171/JEMS/263](https://doi.org/10.4171/JEMS/263).

The original Ahlfors–Bers paper was independently reopened through its indexed [original PDF](https://www.cimat.mx/~mmoreno/teaching/fall10/AhlforsBers.pdf). Actual tool references are `turn443622104view0`, `turn916237710view0`, and `turn916237710view1`. Section5.7, Theorem10, printed pp402–403 gives differentiable parameter dependence; Theorem11, pp403–404 gives holomorphic dependence; the **corollary on printed p404** explicitly gives real-analytic dependence of the normalized disc solution on real parameters. The latter is the most direct formulation for the marked universal-cover step. OCR slips in displayed differential equations are not used to infer any additional theorem. No claim is made to have opened a new physical PDF file on disk during this audit.

## 1. The cutoff gives a valid fixed compactification

At a fixed positive parameter, let a=λ/λ₀ and use the reference collar ζ=x+iy, with x of period2πλ₀. Near the seam the coordinate change is `(x,y)↦(ax,y)`. Pulling back either metric gives the conformal class of `a²dx²+dy²`; the core's additional scalar factor is sec²y. Therefore both sides have exactly the same Beltrami coefficient `(a−1)/(a+1)`, including all spatial derivatives at the seam. The unmatched second derivative of the scalar density does not enter the complex structure.

For the flat-side cutoff in manuscript lines56–67,

`∂y y_s = 1+(a−1)(χ(y)+yχ′(y))`.

The parenthesized function is bounded: it vanishes near the seam, is1 sufficiently far out, and has compact transition. Thus a parameter neighborhood of a=1 makes this derivative uniformly positive. Periodicity is respected by the x-rescaling. Far out, ζ_s=aζ and λ_s=aλ₀, so the filled-disc coordinate `exp(iζ_s/λ_s)` is exactly `exp(iζ/λ₀)`. In particular the identification extends over the marked center and introduces no parameter-dependent singularity there. The remaining cusp charts are fixed.

The fixed smooth cutoffs need not be analytic in the spatial variable. Their parameter dependence is real-analytic in every finite C^k norm, which is the relevant assertion. Combining them with local analytic Fenchel–Nielsen representatives gives a smooth Beltrami coefficient depending real-analytically on the finite-dimensional parameter in C^k, hence in L∞, with norm uniformly below1 after shrinking the parameter neighborhood. This is enough for Ahlfors–Bers. It does not replace the piecewise metric by a globally analytic one.

## 2. Analytic normalized maps descend with the marking

Use the universal cover of the stable punctured reference surface. Its deck group is non-elementary, including the stable sphere and once-punctured torus cases. Lift the invariant coefficient and take the normalized **disc** solution. The p404 corollary gives real-analytic parameter dependence; equivalently one can use reflection and the plane theorem. Reflection is an available normalization, not an assumption that arbitrary plane-normalized solutions preserve the disc.

For each deck transformation γ, invariance makes the conjugate Γ_s(γ) a disc Möbius transformation. Its coefficients depend analytically on s without requiring boundary regularity of the normalized solution: take three fixed, distinct interior points z_j, and recover the unique Möbius transformation from the three pairs `W_s(z_j)↦W_s(γz_j)`. All six points depend analytically on s and remain distinct locally.

The marked conformal class is fixed by the already used infinite-grafting inverse. Consequently these representations are conjugate to the fixed marked representation. Choose three reference hyperbolic elements with distinct attracting fixed points. Their varying fixed points are simple roots of the corresponding Möbius fixed-point equations, hence are analytic functions of the real parameters. The unique disc Möbius map matching the three ordered fixed points gives an analytic local choice of conjugacy. It is the required conjugacy for the whole group, since such a marked conjugacy already exists and the three-point normalization determines it. A lift can be chosen locally near the reference lift; the possible inner-conjugacy ambiguity is discrete. Thus the normalized maps descend to the fixed Y with the prescribed marking.

Finally, a stable marked compactification has no nonidentity conformal automorphism isotopic to the identity relative to the marks. This removes ambiguity in the descended marked isomorphism. The argument uses fixed **marked** Teichmüller data; it would not follow merely from equality of unmarked moduli points.

## 3. Spatial regularity is sufficient for the first shape derivative

Ahlfors–Bers starts with dependence in its indicated Hölder/Sobolev Banach spaces. On every compact subchart of the lifted surface, the coefficients are smooth spatially and analytic in the parameter. Interior elliptic estimates for the Beltrami equation give locally uniform bounds in any prescribed finite spatial differentiability norm, for the solution and parameter derivatives. More explicitly, the real-analytic coefficient can be complexified locally in parameter, preserving a uniform ellipticity bound; the holomorphic solution has locally uniform higher spatial bounds by the same estimates. Cauchy estimates in parameter then give the corresponding analytic dependence in each lower finite spatial norm. Thus the bootstrap does not consist merely of a formal differentiation of an L∞ solution.

At a cap center the tail trivialization has zero Beltrami coefficient. The descended map is holomorphic there, so its derivative at the center is analytic in s by the Cauchy integral formula. The conformal radius, a positive analytic modulus of a nonzero derivative after the stated normalization, is real-analytic. Across the seam the descended maps are spatially smooth. The individual metric pieces remain analytic after their separate trivializations, with equal value and first spatial jet on the moving seam. This is sufficient to differentiate the matching conditions once in the parameter.

Specifically, at the reference seam their logarithmic densities have equal zeroth and first jets, and second normal derivatives1 on the core and0 on the cylinder. The first Eulerian variation is consequently continuous. Differentiating the matched first normal derivative along the seam of normal speed V gives the stated one-sided jump `h_y,+−h_y,−=V`. This step does not differentiate the whole metric twice across the seam, nor assume analytic dependence at a fixed point crossed by the seam. The existing Green calculation applies on the fixed base pieces with these traces.

## Audit record and limits

This was a hand proof audit with local file reads and one targeted original-source reopening. No symbolic calculation, finite enumeration, numerical experiment, source download, or mathematical program was run. The targeted web `find` call returned in a tool-reported0.8seconds; a separate high-resolution runtime was not instrumented. No raw external source body was written inside the deliverable project. Only the narrow audit note and one event were added. The conclusion is that the specific suspected regularity defect is absent under the manuscript's stated fixed, stable, marked hypotheses; it is not a new theorem or source-access closure.
