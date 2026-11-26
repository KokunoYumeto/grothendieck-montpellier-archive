# The positivity hypotheses of GCT VI fail for Kronecker and plethysm coefficients

**Abstract.** Part VI of Mulmuley's geometric complexity theory states three hypotheses about the stretching
quasi-polynomials of Kronecker coefficients, plethysm coefficients and, more generally, multiplicities of subgroup
restriction:
- the saturation index (SH) should be bounded by a polynomial in the size of the input;
- so should the positivity index (PH2);
- the generating function should admit a positive rational form whose largest denominator exponent, the modular
  index, is bounded by such a polynomial (PH3).

We show that these hypotheses fail.

**Kronecker coefficients.** For every n ≥ 2, the series Σ_s g((sⁿ),(sⁿ),(sⁿ)) tˢ of triple-rectangular Kronecker
coefficients has a pole at a primitive root of unity of order 2ⁿ⁻¹·3ʳ, for some r ≥ 0. So every positive rational form
has some denominator exponent at least 2ⁿ⁻¹, and the same holds for every expression P(t)/∏(1 − t^{aᵢ})^{bᵢ}. The input
rank is only n² + 5n. This refutes the existence clause of PH3 for Kronecker coefficients, also in the relaxed form that
Mulmuley gave in the appendix to the paper of Briand, Orellana and Rosas.

The proof works modulo three. The cyclic permutation of the three tensor factors acts on the invariants, and its trace
series is the Hilbert series of the invariants of Cⁿ ⊕ S_(2,1)Cⁿ. In that quotient we find a unique curve fixed by the
grading group μ_{2ⁿ⁻¹}.

**Plethysm coefficients.** Take the coefficients of Sym^d(Sym³Cⁿ) along the ray of the determinant. For every n ≥ 4,
the Hilbert series has simple poles at the primitive 2ⁿ⁻¹-th roots of unity, which refutes PH3. A signed trace of these
poles dominates all other terms. This makes the positivity and saturation indices larger than 2^{cn}, for every c < 1/4
and all large n, which refutes PH2 and SH(a).

**The support theorem.** Both arguments rest on a support theorem for cubic forms. Let a diagonal matrix of two-power
order fix a semistable cubic in n variables. Then its determinant has order at most 2ⁿ⁻¹, with equality only for the
chain cubic x₁²x₂ + ⋯ + x_{n−1}²x_n + x_n³.

**Restriction from a torus.** GCT VI admits restriction from a rank-one torus as an explicit embedding. There the three
hypotheses fail at a fixed input rank.

**Provenance.** The results are due to two runs of GPT-6 Astra (OpenAI, ChatGPT Pro mode). The text was written by
Claude Opus 5.5 (Anthropic) at effort high. No human has checked it.
