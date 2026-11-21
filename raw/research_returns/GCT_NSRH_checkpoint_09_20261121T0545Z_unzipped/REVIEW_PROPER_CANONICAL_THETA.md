# F65: independent full-proof and final-fragment review

Reviewer: `/root/rectangular_and_theta`, GPT-6 Astra Pro; reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

## Targets and verdict

**PASS. No mathematical correction is required.** I read the entire current report and the entire generated fragment, independently reconstructed the proper-multiplicity argument, every parameter-weight case, the explicit alternate pure complex, and the hard-Lefschetz contradiction. I also read the relevant original BBD contexts and visually checked the displayed VIII coefficient. The final fragment matches the complete report, including the distinctions between proper pure complexes and projective pushforwards of pure perverse inputs.

- `agent_proper_canonical_multiplicity_gate.md`: SHA256 `6508633190a36f2a1ca360543f2b3e2e8b6e9982df2ff18fd99abed1545936b8`.
- `finding_F65.tex`: SHA256 `49e9352c49537e7d0facb4a50f75e03e6725f9813d315ce93f78a4951385ee06`.

This review does not assume a relation between VIII's source parameter and IV's source parameter. The separately announced audit of that relation is outside these frozen targets. No supplied positivity conjecture is claimed to assert the proper-geometric hypotheses being tested.

## 1. Proper canonical multiplicity argument

The geometric Hom premise is necessary and is stated correctly. A geometrically absolutely simple perverse label S, with specified pure Weil structure and Frobenius-stable geometric class, has scalar geometric endomorphisms after the permitted coefficient extension. For a geometrically semisimple pure perverse sheaf P, its S-isotypic summand is canonically the evaluation image S tensor Hom_geom(S,P). Frobenius preserves it and acts on the Hom space by conjugation. It is not the space of Frobenius-fixed morphisms.

For proper f and a pure complex L of weight W, the two six-operation bounds and f_!=f_* give a pure pushforward T of weight W. BBD 5.4.1 then gives perverse cohomology of weight W+i. BBD 5.3.8 supplies geometric semisimplicity, and 5.3.1 supplies purity of the selected perverse subquotient. Arithmetic Frobenius need not be semisimple; the report and fragment explicitly allow its Jordan blocks.

The restriction step is carefully stated. One first regards the isotypic object on its closed support. Closed pushforward preserves both weight bounds, and its inverse on supported objects is obtained by the relevant restriction, so it reflects both bounds there. One then restricts to a smooth dense **open** stratum. Open restriction has j^*=j^! and preserves both bounds. This avoids asserting such preservation for an arbitrary closed restriction of a pure complex.

On a d-dimensional dense stratum, write S=M[d]. M has weight w_S-d. The corresponding tensor local system M tensor V_i has weight W+i-d. At a closed point of degree m, the product of an eigenvalue alpha of M with beta^m, for beta an eigenvalue of the base Frobenius on V_i, has the latter weight. Dividing its absolute value by that of alpha gives

`|beta|=q^((W+i-w_S)/2)`

under each embedding covered by the purity hypotheses. Tensor eigenvalues are pairwise products even in the presence of Jordan blocks. Thus V_i is pure of weight W+i-w_S, and placing it in degree i makes the point complex pure of weight W-w_S.

The all-extension or eventual-extension Euler comparison is then exactly the hypothesis of the already proved pure-point Vandermonde criterion. Distinct nonzero spectral roots have linearly independent eventual power sequences; purity permits a given spectral root in only one cohomological degree. There can be no hidden cancellation between different degrees. Therefore the Laurent coefficient condition is

`(-1)^(W-w_S) f(-v) in N[v^{+/-1}]`.

If a nonzero f is divisible by v-v^-1, its transform vanishes at v=1. A nonzero effective Laurent polynomial cannot vanish at a positive real point. Multiplying by an overall sign or a monomial does not remove this zero. The asserted shifted/twisted variants are therefore correct.

## 2. Actual VIII coefficient and normalization distinction

I visually read `primary_sources/GCT_VIII_p34.png`, the original Figure 2. The second displayed line is exactly

`c(gamma_2^1,gamma_1^1;gamma_21^1)=-(q_src^2+q_src+1)(q_src-1)^2/q_src^2`.

Its expansion is `c(t)=-t^2+t+t^-1-t^-2`. No named-generator effectivity premise is needed to apply the conditional multiplicity argument to this actual individual structure constant.

For t=q^n and v=q^(n/2), the trace is

`c(v^2)=-(v-v^-1)^2(v^2+1+v^-2)`.

It is nonzero and vanishes at v=-1, so it fails the tested proper-pure multiplicity comparison. The hypothesis is a geometric comparison added by the proposal, not a consequence of VIII's signed/factored positivity. F62's nonproper mixed model and the normalized proper P2 factor are correctly retained as different constructions.

For t=q^(n/2), the trace is instead c(v), and `-c(-v)` has four positive coefficients. I checked the proposed bounded point complex term by term:

| Summand | Cohomology degree | Frobenius weight | Euler contribution |
|---|---:|---:|---:|
| L_2[-1] | 1 | 2 | -v^2 |
| L_1 | 0 | 1 | v |
| L_-1[2] | -2 | -1 | v^-1 |
| L_-2[3] | -3 | -2 | -v^-2 |

Each weight is one plus its cohomological degree. The complex is pure of weight one and has the stated trace. It is an arithmetic Weil-complex construction; the text does not infer an integral geometric half-Tate motive or a canonical proper product realization.

For t=q^(dn/2), inversion invariance reduces d to |d|>0. If d is even, all four exponents are even but their coefficients have mixed signs, contradicting every possible pure-complex parity. If d is odd, exactly odd complex weights work, with each root of exponent e placed in degree e-w. This gives a construction for every permitted weight. The classification and its dependence on the parameter assignment are exact.

## 3. Independent hard-Lefschetz check

Assume a pure complex has ordinary Euler trace epsilon v^m c(v^d). The power-sum and purity argument fixes the four spectral roots, each with absolute multiplicity one. It therefore fixes the four nonzero cohomology degrees as

`m-2d-w, m-d-w, m+d-w, m+2d-w`.

If the signs do not match their parities, the pure model already fails. Otherwise this support remains forced. There are no additional invisible roots or opposite-parity multiplicities because each nonzero root has only one possible pure degree.

A hard-Lefschetz operator with a single integral center h forces support symmetry. Its extreme degrees give h=m-w. The middle group H^h is zero, whereas H^(h-2d) and H^(h+2d) are both one-dimensional. The required map ell^(2d) between the extremes factors, after d applications of the degree-two operator, through H^h(d)=0. It is zero and cannot be an isomorphism. Tate twists do not change this vanishing. This proves the stated contradiction for every nonzero integer d and for every common monomial or overall sign.

The distinction in the final application is correct. Relative hard Lefschetz is supplied by a **projective morphism with a pure perverse input**, not by an arbitrary proper pushforward of an arbitrary pure complex. Taking the Frobenius-stable geometric S-isotypic multiplicity of the relative Lefschetz maps preserves their isomorphism and their Tate twists. Hence this stronger comparison is excluded even in the odd-d cases where point-complex purity alone is possible.

No Frobenius semisimplicity is used in either argument. In the forced four-root case the corresponding groups are one-dimensional anyway; the general purity and trace steps already allowed Jordan blocks.

## 4. Exact primary contexts inspected

Original BBD publication: https://www.numdam.org/item/AST_1982__100__1_0/; local `primary_sources/BBD.pdf` and `BBD.txt`.

I read the original extracted contexts of:

- BBD 5.1.13--5.1.14, p. 128: the upper/lower six-operation bounds and duality; these yield proper purity and the open-restriction step.
- BBD Proposition 5.3.1, pp. 134--135: perverse subquotients preserve each weight bound.
- BBD Theorem 5.3.8, p. 138: geometric semisimplicity of a pure perverse sheaf.
- The unipotent Jordan example immediately following 5.3.8, pp. 138--139: purity does not imply arithmetic semisimplicity.
- BBD Proposition 5.3.9 and its proof, pp. 139--140: Frobenius-stable isotypic decomposition, geometric Hom multiplicity, and the equivariant evaluation isomorphism.
- BBD Theorem 5.4.1, p. 141: perverse cohomology weights are shifted by i.
- BBD Remark 5.4.9, pp. 143--144: proper direct image of a pure complex is pure.
- BBD 5.4.10, p. 144: a relative ample Chern class gives the degree-two Tate-twisted maps, and the hard-Lefschetz theorem assumes a projective morphism and a pure perverse input.

The separate dictionary correctly treats the coefficient spaces as actual Weil representations and their Euler classes as virtual classes. It does not impose a commutative lambda-ring structure on a noncommutative convolution algebra or attribute the tested nonstandard comparison to SGA/BBD.

## 5. Direct final-text match and scope

I read the entire final `finding_F65.tex`, not merely its theorem statements. It retains every proof step above, both exact parameter rules, the all-n/eventual-n trace premise, the geometric-Hom convention, the specified Weil form and base-extension qualification, the no-insertion premise, the pure point construction, and the stronger projective pure-perverse Lefschetz hypothesis. The report-to-fragment match passes at the two frozen hashes in the first section.

No computation is needed for this review; the four-term expansions and degree/weight table were reconstructed directly. No master paper or shared master log was edited. The source-variable identification and any additional simultaneous-normalization supplement require their own separately stated hypotheses and review.
