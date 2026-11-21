# A36 proof and arithmetic audit

Date: 2026-11-21. Author/reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

## Status and exact scope

**Author whole-proof read: PASS.** Current source is `A36_REFLECTION_NO_FIVE.tex`, SHA256 `0ba06d3c9f2ee2cfa017511ca9c27c662b1c764cfcff92fcf8768a65f0479573`.

The root investigator supplied the actual conductor-five quotient and matching linear-interpolation occupancies. Row_audit supplied a separate extended-GCD Cantor calculation. This agent wrote the complete reflection and correspondence-constant proof, read the entire independent Cantor checker, reran an unchanged copy, and read the full resulting proof from disk. The final source clarifies that the actual Raynaud line lives on the Frobenius twist, splits two long displays, and adds existing source citations.

The claim is deliberately limited: original F256-rational canonical classes and the two fixed correspondence constants have no five-primary part, persistently under constant extension. It does not concern canonical classes of new points over larger fields and does not exclude a useful three-primary component. It supplies an actual counterexample to the forced-five shortcut, not to A29 or section injectivity.

## Whole proof check

1. A27's elliptic factor recurrences give fourth power sums 17 and −16, hence 256 points and Jacobian order 65520. Its five-primary subgroup has order five. The displayed nonzero generator has exact order five, and scalar projection by 13104 therefore gives a surjective quotient. Complete point projection gives occupancies 76,45,45,45,45.
2. The pointed Lang construction is geometrically connected by the Abel fundamental-group surjectivity used in A12 and has a split fibre over the chosen Weierstrass point. Every faithful character has exact coefficient 31, since the four nontrivial fifth roots sum to −1. The canonical top coefficient is 256. Thus the new factor has polynomial `(1+31T+256T^2)^4`, and the degree-four reduction modulo two proves geometric ordinarity, using the comparison already checked in A32.
3. The unique reflection fixing the rational split lift is preserved by Galois, hence defined over F256. Both maps used in the A33 Prym-square isogeny are defined over this field. Therefore the quotient Jacobian polynomial is exactly `(1+31T+256T^2)^2`, with order 288 squared. Ordinary genus two and the integral Rosati-invariant real multiplication follow from the already whole-checked A33 proof.
4. On the full Picard group, define `T2=v_* sigma^2 v^*`. The pullback–norm identity gives `T^2=T2+2`. The divisor `R+T(R)+T2(R)` is a fibre of the degree-five quotient map, including the branch-fibre multiplicities 1,2,2. This proves `(T^2+T−1)L=deg(L) F` without dividing by two or losing possible two-torsion. This exact Picard-degree identity is stronger than the relation restricted to degree zero.
5. For the Raynaud line B on the twist, write `a=T(B)−2B` and `b0=F−5B`. Direct substitution gives `b0=(T+3)a`; multiplication by `2−T` gives `5a`, because `(2−T)(T+3)=5` on the Jacobian. Both factors are invertible on every primary group away from five. In the actual example both constants lie in the rational Jacobian group of order 2^10*3^4, so their five-primary components vanish. This does not assume an unproved geometric constraint on B.

## Exact certificate read and rerun

Read the entire 238-line independent source `work/row_audit/verify_A36_conductor5_cantor.py`, SHA256 `e8a90caf30608422df566d6ccf9203a3f2dd72d1ad15bf156b183bb54ef00688`.

The checker constructs F256, checks every nonzero inverse, preserves `V^2+HV+f=0 mod U` in generalized characteristic-two Cantor composition and reduction, enumerates all points, retains their scalar projections, and checks the exact five-cycle. It derives the character coefficient and the reflection polynomial using integer arithmetic. Its arithmetic is separate from the root investigator's binary-linear interpolation.

An unchanged copy and its executed output are retained under `A36_review_rerun/`. The result is byte-identical to the author's JSON, SHA256 `4504d5214dce26b8afcc69396ad42d7f04eb5c94ee53ac8128e3a34dff04cec7`. The complete five-cycle and all 256 point images are present. This agent does not claim a third independent divisor implementation or formal verification.

The root investigator's initial matching probe was read at `work/root/A27_quintic_reflection_probe.json`. Subsequently the entire retained linear producer `work/root/verify_A36_quintic_linear.py`, SHA256 `0c8c269abbcbd40f28b93d2b660c81ef5d19f8043599f7a81d9f03617a862614`, was read. Its divisor arithmetic is the separately whole-checked A32 binary interpolation, now projecting by 13104. Its complete output, SHA256 `ce2910cec3a96126ae2ecda86110d023e8bc00ec20810808ac8f6ee82dc9d9ea`, was compared with the Cantor result: all 256 point images, all five subgroup elements, the occupancies and the character coefficients are exactly identical. The comparison record is `A36_review_rerun/compare_full_point_images.json`. The linear producer was not rerun by this reviewer; the independent Cantor implementation was rerun as stated above.

## Independent proof reading

Row_audit reported an independent whole-proof PASS at the initial source hash `8a2eaf4530b124b6b8316427ecc0198cf1d227de992b666fc3b4a6ff0255027c`, specifically checking the full Picard-degree identity and ramified-fibre multiplicities as well as the arithmetic-to-reflection deduction. The subsequent source delta only clarifies the Raynaud twist, formats the displays, and adds citations. Root's review and any further delta check are recorded by their authors; they are not conflated with this author's own proof read.

Root independently reported a whole-proof PASS at the initial `8a2eaf...` source, including all arithmetic/reflection/Picard-degree arguments. That is a separate investigator review, not this author's own check.

Effective_galois subsequently reported an independent whole-proof PASS on the complete current A36 source `0ba06d3c9f2ee2cfa017511ca9c27c662b1c764cfcff92fcf8768a65f0479573`, including the exact-field reflection, Picard-degree identity, and constants. Its own arithmetic-source review is a separate event; no supplied-checker rerun is described as a new implementation.
