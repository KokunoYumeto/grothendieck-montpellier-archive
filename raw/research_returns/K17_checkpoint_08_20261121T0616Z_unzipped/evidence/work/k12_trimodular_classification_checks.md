# Restricted trimodular classification: exact scope and checks

Reviewer and author: GPT-6 Astra Pro, `/root/tripod_integral`, 2026-11-21. The clean proof and complete standalone certificate were read in full, the proof was reconstructed independently of the implementation, and the exact certificate was executed successfully. This is a self-check; independent review was requested from the parent and sibling reviewer.

## Statement actually established

`K17-K12-TRIMODULAR-GENERATED` concerns rank-ten projective degree-twelve Voronoi cells whose minimum vectors generate the ambient lattice and whose largest minimum-basis index is at most three. Their orientation generators are either zero or the previously certified generator sigma. The latter has a certified incoming boundary with coefficient one. This removes the whole stated class of generators, not the entire degree-twelve chain group.

The remaining representative support is maximal basis index at least four, or maximal index three with minima generating a proper index-three sublattice. No homology-vanishing conclusion is asserted for those remaining cells.

## Integral normalization and descent

The map V from Z^13 to the rank-ten ambient lattice is surjective by hypothesis. A row basis B of its rank-three kernel is primitive. Complementary maximal minors of V and B are proportional over Q. Both complete Plucker vectors have gcd one: for V by surjectivity, and for B by saturation of its row lattice. Consequently their proportionality scalar is plus or minus one. This verifies the maximal-index translation without assuming a unit minor exists in the original minimum set.

A signed permutation preserving the relation lattice descends to an integral automorphism of its quotient. This applies both to repeated Gale-column transpositions and to the third-record symmetry. The low-excess simpliciality result supplies independent quadratic rays, so the sign of the induced permutation is exactly the orientation sign.

One zero Gale column splits off an integral rank-one summand because the minima generate the ambient lattice. Any putative extra minimum in the rank-nine core would be an extra ambient minimum. Thus the first-record quadratic contradiction applies even if the original positive form has nonzero cross terms with the coloop.

## Primary completeness input

Averkov and Schymura, *On the maximal number of columns of a Delta-modular integer matrix: bounds and computations*, Mathematical Programming 206 (2024), 61-89, DOI https://doi.org/10.1007/s10107-023-01964-2.

The final published text is archived at `work/k12_source_data/averkov_schymura_2024.pdf` and `.txt`. The definitions on printed pages 62-63, all of the relevant classification construction in Section 5.1 on pages 82-84, and Section 5.2 with Tables 1-3 on page 85 were read. Table 1 gives h(1,3)=13, h(2,3)=19, h(3,3)=25. Table 3 gives exactly three extremal equivalence classes for (Delta,m)=(3,3). Table 2 separately records 102 total classes at those parameters. The input is the published complete classification, not a fresh rerun of the entire classification algorithm.

The primary arXiv version is https://arxiv.org/pdf/2111.06294, v2, retrieved as `turn347355058view1`; Tables 1 and 3 are on PDF pages 22 and 23, respectively, and the full algorithm appears on page 21. Fresh searches within that source returned `turn498826685view1` and `turn498826685view2`. The arXiv and final journal pagination differ, and the TeX uses the final journal locator.

The official author repository https://github.com/mschymura/delta-classification was retrieved as `turn419649733view1`. Its README identifies the data as all extremal examples, and the article itself points to this repository. The exact three-record file is https://raw.githubusercontent.com/mschymura/delta-classification/main/data/dim_3_delta_3_extremal.txt. Its archived copy has SHA256 `4afa2c6665f6608ef914b47739609469007e1a3737eb4ad154cfba4397ff5db4`. A fresh browser retrieval of the raw URL and the GitHub blob URL was disabled (`turn347355058view0`, `turn498826685view0`); the already archived complete data were read directly. No success is claimed for those two later retrieval attempts.

The determinant maximum on the convex hull is attained at vertex tuples by multilinearity, applied one variable at a time. Thus all lattice points of that hull can be adjoined without increasing the determinant bound. A 25-point signed set is necessarily an extremizer. An affine unimodular equivalence of two such origin-symmetric polytopes has zero translation, since their unique centers are zero. Therefore the published equivalences are valid changes of integral Gale basis. Nonprimitive columns are allowed in the source definition and in the proof.

## Exact per-record verification

`work/k12_trimodular_classification_certificate.py` is standalone standard-library Python. Its literal vertex records agree with the complete archived author data. It computes all supporting facets from triples, enumerates every lattice point in each coordinate bounding box using exact integer inequalities, and checks that each record has exactly the 25 stated points. Every three-column minor is checked, with maximum three and a unit minor in each model.

The first record is reconstructed from a unit minor into its nine-dimensional quotient. All six auxiliary vectors are nonzero, distinct up to sign and outside the twelve proposed minimum pairs. All 81 entries of the displayed quadratic identity are verified exactly. The identity makes the sum of their six norms equal six if the proposed minima have norm one, contradicting completeness of that proposed set.

The second reconstruction is checked to agree exactly with all twelve vectors of the earlier independently certified tau model. Its rank-ten coloop join is sigma and hence has the already certified filling.

For the third record, the displayed integral matrix has determinant one, preserves the signed column set and induces exactly three transpositions. Its quotient automorphism reverses orientation. No numerical stabilizer guess is used.

The final verifier execution returned three records checked, first record impossible, second record tau, third record odd, and `classification_coverage_recomputed: false`.

## Readback and hashes

The complete 264-line final TeX and complete 111-line verifier were read in full after the affine-equivalence clarification. SHA256:

- TeX: `49346606a0ebf0052db62cf8bcd5e12bddc6db5215ea27b5ae8ef91d6cfa82f9`.
- Verifier: `961b4ffd56f8141a5921cbaf374221915e3a49ac5903b11fdd1755026f57b6a0`.
- JSON: `65b00a58b2ecc287b6b92c0ed39906bedc293545e958d4b3f9b11eda393bb375`.

The fixed-coface lemma in the same TeX retains an explicit complete-minimum-set hypothesis. Common fixed rays alone are not claimed to produce a coface. Its incidence-one conclusion uses a unique actual surviving facet, as in the independently audited coface certificate.

## Previously completed coface review

The parent and archive reviewer separately reported full PASS for `work/k12_survivor_coface_section.tex`. The complete final `work/k12_survivor_coface_archive_audit.md` was read again during this classification check. Its exact rerun gives 388 nodes, thirteen minimum pairs, quadratic rank thirteen, all twelve reflections fixing the new ray, and both boundary coefficients one. The review is scoped to those two boundary identities and does not claim a complete homology computation.
