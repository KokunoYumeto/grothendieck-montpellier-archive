# Task 1(d): character extension

## New findings

characters.tex contains MA-CH-001–004. F-SM-13 is used as the previously supplied Dirichlet numerical result and is not reproved.

- **MA-CH-001:** the finite-order imaginary quadratic formula, with one complex gamma factor, the conjugate Euler coefficient at the inverse test argument, primitive ramified local factors, vanishing conductor/discriminant terms when h(1)=0, and no polar term for a nontrivial character. The full formula is unconditional. Its exact narrow-strip defect is the sum of the excluded completed zeros. MT-M18 interpolation and MT-M30's ideal-valued norm-one restriction show that equality for every allowed test detects every excluded zero. Consequently the every-positive-width assertion requires RH for that character; M suffices. Dirichlet narrow traces use A.
- **MA-CH-002:** an ideal-indexed twisted summation embedding from compact radial tests into the actual centered theta ideal, identified using MT-M22/M24. Its Mellin multiplier is the finite L-function at z+1/2. Ideal Möbius inversion is exact on this image. Finite Euler inverses agree eventually on each compact radial subset, but an interior completed zero supplies a positive lower bound on their distance from the inverse target in the stated weighted Hilbert norm. No onto parametrization of the full theta ideal and no bounded narrow Hilbert inverse is claimed.
- **MA-CH-003:** the explicit cubic character ψ269,3 over Q(ζ3) has conductor (269), norm 269², and arithmetic conductor 3·269²=217083. At the prime above 3 the extension splits completely, so its primitive factor is retained. The prime above 269 is totally tamely ramified. The inert prime above 2 has norm 4 and splits in E/K. The local claims were independently checked by /root/pf26_audit.
- **MA-CH-004:** S0={complex place, primes above 3 and269} is admissible: the Eisenstein integer ring is norm-Euclidean and the set contains all required ramification. A test supported near4 plus an archimedean compensating bump in (1.4,1.6) has finite-S0 local functional 0 but full geometric functional log 2; its zero trace is −log 2. This is a genuine omitted-prime gap in the admissible local setup.

## Normalization and orientation

Meyer and MT-M22 normalize C_K^1 to probability Haar. In the inverse-Euler convention β(p_v)^−1=c_p, the compact projector is

    e_ξ f(g)=∫ ξ(c) f(cg) dc,

and the sector test is β(g)^−1 h(|g|). Left translation by c acts by ξ(c). This matches the actual image criterion in MT-M22; directly naming the projector by the Euler coefficient character without tracking the inverse would switch the character.

Masullo's compact volume in Definition A.3.2.1/(A.3.2.1), pp. 559–560, can differ from 1. It is a fixed scalar for theta-image membership but is not ignorable for the numerical convolution trace. The paper states the normalized convention and the corresponding rescaling of tests/operators. The S-local theorem on p. 514 already divides by local norm-one volume.

The complex local kernel was checked a second way by angular integration:

    ∫_0^{2π} |1−r exp(iθ)|^−2 dθ/(2π)=|1−r²|^−1.

With t=r² and canonical multiplicative measure, this gives A_C with no extra factor 2.

## Checks actually performed

All four new proofs were read in full by their author after drafting. The independent reader checked MA-CH-002 and 004 in full and the local refinement 003 independently. The only substantive wording correction from that review was to quantify the Hilbert annihilator statement over **nontrivial completed zeros**, not arbitrary finite-L zeros. A trivial finite-L zero cancelled by a gamma pole does not annihilate the whole theta ideal. The corrected statement is now in the paper. A typographical exponent was also repaired.

The accompanying arithmetic script checks primality, the exact 3-adic valuation inequality, the distinct F4 roots, and the numerical conductor. It is not a certificate of the analytic formula or the ideal identification.

The supplied Meyer TeX was directly read at the normalization, global trace, divisor, image criterion, and prime-distribution passages. Author-page locators for Theorems 5.8/5.11 and the image criterion are carried from the source-checked predecessor record. The added finite-prime expansion is located exactly in §6.1 immediately after Definition 6.1 rather than assigned an unverified new page number. An attempted source regeneration with the visible pdflatex binary failed before parsing because pdflatex.fmt was unavailable; this was not a characters.tex compilation result. Root owns the final build.

## Remaining gate

The new prime-carrying subspace and exact finite-S discrepancy refine the extension, but do not prove an all-purpose narrow geometric trace comparison independent of zero location. For ψ269,3 that remaining statement is exactly its single-character RH. The conductor computation and finite-S gap themselves use neither A nor M nor PF26.

The Artin motive is the induced rank-two standard S3 representation over Q, not a rank-one norm pullback. This is the relevant distinction between an Artin motive defined over Q and one of the Dirichlet motives covered by A. Grothendieck/Deligne and cote 1 locators are stated in the module with explicit inherited-source limits.
