# A45 general criterion and actual conductor-39 strictness: separate review

Date: 2026-11-21. Reader: GPT-6 Astra Pro, `/root/row_audit`; effort not exposed.

## Complete manuscripts checked

- `work/effective_galois/nonconstant_deck/A45_NONCONSTANT_DECK.tex`, SHA256 `1419e0bc37ca0e768fb2528bfa10fb15426271cc7bf5576f982c09fd13270118`: **entire revised statement and proof read, PASS**.
- `work/row_audit/NONCONSTANT_PRIMITIVE_DESCENT.tex`, SHA256 `73b9c93683a781567d599211caefa482506ad02acd4a3c531ddfcec67be28a2d`: **entire generalized source read, PASS**, separately recorded in `CHECK_EVENTS_A45_DESCENT.tsv`.
- `work/effective_galois/nonconstant_deck/A45_STRICT_39.tex`, SHA256 `d42478a98d77c8e8cbfc08cf16c3da1fb9dbde19d9a552d730d050890f979cca`: **entire statement, three-step proof and finite-computation scope read, PASS**.
- Combined `A45_COMPLETE.tex`, SHA256 `e6577cdf1bfb85815c9996d7b55f74112f5aeb95eb7b2ba0c3a238a032394d42`: exact component comparison confirms that it consists of the first manuscript, the descent source through SD.11, and the strictness manuscript, with only one unmatched newline. This is an assembly check, not another claimed whole-proof reading.

These are targeted proof checks, not a formal verification or an independently authored re-proof.

## Revised all-characteristic, all-genus criterion

The original-field p-primary projection belongs to the actual connected norm kernel. A geometric deck difference has the rational Prym exponent as annihilator even if the difference itself is not rational. Exact order gives a separable function with two zero and two pole supports and multiplicity a power of p.

The controlled-field argument, divisibility of its index by twice that p-power, and the odd cover degree prime to p make the induced cyclic action faithful and free. The genus estimate forces the auxiliary quotient and its cyclic quotient to have genus one.

I checked the strengthened fibre argument completely. If the two positive supports share a fibre, their indices both equal half the degree. Deck equivariance forces the same indices at both pole supports, which must then share their fibre as well. The two fibre equalities contradict freeness of the square of the odd deck generator. Therefore the two positive fibres are singleton totally ramified fibres. Their common index divides the zero multiplicity and is a nontrivial power of p. The two disjoint free deck orbits contribute at least twice the cover degree times that index to the different, giving `p <= e <= g-1`.

The field-compositum argument is valid: the subgroup fixing the compositum is exactly the kernel of the faithful deck action on the small field. Hence the original curve has a separable degree-e elliptic quotient, and the auxiliary cover is the étale base change of that quotient. Total ramification descends through this étale base change at both prescribed points. This proves the unconditional range `2 <= g <= p` and the stated exact higher-genus obstruction.

## Independent finite arithmetic for the strict example

I wrote and executed `work/row_audit/verify_A45_conductor39_cantor.py`, SHA256 `31d5dffe21731f0cafcd40eac31334494d017055cb095363c4793705c13dd2cc`. Its output is `verify_A45_conductor39_cantor.json`, SHA256 `911ee355c093503f616f321ac0ca4b5399caf6259f37d1a46774251ab94d6de9`.

This uses the retained extended-GCD Cantor implementation in `verify_A36_conductor5_cantor.py`; it does not import the effective agent's binary-linear interpolation implementation or its point-image data. It is a separate arithmetic implementation from the producer, adapted from already retained Cantor code rather than newly invented Jacobian arithmetic. The mathematical divisor-class bridge for that Cantor arithmetic is retained with A32.

The checker freshly enumerates all 256 points over the binary field with modulus 0x11b and u=188, projects every point class by 7280 and 5040, reconstructs both complete generator cycles, verifies the original and twisted four-power Frobenius actions, and retains every original/twisted point and both full projected Mumford representatives. It independently checks the Frobenius permutation and quotient action on every point. Both generators, every one of the 256 labels, and all count tables agree with the linear producer. The twist's four rational points and conductor-three labels are also checked directly.

The integer cyclotomic arithmetic is separately implemented by exact polynomial division. Binary extended Euclid gives the displayed conductor-39 Bezout identity and proves that its character value is two times a unit. The checker also verifies the conductor-thirteen unit and the two conductor-three scalar values, 6 and 240. The current certificate stores all point images, both cycles, field encoding, source hashes, cyclotomic polynomials and Bezout coefficients.

## Strictness proof

The Frobenius-stable quotient of the finite Lang kernel defines an actual isogeny over F4. The full Abel-map fundamental-group result supplies geometric connectedness after pullback, and zero supplies the rational point above infinity. The quotient Frobenius has exact order four, so the minimal deck field is F256. The explicit twist of the order-nine representative also checks: its constant coordinate is 188, as stated.

The conductor-three cover is already constant over F4. Its labels over F256 restrict correctly because extending constants multiplies the rational Frobenius label by four, which is one modulo three. The inert integral module argument gives exact exponents 2 and 16 from the two scalar character values. The conductor-thirteen factor has odd rational order over F256 and contributes no rational two-primary torsion over either field.

For conductor 39, the exact character value is two times a unit in the full finite étale cyclotomic algebra, so the rational group order has two-adic valuation 24. The reduced coefficient is one on each of the 24 distinct one-dimensional coherent character lines; the cited Deligne/Katz comparison therefore makes that entire ordinary factor's geometric two-torsion rational. It already has order 2^24, so the entire rational two-primary group is elementary and has exponent 2. This argument uses the actual canonical factor and does not replace it by an uncontrolled isogenous representative. Primitive semilinear descent gives the same exponent over F4.

The proper conductor-three factor grows under the larger full deck field, exactly the possibility left open by the descent lemma. The whole actual Prym consequently has exponents 2 and 16. The inequalities 39>9 and 39<=961 give a strict improvement for this one pointed cover. The whole factor is ordinary of dimension 38, with primitive factor already having nonzero rational two-primary torsion; no assertion is made that other covers fail or that an ordinary factor has no geometric torsion.

## Scope of source checks

The exact Poonen controlled-field and Stacks module-descent passages were directly checked earlier in this run, with their scope recorded in the existing A45 audit. The present full manuscript review also uses the already retained and checked A32 Deligne/Katz comparison and BE.8 integral module argument. No new complete reading of every external proof is claimed here. The finite computation is exact but is not formal verification.

## Final computation-provenance addition

The combined source subsequently became SHA256 `1e930f85e1658b909ec1a44723535c7383dad39405b6812209543bec737e11c5`. I read its complete added final paragraph: it accurately describes the separate retained Cantor implementation, fresh enumeration and two projections, all 256 labels, both cycles, every-point Frobenius permutation, four original-field points, and the two cyclotomic unit identities. It correctly treats the other reader's unchanged rerun as a rerun rather than a third implementation. The mathematical text is unchanged. This narrow provenance check is PASS and is not another whole-proof reading.
