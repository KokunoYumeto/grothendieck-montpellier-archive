# K17-K16-K20-K24 — independent final whole-chain audit

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro, archive_kummer.

**Verdict: PASS under the explicitly stipulated arithmetic theorem of Alpöge.** The final proof establishes the three specified vanishings from that source contract and the independently justified finite computations. It does not assert a new compiled Lean theorem, a new all-prime Vandiver verification, or a conclusion about an uncomputed weight subgroup of a Soulé character.

## Final files read in full

| File | Reviewed SHA256 |
| --- | --- |
| `higher_k_vanishing_section.tex` | `9ed3498fb46a6fd9cf46d0b081c522533d756a908e70f9297a4b0c5cea2330eb` |
| `../hecke_coverage/u3_general_coverage_section.tex` | `35b648ef423a8a11a7dacd2ee06f64e9fcf10015c6ddb336e6004c49d850e52b` |
| `gl2_general_section.tex` | `2a2299a6ca7f0344bf1689eaa2eeb1ccd10068a8c270bf0c7260b2c185dfbfd3` |
| `bernoulli_9496386083_section.tex` | `c816089d721d1429474ad87107248c024e97fffcd8c03ee3147ca64fca33d116` |
| `bernoulli_root_g5.cpp` | `10bb7a4292b2fa6fe2fe27a148431b06b8085166bcda19754fee319bd75eed20` |
| `bernoulli_root_g5.json` | `ab716c444afbe4b83f1ab1aa1aa39deca8f3f43ef17ecd462d796bb36d68711b` |

In addition to the complete TeX files, every line of `gl2_general_certificate.py` (206 lines), `hecke_combined_certificate.py` (124 lines), and the root's second Bernoulli program (92 lines) was read. The complete original Bernoulli program and generic U3 program had just been independently read in the separate reflection and harmonic audits. The final generic harmonic theorem has the complete independent audit `harmonic_hecke_archive_audit.md`. The source-content, conductor, exact strict duality, and full Soulé index checks are retained from `../hecke_level_one/k12_hecke_archive_audit.md` and the named separate primary-source audits.

The complete computational runs were executed by the author and root as recorded in their reports. This reviewer checked the full code and proof and read those completed reports, but did not claim to rerun either billion-term Bernoulli loop or the full generic harmonic replay. Concrete additional array-dimension and polynomial-factor checks performed by this reviewer are recorded in the harmonic audit.

## 1. Uniform source and packet coverage

The general coverage section retains every strengthened source predicate, including `Th.Unl` and the implication from continuity to the actual `WitA`. The literal `KillsMu 2` condition becomes trivial for every e. Twisting rho by chi^(-1) gives the exact source weights (e-1,-1,-e-1); continuity and the ordinary flag persist under the common twist. The already read full `Keep.levelKA_alt`/`levelCore_alt` proofs then give level one at every finite place, including above ell, and infinitesimal character (e,0,-e). The Hodge–Tate relation is (1-e,1,1+e), so no twist is silently changed.

The previously independently checked compact-transfer proof uses distinct conjugate-orthogonal infinity characters, a simple generic parameter with trivial reduced component group, and a pure inner form. These facts persist for every positive even e. Shin's odd-rank temperedness applies uniformly. The central character remains trivial because it is unramified at every finite place and trivial at infinity, over a class-number-one field. Hence the same ramified-prime-three packet and full-lattice-invariant argument applies. Its compact highest weight is (e-1,0,1-e). The scaled operator p^(e-1)T_p has eigenvalue alpha=p^e times the source geometric-Frobenius trace. No hypothesis peculiar to e=6 is reused outside its scope.

## 2. Complete rank-two spaces in the new weights

The conductor lemma itself was proved for every e>=1, ell>3, with the required actual flag and separated slope difference 2e. Therefore it applies to e=8,10,12 without a new local-global compatibility input.

The general modular-form proposition follows from the same primary ring theorem already read for e=6. Multiplication by D identifies M_(2e-5)(Gamma_0(3),chi_-3) with S_(2e+1)(Gamma_0(3),chi_-3): D has no interior zeros and order one at both cusps, and the character is trivial on both cusp translations. The monomials D*a^(2e-5-3j)*b^j are the complete weighted-polynomial basis. Their leading terms q^(j+1) give an integral lower-unitriangular identifying matrix. Thus they are also a basis of the integral Fourier-coefficient lattice, rather than just an arbitrarily scaled rational basis.

The complete standard-library code constructs the theta/divisor-sum and eta-product expansions from scratch to precision 182. Its binomial factors are the exact finite positive-power or negative-power series, with no floating arithmetic. The Hecke correction term is chi(p)*p^(2e), and is included whenever p divides the Fourier index; in particular the e=12,p=7,n=7 entry is present. The first r coefficients identify the full matrix because Hecke stability and the complete basis are already proved. Additional coefficients are checked through floor(182/p). Faddeev–LeVerrier has exact divisibility checks and terminal Cayley–Hamilton verification; independent Bareiss determinants at 0,1 and the target evaluate the same polynomial. The factor lists in the combined certificate match every polynomial displayed in G2.

## 3. The combined product is the right object

The new unit criterion uses

    N_(e,p) = P_(e,p)(1+p^e+p^(2e)) * Q_(e,p)(1+p^(2e)).

Here P is the full scaled U3 characteristic polynomial and Q is the full classical GL2 characteristic polynomial. Both are monic integral. At a prime ell not dividing the product, each evaluation is a unit. In a splitting field at ell, every root is integral, so a product of the integral differences can be a unit only when each difference is a unit. The denominator p^e is a unit when ell != p. Consequently one such p covers every admissible representation in both branches simultaneously. Repeated roots cause no difficulty, and no comparison with source trace-list multiplicities is required.

Crucially, G7 takes the gcd of these combined products. It does not separately choose an auxiliary prime for each branch. For any ell not dividing that gcd, one of p=7 or p=13 supplies a unit combined product and therefore makes every summand in the same source inequality zero.

The complete combined certificate reads both full model polynomials, verifies the sets of e and p, recomputes every evaluation, checks it against each model's output, and takes the exact gcd of the products. It verifies the displayed prime-power factorizations and tests all their prime factors by trial division. The e=8 factors are 2,3,23,401,809,13687. The e=12 factors are 2,3,5,7,13,37,47,28447,300455201. All are below 2^31. The e=10 list contains exactly one factor above that threshold, q=9496386083. Thus the stated range conclusions follow from the actual combined products.

## 4. The isolated residual prime is removed correctly

The final Bernoulli proof was read in full. It derives its congruence from the p-integral Bernoulli recurrence and the exact permutation a -> ga modulo p, with expansion modulo p^2. The sign and factor agree with the independently derived formula in the reflection audit. The half-orbit reduction uses n even and q_(p-a)=g-1-q_a, giving the signed coefficient 2q_a-(g-1).

The root's complete second program uses g=5, ordinary unsigned 128-bit reduction, and every one of the 4,748,193,041 half-orbit terms. The primality and order checks prove its orbit is valid. Every arithmetic bound in the proof is sufficient: raw=5a<5p, signed coefficient at most 4 in absolute value, the unscaled weight product below p^2, and sums reduced after each update. Its loops and exponent arithmetic contain no floating-point dependence. The completed report gives S_5=7110767128, multiplier 9130328994, and residue 3753150554, agreeing with the independently implemented g=2 Montgomery run. Both check endpoints a_h=w_h=-1. The run reports are complete and are distinguished from the earlier truncated benchmark.

The separate reflection lemma has this reviewer's full proof and two independent whole-proof audits. Taking e=10 gives n=q-11, an even index from 2 through q-3, and 1-n congruent to 11 modulo q-1. Herbrand kills A_q^[11]. The full Kummer-radical argument kills A_q^[-10]; its unit kernel has no odd character 11, since only omega occurs in odd units modulo p. The exact K2 vanishing equivalence then kills K_20(Z){q}. This argument has no Vandiver assumption at q and claims only the needed component.

## 5. Final group and character consequences

For ell>2^31 the datum is the same explicit class-number-one field, modulus two, and trivial character as in `ClassNumberThree.gd`. All e in {8,10,12} are positive even and satisfy ell-1>2e. The original discriminant, noncontainment, and class-number hypotheses remain unchanged; ell is different from 2 and 3. The chosen auxiliary primes 7 and 13 are split and automatically different from ell. Thus the direct finite-length inequality and exact strict Selmer/K-group duality apply without a missing exceptional place.

The published Vandiver verification supplies the odd primes below 2^31; it is cited rather than rerun. The even boundary 2^31 is not prime. Rognes–Weibel supplies the 2-primary parts. Each positive even K-group in question is finite, so vanishing of all primary parts gives K_16=K_20=K_24=0 under the stipulated source theorem. Combining with the separately audited K_12 theorem and known K_4,K_8 gives all six specified degrees.

The class-group assertions are the vanishing equivalence K2 at k=4,5,6, not an equality of orders or a claim about all eigenspaces. The full-domain Soulé index K18 at m=9,11,13 then has index one for every odd ell. Its odd m have nontrivial residual Delta character, including small ell, as in the previously checked proof. No deeper weight-domain conclusion is substituted.

Finally, the periodic corollary uses only the equality of the character -2k modulo ell-1. The zero residue is the already known trivial class-group component; residues represented by 1 through 6 use the proved six vanishing degrees. The strict Selmer statements for e=2,4,6,8,10,12 are precisely K5. The programme paragraph preserves the remaining geometric-recognition, factorial, integral-defect, and Iwasawa gates.

## Final readback

The complete final theorem, all new supporting proofs named above, and this audit have been read. No mathematical or source-scope correction is requested. The theorem is ready for promotion with its explicit stipulated-source qualification retained.
