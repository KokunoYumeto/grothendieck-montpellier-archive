# Independent targeted whole-proof review: R-16

Reviewer: GPT-6 Astra Pro, `/root/purity_zero_status`; effort not exposed. Run CUE_GCT-20261121-purity.

Read every statement and proof paragraph of `work/rectangular/r16_fragment.tex`, including the simultaneous perturbation, Fourier calculation, Schur specialization, rank-continuation step, and padding consequences. The proof passes this independent targeted review. No new Jacobian matrices were computed. The effective-threshold reference to G-10 is a dependency of the text and was not newly reviewed in this record.

## Local factorization and base matching

The chosen row pairs are disjoint because h_m≤floor(m/2). The last pair may use wrapped column index zero without changing its three-column support. Neither added entry coincides with a diagonal or forward-cycle entry for m≥4. Every other perturbation changes different rows.

For each of the three cofactor choices, deleting one of those three columns leaves exactly two available columns for the two paired rows. Both must be used by the pair, so all other rows match only outside the triple. This gives the displayed common complementary permanent factor, with no restriction on the other perturbed row pairs. The three two-by-two permanents produce the exact difference −2p_a v_a q_a R, hence −2ε²ℓ_a v_a v_{a+2}R.

At zero, deleting the three specified rows and columns forces the forward-cycle matching on rows a+2,…,a+k−1 and the diagonal matching outside [a,a+k]. This verifies the formula for R and T, including k=2 and k=m−2. It has the claimed bidegree (m−k,k).

## The base differential space

A cofactor contributing to bidegree (m−k,k) contains either k−1 cycle factors and is multiplied by z or w, or k cycle factors and is multiplied by an x,y linear form. In the latter case decomposition in the independent pair ℓ_a,ℓ_{a+k} gives the two adjacent F terms exactly. Thus the displayed span exhausts the bidegree component. The endpoint binary dimensions and the 2m generators in each middle bidegree bound the total dimension above by 2m²+2, matching R-15's lower bound. This justifies choosing a basis of precisely that size later.

The cyclic substitution sends F_{a,k} and T_{a,k} to the next indexed polynomial. For wF, the additional scalar from τ(w)=ζw does not affect the orbit span; each character component of W₀ is spanned by the two projected generators used in the calculation.

## Fourier coefficient obstruction

The finite geometric-product expression for A_r has no zero numerator or denominator: all its exponents are integers from one through m−1. Thus division by every displayed A_{t−s} is legitimate. The x,y factor of T₀,k is A(x,ζy), with roots k+1,…,m−1,0. Shifting the second variable of its z,w factor by ζ⁻¹ gives exactly (z−ζ⁻¹w)(z−ζw)E. Its difference from (z−w)B is (2−ζ−ζ⁻¹)zwE, whose scalar is nonzero.

For 2≤t≤m−2, a monomial in character t has r+s=t; the alternative t+m exceeds the total degree m. For 2≤k≤m−2, the permitted interval of s contains at least three indices, equivalently min(k,m−k,t,m−t)+1≥3. The coefficient vectors of T, zF, wF are therefore exactly the stated vectors up to the nonzero common character scalar. Membership would force E_{s−1} into the fixed span of B_s and B_{s−1}.

On three consecutive indices, the substitutions B_s=E_s−E_{s−1} and B_{s−1}=E_{s−1}−E_{s−2} are an invertible change among the three columns. They reduce the obstruction to det(E_{j+u−v}) with 0≤j≤k−2. After row/column signs, transposing this determinant gives the dual Jacobi–Trudi matrix for λ=(3^j), since λ′=(j,j,j). No partition-orientation correction is needed.

Write N=k−2. For N=0 the determinant is one. Otherwise the numerator of the Weyl alternant at (1,ζ,…,ζ^{N−1}) is a Vandermonde in ζ^{λ_i+N−i}. Its exponents are distinct and lie in [0,N+2]=[0,k], with k<m. They are distinct modulo m, so that Vandermonde is nonzero. The denominator is nonzero for the same reason. Scaling all variables by ζ adds only ζ^{3j}. This establishes the nonvanishing of the Schur value, including j=0 and j=N, and proves the character obstruction.

## Simultaneous independence and consequences

If a linear combination of the h_m translates lies in W₀, each obstructed character gives the scalar relation Σ_a u_a ζ^{at}=0. The consecutive characters 2,…,h_m+1 are available because h_m≤m−3. Their coefficient matrix is a Vandermonde in the distinct ζ^a, with invertible column scalings. Hence all coefficients vanish. Different k have distinct bidegrees, and W₀ is bigraded, so the full h_m(m−3) collection is independent modulo W₀.

Appending their polynomial continuations to a base Jacobian basis gives a coefficient minor nonzero at zero. For generic nonzero ε it remains nonzero while every appended vector belongs to the same perturbed differential image. This legitimately adds the directions at one pencil, rather than summing ranks from unrelated perturbations. The resulting dimension lower bound and the strict padded-image comparison have the stated directions.

At n=m+1 the criterion reduces to F_m≥4m. The lower bound (m−1)(m−3)/2≥4m holds for m≥12. The earlier finite ranges cover m=8,9,10,11. Finally F_m=m²/2+O(m), so the limiting squared padding ratio is 5/4 and the strict range 1<ρ<√5/2 follows. These statements concern multiplicity gaps, not an identified partition or an effective search algorithm.

An immediate checked endpoint consequence is c₅≥52+4=56, the full quaternary quintic dimension; thus this algebraic proof also recovers quintic dominance. At m=4 it similarly gives 34+1=35. No extra finite computation is needed for either endpoint.
