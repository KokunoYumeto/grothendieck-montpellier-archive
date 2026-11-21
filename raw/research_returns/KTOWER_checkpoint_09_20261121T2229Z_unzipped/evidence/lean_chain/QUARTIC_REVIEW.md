# Independent cross-check of the multiplicity and quartic bound

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

## Reviewed material and result

I read all of `../unitary_audit/unitary_results.tex` and `../unitary_audit/coverage_results.tex`, including the complete new proofs of KT-U3-DIM, KT-U3-SPECTRUM, KT-TRACE-MULTIPLICITY, and KT-QUARTIC-BOUND. I then matched the arithmetic interface directly to the pinned source and the carried K17 VK-PT / VK-EXCEPTIONS results. The imported classification, local compatibility, and harmonic-realization theorems remain cited background; this review is not a new proof of those inputs or a Lean kernel build.

**Result: the new multiplicity and quartic deductions pass once the carried 2-primary vanishing input is stated explicitly.** The draft initially grouped every small prime under Vandiver/Kurihara, whose stated range is odd primes. I sent this correction to both the author and root. The carried Rognes–Weibel theorem supplies the missing prime 2; no change to the numerical bound is needed.

## 1. Multiplicity

`NumberU3US.lean:57–59` requires pairwise representation-isomorphism distinctness of the actual finite set. In the irreducible branch, two representations attached with fixed coefficient embedding to the same cuspidal GL3 representation have the same cofinite full Frobenius characteristic polynomials; continuity and semisimplicity allow Chebotarev and Brauer–Nesbitt. The common cyclotomic twist does not affect the conclusion that the original representations are isomorphic. Hence distinct source members require distinct GL3 parameters, whose compact transfers occupy distinct summands. Selecting one fixed eigenline in each gives the necessary linearly independent vectors, even when their eigenvalues at seven coincide.

In the rank-two branch a fixed normalized newform determines its attached semisimple representation, and therefore determines the restricted representation with the trivial summand. Thus distinct source members require distinct normalized forms. Rank-three irreducibility makes the two branches disjoint. Full characteristic polynomials retain all required multiplicities. No injectivity of the numerical trace at seven is assumed.

The uniform integral model in KT-U3-SPECTRUM is sufficient: for `g=U/pi` with `U*U=7I`, the substitution action in bidegree `(d,d)` has denominator `7^d`; multiplying by `7^d` preserves the integral harmonic lattice and its invariant lattice. The exact power-sum formula is rational, so Newton identities also give rational characteristic coefficients; integral coefficients in the quadratic field that are rational are integers. Thus the monic polynomial is in Z[X] uniformly in d. The corresponding classical polynomial is the full integral Hecke characteristic polynomial. All omitted factors have nonnegative normalized l-adic valuations.

## 2. Exact Frobenius and comparison trace

Use the pinned prefix `src/Development/AutomorphicArithmetic/AutomorphicVarieties/` below. There is a prime of norm seven in Q(sqrt(-3)), since seven splits. Choose an arithmetic Frobenius `sigma` there and apply OneChar to `s=sigma^-1`.

- `CharacterLevelBounds/ShaFamMono.lean:15` defines `Chr.Psi` as `chiO^e * psi`.
- `UnitaryThreeGroups/OrbEquiv.lean:28–46`, `frob_val`, gives the cyclotomic value `normV w` at the embedded arithmetic Frobenius, assuming the residue prime differs from l.
- The complete `t_eq` proof at `OrbEquiv.lean:82–91` gives the source comparison at inverse Frobenius. With modulus two, the trivial finite character, and norm seven, it is exactly `7^(-e)+1+7^e`.
- Thus the denominators `7^e` appearing in both trace branches are l-adic units whenever l is not seven. The nonvanishing inequalities in KT-TRACE-MULTIPLICITY prove the universal non-equality premise of OneChar, not just its restriction to a preselected finite set.

## 3. Exact GD range

I read the full proof of `SmallClassNumbers/ClassNumberThree.lean:gd`, lines 64–86, and the complete definition in `HeightAndVanishing/Counts.lean:9–22`. For the trivial finite character modulo two and Q(sqrt(-3)), `gd` assumes only `1<=e`, `Even e`, primality of l, `5<=l`, and `(l-1) does not divide 2e`, together with ambient field and algebra structures. It proves all the other GD fields, including discriminant/class-number coprimality and field noncontainment. There is no condition `e<l`, no regular-weight interval in l, and no extra exclusion beyond those displayed. The field/algebra structures exist for an algebraic closure of Q as used explicitly in `bound_of`.

## 4. Length normalization

`HeightAndVanishing/DirichletPrimeToLPartMulLPowerPart.lean:116–118` defines Vlen and Vn. `CharacterLevelBounds/ShaFamMono.lean:71` defines the normalization as finite length divided by the ramification length e(O). The full `vlen_one` proof, `ClassNumberThree.lean:22–31`, identifies the trivial-character Vlen with the source strict negative Tate Selmer group. OneChar proves finiteness separately before its ENat.toNat expression is used. With the bottom coefficient ring O isomorphic to Z_l, e(O)=1. The carried K17 VK-PT / VK-LOCAL theorem therefore identifies Vn with the l-adic exponent in the finite K-group order. No residual factor of two or coefficient-field degree is lost; the factor two in the final bound is precisely the factor in OneChar.

## 5. All primes

For every positive even e, the carried Rognes–Weibel input kills the 2-primary part. The stipulated Vandiver computation and Kurihara equivalence kill all odd primes below 2^31, including seven. For each remaining prime l:

1. If `(l-1)|2e`, the carried VK-EXCEPTIONS theorem kills the l-primary part.
2. Otherwise `gd` applies with no further weight restriction; l is at least five and differs from seven. The preceding source specialization and multiplicity inequality give `v_l(|K_{2e}(Z)|) <= 2 v_l(N_{e,7})`.

Every prime exponent is therefore bounded, and finiteness gives `|K_{2e}(Z)| divides |N_{e,7}|^2`. A second test prime is unnecessary because the sole residue-prime exclusion, seven, has already been removed arithmetically. The proof uses the complete group order, not merely its mod-l dimension.

## 6. Numerical quartic estimate

The dimension specialization in the reviewed proof agrees algebraically with all six odd residues of the proved degree-d quasipolynomial when d=e-1. The bounds used are

`D_e <= e^3/216 + e/9 + 7/27`,
`r_e <= (2e-2)/3`, and therefore
`S_e <= e^3/216 + 7e/9 - 11/27`.

After division by e^3 the derivative is `(33-42e)/(27 e^4)`, negative for e>=4. Its value at e=4 is exactly `3/64`, so `S_e <= 3e^3/64`. The norm estimate gives

`log |K_{2e}(Z)| <= 2S_e(2e log 7 + 1) < (3/32)e^3(4e+1) <= (51/128)e^4 < (2/5)e^4`.

At e=2 both spaces have dimension zero. Their comparison polynomial values are one, so the divisibility gives the zero K-group. These numerical deductions have no additional arithmetic assumption once the explicitly carried background listed above is included.

## KT-QUARTIC-QUARTER: complete refinement review

Whole-read `unitary_audit/quartic_refinement.tex`. PASS. The stable rank-three dimension plus the entire classical rank-two dimension gives exactly the three displayed residue-class formulas for s_e; substitution into the previously checked stable dimension formulas verifies each algebraic identity. The small degrees are s_2=0 and s_4=2. For e>=6, s_e/e^3<=1/216+4/(9e^2)<=11/648<1/32, while e=4 attains 1/32.

The complete compact norm bound is 57*7^(e-1); addition of the target gives 7^(2e)+(64/7)*7^e+1, and the classical factor has a smaller bound. The ratio is at most 2850/2401<4/3. Stable restriction preserves the operator-norm bound, so no additional Ramanujan claim is used. The earlier arithmetic divisibility by the square of the full comparison integer is unchanged, including exceptional primes and the separate two-primary input. Symmetric-square stable systems remain included.

Fresh Fraction arithmetic in `quartic_refinement_check.py/.json` verifies the exact exponential partial-sum surplus 3130848254169/114688000000000, the factor bound, 11/648<1/32 and the coefficient 239/960<1/4. The whole infinite inequality follows by the displayed algebra and monotonicity; finite computations are only exact checks of the rational constants. e=2 is handled by the empty comparison spaces and the inherited divisibility, so no zero-factor strict-inequality issue arises.
