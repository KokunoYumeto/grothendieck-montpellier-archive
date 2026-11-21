# Scope of the general-target inverse-family probe

Date: 2026-11-21. Author/reviewer: GPT-6 Astra Pro, `/root/row_audit`; effort not exposed.

## Result

No positive universal prescribed-point reduction follows from the tested combination of A40, A42 and the special identities in A43. The exact missing implication is a **cover-selection theorem for a fixed source and its prescribed point**. This record does not assert that such a theorem is false.

The short complete proof in `A43_GENERAL_TARGET_SUPPLEMENT.tex` establishes an actual limitation of the special automorphism mechanism. A37(2) with `S={3}` supplies finite-field ordinary integral Rosati-O5 curves whose Raynaud theta has no nonzero geometric 3-primary point. A geometric order-three curve automorphism inducing `u²+u+1=0` would force a fixed point by tame Riemann–Hurwitz. Functoriality of the actual Raynaud line bundle would then put a nonzero exact-order-three class on theta. Thus some targets have no such automorphism even after constants. This is a consequence of an existing avoidance theorem, not a new main-gate result or a numerical example.

## Where the general calculation stops

For the A13 target, the extra integral relation `pi+V=2T+1` over F2 turns `u=T-pi` into a polarized automorphism of order three. It splits the critical condition into two graphs and gives the Frobenius identities that force the exact double intersection in A43. A general Rosati-O5 action supplies `T²+T=1` and commutation with the field Frobenius, but it does not supply the special trace relation. The complete supplement proves that replacing this omission by a universal automorphism assertion would be false.

The rank formula itself remains valid for any smooth inverse construction with ordinary target: if a reflection map has `r` geometric ramification points, Deuring–Shafarevich gives `f_D=3+r`, and the checked isogeny `J_D ~ J_E² x J_C` gives `f_C=r-1`. Thus a rank-one source requires precisely two such points. The special local intersection argument proves that condition in A43. No assertion that the same condition holds for every target, or that the general inverse family has a particular generic source rank, has been established here.

## Two independent direction and quantifier issues

1. **Varying the inverse parameter does not keep the original source fixed.** A40 fixes a reflection target `E` and constructs sources `C_t`. The original point-section problem fixes `(C,P)`. For a fixed geometric genus-two source there are only finitely many cyclic quintic covers: nonzero classes of `J_C[5]` number `5^4-1=624` with a chosen character, and division by the four choices of generator gives `156` underlying cyclic covers. This is the usual torsion-cover correspondence, also stated in Ozman–Pries §2.1–2.2 (arXiv1502.05959v3 pp3–4). Constants can define and point these covers but do not create additional geometric quintic covering classes. Therefore choosing an arbitrary inverse-family parameter is not a valid operation on a fixed source.

2. **The transfer arrows cannot simply be reversed.** In A33 and A40, `D -> C` is the admissible etale odd cover. A collision on `C` can be lifted through that cover, then pushed through the two degree-two reflection maps `D -> E`. Starting from a collision on an arbitrary `E` gives no corresponding lifting theorem through these ramified degree-two maps. They are not admissible etale odd neighbourhoods. Hence realizing `E` as a reflection quotient is not, by itself, a reverse reduction of its point-section problem to the constructed `C_t`.

A42 gives a dense set of canonical-good points on each fixed target after controlled finite extensions. Density does not place one of the finitely many images of a prescribed lifted source point in that set. A43 provides a checked fixed-cover obstruction even after allowing either source Weierstrass point and every lift and reflection. The choices of another quintic cover, of higher odd degree, or of a geometric primitive-zero construction remain separate possible routes.

## Precise remaining sufficient assertion

For every residual prescribed point `(C,P)`, one would need to choose an allowable odd cover whose common lifted collision either has geometric primitive rank zero, has sufficiently bounded rational Prym exponent, or maps by a suitable reflection construction to a point with a nonzero canonical component at an odd prime `r` satisfying even `ord_r(2)`. The current inverse-family existence and dense-point results establish neither that selection assertion nor its negation.

## Review scope

Read the complete A42 proof at SHA256 `4674c99fa0944da6928d469aaca6e128571f259603b791e294ec3bacba628d87`; its separate review is retained. A43 is retained at SHA256 `05110bc39e79b1f9858f69792bc524da70f2adb75da07a685037bad299967fdb`. The A37 statement and the relevant full proof steps were inspected at source SHA256 `68f88b13eb8057d92ee3ec186596a19b7e6dc193c233075129131efb85c88c20`; this note is not an additional claimed independent re-proof of A37. A40/A33 are used with their existing complete-proof review records. No new computational search was run for this probe.
