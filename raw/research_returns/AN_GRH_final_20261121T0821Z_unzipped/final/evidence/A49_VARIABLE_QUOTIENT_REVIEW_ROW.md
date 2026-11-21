# A49 variable-quotient supplement: entire-proof review

Date: 2026-11-21. Reader: GPT-6 Astra Pro, AN_GRH `/root/row_audit`. Effort is not exposed.

## Exact source and verdict

**PASS, targeted proof check.** I read the entire final source:

`work/gt_certificates/positive_rank_theta/A49_VARIABLE_QUOTIENT_SUPPLY_NOTE.tex`

SHA256: `ee040f74b52aa585476ccddd12739846a3ed1d4a36bb5518c38ada42883d7be8`.

No correction is requested. This is a separate-reader whole-proof check, not an independent re-proof or formal verification. Reading was completed during the 07:00 checkpoint write hold; this audit was saved only after root released that hold.

## Complete checks

1. The finite set S includes2,p and every prime dividing the order of the already rational canonical class κP. Thus κP has only S-primary components in every extension; taking the complementary primary projection kills it. Its order does not acquire new prime divisors after extension.
2. I reopened A42 PE.3–PE.4 and read its complete Step1 again. For j coprime to the specified M, the polynomial V_j(Φ)=1+Φ+...+Φ^(j−1) is invertible on each geometric ell-torsion point group and hence every ell-power torsion group. This remains valid when ell=p and when Frobenius is not semisimple modulo ell. Therefore the actual rational S-primary subgroup is fixed, and its cardinality B is an exact fixed kernel size, not an asymptotic estimate.
3. The progression j=1 modM is infinite. The genus-two Weil bounds give |H_j|≥(sqrt(Q)−1)^4/B while N_j is between Q+1−4sqrt(Q) and Q+1+4sqrt(Q). Consequently |H_j|>N_j and N_j>2(B−1)+1 both hold for sufficiently large admissible degrees. This comparison is uniform for the fixed B; no prime-distribution theorem is used.
4. For each nonzero element of the kernel there are at most two ordered differences of distinct geometric points. Summing over its B−1 nonzero elements bounds all ordered same-coset pairs by2(B−1). Every rational point in a nonsingleton coset participates in at least one such ordered pair, so at least two rational points remain in singleton cosets. At most one singleton coset is zero. Separately, |H_j|>N_j and P in the zero coset force an empty nonzero coset.
5. The nonzero singleton and empty cosets have augmentation coefficients1 and0. Thus the group-ring element is not any scalar multiple of the all-group sum in every characteristic. No parity assumption on N_j is needed; no delta at zero affects these two nonzero cosets.
6. Fourier inversion over an algebraic closure of Fp is valid because H_j has order prime to p. Nonuniformity therefore supplies a nontrivial character with nonzero value. Its cyclic image has order supported outside S, so it is odd and prime to p. A49's original-field Lang construction gives a geometrically connected P-split cover over that same k_j, with the selected faithful L-value nonzero modulo the fixed prime above p.
7. The quotient kills κP. The p-power and inverse character operations therefore preserve this nonvanishing, giving precisely one signed p-orbit of unit values. The argument does not force the remaining faithful orbits to be units, does not assert a rational primitive factor of prime-to-p order, and does not silently invoke A46.
8. After adding the finitely many prime divisors of the selected conductor to S, the argument can be repeated. This gives pairwise coprime nontrivial conductors on suitable finite extensions, not necessarily prime conductors or a signed-primitive conductor. The statement does not require these newly chosen fields or covers to form one fixed tower.

## Retained inputs and review scope

- Current A42, `work/gt_certificates/positive_rank_theta/A42_FIXED_LANG_DENSITY.tex`: PE.3–PE.4 and its complete Step1 reread; the whole theorem had already been checked earlier in this run. No new auxiliary counting cover is used as an allowed prime-to-p neighbourhood.
- Recovered successor final A.10/A.35: complete difference-bound/Fourier proofs were reread during the immediately preceding A49 review. Their exact genus-two difference bound applies in every characteristic.
- Current A49: entire final source `5fecbadc1de4120af3591d0f760591a02fd1ccc3d01927fc898e9e922fa24483` was independently read in this run, including original-field connectedness and the faithful-character formula.
- The finite-field Weil inequalities are the cited standard abelian-variety and curve bounds; no numerical computation or new certificate is claimed here.

## Outcome and remaining requirement

The nonuniformity-only supply question has a positive answer for every prescribed finite-field genus-two pair after suitable constant extensions. This is a meaningful exact partial conclusion. The unresolved step remains controlling an entire faithful conductor, or satisfying a bounded primitive-exponent criterion such as A47. It is not recorded as a new closure or automatic shrink of the full universal witness gate.
