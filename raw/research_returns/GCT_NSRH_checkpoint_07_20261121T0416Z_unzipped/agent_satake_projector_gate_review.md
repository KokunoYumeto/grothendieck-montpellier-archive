# Fresh complete review of the signed-orbit projector gate (F23)

Reviewer: /root/grothendieck_dictionary, GPT-6 Astra Pro, effort not exposed. Date: 21 November 2026. Review type: independent full mathematical check plus targeted primary-source verification.

Reviewed artifact: `agent_satake_projector_gate.md`.

SHA256: `1081646a7e66c55145def984da59a6b5224e0abe126d6d9ae1a5f0d46753564b`.

## Result: PASS

Read all SPG1–SPG8, every proof, the conditional counting-complexity paragraph, source locators, and limitations. The four nested inline-math delimiters reported during review were corrected before recording this hash; no mathematical change was needed.

- SPG1: the signed orbit spans are explicitly induced from the stabilizer character; the proposed tensor-induction map is well defined and dimension comparison proves it is an isomorphism.
- SPG2–SPG3: checked the direction of Frobenius reciprocity, stabilizer-character tests, and primitive-versus-central idempotent factor. Characteristic-zero representations of symmetric groups are split over the stated field, so the rank-one primitive-block argument applies.
- SPG4: checked the induced-character product and both Pieri rules; the horizontal/vertical chain inequalities give the claimed counts. The conditional #P claim includes unique orbit encodings, polynomial validity tests and polynomial witness lengths, including binary-encoded dimensions. It does not claim an Ehrhart theorem from these assumptions alone.
- SPG5–SPG6: reread the full two-component GL2 flag-fiber computation, its cohomological degree, and the intermediate-extension exclusion of the other constituent. The standard2D S3 action is faithful and cannot embed in the order8 signed-permutation group. The explicit allowance for arbitrary third-root phases correctly limits the obstruction.
- SPG7–SPG8: checked Hermite reciprocity and the specialized highest-weight vector, whose swap sign is (-1)^r. This yields exactly the even-r summands. The stretched coefficient equals the integer-point count of the rational point {r/2}, with the stated dimension and denominator. The zero odd residue constituent is allowed by VI strict saturation, so its strict saturation index is zero despite failure of ordinary support saturation.

Primary statements directly read from the local originals: Postnikov/Lian Theorem7.10 printedp16; Goodman–Wallach Theorem4.1.18 and its character formula; Donley–Kim Proposition3.1 equation3.4 and Proposition8.1 equation8.2. Also read supplied GCTVI definition labelled `dintrosat` (Definition1.2.4 in the supplied version). These cited standard inputs were checked as statements; their complete general literature proofs were not independently reproved here.

No mathematical blocker found. No existence assertion for a general signed component basis, no general positive rule, and no nonstandard canonical-basis identification is inferred.
