# Independent checks of the cote 63 Hodge calculations

These are checks of questions already present on scans 66–77, not a development of a Stage 6 research proposal. They use the diplomatic text without changing its readings. Physical line locators are in the claims and readings tables.

## 1. Period convention and the two alphas

Put Λ=ω₁(Z+τZ), Im τ=y>0, ω=dz and η=℘Λ(z)dz. The periods ηᵢ are negatives of the usual zeta quasi-periods. With full periods and ω₁=1, set A=(π²/3)E₂(τ). Then η₁=−A and η₂=−τA+2πi by the Legendre relation. Solving η+αω=βω̄ gives

α=−(ω̄₁η₂−ω̄₂η₁)/(ω̄₁ω₂−ω̄₂ω₁)=π²E₂*(τ)/(3ω₁²),

where E₂*=E₂−3/(πy). The canonical second-kind class is essential: replacing η by η+cω changes α. The exact comparison source is Katz, *p-adic interpolation of real analytic Eisenstein series* (1976), §1.2–1.3, especially Lemma 1.3.6. This is a normalization comparison, not an identification of symbols by name alone.

The later real-structure coefficient a, called α again on scans 73–77, is different. Normalize the alternating pairing by using the basis (ω,η/(2πi)); then ω̄=aω+bη/(2πi), with b=−2iy and a=−πyE₂*/3. In particular a is not the earlier shift coefficient.

## 2. The zero-locus question has an elementary complete answer

**Claim.** E₂* vanishes precisely on the SL₂(Z) orbits of i and ρ=exp(2πi/3).

Work in the closed standard fundamental domain, |x|≤1/2, y≥√3/2. Write r=e^(−2πy), θ=2πx. We have r<1/200. One fully rational certificate for this numerical bound uses π>3.14, √3>1.73 and the finite Taylor sum Σₖ₌₀²⁰(27/5)^k/k!>200, so e^(π√3)>e^5.4>200. The program checks the last rational inequality exactly.

The Fourier expansion gives Im E₂*=−24Σₙ≥1 σ₁(n)rⁿ sin(nθ). The elementary bound |sin(nθ)|≤n|sin θ| and σ₁(n)≤n² show that the tail after n=1 has modulus at most

24|sin θ| Σₙ≥2 n³rⁿ.

Since Σₙ≥1 n³rⁿ=r(1+4r+r²)/(1−r)^4 and (1+4r+r²)/(1−r)^4<21/20 for r≤1/200, the tail is less than the first term whenever sin θ≠0. Thus a zero must lie on x=0 or x=±1/2.

On x=0 the real function E₂*(iy) is strictly increasing in y: the derivative of E₂ is 48πΣ nσ₁(n)rⁿ>0 and that of −3/(πy) is positive. Modularity forces E₂*(i)=0, so this is the unique zero there.

On x=1/2, the absolute value of the derivative of E₂ is at most 48πΣ n³rⁿ. Its subtraction cannot overcome 3/(πy²): y²e^(−2πy) is decreasing for y≥√3/2, and

48π² y²r·(1+4r+r²)/(1−r)^4 < 48·10·(3/800)·(21/20)=189/100<3.

Therefore E₂*(1/2+iy) is strictly increasing as well. Modularity supplies its zero at y=√3/2. The line x=−1/2 is equivalent by translation. This proves the claim, including the boundaries, without relying on a numerical grid. The zero set therefore answers the canonical α=0 question by j∈{0,1728}.

## 3. Real structure and the sign error

Let the normalized alternating form satisfy ⟨ω,y₀⟩=1. With β=−2iρ, ρ>0, a conjugate-linear involution preserving the real pairing has matrix

M=[[a,(|a|²−1)/β],[β,ā]].

Direct multiplication gives M·M̄=I and det M=1. Since σ=−(2i)^−1⟨y₀,ȳ₀⟩, one obtains 4ρσ=|a|²−1, the opposite sign to the transcribed scan 75. For the square lattice, a=0, ρ=1 and σ=−1/4 satisfy every involution/pairing hypothesis and contradict the printed identity. Hodge positivity does not say that both basis vectors have positive Hermitian square.

An independent review corrected a minus sign in the lower-right entry of the
first version of this dossier's matrix. The original nonzero residual is
preserved in `c63_hodge_initial_matrix_error.json`; the final program asserts
both the zero involution residual and determinant1. The scalar identity and
the two counterexamples are unchanged.

The claimed bound |a|≤1 also fails for an actual elliptic lattice. At τ=3i, a=−πE₂*(3i)=1−π plus an exponentially small positive correction. The tail bound |E₂(3i)−1|≤24r(1+r)/(1−r)^3, r=e^(−6π), proves |a|>2.14 and hence |a|²>1. The program records the numerical value and the exact conventions.

## 4. Lattice summation and the phase invariant

Removing the pole in the zeta series at ωᵢ gives the absolutely convergent formula ηᵢ=−3/ωᵢ+ωᵢ²Σₐ∈Λ, a≠0,ωᵢ 1/[a²(a−ωᵢ)]. The program checks finite rectangular sums against the independent Fourier formula with a rigorous, deliberately coarse tail bound. It also subtracts the handwritten rational summands symbolically: the combined τ-expression loses the factor 3 in its constant term and has two sign changes in the numerator. These are reading alarms, not authorized changes to the transcription.

The normalization ω¹²=Δ changes the phase of a by the inverse square of the chosen twelfth-root phase. Raising it to the sixth power cancels the root ambiguity. A convenient exact expression for the resulting invariant is

phase(E₂*(τ)⁶/Δ(τ)),

defined away from j=0,1728. Both numerator and denominator have weight12, so it is modular invariant. It is real analytic and generally not holomorphic. This supplies an explicit modular expression for the page’s invariant; it does not assert an algebraic expression in j alone.

## 5. Algebraicity has a separate and harder quantifier

For E and ω over Qbar, a nonrational CM endomorphism acts on algebraic de Rham cohomology with two distinct algebraic eigenvalues. Its conjugate eigenline is H⁰,¹ under comparison; the algebraic projector onto that eigenline proves the CM direction. This is Katz (1976), Lemma 4.0.7. His Question 4.0.8 asks the exact converse. A rational splitting in Betti cohomology is not interchangeable with a Qbar splitting of algebraic de Rham cohomology. This run has not proved or found an opened source proving that converse.

## 6. Reused Banach-algebra proof

For a unital Banach algebra, ||1−a||<1 gives a⁻¹=Σₙ≥0(1−a)ⁿ. If aₙ→a and sup||aₙ⁻¹||<∞, then ||1−aₙ⁻¹a||≤||aₙ⁻¹||·||aₙ−a||→0; hence aₙ⁻¹a and a are units for large n. The same estimates show openness of the unit group and continuity of inversion. If the manuscript’s symbol D means spectral radius, the alternative uses r(xy)≤r(x)r(y) for commuting x,y, plus the spectral-radius Neumann criterion. This latter reading is explicitly conditional because the preceding definition is not in the supplied fragment.
