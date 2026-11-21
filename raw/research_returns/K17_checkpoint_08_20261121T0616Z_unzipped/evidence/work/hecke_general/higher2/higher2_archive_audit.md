# K17-HECKE-HIGHER2 and K17-K28-K36 — independent final audit

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro, archive_kummer.

**PASS.** The full finite-model proposition passes as stated. The final K_28 and K_36 theorem passes under its explicit stipulated arithmetic-source hypothesis. The remaining K_32 component is retained correctly.

## Material read and actual execution

The following files were read completely: `higher_harmonic_section.tex`, `gl2_higher2_certificate.py`, `comparison_certificate.py`, `k28_k36_vanishing_section.tex`, `bernoulli_8361790201_section.tex`, the original Bernoulli C++ program, and the independently written g22 program. The unchanged underlying general U3 and GL2 routines had just received complete proof/code audits in the preceding review.

This reviewer executed the complete 59-node Lucas primality and comparison certificate. It passed, checking every displayed gcd and its factorization. A separate inspection checked every new harmonic identifying matrix's exact d-by-d shape, the d identifying points, every saved operator shape, every nonzero exact determinant, all orbit counts, and the listed swap dimensions. The full harmonic transformed-evaluation replay was executed by the author and root, rather than relabeled as this reviewer's execution.

This reviewer also independently wrote, compiled and executed the entire 4,180,895,100-term Bernoulli sum with multiplier/enumerator 22 and ordinary 128-bit modular division. That complete execution and proof are recorded in `bernoulli_8361790201_archive_audit.md`; the output is 1827838999 modulo 8361790201 and agrees with the original, different computation.

Reviewed model hashes:

| File | SHA256 |
| --- | --- |
| `higher_harmonic_section.tex` | `06f7c86c6e6887ecfc4a94d4fda26cd9e826cb0d904695c911b7320c97918026` |
| `harmonic_hecke_exact_data.json` | `b362945a162a6e6355be470f753dd2281e6b2dd284b9af8cff1e2a4ef9b8ee6e` |
| `gl2_higher2_certificate.py` | `80424d6d8031b9b4538d05f18417600b13d6b90acc5fa00f915fd4b4b974ad81` |
| `gl2_higher2_certificate.json` | `8434c5e4eb97662ed9c42b756223c60833a3614d96f295c2a0d3fc8e732dea4b` |
| `comparison_certificate.py` | `2018b69e756a5a7e641d5c20000c1ebc413f59688bb148d244cbf4db1d625614` |
| `prime_certificates.json` | `649d55d63458bec04b615fcf40d7f4d31046dc634058450b26645b72fffe84e4` |

## Complete-space and arithmetic checks

The harmonic proof applies uniformly at k=13,15,17. Exhaustive three-part exponent compositions with coordinate differences divisible by 6 include 0, ±6 and ±12; there is no restriction inherited incorrectly from smaller weights. The inspected counts are (64,50), (104,83), and (156,129), yielding full harmonic dimensions 14,21,27. The swap dimensions are (8,6), (12,9), and (15,12). Full contraction rank and full-rank annihilated columns are the correct completeness test.

The same complete 57 and 183 neighbor sets remain valid independent of weight. The scaled substitution, whole-space positive/negative conjugacy, rational basis change by 1+2omega, and integral polynomial-lattice argument likewise do not depend on weight. Modular rank screening is used only to choose points for k=15,17. The actual defining condition is the exact nonzero identifying determinant, checked by the unchanged exact replay; no numerical rank assertion substitutes for it. The final wording accurately distinguishes k=13's original exact point selection.

The full GL2 basis D*a^(2e-5-3j)*b^j has dimensions 8,10,11 for e=14,16,18. The wrapper reconstructs it from the already audited exact routines with precision 260. It retains all p-divisible-index correction terms, identifies the entire matrix through the integral unitriangular initial coefficient matrix, checks coefficients through 37 at p=7 and 20 at p=13, and uses exact characteristic-polynomial and three determinant computations. No stored matrix is input.

## Recursive primality and combined gcds

The Lucas proof was independently reconstructed. For a node n, the complete factorization of n-1 uses previously proved primes. A witness a satisfies a^(n-1)=1 modulo n, and gcd(a^((n-1)/q)-1,n)=1 for every prime q dividing n-1. If r divides n, the order of a modulo r divides n-1; the gcd tests force its valuation at every q to be the full valuation of n-1. Thus that order equals n-1 and divides r-1. Hence r>=n, forcing n prime. The base 2 is explicit. The finite topologically ordered certificate has no circular primality dependence.

The complete replay checked all 59 nodes and every factor of HH.2 and HH.3. It recomputes full unitary and classical polynomial evaluations and their combined products. The gcd of those combined products is the correct simultaneous two-branch criterion. All e=14 factors are below 2^31. The only larger factors are 25078104767246023 for e=16 and 8361790201 for e=18. No inference from U3-only gcds is used in the final arithmetic theorem.

## Final K_28 and K_36 theorem

The whole final theorem and its periodic corollary were read. For ell>2^31 all the same closed datum conditions hold for e=14 and e=18. The uniform source coverage, literal conductor bridge, integral complete-space polynomials, and trace scales match the general unit criterion. Choosing one auxiliary prime p=7 or 13 with unit combined evaluation simultaneously makes every admitted trace difference a unit; it is split and different from ell. The supplied finite-length source inequality gives zero length, and the exact strict duality K5 gives the stated primary K-group vanishing.

For the sole large e=18 factor q=8361790201, n=q-19 is even in the Herbrand range and is q-integral by the recurrence. The independent nonzero residue kills the mirror component [19], then the even component [-18] by the fully proved Kummer reflection, then K_36{q}. It does not assert all of Vandiver at q.

The published HHO range handles all odd primes below 2^31; the boundary 2^31 is not prime. The established Rognes–Weibel result handles 2. Finiteness gives the two global vanishings under the source contract. The class components [-14],[-18] and strict groups S_ell(14),S_ell(18) follow from the exact earlier equivalences. The full Soulé index at m=15 and m=19 is then one, including at small odd ell. Reduction of an onto map gives surjectivity modulo every ell-power. No deeper weight subgroup or factorial normalization is substituted.

The accumulated degree list is exactly k in {1,2,3,4,5,6,7,9}; the periodic corollary correctly lists residues 0 through 7 and 9, leaving 8 unclaimed in general. The final paragraph explicitly retains K_32 and its sufficient Bernoulli condition B_(25078104767246006) modulo 25078104767246023. The index is p-17 as required for e=16.

## Final readback

The complete final proof and this audit were read after writing. No mathematical correction is requested. The model, the two independent degree-36 Bernoulli computations, and the final K_28/K_36 theorem are ready for integration at their stated scopes.
