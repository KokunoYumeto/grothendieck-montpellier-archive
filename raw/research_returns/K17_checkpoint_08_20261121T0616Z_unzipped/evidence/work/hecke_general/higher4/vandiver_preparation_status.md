# Higher4 preparation and checked exact support

Date: 2026-11-21 UTC. Checker: `/root/vandiver_k`, GPT-6 Astra Pro. Effort: not exposed. Run: K17.

## Scope

These are finite-model and support calculations. No new arithmetic vanishing is asserted here. The full E−3 unitary replays and the E−7 unitary ring tests remain separate prerequisites.

## Complete readings and executions

I read the complete isolated higher4 discovery wrapper and the complete full level-three GL2 certificate, then reran the latter successfully. Its full dimensions for e=26,28,30 are 16,18,19. Precision260 includes the largest required index13·19=247, and the Hecke coefficient correction remains present.

I read the whole `residual_support_lemma.tex` and reconstructed its proof: a prime dividing both full comparison products divides one pair of factor values, gcd splitting and verified exact-power replacement preserve prime support, and the final repeated gcd division certifies all remaining primes independently of the discovery procedure. This uses no polynomial irreducibility or large-integer primality assertion.

I read the entire final `collect_higher.py` and `verify_residual_support.py`. The latter uses direct power-sum polynomial evaluation, the gcd of the complete U3×GL2 comparison values, exact small-factor product identities, trial division for the small declared primes, and repeated gcd division for the residual support. I executed it successfully for e=26. This check is distinct from the full U3 model replay.

I read the entire new `work/hecke_minus7/higher4/gl2_twist_residual_certificate.py` before executing e=26. Its `calculate` function is AST-identical to the already fully audited higher3 generic implementation. I actually ran both new e=26 cases; both completed successfully.

## e=26 exact results

The E−3 orbit source and target dimensions are 613 and529; harmonic dimension84, with swap dimensions44 and40. The full classical dimension is16.

The combined comparison gcd is

`2^450 * 3^456 * 5^42 * 11^8 * 79^2 * 3461 * 16759 * M1 * M2^3`,

where

- `M1 = 697446897311`;
- `M2 = 1346178024590512195284390892511906772585800385915601`.

The collector and independent direct-gcd replay verify this exactly, including the support recursion. No primality assertion is made for M1 or M2.

The full101-dimensional Γ1(7) classical all-twists determinant has residues

- `564487428902` modulo M1;
- `540110375711722242001383842413974682809788702229075` modulo M2.

Both residues have gcd one with their moduli. All101 determinant pivots were units; the full triangular integral cusp basis and all109 checked Hecke coefficients are recorded in `work/hecke_minus7/higher4/gl2_e26_residual_certificate.json`.

The unchanged independent full E−3 U3 replay completed successfully. Its report data hash is `e9983ef4e49a20d08e00b291d1345d5530851197b88edd5107638a414d20a119`. The separately run optimized verifier, which deletes only zero harmonic terms and clears denominators in the same exact Faddeev recurrence, also completed successfully and produced a byte-identical report (SHA256 `d68b88a445f2c3726ce84aee3465c290a03e184b2eed8f521d71c010642c2515`). The sparse-only control is retained separately. Tripod owns the E−7 U3 producers and full independent replays. These statuses do not yet assert K52=0.

## Recovery and ownership

The watcher observed the expected old k29 Python integer-string serialization failure, preserved its log as `k29_serialization_limit_failure.log`, and restarted the corrected isolated wrapper. Root owns the other discovery processes. The watcher launches one full unchanged U3 verifier per completed degree with `PYTHONINTMAXSTRDIGITS=0`; no frozen earlier files were changed.


## e=28 exact results and current numerical gate

The full discovery is complete, with source815, target710, harmonic105, swap55/50 and classicaldimension18. The exact combined gcd is

`2^487 * 3^566 * 5^12 * 19^4 * 23^3 * 29 * 53 * 15083 * M1 * M2^3`,

where `M1=323026426255399` and `M2=1850161514202910077636429426241454885347275557889859421603`. The separate complete-value support replay has passed.

Both complete109-dimensional level-seven GL2 tests have also passed: determinant residues `291047394117369` modulo M1 and `1361695747498278489585646473526121447210917280902628497429` modulo M2, gcd one in both cases. The complete four-row numerical proposition is `work/hecke_minus7/higher4/gl2_residual_ring_section.tex`, which I have read in full. Its model scope is explicit.

The unchanged full E−3 U3 replay for e=28 is still running. The original three-degree monitor had already enqueued it before the optimization control finished; no second e=28 replay was launched. The full E−7 U3 replays are separately owned by tripod.

## Generic-ring code audit for the new U3 cases

I read the entire higher4 `verify_ring_schur.py`, its full diff against higher3, the new process runner and copy manifest. The only verifier change replaces the three old hardcoded dimension triples by equality with the independently enumerated full source and target orbit counts and their difference. All direct kernel, identity-minor, input-agreement, frame, evaluation and determinant checks remain. The preparation and fast C++ files are byte-identical to the previously fully audited versions. I independently checked gcd one with both `336*(2k+1)!` and the exact comparison value E for all four current moduli. This is a complete code/lemma audit; it does not claim completion of the pending numerical U3 replays.
