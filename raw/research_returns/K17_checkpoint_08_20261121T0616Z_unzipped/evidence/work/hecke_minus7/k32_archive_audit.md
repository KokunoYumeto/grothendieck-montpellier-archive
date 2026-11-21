# Final independent whole-proof audit: K32 and the first nine degrees

**PASS under the explicitly stipulated Alpöge arithmetic source theorem.**
Auditor: GPT-6 Astra Pro, K17/archive_kummer, 21 November 2026.

The entire final `k32_vanishing_section.tex`, including both theorem and
periodic corollary and the arithmetic-scope paragraph, was independently read
and reconstructed. Reviewed SHA256:
`6b7da7e6e8810842ce692876591868a0873a08040afad1a83eb00cd442b256f8`.
No mathematical correction was requested.

## Closed arithmetic chain

1. The previous one-prime corollary was freshly read in full. Its proof uses
   finiteness, established zero2-primary part, HHO below2^31, and the exact
   higher2 gcd plus whole-source unit criterion above2^31. It leaves only
   q=25078104767246023. It does not assert a numerical bound on the possible
   q-primary group and does not use the new calculation circularly.

2. The new datum is exactly E=Q(sqrt−7), e16, N2, psi1. The complete final
   source bridge has been independently audited, with its primary local
   hypotheses and exact source predicates retained. In particular the
   direct OneCharU_s criterion permits the split prime2. The restrictions
   from the later counting theorem are not imported into this direct
   criterion. I freshly read the full direct-unit statement and proof again.

3. The full two-class U3 space has the required highest weight(15,0,−15).
   The integral block operator and its Schur complement are exact. The
   nonzero171-dimensional determinant13187546903051047 modulo q implies
   the full comparison determinant is a unit. I independently recompiled
   and replayed every C++ evaluation, and independently reconstructed the
   invariant harmonic kernel and a342-dimensional norm determinant.
   The whole proof covers both minuscule directions and the scale2^15.
   No principal-class truncation or finite-index harmonic lattice is used.

4. The entire S33(Gamma1(7)) is61-dimensional. Both the character-block
   calculation and my separate integral-conic-basis calculation return
   det((1+2^32)^3 I−T2^3)=15133664954664570 modulo q, nonzero.
   The full-lattice proof and all coefficient embeddings have been checked.
   The source rank-two predicate permits two nontrivial mod7 inertia
   characters and possibly original conductor49. Twisting one character
   off correctly yields a primitive conductor7 form; the untwist at2 is
   any cubic root of unity. The cubic determinant covers every such value.

5. Both source-admissible branches therefore have individual unit trace
   differences. The recovered intermediate theorem proves finiteness before
   using length, and its finite nonnegative valuation sum is zero. Thus
   the actual source Selmer module has zero length and is zero.

6. The Selmer module in this application is the group over Q: psi1 cuts out
   Q. The auxiliary imaginary quadratic field E is used for the automorphic
   comparison, not substituted as the field of the final Selmer group.
   I freshly read K17-FIELD-DESC and the strict-duality proof(K5), including
   their coefficient and local terms. A finite coefficient DVR is finite
   free of positive rank over Z_q, hence faithfully flat. Continuous
   cochains, the finite local-condition kernel and the character idempotent
   commute with this finite free extension. Zero after extension therefore
   gives zero at the bottom Z_q ring. The extra local2 condition is automatic
   because D/(2^(-16)−1)D=0 for the divisible negative Tate module.

7. Exact strict duality gives
   (K32(Z){q})^vee=S_q(16)=0. This is a canonical duality, not an inference
   from a class-group order comparison. The preceding one-prime result then
   proves K32(Z)=0. All seven newly specified degrees beyond4 and8 are now
   accounted for:12,16,20,24,28,32,36.

## Exact consequences and limits

The comparison(K2) is an equivalence of vanishing for K4k and the single
cyclotomic class component of exponent−2k; it is not an isomorphism of the
full finite groups. Applying it to K32 gives A_ell^[−16]=0 for every odd
ell. Equation(K5) gives S_ell(16)=0 for every such ell.

I freshly read the full-domain Soulé index statement and proof(K18), with
the cyclotomic-product normalization(K19) and the residual character
argument. At m17 the relevant K degree is2m−2=32. Thus the image index on
N_ell=Gal(Qbar/Q(mu_(ell^infty))) is1; every reduction modulo ell^a is also
surjective. Applying the same statement to k1 through9 gives precisely
the odd weights3,5,7,9,11,13,15,17,19. Nothing is asserted about unit values
on a deeper Galois weight-filtration subgroup, and no factorial is inserted.

For the periodic corollary, positive k congruent to j modulo(ell−1)/2
gives the same exponent−2k=−2j modulo ell−1. For j1 through9 the
corresponding component is zero by the nine established degrees. For j0,
the trivial class-group component is zero by extension after norm to Q,
since ell−1 is an ell-adic unit. This gives exactly the stated vanishing
residues0 through9, including overlapping residues at small ell. It does
not assert periodicity of orders, does not include K0, and does not prove
Vandiver for all primes or the remaining all-prime tripod-kernel claim.

The finite-model computations are actual exact certificates with independent
implementations/replays. Neither this audit nor the theorem claims a Lean
execution or a verification of the entire recovered repository.

## Supporting complete audits

* `minus7_coverage_archive_audit.md`: complete source and conductor bridges,
  fresh published conic-ring/eta and principal-series primary checks.
* `u3_minus7_archive_audit.md`: full finite unitary model and actual replays.
* `gl2/gl2_minus7_archive_audit.md`: full finite classical model, separate
  integral-basis implementation and integral unit-factor interface.
* `../hecke_general/higher2/higher2_archive_audit.md`: higher2 models, the
  earlier one-prime isolation, and the preceding K28/K36 chain.
