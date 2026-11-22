# Independent whole-proof review: PNEW-009

Date: 2026-11-21 UTC. Reviewer: /root. Model: GPT-6 Astra Pro.
Effort setting: not exposed. Run: GCT_POS.

I read every proof and paragraph of
`branches/plethysm/fixed_rank_density.tex`. Outcome: **PASS in the stated
fixed-rank, fixed-inner-partition population**.

The polynomial sublevel estimate follows by choosing a primitive lattice
direction on which the top homogeneous polynomial is nonzero, then
slicing into one-variable polynomials of constant nonzero leading
coefficient. The union of root neighborhoods bounds the number of
integer points by O(R^(r-1/e)). The nonnegative top homogeneous parts
of chamber quasipolynomials are justified by arbitrarily distant lattice
points in each residue coset. Top-term domination controls every
nonzero univariate constituent at all real scaling arguments at least
one, and hence the strict saturation index.

The conversion to the literal sum-of-bit-lengths shells is not an
unjustified change of population. A generic positive interior direction
has distinct binary-threshold crossings under one doubling. Open balls
with D consecutive total lengths supply a full-dimensional nonzero
residue class in every sufficiently large shell. The degree equation
determines a coordinate of largest bit length; unbalanced lengths and
all shorter-height faces therefore have exponentially smaller counts.
The remaining, balanced exceptional points obey the polynomial sublevel
bound. All exponents and the stated eta = 1/(2D(D-1)e*) were checked.

I independently opened Baldoni and Vergne, arXiv:1506.02472v1, and read
section 5.1, Proposition 60, Lemma 61, Theorem 63, and the finite-wall
description in Propositions 65--67 (printed pages 51--53). The no-common-
ideal hypothesis applies to the proper image of sl_n in sl_m for m>n.
The finite kernel is handled by the image compact group's weight lattice
and finite congruence conditions. The determinant direction adds one
dimension and yields the sole degree equation d|lambda|=|pi|. Its shift
dm/n is integral, as follows from the determinant character of S_mu.

No uniformity in n or mu follows. The theorem does not decide the
original population in which the embeddings themselves vary, and the
paper says so explicitly. Classical chamber and quantization theorems
remain cited inputs, rather than being claimed as newly proved here.

