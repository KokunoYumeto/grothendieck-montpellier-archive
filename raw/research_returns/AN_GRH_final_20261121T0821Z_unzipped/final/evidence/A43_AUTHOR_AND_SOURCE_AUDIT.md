# A43 author and primary-source audit

2026-11-21. GPT-6 Astra Pro; effort not exposed; AN_GRH /root/row_audit.

## Checked versions and outcome

Author complete proof check: PASS at first complete source SHA256 138dafa7345291012ee09f08fa7cc0a7c44725918e2648a7310600fe0dd209c5. The final addition and clarifications were then checked in full at SHA256 05110bc39e79b1f9858f69792bc524da70f2adb75da07a685037bad299967fdb. The latter adds the second Weierstrass fibre with its complete orbit/distinctness/vertical-avoidance argument; clarifies proper intersection by Gamma numerically 2Theta; makes the final orbit steps explicit by the dihedral relation; and updates the statement and layout. These are author checks, not independent re-proofs or formal verification.

## Exact mathematical scope

For at least95 smooth non-Weierstrass parameters in the existing A13/F128 inverse family, the source has two-rank one. Both source Weierstrass points are rational and split, and every lift and reflection image in each of their two fibres is non-Weierstrass on E(F128), with canonical class of exact order4159. Thus the sufficient A29 canonical detector fails for both Weierstrass points, every lift, and every reflection of this fixed degree-five cover, after all subsequent constant extensions. Changing the cover remains open. No assertion of a section collision or failed geometric theta witness is made.

The proof uses the actual Raynaud theta characteristic, preserved by the Frobenius and order-three automorphism. Changing the theta characteristic leaves the residual family unchanged. The special identity u=T−pi is integral, unitary, and satisfies u squared+u+1=0. The normalized double-point curve VTheta has exactly three transverse branches at0 and no other identifications. The forced nonzero tangency has exact local intersection length2 because the inverse image of TTheta is a smooth reduced graph there and its restriction is curve Frobenius. Total intersection6 leaves one further simple nonzero point, giving exactly two reflection ramification points. Deuring–Shafarevich and the field-defined Jacobian isogeny give ranks5 and1.

Both five-point orbit patterns were checked as identities in the commuting endomorphisms with T squared+T=1, u squared+u+1=0 and pi=T−u. Inverse pi is used only on geometric points, and equals pi to the sixth power on F128 points. The nonzero theta condition and #J(F128)=4·4159 rule out the exceptional coincidences exactly as written. No cancellation of multiplication by2 on arbitrary points is used. The complete argument concerns an explicit algebraic family and an existence/counting result; an individually selected parameter and covering equation were not enumerated.

## Primary sources actually checked

- Milne, Jacobian Varieties, Theorem12.1(a),(b), pp.38–39: the full Torelli statement was reopened/read. The complete displayed uniqueness proof in (b) and complete descent proof of Corollary12.2 were read. The full existence proof of Torelli in §13 was not reread or claimed independently reproved.
- Crew, Etale p-covers in characteristic p, Compositio Mathematica52 (1984), Corollary1.8, printedpp35–36: opened the primary PDF, read the statement and complete short excision proof, and requested page images for the formula. The general underlying compactly-supported cohomology theorem was not independently reproved. Primary URL https://numdam.org/item/CM_1984__52_1_31_0.pdf ; retrieval turn176967448view0 and page images turn474337121view0/1. Parent also retained the same primary PDF at work/sources/Crew1984.pdf.
- Milne, Abelian Varieties, Corollary6.6, Lemma8.3 and Theorem17.3: the exact pullback/projection and Rosati trace identities used here were already reopened and their relevant displayed proofs read during A40–A41 checks. No new proof-count event is attributed to those earlier readings.
- A33's A13 integral-RM supplement, A35's actual Raynaud theta/two-torsion intersection, A38's F128 orders and point counts, and A40–A41 were used with their already completed exact-version proof reviews. Their roles are stated in the A43 proof.

## Review coordination

Root and /root/effective_galois both reported whole-proof PASS at138dafa... and complete final-addition PASS at05110bc.... Their own audit files/events are separate. Effective also authored an independent coefficient-only ring verifier; this author audit does not claim authorship or execution of that verifier.
