# Independent targeted whole-proof review: R-14 and R-15

Reviewer: GPT-6 Astra Pro, `/root/purity_zero_status`; effort not exposed. Run CUE_GCT-20261121-purity.

Read the complete statements, proofs, endpoint discussions, and limitations of R-14 and R-15 in `work/rectangular/findings.tex`. Both proofs pass the targeted mathematical review below. No permanent or Jacobian computations were rerun for this review; these two proofs are algebraic rather than dependent on an unverified extrapolation of the finite certificate table. R-14 uses the earlier table only for its listed numerical instantiations. This is not a formal verification or a full independent literature audit.

## R-14: dimension under padding

The permanent pencil with diagonal x₁ and one cyclic off-diagonal chain has exactly two perfect matchings and computes x₁^m+x₂^{m−1}x₃. Eisenstein at x₃ over C[x₂,x₃], followed by Gauss's lemma, proves irreducibility for m≥2. The reducible homogeneous forms form a finite union of projective multiplication images, hence a closed set. Therefore the general member of the irreducible image cone is irreducible.

The projective multiplication map P³×P(P_{m,4})→P(Symⁿ C⁴)* is everywhere defined: the product of two nonzero polynomials is nonzero. Properness makes its image closed. Its affine cone is exactly the displayed set {ℓ^{n−m}q}, including zero, because the q-cone absorbs arbitrary nonzero scalar multiples. For a general irreducible q of degree at least two, the product has a unique linear factor up to scalar; this determines [ℓ] and then [q]. The map is therefore generically injective, giving projective dimension 3+c_m−1 and affine dimension c_m+3.

Every projected orbit point belongs to this closed image. Conversely the padding linear form and every permanent-entry linear form can be specified simultaneously because the original padding variable is independent and m²+1≤n². Such endomorphism substitutions lie in the orbit closure by density of invertible endomorphisms. Passing to the closure of permanent pencils proves equality of the projected image, not merely a dimension comparison of an auxiliary family.

Both coordinate rings are standard graded. The strict affine dimension inequality gives strict Hilbert-function inequality in every sufficiently large degree because the eventual Hilbert polynomials have degrees one less than the affine dimensions and positive leading coefficients. Decomposing the GL₄ degree-d modules, a strict total dimension inequality forces at least one strict multiplicity inequality. Highest-weight vectors supported in the first four coordinates identify these with the corresponding GL_{n²} multiplicities: the ideal intersection is the projected-image ideal, and the raising operators involving later coordinates annihilate such vectors. This uses the positive polynomial coordinate-weight convention already fixed in the manuscript. The determinant's ambient multiplicities for at most three rows force the strict difference to have exactly four rows.

The arithmetic simplification c_m+3>2n²+2 ⇔ 2n²≤c_m is valid because both quantities are integers. The listed ranges for m=8,…,16 agree with floor(sqrt(binom(m+3,3)/2)); m=4,…,7 yield no n>m. The block-diagonal identity places the padded permanent in the equal-size permanent orbit closure, so the direction of the coordinate quotient and multiplicity inequality is correct. No effective coordinate-degree threshold or asymptotic growing-size separation is inferred.

## R-15: the cyclic base pencil

After deleting row i and column j, the diagonal-plus-cycle graph has the unique matching specified by the cyclic interval from j through i−1. Thus the displayed cofactor product is exact for every pair i,j.

On Λᵢ, all cofactors from any other row vanish because their product contains either ℓᵢ or vᵢ. Row-i cofactors restrict to nonzero multiples of u^{n−1−k}v^k for all k; the distinct a-values and b-values guarantee each scalar is nonzero. Multiplication by y or w spans all degree-n binary monomials. Since each such generator vanishes on every other Λ, the restriction to the direct sum of n line-section spaces is genuinely surjective, giving n(n+1) independent image dimensions.

Each Q_I is in the Jacobian span and vanishes on every Λ. For a fixed proper nonempty interval length k, restriction to Θ_t kills every interval except the unique interval ending at t: survival is equivalent to t∈I and t+1∉I. That surviving restriction is nonzero. This proves independence of the n interval products at each length. Different lengths have distinct bidegrees, and the two endpoint products occupy the endpoint bidegrees. The kernel therefore contributes n(n−1)+2 independent vectors. Adding image and kernel dimensions proves the lower bound 2n²+2 without assuming independence across an arbitrarily selected collection of all cofactors.

## R-15: the missing bidegree vector

A generator in bidegree (n−2,2) can arise only by multiplying a length-one cofactor by z or w, or a length-two cofactor by x or y. In the second case ℓᵢ and ℓᵢ₊₂ are independent for n≥4, so expressing the multiplier in their basis decomposes the rational expression into the two adjacent edge terms. Hence the edge-space formula is exhaustive.

On y=w=1, each edge term has residues Eᵢ at aᵢ and −Eᵢ at aᵢ₊₁, where Eᵢ is a quadratic polynomial divisible by u−bᵢ. The total residues are therefore Rᵢ=Eᵢ−Eᵢ₋₁. For T/L, only the residues at a₂ and a₃ are nonzero and are opposite multiples of (u−b₁)(u−b₃). The recurrence forces all Eᵢ except E₂ to equal a common quadratic E*. Because n≥4, the indices 1,3,4 give three distinct roots of E*, so it is zero. Then E₂ is the stated nonzero multiple and is not divisible by u−b₂. This contradiction proves T is outside the entire base Jacobian image. All boundary cases at n=4 remain valid.

## R-15: the two-chord perturbation

The three complementary matching enumerations are correct. In each, rows 4,…,n are forced to their diagonal entries; the remaining two rows have precisely the two displayed possible matchings. Substituting their formulas into ℓ₁C₃₁−v₁C₃₂−pC₃₃ cancels the unperturbed terms and gives −2pv₁qR=−2ε²T. The multipliers are linear forms, so this is a vector in the full coefficient differential image. Over C, ε≠0 therefore implies T lies in that image.

Choose 2n²+2 actual Jacobian columns independent at ε=0. Together with T they remain independent there, so one augmented coefficient minor is nonzero at zero and is a nonzero polynomial in ε. For every nonzero ε outside its finite root set, T lies in the perturbed image and is independent of those perturbed columns. Thus the image rank is at least 2n²+3. Differential rank is bounded by the dimension of the polynomial map's image in characteristic zero, giving the dimension lower bound.

Each cofactor contains at most one copy of each of the two perturbed entries, so every column has ε-degree at most two. The augmented minor therefore has degree at most 2(2n²+2)=4n²+4; T has ε-degree zero. With integer choices aᵢ=i and bᵢ=i², at least one of the 4n²+5 displayed positive integers avoids all its roots. This is an existence bound for the pencil parameter, not a claim that the minor has been efficiently identified by the review.

Finally the R-14 Hilbert-function/highest-weight argument applies to the two degree-n image cones. G-06 bounds the determinant dimension by 2n²+2; G-05 excludes strict gaps of at most three rows. The claimed four-row multiplicity gap follows for every n≥4 in every sufficiently large coordinate degree. At n=4 the lower bound equals binom(7,3)=35, which gives the advertised algebraic dominance proof. The stated result remains equal-size and unpadded.
