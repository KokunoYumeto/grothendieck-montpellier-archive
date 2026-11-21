# A46 separate-reader whole-proof review

- Date: 2026-11-21.
- Reader: GPT-6 Astra Pro, `/root/row_audit`; effort not exposed.
- Checked complete source: `work/gt_certificates/positive_rank_theta/A46_PRIMITIVE_SIGN_CRITERION.tex`.
- SHA256: `f708446fd0e7af24f61625fc6ea68bd1c019ce1dcfb132958e71d6cc3ceb3ae8`.
- Result: **PASS**. This records a targeted proof check, not a formal verification or a separately authored re-proof.

I read the complete statement, source-credit paragraph, all five proof steps, and the final scope paragraph. The earlier A15/A18 manuscripts had also been read in full when testing the proposed new sign argument. The present review is of the complete new manuscript, including its nonconstant-deck arithmetic step.

## Checks

1. The Ramanujan-sum projector is an integral, Galois-invariant endomorphism. Its actual image is defined over the stated finite field. The identities `A e_n = A` and `A p_n = n A` hold in the rational group algebra and the latter is integral. Vanishing of the actual primitive factor's rational p-primary group therefore gives `A delta = 0` without extending constants or assuming that the geometric deck generator is rational.
2. The covering/Kummer implication is used in its precise pointed form: a rational lift of the prescribed point is sufficient. The geometric cyclic subgroup is normal of index prime to p, so passage to the relevant cores preserves geometric prime-to-p topology. Equal lifted sections make the rational Jacobian difference p-primary.
3. The subset products in the composite projector are distinct because their factors have distinct prime orders. The resulting divisor has exactly `2^omega(n)` simple zeros and as many simple poles on two disjoint free deck orbits. The integer signs do not merge in characteristic two. A function with this divisor is separable in every characteristic.
4. The controlled-field induction is correct. I checked its displayed algebraic identity, the index divisibility, the bound `n > (2^omega(n)-1)^2`, and the exclusion of index one using the étale genus formula. A kernel in the induced cyclic action has order dividing both the odd cover degree and the power-of-two field index. A point stabilizer would similarly force an odd prime to divide a fibre degree. Thus the induced action is faithful and free.
5. A reduced zero fibre has at most one point from each original deck orbit, so the field index is exactly two. The intermediate extension is separable, hence has its quadratic involution. The involution commutes with the cyclic deck group and exchanges the two entire original orbits. Comparing literal integral coefficients on a free orbit gives `A sigma^(-j) = -A`. Iterating through the odd order of `sigma^j` contradicts torsion-freeness of the integral group ring and nonvanishing of A.
6. The geometric p-rank-zero corollary is valid after descent and pointing because geometric p-primary points remain absent under every constant extension. The rational criterion retains its original field throughout the arithmetic step.

## Exact movement and limits

The proof removes the earlier rational primitive-factor elliptic-quotient qualification, in all genera at least two and all characteristics for odd cyclic degrees prime to the characteristic. It does not prove the existence of a suitable cover or a universal theta-incidence statement. No genus-one classification or Deuring–Shafarevich calculation is required for the new endgame.

The Poonen controlled-field source was checked directly earlier in this run: Proposition 2.1 statement, complete displayed Lemma 2.2 and Corollary 2.3 proofs, author pages 3–4, at `https://math.mit.edu/~poonen/papers/gonality.pdf`. The external book proof of Castelnuovo–Severi was not independently reread. This review does not inflate that earlier primary-source reading into another complete source reading.

## Final citation-only change

The final source SHA256 is `490219c87e7d801776092ec7974d2fb128fabdcb7af1daea9411514b9597d6eb`. I inspected its complete exact diff against the preserved whole-read source `A46_PRIMITIVE_SIGN_CRITERION_FULL_INDUCTION.tex`. The only change deletes the reproduced Poonen induction and gives the precise cited Corollary 2.3 applicability: the perfect algebraically closed ground field, finitely many degree-d generators, the controlled integer u with index d/u, and the substitution u=d/e. This narrow change **PASS** agrees with the primary passage already read. Every new argument is unchanged. It is not recorded as another whole-proof reading.
