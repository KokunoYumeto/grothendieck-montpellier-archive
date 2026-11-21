# A44 complete proof and finite-verifier reading

Reader: GPT-6 Astra Pro; effort not exposed; AN_GRH /root.
Date: 2026-11-21T05:45:53.825181+00:00.
Complete source read: SHA256 d1e97e8250896fbbbf6801cc1caa94e6dee85b0092199ccaad17997f66a71e3e.

PASS. I read the entire theorem, its scope paragraph, all six proof steps, the full finite candidate illustration and the concluding application limits. I also read the complete verify_A44_finite.py source. No mathematical correction requested.

The nonvanishing argument uses the exact coefficient factorization and the Weil absolute values correctly. The least-appearance argument only needs semisimplicity on the kernel of the separable polynomial T^(2^m)−1, not of all Frobenius. I checked the exclusion of residue1mod8 by Gauss's lemma, the valuation4 for residues3/5, and the remaining degree2/4 cases for residue7.

In degree2 I checked both possible reciprocal-pair overlaps, including why lambda² in the base field forces its conjugate to be −lambda; every overlap lies among primes dividing q²−1. For disjoint pairs, the coefficients and division-free elimination give the stated D_epsilon. In degree4 the norm exponent has valuation exactly m−1, so the norm is −1 and the constant term gives q²+1. I independently expanded the factorization and elimination formulas by hand.

For all higher primary exponents, the Frobenius orbit degree is a power of two dividing the order of GL4(Z/ell^r); its reduction kernel has odd order. This proves the single explicit finite-field bound uniformly in r. Surjectivity of reduction of unit groups gives the necessary primewise eligibility condition for a whole signed-unit order. No converse is asserted.

The two-adic root calculation is also complete: nonunits and units with residue different from one contribute zero; repeated squaring eventually gives valuation greater than one, thereafter exact growth by one. Reciprocal Weil roots bound the number of unit roots by two. The actual rational two-primary group size thus grows polynomially in 2^m, while the fixed-field Lang lower bound grows exponentially in 2^m. This proves infinitely many odd theta points in the tower, even though only finitely many can be supported on eligible primes. It is correctly distinguished from the fixed-cover hypothesis in A42.

The A13 recurrence, factorization and eligible support agree. I checked the identification of B as the unique ineffective theta characteristic using the three distinct branch characteristics and the canonical pencil. The exact order3 illustration is proved directly: h(r)=1, f(r)=r², F(R)=0 and its conjugate is1; the norm identity gives order3 at R and simple zeros at W0,W1, while the unique pole has order5. Dividing by h² gives the complete divisor3(R−B). Ineffectivity excludes zero. The two choices each of r and a0 give four distinct points in F16. This does not classify all eligible theta points.

The finite verifier source is fully read. It symbolically checks the factor and elimination identities, exhaustively checks only residues for5<=m<=16, computes the A13 resultant and recurrence, factors L, and reduces the norm/point identities in the stated polynomial quotient. Its RR-probe block reads retained output and does not recompute the220 matrices; the script says so accurately. This root event is a source reading, not an additional execution or independent RR implementation. Published Frobenius/Weil and torsion-module inputs are carried with their existing source checks; no new whole-book reading is claimed.

The result closes the specific unbounded-support inference in the pro-two constant tower. It neither proves nor disproves a witness on every curve, and supplies no universal cover selection. It is not by itself counted as a previously open main row changing status. No formal verification or independent-model validation is claimed.

## Final source locator delta

The final source SHA256 is d7ef05d824572383a63e35a89eb8d74f51d2f6a0e28bf2c7d326cabed15fb01a. Its sole delta adds the exact Milne AV Proposition12.9 point-count locator to the existing citation. I checked that citation-only change against the fully read source; no mathematical statement, proof step or certificate changed. This is not counted as a second whole-proof reading.
