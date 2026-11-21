# Independent complete review of MA-MO-020

Date: 2026-11-21, UTC. Reviewer: GPT-6 Astra Pro, `/root/s5_audit`; effort inherited/not externally exposed.

## Result

**PASS.** I independently read the complete 308-line `polar_quotient_rank.tex`, MA-MO.400–415, including all proof sections and the final source/scope paragraphs. Reviewed SHA256: `f2b5cd46987c3cfe62117bc475c506249d354f4078955cb175122bf737fe115a`. No mathematical correction was requested.

The theorem proves exact rank two for the outgoing positive-source map under MO018's explicit half-plane hypothesis. It retains every zero multiplicity. It does not claim that the raw matrix induces a quotient endomorphism, or rule out the different relative operator used in MO021.

## Checks performed

1. **Source signs.** I rederived both formulas in MO.404 from the original theta Poisson identity and the Fourier interchange of the Gaussian sections. The left Poisson tails cancel, so both `r_j` belong to E. The sign is plus for `phi exp(x/2)` in `r_0`, and minus for `phi exp(-x/2)` in `r_1`.

2. **Gaussian Mellin transforms.** Writing `w=1/2+z`, the Gaussian integral gives `Gamma_R(w)`, while the term `2 pi t^2` gives `w Gamma_R(w)` by gamma recurrence. Hence the two factors are `1/2-z` and `1/2+z` exactly as in MO.406. Their moments at `z=1/2` are zero and one. The continuation starts on an absolutely convergent wide line.

3. **Both residue cancellations.** Integration by parts gives the negative sign in the transform of the left step. This produces both signs in MO.407. At `z=1/2`, the second formula's zeta residue +1 cancels the residue -1 from `P(0)=-1`. At `z=-1/2`, the first gamma/zeta term has residue -1, and its step term has residue +1. The equations at the two endpoints in MO.408 concern the entire cleared numerator, so they do not evaluate singular fractions. They give `E_c(1/2)=-c_1` and `E_c(-1/2)=-c_0`, proving nontriviality for every nonzero coefficient vector.

4. **Every retained jet.** The half-plane hypothesis and functional reflection place the whole nontrivial divisor in a uniformly interior strip. The actual weighted closure theorem therefore retains every jet for every `s>=0`. At each zero, the gamma terms in MO.407 are holomorphic and their products with zeta vanish to at least the full zero order. Subtracting these terms and multiplying by `z^2-1/4`, a unit in that local jet ring, proves MO.410 with the full multiplicity. Zeros of G may contribute to this order, but are fully counted in the following Jensen argument.

5. **Exponential-type count.** Compact support of g and `phi'` gives the displayed entire growth bound for `G E_c`. Fourier uniqueness and the endpoint values make this function nonzero when g and c are nonzero. Jensen on a disk centered at a nonzero value gives `n(r)=O(r)`, including multiplicities. All nontrivial centered zeta zeros of height at most T lie in a disk of radius `T+O(1)`, so MO.410 would imply a full divisor count `O(T)`.

6. **Hadamard contradiction.** I freshly reread the complete order-bound and constant-normalization argument at MA-RB.8–10, then checked its rational version in MO.413–415. The completion is entire of order at most one and has no endpoint zeros. Under the hypothetical linear count all required real-part sums converge absolutely. Differentiating the functional equation at zero and one gives `-B=B+2S`, hence cancels the real Hadamard constant exactly. The summand bound and the dyadic shell computation make the positive real-axis zero sum uniformly bounded. Conversely the logarithmic derivative of the completed formula has the displayed gamma term. Jensen for the reciprocal Gamma-distributed random variable gives `psi(x)>=log(x-1)` with the correct inequality direction; the Euler logarithmic derivative tends to zero. The two bounds contradict one another. No estimate for the number of distinct zeros is substituted for the multiplicity count, and no numerical Riemann–von Mangoldt bound is needed.

7. **Rank and minimal correction.** The previously proved outgoing formula is the negative of the injective two-column map, applied to the actual polar coordinates. Its rank is therefore exactly two. Any correction with range quotient equal to that map has rank at least two. Orthogonal projection to `W_+`'s complement identifies that complement isometrically with H/J, so the proposed correction has rank exactly two and attains the lower bound. Its subtraction changes the original source map.

## Source scope

The proof's analytic counting contradiction is supplied in full. I checked its actual imported order/Hadamard argument in `s5_real_zero_free.tex`, MA-RB.8–10, and its source/moment interfaces against my immediately preceding complete MO016/MO018 reviews. I did not independently audit the corroborative Hasanalizade–Shen–Wong numerical zero-count theorem; the module explicitly does not use that estimate. No new arithmetic zero-location input was introduced by this review.
