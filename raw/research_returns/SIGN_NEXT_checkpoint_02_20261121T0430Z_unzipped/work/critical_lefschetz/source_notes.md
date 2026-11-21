# Main-critical source and proof notes

Author: GPT-6 Astra Pro, child `/root/critical_lefschetz`; effort setting not exposed.
Run: SIGN_NEXT. Date: 21 November 2026.

## Finished findings

- **SN-C01:** The usable left-hand condition is historical C, modern B. This is a mathematical and textual reconstruction, corroborated by CSG L11d p.3 and L10d p.2. The overtyped manuscript character itself remains palaeographically ambiguous.
- **SN-C02:** Reading the even critical A-double-prime as ordinary Gysin from degree d-2 to degree d makes the equivalence false. X=P1 gives a geometric counterexample; X an elliptic curve gives the same failure in the abelian class.
- **SN-C03:** The corrected critical weak condition uses L_T composed with Gysin from degree d-2 to degree d+2. Paired with algebraicity detection under restriction, it is exactly A(T)^0. Its difference from ordinary upper critical Gysin is exactly A(W)^0 on the hyperplane W. Full proof in contribution.tex.
- **SN-C04:** Combine SN-C03 with Kleiman 1968 Theorem 2.13(i),(ii-prime) to obtain a valid corrected scan050 proposition and the hyperplane-flag criterion. This does not silently claim that the original definition included the extra L.
- **SN-C05:** Explicit Lefschetz-module countermodel refutes the bare diagram inference R_0+G_0=>A_0. It is not a geometric counterexample to any standard conjecture.

## Exact primary locators

1. Grothendieck, cote 16, scan 050 (= official PDF p.50, folio49), final proposition and its preceding weak definitions; scan040, boxed Lambda_Y = j^* Lambda_X^2 j_*, proves historical C concerns Lefschetz algebraicity; scan049, inverse-correspondence corollary.
2. Grothendieck, letter to Coates dated 6.1.1966 as written, CSG transcription L11d.pdf, printed pp.1-3, especially p.3 Proposition; https://csg.igrothendieck.org/wp-content/uploads/2024/04/L11d.pdf .
3. Grothendieck, preceding archived letter to Coates dated 4.1.1967, CSG L10d.pdf, printed p.2, Proposition (i), (ii), (ii bis), and the flag corollary; https://csg.igrothendieck.org/wp-content/uploads/2024/04/L10d.pdf .
4. S. L. Kleiman, Algebraic cycles and the Weil conjectures, Dix exposes sur la cohomologie des schemas (1968), pp.359-386, Theorem2.13(i),(ii-prime),(iv), pp.372-373; https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf .
5. SGA5, Expose VII, Theorem7.1: the weak Lefschetz input. The upper-degree Gysin isomorphism is its Poincare-dual form.

## Source comparison

The official image scan050 was downloaded and inspected in full at 2200-pixel height. It confirms the mixed 2i/H^i indexing, the even prescription 2i=n-2, the final even diagram with j^*, j_*, then L_X, and a typed C(Y) before the proposition. CSG L11d reads C(X) in that latter sentence, so it is not a wholly reliable correction to all local readings. No wholesale replacement of the supplied transcription is justified.

The left-hand C reading agrees with the published theorem and with the preceding archived letter. The ordinary-Gysin critical prescription cannot simply be applied literally: SN-C02 is decisive at i=0 and does not depend on resolving H^i versus H^(2i).

## Approaches tried

1. Reconstruct the classical square criterion directly using c=(L_1+L_2)^(-2)((L_1+L_2)Delta). An explicit lowering operator can be recovered from c and C(Y), with boundary coefficients 1 for odd strings and d/(d+1) for even strings. This is sound but was not integrated because Kleiman2.13 already supplies the needed criterion and the user asks that known results be cited, not reproved. The approach is recorded here for continuity; no additional result from it is used.
2. Apply the weak hypotheses to Kleiman's class mu=(L_1+L_2)^2 Lambda_X. This does not eliminate the inverse-on-W issue: mu already has a high-degree Gysin preimage coming from an algebraic middle class, while obtaining its lower-degree preimage is the missing step. No result is claimed from this attack.
3. Shift ordinary Gysin to the high critical degree. The dimension-consistent diagram is g L_W r, and SN-C03 identifies the dropped factor precisely. SN-C05 shows why the diagram alone does not repair it.
4. Use the final even diagram to define the corrected weighted Gysin. This yields the fully proved replacement SN-C03--04.

## Checks

The author reread the entire contribution after writing it, checking every map degree, every use of an isomorphism, both directions of SN-C03, the reduction to Kleiman in SN-C04, and all four module identities in SN-C05. Exact small-matrix and ring computations were also run; see verify_critical.py and verify_critical.out. These are targeted checks and computations, not independent re-proofs or a formal proof certificate.

## Scope

No proof of I(X) or semisimplicity is asserted in this contribution. Those are root-owned tasks. No unknown geometric standard conjecture has been refuted. The new geometric refutation applies to the specified literal reading of the weak critical condition. The corrected proposition is complete; the alternative high-degree ordinary-Gysin conjecture is not silently asserted.
