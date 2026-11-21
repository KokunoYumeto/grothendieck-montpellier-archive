# THETA3-C29 independent whole-proof and source review

Reviewer: GPT-6 Astra Pro, run THETA3/noncm_integral; reasoning effort inherited and not separately exposed. Date: 2026-11-21.

## Outcome

**PASS at the stated scope.** I read the complete saved `paper_C29.tex`, reconstructed every argument, and read the relevant original source statements and their proofs. The result is an integral realization of the C23 elliptic-power Poincare kernels by signed combinations of labelled horizontal boundary special divisors. It does not identify the original compact ball model with the auxiliary boundary, replace a fixed-norm sum by a chosen label, or identify this horizontal construction with a full-rank vertical local intersection.

## Exact original source

Bruinier--Howard--Kudla--Rapoport--Yang, *Modularity of generating series of divisors on unitary Shimura varieties*, corrected 2017 author version:

https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/Modularity_arXiv_v1_corrected.pdf

Local files: `work/external/BHKRY_Modularity2017.pdf` and `.txt`. Download manifest: `work/external/BHKRY_Modularity2017_download.json`; SHA256 `5459e09cc754b5a9fe8c42857fdf1c595ef020af3d2693324ec95bb10c75d18a`.

I visually inspected printed pp.46--47, 52--54, 67, 69--70, using the original PDF renders. I also read the complete extracted proof of Proposition 3.4.3, including p.48, and the end of Theorem 3.7.1's proof on p.55.

* Proposition 3.4.3, pp.46--48, identifies the actual boundary abelian scheme with the Serre tensor construction, including the CM-base identification. The Hermitian adjoint relation on p.46 has the required conjugation.
* Proposition 3.6.1, pp.52--53, identifies each nonzero labelled divisor with the zero-section pullback along the Hermitian functional and proves effective Cartier and flatness. Its proof uses the flatness of the functional. Surjectivity also follows directly: composing it with the map defined by its own vector is multiplication by its positive norm.
* Equation (3.6.1), pp.51--52, is the fixed-norm labelled sum. Theorem 3.7.1(4),(8), printed p.54, gives the formal boundary chart with stabilizer quotient and the closure of the interior Kudla--Rapoport divisor. The Pap-model square and exceptional correction in clause (9) are not silently substituted into the Kra statement.
* Section 5.1 and Definition 5.1.1, p.67, define Q=O(0) tensor omega, identify P with Q(sum) Q(first)^(-1) Q(second)^(-1), and give J_(0,1)=Q^2. Hence J_(0,12)=Q^24.
* Proposition 5.1.4, pp.69--70, supplies Theta^24 as an integral section of J_(0,12), with divisor exactly 24 times the zero section, and a nowhere-vanishing section of omega^12. The proof checks absence of vertical components.

## Proof checks

1. The sign and base Hodge-line factor agree with the source. In particular the ratio of the three pulled-back sections is a section of P_(x,y)^24; the base factor is included in Q and has not been dropped.
2. Flatness makes each nonzero-vector pullback an effective Cartier divisor and preserves the exact multiplicity 24. Divisor addition therefore gives the line-bundle identity over the integral base. First Chern classes give the rational Chow identity after dividing by 24.
3. If x+y=0, replacing y by 2y gives x+2y=-x nonzero. Biextension bilinearity gives the claimed factor 48. Zero inputs give the rigidified trivial kernel.
4. On E^2, choosing the Hermitian labels with the appropriate conjugation gives j_x=[a] pr_1 and j_y=pr_2. Its norms are N(a), 1 and N(a)+1, and the resulting line is precisely the normalized kernel of lambda[a] in C23. Matrix decomposition and embedding projectors preserve all coefficients and denominators.
5. Substitution into the C23 cycle is valid as an identity of first Chern operators followed by proper pushforward. The proof does not require ordinary proper intersection. The two-term complexes give the correct derived pullbacks and retain higher Tor when regularity fails; no unwarranted equality of structure sheaves is asserted.
6. A pure nonzero H^1 tensor H^1 class has zero ample degree by parity on each factor, whereas a nonzero effective divisor has positive ample degree. Thus the signed expression is necessary for that pure class.

## Minor source typography, with no effect on C29

The displayed chain on printed p.70 writes Q^24 as O(0)^24 tensor omega^12, although the definition on p.67 gives exponent 24 on omega. Both Hodge powers are trivial by the preceding proposition. C29 correctly uses Q^24=J_(0,12) and the specified theta section, so its formula and normalization do not depend on that printed exponent inconsistency. No correction to the mathematical claim is needed.

