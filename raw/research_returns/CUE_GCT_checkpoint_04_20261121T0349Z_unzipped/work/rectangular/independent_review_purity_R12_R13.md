# Independent targeted whole-proof review: R-12 and R-13

Reviewer: GPT-6 Astra Pro, `/root/purity_zero_status`; effort not exposed. Run CUE_GCT-20261121-purity.

Read both complete theorem statements and proofs in `work/rectangular/findings.tex`, the full certificate specifications, `check_permanent_projection.py`, `check_permanent_range.cpp`, `check_permanent_range_ryser.cpp`, and `check_permanent_range_minors.py`. Inspected the certificate manifests and saved cross-check records. A separate metadata consistency pass checked generators, point order, byte lengths, checksums, selected-column counts, and agreement with every residue in the theorem. It did **not** recompute permanent matrices or determinants. Results are in `independent_review_purity_R12_R13_metadata.json`.

## Outcome

Both mathematical proofs and the specified certificate algorithms pass this targeted review. The positive finite-range statements depend on the supplied finite exact certificates and their recorded computations. This review does not turn those records into a formal proof-assistant verification or claim a new independent run of the matrices.

## R-12

Differentiation with respect to a matrix entry produces its complementary permanent without a cofactor sign; differentiation with respect to the k-th linear-form coefficient supplies x_k. The coefficient-Jacobian orientation and zero-based parameter indexing match the script. The quartic and quintic displayed column lists have respectively 35 and 56 entries and agree with their manifests. The stored quartic integer determinant equals the integer printed in the theorem and has residue77 modulo101; the stored quintic residue is30. The recorded finite-difference column counts are64 and12.

The complementary-permanent coefficient code enumerates permutations and multiplies linear forms exactly over Z. Its determinant routines use exact modular elimination and fraction-free Bareiss updates with exact-division assertions. Each individual pencil parameter occurs with exponent at most one, so the unit finite difference is exactly the derivative, with no Taylor remainder.

A nonzero reduction of a square integer minor proves its nonvanishing over Q and C. Fixing the remaining source coordinates gives a square map with invertible complex differential. The inverse function theorem supplies a nonempty analytic open image; a complex polynomial vanishing there is identically zero, giving the asserted Zariski dominance.

Every pencil is a linear substitution into the original permanent. Density of invertible substitutions places it in the GL orbit closure, and dominance then places the full four-variable coefficient subspace there. For the paper's coordinate convention, all coefficient-generator torus weights are nonnegative. A weight λ with zero entries beyond coordinate4 can therefore use only first-four-variable coefficient functions. Its restriction to that subspace is faithful. Hence a highest-weight polynomial of this weight in the orbit ideal must be zero. Complete reducibility is used only in characteristic zero to convert this ideal statement to the ambient multiplicity equality.

Subtracting G-07 gives the stated deficit. For d=D+s and λ=(D+4s,D,D,D), the shifted partition is (4s), of multiplicity one in Sym^s(Sym^4 V); the displayed one-dimensional highest-weight space verifies this also at s=0. For n=5, the determinant-image dimension bound52<56 gives an equation, while ternary saturation excludes all weights of length≤3. The conclusion is an exactly-four-row multiplicity obstruction, without an asserted occurrence obstruction or specified degree.

## R-13: finite positive certificates

The evaluation-Jacobian E is the coefficient differential followed by a linear evaluation map. Full row rank b_n therefore forces the coefficient differential to have rank b_n; no unproved interpolation invertibility is needed for this implication. Lifting the nonzero integer evaluation minor to characteristic zero suffices for the same dominance argument.

The primary subset recurrence correctly assigns row |S| and the columns S. Since S\{j}<S as integers, the forward pass respects every dependency. Reverse traversal computes the formal derivative of this arithmetic circuit, yielding all complementary permanents in O(n2^n) operations. All intermediate integer bounds fit the specified types for n≤16; gradient sums use uint64 and modular row arithmetic remains bounded. The uint32 linear-congruential update has the intended modulo2^32 semantics.

The Ryser identity is proved by inclusion–exclusion on the image of a map [n]→[n]. The second program uses this different identity, Gray-code updates of row sums, prefix/suffix products that remain valid at zero row sums, and a reverse derivative sweep of those updates. The sign parity n+|S| equals n−|S| modulo2. It shares the specified point/generator conventions but not the subset-permanent recurrence. This matches the claimed scope of algorithmic independence.

The normalized-row rectangular Gaussian elimination selects the left-to-right independent columns. Row swaps, pivot products, and scaling factors produce the determinant of the original selected square minor. The Python recheck uses unnormalized pivot rows on the already-selected square matrices and bounded int64 arithmetic. This is a second determinant algorithm as claimed.

The metadata pass checked all16 generator seeds and confirmed attempt0; every pencil and decreasing-lexicographic point list agrees with the mathematical specification. All matrix-byte checksums agree with the saved determinant recheck records, all16 residues agree with the theorem, and the matrix sizes sum to3,348,864 entries, as stated. The saved Ryser records assert comparison of exactly those entry counts.

## R-13: negative range and multiplicities

The row/column scaling torus has dimension2n−1. On the dense open set of pencils with all entries nonzero, its stabilizer is exactly the one-dimensional subgroup (t,…,t,t⁻¹,…,t⁻¹). Thus generic fibers contain orbits of dimension2n−2, giving image dimension at most4n²−2n+2. At n=17 this is1124<1140. For n≥18 the stated positive difference can be written n²(n−18)+23n−6, so its sign is immediate. This proves non-dominance for every n≥17.

The positive table includes n=1 correctly, but the coordinate-ring conclusion is restricted to n≥2 so that n²≥4. Its highest-weight argument then matches R-12. For4≤n≤16, the determinant has an exactly-four-row equation by G-05/G-06 while the permanent retains the ambient four-row sector. This is precisely the finite-range multiplicity conclusion stated; it gives neither an asymptotic separation nor the comparison between proper four-variable images for n≥17.
