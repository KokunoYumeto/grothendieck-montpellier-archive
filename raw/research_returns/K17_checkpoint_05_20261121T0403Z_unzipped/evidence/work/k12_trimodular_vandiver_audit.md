# Independent whole-proof audit: K17-K12-TRIMODULAR-GENERATED

Reviewer: `/root/vandiver_k`, GPT-6 Astra Pro. Date: 2026-11-21 UTC.
Reasoning effort: not exposed. Verdict: **PASS**, with the exact restricted
scope and published classification dependency retained.

## Material completely read and checked

I read the entire `k12_trimodular_classification_section.tex`, the entire
standalone `k12_trimodular_classification_certificate.py`, and its author's
entire `k12_trimodular_classification_checks.md`. I reconstructed the
argument separately from its implementation and executed the exact
verifier successfully. Its output checks all three records: first
impossible as a complete minimum set, second the earlier certified tau,
third with an odd integral symmetry. The published exhaustive
classification was not rerun.

I also compared the verifier's three literal vertex records by exact
Python parsing with the complete archived primary file
`k12_source_data/delta_dim_3_delta_3_extremal.txt`; they agree exactly.

## Primary source readback

I freshly read the following passages of the final published
Averkov--Schymura paper in `k12_source_data/averkov_schymura_2024.txt`:
the definitions on printed pp.62--63, the complete convex-polytope
reformulation and classification procedure in sections 5.1--5.2 on
pp.82--84, Algorithm 1, and Tables 1--3 on p.85. The definitions allow
nonprimitive columns and bound maximal-size minors, as the proof needs.
The exact values h(1,3)=13, h(2,3)=19, h(3,3)=25 and the three extremal
classes for (Delta,m)=(3,3) are correctly transcribed. The use of all
three values accounts for the distinction between Delta-modular and
Delta-submodular matrices.

I read the complete archived author README and all three data records.
Fresh primary retrievals also succeeded for the arXiv paper,
https://arxiv.org/pdf/2111.06294 (`turn844349831view0`), and author
repository https://github.com/mschymura/delta-classification
(`turn844349831view1`). The archived final journal text supplies the
pagination used in the proof; the arXiv pagination is different.

## Mathematical checks

1. The complementary-Plucker normalization is exact over Z. Surjectivity
   of V makes its maximal-minor vector primitive; saturation of the
   kernel row lattice does the same for B. Rational proportionality
   therefore has scalar plus or minus one. No unproved unit minimum
   basis is being assumed before the reduction to the three records.

2. Signed repeated-column transpositions preserve the integral relation
   lattice, as does a transposition of two zero columns. Their quotient
   automorphisms exchange exactly two independent quadratic rays.
   The previously audited low-excess theorem supplies simpliciality.

3. If no repeated signed columns or two zeros occur, the maximal-column
   bound forces exactly one zero column and twelve nonzero signed
   classes. Taking the convex hull cannot enlarge the determinant
   maximum, by multilinearity in each column. The extremal bound then
   forces every lattice point to be among the twenty-five listed points.
   The lower values for Delta=1,2 force Delta=3. Origin symmetry and
   uniqueness of the center eliminate the translation part of an affine
   unimodular equivalence.

4. A zero Gale column is an integral split coloop under the explicit
   minimum-generation hypothesis. Its rank-nine quotient core has
   precisely the twelve proposed minimum pairs, even when the original
   witness form has cross terms with the coloop.

5. In the first record, all six auxiliary vectors are outside those
   pairs, and the exact quadratic identity gives their total norm six.
   Strictly larger than one for each would contradict that identity.
   The second record is reconstructed integrally as the complete tau
   model, whose filling was independently certified earlier. In the
   third, the given integral relation-space map induces precisely three
   pair transpositions, and therefore an odd orientation action.

6. The fixed-coface lemma retains the necessary admissibility
   hypothesis. Its other facets have odd stabilizers, so a stabilizer of
   the coface preserves the unique surviving facet and fixes the new
   quadratic ray. The incidence is one because it is the unique actual
   surviving facet, with no transfer factor. No coface existence is
   inferred solely from the fixed-vector equations.

7. For the corollary, an actual maximal index three ensures that the
   index of the minimum-generated sublattice divides three. Index at
   most two is already removed. Subtracting the explicit fillings of
   all covered generators preserves the cycle condition and leaves
   exactly the stated support classes.

## Scope

The result removes minimum-generated rank-ten projective degree-twelve
cells of maximal minimum-basis index at most three from homology
representatives. It leaves maximal index at least four and proper
index-three ambient glue. It does not prove either of those remaining
classes vanish, compute the whole rank-ten homology, or establish K_12
vanishing. Completeness of the three published extrema remains a cited
source input, explicitly separate from the executed per-record checks.

Reviewed TeX SHA256:
`49346606a0ebf0052db62cf8bcd5e12bddc6db5215ea27b5ae8ef91d6cfa82f9`.

Reviewed verifier SHA256:
`961b4ffd56f8141a5921cbaf374221915e3a49ac5903b11fdd1755026f57b6a0`.

Archived primary data SHA256:
`4afa2c6665f6608ef914b47739609469007e1a3737eb4ad154cfba4397ff5db4`.
