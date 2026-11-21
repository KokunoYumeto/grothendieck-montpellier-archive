# Root follow-up checks, 2026-11-21 UTC

Reviewer: /root, GPT-6 Astra Pro; reasoning effort not exposed.

## Greenberg commuting section

I read the added paragraph in the full theorem context. The cyclotomic quotient is abelian, so a fixed generator fibre is a Delta-stable right H-torsor. Finite coprime complement conjugacy and compactness trivialize its nonabelian H1 class. The fixed lift has infinite procyclic pro-p closure, hence Zp, and its map to Gamma takes a generator to a generator. It is an isomorphism. This supplies genuinely commuting actions, with no additional arithmetic assumption. The rest of the theorem had already received a whole-proof read.

## K12 partial orientation section

I read the entire combined TeX, not only the conclusion. The minimal positive/negative quadratic circuit has at least 2m vectors; the face in its m-dimensional span and the quotient squares imply m<=d+1 and cone dimension<=2d+1. The published basicness theorem up to dimension9 therefore applies for d<=4. Each distinct rank-one positive-semidefinite ray is extremal, so no dependent circuit remains.

For the orientation result, complementary minors transfer the determinant bound to the Gale matrix. In the unit-index case every minor of the nonidentity block is a maximal minor of [I A], so total unimodularity is justified. Signed repeated columns give an actual lattice transposition. In the proper index-two case the mod2 relation lattice is exact because V is an integral surjection; the six nonzero classes and zero class, together with the one singleton, give a linear functional selecting exactly three doubled classes. Its odd product of swaps preserves the glue. Passing to the radial quotient preserves orientation sign. I checked the exact DHS and Lee theorem statements and dimension/count conventions in the primary PDFs; their full classification computations were not rerun. Verdict PASS for the stated restricted cells, not for all target homology.

## Explicit orientation survivor

I read all of k12_orientation_survivor.md, all of k12_trimodular_exact_certificate.py, and all of k12_trimodular_extremal_check.py. I independently reconstructed the hand classification of Gale symmetries: the unique content-three column fixes the first axis, the three distinct quotient-fibre cardinalities force scalar quotient action, and the interval constraints give only plus/minus I and plus/minus J. The induced ray permutation has four transpositions. The unique zero relation column in the rank-ten orthogonal extension must be fixed, so the same parity conclusion holds there.

I reran the exact certificate. All nine rational LDL pivots are positive, the exact recursive interval search visits326 nodes and finds exactly24 nonzero vectors of norm<=1, the quadratic rank is12, and the maximal minimal-basis index is3. Its interval bound is exhaustive because each next coordinate satisfies an integer-square inequality, with endpoints computed by integer square root and exact floor/ceiling. I checked the output Gram matrix against the matrix in the proof. This is exact arithmetic, not a formal proof-assistant certificate. The floating LP was used only to discover a candidate matrix. No claim about cycles, boundaries or K12 is made. Verdict PASS for the explicit chain-level counterexample.

## Archive recognition

I reread the entire final archive_generic_recognition_section.tex and the independent tripod audit. I freshly reread Mochizuki Theorems A and B on author pages3–4, including the full profinite groups and arithmetic base requirements. The previous root whole-proof check stands. The theorem determines the subset only with the stated full marked generic arithmetic diagram; no effective finite-quotient decision or reconstruction of an omitted marking is asserted.

## Explicit cycle extension

I read all of k12_survivor_boundary_section.tex and all of its standalone certificate, then reran the program successfully. Each deleted-ray facet is full rank; the displayed integral functional has values1 and minus epsilon on exactly the two swapped representatives and zero on all others. Thus g=I+(epsilon v_k-v_j)phi is an integral involution and a genuine orientation reverser on that facet. All twelve facet terms vanish individually. In the rank-ten orthogonal extension the same involutions extend, while the final facet is rank deficient and lies in the relative boundary. The two nonzero orientation generators are cycles, without a nonboundary claim. PASS.

## Explicit coface boundaries

I read the entire final coface TeX and standalone program, then reran the latter. The final denominator720 form has positive rational LDL pivots and exactly26 signed minimum vectors in388 exhaustive search nodes; its quadratic rank is13. Every old facet reflection fixes w=e8+e9, so exactly one facet has a surviving orientation generator. Integral equivalence preserves the property of having an odd stabilizer, which forces every coface stabilizer to fix that unique facet and its complementary ray. It is therefore orientation preserving. I freshly read DEKM section1.2.1 equations(1)-(2) and its spectral-sequence convention: incidence is the sum over actual equivalent facets. The unique surviving facet contributes one incidence of sign plus/minus1, with no target-stabilizer factor; chosen orientation makes it plus1. The orthogonal extension has exactly one more relative-boundary facet and the same unique surviving full-rank facet. Thus both explicit cycles are boundaries. PASS; no whole homology or K12 vanishing asserted.
