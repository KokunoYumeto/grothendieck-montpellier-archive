# Fourier argument for the S5 central equality

Date: 21 November 2026. Author of MA-FQ-001: `/root/s5_audit`, GPT-6 Astra Pro; effort inherited/not externally exposed. Root owns MA-FQ-003/004, and pf26_audit owns MA-FQ-002.

## Result and exact scope

MA-FQ-004 proves `β=b+n` in Calegari's stipulated family under exactly `(R_B)`, the absence of real zeros of B in `(0,1)` away from `1/2`. This closes the positive central-excess branch of MT-S508. The proof does not establish `(R_B)` for every field. M supplies `(R_B)` and, separately, the Hecke zero-location statements that give all-factor GRH after Artin holomorphy. A alone supplies neither general Hecke premise.

## Four complete proofs

1. `s5_crystal.tex`, **MA-FQ-001**: the exact archimedean parameter is `1³⊕sgn²` for both the automorphic comparison and W, so the difference datum has `K_R=0`. Its actual signed critical-line divisor is an integer, locally finite, tempered measure μ. In the plus-sign Fourier convention, `F(−μ)=M_Ω+B0`, where `M_Ω` is positive and `B0` has finite total variation. Add `q(t)dt`, with `q(t)=−(2π)⁻¹∫exp(−itx)dB0(x)`, to remove the correction. Shrinking convolution squares isolate the atomic coefficients, proving that `a(t)=−m_R(t)` is positive definite on `R_discrete`. Consequently `|a(t)|≤k`, and the explicit GNS/Riesz argument gives `a∈B(R_discrete)` with norm k.
2. `s5_coset.tex`, **MA-FQ-002**: Cohen's integer-valued finite-coset representation, together with the completely proved dense-intersection argument, turns an ordinary locally finite support into a finite integer combination of lattice-coset and singleton indicators. Uniform separation is never assumed.
3. `s5_crystal_rigidity.tex`, **MA-FQ-003**: ordinary Poisson summation turns those physical combs into modulated combs supported on finitely many unshifted frequency lattices. Singleton terms give a continuous trigonometric density, which vanishes because the actual Fourier transform is purely atomic. Each frequency lattice contains `log p` for at most one rational prime.
4. The same file, **MA-FQ-004**: each `p∈Ω` gives an uncancelled atom of mass `4 log p/√p` at `log p`. Hence Ω is finite, and the audited S508 criterion forces `k=0`.

## Normalizations independently checked

- The Fourier transform is `Fν(x)=∫exp(itx)ν(dt)`, with inverse factor `(2π)⁻¹` and negative exponent.
- Booker A4 includes n=1 under its minus sum. Thus the conductor atom in `F(−μ)` is **+2 f_R(1) δ0**. This sign was checked on the actual p.3 image, and root corrected a recalled convention before the proof was assembled.
- Bad-prime absolute summability follows from Booker A1 with log power2. No sign assumption or extra all-place transfer hypothesis is used there.
- Bump scaling `φ_ε(t)=ε⁻¹ᐟ²φ(t/ε)` gives autocorrelation `Ψ(t/ε)` of fixed height. The bounded continuous density contributes `O(ε)` at each of finitely many differences; each atom contributes its full mass times `Ψ(0)`.
- Positive definiteness is on `R_discrete`. Its compact-dual representing measure is not identified with the ordinary real Fourier transform of the atomic divisor.
- Physical translation modulates Poisson-comb weights; it does not shift the frequency lattice.

## Source and check boundaries

Calegari (2013), author-hosted publisher PDF p.4 character table, p.8 Lemma3.2 and its preceding oddness paragraph, pp.8–9 opening section4, supplies the specified descent. The exact needed paragraphs and the attached LaTeX were read. Deep modularity and transfer inputs remain Calegari's cited classical results.

Booker (2015), arXiv1308.3067v2, Definition1.3(A1),(A3),(A4), p.3, and Examples1.4(2)–(3), p.4, supply the actual data. The complete relevant continuation/functional-equation proof had already been checked for MA-LD-001. The actual p.3 image was inspected to settle the conductor convention.

Sanders (2020), section12, Theorems12.1/12.3 and definition12.2, gives the required qualitative Cohen consequence. This agent read the precise definitions, theorems and entire printed terminal proof of12.3. Its deep classical idempotent input is cited, not claimed re-proved. PF26 separately read Schreiber (1970), Lemma1.4, Corollary1.5 and Example1.6, pp.807–808, and Kolountzakis arXiv math/9904065v1 section3.2 pp.7–8, including their complete relevant proofs. MA-FQ-002 includes a full independent proof of the real-line coset reduction actually needed.

No theorem requiring uniformly discrete physical support and uniformly discrete spectrum was applied. General signed Fourier quasicrystals need not be periodic; the integer-valued positive-definite coefficient function is the additional structure used here.

## Independent review record

Root, input_audit and pf26_audit each independently read the entire MA-FQ-001 proof and reported passes. This agent independently read the complete MA-FQ-002, MA-FQ-003 and MA-FQ-004 proofs, with actual review events in `s5_crystal_s5_review_events.tsv`. Root also read all four complete proofs and authorized promotion on 21 November 2026. The proof and source events remain distinct from numerical tests, formal certificates, and author self-checks.

The Artin-motive interpretation and exact inherited SGA1/Deligne placements are stated in the MA-FQ-004 scope paragraph and in the original `s5.tex` motive paragraph. The new harmonic-analysis argument closes the central equality for those actual finite-monodromy motives under `(R_B)`; it does not construct a faithful positive operator on their full zero-jet spaces.
