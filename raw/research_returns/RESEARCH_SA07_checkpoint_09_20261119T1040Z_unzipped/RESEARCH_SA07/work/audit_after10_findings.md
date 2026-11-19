# After10: exact two-pair partial tangency in genus three

**F.3.28 is integrated and independently audited.** It proves that the actual universal degree-six quotient vanishes for a special genus-three derivation tangent to four specified basis lines spanning two symplectic pairs. Both complementary generators remain present, and all mixed degree-one Johnson brackets enter the trace equations.

The proof uses the original universal quotient sequence of Nakamura (1996), (4.7.1), p.117, to put the actual degree-six Johnson image inside the kernel. After choosing a basis of the verified one-dimensional quotient, complete reducibility extends its invariant functional to the entire special-derivation space and then to the eighth tensor power of homology. The exact all-genus surjectivity of Morita–Sakasai–Suzuki v2, Proposition 2.1, p.8, expresses that functional through the 105 symplectic contractions. The stable-range bijectivity assertion is not used in genus three.

The finite certificate constructs all 15 balanced specialness blocks. Modular rank lower bounds are matched by independent integer kernel lifts checked against the original integer matrices. The partial-tangent space therefore has exact rational dimension 31. Its complete mixed ES7 matrix has 3920 rows and 31 columns, rank 15, and 16 independent integer kernel vectors.

Every contraction vector of that entire kernel is an exact rational combination of two actual geometric brackets, written right-nested:

1. `[δ_cdf, δ_cef, δ_aef, δ_def, δ_bef, δ_cde]`.
2. `[δ_bce, δ_adf, δ_adf, δ_abd, δ_bce, δ_abc]`.

The contraction minor on `(12)(34)(56)(78)` and `(12)(36)(47)(58)` is `[[−104,−288],[32,192]]`, determinant `−10752`. The program clears that denominator and verifies every coordinate of all 16 identities over the integers. This proves vanishing of every invariant extension of the actual quotient; it does not invoke a map to a smaller arithmetic curve quotient. The later torus projector gives the unrestricted-weight statement. The rational argument applies at every prime.

The final certificate and output are in `output/RESEARCH_SA07/code/check_genus_three_two_pair_partial.py` and `.output.txt`. Agent runtime: 5.903965459 seconds. Root independent rerun: 6.337165875 seconds, exit 0. Elliptic independent rerun: 8.859784069 seconds, exit 0. Both independent reviewers checked the exact MSS source locator and invariant-extension proof. Root handles canonical computation-registry insertion.

The after10 record files contain 10 canonical check events and 2 source-check rows, with no new bibliography key. Existing source keys are `AuditMoritaSakasaiSuzuki2015v2` and `AuditNakamura1996`. The 307-assertion, 154-entry inventory keeps all statuses unchanged. Only `I.B05.01`, `I.B05.02`, and `II.MB15.02` receive stronger dependencies and an explicit retained scope obligation.

## Work-only next steps

The all-genus proper-summand statement has not been proved. Averaging over the symplectic group of the complement preserves the actual universal image, its quotient, and the specified partial tangencies. Its mixed trace equations still require an exact calculation; the outside-handle cancellation in the full-tangency theorem does not apply without its tangency hypothesis.

With only one paired handle constrained in genus three, the modular discovery space has dimension 180, trace-kernel dimension 133, and contraction-image dimension 3. Two explicit degree-six Johnson brackets account for dimension 2. Adding the two explicit proper-filling spiders from MSS still leaves an additional direction in the modular test: the geometric-plus-filling contraction image has rank 4, and adjoining the one-pair trace-kernel image gives rank 5. These are work-only diagnostics. No arithmetic realization or nonzero actual q6 value has been inferred from them.

The full LM6 A.22 gate remains the actual arbitrary detecting-cover CM quotient and its normalizer constraints. This genus-three partial result is not recorded as a resolution of that gate.
