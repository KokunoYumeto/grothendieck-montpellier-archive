# Route2 follow-up: exact scope and exploratory dead ends

Run KTOWER, reviewer `/root/geometry_tower`, GPT-6 Astra Pro, effort not exposed, 2026-11-21 UTC.

## Promoted proof awaiting peer review

`rm_frobenius_avoidance.tex` proves **KT-RM-FROB-AVOID**: for any prescribed odd finite level m, any gamma in SL2(O5/m), and any finite set S of odd primes (overlap with m allowed), there are ordinary genus-two O5 curves in every nonempty open with this finite Frobenius class and no nonzero S-primary point on the actual Raynaud theta. Every power and product of primes in S is excluded. Field size varies and is not bounded.

The new argument strengthens the carried A37 method. It chooses ell-adic lifts of arbitrary congruence classes for which det(G^D−1) is nonzero, freezes the finitely many determinant valuations at a deeper level, then uses the same full-level torsor specialization and carried A19. Both entire carried proofs were reread. Their published moduli/descent/Lang–Weil inputs remain accepted inputs.

**KT-RM-FROB-NONDETERMINATION.** For any b, this gives a positive/negative pair with the same finite Frobenius/RM data at4159^b: the positive curve is the actual carried A13 curve, after a constant extension containing F128 and the needed roots of unity; its actual Frobenius defines gamma. The negative theorem supplies the other curve. **There is no claim of a positive curve for arbitrary prescribed gamma.** Long prescribed Frobenius orbits can obstruct theta incidence. Nor is there a claim about equal field sizes or equal exact Weil polynomials.

The consequence concerns a prescribed finite prime support only. It does not exclude an existence proof choosing primes adaptively from the curve, and does not settle the universal ordinary-O5 question.

## Finite RM incidence exploration, not promoted as a theorem

For a finite subset A of a genus-two theta support, the ordinary difference multiplicity is at most2 away from zero. The carried identity Theta·TTheta=3 also gives a mixed-difference bound at most3 for P−TQ; the zero mixed difference is absent on odd torsion because the intersection Theta intersect TTheta consists of the three nonzero geometric2-torsion points. These provide necessary constraints on signed Frobenius orbit sets and on any proposed transversal of primitive doubling orbits.

I tried these finite constraints on several Frobenius modules. In all completed exploratory checks, the mixed RM condition supplied no additional exclusion after the ordinary difference constraint. These runs were exploratory and inline; they are not saved exact certificates and are not used in the promoted proof.

- The carried A13 Weil polynomial x^4−x^2+4 was checked through quotient modules at eligible small primes. Some primes (including61 and79) failed the ordinary difference condition in the explored quotients. No additional RM-only failure was found.
- The ordinary curve candidate z^2+z=x/(x^3+x+1) has the elementary candidate Weil polynomial x^4+x^3+3x^2+2x+4, with T=pi+2/pi satisfying T^2+T−1. It was explored as another O5 example, not as a certified counterexample. It has obvious positive small-prime behavior, so it did not supply the desired all-odd failure.
- Linear Frobenius eigenline tests for those two polynomials over primes below5000 produced no mixed-RM failure among the sets passing the ordinary difference test.
- An analogous test using the A36 quadratic Frobenius polynomial x^2+31x+256 and independent golden-ratio scalar roots likewise produced no new mixed-RM failure in the completed range.

One quotient-orbit enumeration was deliberately capped at200000 orbit elements and terminated with a `ValueError('large')`; it is not a complete search over its requested range. The first Sympy/FLINT factorization attempt failed because nmod factors could not be ordered; the completed retries used the Python ground type. These execution failures do not affect any theorem: no numerical assertion from these explorations is used as a premise.

## Checks

The author has whole-read the new proof and carried inputs. Lean-chain independently whole-read the new proof and the complete A19/A37 proofs and reported PASS; his explicit-characteristic-two wording correction was applied. Parent independently whole-read both new results and the complete A19/A37 proofs and reported PASS. Archive phrase searches found the recognized carried A37 method but no arbitrary-congruence lift version; this is not an assertion of literature priority.
